"""Build theorem_paper/paper_allbases.{md,tex,pdf} from the section files.
Needs pandoc and tectonic. Run from the repo root:  /usr/bin/python3 theorem_paper/build.py
The LaTeX preamble is taken from paper_hierarchy.tex with title, author and date replaced."""
import re, subprocess, os
D = "theorem_paper"
ORDER = ["sec1_intro.md", "sec2_setting.md", "sec3_even.md", "sec4_odd.md", "sec5_certificate.md",
         "sec6_computations.md", "sec7_caution.md", "sec7_proof_family.md", "sec7_proof_corner.md", "sec8_open.md", "sec9_back.md"]
front = open(f"{D}/front.md").read()
title = re.search(r'^title: "(.*)"$', front, re.M).group(1)
abstract = re.search(r"abstract: \|\n((?:  .*\n?)+)", front).group(1)
abstract = "\n".join(l[2:] for l in abstract.splitlines())
body = "\n\n".join(open(f"{D}/{f}").read().strip() for f in ORDER if os.path.exists(f"{D}/{f}"))
open(f"{D}/paper_allbases.md", "w").write(front.strip() + "\n\n" + body + "\n")
def pandoc(t):
    return subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "--wrap=none", "--shift-heading-level-by=-1"],
                          input=t, capture_output=True, text=True, check=True).stdout
old = open("paper_hierarchy.tex").read()
pre = old[:old.index("\\begin{document}")]
pre = pre.replace("\u2014", "-").replace("\u2013", "-")
pre = re.sub(r"\\title\{.*?\}\n", lambda m: "\\title{" + pandoc(title).strip() + "}\n", pre, flags=re.S)
tex = (pre + "\\begin{document}\n\\emergencystretch=3em\n\\maketitle\n\n\\begin{abstract}\n" + pandoc(abstract).strip()
       + "\n\\end{abstract}\n\n" + pandoc(body) + "\n\\end{document}\n")
open(f"{D}/paper_allbases.tex", "w").write(tex)
r = subprocess.run(["tectonic", "paper_allbases.tex"], cwd=D, capture_output=True, text=True)
out = r.stdout + r.stderr
print("\n".join(l for l in out.splitlines() if "warning" in l.lower() or "error" in l.lower())[:4000]); print("exit", r.returncode)
