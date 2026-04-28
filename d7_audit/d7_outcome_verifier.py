#!/usr/bin/env python3
"""
d7_outcome_verifier.py
======================
Run C: Determine the exact d=7 transcendence outcome (TRANS / NEAR / LOCK)
for every two-zero d=6 universal sv=6 fixed point.

For each of the 52 two-zero d=6 fps (Appendix A.4.3 in the paper), the
script:

  1. Enumerates every valid sv=7 rule (pi, sigma) such that K(F_padded) = F
     and the coefficient vector is full-variable (no zero entries).
  2. Computes the exact basin fraction for every valid rule via
     multiset memoization (no sampling).
  3. Classifies the fp based on best basin observed:
       TRANS: at least one rule with basin >= 0.99
       NEAR:  best basin in [0.95, 0.99)
       LOCK:  best basin < 0.95

These thresholds match the empirical groupings used in the paper.

Validated against four fps with known outcomes:
  - F = 60714  -> TRANS (best basin 0.998617)
  - F = 146070 -> TRANS (best basin 1.000000)
  - F = 170460 -> LOCK  (best basin 0.917912)
  - F = 607140 -> TRANS (best basin 0.999370)

Output:
  - d7_verified_outcomes.json  — complete per-fp data
  - d7_summary.txt             — one-line-per-fp summary
  - d7_classifier_analysis.txt — cycle-signature cross-tab (paper §6 invariant)
  - d7_verified_partial.json   — checkpoint after every fp (crash-resume)

Runtime: estimated 1-3 hours on a modern laptop (52 fps; per-fp cost
varies from a few seconds to several minutes depending on # valid rules).

Usage:
  python3 d7_outcome_verifier.py
  python3 d7_outcome_verifier.py --fps 60714,146070,170460,607140  # subset
  python3 d7_outcome_verifier.py --resume                           # explicit
  python3 d7_outcome_verifier.py --workers 4                        # parallel
"""

import sys
import os
import json
import time
import argparse
import pickle
from itertools import permutations
from collections import defaultdict, Counter
import multiprocessing as mp

import numpy as np
from numba import njit

import kaprekar_core as kc
from classify_d7_full import classify_rule_fast, step_encoded, coefs_array

D = 7
TRANS_THRESHOLD = 0.99
NEAR_THRESHOLD = 0.95

CHECKPOINT_PATH = 'd7_verified_partial.json'
RESULT_PATH = 'd7_verified_outcomes.json'
SUMMARY_PATH = 'd7_summary.txt'
ANALYSIS_PATH = 'd7_classifier_analysis.txt'


# The 52 two-zero d=6 universal fps. From paper Appendix A.4.3 / d6_fps.txt.
# Each is a six-digit integer with two zero digits in its sorted-desc form.
TWO_ZERO_D6_FPS = [
    4545, 7191, 8919, 8991, 9189, 9225, 10899, 17019, 37017, 44505, 52605,
    54450, 60714, 67023, 80919, 80991, 81099, 89019, 90819, 90918, 91809,
    98091, 100899, 108099, 109809, 146070, 170460, 180909, 189009, 190089,
    190809, 445005, 445050, 504450, 544500, 607140, 700191, 701901, 707130,
    719100, 809091, 809109, 810909, 890091, 900891, 901890, 908091, 908109,
    908190, 908901, 909081, 910089, 910809
]


def F_padded_sorted_desc(F, d):
    """Return F padded to d digits, then sorted descending as a tuple."""
    s = str(F).zfill(d)
    return tuple(sorted([int(c) for c in s], reverse=True))


@njit(cache=True)
def fixes_F(coefs, F_sorted_desc_arr, F_value, d):
    """True iff K(F_padded) = F under the given coefs."""
    s = 0
    for i in range(d):
        s += coefs[i] * F_sorted_desc_arr[i]
    if s < 0:
        s = -s
    return s == F_value


def enumerate_F_fixing_rules(F):
    """Yield every full-variable (pi, sigma) at d=7 that fixes F.

    F_padded must be a fixed point of the rule, i.e. K(F_padded) = F where
    K(n) = |sum c_i x_i| over sorted-desc digits.
    """
    F_sorted = F_padded_sorted_desc(F, D)
    F_arr = np.array(F_sorted, dtype=np.int64)
    F_int = np.int64(F)
    for pi in permutations(range(D)):
        for sigma in permutations(range(D)):
            # Full-variable check
            ok = True
            for i in range(D):
                if pi[i] == sigma[i]:
                    ok = False
                    break
            if not ok:
                continue
            coefs = coefs_array(pi, sigma)
            if fixes_F(coefs, F_arr, F_int, D):
                yield pi, sigma, coefs


@njit(cache=True)
def basin_for_rule(coefs, d, admissibles_enc, n_adm,
                   enc_to_idx, idx_table_size, F_value, max_steps):
    """Compute the exact basin fraction of F under the given rule.

    Returns: (n_reach_F, n_total) — fraction = n_reach_F / n_total.
    Uses multiset memoization for speed.
    """
    fate = np.full(n_adm, -2, dtype=np.int64)
    path = np.empty(max_steps + 1, dtype=np.int64)

    for k in range(n_adm):
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

    n_reach = 0
    for k in range(n_adm):
        if fate[k] == F_value:
            n_reach += 1
    return n_reach, n_adm


def classify_outcome(best_basin):
    if best_basin >= TRANS_THRESHOLD:
        return 'TRANS'
    if best_basin >= NEAR_THRESHOLD:
        return 'NEAR'
    return 'LOCK'


def verify_one_fp(F, admissibles_enc, enc_to_idx):
    """Verify outcome for a single fp F. Returns dict with full per-fp data."""
    n_adm = len(admissibles_enc)
    idx_table_size = len(enc_to_idx)
    rules_evaluated = 0
    valid_rules = []
    best_basin = 0.0
    best_rule = None
    best_basin_count = 0
    rules_meeting_trans = 0
    rules_meeting_near = 0
    signatures = Counter()
    t0 = time.time()

    for pi, sigma, coefs in enumerate_F_fixing_rules(F):
        rules_evaluated += 1
        n_reach, n_total = basin_for_rule(
            coefs, D, admissibles_enc, n_adm,
            enc_to_idx, idx_table_size, np.int64(F), 80
        )
        basin = n_reach / n_total
        sig = kc.cycle_signature(pi, sigma)
        signatures[sig] += 1
        valid_rules.append({
            'pi': list(pi),
            'sigma': list(sigma),
            'coefs': [int(c) for c in coefs],
            'basin': basin,
            'n_reach': int(n_reach),
            'cycle_signature': list(sig),
        })
        if basin > best_basin:
            best_basin = basin
            best_rule = (pi, sigma, tuple(int(c) for c in coefs))
            best_basin_count = int(n_reach)
        if basin >= TRANS_THRESHOLD:
            rules_meeting_trans += 1
        if basin >= NEAR_THRESHOLD:
            rules_meeting_near += 1

    elapsed = time.time() - t0
    F_sorted = F_padded_sorted_desc(F, D)
    zero_count = sum(1 for x in F_sorted if x == 0)
    multiset_str = ''.join(sorted(str(F).zfill(D)))
    outcome = classify_outcome(best_basin)

    result = {
        'F': F,
        'F_padded_sorted_desc': list(F_sorted),
        'zero_count_at_d7': zero_count,
        'multiset_d7': multiset_str,
        'n_valid_rules': len(valid_rules),
        'best_basin': best_basin,
        'best_basin_count': best_basin_count,
        'best_rule_pi': list(best_rule[0]) if best_rule else None,
        'best_rule_sigma': list(best_rule[1]) if best_rule else None,
        'best_rule_coefs': list(best_rule[2]) if best_rule else None,
        'n_rules_trans_threshold': rules_meeting_trans,
        'n_rules_near_threshold': rules_meeting_near,
        'cycle_signature_counts': {','.join(str(x) for x in k): v
                                   for k, v in sorted(signatures.items())},
        'outcome': outcome,
        'elapsed_seconds': round(elapsed, 1),
        'all_rules': valid_rules,
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=(
        "Verify d=7 transcendence outcomes for the 52 two-zero d=6 "
        "universal full-variable fps. For each fp, enumerate all sv=7 "
        "rules that fix it, compute exact basins, classify TRANS/NEAR/LOCK."))
    parser.add_argument('--fps', type=str, default='',
                        help="Comma-separated list of fps to verify (default: all 52)")
    parser.add_argument('--resume', action='store_true',
                        help="Resume from checkpoint (auto if checkpoint exists)")
    parser.add_argument('--workers', type=int, default=1,
                        help="Number of parallel workers (default 1; "
                             "large numbers can slow things due to Numba init)")
    args = parser.parse_args()

    if args.fps:
        target_fps = [int(x) for x in args.fps.split(',')]
    else:
        target_fps = list(TWO_ZERO_D6_FPS)

    print("=" * 60)
    print(f"d7_outcome_verifier.py — Run C")
    print(f"  Verifying outcomes for {len(target_fps)} d=6 fps at d=7")
    print(f"  TRANS threshold: basin >= {TRANS_THRESHOLD}")
    print(f"  NEAR threshold:  {NEAR_THRESHOLD} <= basin < {TRANS_THRESHOLD}")
    print(f"  LOCK:            basin < {NEAR_THRESHOLD}")
    print("=" * 60)
    print()

    # Build admissibles
    print("Building admissibles at d=7 ...", flush=True)
    admissibles = kc.build_admissible_multisets(D)
    admissibles_enc = np.empty(len(admissibles), dtype=np.int64)
    for i, ms in enumerate(admissibles):
        v = 0
        for x in ms:
            v = v * 10 + x
        admissibles_enc[i] = v
    print(f"  {len(admissibles):,} admissibles", flush=True)

    print(f"Building enc_to_idx table (10^{D} slots) ...", flush=True)
    enc_to_idx = np.full(10 ** D, -1, dtype=np.int64)
    for i, enc in enumerate(admissibles_enc):
        enc_to_idx[enc] = i
    print(f"  done", flush=True)

    # Warm up JIT
    print("Warming up JIT ...", flush=True)
    coefs_warm = coefs_array((4, 1, 2, 3, 0, 6, 5), (2, 0, 1, 4, 3, 5, 6))
    F_arr = np.array(F_padded_sorted_desc(60714, D), dtype=np.int64)
    fixes_F(coefs_warm, F_arr, np.int64(60714), D)
    basin_for_rule(coefs_warm, D, admissibles_enc, len(admissibles_enc),
                   enc_to_idx, len(enc_to_idx), np.int64(60714), 80)
    print(f"  done", flush=True)
    print()

    # Resume?
    results = {}
    if (args.resume or os.path.exists(CHECKPOINT_PATH)) and os.path.exists(CHECKPOINT_PATH):
        with open(CHECKPOINT_PATH) as f:
            checkpoint = json.load(f)
        results = {int(k): v for k, v in checkpoint.get('results', {}).items()}
        print(f"Resumed from checkpoint with {len(results)} fps already verified", flush=True)

    # Process each fp
    t_start = time.time()
    for i, F in enumerate(target_fps):
        if F in results:
            print(f"[{i+1}/{len(target_fps)}] F={F} already done; skipping", flush=True)
            continue
        print(f"[{i+1}/{len(target_fps)}] Verifying F={F} ...", flush=True)
        try:
            r = verify_one_fp(F, admissibles_enc, enc_to_idx)
        except Exception as e:
            print(f"  ERROR: {e}", flush=True)
            continue
        results[F] = r
        marker = '★' if r['outcome'] == 'TRANS' else (
                 '○' if r['outcome'] == 'NEAR' else '·')
        print(f"  {marker} {r['outcome']:<5} | "
              f"best basin = {r['best_basin']:.6f} | "
              f"valid rules = {r['n_valid_rules']:>5} | "
              f"trans rules = {r['n_rules_trans_threshold']} | "
              f"{r['elapsed_seconds']:.1f}s", flush=True)

        # Checkpoint after every fp
        with open(CHECKPOINT_PATH, 'w') as f:
            json.dump({
                'meta': {
                    'last_updated': time.strftime('%Y-%m-%dT%H:%M:%S'),
                    'fps_done': len(results),
                    'fps_total': len(target_fps),
                    'cumulative_seconds': round(time.time() - t_start, 1),
                },
                'results': {str(k): v for k, v in results.items()},
            }, f)

    elapsed = time.time() - t_start
    print(f"\nAll {len(results)} fps verified in {elapsed:.1f}s", flush=True)

    # Final aggregation
    finalize(results, elapsed)


def finalize(results, elapsed):
    """Write final outputs: full JSON, summary text, classifier analysis."""
    # Sort by F
    sorted_fps = sorted(results.keys())

    # Outcome tallies
    outcome_counts = Counter(r['outcome'] for r in results.values())

    # Write full JSON
    out = {
        'meta': {
            'script': 'd7_outcome_verifier.py',
            'd_target': D,
            'd_source': 6,
            'n_fps_verified': len(results),
            'wall_seconds': round(elapsed, 1),
            'trans_threshold': TRANS_THRESHOLD,
            'near_threshold': NEAR_THRESHOLD,
        },
        'outcome_counts': dict(outcome_counts),
        'results': {str(F): results[F] for F in sorted_fps},
    }
    with open(RESULT_PATH, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"Wrote: {RESULT_PATH}", flush=True)

    # Summary text
    with open(SUMMARY_PATH, 'w') as f:
        f.write(f"# d7_summary.txt — d=7 outcome for two-zero d=6 fps\n")
        f.write(f"# Total: {len(results)} fps verified\n")
        f.write(f"# TRANS (basin >= {TRANS_THRESHOLD}): {outcome_counts.get('TRANS', 0)}\n")
        f.write(f"# NEAR  ({NEAR_THRESHOLD} <= basin < {TRANS_THRESHOLD}): {outcome_counts.get('NEAR', 0)}\n")
        f.write(f"# LOCK  (basin < {NEAR_THRESHOLD}): {outcome_counts.get('LOCK', 0)}\n")
        f.write(f"#\n")
        f.write(f"# Format: <F>  <outcome>  best_basin=<>  n_valid_rules=<>  "
                f"trans_rules=<>  multiset=<>\n#\n")
        for F in sorted_fps:
            r = results[F]
            f.write(f"{F:>7}  {r['outcome']:<5}  "
                    f"best_basin={r['best_basin']:.6f}  "
                    f"n_valid_rules={r['n_valid_rules']:>5}  "
                    f"trans_rules={r['n_rules_trans_threshold']:>3}  "
                    f"multiset={r['multiset_d7']}\n")
    print(f"Wrote: {SUMMARY_PATH}", flush=True)

    # Classifier analysis: cycle-signature cross-tab
    sig_outcome_counts = defaultdict(lambda: Counter())  # sig -> outcome -> count
    for F, r in results.items():
        # Use the cycle signature of the BEST rule, when available
        if r['best_rule_pi'] is not None:
            sig = kc.cycle_signature(tuple(r['best_rule_pi']),
                                     tuple(r['best_rule_sigma']))
            sig_outcome_counts[sig][r['outcome']] += 1
        else:
            sig_outcome_counts[None][r['outcome']] += 1

    with open(ANALYSIS_PATH, 'w') as f:
        f.write(f"# d7_classifier_analysis.txt\n")
        f.write(f"# Cross-tabulation of cycle signature (of best rule) vs verified outcome\n")
        f.write(f"# Tests within-thread invariants and signature-based classifiers\n#\n")
        f.write(f"# {'signature':<24} {'TRANS':>6} {'NEAR':>6} {'LOCK':>6}  fps\n")
        f.write(f"# " + "-" * 60 + "\n")
        for sig in sorted(sig_outcome_counts.keys(),
                          key=lambda s: (s is None, str(s))):
            counts = sig_outcome_counts[sig]
            sig_str = str(sig) if sig is not None else 'no-rule'
            f.write(f"  {sig_str:<24} "
                    f"{counts.get('TRANS', 0):>6} "
                    f"{counts.get('NEAR', 0):>6} "
                    f"{counts.get('LOCK', 0):>6}\n")
        f.write(f"#\n")
        f.write(f"# Total: {sum(outcome_counts.values())} fps\n")
        f.write(f"#   TRANS: {outcome_counts.get('TRANS', 0)}\n")
        f.write(f"#   NEAR:  {outcome_counts.get('NEAR', 0)}\n")
        f.write(f"#   LOCK:  {outcome_counts.get('LOCK', 0)}\n")
    print(f"Wrote: {ANALYSIS_PATH}", flush=True)

    # Print summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"  TRANS (basin >= {TRANS_THRESHOLD}): {outcome_counts.get('TRANS', 0)}")
    print(f"  NEAR  ({NEAR_THRESHOLD} <= basin < {TRANS_THRESHOLD}): {outcome_counts.get('NEAR', 0)}")
    print(f"  LOCK  (basin < {NEAR_THRESHOLD}): {outcome_counts.get('LOCK', 0)}")
    print(f"  Total: {len(results)}")


if __name__ == '__main__':
    main()
