"""End-to-end test of the Theorem: brute-force universality (brute.py) vs own closure check
(prop1_N<N>.json, produced by prop1_sweep.py) for every core of size N at the given lengths.
usage: theorem_test.py N d1,d2,... [workers] [only_passing]"""
import sys, json, time
from multiprocessing import Pool
from refkit import all_cores
from brute import universal

N = int(sys.argv[1])
ds = [int(q) for q in sys.argv[2].split(',') if q]
W = int(sys.argv[3]) if len(sys.argv) > 3 else 8
only_pass = len(sys.argv) > 4 and sys.argv[4] == 'only_passing'

P = json.load(open('prop1_N%d.json' % N))
passing = {(tuple(r['a']), tuple(r['b'])) for r in P['passing']}
term = {(tuple(r['a']), tuple(r['b'])): r['terminal'] for r in P['passing']}


def job(arg):
    (a, b), d = arg
    t0 = time.time()
    r = universal(a, b, d, force_full=False)
    r.update(a=a, b=b, d=d, closure_pass=(a, b) in passing, sec=round(time.time() - t0, 1))
    return r


if __name__ == '__main__':
    cores = [c for c in all_cores(N) if (not only_pass or c in passing)]
    args = [(c, d) for c in cores for d in ds]
    # big jobs first
    args.sort(key=lambda x: -(x[0] in passing) * x[1])
    with Pool(W) as p:
        for r in p.imap_unordered(job, args):
            print(json.dumps(r, default=list), flush=True)
