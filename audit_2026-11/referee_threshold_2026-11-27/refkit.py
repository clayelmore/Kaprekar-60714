"""Independent referee toolkit for PROOF_THRESHOLD.md (written from the Setting section only).

The rule: sorted digits s_0 >= ... >= s_(d-1); sorted digit i goes to place A(i) in the first
number and B(i) in the second, with
    A = (a_0, ..., a_(N-2), N, N+1, ..., d-1, a_(N-1))
    B = (b_0, ..., b_(N-1), N, ..., d-1)
K_d(s) = |first - second|, computed by direct subtraction.
"""
import itertools
import numpy as np


def place_maps(a, b, d):
    N = len(a)
    assert d >= N
    A = list(a[:N - 1]) + list(range(N, d)) + [a[N - 1]]
    B = list(b) + list(range(N, d))
    assert sorted(A) == list(range(d)) and sorted(B) == list(range(d))
    return A, B


# ---------------------------------------------------------------- python big-int, direct
def K_int(s, a, b):
    """s: list of digits sorted descending (length d). Returns integer |P - Q|."""
    d = len(s)
    A, B = place_maps(a, b, d)
    P = sum(s[i] * 10 ** A[i] for i in range(d))
    Q = sum(s[i] * 10 ** B[i] for i in range(d))
    v = abs(P - Q)
    assert v < 10 ** d
    return v


def digits_of(v, d):
    st = str(v).zfill(d)
    assert len(st) == d
    return [int(c) for c in st]


def K_sorted(s, a, b):
    """image as sorted-descending digit list of length len(s)."""
    return sorted(digits_of(K_int(s, a, b), len(s)), reverse=True)


def K_gap(s, a, b):
    """The gap form of the Setting section."""
    d = len(s)
    N = len(a)
    x, y = a[N - 1], b[N - 1]
    c = [10 ** a[i] - 10 ** b[i] for i in range(N - 1)]
    H = sum(10 ** k * (s[k - 1] - s[k]) for k in range(N, d))
    L = sum(c[i] * s[i] for i in range(N - 1)) - 10 ** y * s[N - 1] + 10 ** x * s[d - 1]
    return abs(H + L)


def phi_py(S, a, b):
    """S: tuple of nonzero digits sorted descending. Phi via K_d at d = max(|S|+1, N)."""
    N = len(a)
    d = max(len(S) + 1, N)
    s = list(S) + [0] * (d - len(S))
    v = K_int(s, a, b)
    return tuple(sorted((int(ch) for ch in str(v) if ch != '0'), reverse=True))


def lemma0_ok(a, b):
    """core value is 0 only for constant sorted N-tuples."""
    N = len(a)
    for t in itertools.combinations_with_replacement(range(9, -1, -1), N):
        s = list(t)  # descending
        if s[0] == s[-1]:
            continue
        if K_int(s, a, b) == 0:
            return False, s
    return True, None


def all_cores(N, distinct_only=False):
    perms = list(itertools.permutations(range(N)))
    for a in perms:
        for b in perms:
            if distinct_only and any(a[i] == b[i] for i in range(N)):
                continue
            yield a, b


# ---------------------------------------------------------------- numpy, direct column subtraction
def K_batch(S, a, b):
    """S: (M, d) int array of sorted-desc digits. Returns (M, d) int8 array R with R[:, p] = digit at
    place p of |P - Q| (direct column subtraction with borrow)."""
    M, d = S.shape
    A, B = place_maps(a, b, d)
    P = np.zeros((M, d), np.int16)
    Q = np.zeros((M, d), np.int16)
    P[:, A] = S
    Q[:, B] = S
    R = np.empty((M, d), np.int16)
    borrow = np.zeros(M, np.int16)
    for p in range(d):
        r = P[:, p] - Q[:, p] - borrow
        borrow = (r < 0).astype(np.int16)
        R[:, p] = r + 10 * borrow
    neg = borrow.astype(bool)
    if neg.any():
        Rn = R[neg]
        C = np.empty_like(Rn)
        bo = np.zeros(Rn.shape[0], np.int16)
        for p in range(d):
            r = -Rn[:, p] - bo
            bo = (r < 0).astype(np.int16)
            C[:, p] = r + 10 * bo
        R[neg] = C
    return R.astype(np.int8)


def counts_to_sorted(C, d):
    """C: (M, k) counts for digits (10-k .. 9)?  We use: C has 10 columns for digits 0..9, or 9 columns
    for digits 1..9 (zeros padded to length d). Returns (M, d) sorted-desc digit array."""
    M, k = C.shape
    if k == 9:
        C9 = C.astype(np.int32)
    else:
        C9 = C[:, 1:].astype(np.int32)
    # cum_ge[v] for v = 1..9 : number of digits >= v
    cum = np.cumsum(C9[:, ::-1], axis=1)[:, ::-1]  # cum[:, v-1] = #digits >= v
    idx = np.arange(d)
    S = np.zeros((M, d), np.int8)
    for v in range(9):
        S += (cum[:, v][:, None] > idx[None, :]).astype(np.int8)
    return S


def digit_counts(R, lo=0):
    return np.stack([(R == v).sum(axis=1) for v in range(lo, 10)], axis=1).astype(np.int16)


def all_count_vectors(total, k):
    """All nonnegative int vectors of length k summing to total, shape (M, k)."""
    cur = np.zeros((1, 0), np.int16)
    sums = np.zeros(1, np.int32)
    for j in range(k - 1):
        rem = total - sums
        reps = rem + 1
        newcur = np.repeat(cur, reps, axis=0)
        # values 0..rem for each row
        off = np.concatenate([np.arange(r) for r in reps]) if len(reps) < 2000 else _aranges(reps)
        newcur = np.concatenate([newcur, off[:, None].astype(np.int16)], axis=1)
        sums = np.repeat(sums, reps) + off
        cur = newcur
    last = (total - sums).astype(np.int16)
    return np.concatenate([cur, last[:, None]], axis=1)


def _aranges(reps):
    n = reps.sum()
    starts = np.repeat(np.cumsum(reps) - reps, reps)
    return np.arange(n) - starts


def keys_of(C):
    """Encode count vectors (values < 64) into int64."""
    C = C.astype(np.int64)
    k = np.zeros(C.shape[0], np.int64)
    for j in range(C.shape[1]):
        k = k * 64 + C[:, j]
    return k


def pointer_double(f, vals=None, rounds=40):
    """Return g = f^(2^rounds) and, if vals given, max of vals over the forward orbit (incl. start)."""
    g = f.copy()
    mx = vals.copy() if vals is not None else None
    for _ in range(rounds):
        if mx is not None:
            mx = np.maximum(mx, mx[g])
        g = g[g]
    return g, mx
