#!/usr/bin/env python3
"""Corner scan (2026-11-23).  For half-swap rules, states with small deficits (digits within a bounded distance of
b-1 and 0) move by a map that does not depend on b once b is large.  A cycle found there with largest deficit d
is a cycle in every base b >= 2d+1 (checked on examples, not proved in general).
For each of the 21,641 ten-digit rules: SAMPLES random states with deficits <= D (D from 8..128) in base 4001;
300 vectorized steps, then every remaining state is followed singly.
Usage: limit_map_micro.py SHARD NSHARDS [SAMPLES]  -> limit_map/micro_SHARD.txt
Line: slots, period, largest deficit on the cycle, one cycle state.  Period 0 = unresolved, -1 = two fixed states."""
import sys, numpy as np
b = 4001; n = 5; H = (b - 1) // 2
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
if __name__ == '__main__':
    sh = int(sys.argv[1]); ns = int(sys.argv[2]); samples = int(sys.argv[3]) if len(sys.argv) > 3 else 4000
    rules = [tuple(map(int, l.split('\t')[0].split(','))) for l in open('factor/allbase_sampled_n5.tsv')][sh::ns]
    rng = np.random.default_rng(1000 + sh); nbad = 0
    with open(f'limit_map/micro_{sh}.txt', 'w') as out:
        for a in rules:
            D = rng.choice([8, 16, 32, 64, 128], size=(samples, 1))
            cur = np.sort((rng.random((samples, n)) * (D + 1)).astype(np.int64), axis=1)
            aa = np.array(a)
            for _ in range(300): cur = np.unique(step_np(aa, cur), axis=0)
            ends = set(); res = None
            for rho in map(tuple, cur.tolist()):
                seen = {}; k = 0
                while rho not in seen and k < 200000:
                    seen[rho] = k; k += 1; rho = step(a, rho)
                if rho not in seen: res = (0, max(rho), rho); break
                p = k - seen[rho]
                if p > 1:
                    cyc = [rho]
                    for _ in range(p - 1): cyc.append(step(a, cyc[-1]))
                    res = (p, max(max(c) for c in cyc), min(cyc)); break
                ends.add(rho)
            if res is None and len(ends) > 1: res = (-1, max(max(e) for e in ends), min(ends))
            if res:
                nbad += 1
                out.write(",".join(map(str, a)) + f"\t{res[0]}\t{res[1]}\t{','.join(map(str, res[2]))}\n"); out.flush()
        out.write(f"# shard {sh}/{ns}: rules {len(rules)}, flagged {nbad}\n")
    print(f"shard {sh}: rules {len(rules)}, flagged {nbad}", flush=True)
