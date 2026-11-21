"""Reference implementation (pure Python, exact integers) of K_d and Phi.

Written from the task description only.
"""
from itertools import combinations_with_replacement


def place_maps(a, b, d):
    """A = (a0..a4, 6..d-1, a5), B = (b0..b5, 6..d-1)."""
    assert d >= 6
    A = list(a[:5]) + list(range(6, d)) + [a[5]]
    B = list(b[:6]) + list(range(6, d))
    assert len(A) == d and len(B) == d
    return A, B


def make_K(a, b, d):
    A, B = place_maps(a, b, d)
    coef = [10 ** A[i] - 10 ** B[i] for i in range(d)]

    def K(digits):
        """digits: any iterable of d digits; returns sorted-desc tuple of result digits."""
        s = sorted(digits, reverse=True)
        assert len(s) == d
        v = abs(sum(c * x for c, x in zip(coef, s)))
        assert v < 10 ** d, (digits, v)
        t = str(v).zfill(d)
        return tuple(sorted((int(ch) for ch in t), reverse=True))

    def K_value(digits):
        s = sorted(digits, reverse=True)
        return abs(sum(c * x for c, x in zip(coef, s)))

    return K, K_value


def phi_value(a, b, n):
    """n: nonzero digits sorted descending. Returns V (signed)."""
    k = len(n)
    nn = list(n) + [0] * 7
    V = 0
    for i in range(5):
        V += (10 ** a[i] - 10 ** b[i]) * nn[i]
    V -= 10 ** b[5] * nn[5]
    for j in range(6, k + 1):
        V += 10 ** j * (nn[j - 1] - nn[j])
    return V


def phi(a, b, n):
    """n: tuple of nonzero digits sorted descending -> same representation."""
    V = abs(phi_value(a, b, n))
    return tuple(sorted((int(ch) for ch in str(V) if ch != '0'), reverse=True))


def all_multisets(d):
    """All multisets of d digits, as descending tuples."""
    for c in combinations_with_replacement(range(9, -1, -1), d):
        yield c  # combinations of a descending sequence are descending


def parse_core(line):
    a = b = None
    target = maxsize = None
    for tok in line.split():
        if tok.startswith('a='):
            a = tuple(int(x) for x in tok[2:].split(','))
        elif tok.startswith('b='):
            b = tuple(int(x) for x in tok[2:].split(','))
        elif tok.startswith('target='):
            target = tok[7:]
        elif tok.startswith('maxsize='):
            maxsize = int(tok[8:])
    return a, b, target, maxsize


def check_core(a, b):
    assert sorted(a) == list(range(6)) and sorted(b) == list(range(6))
    assert all(x != y for x, y in zip(a, b))
