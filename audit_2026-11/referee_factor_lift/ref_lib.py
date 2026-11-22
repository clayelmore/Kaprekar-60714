# Independent referee code. Direct digit-string implementation; no project imports.
import numpy as np, itertools, math

def all_multisets(b, L):
    # every sorted-descending digit string of length L in base b
    a = np.array(list(itertools.combinations_with_replacement(range(b-1, -1, -1), L)), dtype=np.int64)
    return a

def V_of(sorted_desc, rule, b):
    # rule = list of (P_q, M_q), q = 0..n-1
    v = np.zeros(sorted_desc.shape[0], dtype=np.int64)
    for q, (P, M) in enumerate(rule):
        v += (b**q) * (sorted_desc[:, P] - sorted_desc[:, M])
    return v

def K_direct(sorted_desc, rule, b):
    # literally builds word1 and word2 as integers and subtracts
    n = len(rule)
    w1 = np.zeros(sorted_desc.shape[0], dtype=np.int64)
    w2 = np.zeros_like(w1)
    for q, (P, M) in enumerate(rule):
        w1 += sorted_desc[:, P] * b**(q+n) + sorted_desc[:, M] * b**q
        w2 += sorted_desc[:, M] * b**(q+n) + sorted_desc[:, P] * b**q
    return np.abs(w1 - w2)

def digits_sorted(vals, b, L):
    d = np.empty((vals.shape[0], L), dtype=np.int64)
    v = vals.copy()
    for i in range(L):
        d[:, i] = v % b
        v //= b
    assert (v == 0).all()
    d.sort(axis=1)
    return d[:, ::-1]

def enumerate_universal(rule, b, maxit=400):
    """Complete enumeration over every digit multiset of length 2n.
    Returns (universal?, endpoint or None, max steps, info)."""
    L = 2 * len(rule)
    S = all_multisets(b, L)
    nonrep = S[:, 0] != S[:, -1]
    S = S[nonrep]
    cur = K_direct(S, rule, b)
    steps = np.ones(len(cur), dtype=np.int64)
    for it in range(maxit):
        nxt = K_direct(digits_sorted(cur, b, L), rule, b)
        ch = nxt != cur
        if not ch.any():
            break
        steps[ch] += 1
        cur = nxt
    else:
        return (False, None, None, 'cycle or >maxit', len(S))
    u = np.unique(cur)
    if len(u) == 1 and u[0] != 0:
        return (True, int(u[0]), int(steps.max()), '', len(S))
    return (False, None, None, 'endpoints=%s' % u[:6].tolist(), len(S))

def all_states(b, n):
    H = (b - 1) // 2
    return [tuple(c) for c in itertools.combinations_with_replacement(range(H + 1), n)]

def state_string(rho, b):
    return [b - 1 - r for r in rho] + [r for r in reversed(rho)]

def V_single(s, rule, b):
    return sum(b**q * (s[P] - s[M]) for q, (P, M) in enumerate(rule))

def state_of_value(K, b, n):
    # state from the digits of the image K itself (top n digits), computed from K not from m-1
    ds = []
    for i in range(2 * n):
        ds.append(K % b); K //= b
    top = ds[n:]
    return tuple(sorted(min(x, b - 1 - x) for x in top))

def classC(rule, b):
    """Check (S), (U), (C1) literally. Returns dict."""
    n = len(rule)
    sts = all_states(b, n)
    T = {}
    S_ok = True
    for rho in sts:
        v = V_single(state_string(rho, b), rule, b)
        if v <= 0:
            S_ok = False
            return dict(S=False, U=False, C1=False)
        K = (b**n - 1) * v
        T[rho] = state_of_value(K, b, n)
    fixed = [r for r in sts if T[r] == r]
    U_ok = False; tau = None; D = None
    if len(fixed) == 1:
        tau = fixed[0]; U_ok = True; D = 0
        for rho in sts:
            x = rho; k = 0
            while x != tau and k <= len(sts):
                x = T[x]; k += 1
            if x != tau:
                U_ok = False; break
            D = max(D, k)
    C1_ok = all(0 in T[rho] for rho in sts if rho[0] >= 1)
    return dict(S=S_ok, U=U_ok, C1=C1_ok, tau=tau, D=D,
                mstar=(V_single(state_string(tau, b), rule, b) if tau else None))

def covers_all_gaps(rule):
    L = 2 * len(rule)
    return all(any(min(P, M) <= j < max(P, M) for P, M in rule) for j in range(L - 1))

def top_lift(rule):
    n = len(rule)
    return [(P + 1, M + 1) for P, M in rule] + [(0, 2 * n + 1)]

def bottom_lift(rule):
    n = len(rule)
    return [(2 * n + 1, 0)] + [(P + 1, M + 1) for P, M in rule]

def digs(N, b, n):
    out = []
    for i in range(n):
        out.append(N % b); N //= b
    assert N == 0
    return out[::-1]

def F_from_Ndigits(nd, b):
    comp = [b - 1 - x for x in nd]
    v = 0
    for x in nd + comp:
        v = v * b + x
    return v
