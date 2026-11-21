# General-core drain + long-length tests from the raw permutation definition.
from ref import *
random.seed(77)
CORES={'A954_x5':((0,1,2,3,4,5),(5,2,0,4,3,1)),'B954_x3':((0,1,2,4,5,3),(3,2,0,5,4,1)),
       'C98721_ms21_x0':((5,4,1,2,3,0),(3,1,4,5,0,2)),'D743211_x0':((1,2,3,5,4,0),(0,4,2,1,3,5)),'E75321_x1':((2,0,5,4,3,1),(1,4,0,5,2,3)),
       'F146070_x4':((3,5,1,2,0,4),(1,4,5,3,2,0))}
TGT={'A954_x5':(9,5,4),'B954_x3':(9,5,4),'C98721_ms21_x0':(9,8,7,2,1),'D743211_x0':(7,4,3,2,1,1),'E75321_x1':(7,5,3,2,1),'F146070_x4':(7,6,4,1)}
def gens(d):
    out=[]; R=random.randint
    for _ in range(5000):
        k=random.choice([2,3,4,6,10]); ds=random.sample(range(10),k); out.append([random.choice(ds) for _ in range(d)])
    for _ in range(4000):
        t=R(max(6,d-9),d-1); out.append([9]*t+[R(0,8) for _ in range(d-t)])
    for _ in range(4000):  # zero-free with many 9s
        t=R(6,d-1); out.append([9]*t+[R(1,8) for _ in range(d-t)])
    for t in range(1,d):   # zero-free 9^t 8^u, 9^t 0^u, 9^t r^u, and strictly decreasing tails (zero-free images for x=0)
        for r in range(0,9): out.append([9]*t+[r]*(d-t))
    for _ in range(3000):
        u=R(1,8); tail=sorted(random.sample(range(1,9),u),reverse=True); z=R(0,1)
        if d-u-z>=1: out.append([9]*(d-u-z)+tail+[0]*z)
    for _ in range(3000):
        k=random.choice([2,3,5,9]); ds=random.sample(range(1,10),k); out.append([random.choice(ds) for _ in range(d)])
    for x in range(10):
        for y in range(10):
            if x!=y:
                for cut in (1,2,5,6,7,d//2,d-7,d-6,d-2,d-1): out.append([x]*cut+[y]*(d-cut))
    for _ in range(1500):
        cuts=sorted(random.sample(range(1,d),9)); s=[];p=0;g=9
        for cu in cuts+[d]: s+=[g]*(cu-p); p=cu; g-=1
        out.append(s)
    return out
for name,(a,b) in CORES.items():
    x=a[5]
    for d in (21,22,30,60):
        c=coef_core(a,b,d)
        def im(s): return tuple(sorted(map(int,str(abs(sum(p*q for p,q in zip(c,s)))).zfill(d)),reverse=True))
        tgt=tuple(TGT[name])+(0,)*(d-len(TGT[name])); assert im(tgt)==tgt
        memo={tgt:0}; n=bad=0; mx=0; stall=0; inc=0; zf_mid=0; maxnon9=0; zf_lowt=0
        tests=set(tuple(sorted(s,reverse=True)) for s in gens(d))
        for s in tests:
            if len(set(s))==1: continue
            n+=1; path=[]; ps=set(); y=s; ok=True
            while y not in memo:
                if y in ps or len(set(y))==1 or len(path)>2000: ok=False; break
                path.append(y); ps.add(y); y2=im(y)
                t0=y.count(9); t1=y2.count(9)
                maxnon9=max(maxnon9,sum(1 for g in y2 if g not in(0,9)))
                if t0>=6:
                    zf=(0 not in y); m=y[-1]
                    exp=t0-1-x+(1 if (zf and m==8) else 0)
                    assert t1==exp,(name,d,y,y2,exp)
                    if t1==t0: stall+=1
                    if t1>t0: inc+=1
                    if 0 not in y2: zf_mid+=1
                if 0 not in y2 and t1<=5: zf_lowt+=1
                y=y2
            if not ok: bad+=1; print("FAIL",name,d,s); continue
            bb=memo[y]
            for p in reversed(path): bb+=1; memo[p]=bb
            mx=max(mx,memo[s])
        print(f"{name} d={d}: tested={n} failures={bad} maxsteps={mx} | t>=6 steps: stalls={stall} increases={inc} zero-free images={zf_mid} | zero-free images with <=5 nines={zf_lowt} | max non-9 nonzero in any image={maxnon9}",flush=True)
