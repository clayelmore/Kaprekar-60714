"""Extra: Phi orbits from random multisets OUTSIDE S (more than five 9s and/or more than
fifteen digits from 1..8), T1 core. Checks they still reach {7,6,4,1}; reports steps/size."""
import random
from kap import phi

a, b = (3, 5, 1, 2, 0, 4), (1, 4, 5, 3, 2, 0)
tgt = (7, 6, 4, 1)
rng = random.Random(7)
N = 100000
fails = []
maxsteps = 0
maxseed = None
for t in range(N):
    n9 = rng.randint(0, 80)
    nlow = rng.randint(0 if n9 > 5 else 16, 80)
    w = [rng.random() for _ in range(8)]
    low = rng.choices(range(1, 9), weights=w, k=nlow)
    x = tuple(sorted([9] * n9 + low, reverse=True))
    if not x:
        continue
    seed = x
    seen = set()
    st = 0
    while x != tgt and x and x not in seen:
        seen.add(x)
        x = phi(a, b, x)
        st += 1
    if x != tgt:
        fails.append((''.join(map(str, seed)), ''.join(map(str, x)) or '{}'))
    elif st > maxsteps:
        maxsteps, maxseed = st, ''.join(map(str, seed))
print(f"outside-S trials={N} fails={len(fails)} examples={fails[:5]} maxsteps={maxsteps} seed={maxseed}")
