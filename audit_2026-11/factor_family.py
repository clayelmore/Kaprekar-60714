#!/usr/bin/env python3
"""Factor family census (2026-11-21, route A).

Length 2n, base b.  A half-swap rule is an assignment of the 2n sorted letters s_0 >= ... >= s_{2n-1} to slots
(P_q, M_q), q = 0..n-1.  K(s) = (b^n - 1) * |V|,  V = sum_q b^q (s[P_q] - s[M_q]).

Facts used (PROOF_HALFSWAP.md 1.2, 1.3, valid for every half-swap rule):
  * V = 0 iff every pair has equal letters.  So "only repdigits map to 0" iff the intervals [P_q, M_q] cover
    every gap between consecutive letters and are connected.  Base independent.
  * A nonzero image is n digits x plus complements, so its sorted digits are determined by the sorted deficits
    rho_1 <= ... <= rho_n (rho = min(x, b-1-x)).  Every state is itself a 2n-digit string, so checking the map
    on all states plus the gap-cover condition is a complete check of the rule on every 2n-digit string,
    EXCEPT (odd b only) a first image that is the repdigit ((b-1)/2)^(2n); that needs a separate check.

Usage: factor_family.py N BASE [out.tsv]     enumerates all (2N)! slot assignments (N <= 5).
Output: one line per universal rule (up to the global sign): endpoint m, F, pairs by place.
"""
import sys, itertools, math
import numpy as np

def states(n, b):
    H = (b - 1) // 2
    st = list(itertools.combinations_with_replacement(range(H + 1), n))
    return st, H

def digits_of_state(rho, b):
    n = len(rho)
    s = [0] * (2 * n)
    for i, r in enumerate(rho):          # rho ascending
        s[i] = b - 1 - r
        s[2 * n - 1 - i] = r
    return s

def gap_cover_ok(A):
    """A: (R, 2n) letters by slot.  True where the pair intervals cover every gap (only repdigits -> 0)."""
    R, L = A.shape
    cov = np.zeros((R, L - 1), dtype=bool)
    for q in range(L // 2):
        lo = np.minimum(A[:, 2 * q], A[:, 2 * q + 1]); hi = np.maximum(A[:, 2 * q], A[:, 2 * q + 1])
        for j in range(L - 1):
            cov[:, j] |= (lo <= j) & (hi > j)
    return cov.all(axis=1)

def transition(A, n, b):
    """Return (T, st): T[r, i] = index of next state of state i under rule r; len(st) = fail sentinel."""
    st, H = states(n, b)
    S = len(st)
    code = {}
    for i, rho in enumerate(st):
        c = 0
        for r in rho: c = c * (H + 1) + r
        code[c] = i
    lut = np.full((H + 1) ** n, S, dtype=np.int32)
    for c, i in code.items(): lut[c] = i
    rep = None
    if b % 2 == 1:
        rep = st.index(tuple([H] * n))
    R = A.shape[0]
    T = np.empty((R, S + 1), dtype=np.int32)
    T[:, S] = S
    pw = [b ** q for q in range(n)]
    for i, rho in enumerate(st):
        if i == rep:
            T[:, i] = -1; continue            # repdigit: not an input; marked, ignored by endpoints()
        s = np.array(digits_of_state(rho, b), dtype=np.int64)
        V = np.zeros(R, dtype=np.int64)
        for q in range(n):
            V += pw[q] * (s[A[:, 2 * q]] - s[A[:, 2 * q + 1]])
        m = np.abs(V)
        N = m - 1
        bad = m == 0
        N[bad] = 0
        d = np.empty((R, n), dtype=np.int64)
        for q in range(n):
            x = N % b; N //= b
            d[:, q] = np.minimum(x, b - 1 - x)
        d.sort(axis=1)
        c = np.zeros(R, dtype=np.int64)
        for q in range(n): c = c * (H + 1) + d[:, q]
        nxt = lut[c]
        nxt[bad] = S
        if rep is not None: nxt[nxt == rep] = S
        T[:, i] = nxt
    return T, st

def endpoints(T):
    """For each rule: the common fixed state index if every state reaches one fixed state, else -1."""
    R, S1 = T.shape
    P = T.copy()
    P[P == -1] = S1 - 1
    for _ in range(12):                       # 2^12 steps
        P = np.take_along_axis(P, P, axis=1)
    S = S1 - 1
    e = P[:, 0]
    live = T[0, :S] != -1
    ok = (P[:, :S][:, live] == e[:, None]).all(axis=1) & (e != S)
    ok &= np.take_along_axis(T, e[:, None], axis=1)[:, 0] == e
    return np.where(ok, e, -1), P

def m_of_state_under_rule(a, rho, n, b):
    s = digits_of_state(rho, b)
    return abs(sum(b ** q * (s[a[2 * q]] - s[a[2 * q + 1]]) for q in range(n)))

def rule_chunks(n, CH=300000):
    """All slot assignments up to the global sign (P < M at the top place), in chunks."""
    L = 2 * n
    it = itertools.permutations(range(L))
    while True:
        blk = list(itertools.islice(it, CH))
        if not blk: return
        A = np.array(blk, dtype=np.int64)
        A = A[A[:, L - 2] < A[:, L - 1]]
        A = A[gap_cover_ok(A)]
        if len(A): yield A

def census(n, b):
    """Returns (list of (m, slots)) for universal rules, set of m fixed by at least one gap-covering rule,
    number of gap-covering rules."""
    res = []; fixable = set(); tot = 0
    for a in rule_chunks(n):
        tot += len(a)
        T, st = transition(a, n, b)
        S = len(st)
        for i, rho in enumerate(st):               # fixed states -> fixable endpoints
            rr = np.nonzero(T[:, i] == i)[0]
            if len(rr):
                s = np.array(digits_of_state(rho, b), dtype=np.int64)
                V = np.zeros(len(rr), dtype=np.int64)
                for q in range(n): V += b ** q * (s[a[rr, 2 * q]] - s[a[rr, 2 * q + 1]])
                fixable.update(np.unique(np.abs(V)).tolist())
        e, _ = endpoints(T)
        for r in np.nonzero(e >= 0)[0]:
            m = m_of_state_under_rule(a[r], st[e[r]], n, b)
            res.append((m, tuple(int(x) for x in a[r])))
    res.sort()
    return res, fixable, tot

def main():
    n = int(sys.argv[1]); b = int(sys.argv[2]); out = sys.argv[3] if len(sys.argv) > 3 else None
    res, fixable, tot = census(n, b)
    from collections import Counter
    cnt = Counter(m for m, _ in res)
    print(f"n={n} base={b}: gap-covering rules {tot}; universal {len(res)}; "
          f"endpoints fixed by some rule {len(fixable)}; endpoints with a universal rule {len(cnt)}")
    if out:
        with open(out, 'w') as f:
            f.write("m\tF\tslots(P0,M0,P1,M1,...)\n")
            for m, a in res:
                f.write(f"{m}\t{(b**n-1)*m}\t{','.join(map(str,a))}\n")

if __name__ == '__main__':
    main()
