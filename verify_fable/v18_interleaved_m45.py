#!/usr/bin/env python3
"""Interleaved (= fold_m of classical) basins at m=4 (d=16) and m=5 (d=20),
rank-array method. Expect ~99.69% and ~9.52%."""
import sys, itertools, time
from math import comb
sys.path.insert(0, '/Users/clayelmore/Downloads')

GAMMA = (999, 90, -90, -999)
def interleaved_c(m):
    return tuple(GAMMA[X] * 10**(4*(m-1-j)) for X in range(4) for j in range(m))

def full_basin_rank(ck, d, F):
    c_rev = tuple(reversed(ck))
    CT = [[comb(b, i) for i in range(d + 1)] for b in range(d + 10)]
    def rank(t_asc):
        r = 0
        for i in range(d):
            r += CT[t_asc[i] + i][i + 1]
        return r
    NST = comb(d + 9, 9)
    status = bytearray(NST)
    t0 = time.time()
    nF = 0; count = 0
    for t in itertools.combinations_with_replacement(range(10), d):
        if t[0] == t[-1]: continue
        count += 1
        r0 = rank(t)
        if status[r0]:
            if status[r0] == 1: nF += 1
            continue
        path = [r0]
        cur = t
        while True:
            n = 0
            for i in range(d):
                n += c_rev[i] * cur[i]
            n = abs(n)
            if n == 0:
                code = 2; break
            s = str(n).zfill(d)
            nxt = tuple(sorted(int(ch) for ch in s))
            if nxt == cur:
                code = 1 if n == F else 2
                break
            rn = rank(nxt)
            if status[rn]:
                code = status[rn]; break
            if rn in path:
                code = 2; break
            path.append(rn)
            cur = nxt
        for rr in path: status[rr] = code
        if code == 1: nF += 1
    return nF, count, time.time() - t0

for m in (4, 5):
    d = 4 * m
    c = interleaved_c(m)
    F = int('6174' * m)
    nF, count, el = full_basin_rank(c, d, F)
    print(f"interleaved m={m} (d={d}): basin {nF:,}/{count:,} = {nF/count:.4f} ({el:.0f}s)", flush=True)
