#!/usr/bin/env python3
"""Collapse shapes of 60714 (paper's ladder) and 146070 at length d: full functional graph on digit multisets.
Prints funnel numbers (distinct states left after k steps) and writes shapes_d<d>.svg."""
import itertools, math, sys
from collections import Counter
d = int(sys.argv[1]) if len(sys.argv) > 1 else 8
def lad60714(d):
    c = [9900,9,90,-9000,-999] if d % 2 else [9900,9,90,-9000,99000,-99999]
    while len(c) < d: n = len(c)+2; c += [9*10**(n-2), -9*10**(n-2)]
    return c
def r146070(d):
    a=[3,5,1,2,0]+list(range(6,d))+[4]; b=[1,4,5,3,2,0]+list(range(6,d)); return [10**x-10**y for x,y in zip(a,b)]
def graph(c):
    states=[t for t in itertools.combinations_with_replacement(range(9,-1,-1),d)]
    nxt={}
    for s in states:
        v=abs(sum(ci*si for ci,si in zip(c,s))); nxt[s]=tuple(sorted((int(x) for x in str(v).zfill(d)),reverse=True))
    return states,nxt
def analyze(name,c,F):
    states,nxt=graph(c); Fm=tuple(sorted((int(x) for x in str(F).zfill(d)),reverse=True)); Z=(0,)*d
    start=[s for s in states if len(set(s))>1]
    img=set(start); funnel=[len(img)]
    for _ in range(80):
        img={nxt[s] for s in img}; funnel.append(len(img))
        if len(img)<=2 and all(nxt[s]==s for s in img): break
    def end(s):
        seen=set()
        while nxt[s]!=s and s not in seen: seen.add(s); s=nxt[s]
        return s
    ends=Counter(end(s) for s in start)
    print(f"{name} d={d}: {len(start)} starting multisets; endpoints {[(''.join(map(str,k)),v) for k,v in ends.items()]}")
    print(f"   funnel (distinct states left after k steps): {funnel}")
    return states,nxt,Fm,Z,start
# ---------- drawing ----------
def tree_svg(states,nxt,roots,start,ox,oy,R,title,sub,out,orange=False):
    kids={}; par={}
    for s in start:
        par[s]=nxt[s]
    allnodes=set(start)|set(roots)|{nxt[s] for s in start}
    for s in allnodes:
        if s in roots: continue
        p=nxt[s]; kids.setdefault(p,[]).append(s)
    depth={}; order=[]
    for r in roots:
        depth[r]=0; order.append(r)
    i=0
    while i<len(order):
        s=order[i]; i+=1
        for k in kids.get(s,[]):
            if k in roots: continue
            depth[k]=depth[s]+1; order.append(k)
    size={}
    for s in reversed(order): size[s]=1+sum(size[k] for k in kids.get(s,[]) if k not in roots)
    leaves=[s for s in order if not [k for k in kids.get(s,[]) if k not in roots]]
    ang={}; cnt=[0]; total=len(leaves)
    # root sectors proportional to basin size, laid out by DFS
    def lay(n):
        stack=[(n,0)]
        while stack:
            m,j=stack.pop(); ks=sorted([k for k in kids.get(m,[]) if k not in roots],key=lambda k:-size[k])
            if not ks: ang[m]=2*math.pi*cnt[0]/total; cnt[0]+=1; continue
            if j<len(ks): stack.append((m,j+1)); stack.append((ks[j],0))
            else: ang[m]=sum(ang[k] for k in ks)/len(ks)
    for r in roots: lay(r)
    D=max(depth.values())
    centers={}
    def xy(s):
        r=R*depth[s]/D; return ox+r*math.cos(ang[s]), oy+r*math.sin(ang[s])
    def col(s,t):
        root=s
        while root not in roots: root=nxt[root]
        if orange: return '#c2410c'
        stops=[(0,(30,58,138)),(0.5,(13,148,136)),(1,(150,170,60))]
        for (t0,c0),(t1,c1) in zip(stops,stops[1:]):
            if t<=t1: u=(t-t0)/(t1-t0); return '#%02x%02x%02x'%tuple(round(c0[k]+u*(c1[k]-c0[k])) for k in range(3))
    for s in sorted([s for s in order if s not in roots],key=lambda s:-depth[s]):
        x1,y1=xy(s); x2,y2=xy(nxt[s]); w=0.3+1.4*math.log10(size[s])
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col(s,depth[s]/D)}" stroke-width="{w:.2f}" stroke-linecap="round" opacity="0.85"/>')
    for r in roots:
        x,y=xy(r); fc='#c2410c' if orange else '#111827'; out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{fc}"/>')
    out.append(f'<text x="{ox}" y="{oy-R-38}" font-size="22" font-weight="bold" text-anchor="middle" fill="#111827">{title}</text>')
    out.append(f'<text x="{ox}" y="{oy-R-14}" font-size="15" text-anchor="middle" fill="#4b5563">{sub}</text>')
    return D
s1,n1,F1,Z1,st1=analyze('60714',lad60714(d),60714)
s2,n2,F2,Z2,st2=analyze('146070',r146070(d),146070)
def endpoint(n,s):
    for _ in range(200): s=n[s]
    return s
good1=[s for s in st1 if endpoint(n1,s)==F1]; bad1=[s for s in st1 if endpoint(n1,s)==Z1]; lost=len(bad1)
W,H,R=1400,800,280
out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif"><rect width="100%" height="100%" fill="#ffffff"/>']
D1=tree_svg(s1,n1,[F1],good1,330,400,R,'60714',f'{len(good1):,} reach 60714 · {lost} collapse to 0 (orange, lower left)',out)
if bad1:
    tree_svg(s1,n1,[Z1],bad1,90,650,70,'','',out,orange=True)
    out.append(f'<text x="90" y="740" font-size="14" text-anchor="middle" fill="#c2410c">0</text>')
D2=tree_svg(s2,n2,[F2],st2,1050,400,R,'146070',f'all {len(st2):,} reach 146070 · none collapse',out)
out.append(f'<text x="20" y="{H-36}" font-size="16" fill="#111827">Every {d}-digit digit combination (repdigits left out), drawn as a tree flowing into its endpoint. Distance from a root = steps remaining.</text>')
out.append(f'<text x="20" y="{H-14}" font-size="14" fill="#4b5563">Line thickness = how many combinations pass through that link. 60714 longest path: {D1} steps. 146070 longest path: {D2} steps.</text></svg>')
open(f'shapes_d{d}.svg','w').write('\n'.join(out)); print('lost',lost,'depths',D1,D2)

f1=[]; f2=[]
for nm,st,n,F,lst in (('60714',st1,n1,F1,f1),('146070',st2,n2,F2,f2)):
    img=set(st)
    while True:
        lst.append(len(img))
        if len(img)<=2 and all(n[x]==x for x in img): break
        img={n[x] for x in img}
W,H,L,B=1000,520,80,60; K=max(len(f1),len(f2))-1
X=lambda i:L+(W-L-40)*i/K; Y=lambda v:H-B-(H-B-50)*math.log10(v)/math.log10(f1[0])
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif"><rect width="100%" height="100%" fill="#ffffff"/>']
for v in (1,10,100,1000,10000,100000,1000000):
    if v<=f1[0]: o.append(f'<line x1="{L}" y1="{Y(v):.0f}" x2="{W-40}" y2="{Y(v):.0f}" stroke="#e5e7eb"/><text x="{L-8}" y="{Y(v)+5:.0f}" font-size="14" text-anchor="end" fill="#111827">{v:,}</text>')
for i in range(0,K+1,5): o.append(f'<text x="{X(i):.0f}" y="{H-B+22}" font-size="14" text-anchor="middle" fill="#111827">{i}</text>')
for lst,colr,lab,yy in ((f1,'#1e3a8a','60714 (two endpoints: 60714 and 0)',70),(f2,'#0d9488','146070',94)):
    o.append('<polyline points="'+' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in enumerate(lst))+f'" fill="none" stroke="{colr}" stroke-width="3"/>')
    o.append(f'<line x1="{W-360}" y1="{yy}" x2="{W-330}" y2="{yy}" stroke="{colr}" stroke-width="3"/><text x="{W-322}" y="{yy+5}" font-size="15" fill="#111827">{lab}</text>')
o.append(f'<text x="{L}" y="28" font-size="18" font-weight="bold" fill="#111827">How fast {d}-digit numbers merge (log scale)</text>')
o.append(f'<text x="{(L+W-40)/2:.0f}" y="{H-12}" font-size="15" text-anchor="middle" fill="#111827">steps taken</text><text x="20" y="{(H-B)/2:.0f}" font-size="15" text-anchor="middle" fill="#111827" transform="rotate(-90 20 {(H-B)/2:.0f})">different numbers still in play</text></svg>')
open(f'funnel_d{d}.svg','w').write('\n'.join(o))
