#!/usr/bin/env python3
# Independent large-d tests of the 146070 rule: Lemma 1, Lemma 2 (exact R'), Lemma 3, main claim, step bound.
import random, sys
from collections import Counter

def place_maps(d):
    if d == 6:
        return [3,5,1,2,0,4], [1,4,5,3,2,0]
    a = [3,5,1,2,0] + list(range(6, d)) + [4]
    b = [1,4,5,3,2,0] + list(range(6, d))
    assert sorted(a) == list(range(d)) and sorted(b) == list(range(d))
    return a, b

_cache = {}
def K(digs, d):
    """Definition: place sorted digit s_i at place a_i (resp. b_i), subtract, absolute value."""
    if d not in _cache:
        _cache[d] = place_maps(d)
    a, b = _cache[d]
    s = sorted(digs, reverse=True)
    assert len(s) == d
    A = ['0']*d; Bc = ['0']*d
    for i in range(d):
        A[d-1-a[i]] = str(s[i]); Bc[d-1-b[i]] = str(s[i])
    return abs(int(''.join(A)) - int(''.join(Bc)))

def digits(x, d):
    st = str(x).rjust(d, '0')
    assert len(st) == d
    return [int(ch) for ch in st]

def orbit_steps(digs, d, cap=100000):
    x_digs = list(digs)
    if len(set(x_digs)) == 1:
        return None
    x = int(''.join(map(str, x_digs)))
    steps = 0
    seen = set()
    while x != 146070:
        key = tuple(sorted(digits(x, d)))
        if key in seen:
            return ('CYCLE', steps)
        seen.add(key)
        x = K(digits(x, d), d)
        steps += 1
        if x == 0:
            return ('ZERO', steps)
        if steps > cap:
            return ('CAP', steps)
    return steps

def R_of(x, d):
    dg = digits(x, d)
    return [v for v in dg if 1 <= v <= 8], dg.count(9)

def lemma2_pred(state, d):
    """state digits; t>=6 nines, others 1..8 or 0. Return predicted (t', Counter R')."""
    t = state.count(9)
    R = sorted([v for v in state if 1 <= v <= 8], reverse=True)
    has0 = 0 in state
    if has0:
        if not R:
            Rp = [8, 1]
        else:
            gaps = [R[i]-R[i+1] for i in range(len(R)-1)]
            Rp = [8 - R[0]] + gaps + [R[-1], 1]
        tp = t - 5
    else:
        m = min(state)
        gaps = [R[i]-R[i+1] for i in range(len(R)-1)]
        if m == 8:
            return t - 4, Counter()
        Rp = [8 - R[0]] + gaps + [1 + m]
        tp = t - 5
    return tp, Counter(v for v in Rp if v != 0)

def check_lemma2(state, d):
    t = state.count(9)
    if t < 6 or t == d:
        return True
    img = K(state, d)
    R, t2 = R_of(img, d)
    tp, Rp = lemma2_pred(state, d)
    dg = digits(img, d)
    ok = (t2 == tp and Counter(R) == Rp and dg.count(0) >= 4 and sum(R) == (9 if Rp else 0))
    if not ok:
        print("LEMMA2 FAIL", d, ''.join(map(str, state)), '->', img, t2, tp, sorted(R), sorted(Rp.elements()))
    return ok

def structured(d, rng):
    out = []
    for r in range(9):
        for pos in range(d):
            s = [9]*d; s[pos] = r; out.append(s)              # all 9s but one digit
    for k in range(1, d):
        for z in (0, 1, 5, 8):
            out.append([9]*k + [z]*(d-k))                      # run of 9s then constant
    for k in range(1, d):
        out.append([9]*k + [0]*(d-k-1) + [1])
        out.append([1] + [0]*(d-1))
        out.append([9]*k + list(range(8, 0, -1))[:max(0, d-k)] + [0]*max(0, d-k-8))
    for blk in (1, 2, 3, 5, 7):
        s = [(9 if (i//blk) % 2 == 0 else 0) for i in range(d)]; out.append(s)
        s = [(9 if (i//blk) % 2 == 0 else 8) for i in range(d)]; out.append(s)
        s = [((i//blk) % 10) for i in range(d)]; out.append(s)
    # staircase: many distinct gaps
    for k in range(6, d-9):
        out.append([9]*k + [8,7,6,5,4,3,2,1] + [0]*(d-k-8))
    for _ in range(300):
        k = rng.randrange(0, d)
        rest = [rng.randrange(0, 10) for _ in range(d-k)]
        out.append([9]*k + rest)
    for _ in range(300):
        out.append([rng.randrange(0, 10) for _ in range(d)])
    for _ in range(200):  # random multiset with random number of distinct values
        vals = rng.sample(range(10), rng.randrange(2, 11))
        out.append([rng.choice(vals) for _ in range(d)])
    out = [s[:d] + [0]*(d-len(s)) if len(s) < d else s[:d] for s in out]
    return [s for s in out if len(set(s)) > 1]

def run(d, rng):
    ins = structured(d, rng)
    maxsteps = 0; maxR = 0; fails = 0; l2 = 0; l2fail = 0
    bound = (d-1)//5 + 43
    for s in ins:
        img = K(s, d)
        R, t = R_of(img, d)
        maxR = max(maxR, len(R))
        if len(R) > 15:
            print("LEMMA1 FAIL", d, s); fails += 1
        if img != 0 and len(set(digits(img, d))) == 1:
            print("REPDIGIT IMAGE", d, s); fails += 1
        # Lemma 2 on every state of the orbit
        x = digits(img, d)
        for _ in range(d):
            if x.count(9) >= 6 and x.count(9) < d:
                l2 += 1
                if not check_lemma2(x, d): l2fail += 1
                x = digits(K(x, d), d)
            else:
                break
        r = orbit_steps(s, d)
        if not isinstance(r, int):
            print("MAIN FAIL", d, ''.join(map(str, s)), r); fails += 1
        else:
            maxsteps = max(maxsteps, r)
            if r > bound:
                print("BOUND FAIL", d, r, bound); fails += 1
    print(f"d={d} inputs={len(ins)} fails={fails} maxSteps_to_integer={maxsteps} bound={bound} maxR={maxR} lemma2_checks={l2} lemma2_fail={l2fail}", flush=True)

if __name__ == '__main__':
    rng = random.Random(20261125)
    # Lemma 3 spot check: nonzero multiset of image independent of d once a zero is present
    bad = 0
    for _ in range(3000):
        n = rng.randrange(1, 25)
        N = [rng.randrange(1, 10) for _ in range(n)]
        ms = set()
        for d in (max(7, n+1), max(7, n+2), n+13, n+40):
            img = K(N + [0]*(d-n), d)
            ms.add(tuple(sorted(v for v in digits(img, d) if v)))
        if len(ms) != 1: bad += 1
    print("Lemma3 d-independence violations:", bad)
    for d in [int(a) for a in sys.argv[1:]]:
        run(d, rng)
