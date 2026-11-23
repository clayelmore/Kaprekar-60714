#!/usr/bin/env python3
"""Rules flagged 'long' in limit_map/surv_bBASE.txt (state set still changing after 4000 steps) (2026-11-23).
Re-sample states, advance 4000 steps, then follow every remaining state one at a time until it repeats.
Reports per base: how many rules end at one fixed state after a slow descent, and how many have a cycle.
Usage: limit_map_long.py BASE [SAMPLES]"""
import sys, numpy as np
from collections import Counter
b = int(sys.argv[1]); samples = int(sys.argv[2]) if len(sys.argv) > 2 else 1500; n = 5
H = (b - 1) // 2
def step_np(a, cur):
    R = cur.shape[0]
    s = np.empty((R, 2*n), dtype=np.int64); s[:, :n] = b - 1 - cur; s[:, n:] = cur[:, ::-1]
    V = np.zeros(R, dtype=np.int64)
    for q in range(n): V += b**q * (s[:, a[2*q]] - s[:, a[2*q+1]])
    N = np.abs(V) - 1; d = np.empty((R, n), dtype=np.int64)
    for q in range(n):
        x = N % b; N //= b; d[:, q] = np.minimum(x, b - 1 - x)
    d.sort(axis=1); return d
def step(a, rho):
    s = [0] * (2 * n)
    for i, r in enumerate(rho): s[i] = b - 1 - r; s[2 * n - 1 - i] = r
    m = abs(sum(b ** q * (s[a[2 * q]] - s[a[2 * q + 1]]) for q in range(n)))
    N = m - 1; d = []
    for _ in range(n): x = N % b; N //= b; d.append(min(x, b - 1 - x))
    return tuple(sorted(d))
rng = np.random.default_rng(b + 1)
res = Counter(); extra = []; cycs = []
for l in open(f'limit_map/surv_b{b}.txt'):
    if l.startswith('#'): continue
    a = tuple(map(int, l.split('\t')[0].split(',')))
    cur = np.sort(rng.integers(0, H + 1, size=(samples, n)), axis=1)
    cur = np.vstack([cur, np.sort(np.array([[0]*n, [0]*(n-1)+[1], [0]*(n-1)+[H], list(range(n))]) % (H+1), axis=1)])
    if b % 2: cur = cur[~(cur == H).all(axis=1)]
    for _ in range(4000): cur = np.unique(step_np(np.array(a), cur), axis=0)
    ends = set(); worst = 0; per = 0
    for rho in map(tuple, cur.tolist()):
        seen = {}; k = 0
        while rho not in seen and k < 3_000_000:
            seen[rho] = k; k += 1; rho = step(a, rho)
        if rho not in seen: per = -1; break
        p = k - seen[rho]
        if p > 1: per = p; break
        ends.add(rho); worst = max(worst, k - 1)
    if per > 1: res['cycle'] += 1; cycs.append((per, l.split('\t')[0], rho))
    elif per == -1: res['unresolved after 3,000,000 steps'] += 1
    elif len(ends) == 1: res['one fixed state, slow'] += 1; extra.append(worst)
    else: res['several fixed states'] += 1
extra.sort()
print(f"base {b}: {dict(res)}; extra steps beyond 4000 (slow ones): "
      f"{'min %d median %d max %d' % (extra[0], extra[len(extra)//2], extra[-1]) if extra else '-'}")
open(f"limit_map/cycles_b{b}.txt","w").write("".join(f"{c[1]}\tcycle\t{','.join(map(str,c[2]))}\t{c[0]}\n" for c in cycs))
