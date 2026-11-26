"""Complete enumeration of the length-8 extension GFEABDHC - HGDFCEAB in small bases.
Run from the repo root: /usr/bin/python3 theorem_paper/checks/ext8_enum.py BMAX"""
import sys, itertools
sys.path.insert(0, "audit_2026-11")
from usage_score import from_words, extend, coeffs
r8 = extend(from_words("EABDFC", "DFCEAB"), 8)
def check(b):
    c = coeffs(r8, b); P = [b**i for i in range(8)]
    def step(s):
        v = abs(sum(x*y for x, y in zip(c, s)))
        return tuple(sorted(((v // p) % b for p in P), reverse=True))
    memo = {}; ends = set(); mx = 0
    for t in itertools.combinations_with_replacement(range(b-1, -1, -1), 8):
        if t[0] == t[-1]: continue
        path = []; cur = t; pos = {}
        while cur not in memo and cur not in pos:
            pos[cur] = len(path); path.append(cur); cur = step(cur)
        if cur in memo: e, d = memo[cur]
        else:
            if pos[cur] != len(path) - 1: return ("CYCLE", cur)
            e, d = cur, -1; 
        for x in reversed(path):
            d += 1; memo[x] = (e, d)
        if cur not in memo or (cur in pos and pos[cur] == len(path)-1): memo[cur] = (e, 0)
        ends.add(e); mx = max(mx, memo[t][1])
    return ("ONE" if len(ends) == 1 else "MANY", ends if len(ends) < 4 else len(ends), mx)
for b in range(3, int(sys.argv[1]) + 1):
    print(b, check(b), flush=True)
