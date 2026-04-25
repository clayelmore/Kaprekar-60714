"""
verify_lemma_5_2.py
===================
Verifies Lemma 5.2 (bounded reaching time to T_d) at digit lengths d=7..16
on both odd and even ladders by exhaustive enumeration over admissible
digit multisets.

For each d and each ladder, enumerates every admissible multiset (non-repdigit,
non-near-repdigit) and iterates the ladder rule until the tail-two-zeros
absorbing set T_d is reached. Records the maximum reaching time.

Expected output (odd ladder):
    d=7: max reaching time 8
    d=9: 3
    d=11: 2
    d=13: 2
    d=15: 1  (one-step closure begins here - Lemma C.3)

Expected output (even ladder):
    d=8: max reaching time 6
    d=10: 3
    d=12: 2
    d=14: 2
    d=16: 1  (one-step closure)

Usage:
    python3 verify_lemma_5_2.py                 # both ladders, d=7..16
    python3 verify_lemma_5_2.py --odd           # only odd
    python3 verify_lemma_5_2.py --even          # only even
    python3 verify_lemma_5_2.py --max-d 18      # extend to d=18
"""

import sys
import time
from itertools import combinations_with_replacement
from collections import Counter


def build_odd_ladder_rule(d):
    """Returns coefficient vector for odd-ladder rule at d (d >= 5, odd)."""
    pi = [4, 1, 2, 3, 0]
    sigma = [2, 0, 1, 4, 3]
    cur_d = 5
    while cur_d < d:
        pi.extend([cur_d + 1, cur_d])
        sigma.extend([cur_d, cur_d + 1])
        cur_d += 2
    return tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(d))


def build_even_ladder_rule(d):
    """Returns coefficient vector for even-ladder rule at d (d >= 6, even)."""
    pi = [4, 1, 2, 3, 5, 0]
    sigma = [2, 0, 1, 4, 3, 5]
    cur_d = 6
    while cur_d < d:
        pi.extend([cur_d, cur_d + 1])
        sigma.extend([cur_d + 1, cur_d])
        cur_d += 2
    return tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(d))


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


def in_Td(ms_desc):
    """Check if the multiset's sorted-descending form ends in at least two zeros."""
    return len(ms_desc) >= 2 and ms_desc[-1] == 0 and ms_desc[-2] == 0


def reaching_time(ms_desc, coefs, d, budget=20):
    """Number of iterations until T_d is reached; or -1 if not within budget."""
    if in_Td(ms_desc):
        return 0
    cur = ms_desc
    for t in range(1, budget + 1):
        val = abs(sum(c * x for c, x in zip(coefs, cur)))
        nxt = tuple(sorted((int(c) for c in str(val).zfill(d)), reverse=True))
        if in_Td(nxt):
            return t
        if nxt == cur:
            return -1  # fixed point not in T_d — orbit stuck
        cur = nxt
    return -1


def verify_ladder(d, coefs, ladder_name):
    print(f"\n{ladder_name} ladder at d={d}...", flush=True)
    t0 = time.time()
    multisets = build_admissible_multisets(d)
    max_t = 0
    failures = 0
    time_dist = Counter()
    for ms in multisets:
        t = reaching_time(ms, coefs, d, budget=15)
        if t == -1:
            failures += 1
        else:
            time_dist[t] += 1
            if t > max_t:
                max_t = t
    elapsed = time.time() - t0
    print(f"  admissible multisets: {len(multisets)}")
    print(f"  max reaching time:    {max_t}")
    print(f"  reaching-time dist:   {dict(time_dist)}")
    print(f"  failures (stuck):     {failures}")
    print(f"  elapsed:              {elapsed:.1f}s", flush=True)
    return max_t, failures


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description=("Finite-state verification of bounded reaching time to T_d "
                     "(tail-2-zeros set) for the 60714 lifting ladders. "
                     "Verifies the structural lemma underlying Theorem 5.2. "
                     "Does NOT verify basin universality (use verify_60714_basin.py for that)."))
    parser.add_argument('--odd', action='store_true',
                        help="Run only the odd ladder (d = 7, 9, 11, ...)")
    parser.add_argument('--even', action='store_true',
                        help="Run only the even ladder (d = 8, 10, 12, ...)")
    parser.add_argument('--max-d', type=int, default=16, dest='max_d',
                        help="Maximum digit length to verify (default 16)")
    args = parser.parse_args()

    run_odd = not args.even
    run_even = not args.odd
    max_d = args.max_d

    if run_odd:
        print("=" * 60)
        print("ODD LADDER (d = 7, 9, 11, ..., max)")
        print("=" * 60)
        for d in range(7, max_d + 1, 2):
            coefs = build_odd_ladder_rule(d)
            verify_ladder(d, coefs, 'odd')
    
    if run_even:
        print("\n" + "=" * 60)
        print("EVEN LADDER (d = 8, 10, 12, ..., max)")
        print("=" * 60)
        for d in range(8, max_d + 1, 2):
            coefs = build_even_ladder_rule(d)
            verify_ladder(d, coefs, 'even')


if __name__ == '__main__':
    main()
