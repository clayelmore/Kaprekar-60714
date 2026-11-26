#!/usr/bin/python3
"""Computed claims in the remarks of theorem_paper/sec3_even.md.

1. Young's block exchange ABCD - CDAB at length 4: in base 3 the string 2210
   maps to 1111 and then to 0, while 32 is the only nonzero fixed value; in
   bases 6, 12, 24 every non-repdigit reaches the unique nonzero fixed value.
2. Step counts of R_3 by complete enumeration of digit multisets, and of the
   reduced map from every state, for the sharpness remark after Theorem 3.3.
Run with /usr/bin/python3.
"""
import itertools
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from check_sec3_even import rule_pairs, K_sorted, sorted_digits, reduced  # noqa: E402


def young_K(s, b):
    A, B, C, D = s
    return abs((A * b**3 + B * b**2 + C * b + D) - (C * b**3 + D * b**2 + A * b + B))


def srt4(x, b):
    d = []
    for _ in range(4):
        d.append(x % b)
        x //= b
    assert x == 0
    return tuple(sorted(d, reverse=True))


def young(b):
    fixed = [x for x in range(1, b**4) if young_K(srt4(x, b), b) == x]
    terminals = set()
    for s in itertools.combinations_with_replacement(range(b - 1, -1, -1), 4):
        if s[0] == s[-1]:
            continue
        seen = []
        cur = s
        while cur not in seen:
            seen.append(cur)
            cur = srt4(young_K(cur, b), b)
        cyc = seen[seen.index(cur):]
        if len(cyc) == 1:
            terminals.add(young_K(cur, b))
        else:
            terminals.add(("cycle", len(cyc)))
    return fixed, terminals


def main():
    ok = True
    x = young_K((2, 2, 1, 0), 3)
    print("base 3: 2210 ->", x, "digits", srt4(x, 3), "->", young_K(srt4(x, 3), 3))
    ok &= srt4(x, 3) == (1, 1, 1, 1) and young_K((1, 1, 1, 1), 3) == 0
    for b in (3, 6, 12, 24):
        fixed, terms = young(b)
        print(f"base {b}: nonzero fixed values {fixed}; terminal values of non-repdigits {sorted(terms, key=str)}")
        if b == 3:
            ok &= fixed == [32] and 0 in terms
        else:
            ok &= len(fixed) == 1 and terms == set(fixed)

    # step counts of R_3
    pr = rule_pairs(3)
    worst = {}
    for b in range(3, 21):
        F = (b - 1) * (b**3 - 1)
        ms = 0
        for s in itertools.combinations_with_replacement(range(b - 1, -1, -1), 6):
            if s[0] == s[-1]:
                continue
            cur, steps = s, 0
            while True:
                v = K_sorted(cur, b, pr)
                steps += 1
                if v == F:
                    break
                cur = sorted_digits(v, b, 3)
                assert steps < 200
            ms = max(ms, steps)
        worst[b] = ms
        ok &= ms <= (b + 17) / 2
    print("R_3 direct, max steps to F by base 3..20:", worst)
    print("  overall max", max(worst.values()))
    # reduced map from every state, n = 3: steps to tau, plus one step to F
    tau = (0, 0, 1)
    top = 0
    topb = None
    for b in range(3, 202):
        H = (b - 1) // 2
        for rho in itertools.combinations_with_replacement(range(H + 1), 3):
            if b % 2 == 1 and rho == (H, H, H):
                continue
            cur, steps = rho, 0
            while cur != tau:
                cur = reduced(cur, b)[1]
                steps += 1
            if steps > top:
                top, topb = steps, b
    print(f"R_3 reduced map from every state, b = 3..201: max steps to tau {top} (first at b={topb})")
    print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
