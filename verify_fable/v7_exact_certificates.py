#!/usr/bin/env python3
"""Exact certificates for the base-case proposition.
1) Farkas infeasibility certificate for degrees 2..6: find y>=0, A^T y = 0, sum(y)=1,
   then verify in exact rational arithmetic -> proves NO Lyapunov of that degree.
2) Degree-7 Lyapunov: take LP solution, rationalize, verify all 53 strict decreases exactly.
"""
import itertools
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

def next_state(p, q):
    n = 999*p + 90*q
    s = sorted((int(ch) for ch in str(n).zfill(4)), reverse=True)
    return (s[0]-s[3], s[1]-s[2])

states = [(p, q) for p in range(1, 10) for q in range(0, p+1)]

def build_A(D):
    monos = [(i, j) for i in range(D+1) for j in range(D+1-i)]
    rows = []
    for s in states:
        if s == (6, 2): continue
        t = next_state(*s)
        rows.append([t[0]**i * t[1]**j - s[0]**i * s[1]**j for (i, j) in monos])
    return np.array(rows, dtype=float), monos

print("=== Farkas certificates (exact) for degrees 2..6 ===")
for D in (2, 3, 4, 5, 6):
    A, monos = build_A(D)
    nrows = A.shape[0]
    # find y >= 0, A^T y = 0, 1^T y = 1
    A_eq = np.vstack([A.T, np.ones(nrows)])
    b_eq = np.concatenate([np.zeros(len(monos)), [1.0]])
    res = linprog(np.zeros(nrows), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, None)]*nrows, method='highs')
    if not res.success:
        print(f"  D={D}: no Farkas vector found (unexpected)"); continue
    y = res.x
    # rationalize: scale, round, verify exactly
    # exact rows as Fractions
    Aex = []
    for s in states:
        if s == (6, 2): continue
        t = next_state(*s)
        Aex.append([Fraction(t[0]**i * t[1]**j - s[0]**i * s[1]**j) for (i, j) in monos])
    verified = False
    for scale in (10**6, 10**8, 10**10, 10**12):
        yr = [Fraction(round(v * scale), scale) for v in y]
        yr = [max(v, Fraction(0)) for v in yr]
        tot = sum(yr)
        if tot == 0: continue
        combo = [sum(yr[r] * Aex[r][c] for r in range(nrows)) for c in range(len(monos))]
        if all(v == 0 for v in combo):
            verified = True
            break
    if verified:
        print(f"  D={D}: EXACT Farkas certificate verified (y>=0, sum>0, A^T y = 0) "
              f"=> 0 <= -sum(y) contradiction => LP infeasible => no degree-{D} Lyapunov.")
    else:
        # fall back: exact rational Farkas via integer null-space search is overkill;
        # report float-level only
        resid = np.abs(A.T @ y).max()
        print(f"  D={D}: float Farkas residual {resid:.2e}; exact rounding failed "
              f"(claim stands numerically, flag as not exactly certified)")

print("\n=== Degree-7 Lyapunov: exact verification ===")
D = 7
A, monos = build_A(D)
res = linprog(np.zeros(len(monos)), A_ub=A, b_ub=-np.ones(A.shape[0]),
              bounds=[(None, None)]*len(monos), method='highs')
print(f"  LP feasible: {res.success}")
if res.success:
    w = res.x
    margins = A @ w
    print(f"  float max margin: {margins.max():.6f} (need < 0)")
    # rationalize and verify exactly
    for scale in (10**6, 10**8, 10**10):
        wr = [Fraction(round(v * scale), scale) for v in w]
        ok = True
        worst = None
        for s in states:
            if s == (6, 2): continue
            t = next_state(*s)
            val = sum(wr[k] * Fraction(t[0]**i * t[1]**j - s[0]**i * s[1]**j)
                      for k, (i, j) in enumerate(monos))
            if worst is None or val > worst: worst = val
            if val >= 0: ok = False
        if ok:
            print(f"  EXACT: rational degree-7 polynomial with strict decrease at all 53 "
                  f"non-fixed states verified (worst margin {float(worst):.4f}, scale {scale}).")
            break
    else:
        print("  exact rationalization failed at tried scales")
