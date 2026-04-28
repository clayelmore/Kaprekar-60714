#!/usr/bin/env python3
"""
Track 1: Validate Type A LOCK predictor on held-out data.

The predictor: F LOCKs at d if no full-variable d-rule that fixes F has a
zero-sum coefficient pair (zsp). We call this "Type A LOCK" or
"algebraic rigidity LOCK".

Verified on Run C training: 4 of 8 LOCKs (17019, 37017, 701901, 707130)
are Type A. 0 of 45 TRANS/NEAR fps are Type A.

Held-out test: apply to 12 fps in Phase 3 Set B (d=6 fps tested at d=7).
Expected: Type A predictor flags some subset of the 6 LOCKs in Set B.

Runtime: ~5-10 minutes total on M5 Pro for the 12 Set B fps.

Usage:
  python3 typeA_validator.py
"""

import json
import time
import sys
from itertools import permutations

try:
    import numpy as np
    from numba import njit
except ImportError:
    print("ERROR: numpy and numba required. Run: pip install numpy numba")
    sys.exit(1)


# Set B held-out: d=6 universal fps tested at d=7
SET_B_FPS = [
    112743, 284679, 477936,  # 0-zero d=6
    11736, 175086, 386064,   # 1-zero d=6
    4545, 89019, 544500,     # 2-zero d=6
    252, 20025, 200025,      # 3-zero d=6
]

# Known outcomes from Phase 3 Set B (computed earlier on the same machine):
EXPECTED_OUTCOMES = {
    112743: 'LOCK', 284679: 'LOCK', 477936: 'ALGEBRAIC_OBSTRUCTION',
    11736: 'LOCK', 175086: 'LOCK', 386064: 'LOCK',
    4545: 'TRANS', 89019: 'TRANS', 544500: 'TRANS',
    252: 'TRANS', 20025: 'TRANS', 200025: 'TRANS',
}


@njit
def has_zero_sum_pair_arr(coefs, d):
    """Does the rule (given by coefs) have any pair i<j with coefs[i] + coefs[j] = 0?"""
    for i in range(d):
        for j in range(i+1, d):
            if coefs[i] + coefs[j] == 0:
                return True
    return False


@njit
def fixes_F_arr(pi_arr, sigma_arr, F_sd_arr, F_int, d):
    s = 0
    for i in range(d):
        s += (10**pi_arr[i] - 10**sigma_arr[i]) * F_sd_arr[i]
    if s < 0:
        s = -s
    return s == F_int


@njit
def is_full_variable(pi_arr, sigma_arr, d):
    for i in range(d):
        if pi_arr[i] == sigma_arr[i]:
            return False
    return True


def zsp_count_for_F(F, d):
    """Count F-fixing full-variable rules at d that have at least one zsp pair.
    Also returns total fixing rule count.
    """
    F_sd = tuple(sorted([int(c) for c in str(F).zfill(d)], reverse=True))
    F_sd_arr = np.array(F_sd, dtype=np.int64)
    F_int = np.int64(F)
    n_zsp = 0
    n_total = 0
    coefs = np.empty(d, dtype=np.int64)
    
    for pi in permutations(range(d)):
        pi_arr = np.array(pi, dtype=np.int64)
        for sigma in permutations(range(d)):
            sigma_arr = np.array(sigma, dtype=np.int64)
            if not is_full_variable(pi_arr, sigma_arr, d):
                continue
            if not fixes_F_arr(pi_arr, sigma_arr, F_sd_arr, F_int, d):
                continue
            for i in range(d):
                coefs[i] = 10**pi[i] - 10**sigma[i]
            n_total += 1
            if has_zero_sum_pair_arr(coefs, d):
                n_zsp += 1
    return n_zsp, n_total


def main():
    print("=" * 70)
    print("Track 1: Type A LOCK validator on held-out Set B")
    print("=" * 70)
    print()
    
    # JIT warmup
    print("JIT warmup ...", flush=True)
    arr = np.array([1, 2, 3], dtype=np.int64)
    fixes_F_arr(arr, arr, arr, np.int64(0), 3)
    has_zero_sum_pair_arr(arr, 3)
    is_full_variable(arr, arr, 3)
    print("warm.\n", flush=True)
    
    print(f"{'F':>7} {'expected':<10} {'zsp_rules':>10} {'total_rules':>12} {'TypeA_pred':<10} {'consistent':<10} {'time':>6}")
    print("-" * 75)
    
    type_a_predictions = 0
    consistent = 0
    inconsistent = []
    
    for F in SET_B_FPS:
        t0 = time.time()
        n_zsp, n_total = zsp_count_for_F(F, 7)
        elapsed = time.time() - t0
        
        # Predict Type A LOCK if zsp_count == 0 AND fixing rules exist
        # If no fixing rules at all (algebraic obstruction), it's not Type A — different category.
        if n_total == 0:
            pred = 'ALG_OBSTR'
        elif n_zsp == 0:
            pred = 'TYPE_A_LOCK'
            type_a_predictions += 1
        else:
            pred = 'NOT_TYPE_A'
        
        expected = EXPECTED_OUTCOMES.get(F, '?')
        
        # Type A LOCK predictor consistent if:
        #   pred == 'TYPE_A_LOCK' AND expected == 'LOCK'  (true positive)
        #   pred == 'NOT_TYPE_A' AND expected != 'LOCK'   (true negative)
        #   pred == 'NOT_TYPE_A' AND expected == 'LOCK'   (TYPE B LOCK — predictor stays silent)
        #   pred == 'ALG_OBSTR' AND expected == 'ALGEBRAIC_OBSTRUCTION'  (correct different category)
        # Inconsistent if pred predicts Type A but actual was TRANS/NEAR.
        if pred == 'TYPE_A_LOCK' and expected != 'LOCK':
            ok = '✗ INCONSIST'
            inconsistent.append(F)
        else:
            ok = '✓'
            consistent += 1
        
        print(f"  {F:>7}  {expected:<10}  {n_zsp:>9}  {n_total:>11}  {pred:<10}  {ok:<10}  {elapsed:>5.1f}s")
    
    print()
    print(f"Total Type A LOCK predictions: {type_a_predictions}")
    print(f"Consistent with expected outcomes: {consistent}/{len(SET_B_FPS)}")
    if inconsistent:
        print(f"INCONSISTENT (Type A predicted, actual was TRANS/NEAR): {inconsistent}")
        print("This would refute the conjecture.")
    else:
        print("Conjecture holds: every Type A prediction matches a LOCK outcome.")
    
    # Save
    output = {
        'set_b_zsp_results': [
            {'F': F, 'expected_outcome': EXPECTED_OUTCOMES[F]}
            for F in SET_B_FPS
        ],
        'type_a_predictions': type_a_predictions,
        'consistent': consistent,
        'inconsistent_fps': inconsistent,
    }
    with open('typeA_validation_results.json', 'w') as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved typeA_validation_results.json")


if __name__ == '__main__':
    main()
