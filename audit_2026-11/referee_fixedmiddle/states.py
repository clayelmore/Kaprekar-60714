"""State-level tests for large bases. The next state is computed by building the actual image string
from the deficit multiset and applying the direct rule (rule.py) -- NOT the reduced formulas.
The reduced formulas of 2.1/3.1 are checked against it separately."""
import sys, random, time
from itertools import combinations_with_replacement
import rule

def setup(n, b):
    L = 2 * n + 1; H = (b - 1) // 2
    step = rule.make_step(n, b)
    F = (b - 1) * (b ** (n + 1) - 1)
    def image(rho):  # rho sorted ascending, length n
        d = [b - 1] + [b - 1 - r for r in rho] + list(reversed(rho))
        return tuple(sorted(d, reverse=True))
    def state_of(digs):  # digs sorted descending, image shape required
        assert digs[0] == b - 1, digs
        rho = tuple(digs[2 * n + 1 - i] for i in range(1, n + 1))
        for i in range(1, n + 1):
            assert digs[i] == b - 1 - rho[i - 1], ("shape", digs)
        return rho
    T = {}
    def nxt(rho):
        if rho not in T:
            d, val = step(image(rho))
            assert val != 0
            T[rho] = (state_of(d), val)
        return T[rho]
    return L, H, F, nxt

def r_(x, b): return min(x, b - 1 - x)

def reduced(n, b, rho):
    """the reduced maps as stated in 2.1 / 3.1 (rho tuple ascending, rho[0]=rho_1)."""
    R = (None,) + rho
    if n % 2:
        k = (n - 1) // 2
        w = [None] + [R[2 * j + 1] - R[2 * j] for j in range(1, k + 1)]
        A = b - 1 - R[1]
        if all(w[j] == 0 for j in range(1, k + 1)):
            out = [0] * (n - 1) + [r_(A - 1, b)]
        else:
            J = max(j for j in range(1, k + 1) if w[j] >= 1)
            out = []
            for j in range(1, J): out += [max(w[j] - 1, 0)] * 2
            out += [w[J] - 1, w[J]] + [0] * (2 * (k - J)) + [R[1]]
    else:
        k = (n - 2) // 2
        w = [None] + [R[2 * j + 2] - R[2 * j + 1] for j in range(1, k + 1)]
        sig = b - 1 - R[1] - R[2]; sig2 = b - 1 - R[2]; h = r_(sig, b)
        if all(w[j] == 0 for j in range(1, k + 1)):
            if sig >= 1: out = [0] * (n - 2) + [R[2], r_(sig - 1, b)]
            else: out = [0] * (n - 1) + [r_(sig2 - 1, b)]
        else:
            J = max(j for j in range(1, k + 1) if w[j] >= 1)
            out = []
            for j in range(1, J): out += [max(w[j] - 1, 0)] * 2
            out += [w[J] - 1, w[J]] + [0] * (2 * (k - J)) + [h, R[2]]
    assert len(out) == n
    return tuple(sorted(out))

def bad(n, b, rho):
    R = (None,) + rho
    if n % 2:
        k = (n - 1) // 2
        return R[1] >= 1 and all(R[2 * j + 1] - R[2 * j] >= 2 for j in range(1, k + 1))
    k = (n - 2) // 2
    w = [None] + [R[2 * j + 2] - R[2 * j + 1] for j in range(1, k + 1)]
    h = r_(b - 1 - R[1] - R[2], b)
    return (R[2] >= 1 and all(w[j] >= 2 for j in range(1, k)) and w[k] >= 1
            and not (w[k] == 1 and h == 0))

def runbound(n, H):
    if n % 2: return max(0, H - 2)
    if n == 4: return max(0, 2 * H - 2)
    return H

def stepbound(n, b):
    if n % 2: return b / 2 + 3
    if n == 4: return b + 2
    return b / 2 + 5

def check(n, b, states, label):
    L, H, F, nxt = setup(n, b)
    tau = tuple([0] * (n - 1) + [1])
    s, v = nxt(tau)
    assert s == tau and v == F, "tau"
    key = 0 if n % 2 else 1  # index of rho_1 (odd) / rho_2 (even)
    viol = []
    maxrun = 0; maxsteps = 0
    run = {}; g = {}
    def G(rho):  # steps from image of rho until value F produced
        path = []; cur = rho
        while cur not in g:
            s, v = nxt(cur)
            if v == F: g[cur] = 1; break
            path.append(cur); cur = s
            if len(path) > 4 * b + 50: raise SystemExit(("cycle?", n, b, rho))
        d = g[cur]
        for x in reversed(path): d += 1; g[x] = d
        return g[rho]
    def RUN(rho):
        path = []; cur = rho
        while cur not in run:
            if not bad(n, b, cur): run[cur] = 0; break
            path.append(cur); cur = nxt(cur)[0]
            if len(path) > 4 * b + 50: raise SystemExit(("badcycle", n, b, rho))
        d = run[cur]
        for x in reversed(path): d += 1; run[x] = d
        return run[rho]
    cnt = 0
    for rho in states:
        cnt += 1
        if n % 2 == 0 and False: pass
        s1, v1 = nxt(rho)
        # reduced formula agrees with direct rule
        if reduced(n, b, rho) != s1: viol.append(("reduced", rho, s1, reduced(n, b, rho)))
        Bd = bad(n, b, rho)
        if rho[key] >= 1 and not Bd and s1[key] != 0: viol.append(("nonbad->0", rho, s1))
        if rho[key] == 0:
            s2 = nxt(s1)[0]
            if not (s1 == tau or s2 == tau): viol.append(("2 steps to tau", rho, s1, s2))
        if Bd:
            Lam, mu = rho[-1], rho[key]
            if n % 2:
                if max(s1) > Lam - 1: viol.append(("2.4", rho, s1))
            elif n >= 6:
                if max(s1) > max(Lam - mu - 1, 2 * mu): viol.append(("3.4a", rho, s1))
                if 2 * s1[1] > Lam - mu - 1: viol.append(("3.4b", rho, s1))
                if bad(n, b, s1):
                    s2 = nxt(s1)[0]
                    if s2[-1] > max(Lam, s1[-1]) - 2: viol.append(("3.4c", rho, s1, s2))
            else:
                if bad(n, b, s1):
                    s2 = nxt(s1)[0]
                    if s2[-1] > Lam - 1: viol.append(("3.5", rho, s1, s2))
        rl = RUN(rho); maxrun = max(maxrun, rl)
        if rl > runbound(n, H): viol.append(("runlen", rho, rl))
        st = 1 + G(rho); maxsteps = max(maxsteps, st)
        if st > stepbound(n, b): viol.append(("steps", rho, st))
    print(f"n={n} b={b} H={H} [{label}] states={cnt} maxbadrun={maxrun} (bound {runbound(n,H)}) "
          f"max 1+steps={maxsteps} (bound {stepbound(n,b)}) violations={len(viol)}", flush=True)
    for x in viol[:5]: print("   ", x)
    return viol

def all_states(n, H):
    return combinations_with_replacement(range(H + 1), n)

def sample(n, H, N, rng):
    for _ in range(N):
        yield tuple(sorted(rng.randint(0, H) for _ in range(n)))

if __name__ == "__main__":
    mode = sys.argv[1]; n = int(sys.argv[2]); bases = [int(x) for x in sys.argv[3].split(",")]
    rng = random.Random(12345)
    for b in bases:
        H = (b - 1) // 2
        t = time.time()
        if mode == "all": check(n, b, all_states(n, H), "all")
        else: check(n, b, sample(n, H, int(sys.argv[4]), rng), "sample")
