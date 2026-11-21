#!/usr/bin/env python3
"""Builds catalog.html (phone page) from catalog_n5.tsv, catalog_n6.tsv and catalog_n7*.tsv.
usage: build_catalog_page.py <n7 tsv> <text describing how far the 7-letter enumeration went>"""
import sys, json, csv
from collections import defaultdict, Counter
n7file=sys.argv[1]; n7note=sys.argv[2]
def load(fn):
    return list(csv.DictReader(open(fn),delimiter='\t'))
def key7(a,b):
    a=[int(x) for x in a.split(',')]; b=[int(x) for x in b.split(',')]; n=len(a)
    if n<7: a,b=a[:n-1]+list(range(n,7))+[a[n-1]], b[:n-1]+[b[n-1]]+list(range(n,7))
    return (tuple(a),tuple(b))
rules={}; sizes={5:load('catalog_n5.tsv'),6:load('catalog_n6.tsv'),7:load(n7file)}
tot={}; conf={}; starts={}
for N in (5,6,7):
    rows=sizes[N]; tot[N]=len(rows); conf[N]=sum(1 for r in rows if int(r['works_from'])<=int(r['enumerated_to'])); starts[N]=Counter(int(r['works_from']) for r in rows if int(r['works_from'])<=int(r['enumerated_to']))
    for r in rows:
        k=key7(r['a'],r['b'])
        if k in rules: continue          # already known from a smaller size
        rules[k]=dict(n=N,name=r['rule'],dig=r['nonzero_digits'],end=max(r['endpoint'].split('/'),key=len),start=int(r['works_from']),ok=int(r['works_from'])<=int(r['enumerated_to']),steps=int(r['max_steps']))
new=Counter(v['n'] for v in rules.values())
sets=defaultdict(list)
for v in rules.values(): sets[v['dig']].append(v)
S=[]
for dig,rs in sets.items():
    rs.sort(key=lambda r:(r['n'],r['start'],int(r['end'].split('/')[0])))
    S.append(dict(d=dig,k=len(dig),c=len(rs),n=min(r['n'] for r in rs),s0=min(r['start'] for r in rs),s1=max(r['start'] for r in rs),
                  e=len({r['end'] for r in rs}),r=[[r['name'],r['end'],r['start'],r['n']] for r in rs]))
S.sort(key=lambda s:(s['k'],-s['c'],s['d']))
bycount=Counter();
for s in S: bycount[s['k']]+=1
rulesby=Counter()
for s in S: rulesby[s['k']]+=s['c']
unconf=sum(1 for v in rules.values() if not v['ok'])
print('rules',len(rules),'sets',len(S),'new by size',dict(new),'unconfirmed',unconf,'starts',{n:sorted(c.items()) for n,c in starts.items()})
def rng(c):
    ks=sorted(c); return f"{ks[0]}" if len(ks)==1 else f"{ks[0]}–{ks[-1]}"
small=[s for s in S if s['k']<=4]
def bars(data,label,unit):
    mx=max(v for _,v in data); out=[]
    for k,v in data:
        out.append(f'<div class="bar" title="{k} {label}: {v:,} {unit}"><span class="bl">{k}</span><span class="bt"><span class="bf" style="width:{max(v/mx*100,0.6):.1f}%"></span></span><span class="bv">{v:,}</span></div>')
    return '\n'.join(out)
html=f'''<title>Kaprekar Endpoint Catalog</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
/* layout: one reading column; a ledger of digit sets that opens into its rules; digits set in mono */
:root{{--bg:#f7f8f6;--surface:#ffffff;--fg:#17201c;--muted:#5a665f;--line:#d9dfda;--accent:#0b6b57;--accent-soft:#e2f1ec;--warn:#9a5b00;--warn-soft:#fbf0dc;
  --display:"Space Grotesk",system-ui,sans-serif;--body:"Inter",system-ui,sans-serif;--mono:"JetBrains Mono",ui-monospace,Menlo,monospace}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#111614;--surface:#19201d;--fg:#e8eeea;--muted:#9aa8a0;--line:#2b3531;--accent:#5fd0b3;--accent-soft:#17332c;--warn:#f0b65a;--warn-soft:#33280f;color-scheme:dark}}}}
:root[data-theme="dark"]{{--bg:#111614;--surface:#19201d;--fg:#e8eeea;--muted:#9aa8a0;--line:#2b3531;--accent:#5fd0b3;--accent-soft:#17332c;--warn:#f0b65a;--warn-soft:#33280f;color-scheme:dark}}
body{{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:16px;line-height:1.55}}
.wrap{{max-width:760px;margin:0 auto;padding-block:28px 56px;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));display:flex;flex-direction:column;gap:30px}}
h1{{font-family:var(--display);font-size:1.9rem;line-height:1.15;margin:0;text-wrap:balance}}
h2{{font-family:var(--display);font-size:1.2rem;margin:0 0 10px;text-wrap:balance}}
p{{margin:0 0 10px}}p:last-child{{margin-bottom:0}}
.sub{{color:var(--muted);margin-top:8px}}.note{{color:var(--muted);font-size:.9rem}}
.mono,td.n{{font-family:var(--mono);font-variant-numeric:tabular-nums}}
.scroll{{overflow-x:auto}}
table{{border-collapse:collapse;width:100%;font-size:.93rem}}
th,td{{text-align:left;padding:7px 12px 7px 0;border-bottom:1px solid var(--line);vertical-align:top}}
th{{font-weight:600;color:var(--muted);font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap}}
td.n{{white-space:nowrap}}
.bar{{display:grid;grid-template-columns:2.2em 1fr 4.2em;align-items:center;gap:10px;padding:3px 0}}
.bl{{font-family:var(--mono);color:var(--muted);text-align:right}}.bv{{font-family:var(--mono);font-variant-numeric:tabular-nums;font-size:.9rem}}
.bt{{display:block;height:14px;min-width:0}}.bf{{display:block;height:100%;background:var(--accent);border-radius:0 4px 4px 0}}
.bar:hover .bf{{opacity:.75}}
.cap{{font-size:.8rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;font-weight:600;margin-bottom:6px}}
.ctl{{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:12px}}
input,select{{font:inherit;color:var(--fg);background:var(--surface);border:1px solid var(--line);border-radius:8px;padding:8px 10px;min-width:0}}
input{{flex:1 1 180px}}input:focus,select:focus,button:focus-visible{{outline:2px solid var(--accent);outline-offset:1px}}
.set{{border-bottom:1px solid var(--line)}}
.set>button{{all:unset;box-sizing:border-box;cursor:pointer;display:grid;grid-template-columns:minmax(0,1fr) auto;gap:4px 14px;width:100%;padding:10px 0}}
.set .d{{font-family:var(--mono);font-weight:600;letter-spacing:.12em;overflow-wrap:anywhere}}
.set .m{{color:var(--muted);font-size:.86rem;grid-column:1/-1}}
.set .c{{font-family:var(--mono);color:var(--accent);font-variant-numeric:tabular-nums}}
.set .rules{{padding:0 0 12px}}
.more{{all:unset;cursor:pointer;color:var(--accent);font-weight:600;font-size:.9rem;padding:8px 0}}
.star{{background:var(--accent-soft);color:var(--accent);font-size:.72rem;font-weight:600;padding:2px 8px;border-radius:999px;margin-left:8px;letter-spacing:.04em;font-family:var(--body)}}
</style>
<div class="wrap">
<header>
  <h1>Kaprekar Endpoint Catalog</h1>
  <p class="sub">Every digit-rearranging rule of 3 to 7 letters that, under one fixed extension recipe, sends every number to a single endpoint from a minimum length onward. Compiled November 21, 2026.</p>
</header>

<section>
  <h2>By rule size</h2>
  <div class="scroll"><table>
    <tr><th>Letters</th><th>Rules tested</th><th>Universal</th><th>New at this size</th><th>Begin at length</th><th>Enumerated</th></tr>
    <tr><td class="n">3</td><td class="n">12</td><td class="n">0</td><td class="n">0</td><td class="n">n/a</td><td>length 9</td></tr>
    <tr><td class="n">4</td><td class="n">216</td><td class="n">0</td><td class="n">0</td><td class="n">n/a</td><td>length 10</td></tr>
    <tr><td class="n">5</td><td class="n">5,280</td><td class="n">{tot[5]}</td><td class="n">{new[5]}</td><td class="n">{rng(starts[5])}</td><td>all 17 through length 20</td></tr>
    <tr><td class="n">6</td><td class="n">190,800</td><td class="n">{tot[6]}</td><td class="n">{new[6]:,}</td><td class="n">{rng(starts[6])}</td><td>all 551 through length 20 (21 where needed)</td></tr>
    <tr><td class="n">7</td><td class="n">9,344,160</td><td class="n">{tot[7]:,}</td><td class="n">{new[7]:,}</td><td class="n">{rng(starts[7])}</td><td>{n7note}</td></tr>
  </table></div>
  <p class="note" style="margin-top:10px">Six letters: 551 rules are universal from a minimum length onward; 75 begin at length 6, and the others begin at lengths 7–10. A rule that works at one size reappears at the next size up (its own extension is a rule of that size), so "new at this size" counts only rules not already found smaller. In total: <strong>{len(rules):,} distinct rules on {len(S)} digit sets.</strong></p>
  <p class="note">"Universal" here means: one nonzero endpoint catches every number that is not a repdigit. Each row's lengths come from complete enumeration. Every length beyond that rests on the all-lengths check, which is written out and reviewed only for 146070.</p>
</section>

<section>
  <h2>How many nonzero digits the endpoints have</h2>
  <div class="cap">Digit sets, by number of nonzero digits</div>
  {bars(sorted(bycount.items()),'nonzero digits','digit sets')}
  <div class="cap" style="margin-top:16px">Rules, by number of nonzero digits</div>
  {bars(sorted(rulesby.items()),'nonzero digits','rules')}
</section>

<section>
  <h2>The smallest digit sets</h2>
  <p>All sets with four or fewer nonzero digits. The endpoint is these digits plus zeros.</p>
  <div class="scroll"><table>
    <tr><th>Nonzero digits</th><th>Rules</th><th>Smallest rule</th><th>Begin at</th><th>Endpoints</th></tr>
    {''.join(f'<tr><td class="n">{" ".join(s["d"])}</td><td class="n">{s["c"]:,}</td><td class="n">{s["n"]} letters</td><td class="n">{s["s0"] if s["s0"]==s["s1"] else str(s["s0"])+"–"+str(s["s1"])}</td><td class="n" style="white-space:normal">{", ".join(sorted({r[1] for r in s["r"]},key=lambda x:int(x.split("/")[0]))[:6])}{" …" if s["e"]>6 else ""}</td></tr>' for s in small)}
  </table></div>
</section>

<section>
  <h2>Every digit set</h2>
  <div class="ctl">
    <input id="q" type="search" inputmode="numeric" placeholder="Search digits or endpoint, e.g. 7641 or 146070" aria-label="Search digits or endpoint">
    <select id="sort" aria-label="Sort"><option value="k">Fewest digits first</option><option value="c">Most rules first</option><option value="n">Smallest rule size first</option></select>
  </div>
  <p class="note" id="count"></p>
  <div id="list"></div>
</section>
</div>
<script>
const S={json.dumps(S,separators=(',',':'))};
const list=document.getElementById('list'),q=document.getElementById('q'),sortSel=document.getElementById('sort'),count=document.getElementById('count');
const FAMOUS={{'7641':"6174's digits",'954':"495's digits",'9981':"10989's digits"}};
function rulesTable(s,limit){{
  const rows=s.r.slice(0,limit).map(r=>`<tr><td class="n">${{r[0]}}</td><td class="n">${{r[1]}}</td><td class="n">${{r[2]}}</td><td class="n">${{r[3]}}</td></tr>`).join('');
  return `<div class="scroll"><table><tr><th>Rule</th><th>Endpoint</th><th>Begins at length</th><th>Letters</th></tr>${{rows}}</table></div>`+(s.r.length>limit?`<button class="more" data-more="${{s.d}}">Show all ${{s.r.length.toLocaleString()}} rules</button>`:'');
}}
function render(){{
  const t=q.value.replace(/[^0-9]/g,''); const key=t.split('').sort().reverse().join('').replace(/0/g,'');
  let v=S.filter(s=>!t||s.d===key||s.d.includes(t)||s.r.some(r=>r[1]===t));
  const m=sortSel.value; v=[...v].sort((a,b)=>m==='c'?b.c-a.c:m==='n'?(a.n-b.n||a.k-b.k):(a.k-b.k||b.c-a.c));
  count.textContent=v.length+' of '+S.length+' digit sets'+(v.length>150?' (showing first 150; search to narrow)':'');
  list.innerHTML=v.slice(0,150).map(s=>`<div class="set"><button aria-expanded="false" data-d="${{s.d}}"><span class="d">${{s.d.split('').join(' ')}}${{FAMOUS[s.d]?`<span class="star">${{FAMOUS[s.d]}}</span>`:''}}</span><span class="c">${{s.c.toLocaleString()}} rule${{s.c>1?'s':''}}</span><span class="m">${{s.e.toLocaleString()}} endpoint${{s.e>1?'s':''}} · smallest rule ${{s.n}} letters · begins at length ${{s.s0===s.s1?s.s0:s.s0+'–'+s.s1}}</span></button><div class="rules" hidden></div></div>`).join('')||'<p class="note">No digit set matches.</p>';
}}
list.addEventListener('click',e=>{{
  const more=e.target.closest('[data-more]'); if(more){{const s=S.find(x=>x.d===more.dataset.more); more.parentElement.innerHTML=rulesTable(s,1e9); return;}}
  const b=e.target.closest('button[data-d]'); if(!b) return; const box=b.nextElementSibling; const open=box.hidden;
  if(open&&!box.innerHTML) box.innerHTML=rulesTable(S.find(x=>x.d===b.dataset.d),40);
  box.hidden=!open; b.setAttribute('aria-expanded',open);
}});
q.addEventListener('input',render); sortSel.addEventListener('change',render); render();
</script>
'''
open('catalog.html','w').write(html); print(len(html)//1024,'KB')
