#!/usr/bin/env python3
"""Audit 2026-11: the 60714 zero-padding ladder, complete classification at each length.
Claim under test: every non-repdigit multiset reaches 60714 or 0 (escape class)."""
import subprocess, sys, itertools
def ladder(d):
    c = [9900,9,90,-9000,-999] if d%2 else [9900,9,90,-9000,99000,-99999]
    while len(c) < d:
        n=len(c)+2; c += [9*10**(n-2), -9*10**(n-2)]
    return c
for d in range(5, int(sys.argv[1])+1):
    c = ladder(d); assert sum(c)==0
    out = subprocess.run(['./kap',str(d)]+[str(x) for x in c],capture_output=True,text=True).stdout.strip().split('\n')
    print(out[0], '|', ' ; '.join(l.strip() for l in out[1:]), flush=True)
