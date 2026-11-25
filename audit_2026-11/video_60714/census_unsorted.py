"""Census of rules WITHOUT the sorting step, base 10, D digits (written 2026-11-25).
A rule is a pair of fixed shuffles (P, Q) of the digit POSITIONS of the number as written; the step is
|P(n) - Q(n)|, padded to D digits. No sorting anywhere. All D!(D!-1)/2 unordered pairs, every start 0..10^D-1.
For each rule: where does everything end up?  Usage: /usr/bin/python3 census_unsorted.py D"""
import sys, itertools, numpy as np
from collections import Counter
D = int(sys.argv[1]); N = 10 ** D
n = np.arange(N, dtype=np.int64)
dig = np.stack([(n // 10 ** (D - 1 - k)) % 10 for k in range(D)], axis=1)   # digits as written, left to right
rep = (dig == dig[:, :1]).all(axis=1)
pw = 10 ** np.arange(D - 1, -1, -1, dtype=np.int64)
perms = list(itertools.permutations(range(D)))
W = np.zeros((len(perms), D), dtype=np.int64)
for i, p in enumerate(perms):
    for k, src in enumerate(p): W[i, src] = pw[k]            # shuffle p puts the digit from position src at place k
vals = (dig @ W.T).astype(np.int32)
name = lambda p: "".join(str(x + 1) for x in p)
rows = []
for i in range(len(perms) - 1):
    f = np.abs(vals[:, i:i+1] - vals[:, i+1:]).astype(np.int32)          # all partners j > i
    cols = np.arange(f.shape[1])
    g = f.copy()
    for _ in range(18): g = g[g, cols]                                   # 2^18 steps: every start is on its cycle
    g1 = f[g, cols]
    for r in cols:
        end = g[:, r]; onfix = (g1[:, r] == end)                         # ended on a fixed point (not a longer cycle)
        to0 = (end == 0)
        c = Counter(end[onfix & ~to0].tolist())
        F, basin = c.most_common(1)[0] if c else (0, 0)
        rows.append((name(perms[i]), name(perms[i+1+r]), int(to0.sum()), int((~onfix).sum()), F, basin, len(c)))
rows.sort(key=lambda r: -r[5])
with open("census_unsorted_d%d.tsv" % D, "w") as fh:
    fh.write("P\tQ\tstarts_ending_at_0\tstarts_ending_in_a_loop\tbest_fixed_point\tits_basin\tnumber_of_nonzero_fixed_points_reached\n")
    for r in rows: fh.write("\t".join(map(str, r)) + "\n")
nonrep = N - 10
print("D=%d rules=%d starts=%d" % (D, len(rows), N))
print("universal rules (every non-repdigit reaches one nonzero number):", sum(1 for r in rows if r[5] == nonrep))
print("rules where at least half of all starts reach one nonzero number:", sum(1 for r in rows if r[5] >= N / 2))
print("rules where NO start reaches a nonzero fixed number:", sum(1 for r in rows if r[5] == 0))
z = np.array([r[2] for r in rows]); lp = np.array([r[3] for r in rows])
print("share of starts ending at 0: median %.1f%%, min %.1f%%" % (100*np.median(z)/N, 100*z.min()/N))
print("share of starts ending in a loop: median %.1f%%, max %.1f%%" % (100*np.median(lp)/N, 100*lp.max()/N))
print("best ten rules (P, Q, to 0, in loops, fixed point, basin, #fixed points):")
for r in rows[:10]: print("  ", r)
