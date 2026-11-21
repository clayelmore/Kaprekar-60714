"""Brute force K_d over all digit multisets of length d for a core.

brute(a, b, d) returns a dict:
  fixed_points  : all fixed points (as d-digit strings)
  cycles        : list of cycles of period >= 2 (lists of d-digit strings)
  endpoints     : Counter of terminal attractor (fixed point string, or 'cycle:...') over non-repdigits
  universal     : True if every non-repdigit reaches one single fixed point
  attractor     : that fixed point (string) if universal
  maxsteps      : max number of K_d applications needed by a non-repdigit to reach its fixed point
"""
import sys
from collections import Counter
from kap import make_K, all_multisets, check_core


def brute(a, b, d):
    check_core(a, b)
    K, _ = make_K(a, b, d)
    nxt = {}
    for s in all_multisets(d):
        nxt[s] = K(s)
    # resolve each state: (attractor, steps)
    res = {}
    for s0 in nxt:
        if s0 in res:
            continue
        path = []
        onpath = {}
        s = s0
        while s not in res and s not in onpath:
            onpath[s] = len(path)
            path.append(s)
            s = nxt[s]
        if s in res:
            att, st = res[s]
            for x in reversed(path):
                st += 1
                res[x] = (att, st)
        else:
            i = onpath[s]
            cyc = path[i:]
            if len(cyc) == 1:
                att = ('fp', ''.join(map(str, cyc[0])))
            else:
                att = ('cycle', tuple(''.join(map(str, c)) for c in cyc))
            for x in cyc:
                res[x] = (att, 0)
            st = 0
            for x in reversed(path[:i]):
                st += 1
                res[x] = (att, st)
    fps = sorted(''.join(map(str, s)) for s in nxt if nxt[s] == s)
    cycles = sorted({att[1] for (att, _) in res.values() if att[0] == 'cycle'})
    ends = Counter()
    maxsteps = 0
    for s, (att, st) in res.items():
        if len(set(s)) == 1:
            continue
        ends[att] += 1
        maxsteps = max(maxsteps, st)
    universal = len(ends) == 1 and next(iter(ends))[0] == 'fp'
    out = dict(fixed_points=fps, cycles=cycles, endpoints=ends, universal=universal,
               attractor=next(iter(ends))[1] if universal else None, maxsteps=maxsteps,
               nstates=len(nxt))
    return out


def actual_value(a, b, d, sorted_digits_str):
    """The fixed point as a number string: K_d applied to its multiset (a fixed point's value)."""
    K, Kv = make_K(a, b, d)
    return str(Kv([int(c) for c in sorted_digits_str])).zfill(d)


if __name__ == '__main__':
    a = (3, 5, 1, 2, 0, 4)
    b = (1, 4, 5, 3, 2, 0)
    for d in range(6, 14):
        r = brute(a, b, d)
        fpvals = [actual_value(a, b, d, f) for f in r['fixed_points']]
        att = r['attractor']
        attval = actual_value(a, b, d, att) if att else None
        print(f"d={d} states={r['nstates']} universal={r['universal']} attractor_multiset={att} "
              f"attractor_value={attval} maxsteps={r['maxsteps']} fixed_point_values={fpvals} "
              f"ncycles={len(r['cycles'])} endpoints={dict((str(k)[:80], v) for k, v in r['endpoints'].items()) if not r['universal'] else ''}")
        sys.stdout.flush()
