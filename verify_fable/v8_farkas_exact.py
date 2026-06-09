#!/usr/bin/env python3
"""Exact rational Farkas certificates for D=2..6.
Strategy: get HiGHS basic solution support, solve the restricted equality system
A[supp].T y = 0, sum y = 1 exactly with Fractions, check y >= 0.
"""
from fractions import Fraction
import numpy as np
from scipy.optimize import linprog

def next_state(p, q):
    n = 999*p + 90*q
    s = sorted((int(ch) for ch in str(n).zfill(4)), reverse=True)
    return (s[0]-s[3], s[1]-s[2])

states = [(p, q) for p in range(1, 10) for q in range(0, p+1)]
nonfp = [s for s in states if s != (6, 2)]

def exact_rows(D):
    monos = [(i, j) for i in range(D+1) for j in range(D+1-i)]
    rows = []
    for s in nonfp:
        t = next_state(*s)
        rows.append([Fraction(t[0]**i * t[1]**j - s[0]**i * s[1]**j) for (i, j) in monos])
    return rows, monos

def solve_exact(M, b):
    """Solve M x = b over rationals (least structured: Gaussian elim, M may be tall).
    Returns x or None."""
    m, n = len(M), len(M[0])
    A = [row[:] + [b[i]] for i, row in enumerate(M)]
    piv_cols = []
    r = 0
    for c in range(n):
        pr = None
        for i in range(r, m):
            if A[i][c] != 0: pr = i; break
        if pr is None: continue
        A[r], A[pr] = A[pr], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n+1)]
        piv_cols.append(c)
        r += 1
        if r == m: break
    # check consistency
    for i in range(r, m):
        if A[i][n] != 0: return None
    x = [Fraction(0)] * n
    for i, c in enumerate(piv_cols):
        x[c] = A[i][n]
    return x

for D in (2, 3, 4, 5, 6):
    rows, monos = exact_rows(D)
    nrows = len(rows)
    Af = np.array([[float(v) for v in row] for row in rows])
    A_eq = np.vstack([Af.T, np.ones(nrows)])
    b_eq = np.concatenate([np.zeros(len(monos)), [1.0]])
    res = linprog(np.zeros(nrows), A_eq=A_eq, b_eq=b_eq,
                  bounds=[(0, None)]*nrows, method='highs')
    if not res.success:
        print(f"D={D}: no float Farkas vector"); continue
    supp = [i for i, v in enumerate(res.x) if v > 1e-9]
    # exact system on support: columns = supp entries; equations: len(monos) zero-sums + sum=1
    M = [[rows[i][c] for i in supp] for c in range(len(monos))]
    M.append([Fraction(1)] * len(supp))
    b = [Fraction(0)] * len(monos) + [Fraction(1)]
    y = solve_exact(M, b)
    if y is None:
        print(f"D={D}: exact solve inconsistent on support {len(supp)}"); continue
    ok_nonneg = all(v >= 0 for v in y)
    # double-check combo exactly over ALL monomials
    combo_ok = all(sum(y[k] * rows[supp[k]][c] for k in range(len(supp))) == 0
                   for c in range(len(monos)))
    total = sum(y)
    if ok_nonneg and combo_ok and total == 1:
        print(f"D={D}: EXACT Farkas certificate, support size {len(supp)} "
              f"=> no degree-{D} Lyapunov (proven).")
        if D == 4:
            print("   support states & weights (state -> weight):")
            for k, i in enumerate(supp):
                if y[k] != 0:
                    print(f"     {nonfp[i]} -> {y[k]}")
    else:
        print(f"D={D}: exact check failed (nonneg={ok_nonneg}, combo={combo_ok})")
