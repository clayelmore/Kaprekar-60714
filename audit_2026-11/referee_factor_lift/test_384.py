import numpy as np
from ref_lib import *
from test_misc import univ_by_states
b = 10
U = np.load('univ_b10_n4.npy').tolist()
sts = all_states(b, 4)
cnt = {'Vtau>0': 0, 'Vtau<0': 0, 'both': 0, 'mixed-sign rules': 0}
for p in U:
    r = [(p[2*q], p[2*q+1]) for q in range(4)]
    vs = {s: V_single(state_string(s, b), r, b) for s in sts}
    tau = [s for s in sts if state_of_value(9999 * abs(vs[s]), b, 4) == s][0]
    if vs[tau] < 0: r = [(M, P) for P, M in r]
    cnt['mixed-sign rules'] += len({v > 0 for v in vs.values()}) == 2
    a = univ_by_states(top_lift(r), 5); c = univ_by_states(top_lift([(M, P) for P, M in r]), 5)
    cnt['Vtau>0'] += a; cnt['Vtau<0'] += c; cnt['both'] += a and c
print(cnt)
