#!/usr/bin/env python3
"""Folding experiment, part 1 (cheap):
- fold_2 and fold_3 of every universal full-variable rule at d=4 -> full basins at d=8, d=12.
- fold_2 of 60714's native d=5 rule -> full basin at d=10.
Folding: c'_{ki+j} = c_i * 10^(d0*(k-1-j)).  Folded states are closed and conjugate
to the base dynamics (verified identity in v5); fixed point is W repeated k times.
"""
import sys, itertools, time
from collections import Counter
sys.path.insert(0, '/Users/clayelmore/Downloads')
from search_multiset_universals_fast import K_apply, sorted_desc_digits, coefs_from_invs

def fold_c(c0, d0, k):
    out = []
    for g in c0:
        for j in range(k):
            out.append(g * 10**(d0*(k-1-j)))
    return tuple(out)

def non_repdigit_multisets(d):
    return [c for c in itertools.combinations_with_replacement(range(9,-1,-1), d)
            if c[0] != c[-1]]

def basin_of(c, d, F, A, report_terminals=False):
    cache = {}
    nF = 0
    term = Counter()
    for ms in A:
        path = []
        cur = ms
        while cur not in cache:
            path.append(cur)
            n = K_apply(c, cur)
            if n == 0:
                for p in path: cache[p] = ('zero', 0)
                break
            nxt = sorted_desc_digits(n, d)
            if nxt == cur:
                for p in path: cache[p] = ('fp', n)
                break
            if nxt in path:
                for p in path: cache[p] = ('cyc', n)
                break
            cur = nxt
        res = cache[cur]
        for p in path: cache[p] = res
        term[res] += 1
        if res == ('fp', F): nF += 1
    if report_terminals:
        top = sorted(term.items(), key=lambda kv: -kv[1])[:6]
        print(f"      terminals (top): {top}")
    return nF / len(A)

# --- recover universal full-variable rules at d=4 ---
def universal_rules_d4():
    A = [c for c in non_repdigit_multisets(4)
         if max(Counter(c).values()) < 3]  # exclude near-repdigits for census convention
    perms = list(itertools.permutations(range(4)))
    out = []
    for pi_inv in perms:
        for sigma_inv in perms:
            if all(pi_inv[i] != sigma_inv[i] for i in range(4)):
                c = coefs_from_invs(pi_inv, sigma_inv, 4)
                # universality with early abort
                cache = {}; okF = None; good = True
                for ms in A:
                    path = []; cur = ms
                    while cur not in cache:
                        path.append(cur)
                        n = K_apply(c, cur)
                        if n == 0:
                            for p in path: cache[p] = 0
                            break
                        nxt = sorted_desc_digits(n, 4)
                        if nxt == cur:
                            for p in path: cache[p] = n
                            break
                        if nxt in path:
                            for p in path: cache[p] = -1
                            break
                        cur = nxt
                    v = cache[cur]
                    for p in path: cache[p] = v
                    if v <= 0: good = False; break
                    if okF is None: okF = v
                    elif v != okF: good = False; break
                if good:
                    out.append((okF, c))
    return out

U4 = universal_rules_d4()
byF = {}
for F, c in U4: byF.setdefault(F, []).append(c)
print("universal full-variable rules at d=4:")
for F in sorted(byF): print(f"  F={F}: {len(byF[F])} rules")

print("\n=== fold_2 of d=4 universal rules (d=8, full basin over non-repdigit multisets) ===")
A8 = non_repdigit_multisets(8)
for F in sorted(byF):
    for c in byF[F]:
        c2 = fold_c(c, 4, 2)
        FF = int(str(F).zfill(4) * 2)
        b = basin_of(c2, 8, FF, A8)
        print(f"  F={F} c={c} -> fold_2 fixes {FF}: basin {b:.4f}{'  *** UNIVERSAL ***' if b == 1.0 else ''}")

print("\n=== fold_3 of d=4 universal rules (d=12, full basin) ===")
A12 = non_repdigit_multisets(12)
t0 = time.time()
for F in sorted(byF):
    c = byF[F][0]  # one rule per F (sign-flip pairs behave same; check first)
    c3 = fold_c(c, 4, 3)
    FFF = int(str(F).zfill(4) * 3)
    b = basin_of(c3, 12, FFF, A12)
    print(f"  F={F} -> fold_3 fixes {FFF}: basin {b:.4f}{'  *** UNIVERSAL ***' if b == 1.0 else ''} ({time.time()-t0:.0f}s)")

print("\n=== fold_2 of 60714 native d=5 rule (d=10, full basin) ===")
c5 = (9900, 9, 90, -9000, -999)
c10 = fold_c(c5, 5, 2)
A10 = non_repdigit_multisets(10)
F10 = 6071460714
b = basin_of(c10, 10, F10, A10, report_terminals=True)
print(f"  fold_2(60714 native) fixes {F10}: basin {b:.4f}{'  *** UNIVERSAL ***' if b == 1.0 else ''}")
