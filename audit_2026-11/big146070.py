#!/usr/bin/env python3
"""146070 rule at very long lengths (exact big-integer arithmetic): random and structured inputs."""
import random, sys
def K(s, d):   # s sorted descending list of d digits
    low = 990*s[0] + 90000*s[1] - 99990*s[2] - 900*s[3] - 99*s[4] - s[5] + 10**4*s[d-1]
    H = sum(10**k*(s[k-1]-s[k]) for k in range(6, d) if s[k-1] != s[k])
    return abs(H + low)
def steps(s, d, cap=100000):
    n = 0; seen = set()
    while True:
        v = K(s, d)
        if v == 146070 and sorted(s, reverse=True)[:4] == [7,6,4,1] and s[4] == 0: return n
        if v == 0: return -1
        t = tuple(sorted(str(v).zfill(d), reverse=True))
        if t in seen: return -2
        seen.add(t); s = [int(x) for x in t]; n += 1
        if n > cap: return -3
random.seed(1)
for d in (30, 50, 100, 200, 400, 1000):
    worst = 0; bad = 0; tests = []
    for _ in range(3000 if d <= 200 else 600):
        k = random.choice([2,3,4,6,10]); ds = random.sample(range(10), min(k,10))
        tests.append(sorted((random.choice(ds) for _ in range(d)), reverse=True))
    for x in range(1,10):                      # near-repdigits and two-block states
        for y in range(10):
            if x == y: continue
            for cut in (1, 2, 5, 6, 7, d//2, d-7, d-6, d-2, d-1):
                tests.append(sorted([x]*cut + [y]*(d-cut), reverse=True))
    for s in tests:
        if len(set(s)) == 1: continue
        r = steps(s, d)
        if r < 0: bad += 1
        worst = max(worst, r)
    print(f"d={d}: {len(tests)} inputs, failures={bad}, max steps={worst}", flush=True)
