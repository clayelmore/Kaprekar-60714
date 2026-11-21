"""Referee's independent implementation of M_n from the explicit letter lists."""
from itertools import combinations_with_replacement

def pairs(n):
    """place -> (P, M) letters, transcribed from the explicit lists in PROOF_FIXEDMIDDLE.md."""
    p = {}
    if n % 2 == 1:
        k = (n - 1) // 2
        p[0] = (n + 1, n + 2); p[1] = (0, 2 * n); p[2] = (n, n - 1)
        for j in range(1, k):
            p[n + 1 - 2 * j] = (2 * j + 1, 2 * j)
            p[n - 2 * j] = (2 * n - 2 * j, 2 * n + 1 - 2 * j)
    else:
        k = (n - 2) // 2
        p[0] = (n - 1, n); p[1] = (2, 2 * n); p[2] = (0, 2 * n - 1); p[3] = (n + 2, n + 1)
        for j in range(1, k):
            p[n + 1 - 2 * j] = (2 * j + 2, 2 * j + 1)
            p[n - 2 * j] = (2 * n - 1 - 2 * j, 2 * n - 2 * j)
    assert sorted(p) == list(range(n)), (n, sorted(p))
    used = sorted(x for pq in p.values() for x in pq)
    assert used == [0] + list(range(2, 2 * n + 1)), (n, used)
    return p

def words(n):
    """word1, word2 as lists of letters indexed by place (place 0 = units)."""
    p = pairs(n)
    L = 2 * n + 1
    w1 = [None] * L; w2 = [None] * L
    for q, (P, M) in p.items():
        w1[q + n + 1] = P; w1[q] = M
        w2[q + n + 1] = M; w2[q] = P
    w1[n] = 1; w2[n] = 1
    return w1, w2

def letters_str(n):
    w1, w2 = words(n)
    A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(A[w1[i]] for i in reversed(range(2 * n + 1))), "".join(A[w2[i]] for i in reversed(range(2 * n + 1)))

def make_step(n, b):
    w1, w2 = words(n)
    L = 2 * n + 1
    pw = [b ** i for i in range(L)]
    def step(sorted_desc):
        a = sum(sorted_desc[w1[i]] * pw[i] for i in range(L))
        c = sum(sorted_desc[w2[i]] * pw[i] for i in range(L))
        v = abs(a - c)
        d = []
        for _ in range(L):
            d.append(v % b); v //= b
        assert v == 0
        return tuple(sorted(d, reverse=True)), abs(a - c)
    return step

def value_of(sorted_desc, b):
    return None
