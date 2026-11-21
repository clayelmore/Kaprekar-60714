#!/usr/bin/env python3
"""Clusters of neighboring surviving rules (2026-11-21). Neighbors: swap the places of two adjacent letters in one word."""
import csv, sys, itertools
from collections import Counter, defaultdict
N=int(sys.argv[1]); fn=sys.argv[2]
rows={(tuple(int(x) for x in r['a'].split(',')),tuple(int(x) for x in r['b'].split(','))):r for r in csv.DictReader(open(fn),delimiter='\t')}
def end(r): return max(r['endpoint'].split('/'),key=len)
par={k:k for k in rows}
def find(x):
    while par[x]!=x: par[x]=par[par[x]]; x=par[x]
    return x
edges=[]
for (a,b) in rows:
    for w in (0,1):
        for i in range(N-1):
            p=[list(a),list(b)]; p[w][i],p[w][i+1]=p[w][i+1],p[w][i]; k=(tuple(p[0]),tuple(p[1]))
            if k in rows and k>(a,b): edges.append(((a,b),k,w,i)); par[find(k)]=find((a,b))
comp=defaultdict(list)
for k in rows: comp[find(k)].append(k)
sizes=Counter(len(v) for v in comp.values())
print(f"N={N}: {len(rows)} survivors, {len(edges)} edges, {len(comp)} clusters; size distribution: {sorted(sizes.items())}")
# what an edge does to the endpoint
rel=Counter(); which=Counter()
for u,v,w,i in edges:
    eu,ev=end(rows[u]),end(rows[v]); L=max(len(eu),len(ev)); eu=eu.zfill(L); ev=ev.zfill(L)
    diff=[j for j in range(L) if eu[j]!=ev[j]]
    if eu==ev: rel['same endpoint']+=1
    elif sorted(eu)==sorted(ev) and len(diff)==2: rel['two digits swapped']+=1
    elif sorted(eu)==sorted(ev): rel[f'same digits, {len(diff)} places differ']+=1
    else: rel['different digit set']+=1
    which[(w,i)]+=1
print(' endpoint relation across an edge:',rel.most_common())
print(' which swap (word, letter pair index):',sorted(which.items()))
L='ABCDEFGH'
def name(a,b):
    A=['']*N;B=['']*N
    for i in range(N): A[N-1-a[i]]=L[i]; B[N-1-b[i]]=L[i]
    return ''.join(A)+'-'+''.join(B)
for root,ks in sorted(comp.items(),key=lambda kv:-len(kv[1]))[:6]:
    ds=Counter(rows[k]['nonzero_digits'] for k in ks); es={end(rows[k]) for k in ks}
    print(f"\n cluster of {len(ks)}: digit sets {ds.most_common(6)}; {len(es)} endpoints; starts {sorted(Counter(rows[k]['works_from'] for k in ks).items())}")
    # invariants inside the cluster: which letters keep their places in every member?
    fa=[i for i in range(N) if len({k[0][i] for k in ks})==1]; fb=[i for i in range(N) if len({k[1][i] for k in ks})==1]
    print('   letters fixed in word 1:',''.join(L[i] for i in fa),' in word 2:',''.join(L[i] for i in fb))
    for k in sorted(ks)[:8]: print('    ',name(*k),end(rows[k]),rows[k]['nonzero_digits'])
