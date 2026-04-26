"""
cross_check_d5_to_d6.py
=======================
Verifies Theorem 4.1: among the 33 universal full-variable fixed points at d=5,
exactly one (60714) is also a universal full-variable fp at d=6.

For each of the 33 fixed points at d=5, this script:
  1. Enumerates all sv=6 full-variable rules fixing F (padded to 6 digits).
  2. Tests each such rule for universality at d=6.
  3. Classifies each fp as:
     - ALGEBRAIC OBSTRUCTION: no sv=6 rule fixes F
     - DYNAMIC OBSTRUCTION: sv=6 rules fix F but none is universal
     - UNIVERSAL LIFTING: at least one sv=6 rule is strict-universal

Expected output (per paper):
    ALGEBRAIC: 17 fixed points
    DYNAMIC:   15 fixed points
    UNIVERSAL: 1 fp (60714)

Runtime: approximately 30 minutes on commodity hardware.

Usage:
    python3 cross_check_d5_to_d6.py
"""

import sys
import json
import time
from itertools import permutations, combinations_with_replacement
from collections import defaultdict, Counter


# The 33 universal fixed points at d=5 (from Theorem 3.3 / Appendix A.3)
D5_UNIVERSAL_FPS = [
    54, 3753, 12456, 14562, 15642, 16524, 16578, 16758, 17685, 18342,
    21456, 21834, 24156, 24183, 24561, 28539, 37584, 37854, 38754, 41562,
    41832, 42183, 43758, 43785, 43875, 45612, 45621, 53928, 58239, 60417,
    60714, 65781, 67581
]


def build_admissible_multisets(d):
    multisets = []
    for ms in combinations_with_replacement(range(10), d):
        ms_desc = tuple(sorted(ms, reverse=True))
        cnt = Counter(ms_desc)
        if len(cnt) == 1:
            continue
        if max(cnt.values()) >= d - 1:
            continue
        multisets.append(ms_desc)
    return multisets


def iterate_to_fp(ms_desc, coefs, d, budget=80):
    cur = ms_desc
    seen = set()
    for _ in range(budget):
        if cur in seen:
            return None
        seen.add(cur)
        val = abs(sum(c * x for c, x in zip(coefs, cur)))
        nxt = tuple(sorted((int(c) for c in str(val).zfill(d)), reverse=True))
        if nxt == cur:
            return val
        cur = nxt
    return None


def check_fp_at_d6(F, admissible_d6):
    """For fp F native at d=5, check all sv=6 rules fixing F at d=6 for universality."""
    F_sorted_d6 = tuple(sorted((int(c) for c in str(F).zfill(6)), reverse=True))
    d = 6
    
    # Step 1: enumerate sv=6 rules with K(F) = F
    fixing_rules = []
    for pi in permutations(range(d)):
        for sigma in permutations(range(d)):
            if any(pi[i] == sigma[i] for i in range(d)):
                continue
            coefs = tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(d))
            if abs(sum(c * x for c, x in zip(coefs, F_sorted_d6))) == F:
                fixing_rules.append((pi, sigma, coefs))
    
    n_algebraic = len(fixing_rules)
    
    if n_algebraic == 0:
        return ('ALGEBRAIC', 0, 0.0, None)
    
    # Step 2: test each fixing rule for universality
    best_basin = 0.0
    best_rule = None
    for pi, sigma, coefs in fixing_rules:
        reached = 0
        for ms in admissible_d6:
            r = iterate_to_fp(ms, coefs, d, budget=60)
            if r == F:
                reached += 1
        basin = reached / len(admissible_d6)
        if basin > best_basin:
            best_basin = basin
            best_rule = (pi, sigma, coefs)
        if basin == 1.0:
            break  # found strict universal; no need to test further
    
    if best_basin == 1.0:
        return ('UNIVERSAL', n_algebraic, 1.0, best_rule)
    else:
        return ('DYNAMIC', n_algebraic, best_basin, best_rule)


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description=("Cross-dimensional check (Theorem 4.1): for each of the 33 universal "
                     "full-variable fixed points at d=5, test whether F admits a universal "
                     "full-variable rule at d=6. Expected result: 17 algebraically obstructed, "
                     "15 dynamically obstructed, 1 universal (60714). Runtime ~30 minutes."))
    parser.add_argument('--save', action='store_true', default=True,
                        help="Write cross_check_d5_d6.json (default true)")
    args = parser.parse_args()

    print("Building d=6 admissible multisets...", flush=True)
    admissible_d6 = build_admissible_multisets(6)
    print(f"  {len(admissible_d6)} admissible multisets at d=6", flush=True)
    
    results = {}
    t_start = time.time()
    
    for i, F in enumerate(D5_UNIVERSAL_FPS):
        t0 = time.time()
        status, n_algebraic, best_basin, best_rule = check_fp_at_d6(F, admissible_d6)
        elapsed = time.time() - t0
        results[F] = {
            'status': status,
            'n_fixing_rules': n_algebraic,
            'best_basin': best_basin,
            'best_rule_pi': list(best_rule[0]) if best_rule else None,
            'best_rule_sigma': list(best_rule[1]) if best_rule else None,
            'best_rule_coefs': list(best_rule[2]) if best_rule else None,
        }
        print(f"[{i+1}/33] F={F}: {status}, n_fixing={n_algebraic}, best_basin={best_basin:.4f}, {elapsed:.0f}s", flush=True)
    
    total_elapsed = time.time() - t_start
    
    # Summary
    counts = Counter(r['status'] for r in results.values())
    print(f"\n==========================================")
    print(f"THEOREM 4.1 VERIFICATION COMPLETE in {total_elapsed:.0f}s")
    print(f"==========================================")
    print(f"  ALGEBRAIC OBSTRUCTION: {counts['ALGEBRAIC']} fixed points (expected 17)")
    print(f"  DYNAMIC OBSTRUCTION:   {counts['DYNAMIC']} fixed points (expected 15)")
    print(f"  UNIVERSAL LIFTING:     {counts['UNIVERSAL']} fixed points (expected 1: 60714)")
    
    # The UNIVERSAL case
    universal = [F for F, r in results.items() if r['status'] == 'UNIVERSAL']
    print(f"\n  UNIVERSAL fp(s): {universal}")
    
    # Save
    with open('cross_check_d5_d6.json', 'w') as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nSaved to cross_check_d5_d6.json")


if __name__ == '__main__':
    main()
