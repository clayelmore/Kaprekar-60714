"""
verifier_strict_d.py — independent verifier for strict-d anchors at d=5,6,7.

Companion script to Appendix F of the paper. This is a from-scratch
implementation distinct from `universality_scan_v3.py`: where v3 iterates
rules first and tests fps, this script iterates fps first and enumerates
fixing rules via direct (A, B) image-pair lookup using a hash set. Both
implementations independently produce the same strict-d anchor lists at
d = 5, 6, 7.

Usage:
    python3 verifier_strict_d.py 5    # scan d=5 in {7,6,4,1,0}
    python3 verifier_strict_d.py 6    # scan d=6 in {7,6,4,1,0,0}
    python3 verifier_strict_d.py 7    # scan d=7 in {7,6,4,1,0,0,0}

Runtimes (commodity hardware):
    d = 5: ~1 s
    d = 6: ~6 s
    d = 7: ~70 s

Outputs JSON files: d{D}_strict_anchors.json with per-fp counts and rules.

This script implements:
    - F-or-0 universality (paper convention from §2 / Appendix F.1)
    - Strict-d criterion (Appendix F, Definitions F.1, F.2, F.3)
"""

import sys
import json
import time
from itertools import permutations
from collections import Counter, defaultdict


# ---------- primitives ----------

def digits_padded(n, d):
    """Return tuple of d digits of n, padded with leading zeros."""
    s = str(n).zfill(d)
    if len(s) > d:
        raise ValueError(f"{n} has more than {d} digits")
    return tuple(int(c) for c in s)


def sort_desc(n, d):
    """Sorted-descending digit tuple of n at length d."""
    return tuple(sorted(digits_padded(n, d), reverse=True))


def apply_rule(pi, sigma, n, d):
    """K(n) = |pi.x - sigma.x| where x = sort_desc(n, d)."""
    x = sort_desc(n, d)
    a = sum(x[i] * (10 ** pi[i]) for i in range(d))
    b = sum(x[i] * (10 ** sigma[i]) for i in range(d))
    return abs(a - b)


def is_admissible(n, d):
    """Non-repdigit AND non-near-repdigit at length d (paper §2.1)."""
    counts = Counter(digits_padded(n, d))
    return max(counts.values()) < d - 1


def iterate(pi, sigma, n, d, F, max_steps=400):
    """Returns ('F', steps), ('0', steps), ('cycle', None), or ('budget', None)."""
    seen = {n: 0}
    cur = n
    for step in range(1, max_steps + 1):
        cur = apply_rule(pi, sigma, cur, d)
        if cur == F:
            return ('F', step)
        if cur == 0:
            return ('0', step)
        if cur in seen:
            return ('cycle', None)
        seen[cur] = step
    return ('budget', None)


def is_full_variable(pi, sigma, d):
    """sv = d iff pi[i] != sigma[i] for all i."""
    return all(pi[i] != sigma[i] for i in range(d))


def coefficient_vector(pi, sigma, d):
    """c_i = 10^pi[i] - 10^sigma[i]."""
    return tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(d))


# ---------- admissible multiset enumeration ----------

def enumerate_admissible_multisets(d):
    """One integer rep per admissible digit multiset at d."""
    reps = []
    def gen(prefix, max_d, remaining):
        if remaining == 0:
            n = int(''.join(str(c) for c in prefix))
            counts = Counter(prefix)
            if max(counts.values()) < d - 1:
                reps.append(n)
            return
        for digit in range(max_d + 1):
            gen(prefix + (digit,), digit, remaining - 1)
    gen((), 9, d)
    return reps


# ---------- strict-d criterion (Appendix F, Def F.1, F.2) ----------

def has_trivial_zero_sum_pair_on_F(pi, sigma, F, d):
    """
    True iff there exist indices i < j with c_i + c_j = 0 AND
    sort_desc(F)_i = sort_desc(F)_j (i.e., a "trivial zero-sum pair on F").
    """
    c = coefficient_vector(pi, sigma, d)
    x = sort_desc(F, d)
    for i in range(d):
        for j in range(i + 1, d):
            if c[i] + c[j] == 0 and x[i] == x[j]:
                return True
    return False


def is_strict_d(pi, sigma, F, d):
    """Strictness (Definition F.2): no trivial zero-sum pair on F."""
    return not has_trivial_zero_sum_pair_on_F(pi, sigma, F, d)


# ---------- fp-first enumeration via (A, B) pair lookup ----------

def integer_perms_of_multiset(multiset_sorted_desc, d):
    """
    Set of distinct integers formable by permuting the multiset into d positions
    (leading zeros allowed; e.g., (0,0,0,1,4,6,7) at d=7 includes 0001467 = 1467).
    """
    seen = set()
    for perm in permutations(multiset_sorted_desc):
        n = sum(dig * (10 ** (d - 1 - k)) for k, dig in enumerate(perm))
        seen.add(n)
    return seen


def realizations_of_pair(pi_image, sigma_image, F_sort_desc, d):
    """
    Given integer images A = pi.x and B = sigma.x with x = F_sort_desc, find
    all (pi, sigma) pairs that realize (A, B). When x has repeated digits,
    multiple (pi, sigma) realize the same (A, B).
    """
    A_decimal = [(pi_image // (10 ** k)) % 10 for k in range(d)]
    B_decimal = [(sigma_image // (10 ** k)) % 10 for k in range(d)]
    x = F_sort_desc

    sd_positions_by_digit = defaultdict(list)
    A_positions_by_digit = defaultdict(list)
    B_positions_by_digit = defaultdict(list)
    for i, v in enumerate(x):
        sd_positions_by_digit[v].append(i)
    for k, v in enumerate(A_decimal):
        A_positions_by_digit[v].append(k)
    for k, v in enumerate(B_decimal):
        B_positions_by_digit[v].append(k)

    for v in sd_positions_by_digit:
        if len(sd_positions_by_digit[v]) != len(A_positions_by_digit.get(v, [])):
            return []
        if len(sd_positions_by_digit[v]) != len(B_positions_by_digit.get(v, [])):
            return []

    digits_present = sorted(sd_positions_by_digit.keys())

    def gen_bijections(sd_pos, target_pos):
        for perm in permutations(target_pos):
            yield dict(zip(sd_pos, perm))

    sigma_realizations = []
    def combine_sigma(digit_idx, sigma_partial):
        if digit_idx == len(digits_present):
            sigma_realizations.append(dict(sigma_partial))
            return
        v = digits_present[digit_idx]
        for bij in gen_bijections(sd_positions_by_digit[v], B_positions_by_digit[v]):
            new_partial = {**sigma_partial, **bij}
            combine_sigma(digit_idx + 1, new_partial)
    combine_sigma(0, {})

    realizations = []
    def combine_pi(digit_idx, pi_partial):
        if digit_idx == len(digits_present):
            pi = tuple(pi_partial[i] for i in range(d))
            for sigma_partial in sigma_realizations:
                sigma = tuple(sigma_partial[i] for i in range(d))
                realizations.append((pi, sigma))
            return
        v = digits_present[digit_idx]
        for bij in gen_bijections(sd_positions_by_digit[v], A_positions_by_digit[v]):
            new_partial = {**pi_partial, **bij}
            combine_pi(digit_idx + 1, new_partial)
    combine_pi(0, {})
    return realizations


def find_strict_anchors(F, d, multisets):
    """For a single fp F, returns dict with fixing/universal/strict rule lists."""
    F_sd = sort_desc(F, d)

    # Enumerate distinct integer images of F's multiset
    S = integer_perms_of_multiset(F_sd, d)

    # Find fixing pairs: (A, B) with |A - B| = F, A != B, both in S
    fixing_pairs = []
    for A in S:
        if (A - F) in S and (A - F) != A:
            fixing_pairs.append((A, A - F))
        if (A + F) in S and (A + F) != A:
            fixing_pairs.append((A, A + F))

    # Expand each pair to (pi, sigma) realizations, filter full-variable
    fixing_rules = []
    seen = set()
    for A, B in fixing_pairs:
        for pi, sigma in realizations_of_pair(A, B, F_sd, d):
            if (pi, sigma) in seen:
                continue
            if is_full_variable(pi, sigma, d):
                seen.add((pi, sigma))
                fixing_rules.append((pi, sigma))

    # Universality test
    universal_rules = []
    for pi, sigma in fixing_rules:
        if apply_rule(pi, sigma, F, d) != F:
            continue
        ok = True
        for n in multisets:
            outcome, _ = iterate(pi, sigma, n, d, F)
            if outcome not in ('F', '0'):
                ok = False
                break
        if ok:
            universal_rules.append((pi, sigma))

    # Strict test
    strict_rules = [(pi, sigma) for pi, sigma in universal_rules
                    if is_strict_d(pi, sigma, F, d)]

    return {
        'fixing_rules': fixing_rules,
        'universal_rules': universal_rules,
        'strict_rules': strict_rules,
    }


# ---------- main scan ----------

MULTISETS_BY_D = {
    5: (7, 6, 4, 1, 0),
    6: (7, 6, 4, 1, 0, 0),
    7: (7, 6, 4, 1, 0, 0, 0),
}


def scan_at_d(d):
    if d not in MULTISETS_BY_D:
        raise ValueError(f"d={d} not supported. Choose 5, 6, or 7.")

    multiset = MULTISETS_BY_D[d]
    print(f"Scanning d={d} multiset {multiset}...")
    multisets = enumerate_admissible_multisets(d)
    print(f"  {len(multisets)} admissible multisets at d={d}")

    candidates = sorted(set(
        sum(dig * (10 ** (d - 1 - k)) for k, dig in enumerate(p))
        for p in permutations(multiset)
    ))
    candidates = [c for c in candidates if c != 0]
    print(f"  {len(candidates)} candidate fps")

    print(f"\n  Scanning each fp...")
    results = {}
    t0 = time.time()
    for i, F in enumerate(candidates):
        r = find_strict_anchors(F, d, multisets)
        if r['fixing_rules']:
            results[F] = r
        if (i + 1) % 100 == 0:
            elapsed = time.time() - t0
            print(f"    [{i+1}/{len(candidates)}] {elapsed:.0f}s")
    print(f"  Total time: {time.time()-t0:.1f}s")

    universal_fps = sorted([F for F, r in results.items() if r['universal_rules']])
    strict_anchors = sorted([F for F, r in results.items() if r['strict_rules']])

    print(f"\n=== d={d} results ===")
    print(f"  Universal fps ({len(universal_fps)}): {universal_fps}")
    print(f"  Strict-d anchors ({len(strict_anchors)}): {strict_anchors}")
    print(f"\n  Per-fp counts (universal fps):")
    print(f"    {'F':>9} {'fixing':>8} {'universal':>10} {'strict':>8}")
    for F in universal_fps:
        r = results[F]
        print(f"    {F:>9} {len(r['fixing_rules']):>8} "
              f"{len(r['universal_rules']):>10} {len(r['strict_rules']):>8}")

    # Save JSON
    serializable = {}
    for F, r in results.items():
        serializable[str(F)] = {
            'fixing_count': len(r['fixing_rules']),
            'universal_count': len(r['universal_rules']),
            'strict_count': len(r['strict_rules']),
            'strict_rules': [{'pi': list(p), 'sigma': list(s)}
                             for p, s in r['strict_rules']],
        }
    out_path = f'd{d}_strict_anchors.json'
    with open(out_path, 'w') as f:
        json.dump(serializable, f, indent=2)
    print(f"\n  Saved: {out_path}")

    return results


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('5', '6', '7'):
        print(f"Usage: python3 {sys.argv[0]} {{5|6|7}}")
        sys.exit(1)
    scan_at_d(int(sys.argv[1]))
