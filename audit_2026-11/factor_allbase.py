#!/usr/bin/env python3
"""Which half-swap (factor family) rules are universal in many bases, and what are their endpoints? (2026-11-21)

Stage 1: census (factor_family.census) in the small bases given; keep rules universal in all of them.
Stage 2: each survivor is checked on EVERY reduced state in the larger bases given (vectorized over states).
Endpoint m is printed as its base-b digit string so that a formula in b can be read off.

Caveat (odd bases): the reduced check does not test whether a FIRST image can be the repdigit ((b-1)/2)^(2n).
Usage: factor_allbase.py N "7,8,10,11,12,13,16" "22,31,50,97"
"""
import sys, itertools
import numpy as np
from factor_family import census, states

def check_rule_states(a, n, b, maxstates=3_000_000, seed=1):
    """Complete reduced check of one rule in base b (all states, or a random sample if too many).
    Returns (ok, m_endpoint or None, complete?)."""
    H = (b - 1) // 2
    from math import comb
    S = comb(H + n, n)
    complete = S <= maxstates
    if complete:
        st = np.array(list(itertools.combinations_with_replacement(range(H + 1), n)), dtype=np.int64)
    else:
        rng = np.random.default_rng(seed)
        st = np.sort(rng.integers(0, H + 1, size=(maxstates // 10, n)), axis=1)
    def step(rho):
        R = rho.shape[0]
        s = np.empty((R, 2 * n), dtype=np.int64)
        s[:, :n] = b - 1 - rho
        s[:, n:] = rho[:, ::-1]
        V = np.zeros(R, dtype=object) if b ** n > 2 ** 62 else np.zeros(R, dtype=np.int64)
        for q in range(n):
            V = V + (b ** q) * (s[:, a[2 * q]] - s[:, a[2 * q + 1]])
        m = np.abs(V)
        N = m - 1
        d = np.empty((R, n), dtype=np.int64)
        for q in range(n):
            x = N % b; N = N // b
            d[:, q] = np.minimum(x, b - 1 - x)
        d.sort(axis=1)
        return d, m
    cur = st
    rep = np.full(n, H) if b % 2 == 1 else None
    if rep is not None:
        cur = cur[~(cur == rep).all(axis=1)]
    seen_m = None
    for it in range(20000):
        cur = np.unique(cur, axis=0)
        nxt, m = step(cur)
        if (m == 0).any(): return False, None, complete
        if rep is not None and (nxt == rep).all(axis=1).any(): return False, None, complete
        if cur.shape[0] == 1 and (nxt == cur).all():
            return True, int(m[0]), complete
        nu = np.unique(nxt, axis=0)
        if nu.shape == cur.shape and (nu == cur).all():
            return False, None, complete           # a cycle or several fixed points
        cur = nu
    return False, None, complete

def digs(m, b, n):
    out = []
    for _ in range(n): out.append(m % b); m //= b
    return out[::-1]

def sym(d, b):
    if d <= 3: return str(d)
    if b - 1 - d <= 3: return "b-" + str(b - d)
    return f"[{d}]"

def main():
    n = int(sys.argv[1])
    small = [int(x) for x in sys.argv[2].split(',')]
    big = [int(x) for x in sys.argv[3].split(',')] if len(sys.argv) > 3 and sys.argv[3] else []
    surv = None; ends = {}
    for b in small:
        res, fixable, tot = census(n, b)
        d = {a: m for m, a in res}
        ends[b] = d
        surv = set(d) if surv is None else surv & set(d)
        print(f"base {b}: universal {len(d)}; still universal in all bases so far: {len(surv)}", flush=True)
    surv = sorted(surv)
    for b in big:
        keep = []; ends[b] = {}
        for a in surv:
            ok, m, comp = check_rule_states(np.array(a), n, b)
            if ok: keep.append(a); ends[b][a] = m
        surv = keep
        print(f"base {b}: survivors {len(surv)}", flush=True)
    allb = small + big
    from collections import defaultdict
    byshape = defaultdict(list)
    for a in surv:
        shapes = tuple(tuple(sym(x, b) for x in digs(ends[b][a], b, n)) for b in allb if b >= 10)
        key = shapes[0] if len(set(shapes)) == 1 else ("VARIES",) + tuple(ends[b][a] for b in allb)
        byshape[key].append(a)
    print(f"\nn={n}: rules universal in every base listed: {len(surv)}; endpoint shapes: {len(byshape)}")
    for k, v in sorted(byshape.items(), key=lambda kv: str(kv[0])):
        print("  m digits:", " ".join(map(str, k)), f"  rules={len(v)}  e.g. slots {v[0]}")

if __name__ == '__main__':
    main()
