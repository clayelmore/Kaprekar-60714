"""Full one-step T_18 closure check for the Section-4 even ladder (E.2 at its threshold).
Every admissible d=18 multiset must map into T_18 (sorted form ending in two zeros) in ONE step."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tower_lib import V, sdesc_val
from itertools import combinations_with_replacement as cwr
from collections import Counter

def ladder_c(d):
    if d%2: c=[9900,9,90,-9000,-999]; L=5
    else:   c=[9900,9,90,-9000,99000,-99999]; L=6
    while L<d: L+=2; c += [9*10**(L-2), -9*10**(L-2)]
    return c

c = ladder_c(18); n=0; viol=0
for s in cwr(range(9,-1,-1), 18):
    cnt = Counter(s)
    if len(cnt)==1: continue
    if any(v==17 for v in cnt.values()): continue
    n += 1
    out = sdesc_val(abs(V(c,s)), 18)
    if out[16]!=0 or out[17]!=0: viol += 1
print(f"admissible d=18 multisets: {n:,}   one-step T_18 violations: {viol}")
