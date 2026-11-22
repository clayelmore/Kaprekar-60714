# Class C rules at 8 digits (base 10) that do not cover every gap: verify literally, lift, enumerate, compare with project tsv.
import random, itertools, numpy as np
from ref_lib import *
b = 10
rows = [l.split('\t') for l in open('classC_b10_n4_mine.txt').read().splitlines()]
tsv = set(l.rstrip('\n').split('\t')[2] for l in list(open('../factor/classC_b10_n5.tsv'))[1:])
print('class C at 8 digits (my search):', len(rows), 'NOGAPCOVER:', sum(r[2] == 'NOGAPCOVER' for r in rows))
intsv = 0; fails = 0; runs = 0
random.seed(3)
for i, (m, slots, tag) in enumerate(rows):
    x = list(map(int, slots.split(',')))
    rule = [(x[2*q], x[2*q+1]) for q in range(4)]
    c = classC(rule, b)
    if not c['S']:
        rule = [(M, P) for P, M in rule]; c = classC(rule, b)
    assert c['S'] and c['U'] and c['C1'] and c['mstar'] == int(m), (rule, c)
    Ns = digs(int(m) - 1, b, 4)
    for lift, nd in ((top_lift(rule), [9] + Ns), (bottom_lift(rule), Ns + [0])):
        s = ','.join('%d,%d' % pm for pm in lift)
        intsv += s in tsv
        if i % 4 == 0:
            u = enumerate_universal(lift, b); runs += 1
            if not (u[0] and u[1] == F_from_Ndigits(nd, b)): fails += 1; print('FAIL', rule, u)
    if i == 0:
        u = enumerate_universal(rule, b)
        print('example seed', rule, 'm*', m, 'covers all gaps', covers_all_gaps(rule), 'seed universal by enumeration:', u[0], u[3])
print('lifts of these seeds present in project classC_b10_n5.tsv: %d of %d' % (intsv, 2 * len(rows)))
print('direct 10-digit enumerations of lifts:', runs, 'failures', fails)
# direct-enumeration cross-check of the census at 6 and 8 digits
for n in (3, 4):
    U = set(map(tuple, np.load('univ_b10_n%d.npy' % n).tolist()))
    allr = [p for p in itertools.permutations(range(2*n)) if p[0] < p[1]]
    test = allr if n == 3 else list(U) [:] + random.sample([p for p in allr if p not in U], 300)
    if n == 4: test = random.sample(list(U), 150) + test[len(U):]
    bad = 0
    for p in test:
        u = enumerate_universal([(p[2*q], p[2*q+1]) for q in range(n)], b)
        bad += (u[0] != (p in U))
    print('n', n, 'direct enumeration vs state-table census on', len(test), 'rules: disagreements', bad)
