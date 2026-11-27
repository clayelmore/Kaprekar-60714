"""Closure check for every core of size N (all a, b; including a_i = b_i).
Quick exact refutation first (Lemma 0, then Phi-orbits of random seeds in python: two different
terminal cycles, a non-fixed terminal cycle, or the empty multiset refute the check); survivors get the
complete vectorized check (closure.closure_check), which also gives M.
usage: scan_closure.py N workers > scan_N<N>.jsonl"""
import sys, json, random
from multiprocessing import Pool
from refkit import all_cores, lemma0_ok, phi_py
from closure import closure_check

N = int(sys.argv[1])
W = int(sys.argv[2]) if len(sys.argv) > 2 else 8


def rand_seed(rng):
    t = rng.randint(0, N - 1)
    k = rng.randint(0, N + 9)
    if rng.random() < 0.3:
        k = N + 9
    S = [9] * t + [rng.randint(1, 8) for _ in range(k)]
    if not S:
        S = [rng.randint(1, 9 if N > 1 else 8)]
    return tuple(sorted(S, reverse=True))


def quick(a, b, rng, n=150):
    memo = {}
    terms = set()
    for _ in range(n):
        S = rand_seed(rng)
        seen = {}
        path = []
        while S not in seen:
            seen[S] = len(path); path.append(S)
            if S not in memo:
                memo[S] = phi_py(S, a, b)
            S = memo[S]
        cyc = frozenset(path[seen[S]:])
        if len(cyc) > 1:
            return 'cycle period %d' % len(cyc)
        if () in cyc:
            return 'empty'
        terms.add(cyc)
        if len(terms) > 1:
            return 'two fixed points'
    return None


def job(core):
    a, b = core
    rng = random.Random(hash(core) & 0xffffffff)
    ok, wit = lemma0_ok(a, b)
    if not ok:
        return dict(a=a, b=b, passes=False, reason='lemma0', witness=wit)
    q = quick(a, b, rng)
    if q:
        return dict(a=a, b=b, passes=False, reason=q)
    r = closure_check(a, b)
    return dict(a=a, b=b, passes=r['passes'], reason='full', M=r['M'], n_terminal=r['n_terminal'],
                terminal=r['terminal'][:1], fixed=r['fixed_terminal'])


if __name__ == '__main__':
    cores = list(all_cores(N))
    with Pool(W) as p:
        for r in p.imap_unordered(job, cores, chunksize=4):
            print(json.dumps(r, default=list), flush=True)
