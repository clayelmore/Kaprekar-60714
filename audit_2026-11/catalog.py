#!/usr/bin/env python3
"""Catalog of every core that passes the all-lengths check (census_out/n<N>_*.txt, written by censusN.c).
For each one, enumerate every length N..max(2N+8, M) completely with ./kap (the all-lengths argument covers
d >= max(2N+9, M+1)), and record the lengths where a single nonzero endpoint catches every non-repdigit.
usage: catalog.py N [N ...]      writes catalog_n<N>.tsv"""
import subprocess, sys, glob, os
TOP=int(os.environ.get('TOP','0')); SUF=os.environ.get('SUF','')
from concurrent.futures import ThreadPoolExecutor
L='ABCDEFGHIJ'
def name(a,b):
    n=len(a); A=['']*n; B=['']*n
    for i in range(n): A[n-1-a[i]]=L[i]; B[n-1-b[i]]=L[i]
    return ''.join(A)+' - '+''.join(B)
def coeffs(a,b,d):
    n=len(a)
    if d==n: aa,bb=a,b
    else: aa=a[:n-1]+list(range(n,d))+[a[n-1]]; bb=b[:n-1]+[b[n-1]]+list(range(n,d))
    return [10**x-10**y for x,y in zip(aa,bb)]
def check(row):
    a,b,tgt,ms,st,flagA=row; n=len(a); top=TOP or max(2*n+8,ms); good={}
    for d in range(n,top+1):
        o=subprocess.run(['./kap',str(d)]+[str(x) for x in coeffs(a,b,d)],capture_output=True,text=True).stdout.split('\n')
        nonrep=o[0].split('nonrep=')[1].split()[0]
        full=[l for l in o if f'basin={nonrep} ' in l and 'FIX' in l and 'val=0 ' not in l]
        if full: good[d]=(full[0].split('val=')[1].split()[0], int(full[0].split('maxsteps=')[1]))
    start=top+1
    while start-1 in good: start-=1
    ends=sorted({v[0] for d,v in good.items() if d>=start})
    return dict(name=name(a,b),a=a,b=b,target=tgt,start=start,top=top,endpoints=ends,
                steps=max([v[1] for d,v in good.items() if d>=start] or [0]),core_steps=st,maxsize=ms,
                early=sorted(d for d in good if d<start),A=flagA)
for N in sys.argv[1:]:
    rows=[]
    for fn in sorted(glob.glob(f'census_out/n{N}_*.txt')):
        for l in open(fn):
            if not l.startswith('CORE') or ' B=1 ' not in l: continue
            p=l.split(); a=[int(x) for x in p[2][2:].split(',')]; b=[int(x) for x in p[3][2:].split(',')]
            rows.append((a,b,p[7].split('=')[1],int(p[9].split('=')[1]),int(p[8].split('=')[1]),p[4]))
    with ThreadPoolExecutor(16) as ex: res=list(ex.map(check,rows))
    with open(f'catalog_n{N}{SUF}.tsv','w') as f:
        f.write('rule\ta\tb\tnonzero_digits\tendpoint\tworks_from\tenumerated_to\tmax_steps\tearlier_lengths\tok\n')
        for r in sorted(res,key=lambda r:(len(r['target']),r['target'],r['name'])):
            ok=(r['start']<=r['top'] and len(r['endpoints'])==1)
            f.write('\t'.join(map(str,[r['name'],','.join(map(str,r['a'])),','.join(map(str,r['b'])),r['target'],'/'.join(r['endpoints']),r['start'],r['top'],r['steps'],r['early'],int(ok)]))+'\n')
    bad=[r for r in res if not(r['start']<=r['top'] and len(r['endpoints'])==1)]
    print(f"N={N}: {len(res)} cores pass the all-lengths check; {len({r['target'] for r in res})} digit sets; {len({e for r in res for e in r['endpoints']})} endpoints; not confirmed by enumeration: {len(bad)}")
    from collections import Counter
    print('   works from length:',sorted(Counter(r['start'] for r in res).items()))
