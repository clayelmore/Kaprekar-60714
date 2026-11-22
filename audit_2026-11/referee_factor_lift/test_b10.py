import sys, random, time
from ref_lib import *
b = 10
rows = [l.rstrip('\n').split('\t') for l in open('../factor/classC_b10_n5.tsv')][1:]
print('rows in tsv', len(rows), 'distinct m', len(set(r[0] for r in rows)))
random.seed(20261121)
k = int(sys.argv[1]) if len(sys.argv) > 1 else 24
do14 = int(sys.argv[2]) if len(sys.argv) > 2 else 6
sel = random.sample(rows, k)
# always include the worked example
sel.append(next(r for r in rows if r[2] == '8,0,1,2,5,4,7,6,3,9'))
fails = 0; runs = 0; maxsteps = {}
t0 = time.time()
for idx, (m, F, slots) in enumerate(sel):
    m = int(m); F = int(F)
    x = list(map(int, slots.split(',')))
    rule = [(x[2*q], x[2*q+1]) for q in range(5)]
    assert sorted(x) == list(range(10))
    c = classC(rule, b)
    ok = c['S'] and c['U'] and c['C1'] and c['mstar'] == m and F == (b**5 - 1) * m
    if not ok: fails += 1; print('CLASS-C MISMATCH', m, slots, c)
    Nstar = digs(m - 1, b, 5)
    def run(r, nd, tag, Dpred):
        global fails, runs
        u = enumerate_universal(r, b)
        runs += 1
        pred = F_from_Ndigits(nd, b)
        cc = classC(r, b)
        good = u[0] and u[1] == pred and cc['S'] and cc['U'] and cc['C1'] and covers_all_gaps(r) and u[2] <= Dpred + 2
        maxsteps.setdefault(tag, []).append((u[2], Dpred + 2, cc['D']))
        if not good:
            fails += 1; print('FAIL', tag, m, slots, u, pred, cc)
        return u
    D = c['D']
    u = enumerate_universal(rule, b); runs += 1
    if not (u[0] and u[1] == F and covers_all_gaps(rule)): fails += 1; print('FAIL seed', m, slots, u)
    maxsteps.setdefault('seed', []).append((u[2], D + 2, D))
    T = top_lift(rule); B = bottom_lift(rule)
    run(T, [9] + Nstar, 'T', D + 1)
    run(B, Nstar + [0], 'B', D + 1)
    if idx < do14 or idx == len(sel) - 1:
        run(top_lift(T), [9, 9] + Nstar, 'TT', D + 2)
        run(bottom_lift(T), [9] + Nstar + [0], 'TB', D + 2)
        run(top_lift(B), [9] + Nstar + [0], 'BT', D + 2)
        run(bottom_lift(B), Nstar + [0, 0], 'BB', D + 2)
    print(idx, m, slots, 'ok' if ok else 'BAD', 'D=%s' % D, 'elapsed %.0fs' % (time.time() - t0), flush=True)
print('total enumeration runs', runs, 'failures', fails)
for t, v in maxsteps.items():
    print(t, 'n=%d' % len(v), 'max observed steps', max(a for a, _, _ in v), 'all within bound:', all(a <= bd for a, bd, _ in v),
          'tight cases:', sum(a == bd for a, bd, _ in v))
