#!/usr/bin/python3
"""Checks for theorem_paper/sec4_odd.md (Section 4, Odd lengths).

Implements the rule M_n directly from the explicit pair lists of Definition 4.3
(word 1: lambda(P_q) at place q+n+1, lambda(M_q) at place q, letter 1 at place n;
word 2 the reverse), and cross-checks those lists against the relabeling of R_n.

Checks:
 1. Explicit lists = lambda applied to R_n; letters partition {0,2,..,2n};
    letter forms of M_3, M_4, M_5.
 2. Complete enumeration over digit multisets of length 2n+1: every
    non-repdigit reaches F = (b-1)(b^(n+1)-1), repdigits map to 0, F fixed;
    max steps against the bounds of Theorem 4.16.
 3. On every state rho (n = 3..8, b = 3..12): the image of a string with state
    rho (Definition 4.6) has the shape of Lemma 4.5; V agrees with Lemma 4.7 /
    4.11; rho' agrees with the (G)/(Z) formulas; Lemmas 4.8, 4.9, 4.12, 4.13
    hold state by state.
 4. Reduced-map orbits from every state (n = 3..8, b = 3..40 where feasible):
    longest bad run against Lemmas 4.10, 4.14, 4.15; steps to tau against
    Theorem 4.16; the run table behind the Computed note after Theorem 4.16.
Run with /usr/bin/python3.
"""
import itertools
import sys
from math import comb

ok = True


def fail(msg):
    global ok
    ok = False
    print("FAIL:", msg)


def m_pairs(n):
    """Definition 4.3, explicit lists: place q -> (lambda(P_q), lambda(M_q))."""
    p = {}
    if n % 2 == 1:
        k = (n - 1) // 2
        p[0] = (n + 1, n + 2)
        p[1] = (0, 2 * n)
        p[2] = (n, n - 1)
        for j in range(1, k):
            p[n + 1 - 2 * j] = (2 * j + 1, 2 * j)
            p[n - 2 * j] = (2 * n - 2 * j, 2 * n + 1 - 2 * j)
    else:
        k = (n - 2) // 2
        p[0] = (n - 1, n)
        p[1] = (2, 2 * n)
        p[2] = (0, 2 * n - 1)
        p[3] = (n + 2, n + 1)
        for j in range(1, k):
            p[n + 1 - 2 * j] = (2 * j + 2, 2 * j + 1)
            p[n - 2 * j] = (2 * n - 1 - 2 * j, 2 * n - 2 * j)
    assert sorted(p) == list(range(n))
    return [p[q] for q in range(n)]


def r_pairs(n):
    """R_n pairs as restated in Definition 4.3's source (Section 3)."""
    p = {}
    if n % 2 == 1:
        k = (n - 1) // 2
        p[0] = (n, n + 1); p[1] = (0, 2 * n - 1); p[2] = (n - 1, n - 2)
        for j in range(1, k):
            p[n + 1 - 2 * j] = (2 * j, 2 * j - 1)
            p[n - 2 * j] = (2 * n - 1 - 2 * j, 2 * n - 2 * j)
    else:
        k = (n - 2) // 2
        p[0] = (n - 2, n - 1); p[1] = (1, 2 * n - 1); p[2] = (0, 2 * n - 2); p[3] = (n + 1, n)
        for j in range(1, k):
            p[n + 1 - 2 * j] = (2 * j + 1, 2 * j)
            p[n - 2 * j] = (2 * n - 2 - 2 * j, 2 * n - 1 - 2 * j)
    return [p[q] for q in range(n)]


def words(n):
    """Return word1, word2 as lists: place -> letter."""
    L = 2 * n + 1
    w1 = [None] * L
    w2 = [None] * L
    for q, (P, M) in enumerate(m_pairs(n)):
        w1[q + n + 1] = P; w1[q] = M
        w2[q + n + 1] = M; w2[q] = P
    w1[n] = 1; w2[n] = 1
    return w1, w2


def apply_rule(s, w1, w2, b):
    """s: letters sorted descending (s[0] largest). Returns |word1 - word2|."""
    v1 = sum(s[w1[a]] * b ** a for a in range(len(s)))
    v2 = sum(s[w2[a]] * b ** a for a in range(len(s)))
    return abs(v1 - v2)


def digits(x, b, L):
    d = []
    for _ in range(L):
        d.append(x % b); x //= b
    assert x == 0
    return d


def r(x, b):
    return min(x, b - 1 - x)


# ---------- check 1 ----------
lam = lambda i: 0 if i == 0 else i + 1
for n in range(3, 16):
    mp = m_pairs(n)
    rp = [(lam(P), lam(M)) for (P, M) in r_pairs(n)]
    if mp != rp:
        fail(f"explicit list != lambda(R_n) at n={n}")
    letters = sorted(x for pr in mp for x in pr)
    if letters != [0] + list(range(2, 2 * n + 1)):
        fail(f"letters not a partition at n={n}")
expected = {3: "DAEBCGF-CGFBDAE", 4: "GACDBFHIE-FHIEBGACD", 5: "DIFAGBCJEKH-CJEKHBDIFAG"}
for n, e in expected.items():
    w1, w2 = words(n)
    L = 2 * n + 1
    f = lambda w: "".join(chr(65 + w[a]) for a in range(L - 1, -1, -1))
    got = f(w1) + "-" + f(w2)
    print(f"letter form n={n}: {got}", "ok" if got == e else "MISMATCH")
    if got != e:
        fail("letter form")


# ---------- check 2 ----------
def bound(n, b):
    H = (b - 1) // 2
    if n % 2 == 1:
        return H + 3
    if n == 4:
        return b + 2
    return b / 2 + 5


print("\nComplete enumeration over multisets:")
for n in (3, 4, 5):
    for b in (3, 4, 5, 7, 10):
        L = 2 * n + 1
        cnt = comb(b + L - 1, L)
        if cnt > 400000:
            print(f"  n={n} b={b}: skipped ({cnt} multisets)")
            continue
        w1, w2 = words(n)
        F = (b - 1) * (b ** (n + 1) - 1)
        nxt = {}
        for ms in itertools.combinations_with_replacement(range(b - 1, -1, -1), L):
            # combinations_with_replacement over descending range gives descending tuples
            val = apply_rule(ms, w1, w2, b)
            nxt[ms] = val
        if nxt[tuple(sorted(digits(F, b, L), reverse=True))] != F:
            fail(f"F not fixed n={n} b={b}")
        steps = {}
        maxs = 0
        for ms in nxt:
            if ms[0] == ms[-1]:
                if nxt[ms] != 0:
                    fail(f"repdigit not to 0 n={n} b={b}")
                continue
            path = []
            cur = ms
            t = 0
            while True:
                if cur in steps:
                    t += steps[cur]; break
                val = nxt[cur]
                t += 1
                path.append(cur)
                if val == F:
                    break
                cur = tuple(sorted(digits(val, b, L), reverse=True))
                if len(path) > 1000:
                    fail(f"no convergence n={n} b={b} from {ms}"); break
            # record steps for path elements
            total = t
            for i, p in enumerate(path):
                steps[p] = total - i
            maxs = max(maxs, steps[ms])
        bd = bound(n, b)
        print(f"  n={n} b={b}: {cnt} multisets, all non-repdigits reach F={F}; max steps {maxs}, bound {bd}",
              "ok" if maxs <= bd else "VIOLATION")
        if maxs > bd:
            fail("step bound")


# ---------- reduced map from the section ----------
def reduced(rho, n, b):
    """Return (V, rho') from Lemma 4.7 (n odd) or 4.11 (n even)."""
    rho = (None,) + tuple(rho)  # 1-indexed
    out = []
    if n % 2 == 1:
        k = (n - 1) // 2
        w = {j: rho[2 * j + 1] - rho[2 * j] for j in range(1, k + 1)}
        A = b - 1 - rho[1]
        V = b * A - (b * b - 1) * w[k] - sum(w[j] * (b - 1) * b ** (n - 2 * j) for j in range(1, k))
        if any(w[j] >= 1 for j in w):
            J = max(j for j in w if w[j] >= 1)
            for j in range(1, J):
                out += [max(w[j] - 1, 0)] * 2
            out += [w[J] - 1, w[J]] + [0] * (2 * (k - J)) + [rho[1]]
            case = "G"
        else:
            out = [0] * (n - 1) + [r(A - 1, b)]
            case = "Z"
    else:
        k = (n - 2) // 2
        w = {j: rho[2 * j + 2] - rho[2 * j + 1] for j in range(1, k + 1)}
        sig = b - 1 - rho[1] - rho[2]
        eta = r(sig, b)
        sig2 = b - 1 - rho[2]
        V = b * b * sig2 + b * sig - (b ** 3 - 1) * w[k] - sum(w[j] * (b - 1) * b ** (n - 2 * j) for j in range(1, k))
        if any(w[j] >= 1 for j in w):
            J = max(j for j in w if w[j] >= 1)
            for j in range(1, J):
                out += [max(w[j] - 1, 0)] * 2
            out += [w[J] - 1, w[J]] + [0] * (2 * (k - J)) + [eta, rho[2]]
            case = "G"
        elif sig >= 1:
            out = [0] * (n - 2) + [rho[2], r(sig - 1, b)]
            case = "Z"
        else:
            out = [0] * (n - 1) + [r(sig2 - 1, b)]
            case = "Z"
    assert len(out) == n
    return V, tuple(sorted(out)), case, w


def is_bad(rho, n, b):
    _, _, _, w = reduced(rho, n, b)
    if n % 2 == 1:
        return rho[0] >= 1 and all(w[j] >= 2 for j in w)
    k = (n - 2) // 2
    sig = b - 1 - rho[0] - rho[1]
    eta = r(sig, b)
    return (rho[1] >= 1 and all(w[j] >= 2 for j in range(1, k)) and w[k] >= 1
            and not (w[k] == 1 and eta == 0))


def letters_of_state(rho, n, b):
    s = [None] * (2 * n + 1)
    s[0] = b - 1
    for i in range(1, n + 1):
        s[i] = b - 1 - rho[i - 1]
        s[2 * n + 1 - i] = rho[i - 1]
    return s


def direct_next_state(rho, n, b):
    w1, w2 = words(n)
    s = letters_of_state(rho, n, b)
    L = 2 * n + 1
    # signed V directly from the pairs
    V = sum(b ** q * (s[P] - s[M]) for q, (P, M) in enumerate(m_pairs(n)))
    img = apply_rule(s, w1, w2, b)
    m = img // (b ** (n + 1) - 1)
    assert img == m * (b ** (n + 1) - 1)
    N = m - 1
    x = digits(N, b, n)
    new = tuple(sorted(r(xi, b) for xi in x))
    # Lemma 4.5 shape of the image
    srt = sorted(digits(img, b, L), reverse=True)
    if srt != letters_of_state(new, n, b):
        fail(f"shape lemma n={n} b={b} rho={rho}")
    return V, new, img


print("\nReduced maps against the direct rule, on every state:")
for n in range(3, 9):
    for b in range(3, 13):
        H = (b - 1) // 2
        tau = tuple([0] * (n - 1) + [1])
        F = (b - 1) * (b ** (n + 1) - 1)
        nst = 0
        for rho in itertools.combinations_with_replacement(range(H + 1), n):
            nst += 1
            Vd, newd, img = direct_next_state(rho, n, b)
            Vr, newr, case, w = reduced(rho, n, b)
            if Vd != Vr:
                fail(f"V n={n} b={b} rho={rho}: {Vd} vs {Vr}")
            if newd != newr:
                fail(f"rho' n={n} b={b} rho={rho}: {newd} vs {newr}")
            if rho == tau and (newr != tau or img != F):
                fail(f"tau n={n} b={b}")
            # Lemmas 4.8 / 4.12
            key = rho[0] if n % 2 == 1 else rho[1]
            if key == 0:
                r1 = reduced(newr, n, b)[1]
                if r1 != tau:
                    fail(f"from-zero lemma n={n} b={b} rho={rho}")
                if case == "Z" and newr != tau:
                    fail(f"from-zero (Z) n={n} b={b} rho={rho}")
            # Lemmas 4.9 / 4.13
            if key >= 1 and not is_bad(rho, n, b):
                k2 = newr[0] if n % 2 == 1 else newr[1]
                if k2 != 0:
                    fail(f"not-bad lemma n={n} b={b} rho={rho}")
            if is_bad(rho, n, b) and case != "G":
                fail(f"bad state not (G) n={n} b={b} rho={rho}")
        print(f"  n={n} b={b}: {nst} states ok" if ok else f"  n={n} b={b}: problems")


print("\nReduced-map orbits: longest bad run and steps (state level):")
summary = {}
for n in range(3, 9):
    for b in range(3, 41):
        H = (b - 1) // 2
        nst = comb(H + n, n)
        if nst > 60000:
            continue
        tau = tuple([0] * (n - 1) + [1])
        nxt = {}
        for rho in itertools.combinations_with_replacement(range(H + 1), n):
            nxt[rho] = reduced(rho, n, b)[1]
        maxrun = 0
        maxsteps = 0
        for rho in nxt:
            # bad runs starting anywhere
            run = 0
            cur = rho
            while is_bad(cur, n, b):
                run += 1
                cur = nxt[cur]
                if run > 10000:
                    fail("infinite bad run"); break
            maxrun = max(maxrun, run)
            # steps for a string whose first image has state rho: 1 + (time to tau) + 1
            t = 0
            cur = rho
            while cur != tau:
                cur = nxt[cur]; t += 1
                if t > 10000:
                    fail("no tau"); break
            maxsteps = max(maxsteps, t + 2)
        if n % 2 == 1:
            rb = max(0, H - 2)
        elif n == 4:
            rb = max(0, 2 * H - 2)
        else:
            rb = max(0, H - 2)
        sb = bound(n, b)
        if maxrun > rb:
            fail(f"bad-run bound n={n} b={b}: {maxrun} > {rb}")
        if maxsteps > sb:
            fail(f"step bound (state level) n={n} b={b}: {maxsteps} > {sb}")
        summary[(n, b)] = (maxrun, rb, maxsteps, sb, H)
for n in range(3, 9):
    row = [(b, v) for (nn, b), v in summary.items() if nn == n]
    mr = max(v[0] for b, v in row)
    print(f"  n={n}: bases {row[0][0]}..{row[-1][0]}; longest bad run {mr}; "
          + "; ".join(f"b={b}: run {v[0]}/{v[1]}, steps {v[2]}/{v[3]}" for b, v in row if b in (3, 4, 5, 7, 10, 11, 12, 20, 30, 40) or b == row[-1][0]))

print("\nComputed note after Theorem 4.16 (b = 3..40):")
r3 = max(summary[(3, b)][0] for b in range(3, 41))
print(f"  n=3: longest bad run {r3} (claim: at most 3)", "ok" if r3 <= 3 else "MISMATCH")
if r3 > 3:
    fail("n=3 run note")
good = all(summary[(4, b)][0] in (summary[(4, b)][4], summary[(4, b)][4] - 1) for b in range(3, 41))
print("  n=4: longest run is H or H-1 for every b:", "ok" if good else "MISMATCH",
      "| b=10:", summary[(4, 10)][0], "b=40:", summary[(4, 40)][0])
if not good or summary[(4, 10)][0] != 4 or summary[(4, 40)][0] != 18:
    fail("n=4 run note")

print("\nALL CHECKS PASS" if ok else "\nSOME CHECKS FAILED")
sys.exit(0 if ok else 1)
