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

## Current State (as of 2026-06-03)

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

### Multiplicity-chain results (proven)
- **Theorem 1**: "6174" repeated m times is a fixed point of an explicit (interleaved
  pair-symmetric) rule at every d=4m. Clean algebra. BUT it is the *cheat* — a lift of the
  d=4 solution, not universal for m≥3 (dynamically isolated).
- **Lemma A** (finiteness): For any rule, F is universal ⟺ F is the unique fixed point AND
  the dynamics is acyclic (no cycles of period ≥2). Fully proven.
- **The decomposition** (verified d=12, d=16, zero exceptions): for *monotone* pair-symmetric
  rules, **Universal ⟺ Acyclic**. "Monotone" = cumulative coefficient sums C_j = c_0+…+c_j ≥ 0
  (a non-negative lattice path; classical Kaprekar d=4 has it). "Acyclic" = the *same*
  obstruction that makes Kaprekar d=4 work and d=5 fail.
- **Fact B** (verified, full 2M-multiset scan): monotone ⟹ unique fixed point.

### The central open problem (sharp form)
> For every m ≥ 1, does there exist a pair-symmetric, **monotone**, {1,4,6,7}^m-preserving rule
> with **no nontrivial cycle**?

By Lemma A + Fact B this is *equivalent* to "a universal exists at every m." Monotonicity is
free (even classical Kaprekar has it); the crux is acyclicity. The block construction
(=classical Kaprekar) is monotone but changes the multiset; the interleaved construction is
monotone + multiset-preserving but cyclic for m≥3. The 15 rules that satisfy all three at d=16
are scrambled with no known closed form → the existence proof is likely **non-constructive**.

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
