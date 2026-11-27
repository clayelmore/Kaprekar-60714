# Checks for PROOF_THRESHOLD.md (2026-11-27). Everything here uses direct subtraction of the two rearranged
# digit strings (no gap form), so it is independent of closure_all.c / censusN.c / threshold_test.c.
# Extended N-letter core (a, b) at length d: sorted digit i goes to place A(i) in the first number and B(i)
# in the second, A = (a_0..a_{N-2}, N, N+1, ..., d-1, a_{N-1}), B = (b_0..b_{N-1}, N, ..., d-1).
import random, sys
random.seed(20261127)
def places(a, b, d):
    N = len(a)
    A = list(a[:N-1]) + list(range(N, d)) + [a[N-1]]
    B = list(b) + list(range(N, d))
    assert sorted(A) == list(range(d)) and sorted(B) == list(range(d))
    return A, B
def K(a, b, s):               # s sorted descending, length d; returns sorted digits of the image
    d = len(s); A, B = places(a, b, d)
    v = abs(sum(x * (10**A[i] - 10**B[i]) for i, x in enumerate(s)))
    return sorted((int(c) for c in str(v).zfill(d)), reverse=True)
def split(img):               # (number of 9s, list of other nonzero digits)
    return img.count(9), [x for x in img if 0 < x < 9]
def rand_core(N):
    while True:
        a = random.sample(range(N), N); b = random.sample(range(N), N)
        if all(x != y for x, y in zip(a, b)): return a, b
def rand_sorted(d):
    k = random.choice([1, 2, 3, 5, 9])
    pool = random.sample(range(10), min(k + 1, 10))
    return sorted((random.choice(pool) for _ in range(d)), reverse=True)
cnt = dict(lemma1=0, drain=0, growth=0, lenfree=0, orbit=0)
worst_R = 0; worst_orbit = {}; worst_drainR = 0
for N in (4, 5, 6, 7, 8):
    worst_orbit[N] = 0
    for _ in range(400 if N < 8 else 150):
        a, b = rand_core(N); x = a[N-1]
        # Lemma 1: one step from any state leaves at most N + 9 nonzero digits other than 9
        for _ in range(40):
            d = random.randint(N, 60); s = rand_sorted(d)
            t, R = split(K(a, b, s)); assert len(R) <= N + 9, (a, b, s); worst_R = max(worst_R, len(R) - N); cnt['lemma1'] += 1
        # Lemma 2 (drain): state 9^t + R (+ zeros), t >= N, not all 9s
        for _ in range(40):
            t = random.randint(N, 40); r = random.randint(0, 14); z = random.randint(0, 6)
            R = [random.randint(1, 8) for _ in range(r)]
            if r == 0 and z == 0: z = 1
            s = sorted([9] * t + R + [0] * z, reverse=True); m = s[-1]
            t2, R2 = split(K(a, b, s))
            want = t - 1 - x + (1 if m == 8 else 0)
            assert t2 == want, (a, b, s, t2, want)
            assert len(R2) <= 9, (a, b, s); worst_drainR = max(worst_drainR, len(R2)); cnt['drain'] += 1
        # growth: with a zero present, nonzero count goes up by at most 1 (or stays <= N)
        # length-free: with a zero present, the nonzero digits of the image do not depend on d
        for _ in range(40):
            d = random.randint(N + 1, 50); s = rand_sorted(d)
            if s[-1] != 0 or s[0] == 0: continue
            sig = sum(1 for v in s if v)
            img = K(a, b, s); sig2 = sum(1 for v in img if v)
            assert sig2 <= max(sig + 1, N), (a, b, s); cnt['growth'] += 1
            s2 = s + [0] * random.randint(1, 9)
            assert [v for v in K(a, b, s2) if v] == [v for v in img if v], (a, b, s); cnt['lenfree'] += 1
        # orbit bound: from a seed (#9 <= N-1, other nonzero <= N+9), every later state has <= 2N+13 nonzero digits
        for _ in range(12):
            t = random.randint(0, N - 1); r = random.choice([N + 9, N + 9, N + 8, random.randint(0, N + 9)])
            style = random.random()
            if style < 0.4: R = [random.randint(1, 8) for _ in range(r)]
            elif style < 0.7: R = [random.choice([8, 7])] * r
            else: R = [random.choice([1, 8])] * r
            nz = sorted([9] * t + R, reverse=True)
            if not nz: continue
            seen = set()
            for step in range(400):
                key = tuple(nz)
                if key in seen or not nz: break
                seen.add(key)
                assert len(nz) <= 2 * N + 13, (a, b, nz)
                worst_orbit[N] = max(worst_orbit[N], len(nz))
                s = nz + [0] * max(3, N + 1 - len(nz))   # padding: at least one zero, so this is the length-free map
                nz = [v for v in K(a, b, s) if v]
            cnt['orbit'] += 1
print("cases:", cnt)
print("largest |R| - N seen in Lemma 1 (bound 9):", worst_R)
print("largest |R'| seen after a drain step (bound 9):", worst_drainR)
print("largest nonzero count on seed orbits, by N (bound 2N+13):", worst_orbit)
print("ALL CHECKS PASS")
