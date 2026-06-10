import itertools, json, time
from collections import Counter

def admissible(d):
    for combo in itertools.combinations_with_replacement(range(10),d):
        cnt=Counter(combo)
        if len(cnt)==1: continue
        if max(cnt.values())>=d-1: continue
        yield tuple(sorted(combo,reverse=True))
def sd(n,d): return tuple(sorted((int(c) for c in str(n).zfill(d)),reverse=True))

V4=lambda t: 9*t[0]-900*t[1]+900*t[2]-9*t[3]
C8=(9*10**4, 9, -900*10**4, -900, 900*10**4, 900, -9*10**4, -9)   # fold2 of 1746
V8=lambda t: sum(C8[i]*t[i] for i in range(8))

out={}
t0=time.time()

# ---------- A. fold4 = c⊗4 at d=16: entry-to-4-coherence ----------
def slices4(s): return [(s[j],s[4+j],s[8+j],s[12+j]) for j in range(4)]
def K4(s): return abs(sum(V4(sl)*10**(4*(3-j)) for j,sl in enumerate(slices4(s))))
def coh4(s):
    sg=[V4(sl) for sl in slices4(s) if V4(sl)!=0]
    return all(x>0 for x in sg) or all(x<0 for x in sg)
mx=0; never=0; n=0
for s in admissible(16):
    n+=1; cur=s; st=0
    while not coh4(cur):
        v=K4(cur)
        if v==0: break
        cur=sd(v,16); st+=1
        if st>80: never+=1; break
    mx=max(mx,st)
out['fold4_entry']={'states':n,'max_entry':mx,'never':never,'sec':round(time.time()-t0)}
print('A done',out['fold4_entry'],flush=True)

# fold4 quotient: factorization + quadruple funnel
t1=time.time(); viol=0; quads=set()
for s in admissible(16):
    if not coh4(s): continue
    vs=[V4(sl) for sl in slices4(s)]
    I=K4(s)
    if I != abs(sum(v*10**(4*(3-j)) for j,v in enumerate(vs))): viol+=1; continue
    md=Counter(str(I).zfill(16)); me=Counter()
    for v in vs: me += Counter(str(abs(v)).zfill(4))
    if md!=me: viol+=1; continue
    quads.add(tuple(abs(v) for v in vs))
def stepq(q):
    I=sum(v*10**(4*(3-j)) for j,v in enumerate(q))
    s2=sd(I,16)
    if sum(s2)==0: return ('ZERO',)
    if not coh4(s2): return ('EXIT',)
    return ('Q', tuple(abs(V4(sl)) for sl in slices4(s2)))
work=set(quads); allq=set(quads); tr={}
while work:
    q=work.pop(); r=stepq(q); tr[q]=r
    if r[0]=='Q' and r[1] not in allq: allq.add(r[1]); work.add(r[1])
good={q for q,r in tr.items() if r[0]=='Q'}
ch=True
while ch:
    ch=False
    drop={q for q in good if tr[q][0]!='Q' or tr[q][1] not in good}
    if drop: good-=drop; ch=True
fixedq=[q for q in good if tr[q][1]==q]
# cycle check
cyc=[]
color={}
for q0 in good:
    if q0 in color: continue
    path=[]; q=q0
    while q not in color:
        color[q]='g'; path.append(q); q=tr[q][1]
        if q not in good: break
    if q in color and color.get(q)=='g' and q in path:
        c=path[path.index(q):]
        if len(c)>1: cyc.append(c)
    for x in path: color[x]='b'
out['fold4_quotient']={'violations':viol,'pairs':len(allq),'good':len(good),
    'fixed':fixedq[:5],'long_cycles':len(cyc),'sec':round(time.time()-t1)}
print('B done',out['fold4_quotient'],flush=True)

# ---------- C. tower element (c8)⊗2 at d=16 ----------
def sup(s): return [(s[0],s[2],s[4],s[6],s[8],s[10],s[12],s[14]),
                    (s[1],s[3],s[5],s[7],s[9],s[11],s[13],s[15])]
def KT(s):
    a,b=sup(s); return abs(V8(a)*10**8 + V8(b))
FP=1746174617461746
print('tower fixes FP?', KT(sd(FP,16))==FP, flush=True)
# universality via orbit-per-state
t2=time.time(); bad=[]; n=0
for s in admissible(16):
    n+=1; cur=s; seen=set()
    while True:
        v=KT(cur)
        if v==FP: break
        cur2=sd(v,16)
        if cur2 in seen or v==0: bad.append((s,v)); break
        seen.add(cur2); cur=cur2
    if len(bad)>20: break
out['tower_universal']={'states':n,'failures':len(bad),'sample_fail':str(bad[:2]),'sec':round(time.time()-t2)}
print('C done',out['tower_universal'],flush=True)

# super-coherence entry + pair quotient for tower
def cohT(s):
    a,b=sup(s); va,vb=V8(a),V8(b)
    sg=[x for x in (va,vb) if x!=0]
    return all(x>0 for x in sg) or all(x<0 for x in sg)
t3=time.time(); mx=0; never=0
for s in admissible(16):
    cur=s; st=0
    while not cohT(cur):
        v=KT(cur)
        if v==0: break
        cur=sd(v,16); st+=1
        if st>80: never+=1; break
    mx=max(mx,st)
out['tower_entry']={'max_entry':mx,'never':never,'sec':round(time.time()-t3)}
print('D done',out['tower_entry'],flush=True)

t4=time.time(); viol=0; pairs=set()
for s in admissible(16):
    if not cohT(s): continue
    a,b=sup(s); va,vb=V8(a),V8(b); I=KT(s)
    if I!=10**8*abs(va)+abs(vb): viol+=1; continue
    if Counter(str(I).zfill(16))!=Counter(str(abs(va)).zfill(8))+Counter(str(abs(vb)).zfill(8)): viol+=1; continue
    pairs.add((abs(va),abs(vb)))
def stepT(p):
    I=10**8*p[0]+p[1]; s2=sd(I,16)
    if sum(s2)==0: return ('ZERO',)
    if not cohT(s2): return ('EXIT',)
    a,b=sup(s2); return ('P',(abs(V8(a)),abs(V8(b))))
work=set(pairs); allp=set(pairs); trT={}
while work:
    p=work.pop(); r=stepT(p); trT[p]=r
    if r[0]=='P' and r[1] not in allp: allp.add(r[1]); work.add(r[1])
goodT={p for p,r in trT.items() if r[0]=='P'}
ch=True
while ch:
    ch=False
    drop={p for p in goodT if trT[p][0]!='P' or trT[p][1] not in goodT}
    if drop: goodT-=drop; ch=True
fixedT=[p for p in goodT if trT[p][1]==p]
cycT=0
color={}
for p0 in goodT:
    if p0 in color: continue
    path=[]; p=p0
    while p not in color:
        color[p]='g'; path.append(p); p=trT[p][1]
        if p not in goodT: break
    if p in color and color.get(p)=='g' and p in path and len(path[path.index(p):])>1: cycT+=1
    for x in path: color[x]='b'
out['tower_quotient']={'violations':viol,'pairs':len(allp),'good':len(goodT),
    'fixed':fixedT[:5],'long_cycles':cycT,'sec':round(time.time()-t4)}
print('E done',out['tower_quotient'],flush=True)

json.dump(out,open('/tmp/kap60714/proofs_runs/tower_d16_results.json','w'),indent=1)
print('ALL DONE', round(time.time()-t0), 'sec total')
