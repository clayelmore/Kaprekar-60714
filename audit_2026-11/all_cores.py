#!/usr/bin/env python3
"""Unbiased census: for EVERY full-variable 6-letter core (ordered pair of place maps a,b; 190,800 of them),
does the reversed-front extension have one universal fixed point at all long lengths?  Writes all_cores_pass.txt"""
import itertools, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
L='ABCDEF'
def letters(a): return ''.join(L[a.index(p)] for p in range(5,-1,-1))
cores=[(a,b) for a in itertools.permutations(range(6)) for b in itertools.permutations(range(6)) if all(x!=y for x,y in zip(a,b))]
def run(ab):
    a,b=ab; c=[10**a[i]-10**b[i] for i in range(5)]
    o=subprocess.run(['./closure_gen']+[str(v) for v in c]+[str(a[5]),str(b[5]),'auto'],capture_output=True,text=True).stdout.strip()
    return (a,b,o)
npass=0; reasons={}
with ThreadPoolExecutor(16) as ex, open('all_cores_pass.txt','w') as out:
    for i,(a,b,o) in enumerate(ex.map(run,cores,chunksize=64)):
        if o.startswith('PASS'):
            npass+=1; out.write(f"{letters(list(a))} - {letters(list(b))}  a={','.join(map(str,a))} b={','.join(map(str,b))}  {o}\n"); out.flush()
        else:
            k=' '.join(o.split()[:2]); reasons[k]=reasons.get(k,0)+1
        if i%20000==0: print(i,npass,flush=True)
print(len(cores),'cores;',npass,'pass;',reasons)
