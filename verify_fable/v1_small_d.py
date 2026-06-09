#!/usr/bin/env python3
"""Verification battery 1: small-d censuses.
- d=3: all 30 rules -> universal fixed points {45,450,495}, collapse rule count 6.
- d=4: 552 rules; full-variable (216) census -> universal fps {1746,2538,5382,6174};
  collapse rules 84; rule c=(0,0,9,-9) drains all admissible multisets to 0.
Conventions: admissible = non-repdigit, non-near-repdigit multisets (d<=6 census convention).
"""
import sys, itertools
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits, coefs_from_invs

def admissible_multisets(d, exclude_near=True):
    out = []
    for combo in itertools.combinations_with_replacement(range(9, -1, -1), d):
        if combo[0] == combo[-1]:
            continue  # repdigit
        if exclude_near:
            cnt = Counter(combo)
            if max(cnt.values()) >= d - 1:
                continue  # near-repdigit (one digit d-1 times)
        out.append(combo)
    return out

def trace(ms, c, d, cache, max_iters=200):
    path = []
    cur = ms
    while True:
        if cur in cache:
            res = cache[cur]
            for p in path: cache[p] = res
            return res
        path.append(cur)
        n = K_apply(c, cur)
        if n == 0:
            res = ('zero', 0)
            for p in path: cache[p] = res
            return res
        nxt = sorted_desc_digits(n, d)
        if nxt == cur:
            res = ('fp', n)
            for p in path: cache[p] = res
            return res
        if nxt in path:  # cycle (path is short; fine)
            res = ('cycle', n)
            for p in path: cache[p] = res
            return res
        cur = nxt

def census(d, exclude_near=True, full_variable_only=False):
    A = admissible_multisets(d, exclude_near)
    print(f"d={d}: admissible multisets = {len(A)} (exclude_near={exclude_near})")
    perms = list(itertools.permutations(range(d)))
    universal_fps = set()
    collapse_rules = 0
    n_rules = 0
    n_fv = 0
    for pi_inv in perms:
        for sigma_inv in perms:
            if pi_inv == sigma_inv: continue
            c = coefs_from_invs(pi_inv, sigma_inv, d)
            fv = all(x != 0 for x in c)
            n_rules += 1
            if fv: n_fv += 1
            if full_variable_only and not fv:
                continue
            cache = {}
            kinds = Counter()
            fps = Counter()
            for ms in A:
                kind, val = trace(ms, c, d, cache)
                kinds[kind] += 1
                if kind == 'fp': fps[val] += 1
            if kinds['zero'] == len(A):
                collapse_rules += 1
            # universal: every admissible multiset reaches a single fp F
            if len(fps) == 1 and kinds['fp'] == len(A):
                F = next(iter(fps))
                universal_fps.add((F, c))
    print(f"  total rules = {n_rules}, full-variable = {n_fv}")
    print(f"  collapse rules (all -> 0) = {collapse_rules}")
    ufp_values = sorted(set(F for F, c in universal_fps))
    print(f"  universal fixed-point values = {ufp_values}")
    return universal_fps, collapse_rules

print("=== d=3, all rules ===")
u3, col3 = census(3, exclude_near=True, full_variable_only=False)
for F, c in sorted(u3):
    sv = sum(1 for x in c if x != 0)
    fd = sorted_desc_digits(F, 3)
    svF = sum(1 for i in range(3) if c[i] != 0 and fd[i] != 0)
    print(f"   F={F} c={c} sv={sv} sv_F={svF}")

print("\n=== d=4, all rules ===")
u4, col4 = census(4, exclude_near=True, full_variable_only=False)
fv_universals = sorted(set(F for F, c in u4 if all(x != 0 for x in c)))
print(f"  full-variable universal fps at d=4: {fv_universals}")

print("\n=== L0 witness at d=4: c=(0,0,9,-9) ===")
A4 = admissible_multisets(4, exclude_near=True)
c0 = (0, 0, 9, -9)
cache = {}
kinds = Counter(trace(ms, c0, 4, cache)[0] for ms in A4)
print(f"  over {len(A4)} admissible multisets: {dict(kinds)}")
