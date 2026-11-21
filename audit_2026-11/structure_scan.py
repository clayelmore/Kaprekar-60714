#!/usr/bin/env python3
"""Which algebraic features separate surviving 6-letter cores from all 190,800?  (2026-11-21)"""
import csv, itertools
from collections import Counter
N=6
def load(f): return {(tuple(int(x) for x in r['a'].split(',')),tuple(int(x) for x in r['b'].split(','))) for r in csv.DictReader(open(f),delimiter='\t')}
S=load('catalog_n6.tsv')
def feats(a,b):
    f={}
    # Kendall distance between the two words = number of letter pairs placed in opposite order
    f['kendall']=sum(1 for i in range(N) for j in range(i+1,N) if (a[i]-a[j])*(b[i]-b[j])<0)
    C=[];s=0;t=[];sg=[]
    for j in range(N-1):
        s+=10**a[j]-10**b[j]; C.append(s); A=set(a[:j+1]);B=set(b[:j+1]); top=max(A^B) if A!=B else -1; t.append(top); sg.append('0' if top<0 else '+' if top in A else '-')
    f['distinct_top']=len(set(t))
    f['top_seq']=tuple(t)
    f['sign_changes']=sum(1 for j in range(N-2) if sg[j]!=sg[j+1])
    f['zero_partial_sums']=sum(1 for c in C if c==0)
    f['minabsC_digits']=min(len(str(abs(c))) if c else 0 for c in C)
    f['maxabsC_digits']=max(len(str(abs(c))) if c else 0 for c in C)
    f['sizes']=tuple(sorted(len(str(abs(c))) if c else 0 for c in C))
    # fixed-letter coincidences: letters whose two places are adjacent
    f['adjacent_places']=sum(1 for i in range(N) if abs(a[i]-b[i])==1)
    f['total_shift']=sum(abs(a[i]-b[i]) for i in range(N))
    f['x_minus_y']=a[N-1]-b[N-1]
    f['x']=a[N-1]; f['y']=b[N-1]
    for i in range(N): f[f'sign_c{i}']=a[i]>b[i]
    return f
keys=None; cs={}; ca={}; n=0
for a in itertools.permutations(range(N)):
    for b in itertools.permutations(range(N)):
        if any(x==y for x,y in zip(a,b)): continue
        f=feats(a,b); n+=1; surv=(a,b) in S
        for k,v in f.items():
            ca.setdefault(k,Counter())[v]+=1
            if surv: cs.setdefault(k,Counter())[v]+=1
print(n,len(S))
for k in ca:
    if k=='top_seq': continue
    print(f"\n{k}:  value  survivors  all  survival-rate(per 1000)")
    for v in sorted(ca[k]):
        print(f"   {str(v):22s} {cs[k][v]:5d} {ca[k][v]:7d}  {1000*cs[k][v]/ca[k][v]:6.2f}")
print("\ntop_seq with highest survival (min 100 cores):")
for v,c in sorted(ca['top_seq'].items(),key=lambda kv:-cs['top_seq'][kv[0]]/kv[1])[:12]:
    if c>=100: print('  ',v,cs['top_seq'][v],c,f"{1000*cs['top_seq'][v]/c:.1f}")
print('top_seq values:',len(ca['top_seq']),' with zero survivors:',sum(1 for v in ca['top_seq'] if cs['top_seq'][v]==0),' cores in zero-survivor classes:',sum(c for v,c in ca['top_seq'].items() if cs['top_seq'][v]==0))
