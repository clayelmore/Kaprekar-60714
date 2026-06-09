#!/usr/bin/env python3
"""Verification battery 5: the base-case obstruction.
Gap system: states (p,q) = (a-d, b-c), 1<=p<=9, 0<=q<=p (54 states),
K = 999p + 90q, next state from sorted digits of K. Unique fp (6,2).
- verify state count, unique fixed point, acyclicity, max reaching time.
- LP feasibility of polynomial Lyapunov at degrees 2,3,4 (expect infeasible)
  and at degree 9 (expect feasible: interpolation threshold).
"""
import itertools
import numpy as np
from scipy.optimize import linprog

def next_state(p, q):
    n = 999*p + 90*q
    s = sorted((int(ch) for ch in str(n).zfill(4)), reverse=True)
    return (s[0]-s[3], s[1]-s[2])

states = [(p, q) for p in range(1, 10) for q in range(0, p+1)]
print(f"states: {len(states)} (expect 54)")
fps = [s for s in states if next_state(*s) == s]
print(f"fixed points: {fps} (expect [(6,2)])")
# closure check: image stays in state set
img_ok = all(next_state(*s) in states for s in states)
print(f"closed under map: {img_ok}")
# reaching times / acyclicity
rt = {}
for s in states:
    seen = []
    cur = s
    while cur != (6, 2):
        if cur in seen:
            print(f"CYCLE found at {s}!"); break
        seen.append(cur)
        cur = next_state(*cur)
    rt[s] = len(seen)
print(f"acyclic, max reaching time: {max(rt.values())}, fp reaching time {rt[(6,2)]}")
# image collapse sequence
I = set(states)
sizes = [len(I)]
while len(I) > 1:
    I = {next_state(*s) for s in I}
    sizes.append(len(I))
print(f"image collapse |I_k|: {sizes}")

def lyapunov_lp(D):
    monos = [(i, j) for i in range(D+1) for j in range(D+1-i)]
    rows = []
    for s in states:
        if s == (6, 2): continue
        t = next_state(*s)
        rows.append([t[0]**i * t[1]**j - s[0]**i * s[1]**j for (i, j) in monos])
    A_ub = np.array(rows, dtype=float)
    b_ub = -np.ones(len(rows))
    cvec = np.zeros(len(monos))
    bounds = [(None, None)] * len(monos)
    res = linprog(cvec, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')
    return res.success, len(monos)

for D in (2, 3, 4, 5, 6, 7, 8, 9):
    feas, nm = lyapunov_lp(D)
    print(f"degree {D} ({nm} monomials): {'FEASIBLE' if feas else 'infeasible'}")
