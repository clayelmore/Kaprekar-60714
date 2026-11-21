#!/usr/bin/env python3
"""Five-letter census, brute force (2026-11-21). For every full-variable 5-letter core (a,b) (5,280 of them),
extend to length d by  a -> a[:4]+[5..d-1]+[a[4]],  b -> b[:4]+[b[4]]+[5..d-1]  and enumerate every length
5..maxd completely with ./kap.  Writes cores5_brute.txt: one line per core with the lengths where a single
nonzero endpoint catches every non-repdigit.  Independent of closure_all5.c."""
import subprocess, sys, itertools
from concurrent.futures import ThreadPoolExecutor
maxd=int(sys.argv[1]) if len(sys.argv)>1 else 12
only=sys.argv[2] if len(sys.argv)>2 else None
cores=[]
if only:
    for l in open(only):
        p=l.split(); cores.append(([int(x) for x in p[1][2:].split(',')],[int(x) for x in p[2][2:].split(',')]))
else:
    for a in itertools.permutations(range(5)):
        for b in itertools.permutations(range(5)):
            if all(x!=y for x,y in zip(a,b)): cores.append((list(a),list(b)))
def check(ab):
    a,b=ab; good={}
    for d in range(5,maxd+1):
        aa=a[:4]+list(range(5,d))+[a[4]]; bb=b[:4]+[b[4]]+list(range(5,d)); c=[10**x-10**y for x,y in zip(aa,bb)]
        o=subprocess.run(['./kap',str(d)]+[str(x) for x in c],capture_output=True,text=True).stdout.split('\n'); nonrep=o[0].split('nonrep=')[1].split()[0]
        full=[l for l in o if f'basin={nonrep} ' in l and 'FIX' in l and 'val=0 ' not in l]
        if full: good[d]=full[0].split('val=')[1].split()[0]
    return a,b,good
with ThreadPoolExecutor(14) as ex: res=list(ex.map(check,cores))
L='ABCDE'
def name(a,b):
    A=['']*5;B=['']*5
    for i in range(5): A[4-a[i]]=L[i]; B[4-b[i]]=L[i]
    return ''.join(A)+' - '+''.join(B)
with open('cores5_brute.txt' if not only else f'cores5_pass_to{maxd}.txt','w') as f:
    for a,b,g in res:
        if g: f.write(f"{name(a,b)}\ta={','.join(map(str,a))}\tb={','.join(map(str,b))}\tuniversal_at={sorted(g)}\tendpoints={sorted(set(g.values()))}\n")
print(len(cores),'cores;',sum(1 for r in res if r[2]),'universal at some length <=',maxd)
for d in range(5,maxd+1):
    u=[r for r in res if d in r[2]]; k=[r for r in u if ''.join(sorted(r[2][d].replace('0','')))=='1467']
    print(f"d={d}: universal {len(u)}; with digits 1,4,6,7: {len(k)}")
tail=[r for r in res if all(d in r[2] for d in range(maxd-3,maxd+1))]
print('universal at each of the last 4 lengths:',len(tail))
for a,b,g in tail: print('  ',name(a,b),'a=',a,'b=',b,'from',min(d for d in g if all(e in g for e in range(d,maxd+1))),'endpoint',g[maxd])
