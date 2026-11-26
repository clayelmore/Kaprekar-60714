#!/usr/bin/python3
"""Checks for theorem_paper/sec7_proof_family.md (Proposition 7.1).

Rule GFEABDHC - HGDFCEAB at length 8, base b = 5t. Notation as in the paper:
X1..X4 the four sorted strings, W = word 1 - word 2, kappa_k the borrows.

 1. Step 0: every inequality stated for X1..X4 (bounds and consecutive
    differences) is linear in t; it is checked to hold for all integers
    t >= its stated threshold (coefficient >= 0 and value at the threshold
    >= 0), and the threshold is checked to be sharp. The maximum threshold
    is t0 = 10.
 2. For each step X_i -> X_{i+1}: the place differences d_k computed from the
    two words agree with the table in the paper; e_k = d_k + b*kappa_k -
    kappa_{k-1} with the stated borrows; sum e_k b^k = sum d_k b^k = word 1 -
    word 2 = the stated expansion of W_i, all as polynomial identities in t;
    b - 1 divides W_i; each e_k equals the stated letter of X_{i+1}, and the
    stated letters are a permutation; some e_k >= 1 for t >= t0, so W_i > 0.
 3. The four strings are pairwise distinct for every t >= t0 (period exactly 4).
 4. Direct iteration of the rule, implemented from the words with integer
    arithmetic, for every t from 10 to 2000: K(X_i) sorts to X_{i+1}, and for
    a string x with sorted digits X1, K^5(x) = K(x) and K(x), ..., K^4(x) are
    four distinct strings.
 5. Below the threshold: for 1 <= t <= 9 the displayed X1 is not weakly
    decreasing; for 4 <= t <= 9 the steps X2 -> X3 -> X4 still hold, K(X4)
    sorts to the descending rearrangement of the entries of X1 (not equal to
    X1), and the orbit ends at the fixed point whose sorted digits are
    (b-1, b-1, b-2, 1, 0, 0, 0, 0).

Prints ALL CHECKS PASS only if everything holds. Run with /usr/bin/python3.
"""
import sympy as sp

t = sp.symbols("t")
b = 5 * t
W1, W2 = "GFEABDHC", "HGDFCEAB"   # most significant place first
T0 = 10
ok = True


def fail(msg):
    global ok
    ok = False
    print("FAIL:", msg)


def X(tv):
    return {
        1: (4*tv - 3, 3*tv + 7, 3*tv + 3, 2*tv - 6, 2*tv - 7, tv + 2, 1, 0),
        2: (5*tv - 1, 5*tv - 4, 3*tv - 5, tv + 2, tv, 4, 1, 0),
        3: (5*tv - 2, 5*tv - 5, 3*tv - 1, 2*tv + 1, 2, 1, 1, 0),
        4: (5*tv - 1, 5*tv - 3, 3*tv + 4, 3*tv + 1, 2*tv - 2, 2*tv - 4, 1, 0),
    }


XS = X(t)
NXT = {1: 2, 2: 3, 3: 4, 4: 1}


def lin_holds_from(expr, start, strict=False):
    """expr = a*t + c (linear); True iff expr >= 0 (or > 0) for all integers t >= start."""
    poly = sp.Poly(sp.expand(expr), t)
    if poly.degree() > 1:
        return False
    a = poly.coeff_monomial(t)
    v = sp.sympify(expr).subs(t, start)
    return a >= 0 and (v > 0 if strict else v >= 0)


# ---------------------------------------------------------------- 1. Step 0
# For each X_i: (b-1-s_0, s_0-s_1, ..., s_6-s_7, s_7) with the stated
# smallest integer t from which each is >= 0 (None: holds for every t >= 1).
STEP0 = {
    1: [(t + 2, None), (t - 10, 10), (4, None), (t + 9, None), (1, None),
        (t - 9, 9), (t + 1, None), (1, None), (0, None)],
    2: [(0, None), (3, None), (2*t + 1, None), (2*t - 7, 4), (2, None),
        (t - 4, 4), (3, None), (1, None), (0, None)],
    3: [(1, None), (3, None), (2*t - 4, 2), (t - 2, 2), (2*t - 1, None),
        (1, None), (0, None), (1, None), (0, None)],
    4: [(0, None), (2, None), (2*t - 7, 4), (3, None), (t + 3, None),
        (2, None), (2*t - 5, 3), (1, None), (0, None)],
}
thresholds = []
for i in range(1, 5):
    s = XS[i]
    actual = [sp.expand(b - 1 - s[0])] + [sp.expand(s[j] - s[j+1]) for j in range(7)] + [sp.expand(s[7])]
    stated = [sp.expand(e) for e, _ in STEP0[i]]
    if actual != stated:
        fail(f"Step 0 expressions for X{i}: {actual} != {stated}")
    for (e, th) in STEP0[i]:
        e = sp.sympify(e)
        if th is None:            # holds for every t >= 1 (no sharp threshold)
            if not lin_holds_from(e, 1):
                fail(f"X{i}: {e} >= 0 not proved for all t >= 1")
            continue
        thresholds.append(th)
        if not lin_holds_from(e, th):
            fail(f"X{i}: {e} >= 0 not proved for t >= {th}")
        if e.subs(t, th - 1) >= 0:
            fail(f"X{i}: threshold {th} for {e} >= 0 is not sharp")
if max(thresholds) != T0:
    fail(f"max threshold {max(thresholds)} != {T0}")
print("Step 0: all", sum(len(v) for v in STEP0.values()),
      "inequalities hold from their stated (sharp) thresholds; overall t0 =", max(thresholds))

# ---------------------------------------------------------------- 2. steps
# Tables of the paper, places listed 7, 6, ..., 0.
TABLE = {
    1: dict(d=[1, t + 1, -1, 3*t - 5, 4, 1, 3 - 4*t, -4],
            kappa=[0, 0, 1, 0, 0, 0, 1, 1],
            e=[1, t, 5*t - 1, 3*t - 5, 4, 0, t + 2, 5*t - 4],
            let="GEACFHDB",
            W=93750*t**7 + 15625*t**6 - 1250*t**5 - 3125*t**4 + 500*t**3 + 5*t**2 + 15*t - 4),
    2: dict(d=[1, 3, -2, 5*t - 5, 2*t + 1, 2, 1 - 5*t, -2*t - 1],
            kappa=[0, 0, 1, 0, 0, 0, 1, 1],
            e=[1, 2, 5*t - 2, 5*t - 5, 2*t + 1, 1, 0, 3*t - 1],
            let="FEABDGHC",
            W=78125*t**7 + 46875*t**6 - 3125*t**5 - 2875*t**4 + 125*t**3 + 25*t**2 + 3*t - 1),
    3: dict(d=[1, 0, 1 - 2*t, 5*t - 3, 2*t - 4, 2*t - 1, 2 - 5*t, 4 - 2*t],
            kappa=[0, 1, 1, 0, 0, 0, 1, 1],
            e=[0, 5*t - 1, 3*t + 1, 5*t - 3, 2*t - 4, 2*t - 2, 1, 3*t + 4],
            let="HADBFEGC",
            W=78125*t**7 - 6250*t**6 + 6250*t**5 - 1625*t**4 - 450*t**3 - 50*t**2 + 8*t + 4),
    4: dict(d=[1, 2*t - 5, -t - 3, 3*t + 3, 2*t - 7, t + 3, 1 - 5*t, 7 - 2*t],
            kappa=[0, 0, 1, 0, 0, 0, 1, 1],
            e=[1, 2*t - 6, 4*t - 3, 3*t + 3, 2*t - 7, t + 2, 0, 3*t + 7],
            let="GDACEFHB",
            W=109375*t**7 - 81250*t**6 - 7500*t**5 + 2125*t**4 - 850*t**3 + 50*t**2 + 3*t + 7),
}
for i in range(1, 5):
    s, T = XS[i], TABLE[i]
    val = lambda ch: s[ord(ch) - 65]
    d = [sp.expand(val(W1[j]) - val(W2[j])) for j in range(8)]          # places 7..0
    if d != [sp.expand(x) for x in T["d"]]:
        fail(f"step {i}: d {d}")
    kap = T["kappa"] + [0]            # kappa_{-1} = 0 appended; kap[0] is kappa_7
    if kap[0] != 0:
        fail(f"step {i}: kappa_7 != 0")
    for j in range(8):                # place k = 7 - j; kappa_{k-1} = kap[j+1]
        if sp.expand(d[j] + b*kap[j] - kap[j+1] - T["e"][j]) != 0:
            fail(f"step {i}: e at place {7-j}")
    word1 = sum(val(W1[j]) * b**(7 - j) for j in range(8))
    word2 = sum(val(W2[j]) * b**(7 - j) for j in range(8))
    sum_d = sum(d[j] * b**(7 - j) for j in range(8))
    sum_e = sum(T["e"][j] * b**(7 - j) for j in range(8))
    for name, a, c in [("word1-word2 = sum d", word1 - word2, sum_d),
                       ("sum e = sum d", sum_e, sum_d),
                       (f"W{i} expansion", T["W"], sum_d)]:
        if sp.expand(a - c) != 0:
            fail(f"step {i}: identity {name}")
    if sp.expand(T["W"]).subs(t, sp.Rational(1, 5)) != 0:
        fail(f"step {i}: b-1 does not divide W{i}")
    nxt = XS[NXT[i]]
    if sorted(T["let"]) != list("ABCDEFGH"):
        fail(f"step {i}: letters not a permutation")
    for j in range(8):
        if sp.expand(T["e"][j] - nxt[ord(T["let"][j]) - 65]) != 0:
            fail(f"step {i}: e at place {7-j} != letter {T['let'][j]} of X{NXT[i]}")
    # W > 0: some digit is >= 1 for all t >= T0 (all digits are >= 0 by Step 0)
    if not any(lin_holds_from(e - 1, T0) for e in map(sp.sympify, T["e"])):
        fail(f"step {i}: no digit >= 1")
    print(f"step {i}: X{i} -> X{NXT[i]}: differences, borrows kappa, digits, identities, "
          f"W{i} expansion, letters verified")

# ---------------------------------------------------------------- 3. distinct
for i in range(1, 5):
    for j in range(i + 1, 5):
        if not any(lin_holds_from(XS[i][k] - XS[j][k] - 1, T0) or
                   lin_holds_from(XS[j][k] - XS[i][k] - 1, T0) for k in range(8)):
            fail(f"X{i}, X{j} not separated for all t >= {T0}")
print("X1..X4 pairwise distinct for all t >=", T0)


# ---------------------------------------------------------------- 4. iteration
def Kstr(s, base):
    """Independent implementation on strings: s is a digit tuple (any order);
    sort it, form the two words as integers, return |difference| as an
    8-digit tuple, most significant first."""
    srt = sorted(s, reverse=True)
    w = [0, 0]
    for n, word in enumerate((W1, W2)):
        for ch in word:
            w[n] = w[n] * base + srt["ABCDEFGH".index(ch)]
    v = abs(w[0] - w[1])
    digs = []
    for _ in range(8):
        digs.append(v % base)
        v //= base
    assert v == 0
    return tuple(reversed(digs))


def K(s, base):
    return tuple(sorted(Kstr(s, base), reverse=True))


bad = []
for tv in range(T0, 2001):
    base = 5 * tv
    x = X(tv)
    for i in range(1, 5):
        if list(x[i]) != sorted(x[i], reverse=True) or min(x[i]) < 0 or max(x[i]) > base - 1:
            bad.append((tv, i, "invalid"))
        if K(x[i], base) != x[NXT[i]]:
            bad.append((tv, i, "step"))
    orbit = [x[1]]
    for _ in range(5):
        orbit.append(Kstr(orbit[-1], base))
    if orbit[5] != orbit[1] or len(set(orbit[1:5])) != 4:
        bad.append((tv, "string cycle"))
if bad:
    fail(f"iteration: {bad[:5]}")
print(f"direct iteration: K(Xi) sorts to X(i+1), K^5(x) = K(x), and K(x)..K^4(x) are"
      f" 4 distinct strings, for every t = {T0}..2000 ({2001 - T0} bases)")
print("  base 50 (t = 10):", X(10))

# ---------------------------------------------------------------- 5. below
for tv in range(1, T0):
    if X(tv)[1][0] >= X(tv)[1][1]:
        fail(f"t = {tv}: X1 unexpectedly has s0 >= s1")
for tv in range(4, T0):
    base, x = 5 * tv, X(tv)
    if not (K(x[2], base) == x[3] and K(x[3], base) == x[4]):
        fail(f"t = {tv}: X2 -> X3 -> X4 fails")
    k4 = K(x[4], base)
    if k4 != tuple(sorted(x[1], reverse=True)) or k4 == x[1]:
        fail(f"t = {tv}: K(X4) not the rearranged X1")
    fix = (base - 1, base - 1, base - 2, 1, 0, 0, 0, 0)
    if K(fix, base) != fix:
        fail(f"t = {tv}: {fix} not fixed")
    s, seen = k4, []
    while s not in seen:
        seen.append(s)
        s = K(s, base)
    if s != fix:
        fail(f"t = {tv}: orbit of K(X4) ends at {s}")
    print(f"  t = {tv} (b = {base}): K(X4) sorts to {k4} != X1 = {x[1]}; orbit ends at the"
          f" fixed point with sorted digits {fix} after {seen.index(s)} more steps")
print("below threshold: X1 not sorted for t <= 9; for 4 <= t <= 9 the orbit leaves the family")

print("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED")
raise SystemExit(0 if ok else 1)
