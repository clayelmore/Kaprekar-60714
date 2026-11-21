#!/usr/bin/env python3
"""Audit 2026-11: candidate escape-free ladder for 146070 (zero-padding direction).
Places: a = (3,5,1,2,0,6,7,...,d-1,4), b = (1,4,5,3,2,0,6,...,d-1)."""
import subprocess, sys
def rule(d, variant=0):
    a=[3,5,1,2,0]+list(range(6,d))+[4]; b=[1,4,5,3,2,0]+list(range(6,d))
    return [10**x-10**y for x,y in zip(a,b)]
for d in range(6,int(sys.argv[1])+1):
    c=rule(d); assert sum(c)==0
    o=subprocess.run(['./kap',str(d)]+[str(x) for x in c],capture_output=True,text=True).stdout.strip().split('\n')
    nonrep=int(o[0].split('nonrep=')[1].split()[0]); rest=' ; '.join(l.strip() for l in o[1:] if 'basin=0 ' not in l)
    print(f"d={d} nonrep={nonrep} | {rest}", flush=True)
print("coefficients at d=10:", rule(10))
