"""N = 5 end-to-end check at d = 24, 25 (= 2N+14, 2N+15): brute force vs own closure check
(scan_N5.jsonl) for: all 17 passing cores with a_i != b_i, 10 other passing cores, every core that
survived the quick refutation but failed the complete closure check, and 40 random failing cores.
usage: n5_theorem.py workers > theorem_N5.jsonl"""
import sys, json, random, time
from multiprocessing import Pool
from brute import universal

W = int(sys.argv[1]) if len(sys.argv) > 1 else 6
S = [json.loads(l) for l in open('scan_N5.jsonl')]
rng = random.Random(5)
der = [r for r in S if r['passes'] and all(r['a'][i] != r['b'][i] for i in range(5))]
oth = rng.sample([r for r in S if r['passes'] and r not in der], 10)
ffail = [r for r in S if r['reason'] == 'full' and not r['passes']]
rfail = rng.sample([r for r in S if r['reason'] != 'full'], 40)
chosen = der + oth + ffail + rfail


def job(arg):
    r, d = arg
    t0 = time.time()
    u = universal(tuple(r['a']), tuple(r['b']), d)
    u.update(a=r['a'], b=r['b'], d=d, closure_pass=r['passes'], closure_reason=r['reason'],
             sec=round(time.time() - t0, 1))
    return u


if __name__ == '__main__':
    args = [(r, d) for r in chosen for d in (24, 25)]
    with Pool(W) as p:
        for u in p.imap_unordered(job, args):
            print(json.dumps(u, default=list), flush=True)
