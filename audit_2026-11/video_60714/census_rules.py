"""Census of every rearrangement-subtraction rule at D digits (base 10), written 2026-11-25, independent of June code.
A rule is a pair of arrangements (P, Q) of the sorted digits; the step is |P - Q|, padded to D digits.
Rules (P, Q) and (Q, P) are the same map, so unordered pairs are enumerated: D!(D!-1)/2 of them.
A rule is UNIVERSAL here if every D-digit string that is not a repdigit reaches one fixed number (strict:
near-repdigits such as 00001 are included, leading zeros kept).
Usage: /usr/bin/python3 census_rules.py D   -> writes census_dD.tsv (endpoint, P, Q, max steps)"""
import sys, itertools, numpy as np
D = int(sys.argv[1])
ms = np.array(list(itertools.combinations_with_replacement(range(9, -1, -1), D)), dtype=np.int64)  # sorted descending
pw = 10 ** np.arange(D - 1, -1, -1, dtype=np.int64)
keys = ms @ pw                      # the sorted-descending number identifies the multiset
order = np.argsort(keys); skeys = keys[order]
rep = (ms[:, 0] == ms[:, -1])
N = len(ms)
perms = list(itertools.permutations(range(D)))
# arrangement p: letter p[k] stands at place k (most significant first) -> weight vector over letters
W = np.zeros((len(perms), D), dtype=np.int64)
for i, p in enumerate(perms):
    for k, letter in enumerate(p): W[i, letter] = pw[k]
vals = ms @ W.T                     # vals[m, i] = value of arrangement i on multiset m
letters = "ABCDEFGH"[:D]
name = lambda p: "".join(letters[x] for x in p)
out, nrules = [], 0
for i in range(len(perms)):
    K = np.abs(vals[:, i:i+1] - vals[:, i+1:])          # all partners j > i at once: shape (N, n-i-1)
    if K.shape[1] == 0: break
    nrules += K.shape[1]
    dig = np.empty(K.shape + (D,), dtype=np.int64); t = K.copy()
    for k in range(D): dig[..., k] = t % 10; t //= 10
    dig.sort(axis=-1)                                   # ascending; weights reversed give the descending number
    f = order[np.searchsorted(skeys, dig @ pw[::-1])]   # f[m, r] = index of the multiset of K
    cols = np.arange(K.shape[1])
    g = f.copy(); steps = 1
    while steps < 4096:
        g2 = g[g, cols]
        if np.array_equal(g2, g): break
        g, steps = g2, steps * 2
    tgt = g[~rep]                                       # where every non-repdigit multiset ends up
    ok = (tgt == tgt[0]).all(axis=0) & (f[tgt[0], cols] == tgt[0]) & ~rep[tgt[0]]
    for r in np.nonzero(ok)[0]:
        m = tgt[0, r]; F = int(K[m, r])
        # exact longest trip for this rule
        h = f[:, r]; cur = np.arange(N); n = 0
        while not (cur[~rep] == m).all(): cur = h[cur]; n += 1
        out.append((F, name(perms[i]), name(perms[i + 1 + r]), n))
out.sort()
with open("census_d%d.tsv" % D, "w") as fh:
    for row in out: fh.write("%0*d\t%s\t%s\t%d\n" % (D, *row))
ends = sorted({r[0] for r in out})
print("D=%d  multisets=%d  rules=%d  universal rules=%d  distinct endpoints=%d" % (D, N, nrules, len(out), len(ends)))
if D <= 5: print("endpoints:", ends)
