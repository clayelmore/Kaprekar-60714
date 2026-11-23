#!/usr/bin/env python3
"""For rules that fail in limit_map/surv_bBASE.txt with a cycle: follow the witness to its cycle, solve the
cycle equations with b symbolic (limit_map_cycle.step_itin), and report period, denominator of the solution,
and the limit orbit point.  Usage: limit_map_families.py BASE [MAXRULES]"""
import sys, sympy as sp
from collections import Counter
from limit_map_cycle import step_itin, step_direct
from factor_family import digits_of_state
B = sp.symbols('b')
def places_of(a, n):
    pl = [None] * (2 * n)
    for q in range(n):
        P, M = a[2 * q], a[2 * q + 1]
        pl[P] = (q + n, q); pl[M] = (q, q + n)
    return pl
def family(a, rho, n, b):
    pl = places_of(a, n); L = 2 * n
    s = tuple(digits_of_state(tuple(rho), b)); seen = {}
    while s not in seen:
        seen[s] = len(seen); s = step_direct(pl, s, b)
    per = len(seen) - seen[s]
    if per == 1: return None
    cyc = [s]
    for _ in range(per - 1): cyc.append(step_direct(pl, cyc[-1], b))
    # start from a point with the fewest ties
    cyc_sorted = sorted(range(per), key=lambda i: len(cyc[i]) - len(set(cyc[i])))
    i0 = cyc_sorted[0]; s = cyc[i0]; ties = len(s) - len(set(s))
    Ac = sp.eye(L); uc = sp.zeros(L, 1); wc = sp.zeros(L, 1)
    for _ in range(per):
        s, it, (A, u, w) = step_itin(pl, s, b)
        Ac, uc, wc = A * Ac, A * uc + u, A * wc + w
    Mx = sp.eye(L) - Ac
    if Mx.rank() < L: return per, None, None, ties, cyc[i0]
    sol = Mx.LUsolve(uc + B * wc)
    slope = [sp.Rational(sp.diff(e, B)) for e in sol]
    den = sp.ilcm(*[x.q for x in slope])
    exact = all(sol[i].subs(B, b) == cyc[i0][i] for i in range(L))
    return per, int(den), tuple(slope), ties, cyc[i0], exact
if __name__ == '__main__':
    b = int(sys.argv[1]); mx = int(sys.argv[2]) if len(sys.argv) > 2 else 10**9; n = 5
    rows = [l.rstrip('\n').split('\t') for l in open((sys.argv[3] if len(sys.argv)>3 else f'limit_map/surv_b{b}.txt')) if not l.startswith('#')]
    dens = Counter(); pers = Counter(); kinds = Counter(r[1] for r in rows); sing = 0; shown = 0
    for r in rows[:mx]:
        if r[1] != 'cycle': continue
        a = tuple(map(int, r[0].split(','))); rho = tuple(map(int, r[2].split(',')))
        f = family(a, rho, n, b)
        if f is None: continue
        pers[f[0]] += 1
        if f[1] is None: sing += 1; continue
        dens[f[1]] += 1
        if shown < 4:
            shown += 1
            print(f"  e.g. slots {r[0]} period {f[0]} denominator {f[1]} slopes {[str(x) for x in f[2]]} matches base-{b} point: {f[5]}")
    print(f"base {b}: failures by kind {dict(kinds)}; cycle periods {dict(sorted(pers.items()))}; "
          f"denominators of the b-slope {dict(sorted(dens.items()))}; singular systems {sing}")
