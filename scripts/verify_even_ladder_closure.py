#!/usr/bin/env python3
"""
verify_even_ladder_closure.py

Verifies one-step T_d closure for the even ladder of the 60714 lifting rule
at sufficiently large d. This addresses the proof gap identified in adversarial
review of the paper (the previous "expected to hold" sketch for even d ≥ 20
has been replaced by a proper algebraic argument; see paper §C.5 Lemma C.4).

What this verifies:
  For every admissible multiset n at digit length d (even, d ≥ 18) under the
  constructed even-ladder rule K_60714^(d), the orbit reaches T_d (the set
  of sorted-descending multisets ending in two zeros) in EXACTLY ONE step.

The script is exhaustive at d ∈ {18, 20} and uses random sampling at higher d
(where exhaustive enumeration becomes impractical on commodity hardware).

Note: at low even d ∈ {8, 10, 12, 14, 16}, one-step closure does NOT hold
universally — those cases are handled by Proposition 5.2's finite-state
enumeration (see paper Table 5.1, max reaching time ≤ 8). The threshold
d ≥ 18 for one-step closure is established in Lemma C.4 via the cliff-sum
bound and block-structure argument.

Usage:
    python3 verify_even_ladder_closure.py 18           # exhaustive (~30 sec)
    python3 verify_even_ladder_closure.py 20           # exhaustive (~3 min)
    python3 verify_even_ladder_closure.py 22 --sample 200000   # sampled
    python3 verify_even_ladder_closure.py 24 --sample 200000   # sampled

Output:
    Number of admissibles tested, number already in T_d, number reaching T_d
    in 1 step, number needing 2+ steps. The latter should always be 0 at
    d ≥ 18.
    
Companion to the paper's verify_60714_basin.py (which checks reaches-60714
not reaches-T_d) and verify_lemma_5_2.py (which covers the low-d cases).
"""

from itertools import combinations_with_replacement
from collections import Counter
import sys
import time
import random
import argparse


def get_coefs(d):
    """Even-ladder coefficient vector at digit length d."""
    if d < 8 or d % 2 != 0:
        raise ValueError(f"This script is for even d >= 8 (got d={d})")
    base = [9900, 9, 90, -9000, 99000, -99999]
    for k in range(7, d, 2):
        base.extend([9 * 10**k, -9 * 10**k])
    return base


def is_admissible(ms):
    """Non-repdigit, non-near-repdigit."""
    cnt = Counter(ms)
    if len(cnt) == 1:
        return False
    if max(cnt.values()) >= len(ms) - 1:
        return False
    return True


def in_T_d(ms_desc):
    """True iff sorted-desc multiset ends in two zeros."""
    return ms_desc[-1] == 0 and ms_desc[-2] == 0


def step(ms_desc, d, coefs):
    """One iteration of K^(d): returns (value, sorted-desc multiset of value)."""
    val = abs(sum(c * x for c, x in zip(coefs, ms_desc)))
    next_ms = tuple(sorted([int(c) for c in str(val).zfill(d)], reverse=True))
    return val, next_ms


def verify_exhaustive(d):
    """Exhaustive verification at digit length d."""
    coefs = get_coefs(d)

    n_admissible = 0
    n_already_T = 0
    n_one_step = 0
    n_two_plus = 0
    two_plus_examples = []

    t0 = time.time()
    print(f"=== Exhaustive verification at d = {d} ===")
    print(f"Estimated admissibles: ~{(d+9 * 10):,} multisets to enumerate")

    for ms in combinations_with_replacement(range(10), d):
        ms_desc = tuple(sorted(ms, reverse=True))
        if not is_admissible(ms_desc):
            continue
        n_admissible += 1

        if n_admissible % 1_000_000 == 0:
            elapsed = time.time() - t0
            print(f"  ... {n_admissible:,} done in {elapsed:.1f}s")

        if in_T_d(ms_desc):
            n_already_T += 1
            continue

        val, next_ms = step(ms_desc, d, coefs)
        if val == 0:
            # Falls into 0 — vacuously in T_d (zero has only zero digits)
            n_one_step += 1
            continue
        if in_T_d(next_ms):
            n_one_step += 1
        else:
            n_two_plus += 1
            if len(two_plus_examples) < 5:
                two_plus_examples.append((ms_desc, val, next_ms))

    elapsed = time.time() - t0
    print()
    print(f"Result for d = {d}:")
    print(f"  Admissibles tested:     {n_admissible:>12,}")
    print(f"  Already in T_d:         {n_already_T:>12,}")
    print(f"  Reach T_d in 1 step:    {n_one_step:>12,}")
    print(f"  Need 2+ steps:          {n_two_plus:>12,}")
    print(f"  Total runtime:          {elapsed:.1f}s")
    print()

    if n_two_plus == 0:
        print(f"✓ THEOREM 5.2 STEP VERIFIED: every admissible at d={d} reaches T_d in ≤ 1 step.")
    else:
        print(f"✗ COUNTEREXAMPLE: {n_two_plus} admissibles need 2+ steps to reach T_d.")
        print(f"  Examples:")
        for ms, val, nxt in two_plus_examples:
            print(f"    {ms}")
            print(f"      K(ms)         = {val}")
            print(f"      K(ms) sorted  = {nxt}")

    return n_two_plus == 0


def verify_sampled(d, sample_size, seed=42):
    """Random-sample verification at digit length d."""
    coefs = get_coefs(d)
    random.seed(seed)

    n_tested = 0
    n_already_T = 0
    n_one_step = 0
    n_two_plus = 0
    two_plus_examples = []

    t0 = time.time()
    print(f"=== Sampled verification at d = {d} ({sample_size:,} samples) ===")

    while n_tested < sample_size:
        # Generate a random sorted-desc multiset of size d
        digits = sorted([random.randint(0, 9) for _ in range(d)], reverse=True)
        ms_desc = tuple(digits)
        if not is_admissible(ms_desc):
            continue
        n_tested += 1

        if n_tested % 100_000 == 0:
            elapsed = time.time() - t0
            print(f"  ... {n_tested:,} samples in {elapsed:.1f}s")

        if in_T_d(ms_desc):
            n_already_T += 1
            continue

        val, next_ms = step(ms_desc, d, coefs)
        if val == 0:
            n_one_step += 1
            continue
        if in_T_d(next_ms):
            n_one_step += 1
        else:
            n_two_plus += 1
            if len(two_plus_examples) < 5:
                two_plus_examples.append((ms_desc, val, next_ms))

    elapsed = time.time() - t0
    print()
    print(f"Sampled result for d = {d}:")
    print(f"  Samples tested:         {n_tested:>12,}")
    print(f"  Already in T_d:         {n_already_T:>12,}")
    print(f"  Reach T_d in 1 step:    {n_one_step:>12,}")
    print(f"  Need 2+ steps:          {n_two_plus:>12,}")
    print(f"  Runtime:                {elapsed:.1f}s")
    print()

    if n_two_plus == 0:
        print(f"✓ No counterexamples found in {n_tested:,} samples at d={d}.")
        print(f"  (Sampled, not exhaustive — for d > 20, full enumeration is impractical.)")
    else:
        print(f"✗ Sampled counterexamples found: {n_two_plus} of {n_tested:,}.")
        for ms, val, nxt in two_plus_examples:
            print(f"  {ms}")

    return n_two_plus == 0


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Verify even-ladder T_d closure for the 60714 lifting rule at d >= 18. "
            "At low even d (8, 10, 12, 14, 16), one-step closure does NOT hold "
            "universally - those cases require Proposition 5.2's finite-state "
            "enumeration (covered by verify_lemma_5_2.py)."
        )
    )
    parser.add_argument("d", type=int, help="Even digit length (target: d >= 18)")
    parser.add_argument(
        "--sample",
        type=int,
        default=0,
        help="Sample size for non-exhaustive verification (0 = exhaustive)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for sampled verification",
    )
    args = parser.parse_args()

    if args.d < 8 or args.d % 2 != 0:
        print(f"Error: d must be even and >= 8 (got {args.d})")
        sys.exit(1)

    if args.d < 18:
        print(f"Note: d = {args.d} is below the d >= 18 threshold of Lemma C.4.")
        print(f"At low even d, one-step T_d closure does NOT hold universally.")
        print(f"Use verify_lemma_5_2.py for the finite-state argument at d <= 16.")
        print(f"Continuing anyway for diagnostic purposes...")
        print()

    print(f"Even-ladder rule at d = {args.d}:")
    print(f"  Coefficients: {get_coefs(args.d)}")
    print()

    if args.sample > 0:
        ok = verify_sampled(args.d, args.sample, args.seed)
    else:
        ok = verify_exhaustive(args.d)

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
