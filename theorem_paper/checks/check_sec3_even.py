#!/usr/bin/python3
"""Checks for theorem_paper/sec3_even.md (Section 3, Even lengths).

Implements the half-swap rule R_n directly from Definition 3.2 of the section
(pairs (P_q, M_q) at place q; word 1 has P_q at place q+n and M_q at place q;
word 2 the reverse), independently of the audit source files.

Checks:
 1. Letter forms of R_3, R_4, R_5.
 2. Complete enumeration over digit multisets: every non-repdigit reaches
    F = (b-1)(b^n-1), repdigits map to 0, F is fixed; maximum number of steps
    compared with the bounds of Theorem 3.3.
 3. On every state rho (n = 3..6, b = 3..12, all states but the repdigit
    state), the reduced-map formulas (V and rho') of Lemmas 3.9 and 3.15
    agree with the direct rule.
 4. Reduced-map iteration over all states for larger bases: longest bad run
    against Lemmas 3.13 and 3.14, and steps from a state to tau.
Run with /usr/bin/python3.
"""
import itertools
import sys
from math import comb


def rule_pairs(n):
    """Return list of (P_q, M_q) for q = 0..n-1, from Definition 3.2."""
    pairs = {}
    if n % 2 == 1:
        k = (n - 1) // 2
        pairs[0] = (n, n + 1)
        pairs[1] = (0, 2 * n - 1)
        pairs[2] = (n - 1, n - 2)
        for j in range(1, k):
            pairs[n + 1 - 2 * j] = (2 * j, 2 * j - 1)
            pairs[n - 2 * j] = (2 * n - 1 - 2 * j, 2 * n - 2 * j)
    else:
        k = (n - 2) // 2
        pairs[0] = (n - 2, n - 1)
        pairs[1] = (1, 2 * n - 1)
        pairs[2] = (0, 2 * n - 2)
        pairs[3] = (n + 1, n)
        for j in range(1, k):
            pairs[n + 1 - 2 * j] = (2 * j + 1, 2 * j)
            pairs[n - 2 * j] = (2 * n - 2 - 2 * j, 2 * n - 1 - 2 * j)
    assert sorted(pairs) == list(range(n)), (n, sorted(pairs))
    letters = sorted(x for p in pairs.values() for x in p)
    assert letters == list(range(2 * n)), (n, letters)
    return [pairs[q] for q in range(n)]


def letter_form(n):
    pr = rule_pairs(n)
    L = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    w1 = [None] * (2 * n)
    w2 = [None] * (2 * n)
    for q, (P, M) in enumerate(pr):
        w1[q + n], w1[q] = L[P], L[M]
        w2[q + n], w2[q] = L[M], L[P]
    # most significant place first
    return "".join(reversed(w1)), "".join(reversed(w2))


def digits(x, b, length):
    out = []
    for _ in range(length):
        out.append(x % b)
        x //= b
    assert x == 0
    return out


def K_sorted(s, b, pr):
    """s sorted descending (s[0] largest); returns K = |word1 - word2|."""
    n = len(pr)
    w1 = 0
    w2 = 0
    for q, (P, M) in enumerate(pr):
        w1 += s[P] * b ** (q + n) + s[M] * b ** q
        w2 += s[M] * b ** (q + n) + s[P] * b ** q
    return abs(w1 - w2)


def V_sorted(s, b, pr):
    return sum(b ** q * (s[P] - s[M]) for q, (P, M) in enumerate(pr))


def sorted_digits(x, b, n):
    return tuple(sorted(digits(x, b, 2 * n), reverse=True))


def r(x, b):
    return min(x, b - 1 - x)


def state_of_value(K, b, n):
    m = K // (b ** n - 1)
    assert K == m * (b ** n - 1)
    N = m - 1
    return tuple(sorted(r(x, b) for x in digits(N, b, n)))


def multiset_of_state(rho, b):
    s = [b - 1 - x for x in rho] + [x for x in rho]
    return tuple(sorted(s, reverse=True))


# ---------- reduced maps exactly as written in the section ----------

def reduced_odd(rho, b):
    n = len(rho)
    k = (n - 1) // 2
    R = (None,) + tuple(rho)  # 1-based
    w = {j: R[2 * j + 1] - R[2 * j] for j in range(1, k + 1)}
    A = b - 1 - 2 * R[1]
    g = r(A, b)
    V = b * A - (b * b - 1) * w[k] - sum(w[j] * (b - 1) * b ** (n - 2 * j) for j in range(1, k))
    if any(w[j] >= 1 for j in w):
        J = max(j for j in w if w[j] >= 1)
        new = []
        for j in range(1, J):
            new += [max(w[j] - 1, 0)] * 2
        new += [w[J] - 1, w[J]]
        new += [0] * (2 * (k - J))
        new += [g]
        case = "G"
    else:
        assert A >= 1
        new = [0] * (n - 1) + [r(A - 1, b)]
        case = "Z"
    assert len(new) == n
    return V, tuple(sorted(new)), case


def reduced_even(rho, b):
    n = len(rho)
    k = (n - 2) // 2
    R = (None,) + tuple(rho)
    w = {j: R[2 * j + 2] - R[2 * j + 1] for j in range(1, k + 1)}
    sig = b - 1 - R[1] - R[2]
    h = r(sig, b)
    V = (b * b + b) * sig - (b ** 3 - 1) * w[k] - sum(w[j] * (b - 1) * b ** (n - 2 * j) for j in range(1, k))
    if any(w[j] >= 1 for j in w):
        J = max(j for j in w if w[j] >= 1)
        new = []
        for j in range(1, J):
            new += [max(w[j] - 1, 0)] * 2
        new += [w[J] - 1, w[J]]
        new += [0] * (2 * (k - J))
        new += [h, h]
        case = "G"
    else:
        assert sig >= 1
        new = [0] * (n - 2) + [r(sig, b), r(sig - 1, b)]
        case = "Z"
    assert len(new) == n
    return V, tuple(sorted(new)), case


def reduced(rho, b):
    return reduced_odd(rho, b) if len(rho) % 2 else reduced_even(rho, b)


def is_bad_odd(rho):
    n = len(rho)
    k = (n - 1) // 2
    R = (None,) + tuple(rho)
    return R[1] >= 1 and all(R[2 * j + 1] - R[2 * j] >= 2 for j in range(1, k + 1))


def bound_steps(n, b):
    if n % 2 == 0:
        return 7
    if n == 3:
        return b / 2 + 10
    return b / 3 + 9


def main():
    ok = True
    # 1. letter forms
    expected = {3: ("CADBFE", "BFECAD"), 4: ("FABCEGHD", "EGHDFABC"), 5: ("CHEAFBIDJG", "BIDJGCHEAF")}
    for n, e in expected.items():
        got = letter_form(n)
        print(f"letter form n={n}: {got[0]} - {got[1]}", "OK" if got == e else "MISMATCH")
        ok &= got == e

    # 2. complete enumeration over multisets
    print("\nDirect enumeration over digit multisets (max steps vs bound):")
    for n in (3, 4, 5, 6):
        pr = rule_pairs(n)
        for b in (3, 4, 5, 7, 10):
            count = comb(2 * n + b - 1, b - 1)
            if count > 400000:
                print(f"  n={n} b={b}: skipped ({count} multisets)")
                continue
            F = (b - 1) * (b ** n - 1)
            Fs = sorted_digits(F, b, n)
            assert K_sorted(Fs, b, pr) == F
            cache = {}
            maxsteps = 0
            for combo in itertools.combinations_with_replacement(range(b - 1, -1, -1), 2 * n):
                s = tuple(combo)  # nonincreasing
                if s[0] == s[-1]:
                    if K_sorted(s, b, pr) != 0:
                        ok = False
                        print("  repdigit not to 0", s)
                    continue
                # iterate
                path = []
                cur = s
                steps = 0
                val = None
                while True:
                    val = K_sorted(cur, b, pr)
                    steps += 1
                    if val == F:
                        break
                    if steps > 200:
                        ok = False
                        print("  no convergence", n, b, s)
                        break
                    cur = sorted_digits(val, b, n)
                maxsteps = max(maxsteps, steps)
            bd = bound_steps(n, b)
            flag = "OK" if maxsteps <= bd else "BOUND VIOLATED"
            ok &= maxsteps <= bd
            print(f"  n={n} b={b}: {count} multisets, all non-repdigits reach F={F}; max steps {maxsteps} (bound {bd:g}) {flag}")

    # 3. reduced maps vs direct rule on all states
    print("\nReduced-map formulas vs direct rule, all states, n=3..6, b=3..12:")
    for n in (3, 4, 5, 6):
        pr = rule_pairs(n)
        for b in range(3, 13):
            H = (b - 1) // 2
            nst = 0
            for rho in itertools.combinations_with_replacement(range(H + 1), n):
                if b % 2 == 1 and all(x == H for x in rho):
                    continue  # repdigit state, excluded
                s = multiset_of_state(rho, b)
                Vd = V_sorted(s, b, pr)
                Kd = K_sorted(s, b, pr)
                Vr, newr, case = reduced(rho, b)
                newd = state_of_value(Kd, b, n)
                if Vd != Vr or newd != newr or Kd != (b ** n - 1) * abs(Vr):
                    ok = False
                    print("  MISMATCH", n, b, rho, Vd, Vr, newd, newr, case)
                nst += 1
            print(f"  n={n} b={b}: {nst} states agree")

    # 4. reduced-map iteration over all states, larger bases
    print("\nReduced-map iteration from every state (bad runs and steps to tau):")
    for n, bases in ((3, range(3, 202)), (4, range(3, 60)), (5, range(3, 40)), (6, range(3, 26)), (7, range(3, 20))):
        worst_run = 0
        worst_run_b = None
        worst_steps = {}
        for b in bases:
            H = (b - 1) // 2
            tau = tuple([0] * (n - 1) + [1])
            ms = 0
            for rho in itertools.combinations_with_replacement(range(H + 1), n):
                if b % 2 == 1 and all(x == H for x in rho):
                    continue
                cur = rho
                steps = 0
                run = 0
                maxrun = 0
                while cur != tau:
                    if n % 2 == 1:
                        if is_bad_odd(cur):
                            run += 1
                            maxrun = max(maxrun, run)
                        else:
                            run = 0
                    cur = reduced(cur, b)[1]
                    steps += 1
                    if steps > 10 * b + 50:
                        ok = False
                        print("  no tau", n, b, rho)
                        break
                ms = max(ms, steps)
                if n % 2 == 1:
                    if n == 3:
                        bd = (b + 7) / 2
                    else:
                        H5 = 2 * (H - 5) / 3 + 2
                        bd = H5
                    if maxrun > bd and maxrun > 0:
                        ok = False
                        print("  BAD RUN BOUND VIOLATED", n, b, rho, maxrun, bd)
                    if maxrun > worst_run:
                        worst_run, worst_run_b = maxrun, b
                    # state-to-tau bound: run + 4 (one step off bad, <=2 to tau, and the run steps)
                    if steps > maxrun + 3:
                        ok = False
                        print("  STATE STEP BOUND VIOLATED", n, b, rho, steps, maxrun)
            worst_steps[b] = ms
            if n % 2 == 0:
                lim = 5 if n == 4 else 4
                if ms > lim:
                    ok = False
                    print("  EVEN STATE STEP BOUND VIOLATED", n, b, ms)
        top = max(worst_steps.values())
        extra = f", longest bad run {worst_run} (at b={worst_run_b})" if n % 2 else ""
        print(f"  n={n}, b={bases.start}..{bases.stop - 1}: all states reach tau; max state-to-tau steps {top}{extra}")

    print("\nALL CHECKS PASS" if ok else "\nSOME CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
