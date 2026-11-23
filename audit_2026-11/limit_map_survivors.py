#!/usr/bin/env python3
"""Limit-map idea, second test (2026-11-22).  The 21,641 ten-digit factor-family rules with no failure found in
bases 7-13, 16 (complete) and 22, 31, 50, 97, 200, 640 (sampled) are sampled in ONE more base.
Prediction under test: cycles are rational orbits, so failures should concentrate in bases with many small
divisors (420, 2520, 315, 3465) and be rare in prime bases of similar size (419, 2521, 313, 3467).
Usage: limit_map_survivors.py BASE [SAMPLES]   -> limit_map/surv_bBASE.txt (slots of rules that FAIL, with a
witness state on a cycle or mapping to a bad value)."""
import sys, os, numpy as np
def run(a, n, b, rng, samples):
    """None if no failure found; else ('zero'|'rep'|'cycle', witness state)."""
    H = (b - 1) // 2
    cur = np.sort(rng.integers(0, H + 1, size=(samples, n)), axis=1)
    ext = [[0]*n, [0]*(n-1)+[1], [H-1]*n if b % 2 else [H]*n, [0]*(n-1)+[H], list(range(n))]
    cur = np.vstack([cur, np.sort(np.array(ext) % (H + 1), axis=1)])
    if b % 2: cur = cur[~(cur == H).all(axis=1)]
    for it in range(4000):
        cur = np.unique(cur, axis=0)
        R = cur.shape[0]
        s = np.empty((R, 2*n), dtype=np.int64); s[:, :n] = b - 1 - cur; s[:, n:] = cur[:, ::-1]
        V = np.zeros(R, dtype=np.int64)
        for q in range(n): V += b**q * (s[:, a[2*q]] - s[:, a[2*q+1]])
        m = np.abs(V)
        if (m == 0).any(): return 'zero', cur[m == 0][0]
        N = m - 1; d = np.empty((R, n), dtype=np.int64)
        for q in range(n):
            x = N % b; N //= b; d[:, q] = np.minimum(x, b - 1 - x)
        d.sort(axis=1)
        if b % 2 and (d == H).all(axis=1).any(): return 'rep', cur[(d == H).all(axis=1)][0]
        if R == 1 and (d == cur).all(): return None
        nu = np.unique(d, axis=0)
        if nu.shape == cur.shape and (nu == cur).all():
            return 'cycle', cur[~(d == cur).all(axis=1)][0]     # a state on a cycle (set is invariant, not all fixed)
        cur = nu
    return 'long', cur[0]
if __name__ == '__main__':
    b = int(sys.argv[1]); samples = int(sys.argv[2]) if len(sys.argv) > 2 else 1500; n = 5
    assert b ** n < 2 ** 62
    rules = [tuple(map(int, l.split('\t')[0].split(','))) for l in open('factor/allbase_sampled_n5.tsv')]
    rng = np.random.default_rng(b)
    os.makedirs('limit_map', exist_ok=True)
    kinds = {}
    with open(f'limit_map/surv_b{b}.txt', 'w') as out:
        for a in rules:
            r = run(np.array(a), n, b, rng, samples)
            if r is not None:
                kinds[r[0]] = kinds.get(r[0], 0) + 1
                out.write(",".join(map(str, a)) + "\t" + r[0] + "\t" + ",".join(map(str, r[1].tolist())) + "\n")
        out.write(f"# base {b}: {len(rules)} rules sampled ({samples} random states each); failures {sum(kinds.values())} {kinds}\n")
    print(f"base {b}: failures {sum(kinds.values())} of {len(rules)} {kinds}", flush=True)
