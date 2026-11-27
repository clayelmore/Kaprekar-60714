"""Brute-force universality of K_d for a core, by direct subtraction, independent of the lemmas.

Stage 1 (refutation by sampling, exact when it refutes): follow K_d orbits of sampled multisets with
python big ints; if a non-repdigit reaches a repdigit (0), or two non-repdigits end in different cycles,
or the common terminal cycle has period > 1, the rule is not universal (witness recorded).
Stage 2 (complete): if stage 1 does not refute, enumerate ALL digit multisets of length d, compute
K_d of each (numpy column subtraction), build the functional graph on multisets and decide exactly.
"""
import random
import numpy as np
from refkit import K_sorted, K_batch, counts_to_sorted, digit_counts, all_count_vectors, keys_of, \
    pointer_double, digits_of, K_int


def orbit_terminal(s, a, b):
    seen = {}
    cur = tuple(s)
    seq = []
    while cur not in seen:
        seen[cur] = len(seq)
        seq.append(cur)
        cur = tuple(K_sorted(list(cur), a, b))
    cyc = seq[seen[cur]:]
    return frozenset(cyc), len(cyc)


def stage1(a, b, d, nsamp=400, rng=None):
    rng = rng or random.Random(1)
    samples = []
    for _ in range(nsamp):
        s = sorted([rng.randint(0, 9) for _ in range(d)], reverse=True)
        samples.append(s)
    for m in range(9):
        samples.append([9] * (d - 1) + [m])
        samples.append([m + 1] + [m] * (d - 1))
        samples.append([9] + [m] * (d - 1))
    for _ in range(nsamp // 4):
        k = rng.randint(1, 3)
        dig = rng.sample(range(10), k + 1)
        s = sorted([rng.choice(dig) for _ in range(d)], reverse=True)
        samples.append(s)
    term = {}
    wit = {}
    for s in samples:
        if s[0] == s[-1]:
            continue
        T, p = orbit_terminal(s, a, b)
        if T not in term:
            term[T] = p
            wit[T] = s
        if len(term) > 1:
            break
    if len(term) > 1:
        ts = list(term)
        return dict(universal=False, stage=1, reason='two terminal cycles',
                    witness=[''.join(map(str, wit[t])) for t in ts],
                    terminals=[sorted(''.join(map(str, c)) for c in t) for t in ts])
    (T, p), = term.items()
    zero = tuple([0] * d)
    if zero in T:
        return dict(universal=False, stage=1, reason='reaches 0', witness=[''.join(map(str, wit[T]))])
    if p > 1:
        return dict(universal=False, stage=1, reason='common cycle of period %d' % p,
                    witness=[''.join(map(str, wit[T]))], cycle=sorted(''.join(map(str, c)) for c in T),
                    single_cycle_candidate=True)
    return None


def stage2(a, b, d):
    blocks = []
    for c9 in range(d + 1):
        v = all_count_vectors(d - c9, 9)
        blocks.append(np.concatenate([v, np.full((v.shape[0], 1), c9, np.int16)], axis=1))
    C = np.concatenate(blocks)
    del blocks
    keys = keys_of(C)
    order = np.argsort(keys)
    C = C[order]; keys = keys[order]
    n = C.shape[0]
    f = np.empty(n, np.int64)
    step = 1000000
    for i in range(0, n, step):
        S = counts_to_sorted(C[i:i + step], d)
        R = K_batch(S, a, b)
        ik = keys_of(digit_counts(R, lo=0))
        j = np.searchsorted(keys, ik)
        assert np.all(keys[j] == ik)
        f[i:i + step] = j
    rep = C.max(1) == d
    g, _ = pointer_double(f, None, rounds=40)
    land = g[~rep]
    ul, cnt = np.unique(land, return_counts=True)
    res = dict(stage=2, n_multisets=int(n))
    def strof(j):
        return ''.join(str(9 - k) * int(C[j][9 - k]) for k in range(10))
    if len(ul) == 1 and f[ul[0]] == ul[0] and not rep[ul[0]]:
        res.update(universal=True, F_multiset=strof(ul[0]))
        # the integer F
        s = [int(q) for q in strof(ul[0])]
        res['F'] = str(K_int(s, a, b)).zfill(d)
        return res
    # not universal: describe
    res['universal'] = False
    # cycles of the landing nodes
    cycles = {}
    for u in ul:
        cyc = [int(u)]
        w = f[u]
        while w != u:
            cyc.append(int(w)); w = f[w]
        cycles[min(cyc)] = cyc
    res['n_terminal_cycles'] = len(cycles)
    res['cycle_periods'] = sorted(len(c) for c in cycles.values())
    res['reaches_repdigit'] = bool(rep[ul].any())
    # a witness non-repdigit for each of the first two cycles
    wits = []
    nonrep_idx = np.nonzero(~rep)[0]
    for key, cyc in list(cycles.items())[:2]:
        cs = set(cyc)
        j = nonrep_idx[np.isin(land, np.array(cyc))][0]
        wits.append(dict(start=strof(j), cycle=[strof(c) for c in cyc][:6]))
    res['witnesses'] = wits
    return res


def universal(a, b, d, force_full=False):
    if not force_full:
        r = stage1(a, b, d)
        if r is not None:
            return r
    return stage2(a, b, d)
