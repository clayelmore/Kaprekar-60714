"""Draw every start flowing into the endpoint as a radial tree (SVG), written 2026-11-25.
  /usr/bin/python3 tree.py            -> tree_60714_d5.svg (rule ADCBE - DEACB) and tree_6174_d4.svg (Kaprekar, ABCD - DCBA)
Each dot is one collection of digits (order does not matter, because every step sorts first). A line joins a
collection to the one it becomes after one step. Collections made of a single repeated digit are left out.
Groups are tagged by distance from the endpoint (class="ring rN") so the picture can be revealed ring by ring."""
import itertools, math
from collections import defaultdict
def build(D, P, Q, label):
    def step(s):                                   # s: digits sorted descending
        p = int("".join(str(s[i]) for i in P)); q = int("".join(str(s[i]) for i in Q))
        return tuple(sorted((int(c) for c in str(abs(p - q)).zfill(D)), reverse=True))
    states = [s for s in itertools.combinations_with_replacement(range(9, -1, -1), D) if s[0] != s[-1]]
    nxt = {s: step(s) for s in states}
    root = tuple(sorted((int(c) for c in label), reverse=True))
    assert nxt[root] == root
    kids = defaultdict(list)
    for s, t in nxt.items():
        if s != root: kids[t].append(s)
    depth, order, stack = {root: 0}, [], [root]
    while stack:
        s = stack.pop(); order.append(s)
        for k in kids[s]: depth[k] = depth[s] + 1; stack.append(k)
    assert len(order) == len(states), "not every start reaches the endpoint"
    strings = lambda s: math.factorial(D) // math.prod(math.factorial(s.count(x)) for x in set(s))
    size = {}
    for s in reversed(order): size[s] = strings(s) + sum(size[k] for k in kids[s])   # starts passing through s
    leaves = {}
    for s in reversed(order): leaves[s] = max(1, sum(leaves[k] for k in kids[s]))
    ang = {}
    def lay(s, a0, a1):
        ang[s] = (a0 + a1) / 2; a = a0
        for k in sorted(kids[s], key=lambda k: -size[k]):
            w = (a1 - a0) * leaves[k] / leaves[s]; lay(k, a, a + w); a += w
    import sys; sys.setrecursionlimit(10000)
    lay(root, -math.pi / 2, 3 * math.pi / 2)
    DM = max(depth.values()); W = 1000; R = 455
    def xy(s):
        r = R * (depth[s] / DM) ** 0.8; return W/2 + r * math.cos(ang[s]), W/2 + r * math.sin(ang[s])
    def col(d):                                    # post-it yellow far out -> white at the endpoint
        t = d / DM; return "rgb(%d,%d,%d)" % (255, 255 - 30 * t, 255 - 170 * t)
    rings = defaultdict(list)
    for s in order:
        if s == root: continue
        x1, y1 = xy(s); x2, y2 = xy(nxt[s])
        w = 0.5 + 5.5 * (size[s] / size[root]) ** 0.5
        # follow the rings: turn toward the parent's direction while moving inward, so links never cut across the middle
        r1 = R * (depth[s] / DM) ** 0.8; r2 = R * (depth[nxt[s]] / DM) ** 0.8; a1 = ang[s]; a2 = ang[nxt[s]]
        n = max(2, int(abs(a1 - a2) * r1 / 12) + 2); pts = []
        for i in range(n + 1):
            t = i / n; e = t * t * (3 - 2 * t); rr = r1 + (r2 - r1) * (t ** 2.2); aa = a1 + (a2 - a1) * e
            pts.append("%.1f %.1f" % (W/2 + rr * math.cos(aa), W/2 + rr * math.sin(aa)))
        rings[depth[s]].append('<path d="M%s" fill="none" stroke="%s" stroke-width="%.2f" stroke-linecap="round" stroke-linejoin="round" opacity="0.8"/>' % ("L".join(pts), col(depth[s]), w))
        if not kids[s]: rings[depth[s]].append('<circle cx="%.1f" cy="%.1f" r="1.6" fill="%s"/>' % (x1, y1, col(depth[s])))
    body = "\n".join('<g class="ring r%d">\n%s\n</g>' % (d, "\n".join(rings[d])) for d in range(DM, 0, -1))
    fs = 46 if D == 5 else 54
    core = ('<circle class="core" cx="500" cy="500" r="%d" fill="#000" stroke="#5fd68a" stroke-width="4"/>'
            '<text class="core" x="500" y="%d" text-anchor="middle" font-family="Space Mono, Menlo, monospace" font-weight="700" font-size="%d" fill="#5fd68a">%s</text>'
            % (fs * 1.75, 500 + fs * 0.34, fs, label))
    inner = body + "\n" + core
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><rect width="1000" height="1000" fill="#000"/>\n' + inner + "\n</svg>\n")
    return svg, inner, dict(states=len(states), strings=size[root], maxdepth=DM)
if __name__ == "__main__":
    for D, P, Q, label, name in ((5, (0,3,2,1,4), (3,4,0,2,1), "60714", "tree_60714_d5"), (4, (0,1,2,3), (3,2,1,0), "6174", "tree_6174_d4")):
        svg, inner, info = build(D, P, Q, label)
        open(name + ".svg", "w").write(svg); open(name + ".inner.svg", "w").write(inner)
        print(name, info, len(svg) // 1024, "KB")
