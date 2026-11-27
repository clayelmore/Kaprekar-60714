"""Tests: gap form == direct subtraction; numpy batch == python big int; Lemmas 0-4 on adversarial
inputs. All images computed by direct subtraction of the two rearranged numbers (K_int)."""
import random
import sys
import numpy as np
from refkit import K_int, K_gap, K_sorted, K_batch, digits_of, lemma0_ok, phi_py

random.seed(int(sys.argv[1]) if len(sys.argv) > 1 else 12345)


def rand_core(N, force_x=None):
    a = list(range(N)); b = list(range(N))
    random.shuffle(a); random.shuffle(b)
    if force_x is not None:
        j = a.index(force_x); a[j], a[N - 1] = a[N - 1], a[j]
    return tuple(a), tuple(b)


def adversarial_states(N, d):
    out = []
    for m in range(9):
        out.append([9] * (d - 1) + [m])               # all 9s but one digit
        out.append([9] * (d - 2) + [m, m] if d >= 2 else [m])
    for _ in range(6):
        out.append(sorted([random.choice([8, 9]) for _ in range(d)], reverse=True))  # 8s and 9s only
        out.append(sorted([random.choice([0, 9]) for _ in range(d)], reverse=True))
        out.append(sorted([random.choice([0, 8, 9]) for _ in range(d)], reverse=True))
        r = random.randint(0, 9); k = random.randint(1, d)
        out.append(sorted([r] * k + [random.randint(0, 9) for _ in range(d - k)], reverse=True))  # many equal
        t = random.randint(N, d) if d >= N else d
        out.append(sorted([9] * t + [random.randint(0, 8) for _ in range(d - t)], reverse=True))
        out.append(sorted([random.randint(0, 9) for _ in range(d)], reverse=True))
    out.append([9] * d)
    out.append([0] * d)
    out.append([1] + [0] * (d - 1))
    out.append([9] * (d - 1) + [0])
    out.append([9] + [0] * (d - 1))
    return out


stats = dict(gap=0, batch=0, L0=0, L1=0, L2=0, L3=0, L4=0)
fails = []
max_R_seen = {}
for trial in range(4000):
    N = random.choice([2, 2, 3, 3, 4, 5, 6, 7, 8])
    fx = random.choice([None, 0, N - 1])
    a, b = rand_core(N, fx)
    x = a[N - 1]
    d = random.choice([N, N, N + 1, N + 1, N + 2] + list(range(N, N + 31)))
    l0, _ = lemma0_ok(a, b) if N <= 5 else (None, None)
    states = adversarial_states(N, d)
    imgs = []
    for s in states:
        v = K_int(s, a, b)
        imgs.append(v)
        # identity
        stats['gap'] += 1
        if K_gap(s, a, b) != v:
            fails.append(('gap', N, a, b, d, s))
        img = digits_of(v, d)
        t = s.count(9)
        sig = sum(1 for q in s if q)
        # Lemma 0
        if l0:
            stats['L0'] += 1
            if v == 0 and s[0] != s[-1]:
                fails.append(('L0', N, a, b, d, s))
        # Lemma 1
        stats['L1'] += 1
        R = sum(1 for q in img if 1 <= q <= 8)
        max_R_seen[N] = max(max_R_seen.get(N, 0), R)
        if R > N + 9:
            fails.append(('L1', N, a, b, d, s, R))
        # Lemma 2
        if t >= N and t < d:
            stats['L2'] += 1
            m = s[-1]
            t2 = img.count(9)
            exp = t - 1 - x + (1 if m == 8 else 0)
            other = sum(1 for q in img if 1 <= q <= 8)
            if t2 != exp or other > 9:
                fails.append(('L2', N, a, b, d, s, t2, exp, other))
        # Lemma 3 / 4
        if s[-1] == 0:
            stats['L3'] += 1
            S = tuple(q for q in s if q)
            nz = tuple(sorted((q for q in img if q), reverse=True))
            if nz != phi_py(S, a, b):
                fails.append(('L3a', N, a, b, d, s))
            for d2 in (len(S) + 1, d + 3, d + 11):
                if d2 < N:
                    continue
                s2 = list(S) + [0] * (d2 - len(S))
                v2 = K_int(s2, a, b)
                if v2 != v:  # value itself is length-free
                    fails.append(('L3b', N, a, b, d, d2, s))
            stats['L4'] += 1
            if len(nz) > max(sig + 1, N):
                fails.append(('L4', N, a, b, d, s, len(nz)))
    # numpy batch vs python
    Sarr = np.array(states, np.int8)
    Rb = K_batch(Sarr, a, b)
    for i, s in enumerate(states):
        stats['batch'] += 1
        vb = int(''.join(str(q) for q in Rb[i][::-1]))
        if vb != imgs[i]:
            fails.append(('batch', N, a, b, d, s))

print('checks:', stats)
print('max |R| seen per N:', dict(sorted(max_R_seen.items())), '(bound N+9)')
print('failures:', len(fails))
for f in fails[:20]:
    print('  ', f)
