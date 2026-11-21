#!/usr/bin/env python3
"""Audit 2026-11: pictures of how digit multisets flow to 146070 under the escape-free ladder.
Writes tree_146070_d6.svg (every 6-digit multiset, radial tree) and steps_profile.svg."""
import subprocess, math, itertools, sys
def rule(d):
    a=[3,5,1,2,0]+list(range(6,d))+[4]; b=[1,4,5,3,2,0]+list(range(6,d)); return [10**x-10**y for x,y in zip(a,b)]
# ---------- radial tree at d=6 ----------
d=6; c=rule(d)
def step(s): return tuple(sorted(str(abs(sum(ci*int(x) for ci,x in zip(c,s)))).zfill(d),reverse=True))
states=[tuple(str(x) for x in t) for t in itertools.combinations_with_replacement('9876543210',d) if len(set(t))>1]
F=tuple(sorted('146070',reverse=True)); par={s:step(s) for s in states if s!=F}
kids={}
for s,p in par.items(): kids.setdefault(p,[]).append(s)
size={}; depth={F:0}
order=[F]
for s in order:
    for k in kids.get(s,[]): depth[k]=depth[s]+1; order.append(k)
assert len(order)==len(states), (len(order),len(states))
for s in reversed(order): size[s]=1+sum(size[k] for k in kids.get(s,[]))
ang={}; leafn=sum(1 for s in states if s not in kids); cnt=[0]
def lay(s):
    stack=[(s,0)]
    while stack:
        n,i=stack.pop(); ks=sorted(kids.get(n,[]),key=lambda k:-size[k])
        if not ks: ang[n]=2*math.pi*cnt[0]/leafn; cnt[0]+=1; continue
        if i<len(ks): stack.append((n,i+1)); stack.append((ks[i],0))
        else: ang[n]=sum(ang[k] for k in ks)/len(ks)
lay(F)
D=max(depth.values()); R=470; W=1000
def xy(s): r=R*depth[s]/D; return W/2+r*math.cos(ang[s]), W/2+r*math.sin(ang[s])
def col(t):  # depth ramp: deep blue (near root) -> teal -> amber (far)
    stops=[(0,(30,58,138)),(0.5,(13,148,136)),(1,(217,119,6))]
    for (t0,c0),(t1,c1) in zip(stops,stops[1:]):
        if t<=t1: u=(t-t0)/(t1-t0); return '#%02x%02x%02x'%tuple(round(c0[i]+u*(c1[i]-c0[i])) for i in range(3))
out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {W+60}" font-family="Helvetica,Arial,sans-serif"><rect width="100%" height="100%" fill="#ffffff"/>']
for s in sorted(par,key=lambda s:-depth[s]):
    x1,y1=xy(s); x2,y2=xy(par[s]); w=0.35+1.6*math.log10(size[s])
    out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col(depth[s]/D)}" stroke-width="{w:.2f}" stroke-linecap="round" opacity="0.85"/>')
out.append(f'<circle cx="{W/2}" cy="{W/2}" r="7" fill="#111827"/><text x="{W/2+12}" y="{W/2-10}" font-size="20" font-weight="bold" fill="#111827">146070</text>')
out.append(f'<text x="20" y="{W+25}" font-size="18" fill="#111827">Every 6-digit digit-multiset ({len(states):,} of them) flowing into 146070. Distance from center = steps remaining (max {D}).</text>')
out.append(f'<text x="20" y="{W+48}" font-size="15" fill="#4b5563">Line thickness = how many multisets pass through that link. Color: blue near the endpoint, amber far away.</text></svg>')
open('tree_146070_d6.svg','w').write('\n'.join(out))
print('tree: nodes',len(states),'max depth',D,'children of root',len(kids[F]),'biggest branch sizes',sorted((size[k] for k in kids[F]),reverse=True)[:6])
# ---------- step profiles ----------
ds=[int(x) for x in sys.argv[1:]] or [6,8,12,16,20]
prof={}
for dd in ds:
    o=subprocess.run(['./kaph',str(dd)]+[str(x) for x in rule(dd)],capture_output=True,text=True).stdout.strip().split('\n')[-1]
    h={int(k):int(v) for k,v in (p.split(':') for p in o.split()[1:])}; tot=sum(h.values()); prof[dd]=[h.get(i,0)/tot for i in range(42)]
    print(dd,'mean steps %.2f'%sum(i*p for i,p in enumerate(prof[dd])),'mode',max(range(42),key=lambda i:prof[dd][i]))
W,H,L,B=1000,560,70,60; ymax=max(max(p) for p in prof.values())*1.08
cols=['#1e3a8a','#0d9488','#d97706','#be185d','#4b5563','#7c3aed']
o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica,Arial,sans-serif"><rect width="100%" height="100%" fill="#ffffff"/>']
X=lambda i:L+(W-L-30)*i/41; Y=lambda v:H-B-(H-B-40)*v/ymax
for i in range(0,42,5): o.append(f'<line x1="{X(i):.0f}" y1="{H-B}" x2="{X(i):.0f}" y2="{H-B+6}" stroke="#111827"/><text x="{X(i):.0f}" y="{H-B+24}" font-size="14" text-anchor="middle" fill="#111827">{i}</text>')
for k in range(0,int(ymax*100)+1,2):
    v=k/100; o.append(f'<line x1="{L}" y1="{Y(v):.0f}" x2="{W-30}" y2="{Y(v):.0f}" stroke="#e5e7eb"/><text x="{L-8}" y="{Y(v)+5:.0f}" font-size="14" text-anchor="end" fill="#111827">{k}%</text>')
for n,(dd,p) in enumerate(prof.items()):
    pts=' '.join(f'{X(i):.1f},{Y(v):.1f}' for i,v in enumerate(p)); o.append(f'<polyline points="{pts}" fill="none" stroke="{cols[n]}" stroke-width="2.5"/>')
    o.append(f'<line x1="{W-200}" y1="{60+24*n}" x2="{W-170}" y2="{60+24*n}" stroke="{cols[n]}" stroke-width="3"/><text x="{W-162}" y="{65+24*n}" font-size="15" fill="#111827">{dd} digits</text>')
o.append(f'<text x="{L}" y="26" font-size="18" font-weight="bold" fill="#111827">Steps needed to reach 146070, by number length</text>')
o.append(f'<text x="{(L+W-30)/2:.0f}" y="{H-10}" font-size="15" text-anchor="middle" fill="#111827">steps to reach 146070</text><text x="18" y="{H/2:.0f}" font-size="15" fill="#111827" transform="rotate(-90 18 {H/2:.0f})" text-anchor="middle">share of digit multisets</text></svg>')
open('steps_profile.svg','w').write('\n'.join(o))
