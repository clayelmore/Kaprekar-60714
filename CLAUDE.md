# CLAUDE.md — Kaprekar Research Project

**For the next Claude working in this repo. Read this first.**

This repo holds a research program generalizing Kaprekar's 1949 result (every 4-digit
non-repdigit number reaches **6174** under sort-descending-minus-sort-ascending). The
program extends 6174 along **two orthogonal axes**:

1. **Zero-padding axis** → **60714** is a universal attractor at every digit length d ≥ 5
   under coefficient-preserving lifted rules. *This is the main paper* (`paper.md`, `paper.tex`,
   `paper.pdf`). Status: written, ~71 pages, v1.0+.
2. **Multiplicity-duplication axis** → the multiset **{1,4,6,7}^m** at d = 4m. *This is the
   newer work* (`multiplicity_chain/`). Status: active research, key structural results proven.

Both axes are generalizations of the same d=4 / 6174 base case.

**NEW (2026-06-09):** a third document, PAPER_FIXED_POINT_HIERARCHY.md (repo root), outlines a
planned *structural* paper classifying ALL fixed points by a ladder L0–L5 (degenerate "everything
zeros out" 45/495 → full-variable universal 6174 → dimension-transcendent 60714 and {1,4,6,7}^m).
The multiplicity-chain PROOF program has CONCLUDED as an open problem: existence robustly supported
(witness count exploding), every standard proof route closed, root-caused to the base case having no
low-degree Lyapunov certificate. See multiplicity_chain/PROOF.md final sections.

**NEW (2026-06-22) — the definitive single paper.** `paper_hierarchy.md` / `paper_hierarchy.pdf`
(repo root, 22 pp) is now THE paper: the merge of Paper 1 (the 60714 zero-padding paper, `paper.md`)
with the L0–L5 hierarchy synthesis, re-audited lemma by lemma. This is "the only paper people will
see" — maintain it, not the older drafts, going forward. Two things future-you MUST know:
- **60714 is DEGENERATE, not full-rank.** sv_F(60714) = 4 — its single zero digit drops out of the
  effective rank. FOUR of the 33 d=5 universals are degenerate (54, 3753, 60417, 60714), not two. So
  the line just above ("dimension-transcendent 60714") is misleading: **transcendence (L5) is
  ORTHOGONAL to the L3/L4 rank axis.** 60714 is transcendent-DEGENERATE — its zero is both the
  absorbing engine of its transcendence AND the cause of its rank-deficiency; the duplication chain
  {1,4,6,7}^m is full-rank, conjecturally transcendent. This is now the paper's central unifying point.
- **Proof upgrades over paper.md.** App E.4 (reaching-time projection lemma) now has PROVEN closed
  forms for both branches — w<v: 9(v−w)·10^(d−4); w>v: 9900(w−v), identical on both ladders — closing
  the induction uniformly in d (was enumerate-to-d=30 [S]; reconfirmed afresh to d=401). Lemma 2.4
  (universality criterion) now adjoins the absorbing state 0 so escape orbits register. Abstract/intro
  carry the honest escape-class caveat (60714 is universal off an explicit collapsing escape class for
  d ≥ 7). Bibliography is the 11-ref set (Iwasaki dropped — that's Kaprekar *numbers*, not the *routine*).
  Re-verified arrangement counts live in Computed 5.6 (e.g. m=3 = 46 universal arrangements under the
  repdigit-only convention); the older counts in the table below may use a different exclusion convention.

**NEW (2026-06-23) — proof assault on the dyadic tower (Conjecture 6.6).** Paper now 24 pp with new
§6 material: **Lemma 6.9** (sign of V_j = a two-digit comparison, x[2^j] vs x[2^(j+1)]; incoherence =
critical plateau — both PROVEN for all levels), **Prop 6.10** (coherence entry within 3 steps, PROVEN
at tower levels 1–2 via abstract gap families, sharp), **Theorem 6.11** (return-map reduction — NB the
OLD Open Problem 7.2 claim "(E)+(F) imply 6.6" had a genuine hole (mixed cycles); the return-map
quotient T̂ repairs it), **Computed 6.12** (T̂ funnels on ALL pairs at levels 1–2, exits included).
Conjecture 6.6 remains OPEN: what's left is (E′) uniform in level (evidence: bound 3 holds at level 3,
60k constructed plateau states) and (F̂) for j≥3 (pair systems outgrow enumeration; 4 natural
monovariants fail; gap-certificates provably can't climb — window-dependence negative, 921/1710 mixed).
Reproduce everything: `python3 multiplicity_chain/session_2026-06-23/verify_tower.py` (ALL CHECKS PASS).

---

## How to use the session log (the practice that keeps this project coherent)

`SESSION_LOG.md` (in this repo) is a running log of what each Claude chat actually did, so the
next chat starts informed instead of guessing. Rules:

1. **Read the Current State block first** — canonical truth as of the last session. If older
   entries contradict it, Current State wins.
2. **Read the most recent 1–2 entries** for recent context.
3. **Skim back further only if** the user references something older.
4. **At session end**, write a new entry at the top (template in the file) and update Current
   State if anything material changed.
5. **Always list "Files produced this session"** with paths and one-line descriptions.

If you've made changes future-you would need to know about, propose updating the log before the
chat ends, even if not asked.

---

## Current State (as of 2026-06-15)

### Two-axis structure
- **60714 paper** (zero-padding axis): complete. See `paper.md`. Don't disturb unless asked.
- **Multiplicity chain** ({1,4,6,7}^m): see `multiplicity_chain/PROOF.md` for the math.

### Multiplicity-chain results (verified)
Classical universal fixed points on {1,4,6,7}^m at d=4m:

| m | d | universals | note |
|---:|---:|---|---|
| 1 | 4 | 2 | classical 6174, 1746 |
| 2 | 8 | 481 | |
| 3 | 12 | 42 | 14-day exhaustive run |
| 4 | 16 | 341 | pair-symmetric structured search |
| 5 | 20 | ≥2 | F=17461746146174617746, F=14617461774617461746 |
| 6 | 24 | ≥1 | F=666174141466617777741414 |
| 7 | 28 | ≥1 | F=6174×7 — EVIDENCE (candidate-1; see m7_witness.json) |

### Multiplicity-chain results (proven)
- **Theorem 1**: "6174" repeated m times is a fixed point of an explicit (interleaved
  pair-symmetric) rule at every d=4m. Clean algebra. BUT it is the *cheat* — a lift of the
  d=4 solution, not universal for m≥3 (dynamically isolated).
- **Lemma A** (finiteness): For any rule, F is universal ⟺ F is the unique fixed point AND
  the dynamics is acyclic (no cycles of period ≥2). Fully proven.
- **Lemma A is the only valid decomposition**: universal ⟺ unique-fp ∧ acyclic. (An earlier
  shortcut "for monotone rules, universal ⟺ acyclic" is INVALID because Fact B is false —
  monotone gives neither unique-fp nor acyclic for free.) Monotone = cumulative sums C_j ≥ 0
  (classical Kaprekar d=4 has it). All period-≥2 cycles live outside the {1,4,6,7} alphabet.
- **Fact B is FALSE** (corrected 2026-06-04): monotone does NOT imply unique fixed point (interleaved d=12 rule has 2 fps). The decomposition needs Lemma As unique-fp condition, which monotonicity does not provide. See PROOF.md multi-agent assault section.

### The central open problem (sharp form)
> For every m ≥ 1, does there exist a pair-symmetric, **monotone**, {1,4,6,7}^m-preserving rule
> with **no nontrivial cycle**?

Monotonicity is free (even classical Kaprekar has it); the crux is **acyclicity + unique-fp**
(Lemma A). Block construction (=classical Kaprekar on block states) is monotone but cyclic on
non-block states; interleaved is monotone but has multiple fixed points AND cycles. The 15
universal d=16 rules are not block-closed (identical 180-state escape set). Ruled out: modular
tower, low-degree Lyapunov, all uniform families. Lead: the obstruction is a finite,
alphabet-external cycle family expressible as linear constraints on c; T_m is bounded (14,32,39,42).
See PROOF.md 'Multi-Agent Proof Assault' for the full, adversarially-verified state.

### Update 2026-06-15 — clean-repeat map, m=3 dissection, no clean pattern
Keep two questions distinct:
- **Main conjecture**: does *some* arrangement of {1,4,6,7}^m universalize? (table above — proven m≤4, evidence m=5,6,7).
- **Clean-repeat question**: is the *tidy* "6174 repeated m times" itself universal? Arrangement/m-dependent: **m=1,2,4 YES (proven, full enum); m=3 NO (proven — best rule 99.98%; the universal m=3 arrangements are SCRAMBLED, e.g. 666141417774); m=5,6,7 yes (EVIDENCE, under non-obvious within-block-scrambled rules).** So "6174 repeated" is NOT automatically universal — m=3 is the unique m≤7 where the tidy repeat fails.
- **Why m=3 fails / the dissection**: the obstruction is the {4,5,9}-"shadow" family (relatives of 549945 / the 4995/5355 cycle). Across 24 near-universal clean-6174×3 rules it is a MIX — ~6 distinct period-1 fixed points + ~17 distinct period-3 cycles. No single rival, form, or period.
- **DEBUNKED this session (do NOT revive):** "m=3 has one parasitic fixed point"; "1,2,4,7 = lazy-caterer sequence"; "shadow scales with a fixed 4-digit-block alphabet"; "one stable rival"; "m=3 rival is uniquely a fixed point." All died under m=5,6 / multi-rule testing.
- **Stable facts:** obstructions always decompose into 4-DIGIT BLOCKS; the rival is always the {4,5,9}-shadow FAMILY. Below the family nothing is stable — consistent with the certificate-cost theorem (no compressible reason). m=3's 0%-universal-rule rate vs m=4's ~6% appears to be arithmetic happenstance at d=12, not a law.
- **Method caution:** the alphabet test is NECESSARY-NOT-SUFFICIENT — at m=3, 24 alphabet-clean rules ALL leak on full enumeration. The m=5,6,7 "evidence" rests on the general sample, not the alphabet test.
See `multiplicity_chain/PROOF.md` (2026-06-15 entry) and `multiplicity_chain/session_2026-06-15/` for scripts.

### Key method note
At d ≥ 20, universal-witnessing rules are far too rare for F-first random search (~10⁻⁸/sample);
you CANNOT verify a guessed F by sampling its rules. Use the **forward** pair-symmetric search
(sample partitions → construct rule → check F's multiset → classify). Memory: the basin list at
d=28 (~124M multisets) exceeds a 16 GB machine — run d≥28 on a bigger box or stream the basin.

### Tooling
- `scripts/search_multiset_universals_fast.py` — the core search engine (shared by both axes).
- `multiplicity_chain/` — PROOF.md (math), THEORY_AND_RULES.md (construction + predictions),
  CAMPAIGN_FINDINGS.md (the search campaign), data/ (verified universal rules as JSON).

### Conventions
- Commit messages end with the Claude co-author trailer.
- Don't commit `*_log.txt`, `*.output`, `__pycache__/` (see .gitignore).
- The local running session logs `SESSION_LOG-*.md` historically lived in `~/Downloads/`;
  going forward, the canonical one lives in this repo as `SESSION_LOG.md`.
