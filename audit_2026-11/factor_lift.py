#!/usr/bin/env python3
"""Does a universal half-swap rule at length 2n lift to length 2n+2 by inserting one new pair? (2026-11-21)

Lift type (i, j, q, sign): two new letters are inserted so that they have ranks i < j among the 2n+2 letters,
the new pair takes place q (old places >= q move up by one), sign +1 means (P, M) = (i, j).
Reads factor/b{B}_n{N}.tsv and factor/b{B}_n{N+1}.tsv (complete censuses) and counts, for each lift type, how
many universal rules at n stay universal at n+1.   Usage: factor_lift.py N [BASE]
"""
import sys, itertools
from collections import Counter
def load(p):
    d = {}
    for ln in open(p).read().split('\n')[1:]:
        if ln:
            m, F, a = ln.split('\t'); d[tuple(map(int, a.split(',')))] = int(m)
    return d
def norm(a):
    a = list(a)
    if a[-2] > a[-1]:
        for q in range(0, len(a), 2): a[q], a[q+1] = a[q+1], a[q]
    return tuple(a)
def lift(a, i, j, q, sg):
    L = len(a) + 2
    old = [r for r in range(L) if r not in (i, j)]
    b = [old[x] for x in a]
    pr = [i, j] if sg > 0 else [j, i]
    return norm(b[:2*q] + pr + b[2*q:])
n = int(sys.argv[1]); B = int(sys.argv[2]) if len(sys.argv) > 2 else 10
lo = load(f"factor/b{B}_n{n}.tsv"); hi = load(f"factor/b{B}_n{n+1}.tsv")
L = 2*n + 2; cnt = Counter(); mm = {}
for i, j in itertools.combinations(range(L), 2):
    for q in range(n + 1):
        for sg in (1, -1):
            for a in lo:
                la = lift(a, i, j, q, sg)
                if la in hi:
                    cnt[(i, j, q, sg)] += 1
                    mm.setdefault((i, j, q, sg), []).append((lo[a], hi[la]))
print(f"n={n}->{n+1} base {B}: {len(lo)} universal rules; lift types {len(list(itertools.combinations(range(L),2)))*(n+1)*2}")
for k, c in cnt.most_common(12):
    print(f"  new letters at ranks {k[0]},{k[1]}  place {k[2]}  sign {k[3]:+d}: {c}/{len(lo)} stay universal; e.g. m {mm[k][0][0]} -> {mm[k][0][1]}")
anyl = set()
for a in lo:
    for i, j in itertools.combinations(range(L), 2):
        for q in range(n + 1):
            for sg in (1, -1):
                if lift(a, i, j, q, sg) in hi: anyl.add(a)
print(f"  rules with at least one universal lift: {len(anyl)}/{len(lo)}")
