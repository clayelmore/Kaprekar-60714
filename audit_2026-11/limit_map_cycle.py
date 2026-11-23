#!/usr/bin/env python3
"""Itinerary test for a cycle of a rule (2026-11-22, limit-map idea, first test).

A rule is a list of (place in word 1, place in word 2) per sorted letter.  One step from sorted digits s:
  d_p = s[letter at place p of word 1] - s[letter at place p of word 2],  V = sum b^p d_p,  sigma = sign V,
  digit y_p = sigma d_p - beta_p + b beta_{p+1}   (beta = borrows, beta_0 = 0),  then sort descending (perm pi).
With (sigma, beta, pi) held fixed the step is affine:  s' = A s + u + b w,  A an integer matrix.
Around a cycle:  (I - A_c) s = u_c + b w_c.  Solve with b symbolic, then find the bases where the solution is
integral and keeps the same itinerary, and confirm each by direct iteration.

Usage: limit_map_cycle.py            (the length-8 extension of EABDFC - DFCEAB and its base-50 4-cycle)
"""
import sys
import sympy as sp
from usage_score import from_words, extend, coeffs

def step_direct(places, s, b):
    L = len(s); c = coeffs(places, b)
    v = abs(sum(x * y for x, y in zip(c, s)))
    return tuple(sorted(((v // b ** i) % b for i in range(L)), reverse=True))

def step_itin(places, s, b):
    """Returns (next sorted digits, (sigma, beta, pi), (A, u, w)) with next = A s + u + b w."""
    L = len(s)
    w1 = [None] * L; w2 = [None] * L
    for letter, (p, q) in enumerate(places): w1[p] = letter; w2[q] = letter
    d = [s[w1[p]] - s[w2[p]] for p in range(L)]
    V = sum(b ** p * d[p] for p in range(L))
    sigma = 1 if V > 0 else -1
    beta = [0] * (L + 1); y = [0] * L
    for p in range(L):
        t = sigma * d[p] - beta[p]
        beta[p + 1] = 1 if t < 0 else 0
        y[p] = t + b * beta[p + 1]
    assert beta[L] == 0 and all(0 <= x < b for x in y)
    pi = sorted(range(L), key=lambda p: (-y[p], p))          # place of the i-th largest digit
    A = sp.zeros(L, L); u = sp.zeros(L, 1); w = sp.zeros(L, 1)
    for i, p in enumerate(pi):
        A[i, w1[p]] += sigma; A[i, w2[p]] -= sigma
        u[i] = -beta[p]; w[i] = beta[p + 1]
    nxt = tuple(y[p] for p in pi)
    return nxt, (sigma, tuple(beta), tuple(pi)), (A, u, w)

def analyze(places, start, b0, label):
    L = len(start); B = sp.symbols('b')
    print(f"== {label}: length {L}, cycle found at base {b0}")
    s = tuple(start); cyc = [s]; itins = []; maps = []
    while True:
        nxt, it, m = step_itin(places, s, b0)
        assert nxt == step_direct(places, s, b0)
        itins.append(it); maps.append(m)
        if nxt == cyc[0]: break
        cyc.append(nxt); s = nxt
        assert len(cyc) < 1000
    k = len(cyc)
    print(f"period {k}"); [print("  ", c) for c in cyc]
    Ac = sp.eye(L); uc = sp.zeros(L, 1); wc = sp.zeros(L, 1)
    for A, u, w in maps:
        Ac, uc, wc = A * Ac, A * uc + u, A * wc + w
    Mx = sp.eye(L) - Ac
    print(f"rank of I - A_cycle: {Mx.rank()} of {L};  rank of A_cycle: {Ac.rank()}")
    xs = sp.symbols(f'x0:{L}')
    sol = sp.linsolve((Mx, uc + B * wc), *xs)
    sol = list(sol)
    if not sol: print("no solution for general b"); return
    s_b = sp.Matrix(sol[0])
    free = s_b.free_symbols - {B}
    print(f"free parameters: {len(free)}")
    print("cycle point as a function of b:")
    for i in range(L): print(f"   s{i} = {sp.factor(s_b[i])}")
    print("limit s/b as b -> infinity:", [sp.limit(e / B, B, sp.oo) for e in s_b] if not free else "n/a")
    if free: return
    # bases where this solution is integral and follows the same itinerary: test directly
    good = []
    for b in range(3, 2001):
        pt = [e.subs(B, b) for e in s_b]
        if any(not x.is_integer for x in pt): continue
        pt = tuple(int(x) for x in pt)
        if not (b - 1 >= pt[0] and all(pt[i] >= pt[i + 1] for i in range(L - 1)) and pt[-1] >= 0): continue
        s = pt; ok = True
        for j in range(k):
            try: nxt, it, _ = step_itin(places, s, b)
            except AssertionError: ok = False; break
            if it != itins[j] or nxt != step_direct(places, s, b): ok = False; break
            s = nxt
        if ok and s == pt: good.append(b)
    print(f"bases 3..2000 where the SAME itinerary gives a true {k}-cycle: {len(good)}")
    print("   ", good[:40], "..." if len(good) > 40 else "")
    if len(good) > 2:
        diffs = sorted({good[i + 1] - good[i] for i in range(len(good) - 1)})
        print("    differences between consecutive such bases:", diffs[:10])
    return good, s_b

if __name__ == '__main__':
    core = from_words("EABDFC", "DFCEAB")
    r8 = extend(core, 8)
    analyze(r8, (48, 45, 29, 21, 2, 1, 1, 0), 50, "length-8 extension of EABDFC - DFCEAB")
