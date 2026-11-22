#!/usr/bin/env python3
"""Build-to-order inside the factor family (2026-11-21, route A).

Target: F = (b^n - 1) * m at length 2n (m has at most n digits).  Find half-swap rules (letters -> slots
(P_q, M_q)) with endpoint F for EVERY non-repdigit 2n-digit string.

Why the check is small (PROOF_HALFSWAP.md 1.2-1.3, true for every half-swap rule):
  (a) only repdigits map to 0  <=>  the intervals [P_q, M_q] cover every gap between neighboring letters;
  (b) every nonzero image is n digits plus their complements, so it is one of C(n+H, n) states, H = (b-1)//2.
So a rule is universal iff (a) holds and every state flows to the state of F.  Base 10: 70 states at 8 digits,
126 at 10, 210 at 12, 330 at 14, 495 at 16.  (Odd bases need one more check, see factor_family.py.)

Usage:
  factor_to_order.py find M N [BASE] [CAP]      rules for one target; prints up to 5 and a certificate count
  factor_to_order.py survey N COUNT [BASE] [CAP] [SEED]   random m; how many get a rule
  factor_to_order.py cert M N SLOTS [BASE]      print the full state table for one rule (SLOTS comma list)
"""
import sys, random, itertools
import numpy as np
from factor_family import transition, endpoints, gap_cover_ok, digits_of_state, states

def state_of_m(m, n, b):
    N = m - 1; out = []
    for _ in range(n):
        x = N % b; N //= b; out.append(min(x, b - 1 - x))
    return tuple(sorted(out))

def signed_reps(m, n, b):
    """All (d_0..d_{n-1}), |d_q| <= b-1, with sum b^q d_q = m."""
    out = []
    def rec(q, v, acc):
        if q == n:
            if v == 0: out.append(tuple(acc))
            return
        r = v % b
        for d in ({r, r - b} if r else {0}):
            rec(q + 1, (v - d) // b, acc + [d])
    rec(0, m, [])
    return out

def fixing_rules(m, n, b, cap, rng):
    """Slot assignments a (len 2n) with V(F) = +m.  Returns (list, truncated?)."""
    rho = state_of_m(m, n, b)
    s = digits_of_state(rho, b)
    L = 2 * n
    out = []; trunc = [False]
    reps = signed_reps(m, n, b); rng.shuffle(reps)
    def rec(q, d, used, acc):
        if len(out) >= cap: trunc[0] = True; return
        if q == n:
            out.append(tuple(acc)); return
        order = [i for i in range(L) if not used[i]]; rng.shuffle(order)
        for P in order:
            want = s[P] - d[q]
            for M in order:
                if M != P and s[M] == want:
                    used[P] = used[M] = True
                    rec(q + 1, d, used, acc + [P, M])
                    used[P] = used[M] = False
                    if trunc[0]: return
    for d in reps:
        rec(0, d, [False] * L, [])
        if trunc[0]: break
    return out, trunc[0]

def universal_rules(m, n, b, cap=200000, seed=1):
    """Returns (winners, n_fixing_with_gap_cover, truncated?)."""
    rng = random.Random(seed)
    if m <= 0 or m >= b ** n: return [], 0, False
    rules, trunc = fixing_rules(m, n, b, cap, rng)
    if not rules: return [], 0, trunc
    A = np.array(rules, dtype=np.int64)
    A = A[gap_cover_ok(A)]
    if not len(A): return [], 0, trunc
    target = state_of_m(m, n, b)
    win = []
    for off in range(0, len(A), 100000):
        a = A[off:off + 100000]
        T, st = transition(a, n, b)
        e, _ = endpoints(T)
        ti = st.index(target)
        for r in np.nonzero(e == ti)[0]:
            win.append(tuple(int(x) for x in a[r]))
    return win, len(A), trunc

def words(a, n):
    """Letters words for slots a: word 1 has P_q at place q+n and M_q at place q."""
    L = 2 * n
    w1 = [None] * L; w2 = [None] * L
    for q in range(n):
        P, M = a[2 * q], a[2 * q + 1]
        w1[q + n] = P; w1[q] = M; w2[q + n] = M; w2[q] = P
    f = lambda w: "".join(chr(65 + w[p]) for p in range(L - 1, -1, -1))
    return f(w1), f(w2)

def certificate(m, n, a, b):
    A = np.array([a], dtype=np.int64)
    assert gap_cover_ok(A)[0], "gap cover fails"
    T, st = transition(A, n, b)
    S = len(st); ti = st.index(state_of_m(m, n, b))
    lines = []; worst = 0
    for i, rho in enumerate(st):
        if T[0, i] == -1: continue
        path = [i]
        while path[-1] != ti:
            path.append(int(T[0, path[-1]]))
            assert path[-1] != S and len(path) < 5000, "not universal"
        worst = max(worst, len(path) - 1)
        s = digits_of_state(rho, b)
        V = sum(b ** q * (s[a[2 * q]] - s[a[2 * q + 1]]) for q in range(n))
        lines.append((rho, abs(V), st[T[0, i]], len(path) - 1))
    return lines, worst

def main():
    mode = sys.argv[1]
    if mode == 'find':
        m = int(sys.argv[2]); n = int(sys.argv[3])
        b = int(sys.argv[4]) if len(sys.argv) > 4 else 10
        cap = int(sys.argv[5]) if len(sys.argv) > 5 else 200000
        win, nfix, trunc = universal_rules(m, n, b, cap)
        F = (b ** n - 1) * m
        print(f"target m={m} F={F} length {2*n} base {b}: fixing rules with gap cover {nfix}"
              f"{' (capped sample)' if trunc else ' (all)'}; universal {len(win)}")
        from factor_classZ import classify
        cl = []
        if b % 2 == 0:
            for a in win[:2000]:
                sg, c1 = classify(a, n, b)
                if sg is not None and c1: cl.append(a)
            print(f"  class C (lifts to every longer length, PROOF_FACTOR_LIFT.md) among the first {min(len(win),2000)}: {len(cl)}")
        for a in (cl[:3] + [w for w in win if w not in cl][:3]):
            w1, w2 = words(a, n); _, worst = certificate(m, n, a, b)
            print(f"  {w1} - {w2}   slots {','.join(map(str,a))}   max steps from a state {worst}"
                  f"{'   class C' if a in cl else ''}")
    elif mode == 'survey':
        n = int(sys.argv[2]); cnt = int(sys.argv[3])
        b = int(sys.argv[4]) if len(sys.argv) > 4 else 10
        cap = int(sys.argv[5]) if len(sys.argv) > 5 else 200000
        seed = int(sys.argv[6]) if len(sys.argv) > 6 else 7
        rng = random.Random(seed)
        nofix = found = notfound_all = notfound_cap = nC = 0
        print("m\tF\tfixing\ttruncated\tuniversal\texample")
        for _ in range(cnt):
            m = rng.randrange(1, b ** n)
            win, nfix, trunc = universal_rules(m, n, b, cap, seed)
            if nfix == 0 and not trunc: nofix += 1
            elif win: found += 1
            elif trunc: notfound_cap += 1
            else: notfound_all += 1
            ex = "-".join(words(win[0], n)) if win else ""
            cC = 0
            if win and b % 2 == 0:
                from factor_classZ import classify
                for a in win[:300]:
                    sg, c1 = classify(a, n, b)
                    if sg is not None and c1: cC += 1; ex = "-".join(words(a, n)) + " (class C)"; break
                nC += cC > 0
            print(f"{m}\t{(b**n-1)*m}\t{nfix}\t{int(trunc)}\t{len(win)}\t{ex}", flush=True)
        print(f"# n={n} base={b} targets={cnt}: no fixing rule {nofix}; every fixing rule fails {notfound_all}; "
              f"not found in capped sample {notfound_cap}; rule found {found}; of these with a class-C rule "
              f"(among the first 300 winners) {nC}")
    elif mode == 'cert':
        m = int(sys.argv[2]); n = int(sys.argv[3]); a = tuple(int(x) for x in sys.argv[4].split(','))
        b = int(sys.argv[5]) if len(sys.argv) > 5 else 10
        lines, worst = certificate(m, n, a, b)
        w1, w2 = words(a, n)
        print(f"Rule {w1} - {w2}, base {b}, length {2*n}.  Endpoint F = {(b**n-1)*m} (m = {m}).")
        print(f"{len(lines)} states; each line: deficits -> m of the image -> next deficits (steps to endpoint)")
        for rho, mm, nx, k in lines:
            print(f"  {''.join(map(str,rho)) if b<=20 else rho} -> {mm} -> {''.join(map(str,nx)) if b<=20 else nx}  ({k})")
        print(f"max steps from a state: {worst}")

if __name__ == '__main__':
    main()
