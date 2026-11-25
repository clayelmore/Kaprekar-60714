"""Complete five-digit check of the rule ADCBE - DEACB (absolute value), written 2026-11-25.
Independent of the June code. Sort the five digits descending as A>=B>=C>=D>=E (leading zeros kept),
form the numbers ADCBE and DEACB, take the absolute difference, pad back to five digits, repeat.
Checks every string 00000..99999, with no exclusions, and reports where each one ends."""
from collections import Counter

def step(n):
    A, B, C, D, E = sorted((int(ch) for ch in f"{n:05d}"), reverse=True)
    x = 10000*A + 1000*D + 100*C + 10*B + E
    y = 10000*D + 1000*E + 100*A + 10*C + B
    return abs(x - y)

# the same map by the June coefficient vector, as a cross-check of the letter form
def step_coeff(n):
    A, B, C, D, E = sorted((int(ch) for ch in f"{n:05d}"), reverse=True)
    return abs(9900*A + 9*B + 90*C - 9000*D - 999*E)

assert all(step(n) == step_coeff(n) for n in range(100000))
assert all(0 <= step(n) <= 99999 for n in range(100000))

end, steps = {}, {}
for n in range(100000):
    seen, m, k = [], n, 0
    while m not in seen:
        seen.append(m); m = step(m); k += 1
    cyc = tuple(sorted(seen[seen.index(m):]))   # the cycle reached
    end[n] = cyc
    steps[n] = seen.index(m)

by_end = Counter(end.values())
print("terminal cycles over all 100000 five-digit strings:")
for cyc, cnt in by_end.most_common():
    print("  ", cyc, cnt)
rep = [n for n in range(100000) if len(set(f"{n:05d}")) == 1]
bad = [n for n in range(100000) if end[n] != (60714,)]
print("repdigits:", len(rep), " not reaching 60714:", len(bad), " same set:", sorted(bad) == sorted(rep))
good = [n for n in range(100000) if end[n] == (60714,)]
print("fixed points:", [n for n in range(100000) if step(n) == n])
mx = max(steps[n] for n in good)
print("max steps to 60714:", mx, "e.g.", [n for n in good if steps[n] == mx][:5])
print("step histogram:", sorted(Counter(steps[n] for n in good).items()))
real = [n for n in range(10000, 100000)]
print("true five-digit integers 10000-99999:", len(real),
      "reach 60714:", sum(end[n] == (60714,) for n in real),
      "do not:", [n for n in real if end[n] != (60714,)])
for n in (12345, 99998, 10000, 54321):
    path, m = [n], n
    while m != 60714:
        m = step(m); path.append(m)
    print(n, "->", " -> ".join(f"{p:05d}" for p in path[1:]))
