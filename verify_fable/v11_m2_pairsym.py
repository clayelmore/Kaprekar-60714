#!/usr/bin/env python3
"""Enumerate ALL pair-symmetric M_2-fixing rules at d=8 and find the universal ones.
Pair-symmetric: partition positions {0..7} into A7,A6,A4,A1 (size 2 each);
pi assigns blocks to their position sets, sigma = pi composed with the swap
7<->1, 6<->4. Rule determined by: pairing lambda7: A7<->A1 (2), lambda6: A6<->A4 (2),
and rank-assignments of the resulting coefficient pairs (2 per block-pair side: 2^4).
Total 64 rules/partition, 2520 partitions.
Fixing is partition-level: digits(|6*S7+2*S6|) == M_2.
"""
import sys, itertools, time, json
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

M2 = Counter('11446677')
d = 8
A8 = [c for c in itertools.combinations_with_replacement(range(9,-1,-1), d) if c[0] != c[-1]]
E = [10**(d-1-p) for p in range(d)]

def universal_check(c, F):
    cache = {}
    for ms in A8:
        path = []
        cur = ms
        while cur not in cache:
            path.append(cur)
            n = K_apply(c, cur)
            if n == 0:
                cache[cur] = 0; break
            nxt = sorted_desc_digits(n, d)
            if nxt == cur:
                cache[cur] = n; break
            if nxt in path:
                cache[cur] = -1; break
            cur = nxt
        v = cache[cur]
        for p in path: cache[p] = v
        if v != F:
            return False
    return True

positions = list(range(d))
t0 = time.time()
n_partitions = 0
n_fixing_partitions = 0
universal_rules = []   # (partition, c, F)
fix_partitions = []
for A7 in itertools.combinations(positions, 2):
    rest1 = [p for p in positions if p not in A7]
    for A6 in itertools.combinations(rest1, 2):
        rest2 = [p for p in rest1 if p not in A6]
        for A4 in itertools.combinations(rest2, 2):
            A1 = tuple(p for p in rest2 if p not in A4)
            n_partitions += 1
            S7 = sum(E[p] for p in A7) - sum(E[p] for p in A1)
            S6 = sum(E[p] for p in A6) - sum(E[p] for p in A4)
            V = 6*S7 + 2*S6
            F = abs(V)
            if Counter(str(F).zfill(d)) != M2:
                continue
            n_fixing_partitions += 1
            fix_partitions.append((A7, A6, A4, A1, F))
            # enumerate 64 orderings
            for l7 in (0, 1):
                pair7 = list(zip(A7, (A1[l7], A1[1-l7])))
                for l6 in (0, 1):
                    pair6 = list(zip(A6, (A4[l6], A4[1-l6])))
                    co7 = [E[a] - E[b] for a, b in pair7]
                    co6 = [E[a] - E[b] for a, b in pair6]
                    for o7 in (0, 1):
                        r7 = (co7[o7], co7[1-o7])
                        for o6 in (0, 1):
                            r6 = (co6[o6], co6[1-o6])
                            for o4 in (0, 1):
                                r4 = (-co6[o4], -co6[1-o4])
                                for o1 in (0, 1):
                                    r1 = (-co7[o1], -co7[1-o1])
                                    c = r7 + r6 + r4 + r1
                                    if any(x == 0 for x in c):
                                        continue
                                    if universal_check(c, F):
                                        universal_rules.append({'partition': [list(A7), list(A6), list(A4), list(A1)],
                                                                'c': list(c), 'F': F})
print(f"partitions: {n_partitions}, M_2-fixing partitions: {n_fixing_partitions}")
print(f"universal pair-symmetric rules: {len(universal_rules)} ({time.time()-t0:.0f}s)")
Fs = Counter(r['F'] for r in universal_rules)
print(f"distinct universal fixed-point arrangements: {len(Fs)}")
print(f"fixed points by rule count (top 12): {Fs.most_common(12)}")
mono = [r for r in universal_rules
        if all(sum(r['c'][:j+1]) >= 0 for j in range(d))]
print(f"monotone universal rules: {len(mono)}")
json.dump(universal_rules, open('/tmp/kap60714/verify_fable/m2_pairsym_universals.json', 'w'))
print("saved m2_pairsym_universals.json")
