"""
verify_60714_ladder.py
======================
Constructs the coefficient-preserving lifting family for F = 60714 at every
digit length d >= 5 (both odd and even ladders), and verifies Theorem 5.2
empirically:
    K^(d)(60714_padded) = 60714 at every d >= 5

Outputs:
    - Explicit pi, sigma, and coefficient vector at each d
    - Verification that K(F) = F holds
    - Letter-string representation of pi and sigma (as used in Appendix B)

Usage:
    python3 verify_60714_ladder.py          # shows d=5..20 and d=100
    python3 verify_60714_ladder.py 50       # shows up through d=50

Relevant paper sections: §5.2, Appendix B, Theorem 5.2.
"""

import sys


def build_ladder(max_d):
    """Build 60714's coefficient-preserving lifting at every d from 5 to max_d,
    on both ladders. Returns dict: d -> (pi, sigma, coefs, ladder_type)."""
    rules = {}
    
    # Odd ladder: d=5, 7, 9, ...
    pi_odd = [4, 1, 2, 3, 0]
    sigma_odd = [2, 0, 1, 4, 3]
    rules[5] = (tuple(pi_odd), tuple(sigma_odd), 'odd (native root)')
    d = 5
    while d + 2 <= max_d:
        new_d = d + 2
        # Odd ladder extension: append (d+1, d) to pi, (d, d+1) to sigma
        pi_odd.extend([d + 1, d])
        sigma_odd.extend([d, d + 1])
        rules[new_d] = (tuple(pi_odd), tuple(sigma_odd), 'odd')
        d = new_d
    
    # Even ladder: d=6 (split root), 8, 10, ...
    pi_even = [4, 1, 2, 3, 5, 0]
    sigma_even = [2, 0, 1, 4, 3, 5]
    if 6 <= max_d:
        rules[6] = (tuple(pi_even), tuple(sigma_even), 'even (split root)')
    d = 6
    while d + 2 <= max_d:
        new_d = d + 2
        pi_even.extend([d, d + 1])
        sigma_even.extend([d + 1, d])
        rules[new_d] = (tuple(pi_even), tuple(sigma_even), 'even')
        d = new_d
    
    return rules


def pi_to_letter_string(pi, d):
    """Return the letter string for pi: reading from highest place to lowest."""
    if d <= 52:
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'[:d]
    else:
        letters = [f'x{i}' for i in range(d)]
    result = [None] * d
    for i in range(d):
        place = pi[i]
        result[d - 1 - place] = letters[i]
    if d > 52:
        return ' '.join(result)
    return ''.join(result)


def coefs_from_permutations(pi, sigma):
    return tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(len(pi)))


def verify_fixed_point(coefs, d):
    F_sorted = [7, 6, 4, 1] + [0] * (d - 4)
    return abs(sum(c * x for c, x in zip(coefs, F_sorted)))


def main():
    max_d = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    
    rules = build_ladder(max_d)
    
    print(f"{'d':>3} | {'ladder':<22} | {'pi (letters)':<28} | {'sigma (letters)':<28} | K(F)")
    print("-" * 105)
    all_ok = True
    for d in sorted(rules.keys()):
        pi, sigma, ladder = rules[d]
        coefs = coefs_from_permutations(pi, sigma)
        K_F = verify_fixed_point(coefs, d)
        pi_str = pi_to_letter_string(pi, d)
        sigma_str = pi_to_letter_string(sigma, d)
        ok = K_F == 60714
        marker = '✓' if ok else '✗'
        all_ok = all_ok and ok
        print(f"{d:>3} | {ladder:<22} | {pi_str:<28} | {sigma_str:<28} | {K_F} {marker}")
    
    print("-" * 105)
    
    # Bonus: d=100 on even ladder
    if max_d < 100:
        print("\nBonus: verification at d=100 (even ladder)...")
        rules_100 = build_ladder(100)
        pi, sigma, ladder = rules_100[100]
        coefs = coefs_from_permutations(pi, sigma)
        K_F = verify_fixed_point(coefs, 100)
        print(f"d=100: K(F) = {K_F} {'✓' if K_F == 60714 else '✗'}")
        print(f"  First 4 coefs (locked): {coefs[:4]}")
        print(f"  Coef 4, 5 (even root): ({coefs[4]}, {coefs[5]})")
        print(f"  Sum of appended pairs (positions 6..99): {sum(coefs[6:])}")
    
    print("\nAll rules verified:", "YES" if all_ok else "NO")


if __name__ == '__main__':
    main()
