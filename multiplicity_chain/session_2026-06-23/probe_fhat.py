"""Monovariant probe on the return-map quotient T-hat (levels 1-2) + worst-case witnesses."""
import sys
from collections import Counter
sys.path.insert(0, '/private/tmp/claude-501/-Users-clayelmore/df4b77c2-f992-4441-8ad2-9f25785ac0ca/scratchpad/tower')
from tower_lib import *

c1 = tower_c(1); c2 = tower_c(2)

def That_level(j_top):
    d0 = 4*2**(j_top-1); L = 2*d0
    c = tower_c(j_top); csub = tower_c(j_top-1)
    pairs = set()
    for s in all_sorted(L):
        if len(set(s)) == 1: continue
        e, o = slices(s)
        A, B = V(csub, e), V(csub, o)
        if A*B >= 0: pairs.add((abs(A), abs(B)))
    T = {}
    for (pA, pB) in pairs:
        s = sdesc_val(pA*10**d0 + pB, L)
        for _ in range(12):
            if len(set(s)) == 1: break
            e, o = slices(s)
            A, B = V(csub, e), V(csub, o)
            if A*B >= 0:
                T[(pA, pB)] = (abs(A), abs(B)); break
            s = K_step(c, s, L)
    return T, d0

for j_top, Fv in [(1, 1746), (2, 17461746)]:
    T, d0 = That_level(j_top)
    target = Counter()
    for ch in str(Fv)*2: target[int(ch)] += 1
    def msdist(pA, pB):
        m = Counter()
        for v in (pA, pB):
            for ch in str(v).zfill(d0): m[int(ch)] += 1
        return sum((m-target).values()) + sum((target-m).values())
    cands = {
        "|A-F|+|B-F|":          lambda a, b: abs(a-Fv)+abs(b-Fv),
        "max|.-F|":             lambda a, b: max(abs(a-Fv), abs(b-Fv)),
        "multiset dist to F^2": lambda a, b: msdist(a, b),
        "|A-B|+|A+B-2F|":       lambda a, b: abs(a-b)+abs(a+b-2*Fv),
    }
    print(f"level {j_top}: T-hat nodes {len(T):,}")
    for name, phi in cands.items():
        viol = sum(1 for p, q in T.items() if p != (Fv, Fv) and phi(*q) >= phi(*p))
        print(f"   monovariant {name:24s}: violations {viol:,}")

print("\nworst-entry witnesses (level 1, entry=2 abstract images):")
for P in range(1, 10):
    for Q in range(1, 10):
        for R in range(Q, 10):
            Kv = 9*P*10**4 - 9*(100*Q - R)
            s = sdesc_val(Kv, 8)
            st = None; cur = s
            for k in range(6):
                e, o = slices(cur)
                if V(tower_c(0), e)*V(tower_c(0), o) >= 0:
                    st = k; break
                cur = K_step(c1, cur, 8)
            if st == 2:
                print(f"  typeA (P,Q,R)=({P},{Q},{R}): K={Kv} digits {s} -> needs 2 more steps")
