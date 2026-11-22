#!/usr/bin/env python3
"""Half-swap rules universal in several small bases (complete census), then SAMPLED in large bases (2026-11-21).
Stage 2 is sampling of reduced states only: a survivor is "no failure found", not an all-base rule.
Usage: factor_allbase_sampled.py N "7,8,9,10,11,12,13,16" "22,31,50,97,200,640" [SAMPLES]
Writes factor/allbase_sampled_n{N}.tsv: slots, then the endpoint m in each base as a digit pattern."""
import sys, numpy as np
from factor_family import census
def run(a, n, b, rng, samples):
    H = (b - 1) // 2
    cur = np.sort(rng.integers(0, H + 1, size=(samples, n)), axis=1)
    # add structured states: few distinct values, extremes
    ext = [[0]*n, [0]*(n-1)+[1], [H-1]*n if b % 2 else [H]*n, [0]*(n-1)+[H], list(range(n))]
    cur = np.vstack([cur, np.sort(np.array(ext) % (H + 1), axis=1)])
    if b % 2: cur = cur[~(cur == H).all(axis=1)]
    last_m = None
    for it in range(4000):
        cur = np.unique(cur, axis=0)
        R = cur.shape[0]
        s = np.empty((R, 2*n), dtype=np.int64); s[:, :n] = b - 1 - cur; s[:, n:] = cur[:, ::-1]
        V = np.zeros(R, dtype=np.int64)
        for q in range(n): V += b**q * (s[:, a[2*q]] - s[:, a[2*q+1]])
        m = np.abs(V)
        if (m == 0).any(): return None
        N = m - 1; d = np.empty((R, n), dtype=np.int64)
        for q in range(n):
            x = N % b; N //= b; d[:, q] = np.minimum(x, b - 1 - x)
        d.sort(axis=1)
        if b % 2 and (d == H).all(axis=1).any(): return None
        if R == 1 and (d == cur).all(): return int(m[0])
        nu = np.unique(d, axis=0)
        if nu.shape == cur.shape and (nu == cur).all(): return None
        cur = nu
    return None
def pat(m, b, n):
    out = []
    for _ in range(n):
        d = m % b; m //= b
        out.append(str(d) if d <= 3 else ("b-%d" % (b - d) if b - d <= 4 else "[%d]" % d))
    return " ".join(out[::-1])
n = int(sys.argv[1]); small = list(map(int, sys.argv[2].split(','))); big = list(map(int, sys.argv[3].split(',')))
samples = int(sys.argv[4]) if len(sys.argv) > 4 else 2000
assert max(big) ** n < 2**62
surv = None
for b in small:
    res, _, _ = census(n, b); d = {a: m for m, a in res}
    surv = d if surv is None else {a: surv[a] for a in surv if a in d}
    print(f"base {b}: universal {len(d)}; in all so far {len(surv)}", flush=True)
rng = np.random.default_rng(3)
ends = {a: {} for a in surv}
for b in big:
    for a in list(ends):
        m = run(np.array(a), n, b, rng, samples)
        if m is None: del ends[a]
        else: ends[a][b] = m
    print(f"base {b} (sampled): no failure found for {len(ends)}", flush=True)
from collections import Counter
shapes = Counter(); out = open(f"factor/allbase_sampled_n{n}.tsv", "w")
for a, e in sorted(ends.items()):
    ps = [pat(e[b], b, n) for b in big]
    key = ps[0] if len(set(ps)) == 1 else "VARIES"
    shapes[key] += 1
    out.write(",".join(map(str, a)) + "\t" + key + "\t" + "\t".join(str(e[b]) for b in big) + "\n")
print(f"n={n}: survivors {len(ends)}; endpoint digit patterns {len(shapes)}")
dig = Counter()
for k, c in shapes.items():
    for t in k.split(): dig[t] += c
print("  digits used in endpoints m (pattern counts):", dict(dig))
for k, c in shapes.most_common(15): print(f"  m = {k}   rules {c}")
