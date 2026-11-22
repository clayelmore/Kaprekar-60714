#!/usr/bin/env python3
"""Class C inside the factor family (2026-11-21): universal half-swap rules, base b even, that are
  (S)  sign-definite: V has one sign on every mirror state, and
  (C1) every zero-free state (all deficits >= 1) has an image that contains a deficit 0 (a digit pair 0, b-1).
For these the extreme-pair lifts are provably universal at every longer length (PROOF_FACTOR_LIFT.md).
Usage: factor_classZ.py N [BASE] [check]  reads factor/b{BASE}_n{N}.tsv; 'check' also verifies both lifts
       of every class-C rule at n+1 and n+2 by the complete state table.
"""
import sys, itertools, numpy as np
from factor_family import states, digits_of_state, transition, endpoints, gap_cover_ok
def classify(a, n, b):
    st, H = states(n, b)
    sgn = set(); c1 = True
    for rho in st:
        if b % 2 == 1 and all(r == H for r in rho): continue
        s = digits_of_state(rho, b)
        V = sum(b**q * (s[a[2*q]] - s[a[2*q+1]]) for q in range(n))
        sgn.add(V > 0)
        if rho[0] >= 1:
            N = abs(V) - 1; z = False
            for _ in range(n):
                x = N % b; N //= b
                if x == 0 or x == b - 1: z = True
            c1 &= z
    return (sgn.pop() if len(sgn) == 1 else None), c1
def orient(a, positive):
    a = list(a)
    if not positive:
        for q in range(0, len(a), 2): a[q], a[q+1] = a[q+1], a[q]
    return a
def lift_top(a):      # a oriented so V > 0.  New extreme pair at the top place, P = new largest letter.
    L = len(a) + 2
    return [x + 1 for x in a] + [0, L - 1]
def lift_bottom(a):   # new extreme pair at place 0 with the minus sign; old places move up by one.
    L = len(a) + 2
    return [L - 1, 0] + [x + 1 for x in a]
def endpoint_m(a, n, b):
    A = np.array([a], dtype=np.int64)
    if not gap_cover_ok(A)[0]: return None
    T, st = transition(A, n, b); e, _ = endpoints(T)
    if e[0] < 0: return None
    s = digits_of_state(st[e[0]], b)
    return abs(sum(b**q * (s[a[2*q]] - s[a[2*q+1]]) for q in range(n)))
if __name__ == '__main__':
    n = int(sys.argv[1]); b = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    chk = len(sys.argv) > 3
    rows = [ln.split('\t') for ln in open(f"factor/b{b}_n{n}.tsv").read().split('\n')[1:] if ln]
    S = C = SC = 0; ends = set(); allm = set(); cls = []
    out = open(f"factor/classC_b{b}_n{n}.tsv", "w"); out.write("m\tF\tslots (oriented so V > 0)\n")
    for m, F, a in rows:
        a_ = tuple(map(int, a.split(','))); s, c = classify(a_, n, b)
        allm.add(m); S += s is not None; C += c
        if s is not None and c:
            SC += 1; ends.add(int(m)); o = orient(a_, s); cls.append((int(m), o))
            out.write(f"{m}\t{F}\t{','.join(map(str,o))}\n")
    print(f"n={n} base={b}: universal rules {len(rows)} (endpoints {len(allm)}); sign-definite {S}; (C1) {C}; "
          f"class C: {SC} rules, {len(ends)} endpoints")
    print("   class-C endpoints m:", sorted(ends)[:60], "..." if len(ends) > 60 else "")
    if chk:
        bad = 0; tested = 0
        import random; random.seed(5)
        sample = cls if len(cls) <= 400 else random.sample(cls, 400)
        for m, o in sample:
            for seq in itertools.product("TB", repeat=2):
                a = o; mm = m; nn = n
                for c in seq:
                    a = lift_top(a) if c == "T" else lift_bottom(a)
                    mm = (b - 1) * b**nn + mm if c == "T" else b * mm - (b - 1)
                    nn += 1
                    got = endpoint_m(a, nn, b); tested += 1
                    if got != mm: bad += 1; print("   FAIL", m, o, seq, got, mm)
        print(f"   lifts checked by complete state table (two levels, top/bottom in every order): {tested}, failures {bad}")
