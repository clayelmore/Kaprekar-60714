#!/usr/bin/env python3
"""d=6 exhaustive full-variable census. Expect 506 universal fps,
zero-count strata 205/240/53/8, digit-sum strata 8/156/244/96/2,
all digit sums divisible by 9."""
import sys, itertools, time, json
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits, coefs_from_invs

def admissible_multisets(d):
    out = []
    for combo in itertools.combinations_with_replacement(range(9, -1, -1), d):
        if combo[0] == combo[-1]: continue
        cnt = Counter(combo)
        if max(cnt.values()) >= d - 1: continue
        out.append(combo)
    return out

def universal_fp_of_rule(c, d, A):
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
        if v <= 0: return None
        if theF is None: theF = v
        elif v != theF: return None
    return theF

d = 6
A = admissible_multisets(d)
perms = list(itertools.permutations(range(d)))
t0 = time.time()
fps = set()
n_fv = 0
for pi_inv in perms:
    for sigma_inv in perms:
        if all(pi_inv[i] != sigma_inv[i] for i in range(d)):
            n_fv += 1
            c = coefs_from_invs(pi_inv, sigma_inv, d)
            F = universal_fp_of_rule(c, d, A)
            if F is not None:
                fps.add(F)
print(f"d=6: admissible={len(A)}, fv rules={n_fv}, universal fps={len(fps)} ({time.time()-t0:.0f}s)")
zc = Counter(str(F).zfill(6).count('0') for F in fps)
ds = Counter(sum(int(ch) for ch in str(F)) for F in fps)
print(f"zero-count strata: {dict(sorted(zc.items()))}")
print(f"digit-sum strata: {dict(sorted(ds.items()))}")
print(f"all digit sums div by 9: {all(s % 9 == 0 for s in ds)}")
print(f"60714 padded present: {60714 in fps}")
json.dump(sorted(fps), open('/tmp/kap60714/verify_fable/d6_universals.json', 'w'))
