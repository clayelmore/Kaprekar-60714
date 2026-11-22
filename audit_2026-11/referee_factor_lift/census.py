# Independent census by state tables (section 2 criterion), vectorized over rules. Base and n from argv.
import sys, itertools, numpy as np, math
from ref_lib import all_states, state_string, enumerate_universal, covers_all_gaps, top_lift, bottom_lift
b = int(sys.argv[1]); n = int(sys.argv[2]); L = 2*n
H = (b-1)//2
sts = all_states(b, n); ns = len(sts)
St = np.array([state_string(r, b) for r in sts], dtype=np.int64)       # ns x L
code = lambda arr: (arr * ((H+1) ** np.arange(n))[None, None, :]).sum(axis=2)
lut = -np.ones((H+1)**n, dtype=np.int64)
for i, r in enumerate(sts):
    lut[sum(x*(H+1)**k for k, x in enumerate(r))] = i
has0 = np.array([r[0] == 0 for r in sts]); 
def analyze(P):
    """P: R x L int array, columns P0,M0,P1,M1,... Returns dict of per-rule arrays."""
    R = P.shape[0]
    V = np.zeros((R, ns), dtype=np.int64)
    for q in range(n):
        V += b**q * (St[:, P[:, 2*q]].T - St[:, P[:, 2*q+1]].T)
    # gap cover
    lo = np.minimum(P[:, 0::2], P[:, 1::2]); hi = np.maximum(P[:, 0::2], P[:, 1::2])
    cov = np.ones(R, dtype=bool)
    for j in range(L-1):
        cov &= ((lo <= j) & (j < hi)).any(axis=1)
    nz = (V != 0).all(axis=1)
    S = (V > 0).all(axis=1) | (V < 0).all(axis=1)
    m = np.abs(V); N = np.where(m > 0, m - 1, 0)
    d = np.empty((R, ns, n), dtype=np.int64)
    x = N.copy()
    for i in range(n):
        dg = x % b; x //= b
        d[:, :, i] = np.minimum(dg, b-1-dg)
    d.sort(axis=2)
    T = lut[code(d)]                       # R x ns ; valid where m>0
    T = np.where(m > 0, T, np.arange(ns)[None, :])   # park V=0 states on themselves (rule then flagged via nz)
    fixed = (T == np.arange(ns)[None, :]) & (m > 0)
    Tk = T.copy()
    for _ in range(int(math.ceil(math.log2(ns))) + 1):
        Tk = np.take_along_axis(Tk, Tk, axis=1)
    const = (Tk == Tk[:, :1]).all(axis=1)
    endfixed = np.take_along_axis(T, Tk[:, :1], axis=1)[:, 0] == Tk[:, 0]
    U = nz & const & endfixed
    univ = U & cov
    mend = np.take_along_axis(m, Tk[:, :1], axis=1)[:, 0]
    C1 = (has0[T] | has0[None, :]).all(axis=1)      # states with rho_1>=1 must map to a state containing 0
    C = S & U & C1
    return dict(cov=cov, univ=univ, mend=mend, C=C, fixed=fixed, m=m, nz=nz, S=S, U=U)
tot = dict(rules=0, cov=0, univ=0, C=0, Ccov=0, nilp=0)
mfix_cov = set(); mfix_all = set(); muniv = set(); mC = set(); mCcov = set()
univ_rules = []; C_rules = []
def chunks():
    buf = []
    for p in itertools.permutations(range(L)):
        if p[0] > p[1]: continue            # one representative per global sign
        buf.append(p)
        if len(buf) == 40000:
            yield np.array(buf, dtype=np.int64); buf = []
    if buf: yield np.array(buf, dtype=np.int64)
for P in chunks():
    a = analyze(P)
    tot['rules'] += len(P); tot['cov'] += int(a['cov'].sum()); tot['univ'] += int(a['univ'].sum())
    tot['C'] += int(a['C'].sum()); tot['Ccov'] += int((a['C'] & a['cov']).sum())
    muniv.update(a['mend'][a['univ']].tolist()); mC.update(a['mend'][a['C']].tolist()); mCcov.update(a['mend'][a['C'] & a['cov']].tolist())
    mfix_cov.update(np.unique(a['m'][a['fixed'] & a['cov'][:, None]]).tolist())
    mfix_all.update(np.unique(a['m'][a['fixed']]).tolist())
    univ_rules += P[a['univ']].tolist(); C_rules += [(p, int(mm), bool(c)) for p, mm, c in zip(P[a['C']].tolist(), a['mend'][a['C']].tolist(), a['cov'][a['C']].tolist())]
print('base', b, 'length', L, 'states', ns, tot)
print(' m fixed by some gap-covering rule', len(mfix_cov), '| by any rule', len(mfix_all), '| m with universal rule', len(muniv),
      '| class C endpoints (gap-covering)', len(mCcov), '| class C endpoints (any)', len(mC))
np.save('univ_b%d_n%d.npy' % (b, n), np.array(univ_rules, dtype=np.int64).reshape(-1, L))
with open('classC_b%d_n%d_mine.txt' % (b, n), 'w') as f:
    for p, mm, c in C_rules: f.write('%d\t%s\t%s\n' % (mm, ','.join(map(str, p)), 'cov' if c else 'NOGAPCOVER'))
