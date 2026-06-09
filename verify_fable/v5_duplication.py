#!/usr/bin/env python3
"""Verification battery 4: the duplication chain {1,4,6,7}^m.
- interleaved rule c at m: ranks of block X in {7,6,4,1} get coefficient
  gamma_X * 10^(4*(m-1-j)) for j=0..m-1  (fold of classical (999,90,-90,-999)).
- check m=1 -> classical; F_m fixed for m=1..8; monotone partial sums m<=8.
- basins of F_m at m=2 (d=8) and m=3 (d=12), non-repdigit convention;
  also full fixed-point inventory of interleaved at d=12 (expect 2: 617461746174, 535549955994).
- folding identity: K'(X^k) = (K(X))^k as multisets, random tests.
- fixed-value formula V = 6*S7 + 2*S6 = 4*C_{m-1} + 2*C_{2m-1} on random pair-symmetric rules.
- witness digit-multiset checks for m=3..6 witnesses.
"""
import sys, itertools, random
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits

GAMMA = (999, 90, -90, -999)

def interleaved_c(m):
    c = []
    for X in range(4):  # blocks 7,6,4,1
        for j in range(m):
            c.append(GAMMA[X] * 10**(4*(m-1-j)))
    return tuple(c)

def non_repdigit_multisets(d):
    return [combo for combo in itertools.combinations_with_replacement(range(9,-1,-1), d)
            if combo[0] != combo[-1]]

print("=== interleaved rule basics ===")
print(f"m=1 c: {interleaved_c(1)} (expect (999,90,-90,-999))")
for m in range(1, 9):
    d = 4*m
    c = interleaved_c(m)
    s = tuple([7]*m + [6]*m + [4]*m + [1]*m)
    Fm = int('6174'*m)
    v = K_apply(c, s)
    mono = all(sum(c[:j+1]) >= 0 for j in range(d))
    print(f"  m={m}: K(sorted M_m)={'F_m OK' if v == Fm else ('FAIL: '+str(v))}, monotone C_j>=0: {mono}")

for m in (2, 3):
    d = 4*m
    c = interleaved_c(m)
    Fm = int('6174'*m)
    A = non_repdigit_multisets(d)
    cache = {}
    term = Counter()
    fps = Counter()
    for ms in A:
        path = []
        cur = ms
        while cur not in cache:
            path.append(cur)
            n = K_apply(c, cur)
            if n == 0:
                for p in path: cache[p] = ('zero', 0); break
            nxt = sorted_desc_digits(n, d)
            if nxt == cur:
                for p in path: cache[p] = ('fp', n)
                break
            if nxt in path:
                for p in path: cache[p] = ('cycle', min(K_apply(c, x) for x in path[path.index(nxt):]))
                break
            cur = nxt
        res = cache[cur]
        for p in path: cache[p] = res
        term[res[0]] += 1
        if res[0] == 'fp': fps[res[1]] += 1
    basin = fps.get(Fm, 0) / len(A)
    print(f"\n=== interleaved m={m} (d={d}): {len(A)} non-repdigit multisets ===")
    print(f"  terminals: {dict(term)}")
    print(f"  fixed points reached: {dict(fps)}")
    print(f"  basin of F_{m}={Fm}: {basin:.4f}")
    if m == 3:
        # full fixed-point inventory: check every multiset for K(ms) == ms
        all_fps = []
        for ms in A:
            n = K_apply(c, ms)
            if n != 0 and sorted_desc_digits(n, d) == ms:
                all_fps.append(n)
        print(f"  ALL fixed points of interleaved at d=12: {sorted(all_fps)}")

print("\n=== folding identity (random tests) ===")
random.seed(7)
def fold_c(c0, d0, k):
    cp = []
    for g in c0:
        for j in range(k):
            cp.append(g * 10**(d0*(k-1-j)))
    return tuple(cp)

for trial in range(5):
    d0 = random.choice([4, 5, 8])
    pi = list(range(d0)); sigma = list(range(d0))
    while True:
        random.shuffle(pi); random.shuffle(sigma)
        if all(pi[i] != sigma[i] for i in range(d0)): break
    from search_multiset_universals_fast import coefs_from_invs
    c0 = coefs_from_invs(tuple(pi), tuple(sigma), d0)
    k = random.choice([2, 3])
    cp = fold_c(c0, d0, k)
    X = sorted(random.choices(range(10), k=d0), reverse=True)
    while X[0] == X[-1]:
        X = sorted(random.choices(range(10), k=d0), reverse=True)
    Xk = tuple(sorted([x for x in X for _ in range(k)], reverse=True))
    KX = K_apply(c0, tuple(X))
    KXk = K_apply(cp, Xk)
    lhs = sorted_desc_digits(KXk, d0*k)
    rhs = tuple(sorted([dgt for dgt in sorted_desc_digits(KX, d0) for _ in range(k)], reverse=True))
    print(f"  d0={d0} k={k}: K'(X^{k}) multiset == (K(X))^{k} multiset: {lhs == rhs}")

print("\n=== fixed-value formula on random pair-symmetric rules (m=3) ===")
m = 3; d = 12
for trial in range(5):
    pos = list(range(d)); random.shuffle(pos)
    A7, A6, A4, A1 = pos[:3], pos[3:6], pos[6:9], pos[9:]
    E = lambda p: 10**(d-1-p)
    # random pairings and assignments
    l7 = random.sample(A1, 3); l6 = random.sample(A4, 3)
    c = [0]*d
    seven = [E(A7[i]) - E(l7[i]) for i in range(3)]
    six = [E(A6[i]) - E(l6[i]) for i in range(3)]
    random.shuffle(seven); random.shuffle(six)
    negf = [-x for x in seven]; negs = [-x for x in six]
    random.shuffle(negf); random.shuffle(negs)
    c = tuple(seven + six + negs + negf)
    S7 = sum(E(p) for p in A7) - sum(E(p) for p in A1)
    S6 = sum(E(p) for p in A6) - sum(E(p) for p in A4)
    s = tuple([7]*3 + [6]*3 + [4]*3 + [1]*3)
    V = sum(ci*si for ci, si in zip(c, s))
    C = [sum(c[:j+1]) for j in range(d)]
    f1 = 6*S7 + 2*S6
    f2 = 4*C[m-1] + 2*C[2*m-1]
    print(f"  K_lin(sorted M_3)={V}, 6S7+2S6={f1}, 4C_(m-1)+2C_(2m-1)={f2}, "
          f"pivot C_(m-1)==C_(3m-1): {C[m-1] == C[3*m-1]}, all equal: {V == f1 == f2}")

print("\n=== witness digit multisets ===")
W = {3: 666141417774, 4: 6614617774614174, 5: 14617461774617461746, 6: 666174141466617777741414}
for m, w in W.items():
    cnt = Counter(str(w))
    ok = all(cnt[ch] == m for ch in '1467') and set(cnt) == set('1467')
    print(f"  m={m}: {w} is arrangement of M_{m}: {ok}")
