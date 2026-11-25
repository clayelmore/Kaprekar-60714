# 60714

A five-digit number that is a fixed point of an explicit Kaprekar-type rule at every digit length d ≥ 5.

At 5 and 6 digits, every input that is not one repeated digit reaches **60714** (at 5 digits: 99,990 of 100,000 strings, in at most 30 steps). At 7 or more digits, every input reaches either 60714 or 0. The inputs that collapse to 0 form an exactly characterized escape class, and its share grows with length: 0.56% of digit collections at 8 digits, about 12% at 24 digits (computed). The classical routine also sends inputs to 0, but only the repdigits; here the collapse reaches other inputs as well.

The paper fixes the digits of 6174 and varies the length: instead of fixing the rule and asking which digit lengths work, it lets the rule change with the length and follows one fixed point, 60714, across all lengths. The same family of rules (two permutations of the sorted digits, subtracted) was defined earlier by Peterson and Pulapaka (2008).

The paper's results include the **classification of universal full-variable fixed points at digit length d** (the catalog 0, 4, 33, 506 at d ∈ {3, 4, 5, 6}), the **coefficient-preserving lifting recipe** that connects rules across digit lengths, and the **escape class** (Definition 4.6) that describes exactly which inputs collapse to 0. 60714 is the only one of the 33 five-digit full-variable fixed points that is universal again at six digits.

## The paper

**[paper_hierarchy.pdf](paper_hierarchy.pdf)**: *The Digits of 6174 at Every Length: Two Liftings of a Universal Kaprekar Fixed Point* (Clay Elmore, November 2026). Markdown source: [paper_hierarchy.md](paper_hierarchy.md).

The older April 2026 version ([paper.pdf](paper.pdf), 80 pages) is kept for reference; its numbering differs from the current paper.

Work continued after 60714. The paper's final section, "Further directions (November 2026)", and the folder [`audit_2026-11/`](audit_2026-11/) record it: a constant at every length in every base, a check that the sorting step is needed at 4 and 5 digits, and the general problem (choose an endpoint, get a rule with a proof), which is open.

An arXiv preprint and an OEIS entry are planned; neither has been submitted yet.

---

## Try it

**[Open the interactive calculator](60714_calculator.html)**

Type any number 5 to 20 digits long. The calculator shows the full trajectory, step by step, until it reaches 60714 or 0.

---

## What's here

| | |
|---|---|
| **[paper_hierarchy.pdf](paper_hierarchy.pdf)** | The current paper, compiled (November 2026). |
| **[paper_hierarchy.md](paper_hierarchy.md)** | Markdown source of the current paper. |
| **[60714_calculator.html](60714_calculator.html)** | Single-file interactive calculator. Open it in any browser. No setup. |
| **[audit_2026-11/](audit_2026-11/)** | The November 2026 independent recomputation and the work that followed. |
| **[paper.pdf](paper.pdf)** | Older version (April 2026, 80 pages, about 900 KB). Includes Appendix F (April 29, 2026; §F.5 revised April 30, 2026): preliminary working notes on a strengthened *strict-d* criterion. |
| **[paper.md](paper.md)** | Markdown source of the older version. About 250 KB; if GitHub's math renderer struggles with the size, browse the [section files](#the-older-april-2026-version-section-by-section) below. |
| **[paper.tex](paper.tex)** | LaTeX source of the older version. Compiles to `paper.pdf` with `pdflatex`. |
| **[d6_fps.txt](d6_fps.txt)** | All 506 universal fixed points at d = 6, with metadata. |
| **[d7_fps.txt](d7_fps.txt)** | All 18,004 universal full-variable fixed points at d = 7, from the exhaustive Run B classification (Appendix D of the older version). |
| **[d7_summary.txt](d7_summary.txt)** | Human-readable summary of the d=7 classification: per-zero-stratum counts, rule totals, and reproducibility metadata. |
| **[d7_classification.json](d7_classification.json)** | Run B output: full machine-readable d=7 classification (10 MB). |
| **[d7_verified_outcomes.json](d7_verified_outcomes.json)** | Run C output: cross-dimensional outcomes for the two-zero d=6 stratum verified at d=7 (42 MB). |
| **[audit_60714_d7.json](audit_60714_d7.json)**, **[audit_60714_d8.json](audit_60714_d8.json)** | Empirical check of the reaching-time lemma at d=7 and d=8 (older version, §5 Remark). |
| **[README_d7_verifier.md](README_d7_verifier.md)** | Documentation for the d=7 outcome verifier methodology. |
| **[scripts/](scripts/)** | Reproducibility scripts for the exhaustive claims of the older version at $d \leq 6$. |
| **[d7_audit/](d7_audit/)** | Self-contained $d = 7$ verification package: Run B (exhaustive classification), Run C (cross-dimensional outcomes), Run A/A2 (60714 lifting audits at $d = 7, 8$). See `d7_audit/README.md`. |

---

## What 60714 actually is

In Kaprekar's classical routine at d = 4, you sort the digits descending, sort them ascending, subtract, and repeat. From every input that is not one repeated digit, you reach **6174** within seven steps.

The routine has no fixed endpoint at d = 5: Kaprekar's rule falls into one of three cycles instead. That has been the standard story for 77 years.

The story changes if you let the rule itself vary. For each digit length d there are many ways to combine the sorted digits: d! · (d! − 1) ordered permutation pairs, each defining its own iteration rule (each map is counted twice, once per sign). Most produce cycles. A small subset send every input to one fixed point. At d = 6 there are exactly **506** such fixed points among full-variable rules.

The natural follow-up question: which of these fixed points persist across lengths? If F is universal at d, is it also universal at d + 1, under some related rule?

The answer is mostly no. Of the 33 universal fixed points at d = 5 (full-variable rules), only one is universal again at d = 6. That one is **60714**. (If rules that leave a letter in place are allowed, the five-digit count is 54, and 22 of them recur at six digits.)

60714 stays a fixed point at every higher d, with an explicit recipe: each rule is built from the d = 5 or d = 6 rule by appending pairs of coefficients summing to zero at the new digit positions. Theorem 4.1 proves that at d = 5, 6 every input that is not one repeated digit reaches 60714, and that at every d ≥ 7 every input reaches 60714 or 0, with the inputs that reach 0 characterized exactly.

The proof combines complete enumeration at 7 ≤ d ≤ 16 with an algebraic argument that covers all larger d.

---

## The main results of the current paper

| Result | Statement |
|---|---|
| **Theorem 3.2** | Exhaustive census: 0, 4, 33, and 506 universal full-variable fixed points at d = 3, 4, 5, 6 respectively |
| **Theorem 3.3** | Of the 33 fixed points at d = 5, exactly one (60714) is also universal at d = 6 |
| **Theorem 4.1** | 60714 is a fixed point at every d ≥ 5; every input reaches it at d = 5, 6; at d ≥ 7 every input reaches 60714 or 0 |
| **Theorem 4.7** | Padded 6174 has no full-variable fixed-point rule at d = 5, and under the lifting family it never regains universality |
| **Sections 5 to 7** | The repetition direction ({1,4,6,7} written m times): folding results, and why a proof for every m is open |

---

## The older April 2026 version, section by section

For in-browser viewing; sections render cleanly on GitHub. Numbering here is that of the older version.

### Main text

| § | Section | Topic |
|---|---|---|
| 1 | [Introduction](sections/01_introduction.md) | Kaprekar's routine, the cross-dimensional question, the 54 → 60714 discovery arc |
| 2 | [Framework](sections/02_framework.md) | Permutation-pair rules, algebraic rank, native digit length |
| 3 | [Classifications at d ≤ 6](sections/03_classifications.md) | Exhaustive enumeration, Theorems 3.1–3.4 |
| 4 | [Cross-check d = 5 → d = 6](sections/04_cross_check.md) | The 32 dimension-locked fixed points |
| 5 | [The 60714 theorem](sections/05_theorem_60714.md) | The lifting construction and its proof |
| 6 | [The {7,6,4,1} thread](sections/06_thread_7641.md) | 60714 vs 6174 vs 60417 vs 1746 |
| 7 | [Open questions](sections/07_open_questions.md) | Conjectures and directions as of April 2026 |

### Appendices

| | Appendix | Topic |
|---|---|---|
| A | [Classification tables](sections/A_classification_tables.md) | Per-d enumeration data, fixed-point catalogs |
| B | [60714 ladder construction](sections/B_60714_ladder.md) | Explicit coefficient vectors through d = 20 |
| C | [Support lemmas](sections/C_support_lemmas.md) | Core non-negativity, Td closure, the d = 15 algebraic hinge |
| D | [Universal full-variable fps at d = 7](sections/D_dF7_observations.md) | Exhaustive d = 7 classification (18,004 fps) and cross-dimensional outcomes for the two-zero d = 6 stratum |
| E | [6174 audit at d = 8, 9](sections/E_6174_audit.md) | The 45-input escape class |
| F | [Strict-d anchors and the {7,6,4,1}-thread tower](sections/F_strict_d_anchors.md) | Preliminary working notes (April 29, 2026; §F.5 revised April 30, 2026): strict-d criterion, the 11-fp d=7 strict-anchor list |

---

## Reproducibility

The exhaustive claims of the older version have corresponding Python scripts in [`scripts/`](scripts/). Pure Python 3 (≥ 3.8), no external dependencies. The November 2026 recomputation behind the current paper is in [`audit_2026-11/`](audit_2026-11/).

| Script | Reproduces (older version numbering) | Runtime |
|---|---|---|
| [`classify_at_d.py`](scripts/classify_at_d.py) | Theorems 3.1–3.4 | d = 5: ~5 s · d = 6: ~5–10 min |
| [`cross_check_d5_to_d6.py`](scripts/cross_check_d5_to_d6.py) | The d = 5 → 6 cross-check | ~30 min |
| [`verify_60714_ladder.py`](scripts/verify_60714_ladder.py) | Fixed-point equation: K(60714) = 60714 at each d | < 1 s |
| [`verify_60714_basin.py`](scripts/verify_60714_basin.py) | Basin and escape class at small d | d = 7: ~3 s · d = 8: ~30 s · d = 9: ~5 min |
| [`verify_lemma_5_2.py`](scripts/verify_lemma_5_2.py) | Bounded reaching time at low d | ~5 min |
| [`verify_even_ladder_closure.py`](scripts/verify_even_ladder_closure.py) | Lemma C.4: one-step T_d closure on the even ladder at d ≥ 18 | d = 18: ~30 s · d = 20: ~3 min |
| [`verify_case2_recovery.py`](scripts/verify_case2_recovery.py) | Lemma C.10: Case 2 admissibility recovery for d ∈ [7, 30] | ~30 s |
| [`audit_6174_d8_d9.py`](scripts/audit_6174_d8_d9.py) | 6174 lifting audit at d = 8, 9 | d = 8: ~3 min · d = 9: ~60 min |

Run any script with `python3 scripts/<script>.py` and `--help` for options.

To regenerate the [`d6_fps.txt`](d6_fps.txt) supplementary file:

```bash
python3 scripts/classify_at_d.py 6 --save-txt
```

### d = 7 verification

For the d = 7 work in Appendix D of the older version (the exhaustive classification, the cross-dimensional outcome verification, and the empirical check of the reaching-time lemma), see the self-contained [`d7_audit/`](d7_audit/) package. It uses Numba parallel acceleration and supports crash-resume on the longer enumerations.

| Script | Reproduces | Runtime |
|---|---|---|
| [`d7_audit/audit_60714_d7.py`](d7_audit/audit_60714_d7.py) | Reaching-time check at d = 7 | ~3 s |
| [`d7_audit/audit_60714_d8.py`](d7_audit/audit_60714_d8.py) | Reaching-time check at d = 8 | ~3 s |
| [`d7_audit/classify_d7_full.py`](d7_audit/classify_d7_full.py) | Run B: exhaustive d=7 classification (18,004 universal fps) | ~5–30 min |
| [`d7_audit/d7_outcome_verifier.py`](d7_audit/d7_outcome_verifier.py) | Run C: cross-dimensional outcomes for the 53-fp two-zero d=6 stratum | ~1–3 hours |
| [`d7_audit/typeA_validator.py`](d7_audit/typeA_validator.py) | §6.6 Observation 6.3: held-out validation of the Type A LOCK characterization | ~5 min |

---

## How this paper was written

The discovery arc, the classification errors and self-corrections, and the proof gaps and their resolution are documented in §1.4 of the older version. In short: brute-force enumeration produced the empirical landscape, an early candidate (54) turned out to be algebraically degenerate, and the search moved on to 60714.

---

## Citation

```bibtex
@unpublished{elmore2026digits6174,
  author = {Elmore, Clay},
  title  = {The Digits of 6174 at Every Length: Two Liftings of a Universal Kaprekar Fixed Point},
  year   = {2026},
  month  = nov,
  note   = {Unpublished manuscript. https://github.com/clayelmore/Kaprekar-60714}
}
```

## How this was made

The questions and the direction are the author's. The computation, checking, and drafting were done with AI models, Anthropic's Claude and OpenAI's ChatGPT, used as research tools. Every count quoted here was produced by code in this repository and can be re-run. No human mathematician has refereed the results.
