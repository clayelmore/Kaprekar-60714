#!/usr/bin/env python3
"""Verification battery 2:
- d=5 exhaustive full-variable census -> expect 33 universal fps; check 60714's native rule
  c=(9900,9,90,-9000,-999); check singletons 54 (sv_F=2) and 3753 (sv_F=4).
- d=5: no full-variable rule fixes padded 6174 (algebraic obstruction).
- d=6: all full-variable rules fixing padded 6174 -> best basin (expect 0.9686).
- d=6 exhaustive census -> expect 506 universal full-variable fps, with zero-count strata
  205/240/53/8 and digit-sum strata 8/156/244/96/2.
"""
import sys, itertools, time
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits, coefs_from_invs

def admissible_multisets(d):
    out = []
    for combo in itertools.combinations_with_replacement(range(9, -1, -1), d):
        if combo[0] == combo[-1]:
            continue
        cnt = Counter(combo)
        if max(cnt.values()) >= d - 1:
            continue
        out.append(combo)
    return out

def universal_fp_of_rule(c, d, A):
    """Return F if rule is universal for a single fp over A, else None. Early abort."""
    cache = {}
    theF = None
    for ms in A:
        path = []
        cur = ms
        while cur not in cache:
            path.append(cur)
            n = K_apply(c, cur)
            if n == 0:
                for p in path: cache[p] = 0
                return None
            nxt = sorted_desc_digits(n, d)
            if nxt == cur:
                for p in path: cache[p] = n
                break
            if nxt in path:
                for p in path: cache[p] = -1
                return None
            cur = nxt
        v = cache[cur]
        for p in path: cache[p] = v
        if v <= 0:
            return None
        if theF is None:
            theF = v
        elif v != theF:
            return None
    return theF

def census_fv(d):
    A = admissible_multisets(d)
    perms = list(itertools.permutations(range(d)))
    t0 = time.time()
    results = {}  # F -> list of c
    n_fv = 0
    for pi_inv in perms:
        for sigma_inv in perms:
            if all(pi_inv[i] != sigma_inv[i] for i in range(d)):
                c = coefs_from_invs(pi_inv, sigma_inv, d)
                n_fv += 1
                F = universal_fp_of_rule(c, d, A)
                if F is not None:
                    results.setdefault(F, []).append(c)
    print(f"d={d}: admissible={len(A)}, full-variable rules={n_fv}, "
          f"universal fps={len(results)}  ({time.time()-t0:.0f}s)")
    return results

print("=== d=5 exhaustive full-variable census ===")
r5 = census_fv(5)
fps5 = sorted(r5)
print(f"  the {len(fps5)} universal fps: {fps5}")
native = (9900, 9, 90, -9000, -999)
print(f"  60714 in list: {60714 in fps5}; native rule among its rules: {native in [tuple(c) for c in r5.get(60714, [])]}")
for F in (54, 3753):
    if F in r5:
        fd = sorted_desc_digits(F, 5)
        svFs = sorted({sum(1 for i in range(5) if c[i] != 0 and fd[i] != 0) for c in r5[F]})
        print(f"  F={F}: sorted={fd}, sv_F values over its universal rules: {svFs}")

print("\n=== d=5: full-variable rules fixing padded 6174 ===")
s6174_5 = sorted_desc_digits(6174, 5)
perms5 = list(itertools.permutations(range(5)))
nfix = 0
for pi_inv in perms5:
    for sigma_inv in perms5:
        if all(pi_inv[i] != sigma_inv[i] for i in range(5)):
            c = coefs_from_invs(pi_inv, sigma_inv, 5)
            if K_apply(c, s6174_5) == 6174:
                nfix += 1
print(f"  count of full-variable rules with K(sorted 06174)=6174: {nfix} (expect 0)")

print("\n=== d=6: full-variable rules fixing padded 6174, best basin ===")
A6 = admissible_multisets(6)
s6174_6 = sorted_desc_digits(6174, 6)
perms6 = list(itertools.permutations(range(6)))
fixers = []
for pi_inv in perms6:
    for sigma_inv in perms6:
        if all(pi_inv[i] != sigma_inv[i] for i in range(6)):
            c = coefs_from_invs(pi_inv, sigma_inv, 6)
            if K_apply(c, s6174_6) == 6174:
                fixers.append(c)
print(f"  fixers found: {len(fixers)} (distinct c: {len(set(fixers))})")
best = 0.0
for c in set(fixers):
    cache = {}
    nF = 0
    for ms in A6:
        path = []
        cur = ms
        while cur not in cache:
            path.append(cur)
            n = K_apply(c, cur)
            if n == 0:
                for p in path: cache[p] = 0
                break
            nxt = sorted_desc_digits(n, 6)
            if nxt == cur:
                for p in path: cache[p] = n
                break
            if nxt in path:
                for p in path: cache[p] = -1
                break
            cur = nxt
        v = cache[cur]
        for p in path: cache[p] = v
        if v == 6174: nF += 1
    frac = nF / len(A6)
    if frac > best: best = frac
print(f"  best basin fraction among fixers: {best:.4f} (expect 0.9686)")
