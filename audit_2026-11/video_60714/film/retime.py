"""Rebuild the scene files so the pictures follow the narration takes in assets/vo/.
Run from this folder after replacing any take:  /usr/bin/python3 retime.py
It overwrites index.html and compositions/*.html, so hand edits to those files are lost."""
import re, subprocess
def dur(name):
    out = subprocess.run(["afinfo", "assets/vo/" + name], capture_output=True, text=True).stdout
    return float(re.search(r"estimated duration: ([\d.]+)", out).group(1))
VO = ["01_four", "02_five", "03_loop", "04_bulb", "05_stays", "05b_why", "05c_count", "06_run", "07_again", "08_last", "08b_tree", "09_claim"]
EXT = {v: next(e for e in ("mp3", "wav", "m4a") if __import__("os").path.exists("assets/vo/%s.%s" % (v, e))) for v in VO}
F, A, B, C, Dd, Y, CT, R0, R1, R2, TR, M = (dur("%s.%s" % (v, EXT[v])) for v in VO)
G = 0.35                                  # pause between takes
r2 = lambda x: round(x, 2)
FOUR = r2(F + 1.2)
TB = r2(A + G); TC = r2(TB + B + G); TD = r2(TC + C + G); RULE = r2(TD + Dd + 1.2)
WHY = r2(Y + 1.0); COUNT = r2(CT + 1.0); TREE = r2(TR + 1.5); T1 = r2(R0 + G); T2 = r2(T1 + R1 + G); RUN = r2(T2 + R2 + 1.3); CLAIM = r2(M + 1.8)
CSS = r"""
    #root { position: absolute; inset: 0; font-family: 'Outfit', sans-serif; color: #f4f4f0; }
    .bg { position: absolute; inset: 0;
      background: #000; }
    .layer { position: absolute; inset: 0; }
    .hl { position: absolute; left: 192px; top: 104px; font-weight: 700; font-size: 68px; letter-spacing: -0.01em; white-space: nowrap; }
    .note { position: absolute; font-weight: 600; font-size: 36px; color: #b9b9b2; white-space: nowrap; }
    .pi { position: absolute; width: 150px; height: 150px; }
    .pi-face { position: relative; width: 100%; height: 100%; background: linear-gradient(170deg, #fff08a 0%, #ffe14d 100%);
      box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.4); border-radius: 3px;
      display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 100px; color: #1c1810; }
    .pi-l { position: absolute; left: 10px; top: 2px; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 40px; line-height: 44px; color: #8a6508; }
    .minus { position: absolute; font-weight: 800; font-size: 110px; line-height: 150px; width: 90px; text-align: center; }
    .bar { position: absolute; height: 7px; border-radius: 4px; background: #f4f4f0; }
    .res { position: absolute; width: 150px; text-align: center; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 112px; line-height: 130px; }
    .formula { position: absolute; text-align: center; font-family: 'Space Mono', monospace; font-weight: 700; font-size: 56px; white-space: nowrap; }
    .num { position: absolute; width: 240px; text-align: center; font-family: 'Space Mono', monospace; font-weight: 700; white-space: nowrap; }
    .big { position: absolute; text-align: center; font-weight: 700; white-space: nowrap; }
    .red { color: #ff6b5e; } .green { color: #5fd68a; }
"""
ROT = [-3, 2, -1.5, 3, -2, 1.5, -2.5, 2.5, -1, 2]
def pi(id_, letter, digit, x, y, r):
    return ('<div id="%s" class="pi" style="left:%dpx;top:%dpx"><div class="pi-face" style="transform:rotate(%sdeg)">'
            '<span class="pi-l">%s</span>%s</div></div>' % (id_, x, y, r, letter, digit))
LOGO = '''    <svg class="logo" data-layout-ignore viewBox="1 7 62 82" fill="none" stroke-linecap="round" stroke-linejoin="round" style="position:absolute;left:1734px;top:934px;width:66px;height:88px">
      <path d="M4 60 H60" stroke="#8FC6E8" stroke-width="1.6"/>
      <g stroke="#EFF3EE" stroke-width="2.5"><path d="M32 60 C32 44 32 30 32 16 l5 0 l0 -6 l-9 0 l0 7 l5 0"/><path d="M32 60 C30 46 22 36 14 28 l6 -1 l-2 -6 l-8 3 l2 5"/><path d="M32 60 C34 46 42 36 50 28 l-6 -1 l2 -6 l8 3 l-2 5"/><path d="M32 60 C29 50 20 46 10 44 l5 -3 l-4 -5 l-7 5 l3 4"/><path d="M32 60 C35 50 44 46 54 44 l-5 -3 l4 -5 l7 5 l-3 4"/></g>
      <g stroke="#EFF3EE" stroke-width="2.5" opacity="0.5" transform="translate(0,60) scale(1,-0.52) translate(0,-60)"><path d="M32 60 C32 44 32 30 32 16 l5 0 l0 -6 l-9 0 l0 7 l5 0"/><path d="M32 60 C30 46 22 36 14 28 l6 -1 l-2 -6 l-8 3 l2 5"/><path d="M32 60 C34 46 42 36 50 28 l-6 -1 l2 -6 l8 3 l-2 5"/><path d="M32 60 C29 50 20 46 10 44 l5 -3 l-4 -5 l-7 5 l3 4"/><path d="M32 60 C35 50 44 46 54 44 l-5 -3 l4 -5 l7 5 l-3 4"/></g>
    </svg>\n'''
def scene(sid, body, script):
    return ('<template>\n  <style>' + CSS + '  </style>\n  <div id="root" data-composition-id="' + sid
            + '" data-width="1920" data-height="1080">\n    <div class="bg"></div>\n' + LOGO + body
            + '\n  </div>\n  <script>\n    const tl = gsap.timeline({ paused: true });\n' + script
            + '\n    window.__timelines["' + sid + '"] = tl;\n  </script>\n</template>\n')
JS_HELPERS = r"""
    const show = (sel, t, o = {}) => tl.fromTo(sel, { opacity: 0, y: o.y ?? 24 }, { opacity: 1, y: 0, duration: o.d ?? 0.4, ease: "power3.out", stagger: o.s ?? 0 }, t);
    const pop = (sel, t, s = 0.09) => tl.fromTo(sel, { opacity: 0, y: -70, scale: 1.18 }, { opacity: 1, y: 0, scale: 1, duration: 0.38, ease: "back.out(1.6)", stagger: s }, t);
    const hide = (sel, t, d = 0.3) => tl.fromTo(sel, { opacity: 1 }, { opacity: 0, duration: d, ease: "power2.in", immediateRender: false }, t);
"""
X0, DX, YT, YB = 200, 170, 280, 460

# ---------- scene 1: four digits ----------
L4, D4 = "ABCD", "7641"
top = "\n".join("      " + pi("four-t%d" % i, L4[i], D4[i], X0 + i*DX, YT, ROT[i]) for i in range(4))
bot = "\n".join("      " + pi("four-b%d" % i, L4[3-i], D4[3-i], X0 + i*DX, YB, ROT[i+5]) for i in range(4))
res = "\n".join('      <span class="res four-res" style="left:%dpx;top:660px">%s</span>' % (X0 + i*DX, "6174"[i]) for i in range(4))
body = f"""    <div id="four-hl" class="clip layer" data-start="0" data-duration="{FOUR}" data-track-index="1"><div class="hl" id="four-hl-t">Four digits. Biggest minus smallest.</div></div>
    <div id="four-board" class="clip layer" data-start="0" data-duration="{FOUR}" data-track-index="2">
{top}
{bot}
      <div class="minus" id="four-minus" style="left:100px;top:{YB}px">&minus;</div>
      <div class="bar" id="four-bar" style="left:190px;top:636px;width:680px"></div>
{res}
      <div class="formula" id="four-formula" style="left:190px;top:830px;width:680px">ABCD &minus; DCBA</div>
    </div>
    <div id="four-side" class="clip layer" data-start="0" data-duration="{FOUR}" data-track-index="3">
      <div class="big" id="four-s1" style="left:1010px;top:330px;width:720px;font-size:60px">Start with any four digits.</div>
      <div class="big" id="four-s2" style="left:1010px;top:440px;width:720px;font-size:60px">Repeat. You always end at</div>
      <div class="big green" id="four-s3" style="left:1010px;top:540px;width:720px;font-size:170px;font-family:'Space Mono',monospace">6174</div>
      <div class="note" id="four-s4" style="left:1010px;top:770px;width:720px;text-align:center">(unless all four digits match)</div>
      <div class="big" id="four-s5" style="left:1010px;top:850px;width:720px;font-size:44px">Kaprekar's constant<br><span id="four-s6" style="display:inline-block;font-weight:500;font-size:38px;color:#b9b9b2">D. R. Kaprekar, 1949</span></div>
    </div>"""
js = JS_HELPERS + r"""
    const F = __F__;
    pop("#four-t0,#four-t1,#four-t2,#four-t3", 0.10 * F);
    pop("#four-b0,#four-b1,#four-b2,#four-b3", 0.26 * F);
    show("#four-formula", 0.30 * F);
    show("#four-minus,#four-bar", 0.36 * F, { y: 0 });
    show(".four-res", 0.40 * F, { s: 0.08, y: 30 });
    show("#four-s1", 0.44 * F); show("#four-s2", 0.50 * F);
    tl.fromTo("#four-s3", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.8)" }, 0.57 * F);
    show("#four-s4", 0.62 * F);
    show("#four-s5", 0.68 * F); show("#four-s6", 0.84 * F);""".replace("__F__", "%g" % F)
open("compositions/four.html", "w").write(scene("four", body, js))

# ---------- scene 2: the rule (classic fails, rearranged works) ----------
L, D = "ABCDE", "76410"
top = "\n".join("      " + pi("rule-t%s" % L[i], L[i], D[i], X0 + i*DX, YT, ROT[i]) for i in range(5))
bot = "\n".join("      " + pi("rule-b%s" % L[i], L[i], D[i], X0 + i*DX, YB, ROT[i+5]) for i in range(5))
res_old = "\n".join('      <span class="res rule-old red" style="left:%dpx;top:660px">%s</span>' % (X0 + i*DX, "74943"[i]) for i in range(5))
res_new = "\n".join('      <span class="res rule-new green" style="left:%dpx;top:660px">%s</span>' % (X0 + i*DX, "60714"[i]) for i in range(5))
ring = [("74943", 1400, 330), ("62964", 1610, 520), ("71973", 1400, 710), ("83952", 1190, 520)]
nums = "\n".join('      <div class="num rule-ring" id="rule-n%d" style="left:%dpx;top:%dpx;font-size:54px;line-height:70px">%s</div>' % (i, x-120, y-35, s) for i, (s, x, y) in enumerate(ring))
body = f"""    <div id="rule-hl1" class="clip layer" data-start="0" data-duration="{TB}" data-track-index="1"><div class="hl" id="rule-hl1-t">Five digits? Try 60714. Same rule.</div></div>
    <div id="rule-hl2" class="clip layer" data-start="{TB}" data-duration="{r2(TC-TB)}" data-track-index="1"><div class="hl" id="rule-hl2-t">Keep going and it never lands.</div></div>
    <div id="rule-hl3" class="clip layer" data-start="{TC}" data-duration="{r2(RULE-TC)}" data-track-index="1"><div class="hl" id="rule-hl3-t">Same five notes. New order.</div></div>
    <div id="rule-board" class="clip layer" data-start="0" data-duration="{RULE}" data-track-index="2">
      <div class="note" id="rule-sorted" style="left:200px;top:212px">60714, sorted biggest first</div>
{top}
{bot}
      <div class="minus" id="rule-minus" style="left:100px;top:{YB}px">&minus;</div>
      <div class="bar" id="rule-bar" style="left:190px;top:636px;width:850px"></div>
{res_old}
{res_new}
      <div class="formula" id="rule-f-old" style="left:190px;top:830px;width:850px">ABCDE &minus; EDCBA</div>
      <div class="formula green" id="rule-f-new" style="left:190px;top:830px;width:850px">ADCBE &minus; DEACB</div>
    </div>
    <div id="rule-loop" class="clip layer" data-start="{TB}" data-duration="{r2(TC-TB+0.3)}" data-track-index="3">
      <div id="rule-loop-in" class="layer">
      <svg id="rule-arcs" class="layer" viewBox="0 0 1920 1080" width="1920" height="1080">
        <defs><marker id="rule-ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#ff6b5e"/></marker></defs>
        <path class="rule-arc" id="rule-a0" d="M1500 338 Q1606 352 1610 462" fill="none" stroke="#ff6b5e" stroke-width="7" stroke-linecap="round" marker-end="url(#rule-ah)"/>
        <path class="rule-arc" id="rule-a1" d="M1610 578 Q1606 698 1502 710" fill="none" stroke="#ff6b5e" stroke-width="7" stroke-linecap="round" marker-end="url(#rule-ah)"/>
        <path class="rule-arc" id="rule-a2" d="M1298 710 Q1194 698 1190 578" fill="none" stroke="#ff6b5e" stroke-width="7" stroke-linecap="round" marker-end="url(#rule-ah)"/>
        <path class="rule-arc" id="rule-a3" d="M1190 462 Q1194 352 1300 338" fill="none" stroke="#ff6b5e" stroke-width="7" stroke-linecap="round" marker-end="url(#rule-ah)"/>
      </svg>
{nums}
      <div class="big red" id="rule-loop-l" style="left:1040px;top:820px;width:720px;font-size:54px">A loop. Round and round.</div>
      </div>
    </div>
    <div id="rule-win" class="clip layer" data-start="{TC}" data-duration="{r2(RULE-TC)}" data-track-index="3">
      <div id="rule-glow" style="position:absolute;left:1240px;top:170px;width:320px;height:320px;border-radius:50%;background:radial-gradient(circle,rgba(255,226,90,0.55) 0%,rgba(255,236,120,0) 68%)"></div>
      <svg id="rule-bulb" style="position:absolute;left:1310px;top:240px" width="180" height="200" viewBox="0 0 180 200">
        <path d="M90 14 C46 14 22 46 22 80 C22 108 40 122 52 138 L128 138 C140 122 158 108 158 80 C158 46 134 14 90 14 Z" fill="#ffd83a" stroke="#fff3b0" stroke-width="5" stroke-linejoin="round"/>
        <rect x="58" y="146" width="64" height="16" rx="6" fill="#f4f4f0"/><rect x="66" y="168" width="48" height="14" rx="6" fill="#f4f4f0"/>
        <path d="M70 92 L90 112 L110 92" fill="none" stroke="#1c1810" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <div class="big" id="rule-w1" style="left:1040px;top:520px;width:720px;font-size:58px">We started with 60714.</div>
      <div class="big" id="rule-w2" style="left:1040px;top:610px;width:720px;font-size:58px">We got 60714 back.</div>
      <div class="big green" id="rule-w3" style="left:1040px;top:720px;width:720px;font-size:120px">It stays.</div>
    </div>"""
js = JS_HELPERS + r"""
    const DX = 170, L = ["A", "B", "C", "D", "E"];
    const slide = (id, from, to, t, d, hop) => {
      tl.fromTo(id, { x: from * DX }, { x: to * DX, duration: d, ease: "power2.inOut", immediateRender: false }, t);
      tl.fromTo(id, { y: 0 }, { y: hop, duration: d / 2, ease: "sine.out", immediateRender: false }, t);
      tl.fromTo(id, { y: hop }, { y: 0, duration: d / 2, ease: "sine.in", immediateRender: false }, t + d / 2);
    };
    const A = __A__, B = __B__, C = __C__, D = __D__, TB = __TB__, TC = __TC__, TD = __TD__;
    show("#rule-hl1-t", 0.15);
    // 60714 arrives in its own order, then sorts: A=7 comes from column 2, B=6 from 0, C=4 from 4, D=1 from 3, E=0 from 1
    const FROM = [2, 0, 4, 3, 1], TL = '[id^="rule-t"] .pi-l';
    tl.set(TL + ",#rule-sorted", { opacity: 0 }, 0);
    L.forEach((l, i) => tl.set("#rule-t" + l, { x: (FROM[i] - i) * DX }, 0));
    tl.fromTo(L.map((l) => "#rule-t" + l).join(","), { opacity: 0, scale: 1.15 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(1.6)", stagger: 0.05 }, 0.16 * A);
    L.forEach((l, i) => slide("#rule-t" + l, FROM[i] - i, 0, 0.42 * A, 0.9, (FROM[i] - i) ? (i % 2 ? 80 : -80) : 0));
    tl.fromTo(TL + ",#rule-sorted", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power2.out", immediateRender: false }, 0.42 * A + 0.9);
    pop(L.map((l) => "#rule-b" + l).join(","), 0.58 * A);
    // classic rule: second row reversed, EDCBA (letter at column i goes to column 4 - i)
    const rev = [4, 2, 0, -2, -4], hop1 = [-95, 60, 0, -60, 95];
    L.forEach((l, i) => slide("#rule-b" + l, 0, rev[i], 0.66 * A, 1.0, hop1[i]));
    show("#rule-f-old", 0.68 * A);
    show("#rule-minus,#rule-bar", 0.82 * A, { y: 0 });
    show(".rule-old", 0.86 * A, { s: 0.08, y: 30 });
    // the loop
    show("#rule-hl2-t", TB + 0.15);
    [0, 1, 2, 3].forEach((i) => {
      const t = TB + 0.3 + i * 0.5;
      tl.fromTo("#rule-n" + i, { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(1.8)" }, t);
      tl.fromTo("#rule-a" + i, { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power2.out" }, t + 0.3);
    });
    show("#rule-loop-l", TB + 0.45 * B);
    const P0 = TB + 2.5, PN = Math.max(4, Math.floor((TC - 0.3 - P0) / 0.36));
    for (let k = 0; k < PN; k++) {
      tl.fromTo("#rule-n" + (k % 4), { scale: 1, color: "#f4f4f0" }, { scale: 1.22, color: "#ff6b5e", duration: 0.17, ease: "power2.out", repeat: 1, yoyo: true, immediateRender: false }, P0 + k * 0.36);
    }
    hide("#rule-loop-in", TC - 0.1);
    // light bulb: same notes, new order
    show("#rule-hl3-t", TC + 0.3);
    tl.fromTo("#rule-bulb", { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.45, ease: "back.out(2.2)" }, TC + 0.3);
    tl.fromTo("#rule-glow", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1.25, duration: 0.5, ease: "power2.out" }, TC + 0.35);
    tl.fromTo("#rule-glow", { scale: 1.25 }, { scale: 1, duration: 0.6, ease: "sine.inOut", immediateRender: false }, TC + 0.85);
    hide(".rule-old", TC + 0.16 * C); hide("#rule-f-old", TC + 0.16 * C); hide("#rule-minus,#rule-bar", TC + 0.16 * C);
    // back to the sorted order first, so the new shuffle starts from the same place as the old one
    L.forEach((l, i) => slide("#rule-b" + l, rev[i], 0, TC + 0.20 * C, 0.8, hop1[i] / 2));
    // top row ABCDE -> ADCBE : B and D trade places
    hide("#rule-sorted", TC + 0.34 * C);
    slide("#rule-tB", 0, 2, TC + 0.36 * C, 1.0, -100);
    slide("#rule-tD", 0, -2, TC + 0.36 * C, 1.0, 100);
    // second row EDCBA -> DEACB
    const to2 = [2, 3, 1, -3, -3], hop2 = [-100, 70, -40, 100, -70];
    L.forEach((l, i) => slide("#rule-b" + l, 0, to2[i], TC + 0.64 * C, 1.1, hop2[i]));
    show("#rule-f-new", TC + 0.38 * C);
    tl.fromTo("#rule-minus,#rule-bar", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "power2.out", immediateRender: false }, TD - 0.9);
    tl.fromTo(".rule-new", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out", stagger: 0.08 }, TD + 0.12 * D);
    show("#rule-w1", TD + 0.50 * D); show("#rule-w2", TD + 0.62 * D);
    tl.fromTo("#rule-w3", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.8)" }, TD + 0.80 * D);"""
for k, v in (("__A__", A), ("__B__", B), ("__C__", C), ("__D__", Dd), ("__TB__", TB), ("__TC__", TC), ("__TD__", TD)):
    js = js.replace(k, "%g" % v)
open("compositions/rule.html", "w").write(scene("rule", body, js))

# ---------- scene 2b: why sort first ----------
body = f"""    <div id="why-hl" class="clip layer" data-start="0" data-duration="{WHY}" data-track-index="1"><div class="hl" id="why-hl-t">Why sort first?</div></div>
    <div id="why-board" class="clip layer" data-start="0" data-duration="{WHY}" data-track-index="2">
      <div class="big" id="why-l1" style="left:192px;top:300px;width:1536px;font-size:60px">Skip the sorting. Just shuffle the digits as written.</div>
      <div class="big" id="why-l2" style="left:192px;top:470px;width:1536px;font-size:130px;font-family:'Space Mono',monospace">7,140 rules tried</div>
      <div class="big red" id="why-l3" style="left:192px;top:650px;width:1536px;font-size:130px;font-family:'Space Mono',monospace">0 work</div>
      <div class="note" id="why-l4" style="left:192px;top:860px;width:1536px;text-align:center;font-size:40px">five digits, every start checked by computer</div>
    </div>"""
js = JS_HELPERS + r"""
    const Y = __Y__;
    show("#why-hl-t", 0.15);
    show("#why-l1", 0.22 * Y);
    show("#why-l2", 0.42 * Y);
    tl.fromTo("#why-l3", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(1.8)" }, 0.74 * Y);
    show("#why-l4", 0.86 * Y);""".replace("__Y__", "%g" % Y)
open("compositions/why.html", "w").write(scene("why", body, js))

# ---------- scene 2c: every digit counts ----------
def letters(prefix, word, x, y, bad=None):
    return "\n".join('      <div class="num %s%s" style="left:%dpx;top:%dpx;width:110px;font-size:110px;line-height:130px">%s</div>'
                     % (prefix, (" red" if bad and ch in bad else ""), x + i*120, y, ch) for i, ch in enumerate(word))
body = f"""    <div id="count-hl" class="clip layer" data-start="0" data-duration="{COUNT}" data-track-index="1"><div class="hl" id="count-hl-t">Every digit counts.</div></div>
    <div id="count-board" class="clip layer" data-start="0" data-duration="{COUNT}" data-track-index="2">
      <div class="note" id="count-n1" style="left:230px;top:250px;font-size:40px">a shortcut rule: everything lands on 45000</div>
{letters("count-o", "ADEBC", 230, 320, "BC")}
{letters("count-o", "EADBC", 230, 460, "BC")}
      <div class="minus count-o" style="left:120px;top:450px">&minus;</div>
      <div class="big red" id="count-x" style="left:230px;top:640px;width:600px;font-size:50px">B and C never move.<br>Two digits are ignored.</div>
      <div class="note" id="count-n2" style="left:1090px;top:250px;font-size:40px">the new order</div>
{letters("count-w green", "ADCBE", 1090, 320)}
{letters("count-w green", "DEACB", 1090, 460)}
      <div class="minus count-w" style="left:980px;top:450px">&minus;</div>
      <div class="big green" id="count-y" style="left:1090px;top:640px;width:600px;font-size:50px">Every letter moves.<br>All five digits matter.</div>
      <div class="big" id="count-z" style="left:192px;top:860px;width:1536px;font-size:60px">No shortcuts. No digit is ignored.</div>
    </div>"""
js = JS_HELPERS + r"""
    const CT = __CT__;
    show("#count-hl-t", 0.15);
    show("#count-n1", 0.16 * CT); show(".count-o", 0.18 * CT, { s: 0.03 });
    show("#count-x", 0.36 * CT);
    show("#count-n2", 0.66 * CT); show(".count-w", 0.68 * CT, { s: 0.03 });
    show("#count-y", 0.76 * CT);
    show("#count-z", 0.88 * CT);""".replace("__CT__", "%g" % CT)
open("compositions/count.html", "w").write(scene("count", body, js))

# ---------- scene 3b: the tree of every start ----------
tree_inner = open("../tree_60714_d5.inner.svg").read()
DMAX = max(int(x) for x in re.findall(r'class="ring r(\d+)"', tree_inner))
body = f"""    <div id="tree-pic" class="clip layer" data-start="0" data-duration="{TREE}" data-track-index="2" data-layout-ignore>
      <svg id="tree-svg" viewBox="0 0 1000 1000" style="position:absolute;left:560px;top:50px;width:980px;height:980px">
{tree_inner}
      </svg>
    </div>
    <div id="tree-hl" class="clip layer" data-start="0" data-duration="{TREE}" data-track-index="1">
      <div class="hl" id="tree-hl-t">Every start, at once.</div>
      <div class="note" id="tree-n1" style="left:192px;top:780px;font-size:40px">99,990 starts</div>
      <div class="note" id="tree-n2" style="left:192px;top:840px;font-size:40px">each line is one step</div>
      <div class="note" id="tree-n3" style="left:192px;top:900px;font-size:40px">one endpoint</div>
    </div>"""
js = JS_HELPERS + r"""
    const TR = __TR__, DM = __DM__;
    show("#tree-hl-t", 0.15);
    tl.fromTo("#tree-svg .core", { opacity: 0 }, { opacity: 1, duration: 0.4, ease: "power2.out" }, 0.2);
    for (let d = DM; d >= 1; d--) tl.fromTo("#tree-svg .r" + d, { opacity: 0 }, { opacity: 1, duration: 0.5, ease: "power2.out" }, 0.5 + (DM - d) * (0.72 * TR / DM));
    show("#tree-n1", 0.20 * TR); show("#tree-n2", 0.42 * TR); show("#tree-n3", 0.68 * TR);""".replace("__TR__", "%g" % TR).replace("__DM__", str(DMAX))
open("compositions/tree.html", "w").write(scene("tree", body, js))

# ---------- scene 3: one worked run, every step animated ----------
def kstep(n):
    d = sorted((int(ch) for ch in "%05d" % n), reverse=True)
    A_, B_, C_, D_, E_ = d
    return abs((10000*A_ + 1000*D_ + 100*C_ + 10*B_ + E_) - (10000*D_ + 1000*E_ + 100*A_ + 10*C_ + B_))
START = 58196
trip = [START]
while trip[-1] != 60714: trip.append(kstep(trip[-1]))
assert len(trip) == 4, trip                      # three steps; the layout below assumes it
SORTED, FROM = [], []                            # per step: sorted digits, and each letter's column in the unsorted number
for n in trip[:-1]:
    txt = "%05d" % n
    idx = sorted(range(5), key=lambda j: (-int(txt[j]), j))   # stable: equal digits keep their order
    SORTED.append([txt[j] for j in idx]); FROM.append(idx)
def pi3(id_, i, x, y, r):
    spans = "".join('<span class="run-d run-d%d" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">%s</span>' % (k, SORTED[k][i]) for k in range(3))
    return ('<div id="%s" class="pi" style="left:%dpx;top:%dpx"><div class="pi-face" style="transform:rotate(%sdeg)">'
            '<span class="pi-l run-l">%s</span>%s</div></div>' % (id_, x, y, r, "ABCDE"[i], spans))
top = "\n".join("      " + pi3("run-t%s" % "ABCDE"[i], i, X0 + i*DX, YT, ROT[i]) for i in range(5))
bot = "\n".join("      " + pi3("run-b%s" % "ABCDE"[i], i, X0 + i*DX, YB, ROT[i+5]) for i in range(5))
res = "\n".join('      <span class="res run-r%d%s" style="left:%dpx;top:660px">%s</span>' % (k, " green" if k == 2 else "", X0 + i*DX, ("%05d" % trip[k+1])[i]) for k in range(3) for i in range(5))
side = "\n".join('      <div class="num%s" id="run-n%d" style="left:1330px;top:%dpx;font-size:76px;line-height:96px">%s</div>' % (" green" if k == 3 else "", k, 262 + 150*k, "%05d" % trip[k]) for k in range(4))
arrows = "\n".join('      <div class="num" id="run-a%d" style="left:1410px;top:%dpx;width:80px;font-size:54px;line-height:60px;color:#b9b9b2">&darr;</div>' % (k, 355 + 150*k) for k in range(3))
body = f"""    <div id="run-hl" class="clip layer" data-start="0" data-duration="{RUN}" data-track-index="1"><div class="hl" id="run-hl-t">Any other start. Say {START}.</div></div>
    <div id="run-board" class="clip layer" data-start="0" data-duration="{RUN}" data-track-index="2">
      <div class="note" id="run-note" style="left:200px;top:212px">sorted, biggest first</div>
{top}
{bot}
      <div class="minus" id="run-minus" style="left:100px;top:{YB}px">&minus;</div>
      <div class="bar" id="run-bar" style="left:190px;top:636px;width:850px"></div>
{res}
      <div class="formula green" id="run-formula" style="left:190px;top:830px;width:850px">ADCBE &minus; DEACB</div>
    </div>
    <div id="run-side" class="clip layer" data-start="0" data-duration="{RUN}" data-track-index="3">
      <div id="run-ring" style="position:absolute;left:1290px;top:694px;width:320px;height:132px;border:9px solid #5fd68a;border-radius:66px"></div>
{side}
{arrows}
      <div class="big" id="run-cap" style="left:1130px;top:870px;width:640px;font-size:50px">Three steps. Then it stays.</div>
    </div>"""
js = JS_HELPERS + r"""
    const DX = 170, L = ["A", "B", "C", "D", "E"], FROM = __FROM__;
    const R0 = __R0__, R1 = __R1__, R2 = __R2__, T1 = __T1__, T2 = __T2__;
    const topTo = [0, 2, 0, -2, 0], botTo = [2, 3, 1, -3, -3];           // ADCBE and DEACB, as column shifts
    const hopT = [0, -100, 0, 100, 0], hopB = [-100, 70, -40, 100, -70];
    const move = (id, from, to, t, d, hop) => {
      tl.fromTo(id, { x: from * DX }, { x: to * DX, duration: d, ease: "power2.inOut", immediateRender: false }, t);
      if (hop) {
        tl.fromTo(id, { y: 0 }, { y: hop, duration: d / 2, ease: "sine.out", immediateRender: false }, t);
        tl.fromTo(id, { y: hop }, { y: 0, duration: d / 2, ease: "sine.in", immediateRender: false }, t + d / 2);
      }
    };
    const fade = (sel, from, to, t, d = 0.25) => tl.fromTo(sel, { opacity: from }, { opacity: to, duration: d, ease: "power2.out", immediateRender: false }, t);
    // start state: everything on the board hidden
    tl.set(".run-d,.run-l,#run-note,#run-minus,#run-bar,#run-formula,#run-ring,#run-cap,.res,#run-n1,#run-n2,#run-n3,#run-a0,#run-a1,#run-a2", { opacity: 0 }, 0);
    tl.set(L.map((l) => "#run-t" + l + ",#run-b" + l).join(","), { opacity: 0 }, 0);
    show("#run-hl-t", 0.15);
    tl.fromTo("#run-n0", { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(1.8)" }, 0.10 * R0);
    // one full step: the number arrives unsorted, sorts, gets letters, reorganizes into two rows, subtracts
    const step = (k, t) => {
      const tops = L.map((l) => "#run-t" + l), bots = L.map((l) => "#run-b" + l);
      if (k > 0) {                                                        // clear the previous step
        fade(tops.concat(bots).join(","), 1, 0, t.in - 0.35); fade(".run-r" + (k - 1), 1, 0, t.in - 0.35);
        fade("#run-minus,#run-bar,#run-note,.run-l", 1, 0, t.in - 0.35);
        tl.set(".run-d" + (k - 1), { opacity: 0 }, t.in - 0.05);
      }
      tl.set(".run-d" + k, { opacity: 1 }, t.in - 0.05);
      L.forEach((l, i) => {                                               // top row arrives in the number's own order
        tl.set("#run-t" + l, { x: (FROM[k][i] - i) * DX, y: 0 }, t.in - 0.04);
        tl.set("#run-b" + l, { x: 0, y: 0 }, t.in - 0.04);
      });
      tl.fromTo(tops.join(","), { opacity: 0, scale: 1.15 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(1.6)", stagger: 0.05, immediateRender: false }, t.in);
      L.forEach((l, i) => move("#run-t" + l, FROM[k][i] - i, 0, t.sort, t.sortD, (FROM[k][i] - i) ? (i % 2 ? 80 : -80) : 0));   // sort
      fade("#run-note,.run-l", 0, 1, t.sort + t.sortD);
      tl.fromTo(bots.join(","), { opacity: 0, y: -180 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out", stagger: 0.04, immediateRender: false }, t.copy);
      L.forEach((l, i) => { if (topTo[i]) move("#run-t" + l, 0, topTo[i], t.top, t.d, hopT[i]); });
      L.forEach((l, i) => move("#run-b" + l, 0, botTo[i], t.bot, t.d, hopB[i]));
      fade("#run-minus,#run-bar", 0, 1, t.res - 0.3);
      tl.fromTo(".run-r" + k, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35, ease: "power3.out", stagger: 0.06, immediateRender: false }, t.res);
      fade("#run-a" + k, 0, 1, t.res + 0.2);
      tl.fromTo("#run-n" + (k + 1), { opacity: 0, x: -40 }, { opacity: 1, x: 0, duration: 0.35, ease: "power3.out", immediateRender: false }, t.res + 0.35);
    };
    step(0, { in: 0.14 * R0, sort: 0.30 * R0, sortD: 0.9, copy: 0.46 * R0, top: 0.54 * R0, bot: 0.72 * R0, d: 1.0, res: 0.93 * R0 });
    fade("#run-formula", 0, 1, 0.56 * R0);
    step(1, { in: T1 + 0.22 * R1, sort: T1 + 0.40 * R1, sortD: 0.7, copy: T1 + 0.54 * R1, top: T1 + 0.64 * R1, bot: T1 + 0.64 * R1, d: 0.8, res: T1 + 0.88 * R1 });
    step(2, { in: T2 + 0.07 * R2, sort: T2 + 0.15 * R2, sortD: 0.7, copy: T2 + 0.24 * R2, top: T2 + 0.31 * R2, bot: T2 + 0.31 * R2, d: 0.8, res: T2 + 0.44 * R2 });
    tl.fromTo("#run-ring", { opacity: 0, scale: 1.3 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)", immediateRender: false }, T2 + 0.50 * R2);
    fade("#run-cap", 0, 1, T2 + 0.72 * R2, 0.4);
    tl.fromTo("#run-ring", { scale: 1 }, { scale: 1.12, duration: 0.3, ease: "sine.inOut", repeat: 1, yoyo: true, immediateRender: false }, T2 + 0.90 * R2);"""
for k_, v_ in (("__R0__", R0), ("__R1__", R1), ("__R2__", R2), ("__T1__", T1), ("__T2__", T2)):
    js = js.replace(k_, "%g" % v_)
js = js.replace("__FROM__", str(FROM))
open("compositions/run.html", "w").write(scene("run", body, js))

# ---------- scene 4: the claim ----------
XC = 545
pis = "\n".join("      " + pi("claim-p%d" % i, "", "60714"[i], XC + i*DX, 270, ROT[i]) for i in range(5))
body = f"""    <div id="claim-hl" class="clip layer" data-start="0" data-duration="{CLAIM}" data-track-index="1"><div class="hl" id="claim-hl-t" style="left:192px;width:1536px;text-align:center">Every five-digit start lands on 60714.</div></div>
    <div id="claim-board" class="clip layer" data-start="0" data-duration="{CLAIM}" data-track-index="2">
{pis}
      <div class="note" id="claim-tag" style="left:192px;top:452px;width:1536px;text-align:center;font-size:42px">the digits of 6174, plus a zero</div>
      <div class="big" id="claim-l1" style="left:192px;top:565px;width:1536px;font-size:48px">Checked by computer: all 99,990 starts with at least two different digits.</div>
      <div class="big" style="left:192px;top:640px;width:1536px;font-size:48px"><span id="claim-l2" style="display:inline-block">Longest trip: 30 steps.</span> <span id="claim-l2b" style="display:inline-block">Left out: the ten repeats, like 11111.</span></div>
      <div class="big" id="claim-l3" style="left:192px;top:725px;width:1536px;font-size:48px">Not Kaprekar's rule. Same idea, new order: <span class="green" style="font-family:'Space Mono',monospace">ADCBE &minus; DEACB</span></div>
      <div class="big" id="claim-l5" style="left:192px;top:815px;width:1536px;font-size:44px">We asked the questions. Claude and ChatGPT did the heavy lifting.</div>
      <div class="note" id="claim-l4" style="left:192px;top:895px;width:1536px;text-align:center;font-size:40px">Paper and code: link in the description</div>
    </div>"""
js = JS_HELPERS + r"""
    const M = __M__;
    show("#claim-hl-t", 0.15);
    pop("#claim-p0,#claim-p1,#claim-p2,#claim-p3,#claim-p4", 0.5);
    show("#claim-l1", 0.10 * M); show("#claim-tag", 0.22 * M);
    show("#claim-l2", 0.36 * M); show("#claim-l2b", 0.50 * M); show("#claim-l3", 0.62 * M); show("#claim-l5", 0.78 * M); show("#claim-l4", 0.93 * M);""".replace("__M__", "%g" % M)
open("compositions/claim.html", "w").write(scene("claim", body, js))

# ---------- root ----------
hosts, t = [], 0.0
starts = {}
for sid, dur in [("four", FOUR), ("rule", RULE), ("why", WHY), ("count", COUNT), ("run", RUN), ("tree", TREE), ("claim", CLAIM)]:
    starts[sid] = t
    hosts.append('      <div id="%s" data-composition-id="%s" data-composition-src="compositions/%s.html" data-start="%g" data-duration="%g" data-track-index="1" data-track-kind="graphics" data-width="1920" data-height="1080"></div>' % (sid, sid, sid, t, dur))
    t += dur
vo_at = [starts["four"], starts["rule"], starts["rule"] + TB, starts["rule"] + TC, starts["rule"] + TD, starts["why"], starts["count"], starts["run"], starts["run"] + T1, starts["run"] + T2, starts["tree"], starts["claim"]]
audio = ['      <audio id="vo-%s" class="clip" src="assets/vo/%s.%s" data-start="%g" data-duration="%g" data-track-index="2" data-volume="1"></audio>' % (v.split("_")[0], v, EXT[v], r2(at + 0.1), r2(d)) for v, at, d in zip(VO, vo_at, (F, A, B, C, Dd, Y, CT, R0, R1, R2, TR, M))]
open("index.html", "w").write("""<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1920, height=1080" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { margin: 0; width: 1920px; height: 1080px; overflow: hidden; background: #000; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="DUR" data-width="1920" data-height="1080">
HOSTS
    </div>
    <script>
      window.__timelines["main"] = gsap.timeline({ paused: true });
    </script>
  </body>
</html>
""".replace("DUR", "%g" % t).replace("HOSTS", "\n".join(hosts + audio)))
print("total", t)
