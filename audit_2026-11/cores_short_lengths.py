#!/usr/bin/env python3
"""For every core that passed the all-lengths check, enumerate lengths 6..20 completely (./kap) and record at
which of those lengths the extended rule is universal for the same fixed point.  Reads all_cores_pass.txt."""
import subprocess, sys
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
maxd=int(sys.argv[1]) if len(sys.argv)>1 else 20
rows=[]
for l in open('all_cores_pass.txt'):
    p=l.split(); a=[int(x) for x in p[3][2:].split(',')]; b=[int(x) for x in p[4][2:].split(',')]; tgt=p[6].split('=')[1]; ms=int(l.split('maxsize=')[1]); st=int(l.split('maxsteps=')[1].split()[0])
    rows.append((p[0]+' - '+p[2],a,b,tgt,ms,st))
def value(a,b,tgt):
    f=[int(x) for x in tgt]+[0]*(6-len(tgt)) if len(tgt)<=6 else None
    return None if f is None else abs(sum((10**a[i]-10**b[i])*f[i] for i in range(6)))
def check(r):
    name,a,b,tgt,ms,st=r; good=[]; F=None
    for d in range(6,maxd+1):
        aa=a[:5]+list(range(6,d))+[a[5]]; bb=b[:5]+[b[5]]+list(range(6,d)); c=[10**x-10**y for x,y in zip(aa,bb)]
        o=subprocess.run(['./kap',str(d)]+[str(x) for x in c],capture_output=True,text=True).stdout.split('\n'); nonrep=o[0].split('nonrep=')[1].split()[0]
        full=[l for l in o if f'basin={nonrep} ' in l and 'FIX' in l]
        if full: good.append(d); F=full[0].split('val=')[1].split()[0]
    return (name,tgt,ms,st,good,F)
with ThreadPoolExecutor(14) as ex: res=list(ex.map(check,rows))
fam=defaultdict(list)
for r in res: fam[r[1]].append(r)
print(f"{len(res)} cores pass the all-lengths check; {len(fam)} digit families")
for tgt,rs in sorted(fam.items(),key=lambda kv:-len(kv[1])):
    allok=[r for r in rs if r[4]==list(range(7,maxd+1)) or r[4]==list(range(6,maxd+1))]
    print(f"\nfamily {tgt}+zeros: {len(rs)} cores; universal at every length 7..{maxd}: {len(allok)}; max nonzero digits visited {max(r[2] for r in rs)}; endpoints: {len({r[5] for r in rs})}")
    for r in sorted(rs,key=lambda r:(r[5] or '',r[0]))[:6]:
        miss=[d for d in range(6,maxd+1) if d not in r[4]]
        print(f"   {r[0]}  endpoint {r[5]}  core steps<= {r[3]}  fails at lengths {miss if miss else 'none'}")
with open('all_cores_summary.txt','w') as f:
    for r in res: f.write(f"{r[0]}\ttarget={r[1]}\tendpoint={r[5]}\tmaxsize={r[2]}\tmaxsteps={r[3]}\tuniversal_at={r[4]}\n")
