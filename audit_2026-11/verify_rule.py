#!/usr/bin/env python3
"""Verify 'UNIV ... F=.. a=.. b=..' lines with the independent engine ./kap (first line of each file given)."""
import sys, subprocess
for fn in sys.argv[1:]:
    line = next(l for l in open(fn) if l.startswith('UNIV'))
    p = dict(x.split('=') for x in line.split()[2:]); a=[int(x) for x in p['a'].split(',')]; b=[int(x) for x in p['b'].split(',')]
    c=[10**x-10**y for x,y in zip(a,b)]; d=len(c)
    o=subprocess.run(['./kap',str(d)]+[str(x) for x in c],capture_output=True,text=True).stdout.strip().split('\n')
    nonrep=o[0].split('nonrep=')[1].split()[0]
    fl=[l for l in o if f"val={p['F']} " in l][0]
    print(f"d={d} F={p['F'].zfill(d)} basin={fl.split('basin=')[1].split()[0]} of {nonrep} non-repdigit multisets; terminals: {len(o)-1} (incl. 0)  c={c}")
