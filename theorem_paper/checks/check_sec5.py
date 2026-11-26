#!/usr/bin/env python3
"""Checks for Section 5 (finite certificate and lifting theorem).

Works only from the statements written in theorem_paper/sec5_certificate.md:
  * a half-swap rule is a list of pairs (P_q, M_q), q = 0..n-1, of sorted-letter
    indices (letter 0 = largest digit); word 1 has P_q at place q+n, M_q at place q;
  * V(s) = sum_q b^q (s[P_q] - s[M_q]), K(s) = (b^n - 1)|V(s)|;
  * state rho = sorted deficits; string of rho: s_{i-1} = b-1-rho_i, s_{2n-i} = rho_i;
  * Criterion (Theorem 5.9): universal iff gap cover and T has a fixed state reached
    from every state;
  * class C (Definition 5.10), lifts (Definition 5.11), Theorem 5.13, Corollary 5.14.

Part 1 compares the criterion with direct complete enumeration of all digit
multisets for random rules (bases 4, 6, 10; 6 and 8 digits).
Part 2 checks the example DHFBIJGECA - JGECADHFBI and its lifts.
Part 3 (referee round): base 2 census, gap weights, odd-base repdigit images,
6174, and the lifts of the reversed orientation of the example seed.

Run: /usr/bin/python3 theorem_paper/checks/check_sec5.py
"""
import random
import sys
from itertools import combinations_with_replacement

# ---------------------------------------------------------------- basics

def V(rule, s, b):
    return sum(b ** q * (s[P] - s[M]) for q, (P, M) in enumerate(rule))


def K_value(rule, s, b):
    n = len(rule)
    return (b ** n - 1) * abs(V(rule, s, b))


def digits(x, b, L):
    out = []
    for _ in range(L):
        out.append(x % b)
        x //= b
    assert x == 0
    return out  # least significant first


def sorted_desc(x, b, L):
    return tuple(sorted(digits(x, b, L), reverse=True))


def covers_every_gap(rule):
    n = len(rule)
    for j in range(2 * n - 1):
        if not any(min(P, M) <= j < max(P, M) for P, M in rule):
            return False
    return True


def string_of_state(rho, b):
    n = len(rho)
    s = [None] * (2 * n)
    for i in range(1, n + 1):
        s[i - 1] = b - 1 - rho[i - 1]
        s[2 * n - i] = rho[i - 1]
    return tuple(s)


def deficit(x, b):
    return min(x, b - 1 - x)


def state_of_m(m, b, n):
    """state of the image (b^n-1) m, m >= 1, via N = m-1 (Lemma 5.6)."""
    assert 1 <= m <= b ** n - 1
    return tuple(sorted(deficit(x, b) for x in digits(m - 1, b, n)))


def states(b, n):
    H = (b - 1) // 2
    return list(combinations_with_replacement(range(H + 1), n))


def T_map(rule, b, signed=False):
    """T on states; returns dict, and dict of V values. Requires V != 0."""
    n = len(rule)
    T, Vs = {}, {}
    for rho in states(b, n):
        v = V(rule, string_of_state(rho, b), b)
        Vs[rho] = v
        if v == 0:
            return None, Vs
        T[rho] = state_of_m(abs(v), b, n)
    return T, Vs


def attracting_fixed_state(T):
    """the state tau with T(tau)=tau reached from every state, or None; also max steps."""
    fixed = [r for r in T if T[r] == r]
    if len(fixed) != 1:
        return None, None
    tau = fixed[0]
    D = 0
    for r in T:
        x, k = r, 0
        while x != tau and k <= len(T):
            x, k = T[x], k + 1
        if x != tau:
            return None, None
        D = max(D, k)
    return tau, D


def criterion(rule, b):
    """Theorem 5.9 verdict: (universal?, endpoint F or None)."""
    assert b % 2 == 0
    if not covers_every_gap(rule):
        return False, None
    T, Vs = T_map(rule, b)
    assert T is not None  # gap cover => V != 0 on every state (Prop 5.5, Lemma 5.7)
    tau, _ = attracting_fixed_state(T)
    if tau is None:
        return False, None
    n = len(rule)
    return True, (b ** n - 1) * abs(Vs[tau])

# ------------------------------------------------- direct enumeration

def brute_universal(rule, b):
    """Every 2n-digit multiset; universal iff a single F != 0 with K(F)=F is reached
    by every non-repdigit. Uses only K on digit strings."""
    n = len(rule)
    L = 2 * n
    nxt = {}
    vals = {}
    for s in combinations_with_replacement(range(b - 1, -1, -1), L):
        s = tuple(sorted(s, reverse=True))
        k = K_value(rule, s, b)
        vals[s] = k
        nxt[s] = sorted_desc(k, b, L)
    # terminal of every multiset
    term = {}
    for s0 in nxt:
        path, s = [], s0
        seen = {}
        while s not in term and s not in seen:
            seen[s] = len(path)
            path.append(s)
            s = nxt[s]
        if s in term:
            t = term[s]
        else:
            cyc = path[seen[s]:]
            t = ('fix', cyc[0]) if len(cyc) == 1 else ('cyc', min(cyc))
        for p in path:
            term[p] = t
    terms = set()
    for s in nxt:
        if len(set(s)) > 1:
            terms.add(term[s])
    if len(terms) != 1:
        return False, None
    (kind, F), = terms
    if kind != 'fix':
        return False, None
    Fval = vals[F]
    if Fval == 0:
        return False, None
    # the fixed integer: K(F) has sorted digits F; check K(Fval) = Fval as integers
    if K_value(rule, sorted_desc(Fval, b, L), b) != Fval:
        return False, None
    return True, Fval


def random_rule(n, rng):
    letters = list(range(2 * n))
    rng.shuffle(letters)
    return [(letters[2 * q], letters[2 * q + 1]) for q in range(n)]

# ------------------------------------------------- part 1

def part1():
    rng = random.Random(20261125)
    total = agree = 0
    summary = []
    for b in (4, 6, 10):
        for n in (3, 4):
            want_u, want_nu = 30, 30
            got_u, got_nu, nogap = [], [], 0
            tries = 0
            while (len(got_u) < want_u or len(got_nu) < want_nu) and tries < 200000:
                tries += 1
                r = random_rule(n, rng)
                u, _ = criterion(r, b)
                if u and len(got_u) < want_u:
                    got_u.append(r)
                elif not u and len(got_nu) < want_nu:
                    if not covers_every_gap(r):
                        nogap += 1
                    got_nu.append(r)
            nu_n = nnu_n = 0
            for r in got_u + got_nu:
                cu, cF = criterion(r, b)
                bu, bF = brute_universal(r, b)
                total += 1
                ok = (cu == bu) and (cF == bF)
                agree += ok
                if not ok:
                    print('MISMATCH', b, n, r, cu, cF, bu, bF)
                nu_n += cu
                nnu_n += (not cu)
            summary.append((b, 2 * n, nu_n, nnu_n, nogap))
    for b, L, u, nu, ng in summary:
        print(f'  base {b:2d}, {L} digits: {u} universal + {nu} non-universal '
              f'({ng} of them fail gap cover); criterion = enumeration on all')
    print(f'PART 1: {agree}/{total} rules agree (verdict and endpoint)')
    return agree == total

# ------------------------------------------------- part 2

def parse_rule(w1, w2):
    """letters A.. = s_0..; word 1 written most significant first (place 2n-1 .. 0)."""
    L = len(w1)
    n = L // 2
    idx = {c: i for i, c in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:L])}
    place1 = {L - 1 - k: idx[c] for k, c in enumerate(w1)}
    place2 = {L - 1 - k: idx[c] for k, c in enumerate(w2)}
    rule = [(place1[q + n], place1[q]) for q in range(n)]
    # word 2 must be the reverse assignment
    for q, (P, M) in enumerate(rule):
        assert place2[q + n] == M and place2[q] == P, 'not a half-swap rule'
    return rule


def rule_words(rule):
    n = len(rule)
    al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    w1 = ''.join(al[rule[q][0]] for q in range(n - 1, -1, -1)) + \
         ''.join(al[rule[q][1]] for q in range(n - 1, -1, -1))
    w2 = ''.join(al[rule[q][1]] for q in range(n - 1, -1, -1)) + \
         ''.join(al[rule[q][0]] for q in range(n - 1, -1, -1))
    return w1, w2


def class_C(rule, b):
    """Definition 5.10 with the given orientation. Returns (ok, tau, m*, D)."""
    n = len(rule)
    T, Vs = T_map(rule, b)
    if T is None or any(v <= 0 for v in Vs.values()):
        return False, None, None, None          # (S)
    tau, D = attracting_fixed_state(T)
    if tau is None:
        return False, None, None, None          # (U)
    for rho in T:
        if rho[0] >= 1 and 0 not in T[rho]:
            return False, None, None, None      # (C1)
    return True, tau, Vs[tau], D


def top_lift(rule):
    n = len(rule)
    return [(P + 1, M + 1) for P, M in rule] + [(0, 2 * n + 1)]


def bottom_lift(rule):
    n = len(rule)
    return [(2 * n + 1, 0)] + [(P + 1, M + 1) for P, M in rule]


def endpoint_from_N(N, b):
    """F = N followed by its digit complement (n digits each)."""
    n = len(N)
    s = N + [b - 1 - x for x in N]
    v = 0
    for x in s:
        v = v * b + x
    return v


def part2(max_brute_len):
    b = 10
    ok_all = True
    seed = parse_rule('DHFBIJGECA', 'JGECADHFBI')
    print('  seed pairs (P_q, M_q), q=0..4:', seed)
    c, tau, mstar, D = class_C(seed, b)
    print(f'  seed class C: {c}, tau = {tau}, m* = {mstar}, max steps to tau D = {D}, '
          f'gap cover: {covers_every_gap(seed)}, states: {len(states(b, 5))}')
    ok_all &= c and mstar == 68701 and covers_every_gap(seed)
    cu, cF = criterion(seed, b)
    print(f'  criterion: universal {cu}, F = {cF}')
    ok_all &= cu and cF == 6870031299
    if max_brute_len >= 10:
        bu, bF = brute_universal(seed, b)
        print(f'  enumeration (92,378 multisets): universal {bu}, F = {bF}')
        ok_all &= bu and bF == 6870031299
    Nstar = [int(ch) for ch in '68700']
    jobs = [('T', top_lift), ('B', bottom_lift)]
    level = [('', seed, Nstar)]
    for depth in (1, 2):
        new_level = []
        for name, r, N in level:
            for tag, f in jobs:
                lr = f(r)
                LN = ([b - 1] + N) if tag == 'T' else (N + [0])
                pred = endpoint_from_N(LN, b)
                c2, tau2, m2, D2 = class_C(lr, b)
                cu2, cF2 = criterion(lr, b)
                w1, w2 = rule_words(lr)
                line = (f'  {name + tag:3s} {2 * len(lr)} digits {w1} - {w2}: class C {c2}, '
                        f'criterion F = {cF2}, predicted {pred}, D = {D2}')
                good = c2 and cu2 and cF2 == pred
                if 2 * len(lr) <= max_brute_len:
                    bu2, bF2 = brute_universal(lr, b)
                    line += f'; enumeration: universal {bu2}, F = {bF2}'
                    good &= bu2 and bF2 == pred
                print(line, 'OK' if good else 'FAIL')
                ok_all &= good
                new_level.append((name + tag, lr, LN))
        level = new_level
    print('PART 2:', 'all OK' if ok_all else 'FAILURE')
    return ok_all


# ------------------------------------------------- part 3 (referee round)

def part3():
    """(a) base 2: every gap-covering half-swap rule is universal, n = 2..5, by
    complete enumeration (rules up to the global sign: letter 0 is a P);
    (b) the gap weight C_j of Section 2 is 0 exactly when gap j is uncovered;
    (c) odd bases: some rule has a first image equal to the repdigit of (b-1)/2;
    (d) 6174 is not a 2-digit block followed by its complement."""
    from itertools import permutations
    ok = True
    for n in (2, 3, 4, 5):
        tot = cov = uni = 0
        for perm in permutations(range(2 * n)):
            rule = [(perm[2 * q], perm[2 * q + 1]) for q in range(n)]
            if not any(P == 0 for P, M in rule):
                continue           # one representative of each sign pair
            tot += 1
            g = covers_every_gap(rule)
            u, F = brute_universal(rule, 2)
            cov += g
            uni += u
            if g != u:
                ok = False
                print('  base 2 MISMATCH', rule, g, u)
        print(f'  base 2, {2 * n} digits: {tot} rules up to sign, {cov} cover every gap, '
              f'{uni} universal')
    rng = random.Random(7)
    for _ in range(2000):
        b = rng.randrange(2, 17)
        n = rng.randrange(1, 7)
        rule = random_rule(n, rng)
        c = [0] * (2 * n)
        for q, (P, M) in enumerate(rule):
            c[P] += b ** (q + n) - b ** q
            c[M] += b ** q - b ** (q + n)
        for j in range(2 * n - 1):
            Cj = sum(c[:j + 1])
            covered = any(min(P, M) <= j < max(P, M) for P, M in rule)
            if (Cj == 0) == covered:
                ok = False
                print('  gap weight MISMATCH', b, rule, j)
    print('  gap weight C_j = 0 iff gap j uncovered: checked on 2000 random rules')
    for b, n in ((3, 2), (3, 3), (5, 2), (5, 3), (7, 3)):
        c0 = (b - 1) // 2
        rep = c0 * (b ** (2 * n) - 1) // (b - 1)
        hit = None
        for _ in range(20000):
            rule = random_rule(n, rng)
            for s in combinations_with_replacement(range(b - 1, -1, -1), 2 * n):
                if len(set(s)) > 1 and K_value(rule, s, b) == rep:
                    hit = (rule, s)
                    break
            if hit:
                break
        print(f'  base {b}, {2 * n} digits: non-repdigit with first image the repdigit of '
              f'{c0}: {hit}')
        ok &= hit is not None
    ok &= (61 * 100 + 38 != 6174) and (6174 % 99 != 0)
    seed = parse_rule('DHFBIJGECA', 'JGECADHFBI')
    rev = [(M, P) for P, M in seed]
    for nm, f in (('top', top_lift), ('bottom', bottom_lift)):
        u, F = brute_universal(f(rev), 10)
        print(f'  {nm} lift of the reversed seed {rule_words(f(rev))}: universal {u}')
        ok &= not u
    print('  6174 = 61|74, complement of 61 is 38; 6174 mod 99 =', 6174 % 99)
    print('PART 3:', 'all OK' if ok else 'FAILURE')
    return ok


if __name__ == '__main__':
    max_brute = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    a = part1()
    c = part2(max_brute)
    d = part3()
    print('ALL CHECKS PASS' if (a and c and d) else 'SOME CHECK FAILED')
