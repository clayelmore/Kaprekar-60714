#!/usr/bin/env python3
"""How rare is a 146070-style ladder?  Take every universal rule at base length d0 whose fixed point has a zero,
extend it with the same recipe (a' = a[:-1]+[d, a[-1]], b' = b+[d]) one length at a time, and see how long it
stays universal with the SAME fixed integer.  usage: ladder_rarity.py rulesfile maxd"""
import sys, subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
maxd = int(sys.argv[2])
rules = []
for l in open(sys.argv[1]):
    if not l.startswith('UNIV'): continue
    p = dict(x.split('=') for x in l.split()[1:]); rules.append((int(p['F']), [int(x) for x in p['a'].split(',')], [int(x) for x in p['b'].split(',')]))
def universal(F, a, b):
    d = len(a); c = [10**x - 10**y for x, y in zip(a, b)]
    o = subprocess.run(['./kap', str(d)] + [str(x) for x in c], capture_output=True, text=True).stdout.split('\n')
    nonrep = o[0].split('nonrep=')[1].split()[0]
    return any(f'val={F} basin={nonrep} ' in l for l in o)
def climb(r):
    F, a, b = r; d0 = len(a)
    if len(str(F)) == d0 and '0' not in str(F): return (F, d0, None)     # no zero digit: recipe would move the fixed point
    top = d0
    while top < maxd:
        d = len(a); a = a[:-1] + [d, a[-1]]; b = b + [d]
        if not universal(F, a, b): break
        top = d + 1
    return (F, d0, top)
with ThreadPoolExecutor(14) as ex: res = list(ex.map(climb, rules))
elig = [r for r in res if r[2] is not None]
print(f"{len(rules)} universal rules at d={res[0][1]}; {len(elig)} have a zero in the fixed point")
h = Counter(r[2] for r in elig)
for k in sorted(h): print(f"  recipe stays universal through d={k}: {h[k]} rules")
print("  survivors to the cap:", sorted({r[0] for r in elig if r[2] == maxd}))
