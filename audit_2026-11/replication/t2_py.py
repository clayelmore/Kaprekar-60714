"""Pure-Python T2 (independent cross-check of phi_check.c) for one core.

Usage: python3 t2_py.py [a0..a5 b0..b5 TARGET]
"""
import sys

from kap import phi, check_core


def run(a, b, target):
    check_core(a, b)
    tgt = tuple(sorted((int(c) for c in target), reverse=True))
    memo = {tgt: 0, (): -1}
    nseeds = nfail = 0
    maxsteps = 0
    maxsize = 0
    fails = []
    def comps(n, rem):
        if n == 0:
            yield ()
            return
        for k in range(rem + 1):
            for rest in comps(n - 1, rem - k):
                yield (k,) + rest

    for c in comps(8, 15):
        s18 = sum(c)
        base = []
        for dgt in range(8, 0, -1):
            base += [dgt] * c[dgt - 1]
        for c9 in range(6):
            if s18 == 0 and c9 == 0:
                continue
            seed = tuple([9] * c9 + base)
            nseeds += 1
            maxsize = max(maxsize, len(seed))
            path = []
            onpath = set()
            x = seed
            while x not in memo and x not in onpath:
                onpath.add(x)
                path.append(x)
                x = phi(a, b, x)
                maxsize = max(maxsize, len(x))
            r = memo.get(x, -1)  # if on path (cycle) -> -1
            for y in reversed(path):
                r = r + 1 if r >= 0 else -1
                memo[y] = r
            if memo[seed] < 0:
                nfail += 1
                if len(fails) < 10:
                    fails.append((seed, x))
            else:
                maxsteps = max(maxsteps, memo[seed])
    return nseeds, nfail, maxsteps, maxsize, len(memo), fails


if __name__ == '__main__':
    if len(sys.argv) > 1:
        v = list(map(int, sys.argv[1:13]))
        a, b, t = tuple(v[:6]), tuple(v[6:]), sys.argv[13]
    else:
        a, b, t = (3, 5, 1, 2, 0, 4), (1, 4, 5, 3, 2, 0), '7641'
    print("seeds=%d fail=%d maxsteps=%d maxsize=%d states=%d fails=%s" % run(a, b, t))
