"""Every sorted (2n+1)-digit string in base b: direct rule M_n (word1 - word2 on digit strings).
Checks: non-repdigits reach F=(b-1)(b^(n+1)-1), F fixed, repdigits -> 0, step bounds."""
import sys, time
from itertools import combinations_with_replacement
import rule

def bound(n, b):
    if n % 2 == 1: return b / 2 + 3
    if n == 4: return b + 2
    return b / 2 + 5

def run(n, b):
    L = 2 * n + 1
    step = rule.make_step(n, b)
    F = (b - 1) * (b ** (n + 1) - 1)
    Fd = []
    v = F
    for _ in range(L): Fd.append(v % b); v //= b
    Fs = tuple(sorted(Fd, reverse=True))
    nxt, val = step(Fs)
    assert val == F and nxt == Fs, "F not fixed"
    # g[c] = number of steps from multiset c until the produced VALUE equals F
    g = {}
    worst = 0; count = 0
    for c in combinations_with_replacement(range(b - 1, -1, -1), L):
        count += 1
        if c[0] == c[-1]:
            _, val = step(c)
            assert val == 0, ("repdigit", c)
            continue
        path = []
        cur = c
        while cur not in g:
            nx, val = step(cur)
            if val == 0:
                raise SystemExit(f"non-repdigit maps to 0: n={n} b={b} {cur}")
            if val == F:
                g[cur] = 1; break
            path.append(cur)
            if len(path) > 10 * b + 50:
                raise SystemExit(f"NO CONVERGENCE n={n} b={b} start={c}")
            cur = nx
        d = g[cur]
        for s_ in reversed(path):
            d += 1; g[s_] = d
        worst = max(worst, g[c])
    ok = worst <= bound(n, b)
    return count, worst, ok

if __name__ == "__main__":
    n = int(sys.argv[1]); bases = [int(x) for x in sys.argv[2].split(",")]
    for b in bases:
        t = time.time()
        cnt, worst, ok = run(n, b)
        print(f"n={n} L={2*n+1} b={b}: {cnt} strings, max steps to F={worst}, bound={bound(n,b)}, {'OK' if ok else 'VIOLATION'} ({time.time()-t:.1f}s)", flush=True)
