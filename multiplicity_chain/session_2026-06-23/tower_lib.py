"""Shared library: the 1746 dyadic tower."""
from itertools import combinations_with_replacement as cwr

def tower_c(j):
    """Coefficient vector of the level-j tower element ((c^x2)^x2)... at d=4*2^j."""
    c = [9, -900, 900, -9]
    d = 4
    for _ in range(j):
        # 2-fold: rank 2i+t gets c_i * 10^{d*(1-t)}
        c = [c[i]*10**(d*(1-t)) for i in range(len(c)) for t in (0,1)]
        d *= 2
    return c

def V(c, s):
    """Signed linear form on sorted tuple s."""
    return sum(ci*si for ci, si in zip(c, s))

def sdesc_val(v, d):
    """Sorted-descending digit tuple of integer v padded to d digits."""
    g = [int(ch) for ch in str(v)]
    g = [0]*(d-len(g)) + g
    return tuple(sorted(g, reverse=True))

def K_step(c, s, d):
    return sdesc_val(abs(V(c, s)), d)

def sign(v):
    return (v > 0) - (v < 0)

def sign_rule(s, j):
    """Claimed sign of V_j on sorted s: <0 iff s[2^j]>s[2^(j+1)]; 0 iff repdigit; else >0."""
    if len(set(s)) == 1:
        return 0
    return -1 if s[1 << j] > s[1 << (j+1)] else +1

def slices(s):
    return s[0::2], s[1::2]

def coherent(s, j_top):
    """Top coherence at level j_top (state length 4*2^j_top): nonzero slice values of
    V_{j_top-1} on even/odd slices share a sign."""
    c_sub = tower_c(j_top - 1)
    e, o = slices(s)
    a, b = V(c_sub, e), V(c_sub, o)
    return a * b >= 0

def all_sorted(d):
    return cwr(range(9, -1, -1), d)
