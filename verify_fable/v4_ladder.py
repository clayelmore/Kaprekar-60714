#!/usr/bin/env python3
"""Verification battery 3: the 60714 zero-padding ladders.
- Build odd ladder from c5=(9900,9,90,-9000,-999), even from c6=(...,99000,-99999),
  appending zero-sum pairs (+9*10^(d-2), -9*10^(d-2)).
- Check K(padded 60714)=60714 at d=5..20 and d=100.
- d=7: full classification over admissible multisets (repdigit+near-repdigit excluded):
  expect every orbit reaches 60714 or 0; count the 0-collapsers; check the 45
  block-aligned (x^5,y^2) multisets all map to 0 in one step.
- d=8: same full classification.
"""
import sys, itertools
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

def ladder_c(d):
    if d % 2 == 1:
        c = [9900, 9, 90, -9000, -999]
        dd = 5
    else:
        c = [9900, 9, 90, -9000, 99000, -99999]
        dd = 6
    while dd < d:
        dd += 2
        c = c + [9 * 10**(dd-2), -9 * 10**(dd-2)]
    return tuple(c)

def admissible_multisets(d):
    out = []
    for combo in itertools.combinations_with_replacement(range(9, -1, -1), d):
        if combo[0] == combo[-1]: continue
        cnt = Counter(combo)
        if max(cnt.values()) >= d - 1: continue
        out.append(combo)
    return out

print("=== fixed point along the ladders ===")
ok = True
for d in list(range(5, 21)) + [100]:
    c = ladder_c(d)
    s = sorted_desc_digits(60714, d)
    v = K_apply(c, s)
    if v != 60714: ok = False
    if d <= 9 or d == 20 or d == 100:
        print(f"  d={d}: K(padded 60714) = {v}  {'OK' if v == 60714 else 'FAIL'}")
print(f"  all d in 5..20 and 100: {'OK' if ok else 'FAIL'}")

for d in (7, 8):
    print(f"\n=== d={d}: full classification under the ladder rule ===")
    c = ladder_c(d)
    A = admissible_multisets(d)
    cache = {}
    term = Counter()
    zero_set = []
    for ms in A:
        path = []
        cur = ms
        while cur not in cache:
            path.append(cur)
            n = K_apply(c, cur)
            if n == 0:
                for p in path: cache[p] = ('zero', 0)
                break
            nxt = sorted_desc_digits(n, d)
            if nxt == cur:
                for p in path: cache[p] = ('fp', n)
                break
            if nxt in path:
                for p in path: cache[p] = ('cycle', n)
                break
            cur = nxt
        res = cache[cur]
        for p in path: cache[p] = res
        term[res] += 1
        if res[0] == 'zero': zero_set.append(ms)
    kinds = Counter(k for (k, v), n in term.items() for _ in range(n))
    print(f"  admissible: {len(A)}")
    for (k, v), n in sorted(term.items()):
        print(f"    -> {k} {v}: {n}")
    # block-aligned step-one check
    npairs = (d - 5) // 2 if d % 2 == 1 else (d - 6) // 2 + 1
    # block structure: native block ranks 0..4 (odd) or 0..3+pair? simpler: directly
    # test multisets of sorted form (x^5, y^2, z^2, ...) constant on native block and pairs
    if d == 7:
        B = [tuple([x]*5 + [y]*2) for x in range(10) for y in range(10)
             if x > y]
        all_zero_one_step = all(K_apply(c, b) == 0 for b in B)
        print(f"  block-aligned (x^5,y^2), x>y: {len(B)} multisets; all K=0 in one step: {all_zero_one_step}")
