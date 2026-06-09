#!/usr/bin/env python3
"""FULL basin enumeration at d=24 for the folded m=3 universal rule.
38,567,100 multisets, rank-indexed bytearray cache (memory ~40MB).
Codes: 0 unknown, 1 reaches F24, 2 other terminal."""
import sys, itertools, time, json
sys.path.insert(0, '/Users/clayelmore/Downloads')

art = json.load(open('/Users/clayelmore/Downloads/d16_1467_test/m3_verified_universals.json'))[0]
c12 = tuple(art['c'])
def fold_c(c0, d0, k):
    return tuple(g * 10**(d0*(k-1-j)) for g in c0 for j in range(k))
c24 = fold_c(c12, 12, 2)
d = 24
F = int('666141417774' * 2)
c_rev = tuple(reversed(c24))  # for ascending tuples

# binomial table: C[b][i] for b in 0..32, i in 0..24
from math import comb
CT = [[comb(b, i) for i in range(25)] for b in range(33)]

def rank(t_asc):
    r = 0
    for i in range(24):
        r += CT[t_asc[i] + i][i + 1]
    return r

NSTATES = comb(33, 9)
status = bytearray(NSTATES)
t0 = time.time()
n_zero = n_F = n_other = 0
count = 0
report = 2_000_000
for t in itertools.combinations_with_replacement(range(10), d):
    if t[0] == t[-1]:
        continue
    count += 1
    r0 = rank(t)
    if status[r0]:
        if status[r0] == 1: n_F += 1
        else: n_other += 1
        if count % report == 0:
            print(f"  {count:,} done, F:{n_F:,} other:{n_other:,} ({time.time()-t0:.0f}s)", flush=True)
        continue
    path = [r0]
    cur = t
    code = None
    while True:
        n = 0
        for i in range(24):
            n += c_rev[i] * cur[i]
        n = abs(n)
        if n == 0:
            code = 2; break
        s = str(n)
        if len(s) < 24:
            s = '0' * (24 - len(s)) + s
        nxt = tuple(sorted(int(ch) for ch in s))
        if nxt == cur:
            code = 1 if n == F else 2
            break
        rn = rank(nxt)
        st = status[rn]
        if st:
            code = st; break
        if rn in path:
            code = 2; break
        path.append(rn)
        cur = nxt
    for rr in path:
        status[rr] = code
    if code == 1: n_F += 1
    else: n_other += 1
    if count % report == 0:
        print(f"  {count:,} done, F:{n_F:,} other:{n_other:,} ({time.time()-t0:.0f}s)", flush=True)

print(f"\nTOTAL admissible (non-repdigit): {count:,}")
print(f"reach F24={F}: {n_F:,}")
print(f"other: {n_other:,}")
print(f"UNIVERSAL: {n_F == count}")
print(f"elapsed {time.time()-t0:.0f}s")
