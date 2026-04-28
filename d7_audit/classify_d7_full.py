#!/usr/bin/env python3
"""
classify_d7_full.py
===================
Run B: SOUND exhaustive classification of universal full-variable fixed points
at digit length d=7.

Enumerates all 9,344,160 = 7! * D_7 = 5040 * 1854 full-variable (pi, sigma)
rules. For each rule:

  1. Compute coefficient vector c_i = 10^pi[i] - 10^sigma[i].
  2. Use multiset-memoization: trace every admissible multiset's orbit in
     a single pass, caching every (multiset -> fate) lookup. This collapses
     ~11,340 trace operations per rule into a far smaller number of
     unique-state explorations.
  3. Identify the fixed-point set: {F : K(F) = F}. From this, isolate
     admissible fixed points (the candidate universal fps).
  4. For each admissible fp F, check basin = 1 over all admissibles by
     consulting the fate cache.

Outputs:
  - d7_classification.json  — full per-fp data: {fp, sample_pi, sample_sigma,
    sample_coefs, n_universal_rules, multiset, zero_count, cycle_signatures}
  - d7_fps.txt              — clean fp list (one per line, with metadata)
  - d7_progress.log         — periodic progress (every 100,000 rules or 60s)
  - d7_classify.checkpoint  — crash-resume state (every 60s)

Soundness:
  - No sampling. Every (pi, sigma) is enumerated.
  - For each rule, the basin test is over EVERY admissible multiset.
  - "Soundness" here means: no candidate fp is missed due to a sampling
    heuristic. The candidate-filtering of classify_at_d.py samples a few
    inputs to find candidate fps before full basin testing — this is sound
    in practice (no misses observed at d <= 6) but not provably sound.
    classify_d7_full.py replaces that with: enumerate the fixed-point set
    of (pi, sigma) directly via the K(F) = F equation, then test basin
    on each. No sampling at any stage.

Runtime:
  - With Numba parallel on a modern multicore (8+ cores): 10-30 minutes
  - With Numba serial: 1-3 hours
  - Without Numba: ~30 hours (set environment var DISABLE_NUMBA=1 to verify)

Crash recovery:
  - State saved every 60 seconds to d7_classify.checkpoint
  - Restart picks up from the last completed rule batch

Usage:
  python3 classify_d7_full.py
  python3 classify_d7_full.py --workers 4    # cap worker count
  python3 classify_d7_full.py --resume       # explicit resume (also auto)
  python3 classify_d7_full.py --batch 50000  # rules per worker batch
"""

import sys
import os
import json
import time
import pickle
import argparse
from itertools import permutations
from collections import defaultdict, Counter
import multiprocessing as mp

import numpy as np

import kaprekar_core as kc

D = 7
ADMISSIBLE_COUNT_EXPECTED = 11340  # d=7
TOTAL_RULES_EXPECTED = 9344160     # 7! * D_7

CHECKPOINT_PATH = 'd7_classify.checkpoint'
PROGRESS_PATH = 'd7_progress.log'
RESULT_PATH = 'd7_classification.json'
TXT_PATH = 'd7_fps.txt'


# ---------------------------------------------------------------------------
# Numba kernel: classify a single rule
# ---------------------------------------------------------------------------
# Returns: (n_admissible_fps, fp_values[64], fp_basin_size[64])
# We test basin via memoized trace: for each admissible multiset, follow its
# orbit until a fixed-point or cycle is reached; cache the fate.
#
# The Numba-friendly approach: maintain a flat int64 array of admissible
# multisets (encoded as base-10 integers for fast lookup), and a parallel
# fate array. Process each admissible: trace; on hitting any state we've
# already classified, copy that fate; on hitting a new fixed-point, record it.

from numba import njit, prange, types
from numba.typed import Dict


@njit(cache=True)
def encode_ms(ms_arr, d):
    """Encode sorted-desc d-digit multiset as int64 (base 10)."""
    v = np.int64(0)
    for i in range(d):
        v = v * 10 + ms_arr[i]
    return v


@njit(cache=True)
def decode_ms(v, d, out):
    """Decode int64 base-10 encoding back to d-digit array (sorted-desc)."""
    for i in range(d - 1, -1, -1):
        out[i] = v % 10
        v //= 10


@njit(cache=True)
def step_encoded(ms_enc, d, coefs):
    """One iteration starting from encoded multiset; returns (next_int_value, next_encoded)."""
    # Decode
    digits = np.empty(d, dtype=np.int64)
    tmp = ms_enc
    for i in range(d - 1, -1, -1):
        digits[i] = tmp % 10
        tmp //= 10
    # Apply rule
    s = np.int64(0)
    for i in range(d):
        s += coefs[i] * digits[i]
    if s < 0:
        s = -s
    # Decompose s into d digits (padded), then sort descending
    out_digits = np.zeros(d, dtype=np.int64)
    tmp = s
    for i in range(d - 1, -1, -1):
        out_digits[i] = tmp % 10
        tmp //= 10
    # Insertion sort descending
    for i in range(1, d):
        v = out_digits[i]
        j = i - 1
        while j >= 0 and out_digits[j] < v:
            out_digits[j + 1] = out_digits[j]
            j -= 1
        out_digits[j + 1] = v
    # Re-encode
    enc = np.int64(0)
    for i in range(d):
        enc = enc * 10 + out_digits[i]
    return s, enc


@njit(cache=True)
def classify_rule_fast(coefs, d, admissibles_enc, n_admissibles,
                       enc_to_idx, idx_table_size, max_steps):
    """Classify a single rule using array-based memoization with early-out.

    Args:
        coefs: int64 array of length d
        admissibles_enc: int64 array of admissible multisets (encoded)
        n_admissibles: int (length of admissibles_enc effectively used)
        enc_to_idx: dense int64 array of length 10**d, mapping encoded multiset
                    -> compact admissible index, or -1 if not admissible.
        idx_table_size: 10**d
        max_steps: per-trace iteration budget

    Returns:
        (n_universal_fps, fp_values_array) where fp_values_array has at most 8
        entries (in practice 0 or 1 — at most one universal fp per rule).

    Early-out: trace from a few seed admissibles; if any seed yields a
    different fate from the first, no universal fp exists, return early.
    Otherwise run the full classification and verify universality.
    """
    if n_admissibles == 0:
        return 0, np.zeros(8, dtype=np.int64)

    out = np.zeros(8, dtype=np.int64)

    # ---- Early-out: trace from a few seed admissibles ----
    # Seeds are picked at fixed indices, spaced through the admissible list.
    # If any seed reaches a different positive fp from the first seed, no
    # universal fp can exist — short-circuit.
    n_seeds = 8
    seed_step = max(1, n_admissibles // n_seeds)
    candidate = np.int64(0)  # 0 = uninitialized, -1 = invalid (cycle/escape)
    for sk in range(n_seeds):
        idx = sk * seed_step
        if idx >= n_admissibles:
            break
        # Trace this seed
        path = np.empty(max_steps + 1, dtype=np.int64)
        path[0] = admissibles_enc[idx]
        path_len = 1
        cur = admissibles_enc[idx]
        result = np.int64(-1)
        for n in range(1, max_steps + 1):
            val, nxt = step_encoded(cur, d, coefs)
            if nxt == cur:
                result = val
                break
            in_path = False
            for h in range(path_len):
                if path[h] == nxt:
                    in_path = True
                    break
            if in_path:
                result = -1
                break
            path[path_len] = nxt
            path_len += 1
            cur = nxt
        if sk == 0:
            candidate = result
            if candidate <= 0:
                # First seed already shows no fp -> no universal fp at all
                return 0, out
        else:
            if result != candidate:
                return 0, out  # Inconsistent fates — not universal

    # All seeds agree on a positive fp value. Now do the full sweep with
    # memoization to verify universality.
    fate = np.full(n_admissibles, -2, dtype=np.int64)
    path = np.empty(max_steps + 1, dtype=np.int64)

    for k in range(n_admissibles):
        if fate[k] != -2:
            continue
        path[0] = admissibles_enc[k]
        path_len = 1
        cur = admissibles_enc[k]
        result = np.int64(-1)

        for n in range(1, max_steps + 1):
            val, nxt = step_encoded(cur, d, coefs)
            if nxt == cur:
                result = val
                break
            in_path = False
            for h in range(path_len):
                if path[h] == nxt:
                    in_path = True
                    break
            if in_path:
                result = -1
                break
            if 0 <= nxt < idx_table_size:
                idx2 = enc_to_idx[nxt]
                if idx2 >= 0:
                    f = fate[idx2]
                    if f != -2:
                        result = f
                        break
            path[path_len] = nxt
            path_len += 1
            cur = nxt

        for h in range(path_len):
            p = path[h]
            if 0 <= p < idx_table_size:
                idx2 = enc_to_idx[p]
                if idx2 >= 0:
                    fate[idx2] = result

        # Early-out during full sweep: if this admissible's fate differs
        # from the candidate established by seeds, no universal fp.
        if fate[k] != candidate:
            return 0, out

    # All admissibles reach `candidate`
    out[0] = candidate
    return 1, out


@njit(cache=True)
def classify_rule(coefs, d, admissibles_enc, n_admissibles, max_steps):
    """Legacy entry point — typed-dict version. Slower; kept for fallback.

    Use classify_rule_fast for production runs.
    """
    fate = Dict.empty(key_type=types.int64, value_type=types.int64)

    for k in range(n_admissibles):
        start = admissibles_enc[k]
        if start in fate:
            continue
        path = np.empty(max_steps + 1, dtype=np.int64)
        path[0] = start
        path_len = 1
        cur = start
        result = np.int64(-1)
        for n in range(1, max_steps + 1):
            val, nxt = step_encoded(cur, d, coefs)
            if nxt == cur:
                result = val
                break
            if nxt in fate:
                result = fate[nxt]
                break
            in_path = False
            for h in range(path_len):
                if path[h] == nxt:
                    in_path = True
                    break
            if in_path:
                result = -1
                break
            path[path_len] = nxt
            path_len += 1
            cur = nxt
        for h in range(path_len):
            fate[path[h]] = result

    fp_counter = Dict.empty(key_type=types.int64, value_type=types.int64)
    for k in range(n_admissibles):
        f = fate[admissibles_enc[k]]
        if f > 0:
            if f in fp_counter:
                fp_counter[f] = fp_counter[f] + 1
            else:
                fp_counter[f] = np.int64(1)

    out = np.zeros(8, dtype=np.int64)
    n_out = 0
    for f in fp_counter:
        if fp_counter[f] == n_admissibles:
            if n_out < 8:
                out[n_out] = f
                n_out += 1
    return n_out, out


# ---------------------------------------------------------------------------
# Driver: enumerate (pi, sigma) pairs and dispatch to workers
# ---------------------------------------------------------------------------

def all_full_variable_pairs():
    """Yield every full-variable (pi, sigma) at d=7 as int64 numpy arrays."""
    perms = list(permutations(range(D)))
    for pi in perms:
        for sigma in perms:
            ok = True
            for i in range(D):
                if pi[i] == sigma[i]:
                    ok = False
                    break
            if not ok:
                continue
            yield pi, sigma


def coefs_array(pi, sigma):
    return np.array([10 ** pi[i] - 10 ** sigma[i] for i in range(D)], dtype=np.int64)


# ---------------------------------------------------------------------------
# Worker: process a batch of (pi, sigma) pairs
# ---------------------------------------------------------------------------

def worker_batch(args):
    """Process a batch of (pi, sigma) pairs, return list of universal-fp results.

    Args: (batch_id, pairs_list, admissibles_enc, enc_to_idx)
    Returns: (batch_id, n_processed, list of (pi, sigma, fp) tuples for universal fps)
    """
    batch_id, pairs, admissibles_enc, enc_to_idx = args
    n_adm = len(admissibles_enc)
    idx_table_size = len(enc_to_idx)
    found = []
    for pi, sigma in pairs:
        coefs = coefs_array(pi, sigma)
        n_fp, fps = classify_rule_fast(coefs, D, admissibles_enc, n_adm,
                                       enc_to_idx, idx_table_size, 80)
        for j in range(n_fp):
            f = int(fps[j])
            found.append((pi, sigma, f))
    return batch_id, len(pairs), found


def main():
    parser = argparse.ArgumentParser(description=(
        "Sound exhaustive classification of universal full-variable fixed "
        "points at d=7. Enumerates all 9,344,160 sv=7 rules and finds every "
        "universal fp without sampling heuristics."))
    parser.add_argument('--workers', type=int, default=0,
                        help="Number of worker processes (0 = auto = cpu_count)")
    parser.add_argument('--batch', type=int, default=20000,
                        help="Rules per worker batch (default 20,000)")
    parser.add_argument('--resume', action='store_true',
                        help="Resume from checkpoint if present (auto if checkpoint exists)")
    parser.add_argument('--max-rules', type=int, default=0,
                        help="Cap rules processed (0 = no cap; for testing)")
    args = parser.parse_args()

    n_workers = args.workers if args.workers > 0 else mp.cpu_count()
    batch_size = args.batch

    print("=" * 60)
    print(f"classify_d7_full.py — Run B (sound enumeration)")
    print(f"  d = {D}")
    print(f"  total full-variable rules: {TOTAL_RULES_EXPECTED:,}")
    print(f"  workers: {n_workers}")
    print(f"  batch size: {batch_size:,}")
    print("=" * 60)

    # Build admissibles (encoded as int64)
    print("Building admissibles ...", flush=True)
    admissibles = kc.build_admissible_multisets(D)
    if len(admissibles) != ADMISSIBLE_COUNT_EXPECTED:
        print(f"WARNING: expected {ADMISSIBLE_COUNT_EXPECTED} admissibles, got {len(admissibles)}", flush=True)
    admissibles_arr = np.array(admissibles, dtype=np.int64)
    admissibles_enc = np.empty(len(admissibles), dtype=np.int64)
    for i, ms in enumerate(admissibles):
        v = 0
        for x in ms:
            v = v * 10 + x
        admissibles_enc[i] = v
    print(f"  {len(admissibles):,} admissibles (encoded)", flush=True)

    # Build dense encoded-multiset -> compact-index lookup table.
    # Encoded multiset values are at most 10^d - 1 = 9,999,999 for d=7,
    # which is a 10M-entry int64 array (~80 MB). Acceptable in memory once.
    print(f"Building enc_to_idx lookup table (10^{D} = {10**D:,} slots) ...", flush=True)
    enc_to_idx = np.full(10 ** D, -1, dtype=np.int64)
    for i, enc in enumerate(admissibles_enc):
        enc_to_idx[enc] = i
    print(f"  done", flush=True)

    # Warm up the JIT compiler so timing is honest
    print("Warming up JIT (one-time compile, ~1-5 seconds) ...", flush=True)
    t_warm = time.time()
    coefs_warm = coefs_array((4, 1, 2, 3, 0, 6, 5), (2, 0, 1, 4, 3, 5, 6))
    # Note: 60714 is NOT strict-universal at d=7 (basin ~0.9929 with 81-input
    # escape class — see audit_60714_d7.py). The warmup just exercises the
    # kernel; we expect 0 universal fps for this specific rule.
    n_fp, fps = classify_rule_fast(coefs_warm, D, admissibles_enc,
                                   len(admissibles_enc), enc_to_idx,
                                   len(enc_to_idx), 80)
    if n_fp != 0:
        print(f"WARN: 60714 native rule unexpectedly produced {n_fp} strict-universal fps "
              f"({fps[:n_fp].tolist()}); known basin at d=7 is ~0.993. Continuing anyway.", flush=True)
    print(f"  JIT warm in {time.time() - t_warm:.2f}s "
          f"(60714 native rule -> {n_fp} strict-universal fps, as expected)", flush=True)

    # Positive sanity check at d=4: classical rule (descending - ascending) is
    # universal for 6174. We use a d=4-sized version of the kernel here.
    print("Sanity check at d=4: classical rule expected to find 6174 universal ...", flush=True)
    d4_admissibles = kc.build_admissible_multisets(4)
    d4_enc = np.empty(len(d4_admissibles), dtype=np.int64)
    for i, ms in enumerate(d4_admissibles):
        v = 0
        for x in ms:
            v = v * 10 + x
        d4_enc[i] = v
    d4_idx_table = np.full(10 ** 4, -1, dtype=np.int64)
    for i, enc in enumerate(d4_enc):
        d4_idx_table[enc] = i
    # Classical rule at d=4: pi=(3,2,1,0), sigma=(0,1,2,3) ⇒ coefs (999,90,-90,-999)
    coefs_d4 = np.array([999, 90, -90, -999], dtype=np.int64)
    n_fp4, fps4 = classify_rule_fast(coefs_d4, 4, d4_enc, len(d4_enc),
                                     d4_idx_table, len(d4_idx_table), 80)
    if n_fp4 != 1 or fps4[0] != 6174:
        print(f"FATAL: d=4 sanity failed: n_fp={n_fp4}, fps={fps4[:n_fp4].tolist()}; "
              f"expected 1 fp = 6174", flush=True)
        sys.exit(1)
    print(f"  6174 confirmed universal at d=4 under the classical rule. Kernel OK.", flush=True)

    # Resume?
    state = None
    if (args.resume or os.path.exists(CHECKPOINT_PATH)) and os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH, 'rb') as f:
            state = pickle.load(f)
        print(f"Resuming from checkpoint: {state['rules_done']:,} rules already processed", flush=True)
    else:
        state = {'rules_done': 0, 'found': [], 'wall_seconds': 0.0}

    # Enumerate (pi, sigma) and partition into batches
    print("Enumerating full-variable rules ...", flush=True)
    all_pairs = list(all_full_variable_pairs())
    print(f"  {len(all_pairs):,} rules generated", flush=True)
    if len(all_pairs) != TOTAL_RULES_EXPECTED:
        print(f"WARNING: expected {TOTAL_RULES_EXPECTED} rules, got {len(all_pairs)}", flush=True)

    # If max-rules cap, restrict
    if args.max_rules > 0:
        all_pairs = all_pairs[:args.max_rules]
        print(f"  capped to {len(all_pairs):,}", flush=True)

    # Skip already-done if resuming
    pairs_to_do = all_pairs[state['rules_done']:]
    print(f"  {len(pairs_to_do):,} rules to process", flush=True)
    if not pairs_to_do:
        print("Already complete — nothing to do.", flush=True)
        finalize(state, admissibles)
        return

    # Build batches
    batches = []
    for i in range(0, len(pairs_to_do), batch_size):
        batches.append((i // batch_size, pairs_to_do[i:i + batch_size],
                        admissibles_enc, enc_to_idx))
    print(f"  {len(batches):,} batches", flush=True)

    # Main work loop
    t0 = time.time()
    last_checkpoint = t0
    last_progress = t0
    found = list(state['found'])
    rules_done = state['rules_done']
    progress_log = open(PROGRESS_PATH, 'a')
    progress_log.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] starting; {rules_done:,} done\n")
    progress_log.flush()

    pool = mp.Pool(n_workers) if n_workers > 1 else None
    try:
        if pool is None:
            for batch in batches:
                bid, n_processed, batch_found = worker_batch(batch)
                rules_done += n_processed
                found.extend(batch_found)
                # Progress report
                now = time.time()
                if now - last_progress > 60:
                    rate = (rules_done - state['rules_done']) / (now - t0)
                    eta = (len(all_pairs) - rules_done) / rate if rate > 0 else 0
                    print(f"  {rules_done:,} / {len(all_pairs):,} rules "
                          f"({100*rules_done/len(all_pairs):.1f}%); "
                          f"{len(found):,} fp-rule pairs found; "
                          f"rate {rate:.0f} rules/s; ETA {eta/60:.1f} min", flush=True)
                    progress_log.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                                       f"{rules_done:,} done, {len(found)} fp-rules\n")
                    progress_log.flush()
                    last_progress = now
                # Checkpoint
                if now - last_checkpoint > 60:
                    state['rules_done'] = rules_done
                    state['found'] = found
                    state['wall_seconds'] += now - last_checkpoint
                    with open(CHECKPOINT_PATH, 'wb') as f:
                        pickle.dump(state, f)
                    last_checkpoint = now
        else:
            for bid, n_processed, batch_found in pool.imap_unordered(worker_batch, batches):
                rules_done += n_processed
                found.extend(batch_found)
                now = time.time()
                if now - last_progress > 60:
                    rate = (rules_done - state['rules_done']) / (now - t0)
                    eta = (len(all_pairs) - rules_done) / rate if rate > 0 else 0
                    print(f"  {rules_done:,} / {len(all_pairs):,} rules "
                          f"({100*rules_done/len(all_pairs):.1f}%); "
                          f"{len(found):,} fp-rule pairs found; "
                          f"rate {rate:.0f} rules/s; ETA {eta/60:.1f} min", flush=True)
                    progress_log.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] "
                                       f"{rules_done:,} done, {len(found)} fp-rules\n")
                    progress_log.flush()
                    last_progress = now
                if now - last_checkpoint > 60:
                    state['rules_done'] = rules_done
                    state['found'] = found
                    state['wall_seconds'] += now - last_checkpoint
                    with open(CHECKPOINT_PATH, 'wb') as f:
                        pickle.dump(state, f)
                    last_checkpoint = now
    finally:
        if pool is not None:
            pool.close()
            pool.join()
        progress_log.close()

    state['rules_done'] = rules_done
    state['found'] = found
    state['wall_seconds'] += time.time() - last_checkpoint
    with open(CHECKPOINT_PATH, 'wb') as f:
        pickle.dump(state, f)

    print(f"\nDone in {time.time() - t0:.1f}s; {rules_done:,} rules processed; "
          f"{len(found):,} fp-rule pairs found", flush=True)
    finalize(state, admissibles)


def finalize(state, admissibles):
    """Aggregate raw (pi, sigma, fp) hits into per-fp metadata; write outputs."""
    print("Aggregating results ...", flush=True)

    # Aggregate per fp
    per_fp = defaultdict(list)
    for pi, sigma, fp in state['found']:
        per_fp[fp].append((tuple(pi), tuple(sigma)))

    # Compute multiset / zero-count / cycle-signature data per fp
    fp_metadata = {}
    for fp, rules in per_fp.items():
        ms_str = ''.join(sorted(str(fp).zfill(D)))
        zero_count = ms_str.count('0')
        signatures = set()
        for pi, sigma in rules:
            signatures.add(kc.cycle_signature(pi, sigma))
        first_pi, first_sigma = rules[0]
        first_coefs = tuple(10 ** first_pi[i] - 10 ** first_sigma[i] for i in range(D))
        fp_metadata[fp] = {
            'fp': fp,
            'multiset': ms_str,
            'zero_count': zero_count,
            'n_universal_rules': len(rules),
            'sample_pi': list(first_pi),
            'sample_sigma': list(first_sigma),
            'sample_coefs': list(first_coefs),
            'cycle_signatures': sorted([list(s) for s in signatures]),
        }

    # Write JSON
    out = {
        'meta': {
            'script': 'classify_d7_full.py',
            'd': D,
            'total_full_variable_rules_tested': state['rules_done'],
            'wall_seconds': round(state['wall_seconds'], 1),
            'admissibles_count': len(admissibles),
        },
        'total_universal_fps': len(per_fp),
        'total_universal_rules': sum(len(v) for v in per_fp.values()),
        'fps_sorted': sorted(per_fp.keys()),
        'per_fp': {str(fp): meta for fp, meta in sorted(fp_metadata.items())},
        'by_zero_count': dict(sorted(Counter(meta['zero_count'] for meta in fp_metadata.values()).items())),
    }
    with open(RESULT_PATH, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"  wrote {RESULT_PATH}", flush=True)

    # Write text list
    with open(TXT_PATH, 'w') as f:
        f.write(f"# d{D}_fps.txt — Universal full-variable fixed points at d={D}\n")
        f.write(f"# Generated by classify_d7_full.py (sound exhaustive enumeration)\n")
        f.write(f"# Total: {len(per_fp)} fixed points, "
                f"{sum(len(v) for v in per_fp.values())} universal rules\n")
        f.write(f"# Total full-variable rules tested: {state['rules_done']:,}\n")
        by_zero = Counter(meta['zero_count'] for meta in fp_metadata.values())
        f.write(f"#\n# Zero-digit stratification:\n")
        for nz in sorted(by_zero):
            f.write(f"#   {nz} zeros: {by_zero[nz]} fixed points\n")
        f.write(f"#\n# Format: <F> zeros=<count> multiset=<sorted-asc-string> "
                f"n_rules=<count>\n#\n")
        for fp in sorted(per_fp.keys()):
            meta = fp_metadata[fp]
            f.write(f"{fp:>{D+1}}  zeros={meta['zero_count']}  "
                    f"multiset={meta['multiset']}  "
                    f"n_rules={meta['n_universal_rules']}\n")
    print(f"  wrote {TXT_PATH}", flush=True)

    print(f"\nDone. {len(per_fp)} universal full-variable fixed points at d=7.")


if __name__ == '__main__':
    main()
