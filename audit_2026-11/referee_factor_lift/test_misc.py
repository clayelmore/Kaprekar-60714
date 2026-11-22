import numpy as np
from ref_lib import *
b = 10
mine = {}
for l in open('classC_b10_n5_mine.txt').read().splitlines():
    m, s, tag = l.split('\t')
    if tag == 'cov':
        x = list(map(int, s.split(','))); rule = [(x[2*q], x[2*q+1]) for q in range(5)]
        if V_single(state_string((0,)*5, b), rule, b) < 0: rule = [(M, P) for P, M in rule]
        mine[','.join('%d,%d' % pm for pm in rule)] = int(m)
tsv = {l.rstrip('\n').split('\t')[2]: int(l.split('\t')[0]) for l in list(open('../factor/classC_b10_n5.tsv'))[1:]}
print('my gap-covering class C at 10 digits', len(mine), 'tsv', len(tsv), 'identical sets and m:', mine == tsv)
# remark: universal 8-digit rules whose top / bottom lift is universal at 10 digits (state-table criterion, my classC-free check)
def univ_by_states(rule, n):
    sts = all_states(b, n); T = {}
    if not covers_all_gaps(rule): return False
    for r in sts:
        v = abs(V_single(state_string(r, b), rule, b))
        if v == 0: return False
        T[r] = state_of_value((b**n - 1) * v, b, n)
    fx = [r for r in sts if T[r] == r]
    if len(fx) != 1: return False
    for r in sts:
        x = r
        for _ in range(len(sts)):
            if x == fx[0]: break
            x = T[x]
        if x != fx[0]: return False
    return True
U = np.load('univ_b10_n4.npy').tolist()
t = bt = 0
for p in U:
    rule = [(p[2*q], p[2*q+1]) for q in range(4)]
    t += univ_by_states(top_lift(rule), 5) or univ_by_states(top_lift([(M, P) for P, M in rule]), 5)
    bt += univ_by_states(bottom_lift(rule), 5) or univ_by_states(bottom_lift([(M, P) for P, M in rule]), 5)
print('520 universal 8-digit rules: top lift universal (either orientation):', t, ' bottom:', bt)
t1 = sum(univ_by_states(top_lift(r if V_single(state_string((0,)*4, b), r, b) > 0 else [(M, P) for P, M in r]), 5)
         for r in ([(p[2*q], p[2*q+1]) for q in range(4)] for p in U))
print(' top lift universal, orientation V(0000)>0 only:', t1)
