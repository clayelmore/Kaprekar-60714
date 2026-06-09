#!/usr/bin/env python3
"""Systematic fold_k(1746) study, k=2..8:
- alphabet proxy at d=4k (definitive on FAIL),
- 200k random-seed scan for passers,
- FULL basin via rank-array for k=4 (d=16) and k=5 (d=20).
"""
import sys, itertools, random, time
from math import comb
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

c4 = (9, -900, 900, -9)
def fold_c(c0, d0, k):
    return tuple(g * 10**(d0*(k-1-j)) for g in c0 for j in range(k))

def trace_term(ms, c, d, cache):
    path = []
    cur = ms
    while cur not in cache:
        path.append(cur)
        n = K_apply(c, cur)
        if n == 0:
            cache[cur] = ('zero', 0); break
        nxt = sorted_desc_digits(n, d)
        if nxt == cur:
            cache[cur] = ('fp', n); break
        if nxt in path:
            cache[cur] = ('cyc', n); break
        cur = nxt
    res = cache[cur]
    for p in path: cache[p] = res
    return res

print("=== fold_k(1746) proxy + seeds, k=2..8 ===")
passers = []
for k in range(2, 9):
    d = 4 * k
    ck = fold_c(c4, 4, k)
    Fk = int('1746' * k)
    states = [t for t in (tuple(sorted(cmb, reverse=True))
              for cmb in itertools.combinations_with_replacement((7, 6, 4, 1), d))
              if t[0] != t[-1]]
    cache = {}
    nF = sum(1 for ms in states if trace_term(ms, ck, d, cache) == ('fp', Fk))
    line = f"  k={k} (d={d}): proxy {nF}/{len(states)}"
    if nF == len(states):
        random.seed(2024 + k)
        ok = 0; tot = 0
        for _ in range(200000):
            ms = tuple(sorted(random.choices(range(10), k=d), reverse=True))
            if ms[0] == ms[-1]: continue
            tot += 1
            if trace_term(ms, ck, d, cache) == ('fp', Fk): ok += 1
        line += f" PASS; seeds {ok}/{tot}"
        passers.append(k)
    else:
        line += " FAIL (definitive: not universal)"
    print(line, flush=True)
print(f"proxy+seed passers: k in {passers}")

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

for k in (4, 5):
    if k in passers:
        d = 4 * k
        ck = fold_c(c4, 4, k)
        Fk = int('1746' * k)
        nF, count, el = full_basin_rank(ck, d, Fk)
        print(f"\nFULL basin fold_{k}(1746) at d={d}: {nF:,}/{count:,} "
              f"{'*** UNIVERSAL ***' if nF == count else 'NOT universal'} ({el:.0f}s)")
