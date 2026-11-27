"""Proposition 1: for every core of size N (all (a,b), including a_i = b_i), enumerate ALL seeds,
follow every Phi-orbit to its cycle, record the largest number of nonzero digits.
Also records the closure-check verdict for every core.
usage: prop1_sweep.py N [max_cores] [workers]"""
import sys, random, json, time
import numpy as np
from multiprocessing import Pool
from refkit import all_cores, phi_py
from closure import closure_check, seeds_array, phi_batch

N = int(sys.argv[1])
maxc = int(sys.argv[2]) if len(sys.argv) > 2 else 0
W = int(sys.argv[3]) if len(sys.argv) > 3 else 12


def job(core):
    a, b = core
    r = closure_check(a, b)
    return dict(a=a, b=b, M=r['M'], M_state=r['M_state'], passes=r['passes'], lemma0=r['lemma0'],
                n_terminal=r['n_terminal'], fixed=r['fixed_terminal'], n_states=r['n_states'],
                terminal=r['terminal'][:2] if r['passes'] else r['terminal'][:1])


if __name__ == '__main__':
    cores = list(all_cores(N))
    random.seed(7)
    if maxc and len(cores) > maxc:
        # always include cores with x = 0 and x = N-1, then random
        cores = random.sample(cores, maxc)
    # sanity: phi_batch vs phi_py on a sample of seeds for the first core
    a, b = cores[0]
    sd = seeds_array(N)
    idx = np.random.RandomState(0).choice(sd.shape[0], 300, replace=False)
    pb = phi_batch(sd[idx], a, b, 2 * N + 40)
    for j, i in enumerate(idx):
        S = tuple(sorted([9 - k for k in range(9) for _ in range(int(sd[i][8 - k]))], reverse=True))
        P = phi_py(S, a, b)
        cnt = [P.count(v) for v in range(1, 10)]
        assert cnt == list(pb[j]), (S, P, pb[j])
    t0 = time.time()
    with Pool(W) as p:
        res = p.map(job, cores, chunksize=1)
    Ms = [r['M'] for r in res]
    out = dict(N=N, n_cores=len(res), n_seeds_per_core=int(sd.shape[0]), bound_2N_13=2 * N + 13,
               max_M=max(Ms), hist_M={str(k): Ms.count(k) for k in sorted(set(Ms))},
               n_pass=sum(r['passes'] for r in res), n_lemma0=sum(bool(r['lemma0']) for r in res),
               passing=[r for r in res if r['passes']],
               argmax=[r for r in res if r['M'] == max(Ms)][:3], seconds=round(time.time() - t0, 1))
    print(json.dumps(out, default=lambda o: list(o) if isinstance(o, tuple) else int(o)))
