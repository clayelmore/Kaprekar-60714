"""Complete enumeration at d = 22 = 2N+14 for three N=4 cores with a_i != b_i for every i, where
sampling showed every non-repdigit ending in one common cycle of period > 1."""
import json
from brute import stage2
for a,b in [((0,1,2,3),(3,2,1,0)), ((1,2,0,3),(3,0,1,2)), ((1,0,2,3),(3,2,0,1))]:
    r = stage2(a,b,22); r.update(a=a,b=b,d=22)
    print(json.dumps(r, default=list), flush=True)
