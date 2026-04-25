"""
audit_6174_d8_d9.py
===================
Exhaustive audit of coefficient-preserving liftings of 6174's classical rule
at d=8 (216 liftings) and d=9 (5,280 liftings).

Verifies the following claims from Theorem 6.1 and Appendix E:
    d=8: 0 strict-universal, 15 NEAR (basin >= 0.99), best basin 0.998141,
         45 escape multisets of form (X,X,X,X,Y,Y,Y,Y) with X > Y >= 0.
    d=9: 0 strict-universal, 302 NEAR, best basin 0.999073, same 45-escape structure.

Runtime:
    d=8: approximately 2-3 minutes
    d=9: approximately 60 minutes

Usage:
    python3 audit_6174_d8_d9.py 8
    python3 audit_6174_d8_d9.py 9
"""

import sys
import time
from itertools import permutations, combinations_with_replacement
from collections import Counter


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


def orbit_reaches(ms_desc, coefs, d, target, budget=60):
    cur = ms_desc
    seen = set()
    for _ in range(budget):
        if cur in seen:
            return False
        seen.add(cur)
        val = abs(sum(c * x for c, x in zip(coefs, cur)))
        if val == target:
            return True
        nxt = tuple(sorted((int(c) for c in str(val).zfill(d)), reverse=True))
        if nxt == cur:
            return False
        cur = nxt
    return False


def audit(d):
    assert d in (8, 9), "This script audits d=8 and d=9 specifically"
    
    F = 6174
    # 6174's sorted-desc at d >= 4 is (7, 6, 4, 1, 0, ..., 0) with (d-4) trailing zeros
    F_sorted = tuple([7, 6, 4, 1] + [0] * (d - 4))
    
    # 6174's native rule at d=4: pi=(3,2,1,0), sigma=(0,1,2,3)
    # Coefficient-preserving lifting: preserve c_0..c_3 at 60714's nonzero-digit positions.
    # So pi_0=3, pi_1=2, pi_2=1, pi_3=0 (forced). Free to assign pi_4..pi_{d-1}.
    # Similarly sigma_0..sigma_3 are forced.
    native_pi = [3, 2, 1, 0]
    native_sigma = [0, 1, 2, 3]
    
    # Free exponents for positions 4..d-1: {4, 5, ..., d-1}
    exp_set = list(range(4, d))
    
    print(f"Building admissible multisets at d={d}...", flush=True)
    admissible = build_admissible_multisets(d)
    print(f"  {len(admissible)} admissible multisets", flush=True)
    
    print(f"Auditing all coefficient-preserving sv={d} liftings...", flush=True)
    t0 = time.time()
    
    strict_count = 0
    near_count = 0
    best_basin = 0
    best_rule = None
    best_escapes = None
    all_basins = []
    
    lift_count = 0
    for pi_tail in permutations(exp_set):
        for sigma_tail in permutations(exp_set):
            # Derangement check on the tail
            if any(pi_tail[i] == sigma_tail[i] for i in range(len(exp_set))):
                continue
            lift_count += 1
            
            pi = tuple(native_pi) + pi_tail
            sigma = tuple(native_sigma) + sigma_tail
            coefs = tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(d))
            
            # Verify K(F) = F
            if abs(sum(c * x for c, x in zip(coefs, F_sorted))) != F:
                continue  # not actually a fixing rule
            
            # Compute basin
            escapes = []
            reached = 0
            for ms in admissible:
                if orbit_reaches(ms, coefs, d, F):
                    reached += 1
                else:
                    escapes.append(ms)
            basin = reached / len(admissible)
            all_basins.append(basin)
            
            if basin == 1.0:
                strict_count += 1
            elif basin >= 0.99:
                near_count += 1
            
            if basin > best_basin:
                best_basin = basin
                best_rule = (pi, sigma, coefs)
                best_escapes = escapes
    
    elapsed = time.time() - t0
    
    print(f"\n{'='*50}")
    print(f"d={d} audit complete in {elapsed:.0f}s")
    print(f"{'='*50}")
    print(f"Total coefficient-preserving liftings: {lift_count}")
    print(f"Rules satisfying K(F)=F: {len(all_basins)}")
    print(f"  Strict-universal (basin=1.0): {strict_count}")
    print(f"  NEAR (basin >= 0.99):         {near_count}")
    print(f"  Best basin:                   {best_basin:.6f}")
    
    if best_rule:
        print(f"\nBest lifting:")
        print(f"  pi    = {best_rule[0]}")
        print(f"  sigma = {best_rule[1]}")
        print(f"  coefs = {best_rule[2]}")
    
    if best_escapes:
        print(f"\nEscape multisets from best lifting ({len(best_escapes)}):")
        # Characterize escape shape
        shapes = Counter()
        for e in best_escapes:
            shape = tuple(sorted(Counter(e).values(), reverse=True))
            shapes[shape] += 1
        print(f"  Shape distribution (sorted digit-count multiplicities):")
        for shape, count in sorted(shapes.items(), key=lambda x: -x[1]):
            print(f"    {shape}: {count}")
        if len(best_escapes) <= 50:
            print(f"  All {len(best_escapes)} escapes:")
            for e in best_escapes:
                print(f"    {e}")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description=("Exhaustive audit of 6174's coefficient-preserving liftings at d=8 or d=9. "
                     "Reproduces Theorem 6.1 / Appendix E claims: 0 strict-universal liftings, "
                     "15 NEAR at d=8 (best basin 0.998141), 302 NEAR at d=9 (best basin 0.999073), "
                     "all with 45-input (X,X,X,X,Y,Y,Y,Y) escape class."))
    parser.add_argument('d', type=int, choices=[8, 9],
                        help="Digit length to audit (8 or 9)")
    args = parser.parse_args()
    audit(args.d)
