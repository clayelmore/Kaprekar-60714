#!/usr/bin/env python3
"""Seven-letter cores that pass both tests (A and B) in bases 4, 5, 7 and 10; gaps seen (2026-11-21)."""
import glob,collections
from usage_score import score,coeffs
def load(pat):
    s={}
    for f in glob.glob(pat):
        for l in open(f):
            if l.startswith('CORE') and ' A=1 B=1 ' in l:
                p=l.split(); s[(p[2][2:],p[3][2:])]=l
    return s
S={b:load(pat) for b,pat in ((4,'bases/b4_n7_*.txt'),(5,'bases/b5_n7_*.txt'),(7,'bases/b7_n7_*.txt'),(10,'census_out/n7_*.txt'))}
for b in S: print('base',b,len(S[b]))
common=set(S[4])&set(S[5])&set(S[7])&set(S[10]); print('in all four:',len(common))
def gaps(pc):
    out=[]
    for b in (7,10,13):
        c=coeffs(pc,b); s=0; C=[]
        for x in c[:-1]: s+=x; C.append(s)
        out.append(len({abs(x) for x in C if x}))
    return min(out)
hist=collections.Counter(); rows=[]
for a,bb in common:
    pc=list(zip(map(int,a.split(',')),map(int,bb.split(',')))); g=gaps(pc); hist[g]+=1
    if g>=6: rows.append((a,bb,pc))
print('gaps seen (of 6) -> rules:',dict(sorted(hist.items())))
print("a\tb\tkept10\tmean10\tmax10\trich10\tdistinct10\tend10\tkept7\tmean7\tend7(dec)")
out=[]
for a,bb,pc in rows:
    r=score(coeffs(pc,10),10); r7=score(coeffs(pc,7),7)
    if r and r7: out.append((r['kept'],a,bb,r,r7))
    else: print(a,bb,'not universal at length 7 itself',bool(r),bool(r7))
for k,a,bb,r,r7 in sorted(out,reverse=True):
    print(f"{a}\t{bb}\t{r['kept']:.2f}\t{r['mean']:.1f}\t{r['max']}\t{r['rich']}/7\t{r['distinct']}\t{r['F']}\t{r7['kept']:.2f}\t{r7['mean']:.1f}\t{r7['F']}")
