#!/usr/bin/env python3
"""Verify the artifact m=3 universal rule with a full d=12 basin run (my own check),
then fold_2 it to d=24 (m=6) and run proxy + 300k random-seed scan."""
import sys, itertools, random, time, json
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

art = json.load(open('/Users/clayelmore/Downloads/d16_1467_test/m3_verified_universals.json'))[0]
c12 = tuple(art['c'])
d = 12
s = tuple([7]*3 + [6]*3 + [4]*3 + [1]*3)
F12 = K_apply(c12, s)
print(f"m=3 rule fixes: {F12}, multiset M_3: {sorted(str(F12)) == sorted('111444666777')}")
print(f"fixed: {sorted_desc_digits(F12, d) == s}")

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

print("=== full d=12 basin (my verification) ===")
t0 = time.time()
cache = {}
nF = 0; ntot = 0
for ms in itertools.combinations_with_replacement(range(9, -1, -1), d):
    if ms[0] == ms[-1]: continue
    ntot += 1
    if trace_term(ms, c12, d, cache) == ('fp', F12): nF += 1
print(f"  basin {nF}/{ntot} {'UNIVERSAL' if nF == ntot else 'NOT'} ({time.time()-t0:.0f}s)")

print("\n=== fold_2 -> d=24 (m=6) ===")
def fold_c(c0, d0, k):
    return tuple(g * 10**(d0*(k-1-j)) for g in c0 for j in range(k))
c24 = fold_c(c12, 12, 2)
d24 = 24
F24 = int(str(F12) * 2)
print(f"K(sorted M_6) == F24: {K_apply(c24, sorted_desc_digits(F24, d24)) == F24}")
cache = {}
ALPH = [t for t in (tuple(sorted(cmb, reverse=True))
        for cmb in itertools.combinations_with_replacement((7, 6, 4, 1), d24))
        if t[0] != t[-1]]
term = Counter(trace_term(ms, c24, d24, cache) for ms in ALPH)
print(f"  alphabet proxy ({len(ALPH)} states): {dict(term)}")
print(f"  proxy {'PASS' if term.get(('fp', F24), 0) == len(ALPH) else 'FAIL'}")
random.seed(99)
term2 = Counter()
t0 = time.time()
for _ in range(300000):
    ms = tuple(sorted(random.choices(range(10), k=d24), reverse=True))
    if ms[0] == ms[-1]: continue
    term2[trace_term(ms, c24, d24, cache)] += 1
print(f"  300k random seeds: {dict(term2)} ({time.time()-t0:.0f}s)")
