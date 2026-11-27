"""Summarize theorem_N<N>.jsonl: per core, the set of universal lengths; compare with closure verdict.
usage: summarize.py N"""
import sys, json
from collections import defaultdict

N = int(sys.argv[1])
thr = 2 * N + 14
rows = [json.loads(l) for l in open('theorem_N%d.jsonl' % N)]
by = defaultdict(dict)
cp = {}
for r in rows:
    k = (tuple(r['a']), tuple(r['b']))
    by[k][r['d']] = r
    cp[k] = r['closure_pass']
ds = sorted({r['d'] for r in rows})
print('N=%d  threshold 2N+14=%d  cores=%d  lengths=%s  rows=%d' % (N, thr, len(by), ds, len(rows)))
print('stage-2 (complete enumeration) runs:', sum(r['stage'] == 2 for r in rows))
bad = []
cyc_univ = []
for k in sorted(by):
    U = [d for d in ds if d in by[k] and by[k][d]['universal']]
    Fs = {by[k][d].get('F', '').lstrip('0') for d in U}
    long_ = [by[k][d]['universal'] for d in ds if d >= thr and d in by[k]]
    for d in ds:
        r = by[k].get(d)
        if r and r.get('single_cycle_candidate'):
            cyc_univ.append((k, d, r['reason'], r['witness']))
    if cp[k] or U:
        print(k, 'closure_pass=%s' % cp[k], 'universal at', U, 'F', sorted(Fs))
    if long_ and (any(x != cp[k] for x in long_)):
        bad.append((k, 'brute/closure disagree at long length',
                    {d: by[k][d]['universal'] for d in ds if d >= thr}))
    if len(set(long_)) > 1:
        bad.append((k, 'universality differs between long lengths'))
print('cores passing closure:', sum(cp.values()))
print('COUNTEREXAMPLES:', len(bad))
for b in bad:
    print('  ', b)
print('rules where every sampled non-repdigit ends in ONE cycle of period > 1 (stage 1):', len(cyc_univ))
for c in cyc_univ[:10]:
    print('  ', c)
