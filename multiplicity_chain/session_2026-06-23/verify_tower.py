"""Reproduces every computation behind Lemma 6.9, Proposition 6.10, Theorem 6.11's
verification (Computed 6.12), and the level-3 evidence, for paper_hierarchy.md.
Runtime: ~1 minute. Requires tower_lib.py alongside."""
import sys, os, random, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tower_lib import *

def check(name, ok):
    print(("PASS  " if ok else "FAIL  ") + name)
    if not ok: sys.exit(1)

# --- Lemma 6.9(a): sign rule, complete at levels 0-2 ---
for j, dj in [(0,4),(1,8),(2,16)]:
    c = tower_c(j)
    bad = sum(1 for s in all_sorted(dj)
              if ((V(c,s)>0)-(V(c,s)<0)) != sign_rule(s,j))
    check(f"sign lemma level {j} (complete, d={dj})", bad==0)

# --- Lemma 6.9(b): plateau characterization, complete at levels 1-2 ---
def plateau(s, jt):
    a, b = 1<<jt, 1<<(jt+1)
    e, o = slices(s)
    return ((s[a]==s[b] and s[a+1]>s[b+1] and len(set(e))>1) or
            (s[a]> s[b] and s[a+1]==s[b+1] and len(set(o))>1))
for jt, L in [(1,8),(2,16)]:
    bad = sum(1 for s in all_sorted(L) if (not coherent(s,jt)) != plateau(s,jt))
    check(f"plateau characterization level {jt} (complete, d={L})", bad==0)

# --- Proposition 6.10: abstract gap families, levels 1 and 2 ---
def entry(s, jt, cap=10):
    c = tower_c(jt); L = len(s)
    for k in range(cap+1):
        if len(set(s))==1: return None      # repdigit met: forbidden
        if coherent(s,jt): return k
        s = K_step(c, s, L)
    return None

worst=0; ok=True
for P in range(1,10):
    for Q in range(1,10):
        for R in range(Q,10):
            for Kv in (9*P*10**4 - 9*(100*Q-R), 9*(100*Q-R)*10**4 - 9*P):
                st = entry(sdesc_val(Kv,8), 1)
                ok &= st is not None; worst = max(worst, 99 if st is None else st)
check(f"(E) level 1: 810 abstract images enter coherence, no repdigits (max +{worst})", ok and worst<=2)

t0=time.time(); worst=0; ok=True; n=0
for e0 in range(10):
    for e1 in range(10):
        for e2 in range(0,e1+1):
            Aval = 9*e0*10**4 + 9*e1 - 900*e2
            if Aval<=0: continue
            for f0 in range(10):
                for f1 in range(1,f0+1):
                    lead = 9*f0-900*f1
                    for f2 in range(10):
                        for f3 in range(0,f2+1):
                            Bval = 10**4*lead + 9*f2 - 900*f3
                            if Bval>=0: continue
                            for Kv in (10**8*Aval + Bval, 10**8*(-Bval) - Aval):
                                st = entry(sdesc_val(Kv,16), 2)
                                ok &= st is not None; worst = max(worst, 99 if st is None else st); n+=1
check(f"(E) level 2: {n:,} abstract images enter coherence, no repdigits (max +{worst}) [{time.time()-t0:.0f}s]", ok and worst<=2)

# --- Computed 6.12: return-map funnel, complete at levels 1-2 ---
for jt, Fv in [(1,1746),(2,17461746)]:
    d0 = 4*2**(jt-1); L=2*d0
    c = tower_c(jt); csub = tower_c(jt-1)
    pairs=set()
    for s in all_sorted(L):
        if len(set(s))==1: continue
        e,o=slices(s); A,B=V(csub,e),V(csub,o)
        if A*B>=0: pairs.add((abs(A),abs(B)))
    T={}; exc=0
    work=set(pairs)
    while work:
        pA,pB = work.pop()
        s = sdesc_val(pA*10**d0+pB, L); r=None
        for _ in range(12):
            if len(set(s))==1: exc+=1; break
            e,o=slices(s); A,B=V(csub,e),V(csub,o)
            if A*B>=0: r=(abs(A),abs(B)); break
            s = K_step(c,s,L)
        if r is None: exc+=1; continue
        T[(pA,pB)]=r
        if r not in T and r not in pairs: pairs.add(r); work.add(r)
    fixed=[p for p,q in T.items() if p==q]
    color={}; cyc=0
    for st0 in T:
        path=[]; p=st0
        while p in T and color.get(p,0)==0:
            color[p]=1; path.append(p); p=T[p]
        if p in T and color.get(p)==1 and p in path and len(path[path.index(p):])>1: cyc+=1
        for q in path: color[q]=2
    check(f"(F-hat) level {jt}: T-hat total on {len(T):,} pairs, 0 exceptions, "
          f"unique fixed pair ({Fv},{Fv}), acyclic", exc==0 and fixed==[(Fv,Fv)] and cyc==0)

# --- level-3 evidence: constructed plateau states, entry <= 3 ---
random.seed(1746); c3=tower_c(3); c2s=tower_c(2)
worst=0; ok=True
for i in range(20000):
    if i%2==0:
        v=random.randint(1,9)
        s=tuple(sorted([random.randint(v,9) for _ in range(8)]+[v]*9+[random.randint(0,v-1) for _ in range(15)],reverse=True))
    else:
        v=random.randint(0,8)
        s=tuple(sorted([random.randint(v+1,9) for _ in range(9)]+[v]*9+[random.randint(0,v) for _ in range(14)],reverse=True))
    if len(set(s))==1: continue
    e,o=slices(s)
    if V(c2s,e)*V(c2s,o)>=0: continue
    st=entry(s,3,cap=12)
    ok &= st is not None; worst = max(worst, 99 if st is None else st)
check(f"level-3 evidence: constructed incoherent d=32 states enter within {worst} steps", ok and worst<=3)
print("\nALL CHECKS PASS")
