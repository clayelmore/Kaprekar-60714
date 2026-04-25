#!/usr/bin/env python3
"""
verify_60714_basin.py

Verifies the basin universality claim of Theorem 5.2 by directly iterating
every admissible digit multiset under the constructed coefficient-preserving
lifting rule K_60714^(d) and checking whether the orbit reaches 60714.

This script is distinct from `verify_lemma_5_2.py`, which only verifies that
orbits enter the tail-2-zeros set T_d in bounded time. Reaching T_d is NOT
the same as reaching 60714: the corrected Theorem 5.2 (§5.2 of the paper)
states that strict universality holds at d = 5, 6 only; at d >= 7, the basin
is A_d minus E_d, where E_d is the escape class of block-aligned multisets and
their backward orbits.

What this script does:
  - Enumerates all admissible digit multisets at digit length d
  - Iterates K_60714^(d) on each
  - Records: how many reach 60714, how many reach 0 (escape class),
    how many enter cycles, max reaching time among successes
  - Reports the empirical escape class and verifies it matches the
    theoretical block-aligned characterization (Definition 5.2)

Usage:
    python3 verify_60714_basin.py 5    # ~0.1 s
    python3 verify_60714_basin.py 6    # ~0.5 s
    python3 verify_60714_basin.py 7    # ~3 s
    python3 verify_60714_basin.py 8    # ~30 s
    python3 verify_60714_basin.py 9    # ~5 minutes
    python3 verify_60714_basin.py 10   # ~30 minutes (Mac)

For larger d, use --sample-size N to run on a random sample of admissibles.

Output:
    Reports basin coverage, escape class size, max reaching time,
    sample failure inputs, and an algebraic verification that the
    step-1 escape class matches the closed-form count of Lemma 5.2.2.
"""

from itertools import combinations_with_replacement
from collections import Counter
from math import comb
import sys
import argparse


def get_coefs(d):
    """Coefficient vector for the constructed 60714 ladder rule at digit length d."""
    if d == 5:
        return [9900, 9, 90, -9000, -999]
    if d == 6:
        return [9900, 9, 90, -9000, 99000, -99999]
    if d % 2 == 1:  # odd ladder
        base = [9900, 9, 90, -9000, -999]
        for k in range(6, d, 2):
            base.extend([9 * 10**k, -9 * 10**k])
        return base
    else:  # even ladder
        base = [9900, 9, 90, -9000, 99000, -99999]
        for k in range(7, d, 2):
            base.extend([9 * 10**k, -9 * 10**k])
        return base


def step(ms, d, coefs):
    """One iteration of K^(d) on the sorted-descending multiset ms."""
    val = abs(sum(c * x for c, x in zip(coefs, ms)))
    next_ms = tuple(sorted([int(c) for c in str(val).zfill(d)], reverse=True))
    return val, next_ms


def is_admissible(ms):
    """True iff ms is non-repdigit and non-near-repdigit."""
    cnt = Counter(ms)
    if len(cnt) == 1:
        return False
    if max(cnt.values()) >= len(ms) - 1:
        return False
    return True


def is_block_aligned(ms, d):
    """True iff ms matches the block-aligned pattern (Definition 5.2)."""
    base = 5 if d % 2 == 1 else 6
    if len(set(ms[:base])) != 1:
        return False
    for i in range(base, d, 2):
        if i + 1 >= d:
            break
        if ms[i] != ms[i + 1]:
            return False
    return True


def trace(ms_desc, d, coefs, max_steps=80):
    """
    Iterate K^(d) starting from ms_desc.
    Returns (final_value, num_steps, fate) where fate is one of:
      'reaches_60714', 'reaches_0', 'cycle', 'timeout'
    """
    cur = ms_desc
    seen = []
    for step_n in range(max_steps):
        if cur in seen:
            return None, step_n, 'cycle'
        seen.append(cur)
        val, nxt = step(cur, d, coefs)
        if nxt == cur:
            if val == 60714:
                return val, step_n, 'reaches_60714'
            elif val == 0:
                return val, step_n, 'reaches_0'
            else:
                return val, step_n, f'reaches_{val}'
        cur = nxt
    return None, max_steps, 'timeout'


def closed_form_E1(d):
    """Closed-form count of step-1 escape class (Lemma 5.2.2)."""
    if d < 7:
        return 0
    d_0 = 5 if d % 2 == 1 else 6
    k = 1 + (d - d_0) // 2
    return comb(10 + k - 1, k) - 10


def main():
    parser = argparse.ArgumentParser(
        description="Verify basin universality of 60714 ladder rule"
    )
    parser.add_argument("d", type=int, help="Digit length (>= 5)")
    parser.add_argument(
        "--sample-size",
        type=int,
        default=0,
        help="Random sample size (0 = exhaustive)",
    )
    parser.add_argument(
        "--show-failures",
        type=int,
        default=10,
        help="Number of failure examples to show",
    )
    args = parser.parse_args()

    d = args.d
    if d < 5:
        print(f"Error: d must be >= 5 (got {d})")
        sys.exit(1)

    coefs = get_coefs(d)
    print(f"=== verify_60714_basin.py: d = {d} ===\n")
    print(f"Constructed coefficient vector ({len(coefs)} coefficients):")
    print(f"  {coefs}\n")

    # Enumerate or sample admissibles
    if args.sample_size > 0:
        import random
        all_admissibles = []
        for ms in combinations_with_replacement(range(10), d):
            ms_desc = tuple(sorted(ms, reverse=True))
            if is_admissible(ms_desc):
                all_admissibles.append(ms_desc)
        if args.sample_size >= len(all_admissibles):
            admissibles = all_admissibles
            print(f"Sample size >= total; running exhaustively.")
        else:
            admissibles = random.sample(all_admissibles, args.sample_size)
            print(f"Random sample of {args.sample_size} from {len(all_admissibles):,} total admissibles.")
    else:
        admissibles = []
        for ms in combinations_with_replacement(range(10), d):
            ms_desc = tuple(sorted(ms, reverse=True))
            if is_admissible(ms_desc):
                admissibles.append(ms_desc)
        print(f"Exhaustive enumeration: {len(admissibles):,} admissible multisets.")

    # Iterate
    fate_counts = Counter()
    successes = []
    failures_to_zero = []
    other_failures = []
    max_reaching_time = 0

    for ms in admissibles:
        val, steps, fate = trace(ms, d, coefs)
        fate_counts[fate] += 1
        if fate == 'reaches_60714':
            successes.append((ms, steps))
            max_reaching_time = max(max_reaching_time, steps)
        elif fate == 'reaches_0':
            failures_to_zero.append((ms, steps))
        else:
            other_failures.append((ms, steps, fate))

    n_total = len(admissibles)
    basin_60714 = fate_counts['reaches_60714'] / n_total

    print()
    print("=== Results ===")
    print(f"  Reach 60714:  {fate_counts['reaches_60714']:>8,} ({basin_60714:.6f})")
    print(f"  Reach 0:      {fate_counts['reaches_0']:>8,}")
    print(f"  Cycles:       {fate_counts['cycle']:>8,}")
    print(f"  Timeouts:     {fate_counts['timeout']:>8,}")
    other = sum(v for k, v in fate_counts.items()
                if k not in ('reaches_60714', 'reaches_0', 'cycle', 'timeout'))
    print(f"  Other:        {other:>8,}")
    print()
    print(f"  Max reaching time among successes: {max_reaching_time}")

    # Verify against Theorem 5.2
    print()
    if d <= 6:
        if fate_counts['reaches_60714'] == n_total:
            print(f"✓ Theorem 5.2 part 2 (strict universality at d = {d}) VERIFIED.")
        else:
            print(f"✗ Theorem 5.2 part 2 (strict universality at d = {d}) FAILED.")
    else:
        E_d_size = fate_counts['reaches_0'] + fate_counts['cycle'] + other + fate_counts['timeout']
        print(f"✓ Empirical escape class size |E_d| = {E_d_size}")
        print(f"  Closed-form |E_d^(1)| (step-1 only): {closed_form_E1(d)}")

        # Verify step-1 component matches block-aligned characterization
        step1_failures = [ms for ms, _ in failures_to_zero
                          if abs(sum(c * x for c, x in zip(coefs, ms))) == 0]
        block_aligned_count = sum(1 for ms in admissibles if is_block_aligned(ms, d))
        if len(step1_failures) == block_aligned_count == closed_form_E1(d):
            print(f"✓ Step-1 escape class matches block-aligned characterization "
                  f"(Definition 5.2): {len(step1_failures)} multisets, exact match.")
        else:
            print(f"⚠ Mismatch: step-1 fails = {len(step1_failures)}, "
                  f"block-aligned = {block_aligned_count}, closed-form = {closed_form_E1(d)}.")

    # Show sample failures
    if failures_to_zero and args.show_failures > 0:
        print()
        print(f"=== Sample of {min(args.show_failures, len(failures_to_zero))} "
              f"failure inputs (orbit reaches 0) ===")
        for ms, steps in failures_to_zero[:args.show_failures]:
            n = int(''.join(str(x) for x in ms))
            ba = "block-aligned" if is_block_aligned(ms, d) else f"step-{steps + 1}"
            print(f"  {n:>{d}} (digits {ms}) → 0 in {steps + 1} step{'s' if steps else ''} [{ba}]")


if __name__ == "__main__":
    main()
