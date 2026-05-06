#!/usr/bin/env python3
"""
search_multiset_universals_fast.py — Faster variant using random Q sampling.

For d >= 8, the original search_multiset_universals.py becomes prohibitively
slow because it enumerates all (P, Q) pairs per F (O(arrangements^2)). This
version uses random Q sampling per F — fast but probabilistic.

For each F, we sample up to N random Q-arrangements. For each, check if P = Q+F
is also a valid arrangement of the multiset. If yes, recover the rule and test
classical universality.

If even one classical universal is found, the answer is YES. If 0 are found
across many F values with high sample counts, the answer is probably NO.

USAGE:
    python3 search_multiset_universals_fast.py --multiset "8,8,5,5,3,3,2,2,0" --d 9 --out d9_2358_universals.json

    # Smoke test (recovers d=4 {1,4,6,7} thread)
    python3 search_multiset_universals_fast.py --smoke-test
"""
import argparse
import json
import random
import sys
import time
from collections import Counter
from itertools import combinations_with_replacement, permutations
from pathlib import Path


# ============================================================================
# PRIMITIVES
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
    if start_ms in cache:
        return cache[start_ms]
    path = [start_ms]
    path_set = {start_ms}
    current = start_ms
    for step in range(1, max_iters + 1):
        if current != start_ms and current in cache:
            cached = cache[current]
            for p in path: cache[p] = cached
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


def classify_rule(F, c, d, all_multisets, max_iters=300):
    cache = {}
    n_to_F = 0
    n_total = 0
    s_to_F = 0
    s_total = 0
    F_digits_set = set(int(ch) for ch in str(F))
    F_digits_set.add(0)
    S = F_digits_set
    
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
        return 'classical', n_to_F, n_total, s_to_F, s_total
    elif s_to_F == s_total:
        return 's_only', n_to_F, n_total, s_to_F, s_total
    elif n_to_F > 0:
        return 'partial', n_to_F, n_total, s_to_F, s_total
    else:
        return 'broken', n_to_F, n_total, s_to_F, s_total


def recover_inv(n_int, F_digits_desc, d):
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


def find_rules_random(F, multiset_list, d, max_q_samples=200000):
    """Find rules via random Q sampling. Returns list of (pi_inv, sigma_inv)."""
    multiset_sorted_str = ''.join(sorted(str(x) for x in multiset_list))
    F_digits_desc = tuple(sorted(multiset_list, reverse=True))
    rules = []
    seen_keys = set()
    seen_q = set()
    
    for trial in range(max_q_samples):
        digits = list(multiset_list)
        random.shuffle(digits)
        if digits[0] == 0: continue
        Q = digits[0]
        for x in digits[1:]:
            Q = Q * 10 + x
        if Q in seen_q: continue
        seen_q.add(Q)
        
        P = Q + F
        s = str(P).zfill(d)
        if len(s) != d: continue
        if ''.join(sorted(s)) != multiset_sorted_str: continue
        
        pi_inv = recover_inv(P, F_digits_desc, d)
        sigma_inv = recover_inv(Q, F_digits_desc, d)
        if pi_inv is None or sigma_inv is None: continue
        
        c = coefs_from_invs(pi_inv, sigma_inv, d)
        if not is_sv_d(c): continue
        
        key = (pi_inv, sigma_inv)
        if key in seen_keys: continue
        seen_keys.add(key)
        rules.append((pi_inv, sigma_inv))
    return rules


def search_cell_fast(multiset, d, max_iters=300, max_q_samples=100000,
                     time_budget=None, verbose=True, progress_every=200):
    multiset = tuple(sorted(multiset, reverse=True))
    
    # Distinct arrangements of multiset
    arrangements = []
    seen = set()
    for arr in permutations(multiset):
        if arr[0] == 0: continue
        F = int(''.join(str(x) for x in arr))
        if F in seen: continue
        seen.add(F)
        arrangements.append(F)
    
    if verbose:
        print(f"=== Searching multiset {multiset} at d={d} (FAST mode) ===")
        print(f"  Distinct arrangements: {len(arrangements)}")
        print(f"  Pre-computing non-repdigit basin...")
    
    all_multisets = list(all_non_repdigit_multisets(d))
    if verbose:
        print(f"  Basin size: {len(all_multisets):,}")
        print(f"  Random Q samples per F: {max_q_samples}")
        print()
    
    classifications = Counter()
    classical_universals = []
    s_only_universals = []
    n_with_rule = 0
    
    start = time.time()
    
    for i, F in enumerate(arrangements):
        elapsed = time.time() - start
        if time_budget and elapsed > time_budget:
            if verbose:
                print(f"\n  TIME BUDGET EXCEEDED at {i}/{len(arrangements)}")
            break
        
        if verbose and i > 0 and i % progress_every == 0:
            rate = i / elapsed if elapsed > 0 else 0
            eta = (len(arrangements) - i) / rate if rate > 0 else 0
            print(f"  [{int(elapsed):>5}s] {i}/{len(arrangements)} | "
                  f"with-rule: {n_with_rule} | classical: {classifications['CLASSICAL']} | "
                  f"S-only: {classifications['GENUINELY_S_ONLY']} | "
                  f"rate: {rate:.1f}/s | ETA: {int(eta)}s")
        
        rules = find_rules_random(F, list(multiset), d, max_q_samples=max_q_samples)
        if not rules:
            classifications['NO_RULE'] += 1
            continue
        n_with_rule += 1
        
        best_verdict = None
        best_basin = 0
        best_rule = None
        for pi_inv, sigma_inv in rules:
            c = coefs_from_invs(pi_inv, sigma_inv, d)
            verdict, n_to_F, n_total, s_to_F, s_total = classify_rule(F, c, d, all_multisets, max_iters)
            if verdict == 'classical':
                best_verdict = 'classical'; best_basin = n_to_F; best_rule = (pi_inv, sigma_inv); break
            if n_to_F > best_basin:
                best_basin = n_to_F; best_rule = (pi_inv, sigma_inv); best_verdict = verdict
        
        record = {
            'F': F, 'n_rules': len(rules), 'best_basin': best_basin,
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
        print(f"  Arrangements searched: {min(i+1, len(arrangements))}")
        print(f"  With at least one K-rule: {n_with_rule}")
        print(f"  Elapsed: {elapsed:.1f}s")
        print()
        for c, n in classifications.most_common():
            print(f"    {c}: {n}")
    
    return {
        'd': d,
        'multiset': list(multiset),
        'n_arrangements_searched': min(i+1, len(arrangements)),
        'n_with_K_rule': n_with_rule,
        'classifications': dict(classifications),
        'n_classical_universal': classifications['CLASSICAL'],
        'n_genuinely_S_only': classifications['GENUINELY_S_ONLY'],
        'classical_universals': classical_universals,
        's_only_universals': s_only_universals,
        'elapsed_seconds': elapsed,
        'mode': 'fast_random_sampling',
    }


def smoke_test():
    """Confirm fast mode reproduces d=4 {1,4,6,7} thread."""
    print("=== SMOKE TEST: d=4 {1,4,6,7} (fast mode) ===\n")
    random.seed(42)
    result = search_cell_fast((7,6,4,1), 4, max_q_samples=1000, verbose=True)
    n_classical = result['n_classical_universal']
    print(f"\n  Found {n_classical} classical universals (expected: 2)")
    if n_classical != 2:
        print(f"  *** SMOKE TEST FAILED ***")
        return False
    print(f"\n=== SMOKE TEST PASSED ===")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--multiset')
    ap.add_argument('--d', type=int)
    ap.add_argument('--max-iters', type=int, default=300)
    ap.add_argument('--max-q-samples', type=int, default=100000,
                    help='Random Q samples per F (default 100K)')
    ap.add_argument('--time-budget', type=int, help='Max seconds (terminates early)')
    ap.add_argument('--out')
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--smoke-test', action='store_true')
    args = ap.parse_args()
    
    if args.smoke_test:
        return 0 if smoke_test() else 1
    
    if not args.multiset or not args.d:
        ap.error('--multiset and --d required (or use --smoke-test)')
    
    random.seed(args.seed)
    multiset = tuple(int(x) for x in args.multiset.split(','))
    if len(multiset) != args.d:
        ap.error(f'multiset has {len(multiset)} digits but --d={args.d}')
    
    result = search_cell_fast(multiset, args.d, max_iters=args.max_iters,
                              max_q_samples=args.max_q_samples,
                              time_budget=args.time_budget)
    
    if args.out:
        with open(args.out, 'w') as f:
            json.dump(result, f, indent=2, default=str)
        print(f"Wrote: {args.out}")
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(0 if smoke_test() else 1)
    sys.exit(main())
