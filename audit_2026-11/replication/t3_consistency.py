"""T3: Phi(nonzero digits of s) == nonzero digits of K_d(s) for random s containing >= 1 zero."""
import random
from kap import make_K, phi

a, b = (3, 5, 1, 2, 0, 4), (1, 4, 5, 3, 2, 0)
rng = random.Random(12345)
Ks = {d: make_K(a, b, d)[0] for d in range(7, 41)}
N = 200000
mism = 0
examples = []
for t in range(N):
    d = rng.randint(7, 40)
    mode = rng.random()
    if mode < 0.4:      # uniform digits
        s = [rng.randint(0, 9) for _ in range(d)]
    elif mode < 0.7:    # few zeros, biased to high digits
        s = [rng.choice([9, 9, 9, 8, 8, 7, 1, 2, 3, 4, 5, 6]) for _ in range(d)]
    else:               # random number of zeros, rest random nonzero
        z = rng.randint(1, d)
        s = [0] * z + [rng.randint(1, 9) for _ in range(d - z)]
    s[rng.randrange(d)] = 0  # guarantee at least one zero
    lhs = tuple(x for x in Ks[d](s) if x)
    n = tuple(sorted((x for x in s if x), reverse=True))
    rhs = phi(a, b, n)
    if lhs != rhs:
        mism += 1
        if len(examples) < 5:
            examples.append((d, ''.join(map(str, sorted(s, reverse=True))), lhs, rhs))
print(f"T3 trials={N} mismatches={mism} examples={examples}")
