"""Checks for Lemma 7.2 and Proposition 7.3 (theorem_paper/sec7_proof_corner.md).

Run: /usr/bin/python3 theorem_paper/checks/check_corner_proof.py
Output is saved next to this script as check_corner_proof_output.txt.

Notation follows the section: eps_q, gamma_q (d_q = eps_q b + gamma_q), sgn(rho),
h_k, theta_k, borrows kappa_k in {-1, 0}, u_k = max(theta_k, -1 - theta_k).

(i)   T_inf, implemented exactly as defined before Lemma 7.2 and with no reference to the
      base b, is compared with the direct rule (word 1 minus word 2 on actual digit
      strings, absolute value, re-sort, read off the deficits) for random half-swap rules
      with n = 1..6, random tuples rho with largest entry D <= 60, every base
      b = B(D), ..., B(D) + 40 with B(D) = 4D + 3, and the bases 10^6 + 3 and 10^9 + 7.
      Also tested: the zero and sign statement (a) in every admissible base, the bound
      2D + 1 of (b), and the "if and only if" of (c) in every admissible base below B(D).
      Bases just below B(D) are probed for information only.
(i')  Exhaustive version for n = 1, 2, 3 and D <= 5.
(iii) Remark (iii): a T_inf cycle with entries <= D is a T_b cycle for b >= 2D + 2
      (tested on cycles found in random rules).
(iv)  Remark (iv): the witness n = 1, pair (0, 1), rho = (D), for D = 0..300.
(v)   Remark (v): the state ((b-1)/2, ..., (b-1)/2) in odd b gets no value from the lemma.
(ii)  The three-state cycle of AFEJBGIDHC - GIDHCAFEJB by direct computation in every
      base 77 <= b <= 1200 and in the bases 100003, 1000003, 1000000007.
"""
import itertools
import os
import random
import sys

OUT_LINES = []


def out(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    OUT_LINES.append(s)


def B(D):
    return 4 * D + 3


# ---------------------------------------------------------------- base-free map
def offsets(rho):
    """Letter j of s^rho is high (value b-1-a_j) for j < n, low (value a_j) for j >= n.
    a_j = rho_{j+1} for j <= n-1 and a_j = rho_{2n-j} for j >= n (rho 1-indexed)."""
    n = len(rho)
    return [("H", rho[j]) if j < n else ("L", rho[2 * n - 1 - j]) for j in range(2 * n)]


def eps_gamma(pairs, rho):
    """(eps_q, gamma_q) from the table of the section."""
    let = offsets(rho)
    res = []
    for P, M in pairs:
        (tP, aP), (tM, aM) = let[P], let[M]
        if tP == "H" and tM == "H":
            res.append((0, aM - aP))
        elif tP == "L" and tM == "L":
            res.append((0, aP - aM))
        elif tP == "H":
            res.append((1, -1 - aP - aM))
        else:
            res.append((-1, 1 + aP + aM))
    return res


def sgn_rho(pairs, rho):
    for e, g in reversed(eps_gamma(pairs, rho)):
        if (e, g) != (0, 0):
            return e if e != 0 else (1 if g > 0 else -1)
    return 0


def T_inf(pairs, rho):
    """Returns (sgn(rho), image tuple or None, list of theta_k). No base appears."""
    n = len(rho)
    sg = sgn_rho(pairs, rho)
    if sg == 0:
        return 0, None, None
    eg = [(sg * e, sg * g) for e, g in eps_gamma(pairs, rho)]
    kappa = 0
    thetas, us = [], []
    for k in range(n):
        h = eg[k][1] + (eg[k - 1][0] if k >= 1 else 0) - (1 if k == 0 else 0)
        theta = h + kappa
        kappa = -1 if theta < 0 else 0
        thetas.append(theta)
        us.append(max(theta, -1 - theta))
    return sg, tuple(sorted(us)), thetas


def admissible(pairs, rho, b):
    """b >= 2D+1 and b - 1 > a_P + a_M for every mixed pair."""
    if b < 2 * max(rho) + 1:
        return False
    let = offsets(rho)
    for P, M in pairs:
        if let[P][0] != let[M][0] and not (b - 1 > let[P][1] + let[M][1]):
            return False
    return True


def has_mixed(pairs, n):
    return any((P < n) != (M < n) for P, M in pairs)


# ---------------------------------------------------------------- direct rule
def direct(pairs, rho, b):
    """Returns (V, state of K(s^rho) or None), using actual digit strings in base b."""
    n = len(rho)
    s = sorted([b - 1 - r for r in rho] + list(rho), reverse=True)   # letters s_0 >= ... >= s_{2n-1}
    assert s == [b - 1 - rho[i] for i in range(n)] + [rho[n - 1 - i] for i in range(n)]
    w1 = w2 = 0
    for q, (P, M) in enumerate(pairs):
        w1 += s[P] * b ** (q + n) + s[M] * b ** q
        w2 += s[M] * b ** (q + n) + s[P] * b ** q
    V = sum(b ** q * (s[P] - s[M]) for q, (P, M) in enumerate(pairs))
    K = abs(w1 - w2)
    assert K == (b ** n - 1) * abs(V) and K < b ** (2 * n)
    if V == 0:
        return 0, None
    digs = [(K // b ** i) % b for i in range(2 * n)]
    letters = sorted(digs, reverse=True)
    state = tuple(letters[2 * n - i] for i in range(1, n + 1))       # rho_i = s_{2n-i}
    # cross-check with Lemma 5.6: the top n digits are N = |V| - 1, and their deficits give the state
    N = abs(V) - 1
    assert tuple(digs[n:]) == tuple((N // b ** i) % b for i in range(n))
    assert tuple(sorted(min(x, b - 1 - x) for x in digs[n:])) == state
    return V, state


def sgn(x):
    return (x > 0) - (x < 0)


def random_rule(n, rng):
    idx = list(range(2 * n))
    rng.shuffle(idx)
    return [(idx[2 * q], idx[2 * q + 1]) for q in range(n)]


def random_rho(n, D, rng):
    if rng.random() < 0.3:   # many ties and extremes
        vals = [rng.choice([0, D, D, rng.randint(0, D)]) for _ in range(n - 1)]
    else:
        vals = [rng.randint(0, D) for _ in range(n - 1)]
    return tuple(sorted(vals + [D]))


def check_iff_c(pairs, rho, b, sg, img):
    """Lemma 7.2(a) and the 'if and only if' of 7.2(c) at an admissible base b. Returns #failures."""
    bad = 0
    V, st = direct(pairs, rho, b)
    if sgn(V) != sg:
        bad += 1
    if sg != 0:
        cond = b >= 2 * max(img) + 1
        if cond != (st == img):
            bad += 1
    return bad


# ================================================================ part (i)
def part_i():
    rng = random.Random(60714)
    HUGE = [10 ** 6 + 3, 10 ** 9 + 7]
    n_rules = 3000
    tuples_per_rule = 4
    mism = sign_bad = bound_bad = iff_bad = 0
    evals = iff_evals = zero_seen = attain = 0
    worst_fail = {}
    for it in range(n_rules):
        n = 1 + it % 6
        pairs = random_rule(n, rng)
        for _ in range(tuples_per_rule):
            D = rng.choice([0, 1, 2, 3, rng.randint(0, 60), rng.randint(0, 60), 60])
            rho = random_rho(n, D, rng)
            sg, img, _ = T_inf(pairs, rho)
            if sg == 0:
                zero_seen += 1
            else:
                if max(img) > 2 * D + 1:
                    bound_bad += 1
                if max(img) == 2 * D + 1:
                    attain += 1
            for b in list(range(B(D), B(D) + 41)) + HUGE:
                V, st = direct(pairs, rho, b)
                evals += 1
                if sgn(V) != sg:
                    sign_bad += 1
                if V != 0 and st != img:
                    mism += 1
            for b in range(max(2, 2 * D + 1), B(D)):
                if admissible(pairs, rho, b):
                    iff_evals += 1
                    iff_bad += check_iff_c(pairs, rho, b, sg, img)
                V, st = direct(pairs, rho, b)
                if not ((sgn(V) == sg) and (V == 0 or st == img)):
                    worst_fail[D] = max(worst_fail.get(D, -1), b)
    out("(i) random half-swap rules, n = 1..6:", n_rules, " tuples per rule:", tuples_per_rule,
        " direct evaluations at b in [B(D), B(D)+40] and 10^6+3, 10^9+7:", evals)
    out("    T_inf vs direct mismatches:", mism)
    out("    Lemma 7.2(a) sign/zero failures:", sign_bad, " (tuples with sgn(rho) = 0 seen:", zero_seen, ")")
    out("    Lemma 7.2(b) image entries exceeding 2D+1:", bound_bad,
        " (tuples whose image attains 2D+1:", attain, ")")
    out("    Lemma 7.2(a) and 7.2(c) 'if and only if' at admissible b in [2D+1, 4D+2]:",
        iff_evals, "evaluations, failures:", iff_bad)
    tight = sorted(D for D, wb in worst_fail.items() if wb == B(D) - 1)
    out("    [info] probe below B(D): sampled D values with a failure at b = 4D+2:", len(tight),
        "of", len(set(worst_fail) | set(tight)), "with any failure (e.g. D =", tight[:8], ")")
    return mism == 0 and sign_bad == 0 and bound_bad == 0 and iff_bad == 0, pairs


def part_i_exhaustive():
    """All half-swap rules for n = 1, 2, 3 and all nondecreasing rho with D <= 5:
    b = B(D)..B(D)+3, and (a) and the iff of (c) at every admissible b in [2D+1, 4D+2]."""
    bad = cnt = 0
    for n in (1, 2, 3):
        rules = set()
        for perm in itertools.permutations(range(2 * n)):
            rules.add(tuple((perm[2 * q], perm[2 * q + 1]) for q in range(n)))
        for pairs in rules:
            for D in range(0, 6):
                for rest in itertools.combinations_with_replacement(range(D + 1), n - 1):
                    rho = tuple(sorted(rest + (D,)))
                    sg, img, _ = T_inf(pairs, rho)
                    if img is not None and max(img) > 2 * D + 1:
                        bad += 1
                    for b in range(B(D), B(D) + 4):
                        V, st = direct(pairs, rho, b)
                        cnt += 1
                        if sgn(V) != sg or (V != 0 and st != img):
                            bad += 1
                    for b in range(max(2, 2 * D + 1), B(D)):
                        if admissible(pairs, rho, b):
                            cnt += 1
                            bad += check_iff_c(pairs, rho, b, sg, img)
    out("(i') exhaustive: all rules n = 1, 2, 3, all rho with D <= 5, b = B(D)..B(D)+3 and all",
        "admissible b below B(D):", cnt, "evaluations, failures:", bad)
    return bad == 0


# ================================================================ remarks (iii), (iv), (v)
def remark_iii():
    """Find T_inf cycles in random rules and check they are T_b cycles for b = 2D+2..2D+30,
    and at b = 2D+1 exactly when (c) is applicable to every state (admissible for all)."""
    rng = random.Random(7)
    found = bad = 0
    for it in range(4000):
        n = 1 + it % 5
        pairs = random_rule(n, rng)
        rho = tuple(sorted(rng.randint(0, 12) for _ in range(n)))
        seen = []
        cur = rho
        for _ in range(60):
            sg, img, _ = T_inf(pairs, cur)
            if sg == 0:
                cur = None
                break
            if cur in seen:
                break
            seen.append(cur)
            cur = img
        if cur is None or cur not in seen:
            continue
        cyc = seen[seen.index(cur):]
        found += 1
        D = max(max(r) for r in cyc)
        bases = list(range(2 * D + 2, 2 * D + 31))
        if all(admissible(pairs, r, 2 * D + 1) for r in cyc):
            bases.append(2 * D + 1)
        for b in bases:
            for r in cyc:
                V, st = direct(pairs, r, b)
                if V == 0 or st != T_inf(pairs, r)[1]:
                    bad += 1
    out("(iii) Remark (iii): T_inf cycles found in random rules:", found, " failures as T_b cycles:", bad)
    return found > 0 and bad == 0


def remark_iv():
    bad = 0
    pairs = [(0, 1)]
    for D in range(0, 301):
        rho = (D,)
        sg, img, thetas = T_inf(pairs, rho)
        eg = eps_gamma(pairs, rho)
        b = 4 * D + 2
        ok = (eg == [(1, -1 - 2 * D)] and sg == 1 and thetas == [-2 * D - 2]
              and img == (2 * D + 1,) and admissible(pairs, rho, b) and (b - 1) // 2 == 2 * D)
        V, st = direct(pairs, rho, b)
        ok = ok and V == 2 * D + 1 and st == (2 * D,) and st != img
        V2, st2 = direct(pairs, rho, B(D))            # and the lemma holds at B(D)
        ok = ok and st2 == img
        bad += not ok
    out("(iv) Remark (iv) witness n = 1, pair (0,1), rho = (D), D = 0..300: T_inf = (2D+1),",
        "base 4D+2 admissible with T_b = (2D), base 4D+3 gives (2D+1); failures:", bad)
    return bad == 0


def remark_v():
    rng = random.Random(11)
    bad = cnt = 0
    for it in range(3000):
        n = 1 + it % 6
        pairs = random_rule(n, rng)
        b = 2 * rng.randint(1, 60) + 1
        D = (b - 1) // 2
        rho = (D,) * n
        adm = admissible(pairs, rho, b)
        sg = sgn_rho(pairs, rho)
        V, _ = direct(pairs, rho, b)
        cnt += 1
        if has_mixed(pairs, n):
            bad += adm                                   # not admissible
        else:
            bad += (not adm) or sg != 0 or V != 0        # admissible, sgn = 0, V = 0
    out("(v) Remark (v): state ((b-1)/2, ...) in odd b, random rules:", cnt, " failures:", bad)
    return bad == 0


# ================================================================ part (ii)
def rule_from_words(w1, w2):
    L = len(w1)
    n = L // 2
    place1 = {ch: L - 1 - i for i, ch in enumerate(w1)}
    place2 = {ch: L - 1 - i for i, ch in enumerate(w2)}
    P, M = [None] * n, [None] * n
    for ch in w1:
        letter = ord(ch) - 65
        p1, p2 = place1[ch], place2[ch]
        assert abs(p1 - p2) == n          # every letter moves exactly n places
        if p1 >= n:
            P[p1 - n] = letter            # P_q sits at place q+n of word 1
        else:
            M[p1] = letter                # M_q sits at place q of word 1
    return list(zip(P, M))


def full_step(pairs, s, b):
    """One application of K to a sorted digit tuple (descending); returns sorted digits."""
    n = len(pairs)
    V = sum(b ** q * (s[P] - s[M]) for q, (P, M) in enumerate(pairs))
    K = (b ** n - 1) * abs(V)
    return tuple(sorted(((K // b ** i) % b for i in range(2 * n)), reverse=True))


def universal(pairs, b):
    L = 2 * len(pairs)
    memo = {}
    ends = set()
    for t in itertools.combinations_with_replacement(range(b - 1, -1, -1), L):
        if t[0] == t[-1]:
            continue
        path = []
        cur = t
        seen = set()
        while cur not in memo and cur not in seen:
            seen.add(cur)
            path.append(cur)
            cur = full_step(pairs, cur, b)
        if cur in memo:
            res = memo[cur]
        else:
            res = cur if full_step(pairs, cur, b) == cur else None
        for p in path:
            memo[p] = res
        if res is None:
            return False
        ends.add(res)
    return len(ends) == 1


def part_ii():
    ok = True
    pairs = rule_from_words("AFEJBGIDHC", "GIDHCAFEJB")
    out("(ii) rule AFEJBGIDHC - GIDHCAFEJB, pairs (P_q, M_q), q = 0..4:", pairs)
    ok &= pairs == [(1, 2), (9, 7), (4, 3), (5, 8), (0, 6)]
    cyc = [(13, 13, 15, 25, 31), (1, 1, 6, 17, 38), (4, 4, 18, 21, 36)]
    for i, rho in enumerate(cyc):
        sg, img, thetas = T_inf(pairs, rho)
        out("    T_inf", rho, "-> sgn", sg, " theta =", thetas, " image", img)
        ok &= sg == 1 and img == cyc[(i + 1) % 3]
    # hypotheses of Lemma 7.2(c) at b = 77, with the numbers quoted in the proof
    nums = []
    for rho in cyc:
        sg, img, _ = T_inf(pairs, rho)
        ok &= admissible(pairs, rho, 77) and 77 >= 2 * max(img) + 1
        nums.append((2 * max(rho) + 1, rho[0] + rho[3], 2 * max(img) + 1))
    ok &= nums == [(63, 38, 77), (77, 18, 73), (73, 25, 63)]
    out("    Lemma 7.2(c) hypotheses at b = 77 (2D+1, rho_1+rho_4, 2 max T_inf + 1):", nums, ok)
    bad = []
    bases = list(range(77, max(B(38), 1200) + 1)) + [100003, 1000003, 1000000007]
    for b in bases:
        s0 = tuple(sorted([b - 1 - r for r in cyc[0]] + list(cyc[0]), reverse=True))
        if s0[0] == s0[-1]:
            bad.append(b)
            continue
        s = s0
        states = []
        for k in range(3):
            s = full_step(pairs, s, b)
            states.append(tuple(sorted(s[5:])))
            if s != tuple(sorted([b - 1 - r for r in states[-1]] + list(states[-1]), reverse=True)):
                bad.append(b)
        if states != [cyc[1], cyc[2], cyc[0]]:
            bad.append(b)
        if full_step(pairs, s, b) == s:
            bad.append(b)
    out("    direct cycle check in every base 77 ..", max(B(38), 1200),
        "and in 100003, 1000003, 1000000007 (", len(bases), "bases): failures:", sorted(set(bad))[:10])
    ok &= not bad
    ok &= all((b - 1) // 2 < 38 for b in range(2, 77)) and (77 - 1) // 2 == 38
    u10 = universal(pairs, 10)
    out("    rule universal in base 10 (complete enumeration of 10-digit multisets):", u10)
    ok &= u10
    return ok


if __name__ == "__main__":
    r1, _ = part_i()
    r1b = part_i_exhaustive()
    r3 = remark_iii()
    r4 = remark_iv()
    r5 = remark_v()
    r2 = part_ii()
    allok = r1 and r1b and r3 and r4 and r5 and r2
    out("ALL CHECKS PASS" if allok else "SOME CHECK FAILED")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "check_corner_proof_output.txt"), "w") as f:
        f.write("\n".join(OUT_LINES) + "\n")
    sys.exit(0 if allok else 1)
