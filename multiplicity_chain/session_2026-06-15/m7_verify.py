import importlib.util, itertools, random
from collections import Counter
spec=importlib.util.spec_from_file_location("eng","/Users/clayelmore/Downloads/search_multiset_universals_fast.py")
eng=importlib.util.module_from_spec(spec); spec.loader.exec_module(eng)
K_apply=eng.K_apply; sdd=eng.sorted_desc_digits
random.seed(28)
def fold_coeffs(base,k):
    c=[0]*(4*k)
    for i in range(4):
        for j in range(k): c[k*i+j]=base[i]*10**(4*(k-1-j))
    return c
d=28; k=7; ms_sorted=tuple([7]*7+[6]*7+[4]*7+[1]*7)

def outcome(c,F,start,cap=800):
    cur=start; seen=set()
    while cur!=F:
        if cur==0: return 'ZERO'
        if cur in seen: return 'CYCLE'
        seen.add(cur); cur=K_apply(c,sdd(cur,d))
        if len(seen)>cap: return 'CAP'
    return 'FP'

def alphabet():
    out=[]
    for a in range(29):
      for b in range(29-a):
        for cc in range(29-a-b):
          e=28-a-b-cc
          if e<0 or max(a,b,cc,e)==28: continue
          out.append(int(''.join(map(str,sorted([7]*a+[6]*b+[4]*cc+[1]*e,reverse=True)))))
    return out
alpha=alphabet()

for name,base in [('6174',[999,90,-90,-999]),('2538',[90,999,-999,-90])]:
    c=fold_coeffs(base,k); F=K_apply(c,ms_sorted)
    print(f"\n=== {name} 7-fold ===  fixed point F={F}")
    # nature of alphabet exceptions
    fails=[n for n in alpha if outcome(c,F,n)!='FP']
    oc=Counter(outcome(c,F,n) for n in fails)
    print(f"  alphabet: {len(alpha)-len(fails)}/{len(alpha)} reach F; exceptions {dict(oc)}")
    for n in fails[:12]:
        print(f"    exception {n}  ->  {outcome(c,F,n)}  multiset={dict(Counter(str(n).zfill(28)))}")
    # large general sample
    G=200000; zero=cyc=cap=fp=0
    for _ in range(G):
        combo=tuple(sorted((random.randint(0,9) for _ in range(d)),reverse=True))
        cnt=Counter(combo)
        if len(cnt)==1 or max(cnt.values())>=d-1: continue
        o=outcome(c,F,int(''.join(map(str,combo))))
        if o=='FP': fp+=1
        elif o=='ZERO': zero+=1
        elif o=='CYCLE': cyc+=1
        else: cap+=1
    print(f"  general sample (~{G}): FP={fp}  ->0(escape)={zero}  CYCLE={cyc}  CAP={cap}")
