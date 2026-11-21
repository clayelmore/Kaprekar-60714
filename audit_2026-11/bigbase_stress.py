#!/usr/bin/env python3
"""Stress test of 'all-base' candidate cores at large bases by random sampling (2026-11-21).
For each core, lengths N, N+1, N+2, N+5 and bases 40, 97, 160, 640, 2500: sample starts, iterate; report the
first base/length where some orbit does not reach a fixed point within 4000 steps, or two different endpoints appear."""
import random,sys
from multiprocessing import Pool
from usage_score import coeffs,extend,from_words
BASES=(40,97,160,640,2500); NS=6000
def test(args):
    name,pc=args; N=len(pc); bad=[]; worst=0
    for d in (N,N+1,N+2,N+5):
        e=extend(pc,d)
        for b in BASES:
            random.seed(d*100003+b); c=coeffs(e,b); F=None; fail=None
            for _ in range(NS):
                if random.random()<.5: s=sorted((random.randrange(b) for _ in range(d)),reverse=True)
                else:
                    m=random.randint(2,d); pool=[random.randrange(b) for _ in range(m)]; s=sorted((random.choice(pool) for _ in range(d)),reverse=True)
                if s[0]==s[-1]: continue
                k=0
                while True:
                    v=abs(sum(x*y for x,y in zip(c,s)))
                    if v==0: fail='reaches 0'; break
                    t=sorted(((v//b**i)%b for i in range(d)),reverse=True)
                    if t==s: break
                    s=t; k+=1
                    if k>4000: fail='cycle'; break
                if fail: break
                worst=max(worst,k)
                if F is None: F=v
                elif F!=v: fail='two endpoints'; break
            if fail: bad.append((d,b,fail))
    return name,bad,worst
if __name__=='__main__':
    jobs=[]
    for l in open('bases/all_base_rules.txt'):
        w=l.split('\t')[0]; w1,w2=w.split(' - '); jobs.append(('6:'+w,from_words(w1,w2)))
    for l in open('bases7/survivors_5gap.txt'):
        if l.strip():
            a,bb=l.split(); jobs.append(('7:'+a+' '+bb,list(zip(map(int,a.split(',')),map(int,bb.split(','))))))
    for l in open('bases7/survivors_4gap.txt'):
        if l.strip():
            a,bb=l.split(); jobs.append(('7g4:'+a+' '+bb,list(zip(map(int,a.split(',')),map(int,bb.split(','))))))
    with Pool(6) as p: res=p.map(test,jobs,chunksize=1)
    for fam in ('6:','7:','7g4:'):
        r=[x for x in res if x[0].startswith(fam)]; ok=[x for x in r if not x[1]]
        print(fam,len(r),'rules;',len(ok),'with no failure found')
        for name,bad,worst in r: print('  ',name,'OK max steps %d'%worst if not bad else 'FAILS at (length, base): '+', '.join(f'({d},{b}) {w}' for d,b,w in bad[:4]))
