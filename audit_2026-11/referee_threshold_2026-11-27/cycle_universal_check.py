"""Complete enumeration for rules where sampling showed one common cycle of period > 1.
Tests the literal wording of 'universal' (one F != 0 reached by every non-repdigit) vs the intended one."""
import json, sys
from brute import stage2
cases = [((0,1,2),(2,1,0),20), ((0,1,2),(2,1,0),21), ((0,1),(1,0),2), ((0,1,2),(2,0,1),17), ((1,0,2),(2,1,0),17)]
for a,b,d in cases:
    r = stage2(a,b,d)
    r.update(a=a,b=b,d=d)
    print(json.dumps(r, default=list), flush=True)
