"""Checks for the cautionary section. Run from the repo root: /usr/bin/python3 theorem_paper/checks/caution_check.py"""
import sys
sys.path.insert(0, "audit_2026-11")
from usage_score import from_words, extend, coeffs

def words(places):
    L = len(places); w1 = [None]*L; w2 = [None]*L
    for letter, (p, q) in enumerate(places): w1[L-1-p] = chr(65+letter); w2[L-1-q] = chr(65+letter)
    return "".join(w1), "".join(w2)
def step(places, s, b):
    L = len(s); v = abs(sum(c*x for c, x in zip(coeffs(places, b), s)))
    return tuple(sorted(((v // b**i) % b for i in range(L)), reverse=True))

core = from_words("EABDFC", "DFCEAB"); r8 = extend(core, 8)
print("length-8 extension:", " - ".join(words(r8)))
s = (48, 45, 29, 21, 2, 1, 1, 0); cyc = [s]
while True:
    s = step(r8, s, 50)
    if s == cyc[0]: break
    cyc.append(s); assert len(cyc) < 50
print("base 50 cycle, period", len(cyc)); [print("  ", c) for c in cyc]

def fam(b):
    q = b // 5
    return (4*q-3, 3*q+7, 3*q+3, 2*q-6, 2*q-7, q+2, 1, 0)
ok = []
for b in list(range(55, 2001, 5)) + [2500, 10000, 100005]:
    s0 = fam(b); s = s0
    for _ in range(4): s = step(r8, s, b)
    per = None; t = s0
    for k in range(1, 5):
        t = step(r8, t, b)
        if t == s0: per = k; break
    ok.append(per == 4)
print("affine family: bases checked", len(ok), "all period 4:", all(ok))
# six-digit rule itself still universal at base 50 (complete enumeration)
import itertools
def universal(places, b):
    L = len(places); ends = set()
    for t in itertools.combinations_with_replacement(range(b-1, -1, -1), L):
        if t[0] == t[-1]: continue
        seen = set(); cur = t
        while cur not in seen:
            seen.add(cur); cur = step(places, cur, b)
        nxt = step(places, cur, b)
        if nxt != cur: return False
        ends.add(cur)
    return len(ends) == 1
print("six-digit rule universal at base 20:", universal(core, 20))

# corner cycle of a ten-digit half-swap rule: base-free in deficits
a = (1, 2, 9, 7, 4, 3, 5, 8, 0, 6); n = 5
pl = [None]*10
for q in range(n):
    P, M = a[2*q], a[2*q+1]; pl[P] = (q+n, q); pl[M] = (q, q+n)
print("corner rule:", " - ".join(words(pl)), " pairs (P_q, M_q), q=0..4:", [(a[2*q], a[2*q+1]) for q in range(n)])
def digs(rho, b): return tuple(sorted([b-1-r for r in rho] + list(rho), reverse=True))
def state(s, b): return tuple(sorted(min(x, b-1-x) for x in s))[:0] or tuple(sorted(s[n:]))
rho0 = (13, 13, 15, 25, 31); bad = []
for b in list(range(77, 1200)) + [100003, 1000003]:
    s = digs(rho0, b); orb = []
    for _ in range(3):
        s = step(pl, s, b); orb.append(tuple(sorted(s[n:])))
        assert tuple(sorted(b-1-x for x in s[:n])) == orb[-1]
    if orb != [(1, 1, 6, 17, 38), (4, 4, 18, 21, 36), rho0]: bad.append(b)
print("corner cycle identical in bases 77..1199, 100003, 1000003:", not bad, bad[:5])
# and the rule is universal in base 10 (complete enumeration of 10-digit multisets)
print("corner rule universal in base 10:", universal(pl, 10))
