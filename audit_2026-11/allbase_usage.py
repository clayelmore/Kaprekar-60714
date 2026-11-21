#!/usr/bin/env python3
"""Score every all-base rule found so far with usage_score.py (2026-11-21)."""
import glob,re,collections,sys
from usage_score import score,coeffs,from_words
def gaps_only(pc):
    out=[]
    for b in (7,10,13):
        c=coeffs(pc,b); s=0; C=[]
        for x in c[:-1]: s+=x; C.append(s)
        out.append(len({abs(x) for x in C if x}))
    return min(out)
rules=[]   # (family, name, places)
for l in open('bases/all_base_rules.txt'):
    w=l.split('\t')[0]; w1,w2=w.split(' - '); rules.append(('six-letter core',w,from_words(w1,w2)))
def allbase(pattern,key):
    d=collections.defaultdict(set); fs=glob.glob(pattern)
    for f in fs:
        b=re.search(r'_b(\d+)_',f).group(1)
        for l in open(f):
            if l.startswith('UNIV'):
                p=dict(x.split('=') for x in l.split()[1:]); d[key(p)].add(b)
    return [k for k,v in d.items() if len(v)==len(fs)]
for n in (3,4):
    for k in allbase(f'halfswap/out_b*_n{n}.txt',lambda p:p['pairs']):
        prs=k.split(','); pc=[None]*(2*n)
        for i,pr in enumerate(prs):
            q=n-1-i; P,M=ord(pr[0])-65,ord(pr[2])-65; pc[P]=(q+n,q); pc[M]=(q,q+n)
        rules.append((f'half-swap L={2*n}',k,pc))
n=3
for k in allbase('midfix/out_b*_n3.txt',lambda p:(p['pairs'],p['Q'])):
    prs=k[0].split(','); pc=[None]*7; pc[ord(k[1])-65]=(n,n)
    for i,pr in enumerate(prs):
        q=n-1-i; P,M=ord(pr[0])-65,ord(pr[2])-65; pc[P]=(q+n+1,q); pc[M]=(q,q+n+1)
    rules.append(('fixed-middle L=7',k[0]+' Q='+k[1],pc))
for k in allbase('oddswap/out_b*_n3.txt',lambda p:p['rule']):
    parts=k.split(','); X,Y,Z=(ord(ch)-65 for ch in parts[0]); pc=[None]*7; pc[X]=(2*n,n); pc[Y]=(n,0); pc[Z]=(0,2*n)
    for i,pr in enumerate(parts[1:]):
        q=n-1-i; P,M=ord(pr[0])-65,ord(pr[2])-65; pc[P]=(q+n,q); pc[M]=(q,q+n)
    rules.append(('rotation L=7',k,pc))
print(len(rules),'all-base rules',collections.Counter(r[0] for r in rules),file=sys.stderr)
hist=collections.defaultdict(collections.Counter); full=[]
for fam,name,pc in rules:
    g=gaps_only(pc); hist[fam][g]+=1
    if g==len(pc)-1: full.append((fam,name,pc))
for fam in hist: print(fam,'gaps seen -> count:',dict(sorted(hist[fam].items())))
print('rules seeing every gap:',len(full))
print("family\trule\tgaps\tkept\tmean\tmax\trich\tdistinct\tendpoint_b10\t|\tkept_b7\tmean_b7\trich_b7")
rows=[]
for fam,name,pc in rules:
    g=gaps_only(pc)
    if g<len(pc)-2: continue
    r=score(coeffs(pc,10),10); r7=score(coeffs(pc,7),7)
    if r is None or r7 is None: print(fam,name,'NOT UNIVERSAL?',r is None,r7 is None); continue
    rows.append((g,r['kept'],fam,name,r,r7))
for g,_,fam,name,r,r7 in sorted(rows,key=lambda t:(-t[0]/ (t[4]['L']-1),-t[1])):
    print(f"{fam}\t{name}\t{g}/{r['L']-1}\t{r['kept']:.2f}\t{r['mean']:.1f}\t{r['max']}\t{r['rich']}/{r['L']}\t{r['distinct']}\t{r['F']}\t|\t{r7['kept']:.2f}\t{r7['mean']:.1f}\t{r7['rich']}/{r7['L']}")
