"""Proposition 1 for larger N on a sample of cores, every seed enumerated (so extreme seeds included).
Sample = random cores + cores with a = b (these gave the largest M for N = 2, 3, 4) + forced x = 0 and
x = N-1.  usage: prop1_sample.py N n_random workers"""
import sys, random, json, itertools
from multiprocessing import Pool
from closure import closure_check

N = int(sys.argv[1]); n = int(sys.argv[2]); W = int(sys.argv[3])


def job(core):
    a, b = core
    r = closure_check(a, b, want_lemma0=False)
    return dict(a=a, b=b, M=r['M'], M_state=r['M_state'], max_state=r['max_state'])


if __name__ == '__main__':
    rng = random.Random(2026)
    perms = list(itertools.permutations(range(N)))
    cores = set()
    while len(cores) < n:
        cores.add((rng.choice(perms), rng.choice(perms)))
    for _ in range(max(4, n // 8)):
        p = rng.choice(perms); cores.add((p, p))
    for xv in (0, N - 1):
        for _ in range(max(4, n // 8)):
            a = list(rng.choice(perms)); j = a.index(xv); a[j], a[-1] = a[-1], a[j]
            cores.add((tuple(a), rng.choice(perms)))
    cores = sorted(cores)
    with Pool(W) as p:
        res = p.map(job, cores, chunksize=1)
    Ms = [r['M'] for r in res]
    print(json.dumps(dict(N=N, n_cores=len(res), bound=2 * N + 13, max_M=max(Ms),
                          hist={str(k): Ms.count(k) for k in sorted(set(Ms))},
                          argmax=[r for r in res if r['M'] == max(Ms)][:4]), default=list))
