"""Own implementation of seeds, Phi, the closure check, and the Proposition 1 orbit bound.

Phi(S) = nonzero digits of K_D(S + zeros) for a fixed D larger than every multiset met (asserted),
computed by direct column subtraction (refkit.K_batch). The note's Lemma 3 (tested separately in
test_lemmas.py) says this does not depend on D.
"""
import numpy as np
from refkit import (K_batch, counts_to_sorted, digit_counts, all_count_vectors, keys_of,
                    pointer_double, lemma0_ok)


def seeds_array(N):
    """All seeds as (M, 9) count arrays for digits 1..9: <= N-1 nines, <= N+9 digits in 1..8, nonempty."""
    v = all_count_vectors(N + 9, 9)[:, :8]  # 8 counts with sum <= N+9
    blocks = []
    for t in range(N):
        blk = np.concatenate([v, np.full((v.shape[0], 1), t, np.int16)], axis=1)
        blocks.append(blk)
    C = np.concatenate(blocks)
    C = C[C.sum(1) > 0]
    return C.astype(np.int16)


def phi_batch(C9, a, b, D):
    sig = C9.sum(1)
    assert sig.max() < D, 'state too large for D'
    S = counts_to_sorted(C9, D)
    out = np.empty_like(C9)
    step = 400000
    for i in range(0, C9.shape[0], step):
        R = K_batch(S[i:i + step], a, b)
        out[i:i + step] = digit_counts(R, lo=1)
    return out


def closure_check(a, b, D=None, seeds=None, want_lemma0=True):
    N = len(a)
    if D is None:
        D = 2 * N + 40
    if seeds is None:
        seeds = seeds_array(N)
    l0, l0wit = lemma0_ok(a, b) if want_lemma0 else (None, None)
    # forward closure of the state set
    known_keys = np.unique(keys_of(seeds))
    states = [seeds]
    frontier = seeds
    allC = [seeds]
    while frontier.shape[0]:
        img = phi_batch(frontier, a, b, D)
        k = keys_of(img)
        uk, ui = np.unique(k, return_index=True)
        new = ~np.isin(uk, known_keys)
        frontier = img[ui[new]]
        if frontier.shape[0]:
            allC.append(frontier)
            known_keys = np.union1d(known_keys, uk[new])
    C = np.concatenate(allC)
    keys = keys_of(C)
    order = np.argsort(keys)
    C = C[order]; keys = keys[order]
    assert np.all(np.diff(keys) > 0)
    img = phi_batch(C, a, b, D)
    f = np.searchsorted(keys, keys_of(img))
    assert np.all(keys[f] == keys_of(img))
    sig = C.sum(1).astype(np.int64)
    g, mx = pointer_double(f, sig)
    sidx = np.searchsorted(keys, keys_of(seeds))
    land = g[sidx]
    M = int(mx[sidx].max())
    argM = int(sidx[np.argmax(mx[sidx])])
    uland = np.unique(land)
    fixed = bool(np.all(f[uland] == uland))
    nonempty = bool(np.all(sig[uland] > 0))
    passes = bool(l0) and len(uland) == 1 and fixed and nonempty
    # describe terminal behaviour
    term = []
    for u in uland[:5]:
        cyc = [int(u)]
        w = f[u]
        while w != u:
            cyc.append(int(w)); w = f[w]
        term.append([tuple(int(q) for q in C[j]) for j in cyc])
    return dict(N=N, a=a, b=b, lemma0=l0, lemma0_witness=l0wit, passes=passes, M=M,
                M_state=tuple(int(q) for q in C[argM]), n_seeds=int(seeds.shape[0]),
                n_states=int(C.shape[0]), n_terminal=int(len(uland)), terminal=term,
                fixed_terminal=fixed, max_state=int(sig.max()))


def counts_str(c9):
    return ''.join(str(9 - i) * int(c9[8 - i]) for i in range(9))
