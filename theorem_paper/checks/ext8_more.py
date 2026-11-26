from rules_check import run
import sys
for b in range(17, 50):
    r = run("GFEABDHC", "HGDFCEAB", b)
    print(b, r[0], r[1], flush=True)
