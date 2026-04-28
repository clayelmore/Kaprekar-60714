"""
kaprekar_core.py
================
Shared infrastructure for the d=7 audit package.

Provides Numba-accelerated primitives for:
  - Sorted-descending multiset enumeration
  - K-rule iteration on sorted-desc tuples
  - Coefficient vector computation from (pi, sigma)
  - Full-variable / derangement check
  - Admissibility check (non-repdigit, non-near-repdigit)
  - Basin verification via multiset memoization

Pure-Python fallbacks are provided for use when Numba is not available
(audit_60714_d7.py runs in seconds without Numba; only the full-enumeration
scripts NEED Numba).

Conventions match the paper's existing scripts (verify_60714_basin.py,
classify_at_d.py): inputs are tuples of digits sorted in non-increasing
order (largest first), and K outputs the sorted-descending form of the
absolute value of the linear combination, padded with leading zeros to
length d.
"""

import sys
from itertools import permutations, combinations_with_replacement
from collections import Counter

import numpy as np

try:
    from numba import njit, prange
    HAS_NUMBA = True
except ImportError:
    HAS_NUMBA = False
    # Provide no-op stand-ins so the module still imports
    def njit(*args, **kwargs):
        if len(args) == 1 and callable(args[0]):
            return args[0]
        def deco(fn): return fn
        return deco
    def prange(*args, **kwargs):
        return range(*args, **kwargs)


# ---------------------------------------------------------------------------
# Pure-Python utilities (used by audit_60714_d7.py and verifier setup paths)
# ---------------------------------------------------------------------------

def is_admissible_tuple(ms_desc):
    """True iff ms_desc (sorted-desc digit tuple) is non-repdigit AND non-near-repdigit."""
    cnt = Counter(ms_desc)
    if len(cnt) == 1:
        return False
    if max(cnt.values()) >= len(ms_desc) - 1:
        return False
    return True


def build_admissible_multisets(d):
    """All sorted-desc admissible digit-multisets at length d. Pure Python."""
    out = []
    for ms in combinations_with_replacement(range(10), d):
        ms_desc = tuple(sorted(ms, reverse=True))
        if is_admissible_tuple(ms_desc):
            out.append(ms_desc)
    return out


def coefs_from_perms(pi, sigma):
    """Coefficient vector c_i = 10^pi[i] - 10^sigma[i]."""
    return tuple(10 ** pi[i] - 10 ** sigma[i] for i in range(len(pi)))


def is_full_variable(pi, sigma):
    """True iff pi[i] != sigma[i] for all i (sv = d)."""
    return all(pi[i] != sigma[i] for i in range(len(pi)))


def step_python(ms_desc, d, coefs):
    """One iteration: K(ms_desc) = sorted-desc form of |sum(c_i * x_i)|."""
    val = abs(sum(c * x for c, x in zip(coefs, ms_desc)))
    return val, tuple(sorted([int(c) for c in str(val).zfill(d)], reverse=True))


def trace_python(ms_desc, d, coefs, max_steps=80):
    """Iterate K from ms_desc until fixed-point or cycle. Returns (final_value, steps, fate).

    fate is one of: 'fixed_<value>', 'cycle', 'timeout'.
    """
    cur = ms_desc
    seen = {cur: 0}
    for n in range(1, max_steps + 1):
        val, nxt = step_python(cur, d, coefs)
        if nxt == cur:
            return val, n - 1, f'fixed_{val}'
        if nxt in seen:
            return None, n, 'cycle'
        seen[nxt] = n
        cur = nxt
    return None, max_steps, 'timeout'


# ---------------------------------------------------------------------------
# 60714's coefficient-preserving lifting at d=7 (odd ladder)
# ---------------------------------------------------------------------------

def coefs_60714_odd_ladder(d):
    """60714's coefficient-preserving lifted rule at odd d >= 5 (and d=6 for even root)."""
    if d == 5:
        return (9900, 9, 90, -9000, -999)
    if d == 6:
        return (9900, 9, 90, -9000, 99000, -99999)
    if d % 2 == 1:  # odd ladder, d >= 7
        base = [9900, 9, 90, -9000, -999]
        for k in range(6, d, 2):
            base.extend([9 * 10**k, -9 * 10**k])
        return tuple(base)
    else:  # even ladder, d >= 8
        base = [9900, 9, 90, -9000, 99000, -99999]
        for k in range(7, d, 2):
            base.extend([9 * 10**k, -9 * 10**k])
        return tuple(base)


# ---------------------------------------------------------------------------
# Numba-accelerated primitives
# ---------------------------------------------------------------------------
# These work on int64 numpy arrays / scalars and are picklable for parallel
# execution. They duplicate the python helpers above with different signatures
# so the JIT can specialize.

@njit(cache=True)
def step_numba(ms_arr, d, coefs):
    """One iteration of K on sorted-desc int8 array; returns (val, next_arr)."""
    s = 0
    for i in range(d):
        s += coefs[i] * ms_arr[i]
    if s < 0:
        s = -s
    # Convert s to d-digit padded form, then sort descending
    out = np.zeros(d, dtype=np.int64)
    tmp = s
    for i in range(d - 1, -1, -1):
        out[i] = tmp % 10
        tmp //= 10
    # Sort descending: simple insertion sort (d is small)
    for i in range(1, d):
        v = out[i]
        j = i - 1
        while j >= 0 and out[j] < v:
            out[j + 1] = out[j]
            j -= 1
        out[j + 1] = v
    return s, out


@njit(cache=True)
def trace_to_fate_numba(ms_arr, d, coefs, max_steps):
    """Iterate K until fixed-point, cycle (signaled by -1), or timeout (-2).
    Returns (final_val, steps_taken).

    Cycle detection uses a small fixed-size history (max_steps slots).
    Returns (val=fixed-point value, steps=#iterations from start) on fixed-point;
    returns (val=-1, steps=k) if a cycle is detected at step k;
    returns (val=-2, steps=max_steps) if the budget runs out.
    """
    history = np.empty((max_steps + 1, d), dtype=np.int64)
    for i in range(d):
        history[0, i] = ms_arr[i]
    cur = ms_arr.copy()
    for n in range(1, max_steps + 1):
        val, nxt = step_numba(cur, d, coefs)
        # Check fixed-point: nxt == cur
        is_fixed = True
        for i in range(d):
            if nxt[i] != cur[i]:
                is_fixed = False
                break
        if is_fixed:
            return val, n - 1
        # Check cycle: nxt matches any earlier history row
        for h in range(n):
            same = True
            for i in range(d):
                if history[h, i] != nxt[i]:
                    same = False
                    break
            if same:
                return -1, n
        for i in range(d):
            history[n, i] = nxt[i]
        cur = nxt
    return -2, max_steps


def admissibles_as_array(d):
    """All admissible sorted-desc multisets at length d as an (N, d) int64 array."""
    mss = build_admissible_multisets(d)
    arr = np.array(mss, dtype=np.int64)
    return arr


# ---------------------------------------------------------------------------
# Full-variable rule enumeration
# ---------------------------------------------------------------------------

def enumerate_full_variable_rules(d):
    """Yield every full-variable (pi, sigma) pair at digit length d.

    Number yielded = d! * D_d (derangement count).
    For d=7: 5040 * 1854 = 9,344,160 rules. The classical rule abcd...|...dcba
    is one specific rule in this set.
    """
    for pi in permutations(range(d)):
        for sigma in permutations(range(d)):
            # Full-variable check (Proposition 2.1 — sigma o pi^{-1} is a derangement)
            ok = True
            for i in range(d):
                if pi[i] == sigma[i]:
                    ok = False
                    break
            if not ok:
                continue
            yield pi, sigma


def coefs_array_from_perms_numba(pi, sigma, d):
    """int64 numpy coefs vector for (pi, sigma) — for Numba consumption."""
    arr = np.empty(d, dtype=np.int64)
    for i in range(d):
        arr[i] = 10 ** pi[i] - 10 ** sigma[i]
    return arr


# ---------------------------------------------------------------------------
# Cycle signature of (pi, sigma) — for paper §6 and Appendix D analysis
# ---------------------------------------------------------------------------

def cycle_signature(pi, sigma):
    """Cycle decomposition of pi · sigma^{-1}, returned as a sorted tuple of cycle lengths.

    Cycle signatures recur in §6: (3,3) at d=6, (2,5) and (3,4) at d=7, etc.
    """
    d = len(pi)
    sigma_inv = [0] * d
    for i in range(d):
        sigma_inv[sigma[i]] = i
    # Composition perm[i] = pi[sigma_inv[i]]
    perm = [pi[sigma_inv[i]] for i in range(d)]
    seen = [False] * d
    cycles = []
    for i in range(d):
        if seen[i]:
            continue
        c = 0
        j = i
        while not seen[j]:
            seen[j] = True
            j = perm[j]
            c += 1
        cycles.append(c)
    return tuple(sorted(cycles))


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def selftest():
    """Quick correctness check on the d=5 native rule for 60714."""
    coefs = coefs_60714_odd_ladder(5)
    assert coefs == (9900, 9, 90, -9000, -999)
    F = (7, 6, 4, 1, 0)
    val, nxt = step_python(F, 5, coefs)
    assert val == 60714, f"expected 60714, got {val}"
    assert nxt == F, f"expected fixed point at {F}"
    if HAS_NUMBA:
        F_arr = np.array(F, dtype=np.int64)
        coefs_arr = np.array(coefs, dtype=np.int64)
        val_nb, nxt_nb = step_numba(F_arr, 5, coefs_arr)
        assert val_nb == 60714
        assert tuple(nxt_nb) == F
    print("selftest: OK (Numba available: %s)" % HAS_NUMBA)


if __name__ == '__main__':
    selftest()
