#!/usr/bin/env python3
"""Independent check of class-C seeds and their lifts with univcheck (every digit multiset, base 10).
Usage: factor_brute.py COUNT [SEED]   picks COUNT class-C rules at n=5, checks seed (10 digits), both lifts
(12 digits) and all four two-level lifts (14 digits)."""
import sys, random, subprocess, itertools
from factor_classZ import lift_top, lift_bottom
def run(a, n, m):
    L = 2*n; w1 = [0]*L; w2 = [0]*L
    for q in range(n):
        P, M = a[2*q], a[2*q+1]
        w1[P] = q+n; w2[P] = q; w1[M] = q; w2[M] = q+n
    F = (10**n - 1) * m
    r = subprocess.run(["./univcheck", str(L), str(F), ",".join(map(str,w1)), ",".join(map(str,w2))],
                       capture_output=True, text=True).stdout.strip()
    return r, F
rows = [ln.split('\t') for ln in open("factor/classC_b10_n5.tsv").read().split('\n')[1:] if ln]
random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
bad = tot = 0
for m, F, a in random.sample(rows, int(sys.argv[1])):
    m = int(m); a = list(map(int, a.split(',')))
    r, F0 = run(a, 5, m); tot += 1; bad += r != "PASS"
    line = [f"{F0:010d}:{r}"]
    for seq in itertools.product("TB", repeat=2):
        aa, mm, nn = a, m, 5
        for i, c in enumerate(seq):
            aa = lift_top(aa) if c == "T" else lift_bottom(aa)
            mm = 9 * 10**nn + mm if c == "T" else 10 * mm - 9
            nn += 1
            if i == 1 or seq[1] == "T":
                r, FF = run(aa, nn, mm); tot += 1; bad += r != "PASS"
                line.append(f"{''.join(seq[:i+1])} {FF:0{2*nn}d}:{r}")
    print("  ".join(line), flush=True)
print(f"# univcheck runs {tot}, not PASS {bad}")
