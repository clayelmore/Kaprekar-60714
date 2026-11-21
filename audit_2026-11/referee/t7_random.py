from ref import *
random.seed(2026)
def gens(d):
    out=[]
    R=random.randint
    for _ in range(6000):  # random with few symbols
        k=random.choice([2,3,4,6,10]); ds=random.sample(range(10),k); out.append([random.choice(ds) for _ in range(d)])
    for _ in range(3000):  # many 9s
        t=R(d-8,d-1); out.append([9]*t+[R(0,8) for _ in range(d-t)])
    for _ in range(3000):  # many 8s
        t=R(d-8,d-1); out.append([8]*t+[R(0,9) for _ in range(d-t)])
    for _ in range(4000):  # zero-free
        k=random.choice([2,3,5,9]); ds=random.sample(range(1,10),k); out.append([random.choice(ds) for _ in range(d)])
    for _ in range(2000):  # zero-free 9s + 8s (+ few others)
        t=R(1,d-1); u=R(0,min(3,d-t)); out.append([9]*t+[R(1,8) for _ in range(u)]+[8]*(d-t-u))
    for x in range(10):    # near repdigits / two blocks
        for y in range(10):
            if x!=y:
                for cut in (1,2,3,4,5,6,7,d//2,d-7,d-6,d-5,d-2,d-1): out.append([x]*cut+[y]*(d-cut))
    for _ in range(3000):  # long plateaus, 3-4 blocks
        k=R(3,5); cuts=sorted(random.sample(range(1,d),k-1)); ds=sorted(random.sample(range(10),k),reverse=True); s=[];p=0
        for dg,cu in zip(ds,cuts+[d]): s+=[dg]*(cu-p); p=cu
        out.append(s)
    for _ in range(1500):  # staircase with all 9 descents
        cuts=sorted(random.sample(range(1,d),9)); s=[];p=0;g=9
        for cu in cuts+[d]: s+=[g]*(cu-p); p=cu; g-=1
        out.append(s)
    return out
for d in (21,22,30,60):
    tgt=tuple(sorted(map(int,str(146070).zfill(d)),reverse=True)); tests=set(tuple(sorted(s,reverse=True)) for s in gens(d)); n=bad=0; mx=0
    memo={tgt:0}
    for s in tests:
        if len(set(s))==1: continue
        n+=1; path=[]; x=s; ok=True
        while x not in memo:
            if x in path or len(set(x))==1 or len(path)>500: ok=False; break
            path.append(x); x=img(x)
        if not ok: bad+=1; print("FAIL",d,s); continue
        b=memo[x]
        for p in reversed(path): b+=1; memo[p]=b
        mx=max(mx,memo[s])
    print(f"d={d}: distinct non-repdigit states tested={n} failures={bad} max steps={mx} bound d/5+42={d/5+42:.1f}")
