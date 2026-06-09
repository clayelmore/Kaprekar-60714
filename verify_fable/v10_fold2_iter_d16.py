#!/usr/bin/env python3
"""Folding experiment part 2: iterated fold_2 from d=8 to d=16.
Candidates: fold_2(fold_2(R)) for each universal full-variable rule R at d=4.
Quick alphabet proxy first, then FULL basin over all 2,042,965 non-repdigit
multisets at d=16 for proxy passers.
"""
import sys, itertools, time
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

def fold_c(c0, d0, k):
    out = []
    for g in c0:
        for j in range(k):
            out.append(g * 10**(d0*(k-1-j)))
    return tuple(out)

BASE = {1746: (9, -900, 900, -9),
        2538: (90, 999, -999, -90),
        5382: (900, -9, 9, -900),
        6174: (999, 90, -90, -999)}

def alphabet_states(F, d):
    """multisets over digits of F (plus nothing else), non-repdigit"""
    digs = sorted(set(int(ch) for ch in str(F)), reverse=True)
    out = []
    for c in itertools.combinations_with_replacement(digs, d):
        if c[0] != c[-1]:
            out.append(tuple(sorted(c, reverse=True)))
    return out

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

d = 16
print("=== alphabet proxy (digits of F, all multisets, non-repdigit) ===")
passers = []
for F4, c4 in BASE.items():
    c16 = fold_c(fold_c(c4, 4, 2), 8, 2)
    F16 = int(str(F4) * 4)
    states = alphabet_states(F4, d)
    cache = {}
    ok = all(trace_term(ms, c16, d, cache) == ('fp', F16) for ms in states)
    print(f"  F={F4}: fold_2^2 fixes {F16}; proxy over {len(states)} alphabet states: {'PASS' if ok else 'FAIL'}")
    if ok:
        passers.append((F4, c16, F16))

print("\n=== FULL basin at d=16 for proxy passers ===")
for F4, c16, F16 in passers:
    t0 = time.time()
    cache = {}
    nF = 0; ntot = 0
    other = Counter()
    for ms in itertools.combinations_with_replacement(range(9, -1, -1), d):
        if ms[0] == ms[-1]: continue
        ntot += 1
        res = trace_term(ms, c16, d, cache)
        if res == ('fp', F16): nF += 1
        else: other[res] += 1
    print(f"  F4={F4}: basin of {F16} = {nF}/{ntot} = {nF/ntot:.6f} ({time.time()-t0:.0f}s)"
          f"{'  *** UNIVERSAL ***' if nF == ntot else ''}")
    if other:
        print(f"    other terminals: {sorted(other.items(), key=lambda kv: -kv[1])[:5]}")
