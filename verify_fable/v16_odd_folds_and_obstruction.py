#!/usr/bin/env python3
"""Complete the fold map:
- fold_5 (d=20) and fold_7 (d=28) of all four d=4 universal rules: alphabet proxy
  (proxy failure is DEFINITIVE non-universality since alphabet states are admissible).
- obstruction probe: for fold_2^2(classical 6174 rule) at d=16, exhibit the cycle/terminal
  that traps an alphabet state.
- also: fold_2 o fold_3? and fold_3 of the universal d=8 fold of 1746 (-> m=6, d=24 proxy).
"""
import sys, itertools
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

def fold_c(c0, d0, k):
    return tuple(g * 10**(d0*(k-1-j)) for g in c0 for j in range(k))

BASE = {1746: (9, -900, 900, -9),
        2538: (90, 999, -999, -90),
        5382: (900, -9, 9, -900),
        6174: (999, 90, -90, -999)}

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

def alphabet_states(digs, d):
    return [t for t in (tuple(sorted(cmb, reverse=True))
            for cmb in itertools.combinations_with_replacement(digs, d))
            if t[0] != t[-1]]

print("=== odd folds from d=4 (proxy; FAIL is definitive) ===")
for k, d in ((3, 12), (5, 20), (7, 28)):
    for F4, c4 in BASE.items():
        ck = fold_c(c4, 4, k)
        Fk = int(str(F4) * k)
        states = alphabet_states((7, 6, 4, 1), d)
        cache = {}
        bad = None
        nF = 0
        for ms in states:
            res = trace_term(ms, ck, d, cache)
            if res == ('fp', Fk): nF += 1
            elif bad is None: bad = (ms, res)
        print(f"  fold_{k}({F4}): proxy {nF}/{len(states)}"
              f"{' PASS' if nF == len(states) else f' FAIL e.g. {bad[0][:6]}.. -> {bad[1]}'}")

print("\n=== obstruction for fold_2^2(6174 classical) at d=16 ===")
c16 = fold_c(fold_c(BASE[6174], 4, 2), 8, 2)
F16 = int('6174' * 4)
states = alphabet_states((7, 6, 4, 1), 16)
cache = {}
fails = [(ms, trace_term(ms, c16, 16, cache)) for ms in states]
failures = [(ms, r) for ms, r in fails if r != ('fp', F16)]
print(f"  alphabet failures: {len(failures)}/{len(states)}")
term_count = Counter(r for _, r in failures)
print(f"  failure terminals: {dict(term_count)}")
# expand one cycle explicitly
if failures:
    ms = failures[0][0]
    seen = []
    cur = ms
    while cur not in seen:
        seen.append(cur)
        n = K_apply(c16, cur)
        cur = sorted_desc_digits(n, 16)
    i0 = seen.index(cur)
    cyc = seen[i0:]
    print(f"  example trapped cycle (period {len(cyc)}):")
    for st in cyc:
        print(f"    {''.join(map(str, st))} -> K={K_apply(c16, st)}")

print("\n=== fold_3 of the universal d=8 fold of 1746 (-> d=24, m=6 proxy) ===")
c8 = fold_c(BASE[1746], 4, 2)
c24 = fold_c(c8, 8, 3)
F24 = int('17461746' * 3)
states = alphabet_states((7, 6, 4, 1), 24)
cache = {}
nF = sum(1 for ms in states if trace_term(ms, c24, 24, cache) == ('fp', F24))
print(f"  proxy: {nF}/{len(states)} {'PASS' if nF == len(states) else 'FAIL'}")
