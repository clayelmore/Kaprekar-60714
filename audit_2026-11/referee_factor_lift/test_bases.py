# Other even bases: brute-force every rule (up to global sign), find class C by literal definition,
# lift, and confirm by complete enumeration of digit multisets.
import sys, itertools, random
from ref_lib import *
def rules_up_to_sign(n):
    L = 2 * n
    for p in itertools.permutations(range(L)):
        if p[0] > p[1]: continue   # crude sign normalization: fix orientation of pair 0, then test both signs
        yield [(p[2*q], p[2*q+1]) for q in range(n)]
random.seed(7)
for b, n, cap in [(2,2,99),(2,3,40),(4,2,99),(4,3,99),(4,4,60),(6,2,99),(6,3,99),(6,4,40),(8,2,99),(8,3,99),(8,4,30),(12,3,30),(4,5,25),(6,5,12)]:
    found = []
    cnt = 0
    it = rules_up_to_sign(n)
    if n == 5:
        # sample random permutations rather than all 1.8M
        def gen():
            for _ in range(60000 if b == 4 else 150000):
                p = list(range(2*n)); random.shuffle(p)
                yield [(p[2*q], p[2*q+1]) for q in range(n)]
        it = gen()
    seen = set()
    for r in it:
        cnt += 1
        for rr in (r, [(M, P) for P, M in r]):
            c = classC(rr, b)
            if c['S'] and c['U'] and c['C1']:
                key = tuple(rr)
                if key not in seen:
                    seen.add(key); found.append((rr, c))
    nogap = [f for f in found if not covers_all_gaps(f[0])]
    print('base', b, 'n', n, 'rules scanned', cnt, 'class C', len(found), 'of which NOT covering every gap', len(nogap), flush=True)
    random.shuffle(found)
    test = nogap[:5] + found[:cap]
    fails = 0; runs = 0
    for rule, c in test:
        Ns = digs(c['mstar'] - 1, b, n)
        if covers_all_gaps(rule):
            u = enumerate_universal(rule, b); runs += 1
            if not (u[0] and u[1] == (b**n - 1) * c['mstar']): fails += 1; print(' FAIL seed', rule, u)
        else:
            u = enumerate_universal(rule, b); runs += 1
            if u[0]: fails += 1; print(' UNEXPECTED: gap-uncovered seed universal', rule)
        T = top_lift(rule); B = bottom_lift(rule)
        jobs = [(T, [b-1] + Ns), (B, Ns + [0])]
        if 2 * n + 4 <= (12 if b <= 6 else 10):
            jobs += [(top_lift(T), [b-1]*2 + Ns), (bottom_lift(T), [b-1] + Ns + [0]), (top_lift(B), [b-1] + Ns + [0]), (bottom_lift(B), Ns + [0, 0])]
        for r2, nd in jobs:
            u = enumerate_universal(r2, b); runs += 1
            c2 = classC(r2, b)
            if not (u[0] and u[1] == F_from_Ndigits(nd, b) and c2['S'] and c2['U'] and c2['C1']):
                fails += 1; print(' FAIL lift', rule, r2, u, F_from_Ndigits(nd, b), c2)
    print('   tested seeds', len(test), 'enumeration runs', runs, 'failures', fails, flush=True)
