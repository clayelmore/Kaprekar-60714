#!/usr/bin/env python3
"""Fold ALL 312 pair-symmetric universal rules at m=2 to d=16; proxy filter;
FULL basin for every proxy passer. Reports survival count exactly."""
import sys, itertools, json, time
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

def fold_c(c0, d0, k):
    return tuple(g * 10**(d0*(k-1-j)) for g in c0 for j in range(k))

rules = json.load(open('/tmp/kap60714/verify_fable/m2_pairsym_universals.json'))
print(f"loaded {len(rules)} universal m=2 pair-symmetric rules")

d = 16
ALPH = [tuple(sorted(c, reverse=True))
        for c in itertools.combinations_with_replacement((7, 6, 4, 1), d)]
ALPH = [s for s in ALPH if s[0] != s[-1]]

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

passers = []
t0 = time.time()
for i, r in enumerate(rules):
    c16 = fold_c(tuple(r['c']), 8, 2)
    F16 = int(str(r['F']) * 2)
    cache = {}
    if all(trace_term(ms, c16, d, cache) == ('fp', F16) for ms in ALPH):
        passers.append((r, c16, F16))
print(f"proxy passers: {len(passers)}/{len(rules)} ({time.time()-t0:.0f}s)")
pf = Counter(str(F16) for _, _, F16 in passers)
print(f"passer fixed points: {dict(pf)}")

print("\n=== FULL d=16 basins for passers ===")
full_universal = []
for r, c16, F16 in passers:
    t1 = time.time()
    cache = {}
    nF = 0; ntot = 0
    for ms in itertools.combinations_with_replacement(range(9, -1, -1), d):
        if ms[0] == ms[-1]: continue
        ntot += 1
        if trace_term(ms, c16, d, cache) == ('fp', F16):
            nF += 1
    uni = (nF == ntot)
    if uni: full_universal.append((r, F16))
    print(f"  base F={r['F']} partition={r['partition']} -> F16={F16}: "
          f"{nF}/{ntot} {'UNIVERSAL' if uni else ''} ({time.time()-t1:.0f}s)")
print(f"\nfold_2-surviving universal rules at m=4: {len(full_universal)}/{len(rules)}")
json.dump([{'base': r, 'F16': F16} for r, F16 in full_universal],
          open('/tmp/kap60714/verify_fable/fold2_survivors_d16.json', 'w'), default=str)
