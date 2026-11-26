"""Independent check of rules printed in letters (referee frame check)."""
import itertools, sys
def coeffs(w1, w2, b):
    L = len(w1); c = [0]*L
    for i, ch in enumerate(w1): c[ord(ch)-65] += b**(L-1-i)
    for i, ch in enumerate(w2): c[ord(ch)-65] -= b**(L-1-i)
    assert sorted(w1) == sorted(w2) == [chr(65+i) for i in range(L)]
    return c
def run(w1, w2, b, want=None):
    L = len(w1); c = coeffs(w1, w2, b)
    def step(s):
        v = abs(sum(x*y for x, y in zip(c, s)))
        return tuple(sorted(((v//b**i) % b for i in range(L)), reverse=True)), v
    done = {}  # multiset -> endpoint value or None
    ends = set(); maxd = 0
    for t in itertools.combinations_with_replacement(range(b-1, -1, -1), L):
        if t[0] == t[-1]: continue
        path = []; cur = t; seen = {}; val = None
        while cur not in done and cur not in seen:
            seen[cur] = len(path); path.append(cur)
            nxt, v = step(cur)
            if nxt == cur: val = ('fix', v); break
            cur = nxt
        if val is None:
            if cur in done: val = done[cur]
            else: val = ('cycle', cur)
        for p in path: done[p] = val
        ends.add(val)
        if len(ends) > 1: return "FAIL", list(ends)[:3]
    return "PASS", ends
if __name__ == "__main__":
    tests = [("HDCGFIEBA", "ICDHGBAEF", 10), ("ABCD", "CDAB", 2), ("ABCD","CDAB",3), ("ABCD","CDAB",6), ("ABCD","CDAB",12), ("ABCD","CDAB",5),("ABCD","CDAB",10),
             ("CADBFE","BFECAD",10), ("EABDFC","DFCEAB",10), ("EABDFC","DFCEAB",7), ("GFEABDHC","HGDFCEAB",10)]
    # Nuez extreme swap: descending minus descending with first/last swapped
    for L in range(3, 9):
        w1 = "".join(chr(65+i) for i in range(L)); w2 = w1[-1] + w1[1:-1] + w1[0]
        tests.append((w1, w2, 10))
    if len(sys.argv) > 1: tests = [("BACEGFJIMHLKD", "CGHBDAFLKIMJE", 10)]
    for w1, w2, b in tests:
        print(w1, "-", w2, "base", b, run(w1, w2, b), flush=True)
