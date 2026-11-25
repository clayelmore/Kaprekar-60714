"""Build paper_hierarchy.tex and paper_hierarchy.pdf from paper_hierarchy.md.
Needs pandoc and tectonic (brew install pandoc tectonic). Run from the repo root:
    /usr/bin/python3 scripts/build_hierarchy_pdf.py
The LaTeX preamble (everything before \\begin{document}) is kept from the existing paper_hierarchy.tex."""
import re, subprocess, sys, os
md = open("paper_hierarchy.md").read()
m = re.match(r"---\n(.*?)\n---\n(.*)", md, re.S)
front, body_md = m.group(1), m.group(2)
abstract_md = re.search(r"abstract: \|\n((?:  .*\n?)+)", front).group(1)
abstract_md = "\n".join(l[2:] for l in abstract_md.splitlines())
def pandoc(text):
    return subprocess.run(["pandoc", "-f", "markdown", "-t", "latex", "--wrap=none", "--shift-heading-level-by=-1"], input=text, capture_output=True, text=True, check=True).stdout
tex_old = open("paper_hierarchy.tex").read()
preamble = tex_old[:tex_old.index("\\begin{document}")]
out = (preamble + "\\begin{document}\n\\emergencystretch=3em\n\\maketitle\n\n\\begin{abstract}\n" + pandoc(abstract_md).strip()
       + "\n\\end{abstract}\n\n" + pandoc(body_md) + "\n\\end{document}\n")
open("paper_hierarchy.tex", "w").write(out)
r = subprocess.run(["tectonic", "paper_hierarchy.tex"], capture_output=True, text=True)
warn = [l for l in (r.stdout + r.stderr).splitlines() if "warning" in l.lower() or "error" in l.lower()]
print("\n".join(warn[:40])); print("exit", r.returncode)
