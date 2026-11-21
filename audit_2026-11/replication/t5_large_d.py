"""T5: direct K_d iteration at large d for the T1 core, random + adversarial inputs."""
import random
from collections import Counter
from kap import make_K

a, b = (3, 5, 1, 2, 0, 4), (1, 4, 5, 3, 2, 0)
rng = random.Random(2026)


def gen(d, kind):
    if kind == 'uniform':
        return [rng.randint(0, 9) for _ in range(d)]
    if kind == 'many9':
        k = rng.randint(d - 3, d)
        return [9] * k + [rng.randint(0, 9) for _ in range(d - k)]
    if kind == 'many8':
        k = rng.randint(d // 2, d)
        return [8] * k + [rng.randint(0, 9) for _ in range(d - k)]
    if kind == 'nozero':
        return [rng.randint(1, 9) for _ in range(d)]
    if kind == 'nozero_high':
        return [rng.choice([9, 9, 8, 8, 7, 1]) for _ in range(d)]
    if kind == 'nearrep':
        x = rng.randint(0, 9)
        s = [x] * d
        for _ in range(rng.randint(1, 3)):
            s[rng.randrange(d)] = rng.randint(0, 9)
        return s
    if kind == 'twoblock':
        x, y = rng.sample(range(10), 2)
        k = rng.randint(1, d - 1)
        return [x] * k + [y] * (d - k)
    if kind == 'threeblock':
        x, y, z = rng.sample(range(10), 3)
        i, j = sorted(rng.sample(range(1, d), 2))
        return [x] * i + [y] * (j - i) + [z] * (d - j)
    if kind == 'fewdistinct':
        al = rng.sample(range(10), rng.randint(2, 4))
        return [rng.choice(al) for _ in range(d)]
    raise ValueError(kind)


KINDS = ['uniform', 'many9', 'many8', 'nozero', 'nozero_high', 'nearrep', 'twoblock', 'threeblock', 'fewdistinct']

for d in (25, 40, 100):
    K, _ = make_K(a, b, d)
    expected = tuple(sorted([7, 6, 4, 1] + [0] * (d - 4), reverse=True))
    N = 36000
    ends = Counter()
    maxsteps = 0
    maxseed = None
    fails = []
    tested = 0
    skipped_rep = 0
    for t in range(N):
        kind = KINDS[t % len(KINDS)]
        s = tuple(sorted(gen(d, kind), reverse=True))
        if len(set(s)) == 1:
            skipped_rep += 1
            continue
        tested += 1
        seen = {}
        x = s
        steps = 0
        while x not in seen:
            seen[x] = steps
            y = K(x)
            if y == x:
                break
            x = y
            steps += 1
            if steps > 100000:
                break
        if K(x) == x:
            ends[''.join(map(str, x))] += 1
            if x != expected:
                fails.append((kind, ''.join(map(str, s)), 'fixed point ' + ''.join(map(str, x))))
            elif steps > maxsteps:
                maxsteps, maxseed = steps, (kind, ''.join(map(str, s)))
        else:
            fails.append((kind, ''.join(map(str, s)), 'cycle/period %d' % (steps - seen.get(x, 0))))
    print(f"d={d} tested={tested} (skipped repdigits={skipped_rep}) failures={len(fails)} "
          f"maxsteps={maxsteps} maxsteps_seed={maxseed} distinct_endpoints={len(ends)} "
          f"fail_examples={fails[:5]}")
