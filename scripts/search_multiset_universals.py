#!/usr/bin/env python3
"""
search_multiset_universals.py — Search a digit multiset cell for classical
universals.

Given a digit multiset (e.g., (8,8,5,5,3,3,2,2)) and dimension d, this script:
  1. Enumerates all distinct arrangements F of the multiset
  2. For each F, finds all K-rules (pi_inv, sigma_inv) with K(F)=F and sv=d
  3. For each rule, tests classical universality (full non-repdigit basin)
  4. Classifies each F as CLASSICAL, GENUINELY_S_ONLY, or NO_VALID_UNIVERSAL_RULE

Designed for testing whether digit sets OTHER than {1,4,6,7} produce universal
threads parallel to the canonical Kaprekar-pure cycle.

USAGE:
    # Smoke test (re-discovers the d=4 {1,4,6,7} thread)
    python3 search_multiset_universals.py --smoke-test

    # Search d=4 with {2,3,5,8}
    python3 search_multiset_universals.py --multiset "8,5,3,2" --d 4

    # Search d=8 with {8,8,5,5,3,3,2,2} (medium — ~5-15 minutes)
    python3 search_multiset_universals.py --multiset "8,8,5,5,3,3,2,2" --d 8 --out d8_2358_universals.json

    # Search d=12 with {8,8,8,5,5,5,3,3,3,2,2,2} (long — Mac-only, hours)
    python3 search_multiset_universals.py --multiset "8,8,8,5,5,5,3,3,3,2,2,2" --d 12 --out d12_2358_universals.json

OUTPUT JSON STRUCTURE:
    {
      "d": int,
      "multiset": [int, ...],
      "n_arrangements_searched": int,
      "n_with_K_rule": int,
      "n_classical_universal": int,
      "n_genuinely_S_only": int,
      "elapsed_seconds": float,
      "classical_universals": [{F, rule_count, best_basin, ...}],
      "s_only_universals":   [{F, rule_count, best_basin, ...}],
    }
"""
import argparse
import json
import sys
import time
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, permutations
from pathlib import Path


# ============================================================================
# CORE PRIMITIVES (self-contained — no external deps)
# ============================================================================

def all_non_repdigit_multisets(d):
    for combo in combinations_with_replacement(range(9, -1, -1), d):
        if combo[0] == combo[-1]:
            continue
        yield combo


def K_apply(c, ms_desc):
    return abs(sum(c[i] * ms_desc[i] for i in range(len(c))))


def sorted_desc_digits(n, d):
    s = str(n).zfill(d)
    return tuple(sorted((int(ch) for ch in s), reverse=True))


def coefs_from_invs(pi_inv, sigma_inv, d):
    return tuple(10**(d-1-pi_inv[i]) - 10**(d-1-sigma_inv[i]) for i in range(d))


def is_sv_d(c):
    return all(x != 0 for x in c)


def trace_to_terminal(start_ms, c, F, d, max_iters, cache):
    """Cached K-trace; returns (kind, val) where kind in
    {'fp_F', 'fp_other', 'zero', 'cycle', 'maxiter'}."""
    if start_ms in cache:
        return cache[start_ms]
    
    path = [start_ms]
    path_set = {start_ms}
    current = start_ms
    
    for step in range(1, max_iters + 1):
        if current != start_ms and current in cache:
            cached = cache[current]
            for p in path:
                cache[p] = cached
            return cached
        
        n = K_apply(c, current)
        if n == 0:
            for p in path: cache[p] = ('zero', 0)
            return ('zero', 0)
        
        new_ms = sorted_desc_digits(n, d)
        if new_ms == current:
            kind = 'fp_F' if n == F else 'fp_other'
            for p in path: cache[p] = (kind, n)
            return (kind, n)
        if new_ms in path_set:
            for p in path: cache[p] = ('cycle', n)
            return ('cycle', n)
        path.append(new_ms)
        path_set.add(new_ms)
        current = new_ms
    
    final_n = K_apply(c, current)
    for p in path: cache[p] = ('maxiter', final_n)
    return ('maxiter', final_n)


def classify_rule(F, c, d, all_multisets, max_iters=500):
    """Classify (F, rule). Returns (verdict, n_to_F, n_total, s_to_F, s_total)."""
    cache = {}
    n_to_F = 0
    n_total = 0
    s_to_F = 0
    s_total = 0
    # S = the alphabet of F's multiset (extended with 0)
    F_digits = set(int(c) for c in str(F))
    F_digits.add(0)
    S = F_digits
    
    for ms in all_multisets:
        n_total += 1
        is_S = all(x in S for x in ms)
        if is_S:
            s_total += 1
        kind, val = trace_to_terminal(ms, c, F, d, max_iters, cache)
        if kind == 'fp_F':
            n_to_F += 1
            if is_S:
                s_to_F += 1
    
    if n_to_F == n_total:
        return ('classical', n_to_F, n_total, s_to_F, s_total)
    elif s_to_F == s_total:
        return ('s_only', n_to_F, n_total, s_to_F, s_total)
    elif n_to_F > 0:
        return ('partial', n_to_F, n_total, s_to_F, s_total)
    else:
        return ('broken', n_to_F, n_total, s_to_F, s_total)


# ============================================================================
# K-RULE DISCOVERY for a given F
# ============================================================================

def find_all_rules_fixing_F(F, multiset, d, max_pq_pairs=None):
    """Find ALL distinct (pi_inv, sigma_inv) rules with K_{pi,sigma}(F) = F and sv=d.
    
    Uses (P, Q) enumeration: for every pair of arrangements (P, Q) of multiset
    with |P - Q| = F, recover the inverse permutations.
    """
    F_digits_desc = tuple(sorted(multiset, reverse=True))
    multiset_sorted_str = ''.join(sorted(str(x) for x in multiset))
    
    rules = []
    seen = set()
    arrangements = []
    seen_arr = set()
    for arr in permutations(multiset):
        if arr[0] == 0: continue
        n = int(''.join(str(x) for x in arr))
        if n in seen_arr: continue
        seen_arr.add(n)
        arrangements.append(n)
    
    # For every (P, Q) with |P - Q| = F:
    for P in arrangements:
        for Q in arrangements:
            if P == Q: continue
            if abs(P - Q) != F: continue
            
            # Recover pi_inv from P: pi_inv[i] = position of F_digits_desc[i] in P
            pi_inv = recover_inv(P, F_digits_desc, d)
            sigma_inv = recover_inv(Q, F_digits_desc, d)
            if pi_inv is None or sigma_inv is None: continue
            
            c = coefs_from_invs(pi_inv, sigma_inv, d)
            if not is_sv_d(c): continue
            
            key = (pi_inv, sigma_inv)
            if key in seen: continue
            seen.add(key)
            rules.append((pi_inv, sigma_inv))
            
            if max_pq_pairs and len(rules) >= max_pq_pairs:
                return rules
    
    return rules


def recover_inv(n_int, F_digits_desc, d):
    """Recover the inverse permutation that maps F_digits_desc[i] to position 
    of that digit in n_int's string representation."""
    s = str(n_int).zfill(d)
    if len(s) != d: return None
    used = [False]*d
    inv = [None]*d
    for i in range(d):
        target = str(F_digits_desc[i])
        for j in range(d):
            if not used[j] and s[j] == target:
                inv[i] = j; used[j] = True; break
        if inv[i] is None: return None
    return tuple(inv)


# ============================================================================
# MAIN SEARCH
# ============================================================================

def search_cell(multiset, d, max_iters=500, max_pq_pairs=None, verbose=True, progress_every=100):
    """Search every distinct arrangement of multiset at dimension d.
    
    For each arrangement F, finds all K-rules and classifies as CLASSICAL or 
    GENUINELY_S_ONLY. Returns full report dict.
    """
    multiset = tuple(sorted(multiset, reverse=True))
    
    # Enumerate distinct arrangements
    arrangements = []
    seen = set()
    for arr in permutations(multiset):
        if arr[0] == 0: continue
        F = int(''.join(str(x) for x in arr))
        if F in seen: continue
        seen.add(F)
        arrangements.append(F)
    
    if verbose:
        print(f"=== Searching multiset {multiset} at d={d} ===")
        print(f"  Distinct arrangements: {len(arrangements)}")
    
    # Pre-compute the basin
    if verbose:
        print(f"  Pre-computing all non-repdigit d={d} multisets...")
    all_multisets = list(all_non_repdigit_multisets(d))
    if verbose:
        print(f"  Basin size: {len(all_multisets):,}")
        print()
    
    classifications = Counter()
    classical_universals = []
    s_only_universals = []
    n_with_rule = 0
    
    start = time.time()
    
    for i, F in enumerate(arrangements):
        elapsed = time.time() - start
        if verbose and i > 0 and i % progress_every == 0:
            rate = i / elapsed if elapsed > 0 else 0
            eta = (len(arrangements) - i) / rate if rate > 0 else 0
            print(f"  [{int(elapsed):>4}s] {i}/{len(arrangements)} | "
                  f"with-rule: {n_with_rule} | "
                  f"classical: {classifications['CLASSICAL']} | "
                  f"S-only: {classifications['GENUINELY_S_ONLY']} | "
                  f"rate: {rate:.1f}/s | ETA: {int(eta)}s")
        
        # Find all rules
        rules = find_all_rules_fixing_F(F, multiset, d, max_pq_pairs=max_pq_pairs)
        if not rules:
            classifications['NO_RULE'] += 1
            continue
        n_with_rule += 1
        
        # Try every rule until classical found, else best-effort
        best_verdict = None
        best_basin = 0
        best_rule = None
        rule_results = []
        
        for r_idx, (pi_inv, sigma_inv) in enumerate(rules):
            c = coefs_from_invs(pi_inv, sigma_inv, d)
            verdict, n_to_F, n_total, s_to_F, s_total = classify_rule(F, c, d, all_multisets, max_iters)
            rule_results.append({
                'rule_idx': r_idx,
                'verdict': verdict,
                'n_to_F': n_to_F,
                'n_total': n_total,
                's_to_F': s_to_F,
                's_total': s_total,
            })
            if verdict == 'classical':
                best_verdict = 'classical'
                best_basin = n_to_F
                best_rule = (pi_inv, sigma_inv)
                break
            elif n_to_F > best_basin:
                best_basin = n_to_F
                best_verdict = verdict
                best_rule = (pi_inv, sigma_inv)
        
        # Final classification
        record = {
            'F': F,
            'n_rules': len(rules),
            'best_basin': best_basin,
            'best_rule_pi_inv': list(best_rule[0]) if best_rule else None,
            'best_rule_sigma_inv': list(best_rule[1]) if best_rule else None,
        }
        
        if best_verdict == 'classical':
            classifications['CLASSICAL'] += 1
            classical_universals.append(record)
        elif best_verdict == 's_only':
            classifications['GENUINELY_S_ONLY'] += 1
            s_only_universals.append(record)
        elif best_verdict == 'partial':
            classifications['PARTIAL'] += 1
        else:
            classifications['BROKEN'] += 1
    
    elapsed = time.time() - start
    
    if verbose:
        print()
        print("=" * 60)
        print(f"=== SUMMARY: multiset {multiset} at d={d} ===")
        print(f"  Arrangements searched: {len(arrangements)}")
        print(f"  With at least one K-rule: {n_with_rule}")
        print(f"  Elapsed: {elapsed:.1f}s")
        print()
        for c, n in classifications.most_common():
            print(f"    {c}: {n}")
        print()
    
    return {
        'd': d,
        'multiset': list(multiset),
        'n_arrangements_searched': len(arrangements),
        'n_with_K_rule': n_with_rule,
        'classifications': dict(classifications),
        'n_classical_universal': classifications['CLASSICAL'],
        'n_genuinely_S_only': classifications['GENUINELY_S_ONLY'],
        'classical_universals': classical_universals,
        's_only_universals': s_only_universals,
        'elapsed_seconds': elapsed,
    }


# ============================================================================
# SMOKE TEST
# ============================================================================

def smoke_test():
    print("=== SMOKE TEST: d=4 {7,6,4,1} should produce 2 classical universals ===\n")
    result = search_cell((7,6,4,1), 4, verbose=True)
    
    if result['n_classical_universal'] != 2:
        print(f"\n*** SMOKE TEST FAILED: expected 2 classical, got {result['n_classical_universal']} ***")
        return False
    
    Fs = sorted(r['F'] for r in result['classical_universals'])
    if Fs != [1746, 6174]:
        print(f"\n*** SMOKE TEST FAILED: expected [1746, 6174], got {Fs} ***")
        return False
    
    print(f"\n=== SMOKE TEST PASSED: found 6174, 1746 ===\n")
    
    # Also: confirm {2,3,5,8} parallel finding
    print("=== Verifying d=4 {8,5,3,2} parallel ===\n")
    result2 = search_cell((8,5,3,2), 4, verbose=True)
    Fs2 = sorted(r['F'] for r in result2['classical_universals'])
    print(f"Classical universals at d=4 {{8,5,3,2}}: {Fs2}")
    
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--multiset', help='Comma-separated digits (descending), e.g. "8,8,5,5,3,3,2,2"')
    ap.add_argument('--d', type=int, help='Dimension')
    ap.add_argument('--max-iters', type=int, default=500, help='Max iters per K-trace')
    ap.add_argument('--max-pq-pairs', type=int, help='Cap rules per F (default: all)')
    ap.add_argument('--out', help='Save result JSON')
    ap.add_argument('--smoke-test', action='store_true')
    ap.add_argument('--quiet', action='store_true')
    args = ap.parse_args()
    
    if args.smoke_test:
        return 0 if smoke_test() else 1
    
    if not args.multiset or not args.d:
        ap.error('--multiset and --d required (or use --smoke-test)')
    
    multiset = tuple(int(x) for x in args.multiset.split(','))
    if len(multiset) != args.d:
        ap.error(f'--multiset has {len(multiset)} digits but --d={args.d}')
    
    result = search_cell(multiset, args.d, max_iters=args.max_iters,
                         max_pq_pairs=args.max_pq_pairs, verbose=not args.quiet)
    
    if args.out:
        with open(args.out, 'w') as f:
            json.dump(result, f, indent=2, default=str)
        if not args.quiet:
            print(f"Wrote: {args.out}")
    
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(0 if smoke_test() else 1)
    sys.exit(main())
