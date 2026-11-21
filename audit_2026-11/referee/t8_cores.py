from ref import *
CORES={'A954':((0,1,2,3,4,5),(5,2,0,4,3,1)),'B954':((0,1,2,4,5,3),(3,2,0,5,4,1)),
       'C98721_ms21_x0':((5,4,1,2,3,0),(3,1,4,5,0,2)),'D743211_x0':((1,2,3,5,4,0),(0,4,2,1,3,5)),'E75321_x1':((2,0,5,4,3,1),(1,4,0,5,2,3))}
for name,(a,b) in CORES.items():
    for d in range(7,13):
        c=coef_core(a,b,d); assert sum(c)==0
        def im(s): 
            v=abs(sum(x*y for x,y in zip(c,s))); return tuple(sorted(map(int,str(v).zfill(d)),reverse=True)),v
        memo={}; terms=Counter(); n=0
        for s in itertools.combinations_with_replacement(range(9,-1,-1),d):
            if len(set(s))==1: assert im(s)[1]==0; continue
            n+=1; path=[]; idx={}; x=s
            while x not in memo and x not in idx:
                idx[x]=len(path); path.append(x); x=im(x)[0]
            if x in memo: t=memo[x]
            else:
                cyc=path[idx[x]:]; t=('FIX',im(cyc[0])[1]) if len(cyc)==1 else ('CYC',len(cyc),min(im(y)[1] for y in cyc))
            for p in path: memo[p]=t
            terms[t]+=1
        top=terms.most_common(3)
        print(name,f"d={d} nonrep={n} terminals={len(terms)}", "UNIVERSAL "+str(top[0][0]) if len(terms)==1 else "NOT universal "+str(top),flush=True)
