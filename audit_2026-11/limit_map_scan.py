#!/usr/bin/env python3
"""Find cycles of the length-8 extension of EABDFC - DFCEAB by sampling, base by base (2026-11-22).
Prints, per base, each distinct cycle (period, smallest point, point divided by b-1)."""
import sys, random
from usage_score import from_words, extend, coeffs
r8 = extend(from_words("EABDFC", "DFCEAB"), 8); L = 8
def cycles(b, ns, seed=1):
    rng = random.Random(seed * 7919 + b); c = coeffs(r8, b); found = {}; fixed = set()
    for _ in range(ns):
        s = tuple(sorted((rng.randrange(b) for _ in range(L)), reverse=True))
        if s[0] == s[-1]: continue
        seen = {}
        while s not in seen:
            seen[s] = len(seen)
            v = abs(sum(x * y for x, y in zip(c, s)))
            s = tuple(sorted(((v // b ** i) % b for i in range(L)), reverse=True))
        per = len(seen) - seen[s]
        if per == 1: fixed.add(s); continue
        cyc = [s]
        for _ in range(per - 1):
            v = abs(sum(x * y for x, y in zip(c, cyc[-1])))
            cyc.append(tuple(sorted(((v // b ** i) % b for i in range(L)), reverse=True)))
        key = min(cyc); found[key] = (per, found.get(key, (0, 0))[1] + 1)
    return found, fixed
if __name__ == '__main__':
    lo, hi, ns = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    for b in range(lo, hi + 1):
        f, fx = cycles(b, ns)
        print(f"base {b}: fixed points {len(fx)}; cycles {len(f)}", flush=True)
        for k, (per, hits) in sorted(f.items()):
            print(f"    period {per} hits {hits}/{ns}  {k}  /(b-1): {' '.join('%.3f' % (x/(b-1)) for x in k)}")
