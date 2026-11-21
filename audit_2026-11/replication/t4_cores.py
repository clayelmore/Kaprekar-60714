"""T4: re-check a sample of cores from all_cores_pass.txt.

Sample: 25 random lines (random.Random(2026).sample), every line with target=954, and three
lines with maxsize=21 (drawn with the same RNG, continuing after the 25). For each core:
 (i)  phi_check (C) with the core and its target  -> seeds failing, max steps, max size
 (ii) brute force K_d for d = 6..11.
"""
import os
import random
import subprocess
import sys
from kd_brute import brute, actual_value
from kap import parse_core

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, '..', 'all_cores_pass.txt')

lines = [l.rstrip('\n') for l in open(DATA) if l.strip()]
rng = random.Random(2026)
pick = rng.sample(range(len(lines)), 25)
t954 = [i for i, l in enumerate(lines) if ' target=954 ' in l + ' ']
ms21 = [i for i, l in enumerate(lines) if ' maxsize=21' in l + ' ']
pick21 = rng.sample(ms21, 3)
chosen = []
for tag, idxs in (('random', pick), ('target954', t954), ('maxsize21', pick21)):
    for i in idxs:
        chosen.append((tag, i))
print(f"total lines={len(lines)} lines with target=954: {len(t954)}, maxsize=21: {len(ms21)}; checking {len(chosen)} (with duplicates across groups if any)")
sys.stdout.flush()

done = {}
for tag, i in chosen:
    line = lines[i]
    a, b, target, fmax = parse_core(line)
    if i in done:
        print(f"[{tag}] line {i+1}: duplicate of earlier check -> {done[i]}")
        continue
    out = subprocess.run([os.path.join(HERE, 'phi_check')] + [str(x) for x in a + b] + [target],
                         capture_output=True, text=True).stdout
    res = [l for l in out.splitlines() if l.startswith('RESULT')][0]
    core_line = [l for l in out.splitlines() if l.startswith('core')][0]
    kv = dict(t.split('=', 1) for t in res.split()[1:])
    fixed = core_line.split('fixed=')[1]
    extra = [l for l in out.splitlines() if l.startswith(('FAIL', 'CYCLE'))]
    # (ii)
    dres = []
    for d in range(6, 12):
        r = brute(a, b, d)
        if r['universal']:
            nz = ''.join(c for c in r['attractor'] if c != '0')
            ok = nz == target
            dres.append(f"{d}:{'Y' if ok else 'U(' + nz + ')'}")
        else:
            nend = len(r['endpoints'])
            ncyc = len(r['cycles'])
            dres.append(f"{d}:N(ends={nend},cyc={ncyc})")
    first_ok = None
    for item in dres:
        d, v = item.split(':')
        if v == 'Y':
            if first_ok is None:
                first_ok = int(d)
        else:
            first_ok = None
    summary = (f"[{tag}] line {i+1}: a={','.join(map(str, a))} b={','.join(map(str, b))} target={target} "
               f"phi_fixed={fixed} seeds={kv['seeds']} fail={kv['fail']} maxsteps={kv['maxsteps']} "
               f"maxsize={kv['maxsize']} (file {fmax}, {'agree' if int(kv['maxsize']) == fmax else 'DIFFER'}) "
               f"maxsize_nonseed={kv['maxsize_nonseed']} | Kd d6..11: {' '.join(dres)} | "
               f"universal-to-target from d={first_ok} through 11")
    file_fields = dict(t.split('=', 1) for t in line.split() if '=' in t and not t.startswith(('a=', 'b=')))
    summary += f" | file: maxsteps={file_fields.get('maxsteps')} states={file_fields.get('states')} vs mine states={kv['states']}"
    done[i] = 'see above'
    print(summary)
    for l in extra[:4]:
        print('     ', l)
    sys.stdout.flush()
