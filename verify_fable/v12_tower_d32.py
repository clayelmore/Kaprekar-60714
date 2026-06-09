#!/usr/bin/env python3
"""The 1746 fold tower at d=32 (m=8): evidence pass.
c32 = fold_2^3 applied to c4=(9,-900,900,-9). F32 = '1746'*8.
- check fixed point
- alphabet proxy: ALL multisets over {1,4,6,7} of size 32 (non-repdigit) reach F32?
- external-seed scan: 200k random non-repdigit multisets at d=32 traced to terminal.
"""
import sys, itertools, random, time
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

def fold_c(c0, d0, k):
    return tuple(g * 10**(d0*(k-1-j)) for g in c0 for j in range(k))

c4 = (9, -900, 900, -9)
c8 = fold_c(c4, 4, 2)
c16 = fold_c(c8, 8, 2)
c32 = fold_c(c16, 16, 2)
d = 32
F = int('1746' * 8)
s = sorted_desc_digits(F, d)
print(f"K(sorted F32) == F32: {K_apply(c32, s) == F}")

def trace_term(ms, c, d, cache, maxsteps=2000):
    path = []
    cur = ms
    steps = 0
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
        steps += 1
        if steps > maxsteps:
            cache[cur] = ('maxiter', n); break
    res = cache[cur]
    for p in path: cache[p] = res
    return res

print("\n=== alphabet proxy over {1,4,6,7}^32 multisets ===")
t0 = time.time()
cache = {}
states = [tuple(sorted(cmb, reverse=True))
          for cmb in itertools.combinations_with_replacement((7, 6, 4, 1), d)]
states = [st for st in states if st[0] != st[-1]]
term = Counter(trace_term(ms, c32, d, cache) for ms in states)
print(f"  {len(states)} states: {dict(term)} ({time.time()-t0:.0f}s)")
print(f"  proxy {'PASS' if term.get(('fp', F), 0) == len(states) else 'FAIL'}")

print("\n=== random external-seed scan (200k seeds) ===")
random.seed(123)
t0 = time.time()
term2 = Counter()
for trial in range(200000):
    ms = tuple(sorted(random.choices(range(10), k=d), reverse=True))
    if ms[0] == ms[-1]: continue
    term2[trace_term(ms, c32, d, cache)] += 1
print(f"  terminals: {dict(term2)} ({time.time()-t0:.0f}s)")
nfp = term2.get(('fp', F), 0)
tot = sum(term2.values())
print(f"  reached F32: {nfp}/{tot}")
