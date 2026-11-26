from rules_check import run
for b in list(range(3, 14)) + [16]:
    r = run("AFEJBGIDHC", "GIDHCAFEJB", b)
    print(b, r[0], r[1] if r[0]=="PASS" else r[1], flush=True)
