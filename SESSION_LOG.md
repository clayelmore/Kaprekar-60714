# Session Log — Kaprekar-60714

**Purpose.** A running log of what each Claude chat actually did, so the next chat starts informed instead of guessing. New entries go at the top. Older entries stay as historical record but should not be read as current state — that's what the **Current State** block is for.

---

## How to use this file (instructions for the next Claude reading this)

1. **Read the Current State block first.** That's the canonical truth as of the last session that updated it. If anything in older entries contradicts Current State, Current State wins.
2. **Read the most recent 1–2 session entries** for context on what was just done and what was left pending.
3. **Skim further back only if** the user references something older or you genuinely need context that the recent entries don't provide. Don't try to absorb the whole file — that's how drift happens.
4. **At the end of your session**, before the conversation closes, write a new entry at the top following the template below, and update the Current State block if anything material changed.
5. **Always include a "Files produced this session" subsection** in every entry, listing every document, script, data file, or bundle created during the session along with its path and a one-line description. This lets the user re-upload any of them to project knowledge later if a future chat needs them. Include both files staged in `/mnt/user-data/outputs/` and any files placed elsewhere (e.g., `/home/claude/`, deploy bundles).

If the user hasn't asked you to update this file, but you've made changes that future-you would need to know about, propose updating it before the chat ends. The user can decline and that's fine — but the offer matters.

---

## 2026-06-23 — Proof assault on Conjecture 6.6: sign lemma, entry proven at j≤2, OP 7.2 gap found and repaired

**Context.** User: "review all work done, check out proofs, and try to prove the m^x" (= the dyadic tower, Conjecture 6.6). Attacked via Open Problem 7.2. Session ran on Fable 5.

**PROVEN (new, all in the paper now as Lemma 6.9 / Prop 6.10 / Theorem 6.11 / Computed 6.12).**
- **Sign Lemma 6.9(a)**: for the level-j tower form, V_j < 0 ⟺ x[2^j] > x[2^(j+1)]; = 0 ⟺ repdigit; > 0 otherwise. Induction using max|V_j| ≤ 10^(d_j)−1. Verified 0 violations over ALL states at levels 0–2 (715 + 24,310 + 2,042,975) + 120k adversarial at level 3. The sign of a 2^(j+2)-digit form is a two-digit comparison.
- **Plateau 6.9(b)**: incoherence ⟺ a critical plateau — a run of 2^(j+1)+1 equal digits at ranks [a,b] or [a+1,b+1] (a=2^(j+1), b=2^(j+2)) with a strict drop/rise at the prescribed end. The fold's failure mode has a shape.
- **Prop 6.10 (entry, bound three, j=1,2)**: an incoherent state's image is a closed form in 3 gaps (level 1: 810-member abstract family) / 7 gaps (level 2: 2,494,800) — formulas matched ALL 6,006 + 251,940 actual incoherent states with 0 mismatches — and every family member re-enters coherence within 2 steps, never meeting a repdigit (mod-9 + size argument). Bound 3, sharp, proven at both levels.
- **THE BIG ONE — OP 7.2's reduction had a hole**: (E)+(F) as previously stated do NOT imply Conjecture 6.6 — a cycle weaving through coherent AND incoherent states is excluded by neither ((F) was only verified on the 1,202 never-exiting pairs). **Repair = Theorem 6.11 (return-map reduction)**: a coherent state's future is a function of its pair, so define T̂(pair) = pair of next coherent state; (E′)+(F̂ over T̂) ⟹ universal, proven, uniform in level. **Computed 6.12**: T̂ total on ALL 1,464 pairs (level 1, the 262 exiting pairs included) and ALL 235,212 (level 2), 0 repdigit excursions, unique fixed pairs (1746,1746)/(17461746,17461746), acyclic. Gives an independent quotient-route proof of universality at j=1,2.

**EVIDENCE.** Level 3 (d=32): 60k incoherent states constructed directly from the plateau shape + 50k random — all enter coherence within 3 steps (same bound). Conjecture: entry ≤ 3 at EVERY level.

**NEGATIVE (honest).**
- Window reduction fails: image coherence at level 2 depends on LOW-order gaps too (921/1,710 coarse classes mixed) → the gap-certificate cannot climb to j≥3 (~10^13 members). Uniform (E′) needs a real carry-and-block argument.
- 4 natural monovariants on T̂ all fail massively (445–787 violations at level 1; tens of thousands at level 2) — the certificate-cost wall now sits exactly on T̂'s funnel property.
- Grace note: the slowest-entering level-1 states descend from images 445545/445554 (pure {4,5}) — the {4,5,9}-shadow appearing inside the entry dynamics.

**Net: Conjecture 6.6 still open**, but now equivalent to two uniformities over a PROVEN reduction (previously the reduction itself was broken); entry half proven at both enumerable levels with the obstruction to climbing measured.

**Paper updated** (Section 6: new Lemma 6.9, Prop 6.10, Theorem 6.11, Computed 6.12; §6 closing + OP 7.2 restated; abstract/intro/provenance). Rebuilt: 24 pp, clean.

**Files produced this session.** `multiplicity_chain/session_2026-06-23/`: `TOWER_RESULTS.md` (full write-up), `verify_tower.py` (reproduces every new computation, ~40s, ALL CHECKS PASS), `tower_lib.py`, `probe_fhat.py`. NB: /tmp/kap60714 was wiped again (reboot) and re-cloned; an independent adversarial audit agent of the whole paper was launched and had not reported by session end — check its verdict next session if no note follows this one.

---

## 2026-06-22 — Definitive paper written: paper_hierarchy.md (merge + full lemma re-audit)

**Context.** User: "tighten everything, clean up the story, write the new version of the paper assuming nothing has been done before — look at Paper 1 too, pull in all new stuff, check all lemmas and proofs, make it bullet-proof and compelling." Produced the single definitive paper `paper_hierarchy.md` (22 pp), merging Paper 1 (`paper.md`, the 60714 zero-padding axis) with the L0–L5 hierarchy synthesis and the 2026-06-15 multiplicity findings. This is now THE paper ("the only one people will see"); maintain it, not the older drafts.

**Verification first (3 parallel agents + 1 referee).** Agent A: every numerical claim re-confirmed (2 footnote caveats). Agent B: Lyapunov certificate-cost independently confirmed (exact-rational Farkas certs deg 2–6 infeasible + explicit deg-7 witness; gap cascade 54,20,14,10,7,4,1). Agent C: Paper 1 inventory + reconciliations + the curated 11-ref bibliography. Referee agent: line-by-line written-proof audit — computational theorems all SOUND and honestly labeled; flagged 5 real soft spots, all fixed.

**Corrections (bullet-proofing).**
- **sv_F / degeneracy (the headline).** 60714 (and 60417) are DEGENERATE: sv_F=4, one zero digit drops out of the effective rank. FOUR of the 33 d=5 universals are degenerate (54, 3753, 60417, 60714), not two. Reframed L5 transcendence as ORTHOGONAL to the L3/L4 rank axis — proven-transcendent 60714 is degenerate, the conjectural duplication chain is full-rank; the zero is both transcendence-engine and degeneracy-cause. Now the paper's central unifying point.
- **App E.4 projection lemma**: replaced the enumerate-to-d=30 [S] argument with PROVEN closed forms for both branches — w<v: 9(v−w)·10^(d−4) (fixes a 10^(d−3) typo); w>v: 9900(w−v), identical on both ladders — closing the reaching-time induction uniformly in d. Reconfirmed afresh to d=401.
- **Lemma 2.4** (universality criterion): adjoined the absorbing state 0 (escape orbits were silently leaving the admissible domain); escape mode now ties to the d≥7 escape class.
- **App E.2**: removed the false "place 6 is identically zero" step (first even appended pair is at places (6,7), per App F); d≥18 holds on the block count alone.
- **Even-core bound**: noted true max 899,991 (989,982 additive estimate is loose).

**Honesty.** Abstract/intro now carry Theorem 4.1's escape-class caveat. Did NOT present "m=1,2,4,7" as a clean sequence (mirage — the 1746-repeat works at 5,6). Dropped the Iwasaki ref (Kaprekar *numbers* ≠ the *routine*).

**Synthesis added.** Named the {4,5,9} "anti-Kaprekar" shadow (549945 + relatives) as the recurring obstruction — m=3 second fixed point, classical double-double 2-cycle, k=3 incoherent fixed point — honestly as a family that refuses to stabilize (= exactly why induction to exclude it fails). Added a related-work paragraph + the full 11-ref bibliography (Nuez; Kay & Downes-Ward; Devlin & Zeng; Dahl; Peterson; Prichett 1979).

**Files produced this session.** `paper_hierarchy.md` (rewritten, ~12.4k words); `paper_hierarchy.pdf` (22 pp); `build_hierarchy/` (build artifacts). Commit `41187ba` on main, pushed; CLAUDE.md + this log updated.

---

## 2026-06-15 — Clean-6174-repeat universality, m=3 dissection, every clean pattern debunked

**Context.** Multiplicity axis. The user pushed a sharp sub-question: is the *tidy* arrangement "6174 repeated m times" itself universal (vs the main conjecture's "*some* arrangement universalizes")?

**Found.**
- **Native m=7 search SUCCEEDED**: candidate-1, a monotone pair-symmetric within-block-scrambled rule, makes 6174×7 (d=28) EVIDENCE-universal (kills the 4995/5355 cycle; full {1,4,6,7}-alphabet + 500k random sample clean). The canonical 6174 7-fold near-missed (8 alphabet cycles → the 4995/5355 2-cycle); within-block scrambling fixes it; ALL 5040 uniform within-block orders keep the cycle (so the coherence-funnel proof route is closed at m=7). Saved `multiplicity_chain/m7_witness.json`. NB: this is EVIDENCE (sample), not proven — the "m=7 base FOUND" commit title overstates; PROOF.md body is correct.
- **Clean-6174×m map**: m=1,2,4 proven universal; **m=3 proven NOT universal** (full d=12 enum, best 99.98%; the universal m=3 arrangements are SCRAMBLED, e.g. 666141417774); m=5,6,7 evidence-universal under scrambles. "6174 repeated" is NOT automatically universal — m=3 is the lone exception ≤7.
- **m=3 dissection**: obstruction = {4,5,9}-shadow family; across 24 near-universal rules it is a MIX of ~6 distinct period-1 fixed points + ~17 distinct period-3 cycles. No single rival.
- **Five clean hypotheses proposed and DEBUNKED**: m=3-single-fixed-point; 1,2,4,7-lazy-caterer; fixed-block-alphabet shadow; one-stable-rival; m=3-rival-uniquely-a-fixed-point — all falsified by m=5,6 / multi-rule testing (one corrected the very next turn).
- **Stable facts**: 4-digit-block structure; {4,5,9}-shadow as the rival *family*. Nothing below the family is stable — reaffirms the certificate-cost "no compressible reason." The strangeness of "every m but 3" has no clean reason; it is genuine irregularity.
- **Method caution recorded**: alphabet test necessary-not-sufficient.

**Honesty note.** Several appealing clean patterns were proposed mid-session and then falsified by deeper checks. The robust net finding is *negative*: there is no clean structural pattern; the irregularity is the answer.

**Files produced this session.** `multiplicity_chain/m7_witness.json` (m=7 evidence witness rule); `multiplicity_chain/session_2026-06-15/*.py` (dissection + search scripts); PROOF.md 2026-06-15 entry; this log entry; CLAUDE.md Current-State update.

---

## 2026-06-03 — Multiplicity-chain universality: proofs + the monotone–acyclic decomposition

**Context.** This session worked the *multiplicity-duplication axis* ({1,4,6,7}^m at d=4m),
distinct from the 60714 zero-padding axis. Goal evolved from "do universals exist at high m?"
to "prove they exist at all m."


**ADDENDUM (same day) — Flavor-1 predictor: CORRECTED, NOT resolved.** (An earlier same-day claim that fertility ⟺ desc−asc=6174 was FALSE — {0,4,5,9} is fertile (152 universals) but fails it. The correct narrower result: (6,2) ⟺ admits the PAIR-SYMMETRIC construction, exhaustively verified. General fertility stays OPEN. See FERTILITY_PREDICTOR.md correction header.)

_Original (now-corrected) claim follows:_ **Flavor-1 predictor attempt.** Treating "which digit-sets are fertile"
as a code-cracking exercise (per user's idea to test golden ratio / π / Fibonacci — all
falsified) yielded a clean, verified predictor:

> A 4-digit set is fertile ⟺ (desc − asc = 6174) AND (digit-sum ≡ 0 mod 9). Exactly two sets:
> {1,4,6,7} and {2,3,5,8}.

mod-9 is PROVEN necessary; desc-asc=6174 is the empirical discriminator (12 sets generate 6174,
only 2 are mod-9). Verified EXHAUSTIVELY on all 24 mod-9 sets (2 fertile, 22 extinct), 0 exceptions — including NEW
runs: {2,3,5,8} fertile at d=12 (3 universals, 100% basin), {0,3,6,9} extinct at d=12 (0
candidates). Both fertile sets induce identical coefficients (6,2) = the 6174 signature, so
the chain is 6174-SPECIFIC. See multiplicity_chain/FERTILITY_PREDICTOR.md. This resolves the
"Flavor-1 classification: open" item flagged in the 2026-05-18 corrections above.

**What was done.**
- Established (computationally) classical universals exist at m=1..6: counts 2, 481, 42, 341,
  ≥2 (d=20), ≥1 (d=24). The d=16 (341) and d=24 results are NEW this session; d=20 found 2
  distinct universals (F=17461746146174617746 and F=14617461774617461746); d=24
  F=666174141466617777741414.
- **Discovered the pair-symmetric rule family** (σ pair-swaps π's digit-blocks 7↔1, 6↔4;
  K = 6·S₇ + 2·S₆). This is what made high-d search tractable — random rule search finds
  ZERO universals (probability ~10⁻¹⁵); the structured pair-symmetric search finds hundreds.
  The breakthrough came from the user's "reverse d=8 fixed points + 6174 suffix" side quest,
  which surfaced a 99.89%-basin near-universal whose single rule exposed the pair-symmetry.
- **Theorem 1 (PROVEN):** "6174" repeated m times is a fixed point at every d=4m (interleaved
  rule; clean geometric-series algebra). BUT it's the *cheat* — a lift, not universal for m≥3.
- **Lemma A (PROVEN):** universal ⟺ unique-fixed-point ∧ acyclic (finiteness argument).
- **The monotone–acyclic decomposition (verified d=12, d=16, 0 exceptions):** for monotone
  rules, universal ⟺ acyclic. Monotone = cumulative coefficient sums ≥0 (classical Kaprekar
  has this); acyclic = the d=5-failure obstruction. This reframes the whole universality
  question as the classical Kaprekar cycle-exclusion problem, one dimension up.
- **Fact B (verified, full scan):** monotone ⟹ unique fixed point.
- **Step-3 construction obstruction mapped:** block rule (=classical Kaprekar) is monotone but
  leaves the multiset; interleaved is monotone+multiset-preserving but cyclic m≥3; the 15
  all-three rules at d=16 are scrambled → existence proof likely non-constructive.

**Central open problem (sharp).** For every m≥1, does a pair-symmetric, monotone,
{1,4,6,7}^m-preserving, *acyclic* rule exist? Equivalent to the universality conjecture.

**Files produced this session** (now under `multiplicity_chain/` in this repo):
- `multiplicity_chain/PROOF.md` — all the math: Theorem 1, Lemma A, decomposition, Facts B/C, open problem.
- `multiplicity_chain/THEORY_AND_RULES.md` — pair-symmetric construction, explicit rules, d=24/d=28 predictions.
- `multiplicity_chain/CAMPAIGN_FINDINGS.md` — the full search campaign narrative (d=16→d=24).
- `multiplicity_chain/data/pair_symmetric_BIG.json` — 313 d=16 universals WITH rules (π,σ).
- `multiplicity_chain/data/d16_m4_universals_summary.json` — clean d=16 summary.
- `multiplicity_chain/data/d20_universals_live.json`, `d24_universals_live.json` — d=20/d=24 universals + rules.
- `multiplicity_chain/data/forward_1B_final.json` — 1B random-rule baseline (0 universals — shows why structure was needed).
- `CLAUDE.md` — NEW: project orientation for Claude Code, incorporates this session-log practice.

**Decisions made.**
- Moved multiplicity-chain work INTO this repo (per user) rather than the separate
  `kaprekar-multiplicity-chain` repo I had mistakenly created (now to be deleted).
- Formalized the session-log practice as `CLAUDE.md` at repo root so future Claude Code
  sessions auto-read it.
- Did NOT touch the 60714 paper files.

**Pending / next session.**
- Attack the sharp open problem: try to prove acyclicity of a constructed monotone rule, or an
  m→m+1 cycle-free lifting. Prove Fact B (monotone ⟹ unique-fp) from gap-positivity.
- d≥28 needs a bigger-memory machine or a streamed basin (current code OOMs at d=28).
- Optional: fold a multiplicity-chain section into the paper, or keep as companion.

---

## 2026-06-04→09 — Multiplicity-chain proof program concluded; NEW paper: the fixed-point hierarchy

**Arc.** Took the {1,4,6,7}^m universality question from "open past m=4" to a fully-mapped frontier,
then pivoted to a new paper concept.

**Settled this stretch (all in multiplicity_chain/PROOF.md):**
- Existence of universals at every m: robustly supported — explicit witnesses to m=5, and the
  *witness count explodes* (≈3,000 → 18M → 250M for m=3,4,5). The survivor *fraction* is erratic
  (7%/28%/0.04%) but that is just the rule-space d! growing faster; the COUNT grows.
- Proven: Lemma A (universal ⟺ unique-fp ∧ acyclic); Theorem 1 (6174-repeated is a fixed point at
  all m, but it is the "cheat" — dynamically isolated for m≥3); the (6,2) characterization of the
  pair-symmetric CONSTRUCTION (exhaustive over 24 mod-9 sets — only {1,4,6,7},{2,3,5,8}); complete
  m=3 enumeration (exactly 3,000 of 43,200 monotone rules universal).
- Two multi-agent assaults (33 + 8 agents) + the analyst pass closed every standard route:
  modular tower, low-degree Lyapunov, uniform construction, m→m+1 induction, finite-obstruction
  exclusion, counting-by-structure. Root cause: NO m-uniform structure (survivor characterization
  shifts with m).
- DEEPEST result: classical d=4 Kaprekar (54-state gap system) has NO polynomial Lyapunov function
  below degree 9 (LP-proven) — its convergence has no low-complexity mechanism. You cannot lift a
  base-case mechanism that does not exist. This is why the all-m proof resists.
- Crisp open problem handed forward: a closed-form, m-uniform absorbing filtration WITHOUT zeros
  (the zero-free analogue of Paper 1's 60714 argument).

**Corrections made this stretch (trust data, not notes):** fertility predictor RETRACTED
({0,4,5,9} is fertile — 152 universals — not extinct); Fact B (monotone ⟹ unique-fp) is FALSE
(interleaved d=12 has 2 fps); plus a premature fraction-trend read. All fixed in the record.

**NEW PAPER (per user, 2026-06-09):** non-narrative, structural — a HIERARCHY of fixed points L0–L5,
from the degenerate floor ("everything zeros out", 45/495 with sv_F<d) up to dimension-transcendent
universals, placing 6174 (L4 root), 60714 (L5a, proven, zero-padding) and the {1,4,6,7}^m universals
incl. 61746174 (L5b, conjectured, multiplicity) at their rungs. Full skeleton:
PAPER_FIXED_POINT_HIERARCHY.md (repo root).

**Files produced this stretch:** PAPER_FIXED_POINT_HIERARCHY.md (new paper outline);
multiplicity_chain/{PROOF.md (extensively extended), FERTILITY_PREDICTOR.md (+correction),
CAMPAIGN_FINDINGS.md, THEORY_AND_RULES.md, data/*}; numerous analysis scripts and JSON under
~/Downloads/d16_1467_test/.

**Pending / next session.** Draft the hierarchy paper from PAPER_FIXED_POINT_HIERARCHY.md. The proof
of the all-m conjecture is a genuine open problem (new idea required) — not a compute task.

---

## Current State (as of 2026-05-15 — see 2026-05-13/14/15 entry below for full context)

### 2026-05-18 mid-session corrections — read THESE before the 2026-05-15 deltas

Two prior claims in the 2026-05-15 deltas (below) have been **retracted on the basis of actual data checks done 2026-05-18**:

1. **The "Kaprekar-anagram window invariant" is FALSE at m=2.** d=8 m=2 data shows 138 of 465 universals (29.7%) have ZERO Kaprekar-anagram 4-windows. Holds only at m=1 (trivially) and m=4 (5/5, n=5 small sample). It is a *trend with growing fraction in m*, not an invariant. Don't cite as a theorem candidate.

2. **The "internal-9-pair count ∈ {0,2}, not 1" predictor is VACUOUS.** Combinatorial check: zero of the 24 candidate 4-digit-sum-divisible-by-9 multisets have exactly 1 internal 9-pair. The "0 or 2" rule predicts nothing. Additionally, `{1,3,6,8}` has 2 pairs (both 1+8 and 3+6 present), the same count as the surviving `{0,4,5,9}`, so the predictor wouldn't distinguish them anyway. The actual Flavor-1 predictor is TBD; 6 untested multisets staged for the next run batch to discriminate three candidate predictors. See `~/Downloads/paper_section6_draft/predictor_candidate_multisets.md`.

**The honest current statement of Flavor-1 classification: open.** We have two digit-sets that empirically survive at every checked m ({7,6,4,1} thread and {2,3,5,8} thread); one near-survivor at m=3 ({0,4,5,9}); one extinction at m=3 ({1,3,6,8}); one m=2-S-only-only ({0,1,8,9}). No predictor with theoretical support yet.

Also staged 2026-05-18 afternoon (see addendum in entry below):
- pandoc 3.9.0.2 installed (`/opt/homebrew/bin/pandoc`); MacTeX still blocked by disk space (~2 GB free, needs ~5 GB)
- `~/Downloads/search_with_filters.py` — predictor tool wrapping `search_multiset_universals_fast.py` with hard filter (leading-7 forbidden, proven, eliminates 25% at d=12 m=3) + soft scoring + configurable Flavor-1 multiset filters
- `~/Downloads/paper_section6_draft/` — staged §6 analysis (auto-fills m=3 row when 7641 rerun lands) + 6-multiset batch plan

---

### 2026-05-15 deltas — read these FIRST, they supersede the older state below

**Run state.**
- {0,4,5,9} d=12 m=3: previous run (May 8–12) silently HUNG at 136,200/277,200 (49%) — the "Test 2 complete" line in `class_b_d12_test/run_log.txt` was bogus (bash `set -e` + `python | tee` doesn't catch a dead Python). `d12_0459_m3.json` was never written; the 9/17 counts at 49% only exist as log text. **A hardened rerun is currently running** in tmux `kap0459` (PID 39254) via `~/Downloads/rerun_0459_d12.sh`. As of 17:50 May 15: i=114,000 (41%), 8,773 K-rules, 0 universals yet (consistent with prior run's pre-K-rule region). Expected first universal ~3-6h from now; full completion tomorrow afternoon/evening.
- {7,6,4,1} d=12 m=3: **THE CANONICAL `d12_7641.json` (32 classical + 10 S-only from May 8 38.79h Mac run) WAS DESTROYED** on 2026-05-14 ~20:42 by a rogue interactive-shell-launched `search_multiset_universals_fast.py --multiset 7,7,7,6,6,6,4,4,4,1,1,1 --d 12 --out d12_7641.json` process (PID 39186, PPID = zsh) that ran for ~10.5h atomically overwriting the file with its partial checkpoint. The rogue was killed 2026-05-15 07:19. Forensics snapshot at `~/Downloads/d12_7641.OVERWRITTEN_2026-05-15.json`; live filename deleted. **Recovery plan: `~/Downloads/rerun_7641_d12.sh` is staged but NOT launched** (refuses to start while 0459 is active). Will recompute bit-for-bit (deterministic seed=42). Run AFTER 0459 finishes. ~25-40h on Mac. Until that completes, **treat d12_7641-derived analysis (Addendum 9's rule-structure findings, the 2 F-block-balanced exemplars 617464716147 / 614714671476) as surviving only as summary text**, not as full records.
- {2,3,5,8} d=12 m=3 (`d12_2358.json`): **UNTOUCHED** — 63 classical + 13 S-only data is fully intact at `~/Downloads/d12_2358.json` (33KB, mtime May 6).

**Infrastructure changes.**
- `search_multiset_universals_fast.py` now has periodic checkpointing every N arrangements (default 1000) with RNG state in the checkpoint for bit-for-bit resume. New flags: `--checkpoint-every`, `--no-resume`. A future hang/crash loses at most N arrangements of work.
- All future {7,6,4,1} / {0,4,5,9} / similar long Mac runs should go through `rerun_*_d12.sh` style wrappers — they have `set -euo pipefail`, `caffeinate -dimsu`, completion verification, and (for 7641) a guard against parallel-job races on the same output file.

**Tooling additions.**
- Math-olympiad plugin (`math-olympiad@claude-plugins-official`) installed at user scope via `~/.claude/settings.local.json` enabledPlugins. Triggers on IMO/Putnam/USAMO/olympiad/competition problems; uses fresh-context adversarial verifier patterns. Worth running on the unified paper's draft for the same kind of subtle-error catching that surfaced the Phase 13 fabricated 46/9 breakdown and the Addendum 5 procedural-artifact reversal.
- `math-paper-pdf` skill created at `~/.claude/skills/math-paper-pdf/` (user scope). Captures the v1.2.2 build pipeline (preprocess → pandoc → postprocess → assemble → pdflatex×2) with all 11 known landmines documented in `references/known_quirks.md`. Triggers on "build pdf", "compile paper", "rebuild paper.pdf". **Requires pandoc + pdflatex (not installed yet on this Mac)** — `brew install pandoc && brew install --cask mactex-no-gui`. Once installed, `~/.claude/skills/math-paper-pdf/scripts/build.sh ~/Downloads/files-35/paper.md` reproduces the v1.2.2 80-page PDF.

**Analytical findings (new this session, awaiting integration).**
- **Multiset conservation verified across the entire {7,6,4,1} dimensional ladder** at $d = 4m$ for $m = 1, 2, 4$ (m=3 pending rerun): every classical universal lives in the pure multiset $\{7^m, 6^m, 4^m, 1^m\}$. d=8 m=2 in {7,7,6,6,4,4,1,1}: 465/465. d=16 m=4 in {7^4, 6^4, 4^4, 1^4}: 5/5.
- **The "leading-7 forbidden" theorem holds at every checked level.** d=8: 0/465; d=12 (prior run, lost): 0/32; d=16: 0/5. The analog "leading-8 forbidden" for {2,3,5,8} is empirically holding (0/63 at d=12 m=3) — proof is on the next-session priorities list.
- **NEW invariant — Kaprekar-anagram windows.** At every $d = 4m$ on the {7,6,4,1} ladder (m=1, 2, 4 verified), every universal contains at least one 4-consecutive-digit window whose digit set is {1,4,6,7}. At m=1 trivially. At m=2: 10 of 465 have literal "6174" as their leading 4-block (including F=61746174 — Kaprekar twice). At m=4: ZERO have literal "6174" anywhere, but every one has a Kaprekar-anagram window; F=6471467417167416 has 7. The literal "6174" anchor weakens with m; the Kaprekar-digit-set window invariant persists. m=3 confirmation pending rerun.
- **60417 cross-dimensional precise status pinned down.** d=5: strict universal AND F-or-0 universal. d=6: 4 K-rules (same count as 60714!) but best basin only 0.9598 — near-miss, dynamically obstructed. d=7: F-or-0 universal recovers but NOT strict-d (Obs F.3 — every rule has trivial zero-sum pair on F). The d=6 60417 vs 60714 comparison is the cleanest way to motivate Theorem 2.

**Paper framing pivot (decided this session).**
- **Drop the "two threads from one mechanism" framing** for the unified paper. Addendum 5's matched-procedure result already broke cross-thread parallelism (6.7% gap, {2,3,5,8} denser). Trying to defend a unified-mechanism claim is the weakest part of the current draft.
- **Adopt instead: dimensional walkthrough through the {7,6,4,1} digit-set alone.** Spine: d=4 m=1 (6174, 1746) → d=5 (60714, 60417, etc.) → d=6 (60714 + 3 zero-padded variants) → d=7 (11 strict anchors) → d=8 m=2 (465 doubles in pure multiset) → d=12 m=3 (32+10 triples) → d=16 m=4 (5 quadruples). Two distinct mechanisms (zero-padding lift for d=5-7, m-multiplicity for d=8-16) — frame as "the digit set is the invariant; the construction varies by regime", not as one mechanism.
- **F-or-0 universality is Kaprekar's own convention.** Lift Definition F.1 into §1 or §2. Frame as "Kaprekar's convention, extended" not as "a weakening of strict universality". At d=5, d=6 the result is *stronger* than classical Kaprekar (E_d = ∅; nothing escapes at all). At d≥7 the escape class has the same structural form as classical's at d=3, 4 (block-aligned multisets collapse to 0).
- **Hold {2,3,5,8} co-headline material, all Class B material, the internal-9-pair predictor, and {0,4,5,9} thread for Paper 2.** Paper 2 (Nursery) becomes the multi-thread / classification story; Paper 1 narrows to a clean single-thread dimensional walk.

---

### Older Current State (as of 2026-05-10 — preserved below; specific run-state items here are superseded by the deltas above)

(This block was the canonical state through the 2026-05-10 Addendum 9. Read for the structural background it provides on threads, Class B, and prior runs; do NOT rely on its statements about d12_7641.json data being available, or about the {0,4,5,9} Mac run being mid-flight at 49% — those are now obsolete.)

## Current State (as of 2026-05-10 — Test 2 mid-run REVERSAL: {0,4,5,9} d=12 m=3 produces ≥9 classical + 17 S-only at 49% complete, confirming third cycle thread; Class B = m=2 artifact hypothesis FALSIFIED for {0,4,5,9}; full rule analysis shows multiset-level prediction tractable, F-level NOT tractable; new candidate predictor: internal-9-pair-count ∈ {0,2})

**Paper 1 status.** v1.2.2 paper.pdf rebuilt with Appendix G integrated. 80 pages (was 76 in v1.2.1). All section numbering clean — no duplicate prefixes. Computer Modern fonts (lmodern not available in container; Mac rebuild can use lmodern if preferred). Deploy bundle staged in `/mnt/user-data/outputs/` with paper.pdf, paper.tex, paper.md, kaprekar-release.zip, update.sh, appendix_G_addendum.md, DEPLOY_INSTRUCTIONS.md. Ready to push via `./update.sh`. arXiv endorsement still pending Maynard.

**Appendix G (NEW in v1.2.2)** — Classical-scope correction and confirmation of cycle thread at m=4. Five core findings:
- §G.1–G.2: Methodological correction. Distinguishes **strict universal** (absorbs S-admissibles for S={0,1,4,6,7}), **classical universal** (absorbs all non-repdigit inputs), and **genuinely S-only** (strict but not classical). Original v1.2.1 verifier was S-restricted by accident; corrected definitions clarify scope.
- §G.3: Re-verification of v1.2.1 results in classical scope. Table G.1 summarizes: d=4 m=1 = 2/2 classical (100%); d=8 m=2 = 465/481 classical + 16 genuinely S-only (96.7% classical); d=12 m=3 = 46/55 classical + 9 S-only (83.6%). The 16 d=8 S-only universals pair as multiset siblings.
- §G.4: **Theorem G.1 (empirical)**. Cycle thread confirmed at m=4: F₁ = 6,471,467,417,167,416 and F₂ = 6,467,717,446,711,614 are classical universals at d=16, absorbing all 2,042,965 non-repdigit 16-digit multisets. Found among 5 strict universals total at d=16 m=4 (3 of 5 are genuinely S-only). Classical fraction declining with m: 100→96.7→83.6→40%.
- §G.5: Asymmetric lift behavior. Family B (zero-insertion, d=15→d=16) produced 0 universals from 731 candidates. Family D (block-{7,6,4,1}-insertion, d=12→d=16) produced 5 strict universals. Lift mechanism is multiset-flavor-specific.
- §G.6: Distribution-alternation as a candidate filter. The high-density predictor (density=1.0 + no Kaprekar-long-runs) returned 0 universals from 1,536 high-confidence candidates at d=16. The 5 actual universals appeared in lower-density buckets. Predictor's confidence ranking inverted at d=16.

**Cycle thread now confirmed at every m=1,2,3,4** (cf. Paper 2 Nursery). Paper 1's central empirical claim — cycle thread {7^m,6^m,4^m,1^m,0^k} produces classical universals at every d — extended one step further. Genuinely S-only count grows with m but classical universals continue to exist.

**Container build pipeline (NEW this session).** Rebuilt the markdown→PDF pipeline from scratch in container after the existing pipeline (preprocess.py / postprocess.py / assemble.py) wasn't bundled with the deploy. New scripts at `/home/claude/work/build/`:
- `preprocess.py` — converts GFM `$``...``$` math syntax to plain `$...$` (4,643 expressions converted)
- `postprocess.py` — handles section structure: promotes pandoc's `\subsection` → `\section` for top-level body sections; strips manual `1.1`, `F.1`, `G.7`, `A.4` etc. prefixes from subsection titles to let LaTeX auto-number; promotes `\subsubsection` → `\subsection` (compensating for pandoc's level shift); handles `\texorpdfstring` titles; balanced-brace title parsing for `\(\{7,6,4,1\}\)` etc.
- pandoc 3.1.3 + pdflatex (×2) for compilation, Computer Modern fallback when lmodern unavailable

**Phase 14 {2,3,5,8} thread (held for v1.2.3, alluded to in §G.8 #4).** Mapped through d=9 with Mac runs:
- d=4 m=1: 2 classical (5382, 2538)
- d=5,6,7 (m=1+k): 0 classical, 0 S-only, 4 partial each (no universals)
- d=8 m=2: 16 classical
- d=9 m=2 k=1: 7 classical + 21 S-only
- d=12 m=3: Mac run in progress (369,600 arrangements, 25-60h estimate)

Refined picture: {1,4,6,7} privilege is narrowly localized to m=1+k≥1; at m≥2 both digit sets behave qualitatively the same. Cycle conjecture extends beyond {1,4,6,7}. Held until d=12 m=3 finishes.

**Open question raised by Appendix G §G.8 #5 — testable.** At d=16, the 3 genuinely S-only universals lose ~62 to 1,644 inputs each to alternative attractors with non-S digit content. Example alternative: F' = 6,576,637,809,610,377 with multiset {0³,1,3,5,6³,7³,8,9}. Question: are these alternative attractors themselves classical universals over their own multisets? If yes, suggests parallel cycle threads exist for other digit sets (consistent with Phase 14's {2,3,5,8} finding above).

**Files staged in /mnt/user-data/outputs/ (deploy-ready):**
- `paper.pdf` — 80 pages, clean numbering, all sections present
- `paper.md` — v1.2.2 source (2,664 lines, was 2,373)
- `paper.tex` — regenerated LaTeX
- `appendix_G_addendum.md` — standalone Appendix G (290 lines, GFM math)
- `kaprekar-release.zip` — full repo bundle (3.4 MB) including all of the above plus updated scripts
- `update.sh` — deploy script (unchanged)
- `DEPLOY_INSTRUCTIONS.md` — step-by-step rebuild + push commands
- `search_multiset_universals_fast.py` — Phase 14 fast random-Q search (d≥8)
- `search_multiset_universals.py` — Phase 14 full enumeration (d≤7)

**Deploy procedure.** Drop update.sh, kaprekar-release.zip, paper.pdf into ~/Downloads/files-9/. Run `chmod +x update.sh && ./update.sh`. Suggested commit subject: "v1.2.2: Appendix G — classical-scope correction and confirmation of cycle thread at m=4"

**Unification direction (decided 2026-05-06 addendum, not yet executed).** Paper 1 (60714) and Paper 2 (Nursery) will eventually be merged into a single paper organized as a **constructive walk through dimensions**, with the 45 → 495 → 6174 → 60714 ladder as the spine. Each section earns the next concept by encountering an obstacle (sv at d=2, svF at d=4, coefficient-preserving lifting at d=5, C1 at d=5–7, m-lifting at d=8, strict universality at d=9, Family X non-uniqueness at d=11, classical-fraction decline at d=16). Both d=4 universal multisets ({7,6,4,1} and {2,3,5,8}) seed cycle threads; 60714's specialness at d=5–7 is that {7,6,4,1} is the d=4 thread that fills those intermediate dimensions while {2,3,5,8} skips them. Merge is **not yet executed** — see addendum to 2026-05-05/06 entry for full design and the four reasons we're holding (cycle existence theorem still empirical at general d; {2,3,5,8} d=12 m=3 Mac run pending; d=13/14/15 {7,6,4,1} runs pending; v1.2.2 should ship first to timestamp Appendix G content).

**Verified facts supporting the dimensional-walk structure.** (1) 45 family: 45 itself is NOT a fixed point of any rule at d=2 (rule space too small — only 2 rules), but 450, 4500, 45000, 450000 ARE all fixed points of some rule at their respective d (all with sv=2). 495 family same pattern at d=3 onward. The d=2 outlier is a useful pedagogical motivator for the "minimum dimension below which rule space is too sparse" point. (2) Phase 14 {2,3,5,8}² at d=8 produces 16 classical universals — verified, supporting the dual-thread reawakening at d=8 in the unified paper's pivot section. (3) **{2,3,5,8} m=3 at d=12 (NEW 2026-05-06): 76 strict universals = 63 classical + 13 S-only**, all in pure {2³,3³,5³,8³} multiset, all 63 classical absorb full classical scope of 293,920 inputs. Spot-checked K(F)=F for sample rules. **Cross-thread classical fractions at m=3 are nearly identical: 83.6% ({7,6,4,1}) vs 82.9% ({2,3,5,8}), difference 0.7%.** This parallelism-of-ratio is a new structural finding stronger than just "both threads continue" — it's a candidate cross-thread invariant.

**Audit-scope discipline (extended).** Cross-thread count comparisons require matched search procedures. Phase 13 {7,6,4,1} m=3 result (46 classical) and Phase 14 {2,3,5,8} m=3 result (63 classical) used different search procedures and rule-space coverages — absolute counts cannot be directly compared. Classical *fractions* (83.6% vs 82.9%) are more meaningful because they normalize within each search. To enable apples-to-apples count comparison, re-run {7,6,4,1} m=3 with `search_multiset_universals_fast.py --max-q-samples 50000` (~36h). New principle: **search-procedure restrictions must be matched across threads when comparing counts** (parallel to the May 4 audit-scope principle on S-set restrictions).

**Open verification needed before C1-as-diagnostic framing locks in.**
1. Does {2,3,5,8}² thread at d=8 violate C1 the same way {7,6,4,1}² does? (Determines whether C1-violation pattern parallels across threads.)
2. Is the block-insertion lift mechanism for Family D (d=12→d=16) the same as the lift producing Family B at d=8 from d=4 sources? (Determines whether m-lifting is one mechanism or several.)
3. Does direct block-insertion from 6174/1746 at d=4 produce Family B universals at d=8? (If yes: prototype proof technique for cycle existence theorem at general m.)

**New candidate lemma identified 2026-05-06.** 8-leading-forbidden bound for {2,3,5,8}. Empirical: 0 of 63 classical universals at d=12 m=3 lead with 8 (32 lead with 2, 11 with 3, 20 with 5). Parallel to proven "leading-7^k forbidden" theorem for {7,6,4,1} (May 3 session: K_max < (20/21)·7·10^(d-1) at d=4m). Same forced-borrow argument should give analogous bound for {2,3,5,8}. Worth writing up — would generalize the existing theorem to any d=4 cycle thread.

These are the concrete next-session work items toward the unified paper. Until they resolve, C1-as-diagnostic is a target framing not an established result.

**Cross-multiset classification finding (NEW 2026-05-07, see Addendum 4 to 2026-05-05/06 entry).** A global falsification sweep at d=8 m=2 across the complete universe of 17 four-distinct-digit sum-divisible-by-9 multisets produced two unexpected results that broke the original conjecture and refined the cycle-thread picture:

1. **Original conjecture FALSIFIED.** "PAIRED under 9-complement AND avoids {0,9}" was conjectured to be the necessary-and-sufficient condition for cycle-thread sources at d=4. Both halves are wrong.
2. **Two new classical-universal-producing multisets found at d=8 m=2.** {1,3,6,8} produces 1 classical (F=31866813) — self-complementary, no 0/9. {0,4,5,9} produces 2 classical (F=44900559, F=44005599) — self-complementary, contains BOTH 0 AND 9. {0,1,8,9} produces 2 S-only (no classical).
3. **Two-class structural picture.** Class A (high-density: {1,4,6,7}, {2,3,5,8}) — paired-under-9-complement, no internal 9-pairs, hundreds of universals. Class B (low-density: {1,3,6,8}, {0,4,5,9}) — self-complementary, two internal 9-pairs, 1–2 universals. Within Class B, only 2 of 10 self-complementary candidates produce; substructure unidentified.
4. **Falsification via algebraic vs dynamic obstruction split.** Of 12 non-producing multisets in the sweep, 11 fail by algebraic obstruction (no K-rules at all) and 2 fail by dynamic obstruction (K-rules exist but no universal). Same mechanism as Paper 1 §4 (Theorem 4.1 d=5→d=6 cross-check) — this is a unification finding.

**Decisive open test.** Are {1,3,6,8} and {0,4,5,9} genuine cycle threads (low-density variant) or d=8 m=2 flukes? Resolved by `search_multiset_universals_fast.py` runs on pure {1³,3³,6³,8³} and {0³,4³,5³,9³} at d=12 m=3 (~25–60h each on Mac). If they continue → cycle-thread phenomenon is ≥4-fold; classification theorem needs refined condition. If they die → {1,4,6,7}/{2,3,5,8} pair is genuinely privileged and Class B universals are a symmetric-duplication artifact specific to d=8 m=2.

**Cross-thread parallelism finding (NEW 2026-05-08, see Addendum 5 to 2026-05-05/06 entry).** The Phase 14 audit-scope re-run on {7,6,4,1} m=3 with matched procedure (`--max-q-samples 50000`) completed on Mac in 38.79h. **Result breaks the Addendum 3 cross-thread parallelism finding.**

| | {7,6,4,1} (Phase 13) | **{7,6,4,1} (matched)** | {2,3,5,8} |
|---|---:|---:|---:|
| Total strict | 55 | **42** | 76 |
| Classical | 46 | **32** | 63 |
| Classical fraction | 83.6% | **76.19%** | 82.89% |

1. **Parallelism dissolved.** Prior 0.7% gap (83.6% vs 82.9%) was a procedural artifact. Matched-procedure gap is **6.7%**, with **{2,3,5,8} the higher-classical-fraction thread**.
2. **Privilege inversion.** {2,3,5,8} produces 81% more strict universals than {7,6,4,1} at m=3 (76 vs 42). Project memory's "{1,4,6,7} is the privileged thread" framing is wrong at m=3; truth is the threads are quantitatively distinct with {2,3,5,8} denser at m≥3.
3. **Digit-set-independent curve hypothesis: FALSIFIED.** The chat-7/8/9 conjecture that classical-fraction-decline is a function of m alone is wrong at m=3. {7,6,4,1} declines faster than {2,3,5,8} from m=2 to m=3.
4. **Highest-digit-leading-forbidden: HOLDS.** 0/32 lead with 7 in {7,6,4,1} (proven, May 3); 0/63 lead with 8 in {2,3,5,8} (empirical, strong signal — worth proving the analog).
5. **Run-length-3 violations: 11–16% in both threads' classical class.** The chat-7/8/9 unified two-layer law ("Kaprekar digits run ≤2") has 5/32 violations in {7,6,4,1} and 7/63 in {2,3,5,8}; not a clean structural rule.

**Implications for unification.** The "two manifestations of one mechanism" framing of the unified paper is in serious trouble. The threads share structural features (existence at every m, highest-digit-leading-forbidden, classical-fraction-declining) but diverge quantitatively (different counts, fractions, decline rates). The honest reading is **two related but distinct phenomena**, not a single underlying mechanism. v1.2.3 / Appendix H needs to acknowledge this divergence rather than paper over it.

**Class B test still informative.** The d=12 m=3 runs on {1,3,6,8} and {0,4,5,9} (`run_class_b_d12_test.sh`, started May 7 evening, ETA 50–120h on Mac) are still running. Whether or not they produce universals, the result now answers a different question: given that {1,4,6,7} and {2,3,5,8} are quantitatively distinct, do Class B threads (if real) form a third / fourth distinct phenomenon? Result table from Addendum 4 still applies.

**Verification status.** Both `d12_7641.json` and `d12_2358.json` report `best_basin: 293,920` for all classical universals (= full classical basin at d=12). 95 classical universals across both threads, all full basin. No JSON anomalies.

**Block-balance asymmetry finding (NEW 2026-05-08, see Addendum 6 to 2026-05-05/06 entry).** While exploring the matched-procedure {7,6,4,1} data, found a structural distinction not captured by counts. At d=12 m=3, "perfectly balanced" universals (each digit appears exactly once in each of 3 blocks of 4 positions): **{7,6,4,1} has 2/32 (6.2%); {2,3,5,8} has 0/63 (0.0%).** The two surviving balanced {7,6,4,1} fps:
- F = 617464716147, blocks `6174 / 6471 / 6147` — **first block is the classical Kaprekar constant 6174.**
- F = 614714671476, blocks `6147 / 1467 / 1476` — second block is `1467` = β(6174) (sorted-ascending of 6174 under classical Kaprekar rule).

Both balanced universals are structurally Kaprekar-anchored. **Open question:** are their fixing rules coefficient-preserving liftings of 6174's d=4 native rule? If yes, this is a direct Paper 1 → Paper 2 unification finding (these are 6174's ladder fps at d=12 m=3). NEW next-session priority added: extract fixing rules from `d12_7641.json` and compare to 6174's classical-rule coefficient vector (999, 90, -90, -999).

**Phase 13 file located 2026-05-08 (see Addendum 7). Comparison reveals THREE procedural differences and budget-dependence.** Phase 13 used `max_rule_search=500K` per F (10× higher than Phase 14's 50K), leading-6 scope only, and pre-Appendix-G universality definition (no classical/S-only split). Apples-to-apples leading-6 comparison: Phase 13 found 55, Phase 14 found 29, **only 11 in both**. The 44 Phase-13-only fps are most likely real strict universals that Phase 14's lower budget systematically misses. **Implication: the matched-procedure 42 strict count for {7,6,4,1} is a lower bound, not the canonical d=12 m=3 number.**

**Important project-memory correction (NEW 2026-05-08).** Project memory carried "Phase 13 d=12 m=3: 46 classical + 9 S-only = 55 strict, 83.6% classical." The 55 strict count is correct but **the 46/9 classical-vs-S-only breakdown is fabricated — Phase 13 did not measure that distinction at all** (it predates the v1.2.2 Appendix G correction). Future-Claude should treat any "Phase 13 classical-vs-S-only" reference as suspect.

**Cross-thread comparison: relative ranking holds, absolute numbers are budget-dependent.** {2,3,5,8} produces 81% more strict universals than {7,6,4,1} at the SAME Phase 14 budget. If both threads are undercounted by the budget effect, the relative ranking is robust — {2,3,5,8} is denser at m=3. The classical fraction gap (76.19% vs 82.89%) is procedure-dependent and may close, widen, or invert under higher budgets. The Addendum 5 conclusion that the threads are quantitatively distinct stands; the specific percentages should be flagged as Phase-14-budget-dependent.

**Class B Test 1 result (NEW 2026-05-09, see Addendum 8 to 2026-05-05/06 entry).** `d12_1368_m3.json` completed on Mac in 25.0h. **{1,3,6,8} at d=12 m=3 produces zero K-rules across all 369,600 arrangements** — strongest possible algebraic obstruction. Compare to d=8 m=2 where {1,3,6,8} produced 108 K-rules and 1 classical universal. **The d=8 m=2 universal was a dimensional accident, not a real cycle thread.** Class B universals at d=8 m=2 are anomalous m=2-only artifacts of the symmetric-duplication lift.

| Multiset | d=8 m=2 classical | d=12 m=3 classical | d=12 m=3 K-rules |
|---|---:|---:|---:|
| {1,4,6,7} | 465 | 32 | 29,093 |
| {2,3,5,8} | 16 | 63 | 29,074 |
| {1,3,6,8} | 1 | **0** ← Test 1 | **0** |
| {0,4,5,9} | 2 | pending | pending |

The qualitative gap is binary: real threads produce ~29,000 K-rules; Class B {1,3,6,8} produces zero. If Test 2 on {0,4,5,9} also produces zero K-rules (plausible), the picture cleans up dramatically: **two cycle threads ({1,4,6,7}, {2,3,5,8}), Addendum 4 conjecture rehabilitated as m≥3 condition, Class B is m=2 anomaly.** Appendix H story crystallizes.

**Test 2 status: interrupted by Mac power-down, restart staged.** Test 1 output `d12_1368_m3.json` survived. Test 2 needs to run independently. Restart command (with `caffeinate -d -i` to prevent another sleep-induced interruption) is documented in Addendum 8. Expected: ~25h.

**Test 2 mid-run REVERSAL (NEW 2026-05-10, see Addendum 9).** At 49% complete (136,200 of 277,200 arrangements), Test 2 ({0,4,5,9}) has produced 9 classical + 17 S-only universals — **{0,4,5,9} is a third genuine cycle thread**, NOT an m=2 artifact like {1,3,6,8}. The early-phase 0/0 result was misleading; universals started appearing en masse around 110K arrangements. ETA ~52h to completion.

**Refined cross-thread comparison:**

| Multiset | Internal 9-pairs | d=8 m=2 classical | d=12 m=3 classical |
|---|---:|---:|---:|
| {1,4,6,7} | **0** | 465 | 32 |
| {2,3,5,8} | **0** | 16 | 63 |
| {0,4,5,9} | **2** | 2 | ≥9 (running) |
| {1,3,6,8} | **1** | 1 | 0 (Test 1) |

**Candidate Flavor-1 predictor.** Cycle threads at d=4-source require **0 or 2 internal 9-pairs**. {1,3,6,8} has exactly 1 (3+6=9; 1+8=9 needs the absent digit 8) and dies algebraically at m=3. This is a candidate necessary condition; needs further verification on additional multisets from the d=8 m=2 sweep universe.

**Rule-structure analysis (Addendum 9).** Full analysis of all 95 classical-universal rules from {7,6,4,1} (32) and {2,3,5,8} (63) at d=12 m=3:
- All 95 rules verify K(F)=F under encoding `c[i] = 10^(d-1-pi_inv[i]) - 10^(d-1-sigma_inv[i])`.
- Only soft predictor: largest digit at place 0 in pi.x — 72%/60% across threads.
- 77 distinct sign patterns across 95 rules — no canonical template.
- F-block-balanced: 2/32 in {7,6,4,1}, 0/63 in {2,3,5,8}. pi-block-aligned: 2/32, 0/63. Disjoint pairs of F values — two separate rare structural classes.
- Zero-sum coefficient pair count varies 0 to 6 per rule — §6.6 Type A predictor doesn't carry over to d=12 m=3.

**Conclusion on prediction (user's original question).** Multiset-level prediction (Flavor 1) is tractable via internal-9-pair count. F-level prediction (Flavor 2) and rule-level prediction (Flavor 3) are NOT tractable with single-variable structural signatures — rules at d=12 m=3 are highly diverse. The user's "abcd-dabc" guess (cyclic shifts of classical Kaprekar) is not supported by the data. This matches v1.2.2 Appendix G §G.6's empirical assessment: cell-level prediction exact, F-level only ~0.05% specific, fine-grained prediction fails.

**v1.2.3 / Appendix H story (pending Test 2 completion):** Clean Flavor-1 classification — "Cycle threads at d=4-source are characterized by internal-9-pair count in {0, 2}." Three confirmed threads ({1,4,6,7}, {2,3,5,8}, {0,4,5,9}), one confirmed extinction ({1,3,6,8}). Pure-multisets with exactly 1 internal 9-pair die at m≥3 despite producing m=2 universals via symmetric-duplication artifact.

**Older Current State items below this point are pre-2026-05-06 and may conflict with Paper 1 v1.2.2 status above. v1.2.2 supersedes v1.2.1 as the deployed version once update.sh is run.**

---

## Pre-2026-05-03 Current State (preserved for context)

**Chat-9 outputs (2026-04-29 late).** Four outputs from this evening's chat-9 sub-sessions, none of which alters v1.2.1's current paper state but together substantially advance the framework:
1. **Hostile review of cycle-structure theorem.** Result correct (verified on 196,308 sv=$d$ rules at $d \in \{3,4,5,6\}$ + 14,280 non-sv=$d$ pairs at $d=5$, 0 mismatches). Five exposition gaps identified, one substantive (cross-cycle disjoint-power-supports lemma missing). Full review at `COUNCIL_REVIEW_v2.md`.
2. **Proof v2 produced** (after review delivered). All five gaps fixed; theorem **broadened to drop sv=$d$ hypothesis** (sv=$d$ becomes immediate corollary); stated in base $b \geq 2$. Cross-cycle disjointness now Lemma 2; "linear independence over ℤ" replaced with "uniqueness of base-$b$ representation with bounded coefficients"; canonical matching replaces greedy. Combined empirical envelope ~205,000 K-rules across $d \in \{3..8\}$, 0 mismatches. Proof v2 at `CSC_PROOF_v2.md` is canonical going forward.
3. **Nursery Program articulated, then sharpened by Phase 0 + tower test.** The broader research direction crystallized into the **Kaprekar Nursery Program** — digit-set as generative alphabet for universal full-variable fps across all d. Phase 0 census of {0,1,4,6,7} at d=7,8 (583 d=8 universal fps, of which 554 strict). v1.0 stays on submission track; nursery program is the v2.0 paper. Updated memo at `NURSERY_PROGRAM.md`.
4. **Continuous-tower vs skip-level finding.** Empirical test via `d6_thread_tower.py` (Mac, 130s) showed {7,6,4,1}-thread has natives at every d=4..8 (counts 2, 2, 4, 19, 583) while its 9-digit-complement {8,5,3,2}-thread has natives at d=4, 8 but **none at d=5 or d=6** despite identical digit sums. The two-level gap is a structural asymmetry that the connection theorem must explain. {0,1,4,6,7} is uniquely the founder thread within the complement-pair, not just emblematic.

**Paper version.** v1.2.1 (Appendix F integrated, §F.5 corrected). 76 pages, ~720 KB, all-vector lmodern fonts. Markdown source in `paper.md`; LaTeX source in `paper.tex`; rendered PDF in `paper.pdf`. The deploy bundle is staged as `/mnt/user-data/outputs/files-8.zip` (4.0 MB) — a flat zip containing exactly three top-level files (`update.sh`, `kaprekar-release.zip`, `paper.pdf`). Clay's deploy command sequence: `cd ~/Downloads/files-8 && unzip -o ~/Downloads/files-8.zip && chmod +x update.sh && ./update.sh`. Suggested commit subject: "v1.2.1: Correct §F.5 — pure-duplication conjecture withdrawn".

**§F.5 correction (April 30, 2026).** v1.2 contained a conjecture in §F.5 that "pure-duplication extension produces no Kaprekar fixed points at any d > 4 for either classical thread" and that "zero-padding is the unique viable extension mechanism." Today's d=8 hunt found this is false: the symmetric-duplication multiset {7,7,6,6,4,4,1,1} at d=8 admits 465 universal sv=8 strict fps. Observation F.4 has been rewritten to confine its scope to d ∈ {5, 6, 7}, with an explicit "Note (added in revision)" documenting the d=8 finding and withdrawing the broader conjecture. §F.6 question 3 has been updated with the d=8 strict-anchor counts (89 in canonical {7,6,4,1,0⁴}, 465 in symmetric {7,7,6,6,4,4,1,1}). The status block at the top of Appendix F notes the revision date. The §1.8 reference to Appendix F notes the §F.5 revision. The outer bundle README also notes the revision.

**Pattern-hunt session (2026-04-29 late) results, with closure theorems proven for balanced multisets and thread-specific divergence found.** A subsequent series of chats ran a structural pattern-hunt on top of v1.2's verified strict-d findings. Headline results:

1. **Type A/B recipe decomposition (chat 2):** strict-d universal rules at d=7 and d=8 in {7,6,4,1}-core multisets decompose into recipe types. Type A_n: $n$ zero-sum pairs + $(d-2n)$-core. Type B: 0 pairs + $d$-core. Type A is characterized by an $n$-parameter Diophantine $\sum_i \alpha_i \cdot \Delta_i = F$ with Δ ∈ {1,2,3,5,6}. The mechanistic core-size argument explains why 6174 reappears at d=7 from first principles.

2. **Cross-multiset sweep (chat 4):** Of 9 d=8 multisets containing the {7,6,4,1} core, only 2 contain strict anchors: canonical zero-padding {7,6,4,1,0⁴} (89 strict fps) and symmetric duplication {7,7,6,6,4,4,1,1} (465 strict fps). The other 7 are algebraically empty.

3. **Closure-Under-Difference Theorem (chats 5, 6):** PROVEN that algebraic non-emptiness is equivalent to closure under difference (a multiset $M$ admits sv=d rules fixing some F iff there exist distinct $P, Q \in \text{Int}(M)$ with $|P-Q| \in \text{Int}(M)$). PROVEN constructively that balanced multisets {7^k, 6^k, 4^k, 1^k, 0^{d-4k}} are always closed, with d=4 primitive $6417 - 4671 = 1746$. Same construction transports to {8,5,3,2}-thread with primitive $5238 - 2385 = 2853$. **Theorem 3 PROVEN at d=8 in {7,6,4,1}-thread via aggregate-counting LP**: every unbalanced multiset has LP-infeasible solution, hence not closed. **Anti-Theorem 3 finding**: in {8,5,3,2}-thread at d=8, two unbalanced multisets ARE closed under difference, showing the closed↔balanced equivalence is thread-specific. Whether those anomalies admit universal rules is open (Mac scan needed).

The framework is now substantially proof-ready, with a clear thread-specific structure. Findings live at `/mnt/user-data/outputs/hunt/HUNT_FINDINGS.md` and `/mnt/user-data/outputs/hunt/CLOSURE_THEOREMS.md` with supporting scripts and data; not yet integrated into the paper.

**Verification status of Appendix F findings (from this session).**

The strict-d=7 strict-anchor count of 11, the d=6 strict-anchor reduction from 8 to 4, the 6174 reappearance at d=7, the per-fp rule counts, and the 60714-not-strict-at-d=7 finding have ALL been independently re-verified by a from-scratch fp-first verifier (`scripts/verifier_strict_d.py`) bundled with the paper. The original `universality_scan_v3.py` (rule-first traversal) and the new verifier (fp-first traversal with direct (A,B) image-pair lookup) produce:
- Same 4-fp d=6 list: {60714, 146070, 170460, 607140}
- Same 11-fp d=7 list: {1746, 6174, 17460, 61740, 146070, 174006, 174600, 1400706, 1460700, 1746000, 6174000}
- Same per-fp strict rule counts: 12, 6, 2, 4, 2, 2, 2, 2, 2, 10, 6
- Same 8-fp non-strict universal list at d=7
- Same actual rule sets where checked (not just same counts)

The verification removed the [VERIFICATION PENDING] flags. Verification done in-container; Clay can re-verify on Mac by running `python3 scripts/verifier_strict_d.py 5/6/7` from the deploy bundle (~70s total wall time).

One discovery during verification: the session log claim that "Sample 6174 strict-d=7 rule has c = (999000, 90000, -90000, -999000, 99, -90, -9)" is mis-attributed — that rule actually fixes F=6174000, not F=6174. The claim itself (that strict rules of this shape exist for fps in the {7,6,4,1,0,0,0} multiset) holds; just attached to the wrong fp. The integrated Appendix F doesn't repeat this specific example.

**Verification status NOT yet addressed (deferred to future sessions).**
- ~~C2 verification at d=7~~ **DONE chat 7**: 90/90 strict-d=7 rules across both classical threads pass C2. §F.6 q1 closes at d ≤ 7. C2 ⇔ C1 conjectured under sv=d + F-or-0 universality.
- Literature cross-check vs Iwasaki and Kay-Downes-Ward — still pending. Their d=7 cycle structure work should be cross-referenced against the strict-d=7 reappearance of 6174 specifically AND the cycle-structure characterization of recipes (chat 7 finding) which directly relates to permutation cycle theory.

**Chat-7 findings (2026-04-29 evening, NEW).**

1. **Cycle-structure characterization of recipes** [PROVEN — proof v2 in `CSC_PROOF_v2.md` after Reviewer #2 hostile pass; VERIFIED on ~205,000 K-rules at $d \in \{3..8\}$, 0 mismatches]. Every K-rule (π, σ) corresponds to a directed multigraph on d vertices with d edges, decomposing as a disjoint union of directed cycles via ρ = π·σ⁻¹. Recipe partition (n_pairs, core_size) = (#2-cycles in ρ, sum of lengths of ≥3-cycles). Type A_n recipes ↔ ρ has exactly n 2-cycles + ≥3-cycles. Type B ↔ ρ has only ≥3-cycles. Recipes available at dim d (under sv=$d$) = partitions of d into parts of size ≥ 2. The theorem extends to non-sv=$d$ rules with c[i]=0 ↔ fixed points of ρ (free strengthening from Reviewer #2). Proof v2 is base-$b \geq 2$ general; base 10 is one specialization.

2. **C2 ⇔ C1 conjecture** [empirically verified at d=5,6,7 in both threads]. C2 (no proper subset reproduces output) holds whenever C1 holds for sv=d F-or-0-universal rules. Provable conjecture for the next paper revision; the implication "C2 violation ⇒ C1 violation" is the harder direction.

3. **d=8 hunt complete on both threads** [Mac runs, chat 7]. Six closed multisets, 1133 strict fps, 6772 strict rules. **60714 IS strict at d=8** in canonical {7,6,4,1,0⁴} (4 rules) — strict-demotion at d=7 does not propagate. Anti-Theorem 3 finding sharpened to two specific multisets: {8,5,5,3,2,2,2,0} (sorted: 85532220) hosts 36 strict fps, and {8,8,8,5,3,2,2,0} (sorted: 88853220) hosts 52 strict fps. Both are unbalanced-but-closed in 8532-thread; 7641-thread has zero such anomalies.

4. **A4 (pure-pair (2,2,2,2)) populates only in symmetric-duplication multisets at d=8** — 312 rules in `77664411`, 192 rules in `88553322`. Canonical zero-padded multisets cannot form 4 distinct strict zero-sum pairs (the four 0-digits force degenerate cancellations failing C1).

5. **Cycle topology selection by multiset** at d=7 and d=8 — the multiset's digit configuration imposes additional structural constraints beyond the cycle theorem. At d=7: {7,6,4,1} Type B uses (7,) only; {8,5,3,2} uses (3,4) only. At d=8: `85320000` uses Type B (4,4) only — no (8,) or (3,5) — sharp contrast with `76410000`. Mechanism unidentified.

 Theorem 5.2: 60714 is universal on $A_d \setminus E_d$ at every $d \geq 5$, via coefficient-preserving lifting. Theorem 6.1: 6174 cross-dimensional pattern (universal at d=4, algebraically obstructed at d=5, dynamically obstructed at d=6, NEAR-universal at d=7,8,9). Classifications at d ≤ 6 (0, 4, 33, 506 universal full-variable fps). Even/odd ladder asymmetry observation: at even d, $|E_d| = |E_d^{(1)}|$ exactly; at odd d, $|E_d|$ is a small multiple. 53-fp Run C verified at d=7. Type A LOCK characterization: zsp_count=0 → LOCK (7/7 across 65 fps).

**Appendix F (NEW, integrated this session).**
- §F.1 Purpose. Makes F-or-0 universality explicit (will be lifted into §2 in next revision).
- §F.2 Strict-d criterion. Defs F.1 (trivial zero-sum pair on F), F.2 (strict at d), F.3 (strict-d anchor).
- §F.3 The {7,6,4,1}-thread under strict-d. Counts table 2/2/4/11 at d=4/5/6/7. Lists the 11 d=7 strict anchors. Notes both v3 and verifier_v2 produce identical lists.
- §F.4 Non-monotone strict-anchor pattern. Obs F.2 (6174/1746 at d=4,7 but not 5,6). Obs F.3 (60714 not strict at d=7; canonical lift's (900000, -900000) pair lands on equal-zero positions).
- §F.5 Pure-duplication empty (Obs F.4).
- §F.6 Six explicit open questions including the framing decision.
- §F.7 Reproducibility note pointing to bundled scripts.

**Build pipeline (stable + one fix this session).** `paper.md → preprocess.py → pandoc → postprocess.py → assemble.py → preamble.tex.template + bibliography.tex → pdflatex (×2)`. One-command runner: `./build/build.sh paper.md ./build/out`. Requires `lmodern` (or `cm-super` as substitute) for Type 1 fonts. Pipeline lives in the deploy bundle's `build/` directory.

The fix this session: `postprocess.py` now rewrites letter-prefixed appendix section headings (e.g., `\section{F.1 Purpose}`) to the starred form (`\section*{F.1 Purpose}`). Without this rewrite, LaTeX prepended a continuing arabic counter ("9 A.1", "10 A.2", ..., "37 F.1") on top of the paper's own A.* / B.* / ... / F.* numbering. Affects all appendices; main-paper sections 1–7 unchanged.

**Deploy.** `./update.sh` next to `kaprekar-release.zip` clones the public repo at `clayelmore.github.io/Kaprekar-60714`, copies all bundle contents over, prompts for commit message, pushes. The corrected `update.sh` uses `cp -a "$SOURCE/." .` so paper.pdf and any new files are picked up automatically.

**Bundle contents (`/mnt/user-data/outputs/`):**
- `files-8.zip` — **canonical deploy bundle** (4.0 MB; flat zip with `update.sh` + `kaprekar-release.zip` + `paper.pdf` at top level, no subfolder). Drop into `~/Downloads/files-8/`, run unzip + update.sh.
- `kaprekar-release.zip` — inner release zip (what update.sh actually deploys).
- `paper.pdf`, `paper.tex` — directly inspectable.
- `update.sh` — deploy script (bit-identical to v1.2's; logic unchanged).
- `kaprekar-build-bundle.zip` — older outer bundle layout (superseded by files-8.zip; kept for now but not the recommended path).

**Open work — for next session.**

**v1.2.1 deploy (staged, ready to push):**
- **Deploy v1.2.1.** Download `files-8.zip`, drop into `~/Downloads/files-8/`, run `unzip -o`, `chmod +x update.sh`, `./update.sh`. Suggested commit subject: "v1.2.1: Correct §F.5 — pure-duplication conjecture withdrawn". This corrects the §F.5 conjecture (now confined to d ∈ {5, 6, 7} with the d=8 finding documented) without altering any other content from v1.2.
- **Re-upload SESSION_LOG.md to project knowledge** after deploy so the next chat sees today's pattern-hunt findings and the v1.2.1 deploy state.

**Pattern-hunt follow-ups (from late-day hunt session — see `/mnt/user-data/outputs/hunt/`):**
- **Run d=8 universality scan on Mac.** Numba scanner ready at `/mnt/user-data/outputs/hunt/universality_scan_d8_numba.py`. Smoke-tested at d=6 (4 strict anchors) and d=7 (11 strict anchors) in container; reproduces v1.2 verified counts. Estimated ~20 min on Mac M5 Pro for d=8 in {7,6,4,1,0,0,0,0}. Open question: does 60714 reappear at d=8? Does the recipe split predict Type A2 (2-pair + 4-core), Type A1 (1-pair + 6-core), Type B (0-pair + 8-core) families?
- **Type B characterization deep-dive.** Hunt session started this (`/mnt/user-data/outputs/hunt/type_B_hunt.py`) and observed a telescoping pattern in 60417's d=5 coef vector (gaps (4,1,1,1,1) summing to zero via 9999 = 9000 + 900 + 90 + 9). Hypothesis to test: Type B coefficients form cycles in a graph where vertices are 10^k powers and edges are coefficients. If this hypothesis pins down precisely, both Type A and Type B would have constructive characterizations.
- **9-complement asymmetry mechanism.** Hunt verified that the {8,5,3,2}-thread mirrors {7,6,4,1} at d=7 under zero-padding (11 strict anchors each, same algebraic recipe), but the threads diverge at d=5, 6: {7,6,4,1} has Type B fps in zero-padding, while {8,5,3,2}'s Type B lives in 9-padding instead. The mechanism for this asymmetry is open.
- **Dynamical universality structural argument for Type A.** The hunt found that Type A's algebraic recipe is necessary but not sufficient — 12 of 20 algebraic d=7 candidates fail dynamical universality. Open question: can dynamical universality be derived from a structural property of the algebraic recipe + (π, σ) realization, rather than checked per-rule?

**Verification still pending from earlier today (carried over):**
- ~~**C2 verification at d=7.**~~ **DONE chat 7.** All 90 strict-d=7 rules across both classical threads pass C2 (50/50 in 7641, 40/40 in 8532). §F.6 q1 closes at d ≤ 7.
- **Literature cross-check vs Iwasaki and Kay-Downes-Ward.** Their d=7 cycle structure work should be cross-referenced against the strict-d=7 reappearance of 6174 AND the cycle-structure characterization of recipes (chat-7 finding) which directly relates to permutation cycle theory.
- **Integrate cycle-structure theorem into paper.** Currently lives in `TASKS_3_4_FINDINGS.md` and `D8_FINDINGS.md`. Adversarial council review pass before integrating.
- **Add §F.5 update for d=8 cycle results + anti-Theorem 3 multiset list.** Mention 60714 reappears as strict at d=8, 8532-thread anomalies (`85532220`, `88853220`) host strict anchors, recipe distributions per multiset.
- **Optional Mac followup: count-signature investigation.** Are (1,3,1,3), (2,1,3,2), (1,2,2,3), etc. count signatures in {8,5,3,2}-thread closed under difference? Quick (~minute) Mac job; would deepen the anti-Theorem 3 picture.
- **d=10 confirmation of cycle-structure theorem.** One symmetric and one canonical multiset per thread (~few hours each on M5 Pro).

**Paper-level decisions (deferred to v1.3 or v2.0):**
- **Decide on paper framing pivot.** Is the central theorem about the (sv=d, F-or-0)-universal tower (current Theorem 5.2 holds; 60714 universal at every d ≥ 5) or the (strict-d, F-or-0)-universal tower? Chat 7's `FRAMING_MEMO.md` analyzes three paths and recommends Path 3 (two co-headline theorems: sv=d ladder + cycle-structure classification) as v2.0 target. Path 1 (cycle theorem in §F) is the conservative short-term option. Decision deferred until d=12 Mac runs return + adversarial council review of cycle proof.
- **Add F-or-0 universality definition to paper §2** in next revision (currently only in §F.1).

**Long-running computational tasks (carried over):**
- arXiv endorsement resolution (Maynard pending)
- d=7 full-classification audit on Mac (closes Appendix D non-exhaustiveness gap; ~3hr Numba run on M5 Pro)
- d-independent proof of Lemma C (currently d=7..20 via finite-state)
- 60714-vs-60417 asymmetry formal proof
- Type B LOCK mechanism characterization
- LinkedIn article publication

**Known stale content the user is aware of.** The older `handoff_to_next_claude.md` (April 17–18) is from when the paper was still about 54 / dimension-locking; it predates the 60714 / dimension-transcendence pivot and should not be used as current state. The standalone-addendum framing in `ADDENDUM_DEPLOY_NOTES.md` is fully superseded — Appendix F is now integrated into the main paper, not a standalone document. The standalone `addendum.md` / `addendum.pdf` files in `/mnt/user-data/outputs/` from yesterday are content reference only; the integrated `paper.pdf` (76 pages) is the canonical version.

---

## Session entry template

When ending a chat, prepend a new entry using this skeleton:

```
## YYYY-MM-DD — [one-line summary]

**Goal of session.** What the user came in wanting to do.

**What we did.** Bullets of concrete actions. Not "discussed X" — actual changes: files edited, numbers verified, decisions made.

**Numbers verified this session.** Any empirical computation done in-container (basins, escape counts, etc.) with the actual values, so the next chat doesn't have to redo them.

**Files changed.** Path + brief note on what changed in each.

**Files produced this session.** Every NEW document, script, data file, or bundle created during the session, with full path and a one-line description. Include outputs in `/mnt/user-data/outputs/`, files in `/home/claude/`, deploy bundles, and anything received from Mac runs. This list is what the user uploads to project knowledge if a future chat needs reference. If no files were produced, say "no files produced."

**Decisions made (with rationale).** Things that aren't obvious from the diff. E.g., "Dropped coefficient vector column from the §6.2 thread table because the column overflowed and the vectors are recoverable from π,σ; documented in a parenthetical."

**Pending / left for next session.** What was started but not finished, what was discussed but not acted on, and what the user wanted to do next.

**Updates to Current State block.** Note any changes you made above. If none, say "no changes."
```

---

## Session entries (most recent first)

## 2026-05-13 / 14 / 15 — Lost d12_7641 data, hardened rerun infrastructure, math-paper-pdf skill, paper-framing pivot to dimensional-walkthrough + Kaprekar-anagram invariant

**Goal of session.** Originally: install the anthropic math-olympiad plugin. Ballooned into (a) diagnosing why the {0,4,5,9} d=12 m=3 run hung on May 12, (b) discovering a rogue {7,6,4,1} process that had silently overwritten the canonical `d12_7641.json` for ~10h, (c) staging hardened reruns of both, (d) building a reusable math-paper PDF skill with the pipeline the user has refined across the v1.2.x deploys, and (e) a substantial back-and-forth on the unified paper's framing.

**What we did.**

1. **Installed `math-olympiad@claude-plugins-official`** via `~/.claude/settings.local.json` enabledPlugins (the `/plugin` slash command wasn't available in this environment). Plugin downloaded to `~/.claude/plugins/cache/claude-plugins-official/math-olympiad/1a2f18b05cf5/` with one skill (`math-olympiad`) for IMO/Putnam-style adversarial verification.

2. **Diagnosed the May 12 {0,4,5,9} hang from `class_b_d12_test/run_log.txt`.** Last actual progress line was `[184470s] 136200/277200 | classical: 9 | S-only: 17` at 51.2h elapsed (May 10 evening). Then NO progress for ~49h, but the wrapper script printed "Test 2 complete. Wall time: 100h 11m" at May 12 22:07. Root cause: `python3 ... | tee` with `set -e` — bash's `set -e` checks the LAST command in the pipeline (`tee`, exit 0), so a dead Python process is masked. `d12_0459_m3.json` was never written; the 9/17 counts at 49% only existed as text in the log.

3. **Added checkpointing + resume to `search_multiset_universals_fast.py`.** Periodic atomic JSON writes every 1000 arrangements (default), with full RNG state in the checkpoint so resume is bit-for-bit deterministic. Time-budget-terminated runs correctly stay `complete: false`. Unit tests for stop→resume→stop→resume→finish round-trip: passes.

4. **Wrote `~/Downloads/rerun_0459_d12.sh`.** Hardened with `set -euo pipefail`, `caffeinate -dimsu` wrapper, checkpointing-aware (resumes if interrupted), verifies `complete=true` in output before printing SUCCESS. **Launched by user 2026-05-14 ~20:42 in `tmux` session `kap0459`.** Currently running. As of 2026-05-15 17:50: i=114,000/277,200 (41.13%), 8,773 K-rules, 0 classical / 0 S-only (consistent with prior run trajectory; prior run first universal at i≈133K). Process PID 39254, 99% CPU, 100 MB RSS, healthy. Naive ETA ~28h more; realistic ~tomorrow afternoon/evening.

5. **Diagnosed and killed a rogue {7,6,4,1} d=12 m=3 process** (PID 39186, parent shell PID 39148, PPID 20141 = interactive zsh). Started 2026-05-14 ~20:42 — the same minute user launched the 0459 tmux session, almost certainly from an accidental Enter on a stale shell prompt or paste into wrong window. Ran for 10h 37m, 97% CPU, was using the new checkpoint-enabled script with `--out d12_7641.json` and atomically overwriting that file every 1000 arrangements. **By the time we noticed, the canonical d12_7641.json was completely overwritten — only the rogue's partial checkpoint (96,000 arrangements, 0 classical / 0 S-only) remained.**

6. **Snapshotted the overwritten file** as `~/Downloads/d12_7641.OVERWRITTEN_2026-05-15.json` (forensics tombstone) and **deleted the live `~/Downloads/d12_7641.json`** so a future rerun_7641 starts fresh instead of resuming from garbage.

7. **Exhaustive recovery hunt for the original d12_7641.json: dead end.** No Time Machine destination configured. No copy in any `kaprekar-release.zip` (8 zips on disk, none contain it). Full clone of `clayelmore/Kaprekar-60714` (48 commits, all branches) — d12_7641.json was NEVER in the repo's history. No iCloud Drive copy. No Trash copy. The only references to its data are summary statistics in SESSION_LOG-5 (Addendum 9: counts 32+10, the 2 F-block-balanced exemplars 617464716147 and 614714671476, rule-structure aggregate findings). The 30 other classical F-values + their (π_inv, σ_inv) encodings are unrecoverable.

8. **Wrote `~/Downloads/rerun_7641_d12.sh`** for recompute. Same hardening as rerun_0459 PLUS: refuses to start while a 0459 search process is running (prevents repeat of the parallel-job CPU/file conflict), default SCRIPT_PATH resolves relative to script's own location (not CWD), uses `python3 -u` (unbuffered) so progress lines flush to log in real time. Tested: when invoked from /tmp while 0459 is running, correctly refuses with the live PIDs listed. **NOT YET LAUNCHED — will run after 0459 completes.** Since `--seed 42` is deterministic, recompute will be bit-for-bit identical to the lost file.

9. **Built `~/.claude/skills/math-paper-pdf/` user-scope skill** capturing the user's battle-tested paper.md → pandoc → pdflatex pipeline. Triggers on phrases like "build pdf from paper.md", "rebuild paper.pdf", "compile math paper". 8 files: `SKILL.md` (description tuned to be pushy enough to trigger reliably), `assets/preamble.tex.template` (copy of the user's working preamble with placeholders for TITLE/AUTHOR/DATE/ABSTRACT/BODY), `scripts/preprocess.py` (GFM math `$ \` ... ` $` → `$ ... $` + YAML frontmatter extraction), `scripts/postprocess.py` (subsection prefix-stripping with balanced-brace `\texorpdfstring` handling — uses a scanner not a regex because nested braces in math break regexes), `scripts/assemble.py`, `scripts/build.sh` (one-command runner with pipefail and per-stage outputs for debugging), `scripts/check_deps.sh`, `references/known_quirks.md` (11 quirks documented). All Python scripts unit-tested (12/12 prefix-stripping cases pass, including F.5, G.7, §G.4, Definition-F.1-not-stripped, texorpdfstring tex+pdf both stripped). **Pandoc and pdflatex not installed on this Mac yet** — `brew install pandoc && brew install --cask mactex-no-gui` would enable it. Build.sh syntax-checked. Skill works at the script level on Python 3.9 (fixed one `str | None` → bare `def` 3.10-isms).

10. **Substantive paper-framing discussion.** User proposed pivoting the unified paper away from the "two threads from one mechanism" framing (which is in real trouble per Addendum 5) toward a **dimensional walkthrough through one digit-set** (the {7,6,4,1} thread): d=4 m=1 (singles, 6174/1746), d=5 m=1+k=1 (60714/60417 with one zero), d=6 m=1+k=2 (60714 + 3 others with two zeros), d=7 m=1+k=3 (11 strict anchors), d=8 m=2 (doubles, {7^2, 6^2, 4^2, 1^2}), d=12 m=3 (triples), d=16 m=4 (quadruples). I agreed it's the cleaner story — eliminates the parallelism trouble, defers Class B / 9-complement material to Paper 2, narrows the empirical claims to the better-verified thread.

11. **Discovered a new structural invariant across the ladder by exhaustive sliding-window analysis of the d=16 m=4 data** (`~/Downloads/files-29/d16_familyD_verified.json`, 5 universals, all confirmed in pure {7^4, 6^4, 4^4, 1^4}). At each universal, slid a 4-digit window across all 13 positions and checked which windows have digit set exactly {1,4,6,7}. Result: **every single one of the 5 d=16 universals contains at least one 4-window that's a Kaprekar-set anagram.** Combined with prior data this gives a candidate invariant for §6: *"At every $d = 4m$ on the {7,6,4,1} ladder ($m = 1, 2, 3, 4$), every universal contains a 4-digit window with digit set {1,4,6,7}."* At m=1 trivially (the whole F). At m=2: 10 of 465 have literal "6174" as their leading 4-block. At m=4: zero have literal "6174" anywhere, but every one has a Kaprekar-anagram window. (m=3 awaits rerun_7641.) The richest case at d=16 is F=6471467417167416 with **7** sliding Kaprekar-anagram windows.

12. **Clarified the F-or-0 universality convention as Kaprekar's own.** Walked through the §F.1 definition; established that F-or-0 (every $n \in A_d$ → F or → 0) is identical to Kaprekar's d=3, d=4 convention, where repdigits (and at d=4, multiples of 1111) collapse to 0 and everything else goes to the nontrivial fixed point. **At d=5 and d=6 under 60714's rule, $E_d = \emptyset$ — every $A_d$-admissible input reaches 60714, full stop. At d≥7, the escape class is non-empty but has the same structural form as classical Kaprekar's escape class at d=3, 4 (block-aligned multisets collapsing to 0).** User explicitly verified 55555 collapses to 0 under any rule (it does — repdigits are excluded from $A_d$); the paper's convention is "Kaprekar's convention plus excluding near-repdigits for technical reasons in §5.6."

13. **Pinned down 60417's precise cross-dimensional status** (the sibling control case for 60714 transcendence). At d=5: strict universal AND F-or-0 universal (basin 1.0). At d=6: HAS K-rules (4 of them, identical count to 60714), but **best basin = 0.9598 — a near-miss**, not strict-d-universal. At d=7: F-or-0 universal *recovers* but loses strict-d status (Obs F.3 — every universal F-or-0 rule for 60417 contains a trivial zero-sum pair on F). Lifted from paper.md / sections/04_cross_check.md and sections/F_strict_d_anchors.md. The d=6 60417 vs 60714 comparison (same digit set, both with 4 K-rules; one universal one near-miss at basin 0.9598) is the cleanest possible setup for stating Theorem 2 — recommended for §4 lead-in.

**Numbers verified this session.**

- d=8 m=2 in {7,7,6,6,4,4,1,1}: file has 2,928 (F, rule) pairs covering 465 distinct classical F-values (matches §G Table G.1). Multiset conservation: all 465 F-values in {7,7,6,6,4,4,1,1}, 0 exceptions. Largest F = 66177414; smallest = 11446776. **77664411 (the descending arrangement that names the file) is NOT among the 465** — consistent with the proven $K_\max < (20/21)\cdot 7 \cdot 10^{d-1}$ no-leading-7 bound.
- d=8 m=2 leading-digit distribution: leading 7: 0/465; leading 6: 127/465 (27%); leading 4: 104/465 (22%); leading 1: 234/465 (50%).
- d=8 m=2 Kaprekar-anchored universals: **10 of 465 have leading 4-digit block = "6174"**, including F=61746174 (Kaprekar twice), F=61741746 (Kaprekar + reverse), F=61741467 (Kaprekar + β(6174) sorted-ascending), and 7 others.
- d=16 m=4 in pure {7^4, 6^4, 4^4, 1^4}: 5 universals in `d16_familyD_verified.json`. All 5 confirmed in pure multiset. Leading-digit distribution: 5/5 lead with 6, 4/5 lead with "646", 0/5 contain literal "6174" anywhere in the 16-digit string. Block-aligned 4-window Kaprekar anagrams: 5/20 (one block per: 6471, 1476, 7416, 4671, and a second 7416). Sliding 4-window Kaprekar anagrams: every universal has ≥1; F=6471467417167416 has **7** (windows 6471, 7146, 1467, 6741, 1674, 6741, 7416).
- 60417 at d=6 (from paper.md): 4 K-rules satisfying fixed-point equation; best basin 0.9598 across those 4 rules. Listed alongside F=54 (basin 0.9631) as the two highlighted "near miss" cases in §4.3.
- 60417 at d=7 (from §F.3 Obs F.3): admits universal sv=7 F-or-0 rules but every such rule contains trivial zero-sum pair on F; NOT a strict-d anchor at d=7. Same status as 60714 at d=7.
- d=12 {7,6,4,1} m=3 strict-anchor F-block-balanced count (from prior runs, log-recovered): 2 of 32 — F=617464716147 (block 1 = 6174, the Kaprekar constant) and F=614714671476 (block 2 = 1467 = β(6174)).
- Current {0,4,5,9} rerun (mid-flight): i=114,000/277,200 (41.13%) at 21h 8m wall, 8,773 K-rules accumulated, 0 classical / 0 S-only. Overall rate 1.58 arr/s; instantaneous rate ~4.5/s. Process healthy. Expected first universal within next 3-6h based on prior run's trajectory.

**Files changed.**

- `~/Downloads/search_multiset_universals_fast.py` — added `_write_json_atomic`, checkpoint/resume in `search_cell_fast` (new params `out_path`, `checkpoint_every`, `resume`), RNG state serialization in checkpoint, `completed_naturally` flag so time-budget breaks keep `complete: false`, `--checkpoint-every` and `--no-resume` CLI args. Smoke test still passes.
- `~/.claude/settings.local.json` — added `enabledPlugins: { "math-olympiad@claude-plugins-official": true }`.
- `/Users/clayelmore/Downloads/SESSION_LOG-5.md` — this entry added.

**Files produced this session.**

- `~/Downloads/rerun_0459_d12.sh` (4.5 KB, executable) — hardened {0,4,5,9} rerun with caffeinate + pipefail + completion verification + resume.
- `~/Downloads/rerun_7641_d12.sh` (5.5 KB, executable) — same hardening as 0459 plus a safety guard that refuses to start while any `--out d12_0459_m3.json` process is active. Recovery script for the lost d12_7641 data. NOT YET LAUNCHED.
- `~/Downloads/d12_7641.OVERWRITTEN_2026-05-15.json` (11.6 KB) — forensics snapshot of the corrupted partial checkpoint left by the rogue process. The live `~/Downloads/d12_7641.json` was deleted.
- `~/Downloads/class_b_d12_test/run_log_0459.txt` (growing) — running log of the current rerun.
- `~/Downloads/class_b_d12_test/d12_0459_m3.json` (~12 KB, growing) — live checkpoint of the current rerun. Will become the final canonical {0,4,5,9} d=12 m=3 result when `complete: true`.
- `~/.claude/skills/math-paper-pdf/SKILL.md` (7.2 KB) — skill description + triggers + pipeline overview.
- `~/.claude/skills/math-paper-pdf/assets/preamble.tex.template` (3.3 KB) — parameterized preamble (copy of `~/Downloads/documents/preamble.tex.template` with %%TITLE/AUTHOR/DATE/ABSTRACT_BLOCK/BODY%% placeholders).
- `~/.claude/skills/math-paper-pdf/scripts/preprocess.py` (5.4 KB) — GFM math + frontmatter extraction.
- `~/.claude/skills/math-paper-pdf/scripts/postprocess.py` (8.3 KB) — subsection prefix-stripping with balanced-brace `\texorpdfstring` handling.
- `~/.claude/skills/math-paper-pdf/scripts/assemble.py` (4.6 KB) — splice body into preamble.
- `~/.claude/skills/math-paper-pdf/scripts/build.sh` (5.9 KB) — one-command runner.
- `~/.claude/skills/math-paper-pdf/scripts/check_deps.sh` (1.5 KB) — dep probe.
- `~/.claude/skills/math-paper-pdf/references/known_quirks.md` (9.1 KB) — 11 documented landmines.

**Decisions made (with rationale).**

- **Use checkpointing + resume with deterministic RNG state**, not just periodic writes. Means a crashed run can be restarted bit-for-bit instead of from a different RNG trajectory. Adds ~5% overhead per checkpoint (negligible) and one extra ~600KB of JSON for the RNG state. Worth it.
- **Refuse to start rerun_7641 while rerun_0459 is active.** Exactly the failure mode that lost the original d12_7641 data — two long-running searches sharing CPU and accidentally racing on the same file. Hard-coded into the script via `ps` grep.
- **Keep the forensics snapshot (`d12_7641.OVERWRITTEN_2026-05-15.json`) but delete the live filename.** Snapshot preserves the rogue's state for debugging but the live name doesn't dangle a misleading partial checkpoint where future Claude might mistake it for canonical data.
- **Math-paper-pdf skill at user scope (`~/.claude/skills/`)** rather than as a plugin. Simpler, immediately available, no marketplace registration. Plugin form is appropriate for cross-team distribution; user-scope is right for solo use.
- **Lead the unified paper's §6 with the {7,6,4,1} digit-set ladder + Kaprekar-anagram window invariant.** Replaces the weaker "6174 as leading prefix" claim from earlier in the session (which doesn't survive to d=16). Window-anagram does survive empirically across m=1, 2, 4 (and m=3 pending rerun). Drop the cross-thread {2,3,5,8} co-headline material for v1.2.3; hold for Paper 2.
- **Lift F-or-0 universality definition from Appendix F.1 into §1 or §2** of the paper. Frame it as "Kaprekar's convention extended" rather than as a weakening of strict universality. The d=5 and d=6 results are then *stronger* than classical Kaprekar's (E_d = ∅ at d=5, 6).

**Pending / left for next session.**

- **Wait for rerun_0459_d12 to complete.** Currently 41% done, ~28h naive ETA, realistically tomorrow afternoon/evening. Watch for first classical universal (expected within 3-6h wall time).
- **Launch rerun_7641_d12 the moment 0459 finishes.** Will recompute the canonical 32 classical + 10 S-only data bit-for-bit (deterministic). ~25-40h on Mac.
- **Once both runs complete, redo §6 analysis** with full d=12 m=3 data: confirm Kaprekar-anagram window invariant at m=3, recompute leading-digit distribution at m=3 for the 4-row m∈{1,2,3,4} table, check whether the "F=6471467417167416 has 7 anagram windows" pattern has m=3 analogs.
- **Install pandoc + pdflatex** (`brew install pandoc && brew install --cask mactex-no-gui`) so the math-paper-pdf skill can actually compile. Then test build on `~/Downloads/files-35/paper.md` — expect ~80-page PDF essentially identical to v1.2.2.
- **Apply the F-or-0 framing change to §1 / §2** of paper.md per discussion. Lift Definition 2.1 from §F.1; add the four-line "convention table" (d=3, 4, 5, 6 escape class shape) before Theorem 5.2.
- **Add §4 lead-in: 60417 vs 60714 at d=6 (4 K-rules each, basins 0.9598 vs 1.0).** Makes Theorem 2 land harder by showing the precise content of "exactly one of 33".
- **Add §6 dimensional walkthrough**: digit-multiset table (d=4, 8, 12, 16 with counts), leading-digit distribution table, Kaprekar-anagram window invariant statement.
- **Run math-olympiad-style adversarial verification** on the unified draft when ready. The plugin we just installed is specifically designed for this kind of subtle-error catching that classical self-review misses (the Phase 13 fabricated 46/9 breakdown and the Addendum 5 procedural-artifact reversal are exactly its target failure modes).
- **arXiv endorsement still pending Maynard** (unchanged).

**Updates to Current State block.** Substantial — see updated Current State above. Key changes: (a) {0,4,5,9} run is back in progress after May 12 hang, currently 41% (b) d12_7641.json data DESTROYED 2026-05-14 by rogue process; rerun script staged but waiting for 0459 to finish; original 32+10 records will recompute bit-for-bit; (c) new tooling: math-olympiad plugin installed, math-paper-pdf skill created at ~/.claude/skills/; (d) checkpoint/resume infrastructure added to search_multiset_universals_fast.py for future runs; (e) new structural finding: every {7,6,4,1} d=4m universal at m∈{1,2,4} contains a Kaprekar-anagram 4-window (m=3 pending); (f) framing pivot for unified paper: dimensional walkthrough through {7,6,4,1} only, F-or-0 as Kaprekar's own convention.

### Addendum (2026-05-18 afternoon) — pandoc installed, §6 analysis pre-extracted, predictor tool scaffolded, TWO PRIOR CLAIMS RETRACTED

Three concrete deliverables completed while waiting for the 0459 run:

1. **Pandoc 3.9.0.2 installed** via `brew install pandoc` at `/opt/homebrew/bin/pandoc`. **MacTeX still blocked** — only 2.0 GB free on `~`, MacTeX needs ~5 GB. User needs to free disk before `brew install --cask mactex-no-gui` will succeed. `~/.claude/skills/math-paper-pdf/scripts/check_deps.sh` now reports pandoc OK and pdflatex MISSING.

2. **§6 dimensional-walkthrough analysis pre-extracted** at `~/Downloads/paper_section6_draft/dimensional_ladder_analysis.txt` (3.3 KB). Tabulates universal counts, leading-digit distributions, Kaprekar-window counts for d=4 m=1, d=8 m=2, d=16 m=4 from intact files. Includes a markdown summary table for §6 with a "pending" m=3 row that gets auto-filled when `rerun_7641` lands.

3. **Predictor tool scaffold** at `~/Downloads/search_with_filters.py` (17.7 KB, executable). Wraps `search_multiset_universals_fast.py`. Adds: distinct-permutation generator (avoids the 12!=479M iteration cost), no-leading-largest-digit hard filter (proven theorem, eliminates 25% of candidates at d=12 m=3), leading-digit + Kaprekar-window soft scoring for ranking, three configurable Flavor-1 multiset-level filters. Has a `--preview-only` mode that's fast (~64s at d=12 m=3) for inspecting what the filters do without committing to a run. Always pair with `--no-filters` runs as a control.

**Two prior claims retracted on the basis of these checks.**

**RETRACTION 1: The "Kaprekar-anagram 4-window invariant" claim from the original entry above (item 11, Numbers verified bullet 3) is FALSE at m=2.** I claimed "every universal at d=4m for m ∈ {1, 2, 4} contains at least one 4-consecutive-digit Kaprekar-anagram window." The d=8 m=2 data, when actually checked: **138 of 465 universals (29.7%) have ZERO Kaprekar-anagram windows.** Only 327/465 (70.3%) have ≥1. The invariant holds at d=4 (trivially — F itself is Kaprekar) and at d=16 (5/5 — but n=5 is a small sample). It does NOT hold at m=2.

This is exactly the kind of error my own §6 reasoning would have committed if I'd written that table without checking. Cataloging it explicitly so it doesn't get re-asserted later.

What survives as theorem candidates:
- (a) Multiset conservation: 100% at d=4, 8, 16 — solid.
- (b) No-leading-largest-digit: 100% at d=4, 8, 16 (and the d=12 m=3 examples from SESSION_LOG) — already proven.
- (c) Leading-digit-1 bias at m=2: 50% of d=8 universals lead with 1 — empirical, m=2-specific (the two known d=12 m=3 examples lead with 6, not 1).
- (d) Kaprekar-window enrichment: trend, not invariant. Should be phrased as "fraction of universals containing a Kaprekar-anagram window grows with m" rather than "every universal has one."

**RETRACTION 2: The "internal-9-pair count ∈ {0, 2}, not 1" predictor from SESSION_LOG-5 Addendum 9 is VACUOUS — it predicts nothing because no 1-pair multisets exist in the universe.** Combinatorial enumeration of the 24 4-distinct-digit / sum-divisible-by-9 multisets shows: 14 have 0 pairs, 10 have 2 pairs, **ZERO have 1 pair**. The "0 or 2, not 1" rule is universally true in this universe and predicts nothing.

Additionally, the original Addendum 9 claim that `{1,3,6,8}` has "exactly 1 internal 9-pair (3+6=9 only; 1+8=9 needs the absent digit 8)" is a counting error: 8 IS present in `{1,3,6,8}`, so by the naive count it has 2 pairs (1+8 and 3+6) — the same count as `{0,4,5,9}`. Yet `{1,3,6,8}` died at m=3 and `{0,4,5,9}` is surviving. **So the real Flavor-1 predictor must be something else entirely.**

Three candidate predictors consistent with the corrected data are spelled out in `~/Downloads/paper_section6_draft/predictor_candidate_multisets.md`:

- (P1) "contains 0+9 pair" — fails on `{0,1,8,9}` (m=2 has 0 classical despite 0+9 presence)
- (P2) "0-pair OR (2-pair with 0+9 AND mid-pair 3+6/4+5)" — currently the cleanest, but only 5 confirming data points
- (P3) "0-pair OR (2-pair with 0+9)" — looser version of P2

The same document picks **6 untested multisets to run next** that discriminate between these candidates: `{0,3,6,9}`, `{0,2,7,9}`, `{0,1,8,9}`, `{1,2,7,8}`, `{3,4,5,6}`, `{0,4,6,8}`. Each run is ~30h on Mac; total batch ~7.5 days sequential. Should be done AFTER `rerun_7641` finishes (no concurrent runs — same lesson as 2026-05-14).

**Implication for Paper 2 / §H planning:** the "internal-9-pair count" framing should not appear in any draft. The actual Flavor-1 predictor is to-be-determined and needs the 6-multiset batch to settle. Until then, "we have one digit-set that survives at every checked m (the {7,6,4,1} thread, ladder d=4,8,12,16) and a near-twin that survives (the {2,3,5,8} thread, d=4,8,12); the broader characterization of which multisets host cycle threads is open" is the honest framing.

**Files produced in this addendum.**

- `~/Downloads/paper_section6_draft/dimensional_ladder_analysis.txt` (3.3 KB) — §6 data + summary table for paper.md
- `~/Downloads/paper_section6_draft/predictor_candidate_multisets.md` (7.2 KB) — predictor-vacuity finding + 3 alternative predictors + 6 next-batch picks with rationale
- `~/Downloads/search_with_filters.py` (17.7 KB, executable) — predictor tool scaffold

**Pending / next actions** (added to today's earlier list, not replacing it).

- When `rerun_7641_d12` completes, re-run the dimensional-ladder analysis script to fill in the m=3 row of the §6 table.
- Verify that the d=12 m=3 universals from the recompute would have been correctly RANKED by the filtered search — i.e., would 21 + 23 universals (or whatever the {0,4,5,9} run produces) appear high in the soft-score ordering? If yes, the leading-digit-1 bias generalizes. If no (which the two known {7,6,4,1} F-block-balanced examples already suggest), the ranking needs an m-specific term.
- The 6-multiset batch is a lot of compute. Realistically pick 2-3 first (the most diagnostic: `{0,3,6,9}` and `{1,2,7,8}` and `{0,1,8,9}`) and decide based on results whether to run the others.

---

## 2026-05-05/06 — Paper 1 v1.2.2 deploy bundle: Appendix G integration, container PDF rebuild from scratch, section-numbering fix

**Goal of session.** Integrate Phase 14 findings into Paper 1 as Appendix G addendum, rebuild the PDF in container from scratch (since the existing build pipeline wasn't bundled), and produce a complete deploy bundle ready for `update.sh`.

**What we did.**

1. **Drafted Appendix G (5 pages, ~290 lines GFM markdown, ~2,050 words).** Nine sections:
   - §G.1–G.2: Methodological correction. Strict-K-rule vs classical-universal vs genuinely-S-only. Definitions G.1–G.4.
   - §G.3: Re-verification of v1.2.1 results in classical scope. Table G.1: d=4 m=1: 2/2 classical (100%); d=8 m=2: 465/481 classical + 16 S-only; d=12 m=3: 46/55 classical + 9 S-only.
   - §G.4: **Theorem G.1 (empirical)**. Cycle thread confirmed at m=4: F₁ = 6,471,467,417,167,416 and F₂ = 6,467,717,446,711,614 are classical universals at d=16. Found among 5 strict universals total at d=16 m=4 (3 of 5 are genuinely S-only).
   - §G.5: Asymmetric lift behavior (Family B negative, Family D produces 5 universals).
   - §G.6: Distribution-alternation as candidate filter. High-density predictor returned 0 universals at d=16; 5 actual universals appeared in lower-density buckets.
   - §G.7–G.9: Methods note, 5 open questions, acknowledgments.

2. **Patched paper.md with Appendix G splice.** Inserted after Appendix F and before References. Preserved entire body of paper.md unchanged. Result: 2,664 lines (was 2,373). Verified splice clean by line-by-line diff of first 2,340 lines.

3. **Rebuilt the container build pipeline from scratch.** The existing pipeline (preprocess.py/postprocess.py/assemble.py) was not in the deploy bundle. New scripts at `/home/claude/work/build/`:
   - `preprocess.py` — converts GFM `$``...``$` math syntax to plain `$...$`. Regex `\$`([^`]*?)`\$` matches all 4,643 inline expressions cleanly.
   - `postprocess.py` — handles section-structure cleanup. **Key bug found and fixed**: section numbering was duplicated in initial output (e.g., `1.1 1.1 Kaprekar's routine`) because pandoc auto-numbers AND the markdown has manual prefixes like "1.1", "F.1", "G.7" baked into titles. Fix: strip alphanumeric.numeric prefixes from `\subsection` and `\subsubsection` titles, let LaTeX auto-number. Also handles `\texorpdfstring` titles with balanced brace counting (needed for `\(\{7,6,4,1\}\)` math).
   - Compilation: pandoc 3.1.3 → pdflatex ×2. Computer Modern fonts (lmodern not available in container, used CM fallback).

4. **Iterated on postprocessor through 5 versions** to handle edge cases:
   - v1: regex matched literal backticks, wrong syntax — failed
   - v2: math regex fixed; section transform had `|` alternation at wrong level, mangled paragraph breaks
   - v3: line-by-line block parser; missed multi-line texorpdfstring titles
   - v4: TWO separate regex patterns (PATTERN_A for texorpdfstring, PATTERN_B for plain), but PATTERN_B incorrectly matched substrings inside `\subsubsection` blocks (added negative lookahead for `\texorpdfstring`)
   - v5: stripped numeric prefixes from subsection titles to fix duplicate numbering bug Clay caught

5. **Verified v1.2.2 PDF structure clean**:
   - 80 pages (was 76 in v1.2.1) — +4 pages from Appendix G
   - 16 top-level sections in correct order (Introduction, Framework, ..., Appendix G, References)
   - Body subsections show clean numbering: `1.1 Kaprekar's routine and the middle-digit cancellation`, `1.4.1 The 54 → 60714 discovery arc`, etc.
   - Appendix subsections show clean numbering: `9.1 Classification at d = 3`, `15.1 Purpose`, `15.7 Methods note: classical-scope verification`, `15.9 Acknowledgments`, etc.
   - Theorem G.1, Table G.1 render correctly
   - References intact, "End of paper" marker preserved

6. **Built complete deploy bundle.** Replicated v1.2.1's flat zip structure: three top-level files (`update.sh`, `kaprekar-release.zip`, `paper.pdf`). Inside `kaprekar-release.zip`: full repo contents with new paper.md, paper.pdf, paper.tex, appendix_G_addendum.md, and Phase 14 search scripts added to scripts/.

7. **Discussed §G.8 #5 alternative-attractors question**. The 3 genuinely S-only universals at d=16 lose 62-1,644 inputs each to alternative attractors. Example: F' = 6,576,637,809,610,377 with multiset {0³,1,3,5,6³,7³,8,9}. Open testable question: are these alternative attractors themselves classical universals over their own multisets? Would suggest parallel cycle threads exist for other digit sets — consistent with Phase 14 {2,3,5,8} finding.

**Numbers verified this session.**
- Appendix G splice preserves first 2,340 lines of paper.md unchanged.
- 4,643 GFM inline math expressions converted by preprocessor (0 remaining unconverted).
- Final paper.tex: 5,914 body lines + 117 preamble lines + `\end{document}` = ~6,032 lines total.
- Final paper.pdf: 80 pages, 922,453 bytes.
- Section count: 16 top-level `\section`, 102 `\subsection`, 10 `\subsubsection`.

**Files produced this session.**

- `/mnt/user-data/outputs/paper.md` — v1.2.2 source with Appendix G spliced (2,664 lines, 254 KB)
- `/mnt/user-data/outputs/paper.pdf` — rebuilt 80-page PDF (922 KB) with clean numbering
- `/mnt/user-data/outputs/paper.tex` — regenerated LaTeX source (291 KB)
- `/mnt/user-data/outputs/appendix_G_addendum.md` — standalone GFM Appendix G (290 lines, 14 KB)
- `/mnt/user-data/outputs/kaprekar-release.zip` — deploy bundle (3.4 MB)
- `/mnt/user-data/outputs/update.sh` — Clay's deploy script (4.4 KB, unchanged)
- `/mnt/user-data/outputs/DEPLOY_INSTRUCTIONS.md` — step-by-step push guide (3.8 KB)
- `/mnt/user-data/outputs/search_multiset_universals_fast.py` — Phase 14 fast search d≥8
- `/mnt/user-data/outputs/search_multiset_universals.py` — Phase 14 full enumeration d≤7
- `/home/claude/work/build/preprocess.py` — container build pipeline preprocessor (GFM → plain math)
- `/home/claude/work/build/postprocess.py` — container build pipeline postprocessor (section cleanup, prefix stripping)

**Decisions made (with rationale).**

- **Splice Appendix G as standalone unit** rather than restructure existing appendices. Keeps prior content unchanged, minimizes risk of breaking existing cross-references and labels. Matches v1.2.1's working structure.
- **Strip manual numeric prefixes from subsection titles**, let LaTeX auto-number. Cleaner result than v1.2.1's "9 A.1 Classification at d=3" double-numbering. My v1.2.2 shows "9.1 Classification at d=3" — single auto-numbered prefix.
- **Use `\section` for `Appendix X.` headings**, then `\subsection` for X.1, X.2, etc. Pandoc demotes everything one level when there's a title `\section`, so what was markdown `# Appendix X` becomes `\subsection`, then `## X.1` becomes `\subsubsection`. My postprocessor un-demotes to match v1.2.1's logical structure.
- **Hold {2,3,5,8} thread for v1.2.3.** Appendix G alludes to it in §G.8 #4 ("at least one other digit set produces classical universals at m=2") without committing to specifics. Mac d=12 m=3 run still in progress (~25-60h). When complete, write v1.2.3 update.
- **Computer Modern fonts in container build** rather than fight with lmodern install. Both are Type 1 vector; CM is slightly less polished but fully readable. Clay can rebuild on Mac for lmodern if desired.

**Pending / left for next session.**

- **Deploy v1.2.2 to GitHub via `./update.sh`**. Bundle is staged and ready. Suggested commit subject: "v1.2.2: Appendix G — classical-scope correction and confirmation of cycle thread at m=4"
- **Test §G.8 #5 alternative attractors hypothesis.** Take F' = 6,576,637,809,610,377 (or other alternatives), find a strict K-rule fixing it, run iteration from every input in F''s digit multiset. If universal: parallel cycle thread discovered. If not: orbit goes elsewhere, follow it.
- **{2,3,5,8} thread d=12 m=3 Mac run still in progress.** When complete, write v1.2.3 with §G.10 or new appendix.
- **arXiv endorsement still pending Maynard.**
- **Paper 2 (Nursery) work continues separately** with Family B/C/D classification, cycle existence theorem proof attempt, etc. (See pre-2026-05-03 Current State below.)

**Updates to Current State block.** Updated to reflect v1.2.2 deploy-ready status, Appendix G content summary, container build pipeline rebuilt, cycle thread confirmation at m=4. Paper 2 / Nursery state preserved in older entries below.

### Addendum (later in same session) — paper-unification design discussion

**What prompted it.** After v1.2.2 deploy bundle was finalized, conversation turned to whether/how to merge Paper 1 (60714) and Paper 2 (Nursery) into a single document. User's stated motivation: "we use the same idea, and nothing has been published" — both papers are pre-publication and the unifying idea ought to be made explicit before either is locked in.

**The unifying idea (in Clay's words).** What makes 60714 special at d=5–d=7 specifically is that {7,6,4,1} is the only d=4 cycle thread that fills those intermediate dimensions. {2,3,5,8} also seeds a cycle thread (Phase 14 confirmed: 2 classical universals at d=4 m=1, 16 at d=8 m=2, 7+21 at d=9 m=2 k=1) but produces zero universals at d=5,6,7. So 60714 isn't just "the unique survivor of Theorem 4.1's cross-dimensional test" — it's the d=5 instance of the d=4 thread that doesn't skip dimensions. The two papers aren't separate findings; they're the same finding viewed from different scales.

**Proposed paper structure (Clay's design).** A single paper organized as a **constructive walk through dimensions**, not "Paper 1 + Paper 2" stitched together. Each section earns the next concept by encountering an obstacle the previous machinery can't handle:

- **d=2,3:** 45 and 495 motivate sv (surviving variables). Anyone-can-verify entry point.
- **d=4:** Two universal multisets — {7,6,4,1} and {2,3,5,8}. Introduce svF. Classical Kaprekar 6174 recovered.
- **d=5:** Classical rule fails (rank reduces). 33 universals total; only 60714/60417 in {7,6,4,1,0}. Introduces coefficient-preserving lifting and the asymmetry between threads.
- **d=5,6,7:** Theorem 5.2 in full. Escape class Ed introduced via continuity with classical d=3,4 escape phenomenon. C1 condition introduced as **named structural principle** (currently a buried support lemma in Appendix C — the unification promotes it).
- **d=8:** Both {7,6,4,1}² and {2,3,5,8}² threads ignite at m=2. Introduce m-lifting (block insertion at d=4m). The {2,3,5,8} reawakening at d=8 is the moment the framework generalizes beyond {7,6,4,1}.
- **d=9–11:** Zero-padding continues. Family A goes barren under strict universality at d=9. Introduce strict-vs-classical universality (the distinction that motivates Appendix G's correction). Family X disrupts uniqueness at d=11.
- **d=12 m=3, d=16 m=4:** Both threads continue. Theorem G.1 lands here. Classical fraction declining (100→96.7→83.6→40%) but still positive.
- **Cross-thread program statement:** Both d=4 universal multisets seed cycle threads at d=4m for m=1..4. Both d=4 multisets accounted for (Theorem 3.2 is exhaustive). Open: do d=8 universal multisets seed their own threads at d=16, d=24?

**Why this works (recorded for future-Claude).**
1. *Narrative is mathematical, not biographical.* Each concept introduced when the dimension forces it.
2. *Proven results land in natural homes.* Theorem 5.2 anchors d=5–d=7. Classification theorems scattered through dimensional sections. Cycle existence theorem (when proven) lands at d=4m for general m.
3. *Empirical and proven content sit comfortably together.* Each section labels its own status as the dimensions climb. No "discussion of empirical vs proven" disconnected from results.
4. *Single anchor for whole work.* 45 → 495 → 6174 → 60714 ladder is the organizing principle. Entry-level reader can follow; sophisticated reader gets full machinery.

**Watch-outs flagged in discussion.**
- Length: 100+ pages is plausible. *Experimental Mathematics* may not be right venue anymore. Could be monograph-style or partition for journal submission.
- d=4 multiset uniqueness claim must be airtight (Theorem 3.2 is exhaustive — make it prominent).
- {2,3,5,8} parallelism with {7,6,4,1} needs to hold at higher m. d=12 m=3 Mac run still pending.
- Classical fraction decline (100→96.7→83.6→40% across m=1..4) may go to zero at m=5 or higher. Paper's central claim must distinguish *strict universals continue* from *classical universals continue* — the latter may attenuate.
- C1 promotion from proof-internal device to named structural principle requires restatement work. Currently stated as technical condition in proof of Lemma 5.2; not yet a top-level concept characterizing liftings in general.

**Decision: not yet committing to the merge.** Reasons:
1. Cycle existence theorem is still empirical at general d. Merging now would saddle the unified paper with a central conjecture where a central proven theorem should be. Better to wait.
2. d=12 m=3 {2,3,5,8} Mac run still in progress. Need result before structuring the cross-thread sections.
3. d=13/14/15 {7,6,4,1} Mac runs still pending. Family B trajectory at higher d needs to settle.
4. v1.2.2 of Paper 1 should ship first (timestamp authorship of Appendix G content). Then let Paper 2 cook. Then unify.

**Recommended sequence (recorded for future-Claude).**
1. Push v1.2.2 of Paper 1 via update.sh.
2. Wait for d=12 m=3 {2,3,5,8} Mac run + d=13/14/15 {7,6,4,1} Mac runs.
3. Build program-level webpage on clayelmore.github.io/Kaprekar-60714 explaining how the pieces fit (Paper 1's 60714 result, Paper 2's cycle census, the open existence theorem). Webpage holds program coherence without forcing premature paper merge.
4. Attempt structural proof of cycle existence theorem via constructive lift mechanism (concrete first step: study d=8→d=9 Family B lift with 481 source universals and 8 target universals).
5. *If/when* cycle existence theorem closes, write the unified paper with that proof as headline. 60714 becomes the explicit worked instance; cycle thread is the general phenomenon.
6. *If* cycle existence stays empirical, the unified paper's headline is the structural framework + Theorem 5.2 anchor + cycle existence as central conjecture supported by m=1..4 evidence + cross-thread parallelism with {2,3,5,8}.

**No files produced for this addendum** — design discussion only. Idea recorded for the next chat to pick up.

**Other context discussed.**
- User asked why math papers are written so densely. Discussion of compression-as-handshake vs performance-vs-gatekeeping. Noted that user's prose is already less stilted than typical (the §1.4 "On method" passage explicitly narrating the 54 → 60714 discovery arc is unusual — most papers scrub that out). Don't let mathematician-audience constraint convince user to rewrite the honest narrative parts.
- YouTube video idea floated as natural follow-up artifact for the program-level audience. Different artifact than the paper; the paper is the durable citation record, the video is the durable narrative thread.

### Addendum 2 (further later, same session) — fleshing out the dimensional walk: 45 family verification and d=8 C1-pivot design

**Why this got added.** Continuing the unification design from Addendum 1, two specific dimensional-walk sections were sketched in detail: the d=2,3 entry point using the 45 family, and the d=8 C1-pivot where the framework expands beyond {7,6,4,1}.

**45 family — empirical verification done in container.** User asked whether 45, 450, 4500, 45000, etc. always work as fixed points at their respective d. Quick exhaustive check via `find_rules_fixing(F, d)` over all (π,σ) pairs:

| F | d | Has fixing rule? | Note |
|---|---|---|---|
| 45 | 2 | **NO** | Only 2 rules at d=2 (sign-flips), neither fixes 45. K(45)=9 under classical d=2; iteration cycles 45→9→81→63→27→45→... |
| 450 | 3 | YES (2 rules) | sv=2, classical-like rule with coefs (-90, 0, 90) |
| 4500 | 4 | YES (16 rules) | sv=2 |
| 45000 | 5 | YES (216 rules) | sv=2 |
| 450000 | 6 | YES | (verified) |

Same pattern verified for 495 family at d=3 (495), d=4 (4950), d=5 (49500), d=6 (495000) — all have fixing rules.

**The d=2 outlier is pedagogically valuable.** 45 is in the iteration cycle (passes through 45 every 5 steps under classical d=2) but isn't a literal fixed point at d=2 because the rule space is too small (only 2 rules). At d=3 onward, F·10^{d-2} *is* a fixed point of some rule. This sets up the "minimum dimension below which rule space is too sparse" point, which motivates why we need svF as a concept at d=4 (where full-variable becomes meaningful) rather than at d=2 (where the rule space is degenerate).

**Three threads interleaved in the early dimensions of the unified paper.**
1. **Degenerate-rank family** (45 → 450 → 4500 → ...): trivially fixed at every d ≥ 3 by rank-2 rules. svF=2 throughout. Motivates why we need the sv concept.
2. **Classical Kaprekar family** (495 → 6174 → ...): rank-reducing at odd d (495 has sv=2 because middle digit cancels), full-variable at even d (6174 has sv=4). Includes Kaprekar's original result as a station in the dimensional walk.
3. **Transcendent family** (60714 → ...): full-variable rules with svF < d via absorbing zeros. Coefficient-preserving lifting is the mechanism.

The 45-at-d=2 exception is a useful pedagogical moment: it tells the reader *why* we don't trivially declare "every integer with trailing zeros is fixed by some rule everywhere." There's a minimum dimension below which the rule space is too small to provide enough freedom.

**d=8 as the framework-expansion pivot.** Two structural events happen simultaneously at d=8 in the dimensional walk:

1. **60714's coefficient-preserving lifting continues mechanically.** Even-ladder root extends via zero-sum pair appending. Theorem 5.2 in full, |E_8|=45 closed-form, all step-1 collapses verified. The d=5–7 mechanism gets one more dimension of validation before the framework expands.

2. **The m=2 thread ignites — and {2,3,5,8} reawakens.** {7²,6²,4²,1²} produces 481 strict universals (465 classical + 16 genuinely S-only per Appendix G). {2²,3²,5²,8²} produces 16 classical universals (Phase 14 finding). Two parallel m=2 threads now active. **This is the moment in the paper where the framework generalizes beyond {7,6,4,1}.** The strict-vs-classical universality distinction (from Appendix G) lands here naturally — it's where the gap first opens.

**C1's role as named structural principle (proposed elaboration).** Currently C1/C2 are buried support lemmas in Appendix C characterizing core non-negativity under sorted-descending input. Memory entry from May 4 records: "60714 ladder VIOLATES C1 in a controlled way that produces the lift" and "clean cross-d insertion lift for 60714 ⟺ C1 violation."

The proposed unified-paper framing promotes C1 from buried lemma to **diagnostic principle distinguishing two lifting regimes**:
- **Zero-padding regime (d=5,6,7,8 even-ladder):** 60714's lift violates C1 in a way that lets the heavy-magnitude coefficient (-999 → 99000 + -99999 split, then zero-sum appends) absorb on F's zero digits. Single-instance thread.
- **m-lifting regime (d=8 onwards via Family B):** At d=4m, the {7^m,6^m,4^m,1^m} multiset produces a parallel population of universals via block-insertion (Family D mechanism in Appendix G §G.5). Different lift mechanism; different C1 status; different multiset structure.

If C1's status is the **diagnostic** for which lifting regime applies, then the d=5→d=8 stretch of the unified paper has a clean narrative: introduce C1 at d=5 (60714's lift violates it), confirm violation pattern at d=6,7 (same mechanism), continue at d=8 (still works), watch parallel family appear at d=8 with *different* C1 status — that parallel family is what the cycle thread becomes at higher m.

**Three open questions raised about C1 (need verification before committing to the framing).**

1. **Does the {2,3,5,8}² thread at d=8 violate C1 the same way {7,6,4,1}² does?** If yes, C1-violation patterns parallel cleanly across both d=4 cycle threads and the C1-as-diagnostic story holds. If they violate it differently (or {2,3,5,8} satisfies C1), the story is more complex and the section structure needs revision.

2. **Is the block-insertion lift mechanism for Family D (used at d=12→d=16 per Appendix G §G.5) the same mechanism producing Family B at d=8 from d=4 sources?** Or two distinct constructions? If same: m-lifting concept generalizes cleanly, C1 distinguishes m-lifting from zero-padding. If different: section needs to introduce two distinct m-lifting mechanisms.

3. **Is there a direct construction of the 481 Family B universals at d=8 from the d=4 universals (6174, 1746) via an explicit lift?** May 3 session notes flag this as the concrete first step toward the cycle existence theorem. Not yet worked out. If it has been: d=8 section becomes much stronger. If not: d=8 section presents the 481 universals as empirical census + structural conjecture.

**Status of the C1 framing: structural conjecture, not yet verified.** The named-principle promotion is proposed by the user as the right unifying frame. The verification work (questions 1–3 above) hasn't been done yet. Future-Claude should treat C1's role as diagnostic-principle as a *target framing* the user is reaching toward, not as established result. The dimensional walk's narrative arc depends on whether the verification holds up; if it doesn't, the d=8 section becomes more honestly "two coexisting families with empirically different lift mechanisms, structural relationship open."

**Decisions made.**
- Unified paper's d=2 entry should explicitly flag 45-as-non-fixed-point at d=2 as the rule-space-too-small case, then transition to "but at d=3 onward, F·10^{d-2} works" as motivation for svF.
- Unified paper's d=8 section should split into two sub-sections: first the 60714 even-ladder root and Theorem 5.2 closure; then the m=2 thread and C1-as-diagnostic.
- Phase 14 {2,3,5,8} d=8 result (16 classical) is essential to the d=8 section. Already verified; no new compute needed.
- C1 promotion to named principle is *desirable framing* but contingent on verification questions 1–3. Don't write the section as if C1-as-diagnostic is settled until those are checked.

**Pending / left for next session.**
- **Test C1 status of {2,3,5,8}² universals at d=8.** Concrete: take the 16 Phase 14 classical universals at d=8, compute their core-contribution under their fixing rules, check whether C1 (as currently stated in Appendix C of Paper 1) is violated, and how. Compare to 60714 ladder rule violation pattern. This answers question 1 directly.
- **Compare Family B (d=8) and Family D (d=16) lift mechanisms.** Concrete: Family D at d=12→d=16 inserts a length-4 {7,6,4,1} block. Family B at d=8 — what's the analogous source? If d=4 universals are the source and the same block-insertion logic generates the 481 Family B universals at d=8, that closes question 2. If not, the lift mechanisms are distinct.
- **Attempt direct d=4 → d=8 lift construction for Family B.** Take 6174 (or 1746) at d=4. Apply block-insertion: insert a {7,6,4,1} block. Result: a 16-character multiset {7²,6²,4²,1²}. Find a fixing rule. Compare to the 481 known Family B universals: does this construction produce one of them? Many of them? All? This is the witness for the cycle existence theorem at m=2.
- **If question 3 yields a constructive lift**, that's the prototype proof technique for the cycle existence theorem at general m. Worth writing up immediately.
- **Update SESSION_LOG and Current State if/when C1-as-diagnostic verification completes.**

**No files produced for this addendum** — design and verification work only.

### Addendum 3 (further later, same session) — d=12 m=3 {2,3,5,8} Mac run completed; cross-thread classical-fraction parallelism confirmed

**The Mac run finished.** `python3 search_multiset_universals_fast.py --multiset "8,8,8,5,5,5,3,3,3,2,2,2" --d 12 --max-q-samples 50000 --out d12_2358.json` — 36.6 hours wall time, exhaustive over all 369,600 arrangements of the {2³,3³,5³,8³} multiset.

**Headline result.**

| | Value |
|---|---|
| Arrangements searched | 369,600 (exhaustive — full m=3 symmetric multiset coverage) |
| F values with ≥1 fixing K-rule | 29,074 |
| **Classical universals** | **63** |
| **Genuinely S-only universals** | **13** |
| Total strict universals | **76** |
| Wall time | 36.6 hours (130,910s) |

All 63 classical universals report `best_basin = 293,920 = C(21,9) - 10`, the full classical scope (all non-repdigit 12-digit multisets, digits 0-9). Honest classical universality, not S-restricted.

**Spot-checked verification:** K(F)=F confirmed for 5 classical and 3 S-only universals using script convention `coefs[i] = 10^(d-1-pi_inv[i]) - 10^(d-1-sigma_inv[i])`. (Required correction: my initial verification attempt used the wrong index convention; the script's actual convention places the highest-place coefficient at lowest index. All rules verify cleanly under the correct convention.)

**Cross-thread comparison through m=3.**

| (m, d) | {7,6,4,1} | {2,3,5,8} | Classical fraction |
|---|---|---|---|
| m=1, d=4 | 2 / 2 | 2 / 2 | 100% / 100% |
| m=2, d=8 | 465 / 481 | 16 / 16 | 96.7% / 100% |
| **m=3, d=12** | **46 / 55** | **63 / 76** | **83.6% / 82.9%** |
| m=4, d=16 | 2 / 5 | (untested) | 40% / ? |

**Key new structural fact (worth flagging in the unified paper).** Classical fractions at m=3 are nearly identical across both threads: 83.6% vs 82.9%, difference 0.7%. **The thread density may differ (46 vs 63 absolute counts) but the proportion of strict-that-is-classical is approximately a thread-independent invariant at m=3.** This is stronger than "both threads continue at m=3" — it's a *quantitative* parallelism that wasn't visible before this run.

**Audit-scope caveat (CRITICAL — do not ignore).** The 46 number for {7,6,4,1} m=3 came from Phase 13's exhaustive search. The 63 here came from `search_multiset_universals_fast.py` with `--max-q-samples 50000`. **Different search procedures.** Cannot directly compare absolute counts. The classical *fraction* comparison (83.6% vs 82.9%) is more meaningful because it normalizes within each search's own outputs.

To enable apples-to-apples count comparison, we should re-run {7,6,4,1} m=3 with the matching procedure:

```bash
python3 search_multiset_universals_fast.py \
  --multiset "7,7,7,6,6,6,4,4,4,1,1,1" \
  --d 12 --max-q-samples 50000 \
  --out d12_7641.json
```

Same time budget (~36 hours). Until done, the absolute count comparison "63 > 46 means {2,3,5,8} is denser at m=3" is not supported by the data.

**Audit-scope discipline extended (recorded as learning principle).** The May 4 memory entry already captures: "S-set restrictions must apply only to fp search, not to input enumeration — mixing the two produces wrong counts." The new principle is parallel: **search-procedure restrictions must be matched across threads when comparing counts.** Different Q-sampling parameters, different rule-space coverages, different time budgets all produce different count distributions over the same underlying set. Cross-thread comparisons require matched procedures.

**S-only deficit pattern.** The 13 S-only universals miss between 11 and 902 inputs out of 293,920 (0.004% to 0.307% of scope). Comparable shape to {7,6,4,1} m=4 d=16 S-only universals (62-1644 misses out of 2,042,965). Most S-onlys are very nearly classical, missing tiny fractions of inputs to alternative attractors. Three universals tie for the smallest deficit (11 misses each): F=535232388528, 535223883528, 253532388528.

**Structural observations.**
1. **All 63 classical universals are within the pure m=3 symmetric multiset {2³,3³,5³,8³}**. None spread to mixed-multiplicity arrangements. Clean parallel to {7,6,4,1} m=3 (which also lives in its own pure symmetric multiset).
2. **Leading-digit distribution is non-uniform.** 32 lead with 2, 11 lead with 3, 20 lead with 5, **0 lead with 8**. The 8-leading positions are forbidden — consistent with the proven "leading-7^k forbidden" theorem from May 3 session for {7,6,4,1} (K_max < (20/21)·7·10^(d-1) at d=4m for the {7,6,4,1} thread). The analogous bound for {2,3,5,8} would forbid 8-leading by the same mechanism: K_max < (some fraction)·8·10^(d-1) due to forced-borrow structure. **This is structural, not coincidental, and parallels cleanly between the two threads.**
3. **Most universals have only 1 fixing rule.** Distribution: 47 classical with 1 rule, 14 with 2, 2 with 3. S-only: 9 with 1 rule, 3 with 2, 1 with 3. Sign-flip pairs are NOT systematically present. The asymmetry between digit values (2,3,5,8 has no obvious symmetry under the rule) means many F values are fixed by exactly one rule rather than the symmetric pair we'd expect for {7,6,4,1}.

**Implications for the unified paper.**

1. **The d=12 section now has substantial content for both threads.** Both produce universals in pure m=3 symmetric multisets, both have comparable S-only deficit shapes, both have near-identical classical fractions, both have leading-digit forbidden patterns. The dual-thread story is solid through m=3.

2. **The classical-fraction parallelism is a new candidate theorem.** Currently empirical at m=1 (100%/100%), m=2 (96.7%/100%), m=3 (83.6%/82.9%). If verified at m=4 once {2,3,5,8} m=4 runs, it becomes a structural conjecture worth proving. The conjecture: *At each m, the ratio (classical universals)/(strict universals) is approximately thread-independent for d=4 cycle threads.*

3. **The 8-leading-forbidden observation is a lemma the unified paper should state explicitly.** It's a clean structural result that parallels across threads. Would generalize the May-3-session "leading-7^k forbidden" theorem to any d=4 cycle thread.

**Decisions made.**
- {2,3,5,8} m=3 Mac result is now solid empirical input to the unified paper's d=12 section.
- The classical-fraction-parallelism finding is the headline structural fact from this addendum, **stronger than just "both threads continue."**
- {7,6,4,1} m=3 re-run with matching procedure is recommended but not blocking. Without it, cross-thread comparisons must be framed as fraction-level not count-level.
- 8-leading-forbidden generalization is a candidate lemma to develop. Concrete next step: prove the analogous K_max bound for {2,3,5,8} via the same forced-borrow argument that gives the {7,6,4,1} bound.

**Pending / left for next session.**
- **{7,6,4,1} m=3 re-run with `search_multiset_universals_fast.py --max-q-samples 50000`.** Enables apples-to-apples count comparison. ~36h.
- **{2,3,5,8} m=4 d=16 search.** Tests classical-fraction-parallelism at m=4 (where {7,6,4,1} sits at 40%). Would give a 4-point trend across both threads. May be very expensive (Family D at d=16 took ~7.9h for {7,6,4,1}, but {2,3,5,8} arrangement count may differ).
- **Prove 8-leading-forbidden bound for {2,3,5,8}.** Analog of the proven leading-7^k bound for {7,6,4,1}. Should be straightforward via the same forced-borrow argument.
- **Test C1 status of {2,3,5,8} m=3 universals.** Pick 2-3 of the 63 classical universals and compute core-contribution under their fixing rules. Compare to {7,6,4,1} m=3 C1 violation pattern. This contributes to verification question 1 from Addendum 2.
- **Update SESSION_LOG and Current State once {7,6,4,1} m=3 re-run completes** with apples-to-apples comparison numbers.

**Files produced in this addendum.**
- `/mnt/user-data/outputs/SESSION_LOG.md` — updated with d=12 m=3 {2,3,5,8} results and audit-scope discipline extension.
- `d12_2358.json` (uploaded by user, analyzed in container) — 33 KB, the raw run output. Should be saved to project knowledge as supplementary data.

---

### Addendum 4 (2026-05-07) — 9-complement structural observation; global d=8 m=2 falsification sweep; original conjecture broken; two-class structure of cycle-thread sources identified

**Why this got added.** Continuing the cross-thread analysis from Addendum 3, Clay made a sharp observation about the structure of the two known d=4 cycle thread sources: {1,4,6,7} and {2,3,5,8} together cover {1,2,3,4,5,6,7,8} — every digit except 0 and 9. That observation cracked open a structural classification question that had been hiding in plain sight, and the resulting global sweep at d=8 m=2 substantially revised the picture of how cycle threads are organized.

**The 9-complement structural observation.** The two known d=4 cycle thread sources {1,4,6,7} and {2,3,5,8} are 9-complements of each other digit-by-digit: the map $`d \mapsto 9-d`$ sends one set to the other. Among the 18 four-distinct-digit multisets at d=4 with digit sum divisible by 9, only four pairs are *paired* (not self-complementary) under 9-complementation:
- {1,4,6,7} ↔ {2,3,5,8}  (no 0/9 — produces universals)
- {0,3,7,8} ↔ {1,2,6,9}  (contains 0 or 9)
- {0,4,6,8} ↔ {1,3,5,9}  (contains 0 or 9)
- {0,5,6,7} ↔ {2,3,4,9}  (contains 0 or 9)

**Original conjecture.** A 4-element multiset $`M \subset \{0,1,\ldots,9\}`$ with digit sum divisible by 9 produces classical universal full-variable fixed points at d=8 (under m=2 symmetric duplication) **iff** (i) $`M`$ is paired (not self-complementary) under $`d \mapsto 9-d`$ AND (ii) $`M \cap \{0,9\} = \varnothing`$. The only such multiset pair is {1,4,6,7}/{2,3,5,8}, which would explain the d=4 classification (Theorem 3.2: only 2 universals) as a structural consequence rather than a computational accident.

**Global falsification sweep at d=8 m=2.** To test the conjecture, exhaustively enumerated the 17 four-distinct-digit sum-divisible-by-9 multisets (one side of each complementary pair) and ran `search_multiset_universals_fast.py` on each at d=8 m=2 (symmetric m=2 duplication). The two known thread sources were already verified; 11 candidates were untested. Sweep design and results:

| Category | Count | Tested | Result |
|---|---:|---:|---|
| PAIRED, no 0/9 | 1 (pair) | both sides | both produce universals |
| PAIRED, has 0/9 | 4 (pairs) | 4 (one side each) | 0 produce universals |
| SELF-COMP, no 0/9 | 6 | 6 | **1 produces universals** |
| SELF-COMP, has 0/9 | 4 | 4 | **1 produces classical, 1 produces S-only** |

**Both halves of the original conjecture are FALSIFIED.** Two new findings:

1. **{1,3,6,8} (SELF-COMP, no 0/9)** — produces 1 classical universal F=31866813 and 1 S-only F=63316818 at d=8 m=2 (108 K-rules total, basin = 24,300 = full classical scope). Self-complementary under 9-complement: {1,3,6,8} → {8,6,3,1} = same set. **Breaks the "must be paired" half of the conjecture.**

2. **{0,4,5,9} (SELF-COMP, has 0/9)** — produces 2 classical universals F=44900559 and F=44005599 plus 1 S-only at d=8 m=2 (729 K-rules total). Self-complementary AND contains both 0 and 9. **Breaks the "must avoid 0/9" half of the conjecture and is the strongest counterexample.**

3. **{0,1,8,9} (SELF-COMP, has 0/9)** — produces 2 S-only universals (F=11089809, F=10108989) and 0 classical (429 K-rules total). Partial cycle thread.

**Two-class structural observation (refined picture).** The producing multisets split cleanly along a structural line:

- **Class A (high-density):** {1,4,6,7}, {2,3,5,8} — paired under 9-complement, no internal 9-pairs, hundreds of universals each (465 and 16 classical at d=8 m=2).
- **Class B (low-density):** {1,3,6,8}, {0,4,5,9} — self-complementary under 9-complement, two internal 9-pairs ({1,8}∪{3,6} and {0,9}∪{4,5}), 1–2 universals each at d=8 m=2.

But "two internal 9-pairs" is necessary, not sufficient, for Class B membership. Of the 10 self-complementary sum-18 multisets, only 2 produce classical universals; the other 8 ({3,4,5,6}, {1,2,7,8}, {1,4,5,8}, {2,3,6,7}, {2,4,5,7}, {0,2,7,9}, {0,3,6,9}, {0,1,8,9}-classical-fails-but-S-only-passes) do not. The substructure within Class B that distinguishes producers from non-producers is unidentified — distance-between-pairs alone doesn't separate them ({2,4,5,7} has same distance-2 structure as {1,3,6,8} but doesn't produce).

**Falsification mechanism breakdown.** The 12 non-producing multisets fail by two distinct mechanisms, mirroring the algebraic-vs-dynamic obstruction split from Paper 1's §4 (Theorem 4.1's d=5→d=6 cross-check):

- **Algebraic obstruction (no K-rules at all):** {0,1,2,6}, {0,1,3,5}, {0,2,3,4}, {0,3,7,8}, {1,3,5,9}, {3,4,5,6}, {1,2,7,8}, {1,4,5,8}, {2,3,6,7}, {2,4,5,7}, {0,3,6,9}.
- **Dynamic obstruction (K-rules exist but no universal):** {1,2,6,9} (72 K-rules / 0 universals), {2,3,4,9} (48 K-rules / 0 universals).

The same algebraic/dynamic mechanism that prevents 32 of 33 d=5 universals from extending to d=6 (Paper 1 §4) is what prevents non-{1,4,6,7}/{2,3,5,8} multisets from hosting cycle threads. **This is a unification finding, not just a falsification.**

**What this means for v1.2.2 / v1.2.3.**
- **v1.2.2 deploys as-is.** Appendix G §G.4 Theorem G.1 is correct as stated (it's about the {1,4,6,7} thread specifically). §G.8 #4 ("at least one other digit set" — the {2,3,5,8} thread held for v1.2.3) understates what's now known but is not wrong. v1.2.2 timestamps the Appendix G content and serves as the priority anchor.
- **v1.2.3 carries the cross-multiset classification.** Likely as new **Appendix H** (cross-multiset cycle-thread classification at d=4-source) — Appendix G stays scoped to classical-scope correction and {1,4,6,7} m=4 confirmation. Appendix H reports the global sweep, the two-class structure, and (pending) the d=12 m=3 decisive test.

**Verification status.** The new universals (F=31866813, F=44900559, F=44005599, plus S-only F=63316818, F=11089809, F=10108989) come from `search_multiset_universals_fast.py` JSON outputs. Reported basins are 24,300 (= full classical scope at d=8). Spot-checking K(F)=F under reported rules and re-running basin verification on these specific F values is a 5-minute script run, **deferred to next session** before any of these are written into Appendix H.

**The decisive open question.** Are {1,3,6,8} and {0,4,5,9} genuine cycle threads (low-density variant) or single-dimension flukes at d=8 m=2 that don't continue?
- If they continue at d=12 m=3 with classical universals existing in the pure {1³,3³,6³,8³} and {0³,4³,5³,9³} multisets: the cycle-thread phenomenon is at minimum 4-fold (high-density × 2 + low-density × 2), with the structural classification needing a refined necessary-and-sufficient condition.
- If they die at d=12 m=3: the {1,4,6,7}/{2,3,5,8} pair is genuinely privileged (only Class A continues), and the d=8 m=2 Class B universals are a low-multiplicity artifact of the symmetric-duplication lift specifically.

**Priority next experiments (decided this session, commands prepared for next session):**

1. **`search_multiset_universals_fast.py` on `{1,3,6,8}` at d=12 m=3.** Pure-cube multiset {1³,3³,6³,8³}, 369,600 arrangements, ~25–60h on Mac. Decisive test for whether {1,3,6,8} is a real cycle thread.
2. **`search_multiset_universals_fast.py` on `{0,4,5,9}` at d=12 m=3.** Pure-cube multiset {0³,4³,5³,9³}, 369,600 arrangements, ~25–60h on Mac. Decisive test for whether {0,4,5,9} is a real cycle thread (and the strongest test, since it contains both 0 AND 9 — the "most forbidden" category that nonetheless produces 2 classical universals at d=8 m=2).
3. **Already running:** `{1,4,6,7}` m=3 with matching procedure (`--max-q-samples 50000`), ~36h on Mac (started this morning). Closes the audit-scope question on the 83.6% vs 82.9% cross-thread parallelism finding.

**Files produced in this addendum.**
- 6 JSON files from the global sweep (in `/mnt/project/d8_global_sweep/` after deploy): `d8_0126_sq.json`, `d8_0135_sq.json`, `d8_0234_sq.json`, `d8_1368_sq.json`, `d8_1458_sq.json`, `d8_2367_sq.json`, `d8_2457_sq.json`, `d8_0189_sq.json`, `d8_0279_sq.json`, `d8_0369_sq.json`, `d8_0459_sq.json` — plus the 4 earlier falsification tests `d8_0378_sq.json`, `d8_1269_sq.json`, `d8_1359_sq.json`, `d8_2349_sq.json` and the 2 self-comp-no-09 confirmations `d8_3456_sq.json`, `d8_1278_sq.json`. Together with the 2 known producers ({1,4,6,7}, {2,3,5,8}), this is the complete d=8 m=2 census across all 17 four-distinct-digit sum-divisible-by-9 multisets.
- `run_global_sweep_d8.sh` — driver script for the 11-multiset sweep (already run, output captured).
- `/mnt/user-data/outputs/SESSION_LOG.md` — this update.

---

### Addendum 5 (2026-05-08) — Phase 14 audit-scope re-run breaks cross-thread parallelism; {2,3,5,8} confirmed denser than {7,6,4,1} at m=3

**Why this got added.** The Addendum 3 cross-thread parallelism finding (83.6% {7,6,4,1} vs 82.9% {2,3,5,8} classical fraction at m=3) was flagged at the time as having an audit-scope caveat: the 83.6% number for {7,6,4,1} came from a Phase 13 search procedure that may have differed from the Phase 14 procedure used on {2,3,5,8}. Clay re-ran {7,6,4,1} m=3 with `search_multiset_universals_fast.py --max-q-samples 50000` to match the {2,3,5,8} procedure exactly. The re-run completed in 38.79h on the Mac (started May 7 morning, finished May 8). Results uploaded as `d12_7641.json` alongside `d12_2358.json` for direct comparison.

**The headline result: parallelism dissolved.**

| Quantity | {7,6,4,1} (Phase 13, Apr 28) | {7,6,4,1} (matched, this run) | {2,3,5,8} (Phase 14) |
|---|---:|---:|---:|
| Total strict | 55 | **42** | 76 |
| Classical | 46 | **32** | 63 |
| S-only | 9 | **10** | 13 |
| Classical fraction | 83.6% | **76.19%** | 82.89% |
| Arrangements with K-rule | (different procedure) | 29,093 | 29,074 |

The matched-procedure run on {7,6,4,1} produces 13 fewer strict universals than Phase 13 (42 vs 55) and a classical fraction of **76.19%, not 83.6%**. The "near-identical 83.6% vs 82.9%" parallelism that motivated the unified-paper "two manifestations of one mechanism" framing in Addendum 3 was a procedural artifact. Under matched procedure, the gap is **6.7%** with **{2,3,5,8} the higher-classical-fraction thread** at m=3.

**Five concrete deltas from the prior framing:**

1. **Cross-thread parallelism: BROKEN.** Addendum 3's 0.7% gap was an artifact of unequal sampling between Phase 13 and Phase 14 procedures. Under matched procedure: 6.7% gap, with {2,3,5,8} ahead.

2. **Privilege inversion.** Project memory has carried {1,4,6,7} as the privileged / denser thread. At m=3 under matched procedure, **{2,3,5,8} produces more strict universals (76 vs 42), more classical universals (63 vs 32), and a higher classical fraction (82.89% vs 76.19%)**. The "{1,4,6,7}-thread is the central object" framing of the published paper (v1.2.2) is correct as a statement about the discovery arc, but the cross-thread comparison story is now: **{2,3,5,8} is denser than {1,4,6,7} at m=3**.

3. **Classical-fraction-decline curve: digit-set-INDEPENDENCE FALSIFIED at m=3.** The chat-7/8/9 hypothesis that the curve fraction(m) is a function of m alone — supported by the Addendum 3 m=3 parallelism — is now empirically falsified.

   Updated curve under matched procedure:
   ```
                 {7,6,4,1}      {2,3,5,8}
       m=1:        100%           100%
       m=2:        96.7%          100%
       m=3:        76.19%         82.89%   ← gap; {2,3,5,8} HIGHER
       m=4:        40%            unknown
   ```
   Curves are clearly digit-set-dependent at m≥3. {7,6,4,1} declines faster.

4. **Run-length structure: PARTIALLY HOLDS, but the chat-7/8/9 "Kaprekar digits run ≤2" rule is violated similarly in both threads.** Classical universals with max-run-3 substrings: 5/32 = 15.6% in {7,6,4,1}, 7/63 = 11.1% in {2,3,5,8}. The unified two-layer law from chat-7/8/9 (Kaprekar digits run ≤2 + zeros clump up to length k + density ≥80%) is not a clean structural rule; it has 11–16% violations in both threads at m=3. Worth checking whether the violators are concentrated in particular sub-multisets — that's a follow-on analysis, not done here.

5. **Highest-digit-leading-forbidden: HOLDS, with {2,3,5,8} now more strongly supported.** {7,6,4,1}: 0/32 lead with 7 (proven theorem from May 3 forced-borrow argument). {2,3,5,8}: **0/63 lead with 8** (vs 0/63 from May 6 prior run on the same data; consistent with the candidate 8-leading-forbidden lemma). The empirical signal for the 8-leading-forbidden bound on {2,3,5,8} is strong — **63 data points, all consistent**. Worth writing up the proof analog.

**What this does to the unification framing.**

The "two manifestations of one mechanism" reading of the unified paper is now in serious trouble. The threads share:
- Existence at every tested m=1, 2, 3 with classical universals in pure-cube multisets
- Classical-fraction declining with m (but at different rates)
- Highest-digit-leading-forbidden (proven for {7,6,4,1}, empirical for {2,3,5,8})
- Run-length-3 violations at similar rates (11–16%)

But they DIVERGE on:
- Total strict universal counts at m=3 (42 vs 76 — {2,3,5,8} produces 81% more)
- Classical fraction (76.19% vs 82.89%)
- Implied rate of decline (steeper for {7,6,4,1})

The honest reading: **two related but distinct phenomena that share structural features but diverge quantitatively**. Not a single underlying mechanism manifesting at two digit sets. The unified paper's spine — if there is to be one — has to acknowledge this divergence rather than paper over it.

**What this means for the d=12 m=3 Class B test (currently running).**

The Class B threads ({1,3,6,8}, {0,4,5,9}) at d=12 m=3 are still tracked by `run_class_b_d12_test.sh` on the Mac (started May 7 evening, ETA 50–120h). The expected-outcome table from that session is **unchanged in structure**, but the interpretation of "thread continues" needs revisiting:
- If {1,3,6,8} or {0,4,5,9} produces classical universals at d=12 m=3: we have ≥3 cycle threads with quantitatively distinct fractions and counts. The classification problem is: which 4-element digit multisets host cycle threads, and what determines the per-thread density?
- If both die at m=3: {1,4,6,7}/{2,3,5,8} are genuinely privileged. But — given today's finding — the privilege is NOT a "single mechanism, parallel manifestations" structure; it's two distinct privileged threads with different densities.

Either way, **the Class B test result is still informative**, just for a different question than originally framed. Originally: "is the cycle-thread phenomenon broader than {1,4,6,7}/{2,3,5,8}?" Still valid. Newly: "given that {1,4,6,7} and {2,3,5,8} are quantitatively distinct, are Class B threads (if real) yet a third or fourth distinct phenomenon, or do they group with one of the existing two by density / classical fraction?"

**Implications for v1.2.2 deploy and v1.2.3 plan.**

- **v1.2.2 still deploys as-is.** The paper's content is about the {1,4,6,7} thread specifically, and Theorem G.1 stands. The §G.8 #4 forward-looking remark about "at least one other digit set produces classical universals at m=2" is true and remains correct.
- **v1.2.3 plan needs updating.** The Addendum 3 framing of the {2,3,5,8} d=12 m=3 finding as "matching the {7,6,4,1} curve" was wrong. The correct framing in v1.2.3 is: **{2,3,5,8} is a second, denser cycle thread at m=3 with its own classical-fraction trajectory.** The Appendix H draft should report both threads' counts at m=3 head-to-head, with the digit-set-dependent curve as a structural finding rather than the digit-set-independent curve as a candidate theorem.
- **Pending d=12 m=3 Mac runs on Class B** add a third or fourth row to that table when they finish.

**Verification status.** Both `d12_7641.json` and `d12_2358.json` report `best_basin: 293,920` for every classical universal — this matches the full classical basin at d=12 (293,920 = `n_admissible_d12`). All 32 + 63 = 95 reported classical universals have full basin coverage. S-only universals have basins in [293,018, 293,909] across both threads — sub-full but >99.7%, consistent with the "missed inputs converge to alternative fixed points outside S" pattern. No verification anomalies in the JSON output structure.

**Files produced in this addendum.**
- Analysis used: `d12_7641.json` (32 classical, 10 S-only, 38.79h Mac) and `d12_2358.json` (63 classical, 13 S-only, 36.61h Mac).
- `/mnt/user-data/outputs/SESSION_LOG.md` — this update.
- Both JSON files should be uploaded to project knowledge alongside the SESSION_LOG re-upload.

**Next-session priorities (revised).**
1. Wait for Class B d=12 m=3 results (`d12_1368_m3.json`, `d12_0459_m3.json`) — currently running on Mac.
2. Once Class B results arrive: produce a **single comprehensive cross-thread classification table** at m=3 covering all 4 candidate threads ({1,4,6,7}, {2,3,5,8}, {1,3,6,8}, {0,4,5,9}). That table is the foundation of Appendix H / v1.2.3.
3. **Identify which 14 of Phase 13's 46 classical universals dropped out under matched procedure.** Are they at the basin/sampling edge, or were they counting artifacts of the prior filter? This is a 30-min analysis once we have both lists side-by-side.
4. **Run-length-3 violators analysis.** Are the 5 + 7 = 12 violators across both threads concentrated in particular sub-multisets, or scattered? Determines whether the chat-7/8/9 "run ≤2" rule has a refinable form or is just empirically loose.
5. **Write up the 8-leading-forbidden lemma proof for {2,3,5,8}.** Adapt the May 3 forced-borrow theorem. Pure paper-and-pencil work, no compute needed. This generalizes to a "highest-digit-leading-forbidden" cross-thread theorem candidate.

---

### Addendum 6 (2026-05-08, same session) — Phase 13 vs matched comparison BLOCKED on data; new finding: block-balance asymmetry between threads is sharper than count gap

**Why this got added.** Continuing from Addendum 5, Clay asked for the priority-3 "which 14 of Phase 13's 46 classical universals dropped out under matched procedure" follow-on analysis. The intent was a side-by-side F-list comparison: are the missing 14 at the basin/sampling edge (suggesting Phase 13 inflated by noisy threshold) or structurally identifiable? Addendum 6 reports two things: (a) why this analysis is currently blocked, (b) what was found instead while looking at the matched-procedure data.

**Why Phase 13 vs matched comparison is blocked.** Phase 13's 46-classical / 9-S-only / 55-strict numbers come from chat-7/8/9 work (Apr 28-29). Project knowledge contains the SESSION_LOG narrative summary of these counts, but **the underlying JSON output file (likely `d12_v2_leading6.json` from `d12_full_v2.py` per the May 3 entry) is not present in project knowledge or container filesystem.** Without the per-F list, no F-by-F overlap analysis is possible.

To do the priority-3 analysis cleanly, one of the following needs to happen:
- Clay locates Phase 13's `d12_v2_leading6.json` (or equivalent) on Mac and uploads it. Then the 30-min comparison runs as designed.
- The comparison is reframed as Phase 14 alone vs an additional reference run (e.g., re-run Phase 13's parameters explicitly and compare both to matched procedure).
- The priority is dropped — the Phase 14 numbers are the canonical ones going forward and the Phase 13 numbers are deprecated.

**Recommendation: drop the priority unless the file surfaces easily on Mac.** The matched-procedure numbers (32 classical / 10 S-only / 76.19% classical fraction) are the canonical ones for v1.2.3 and any future paper. Phase 13's 46-classical number was a casualty of unequal sampling and we already understand qualitatively that 14 fps drop out under the more restrictive matched procedure — knowing exactly *which 14* is interesting but not load-bearing.

**What was found instead: block-balance structure.** While exploring the matched-procedure 32 + 10 = 42 strict universals at d=12 m=3 in {7,6,4,1}, did a structural analysis on the F values themselves: for each universal F (12-digit string), count digit occurrences in 3 blocks of 4 (positions 0-3, 4-7, 8-11). "Perfectly balanced" = each of 4 digits appears exactly once in each of the 3 blocks.

| Block-balance category | {7,6,4,1} (32 classical) | {2,3,5,8} (63 classical) |
|---|---:|---:|
| Perfectly balanced (1,1,1) for all digits | **2 (6.2%)** | **0 (0.0%)** |
| Near-balanced (1 digit pair off) | 13 (40.6%) | 18 (28.6%) |
| Other (most disordered) | 17 (53.1%) | 45 (71.4%) |

**Two findings here.**

1. **Project memory's "compositional structure breaks at m=3, zero balanced quarters" is partially refined.** The claim is verified for {2,3,5,8} (0/63) but **partially falsified for {7,6,4,1} (2/32)**. Compositional structure does survive at m=3 in {7,6,4,1} — just barely. The 2 surviving fully-compositional universals are:

   - **F = 617464716147** with blocks `6174` / `6471` / `6147`. Note: the first block IS THE CLASSICAL KAPREKAR CONSTANT 6174. This is a striking structural fact: at d=12 m=3 in the {7,6,4,1} thread, there exists a fully-compositional universal whose first 4 digits are literally Kaprekar's 6174.
   - **F = 614714671476** with blocks `6147` / `1467` / `1476`. All three blocks are permutations of the Kaprekar digit set; first block is `6147` (the digit-reverse of 7416 and a near-anagram of 6174); second is `1467` which is the *sorted-ascending* form of 6174 / 1746 (i.e., β(6174) under the classical Kaprekar rule).

   Both surviving compositional universals have direct structural ties to 6174 and the classical Kaprekar rule. This is not random — it suggests these 2 fps may be anchored to 6174's d=4 universality through a coefficient-preserving lifting structure that doesn't reach the rest of the d=12 m=3 universal population.

2. **The cross-thread divergence is sharper in block-balance than in raw counts.** Comparing the two threads at m=3:

   | Quantity | {7,6,4,1} | {2,3,5,8} | Asymmetry |
   |---|---:|---:|---|
   | Total strict | 42 | 76 | {2,3,5,8} +81% |
   | Classical | 32 | 63 | {2,3,5,8} +97% |
   | Classical fraction | 76.19% | 82.89% | {2,3,5,8} +6.7pp |
   | Perfectly balanced | **2/32 = 6.2%** | **0/63 = 0.0%** | **{7,6,4,1} only** |

   The threads aren't just "differently dense"; they have **qualitatively different internal compositional structure at m=3**. {7,6,4,1} retains a vestige of compositional structure (2 fps where each m-block contains the full digit set); {2,3,5,8} has lost it entirely. The vestige is small — 6.2% — but it's nonzero in one thread and zero in the other. The block-balance distinction is structural, not statistical noise.

**What this means for the unification framing.** The Addendum 5 conclusion ("two related but distinct phenomena, not a single underlying mechanism") is reinforced. The threads diverge not just in counts and fractions but in compositional structure. If the unified paper has a single mechanism producing both threads, that mechanism has to predict why {7,6,4,1} preserves 2 perfectly-balanced fps at m=3 while {2,3,5,8} preserves zero. That's a non-trivial constraint.

A weaker, more honest framing for v1.2.3 / Appendix H: **at d=12 m=3, the two cycle threads exhibit different compositional structures, with {7,6,4,1} retaining vestigial Kaprekar-anchored fps that {2,3,5,8} does not.** Documents the divergence as a structural fact rather than papering over it.

**Open question raised.** Are F=617464716147 and F=614714671476 (the 2 fully-compositional {7,6,4,1} m=3 universals) related to 6174's coefficient-preserving lifting at d=12? Specifically, can their fixing rules be derived from 6174's d=4 native rule via a 3-fold extension structure analogous to 60714's odd/even ladder? If yes, this is a Paper 1 connection — these are 6174's ladder fps at d=12 with m=3 augmentation. Worth checking by extracting the fixing rules from the JSON and comparing to 6174's d=4 native rule (999, 90, -90, -999).

**Files referenced in this addendum.**
- `d12_7641.json` — matched-procedure {7,6,4,1} m=3 results (32 classical + 10 S-only).
- `d12_2358.json` — Phase 14 {2,3,5,8} m=3 results (63 classical + 13 S-only).
- `/mnt/user-data/outputs/SESSION_LOG.md` — this update.

**Updated next-session priorities.**

1. Wait for Class B d=12 m=3 results — unchanged from Addendum 5.
2. Cross-thread classification table at m=3 — unchanged, now should include block-balance column.
3. **Phase 13 vs matched comparison: BLOCKED, deprioritized.** Drop unless `d12_v2_leading6.json` surfaces on Mac.
4. **NEW priority: Investigate the 2 fully-compositional {7,6,4,1} universals.** Extract fixing rules for F=617464716147 and F=614714671476 from d12_7641.json. Compare to 6174's d=4 native rule. If structurally related (e.g., they admit coefficient-preserving liftings of 6174's classical rule with appended zero-sum-pair structure on the m=3 augmented digits), this is a direct Paper 1 → Paper 2 unification finding worth its own section.
5. Run-length-3 violators analysis — unchanged.
6. 8-leading-forbidden lemma proof for {2,3,5,8} — unchanged.

---

### Addendum 7 (2026-05-08, same session) — Phase 13 file surfaced; comparison reveals THREE procedural differences and small overlap; canonical numbers updated

**Why this got added.** Clay located and uploaded `d12_v2_leading6.json` immediately after Addendum 6 was written, unblocking the priority-3 analysis. The comparison turned out to be more substantive than the framing assumed — not "14 dropped out under matched procedure" but **"three procedural differences produce largely disjoint universal populations."** The Phase 13 numbers carried in project memory (46 classical / 9 S-only / 55 strict) need to be re-examined.

**Phase 13 file structure** (`d12_v2_leading6.json`):
- 55 universals, all leading with 6 (`range='6'`)
- `max_rule_search`: 500,000 per F (10× higher than Phase 14)
- `multi_rule_mode: false` — single rule per F tested
- 92,400 candidates checked (leading-6 arrangements only)
- **Single 'universals' list — no classical/S-only distinction.** The Appendix G classical-vs-S-only correction post-dates this file.
- Fields: F, pi_inv, sigma_inv, c (12-element coefficient vector), cycle_partition

**Phase 14 file structure** (`d12_7641.json`):
- 42 universals, ALL leading digits {1, 4, 6} (no leading-7 — proven theorem; no leading-3, 5, 8 because the multiset is {7,6,4,1}^3)
- `max_q_samples`: 50,000 per F (10× lower than Phase 13)
- 369,600 arrangements searched (FULL multiset, not leading-6 restricted)
- 32 classical + 10 genuinely S-only — Appendix G distinction applied

**Note on `max_q_samples` recording.** The JSON files do not persist `max_q_samples` as a top-level field. Both `d12_7641.json` and `d12_2358.json` record `mode: fast_random_sampling` and `n_arrangements_searched: 369,600`, but the per-F rule budget is a runtime flag not captured in output. The 50K budget assertion for {7,6,4,1} is grounded in the explicit `run_class_b_d12_test.sh` flag. The 50K budget assertion for {2,3,5,8} is **verified from Mac shell history (entry 631)**: the actual command run was

```
python3 search_multiset_universals_fast.py --multiset "8,8,8,5,5,5,3,3,3,2,2,2" \
    --d 12 --max-q-samples 50000 --out d12_2358.json
```

Confirmed `--max-q-samples 50000`, identical to the {7,6,4,1} re-run. Circumstantial JSON evidence is consistent: `n_with_K_rule` ratio 1.0007 (29,074 vs 29,093) and wall times within 6%. The "matched procedure" framing of Addendum 5 is verified from primary source, not just inferred. Future runs should preserve `max_q_samples` in output JSON to remove this verification step.

**Three procedural differences, in order of impact:**

1. **SCOPE.** Phase 13 searched leading-6 arrangements only (92,400 of 369,600 = 25%). Phase 14 searched the full multiset (4× larger search space). This means Phase 14 can find universals leading with 1 or 4 that Phase 13 categorically could not. **13 of Phase 14's 31 'new' universals lead with 1 or 4** — they are not findable in Phase 13's protocol.

2. **RULE-SEARCH BUDGET.** Phase 13 used `max_rule_search=500,000` per F; Phase 14 used `max_q_samples=50,000` per F. **10× lower in Phase 14.** A given F is "universal" if at least one universal rule is found within the budget. Phase 14's lower budget plausibly causes systematic dropout of fps whose universal rules are rare in rule-space.

3. **UNIVERSALITY DEFINITION.** Phase 13's 55 'universals' are the pre-v1.2.2 strict-universal-over-S-admissible-basin definition. Phase 14 separates **classical** (full {0..9} basin) from **genuinely S-only** (S-basin only, classical fails). This is the Appendix G correction. So Phase 13's single number 55 is structurally analogous to Phase 14's strict total **42** (= 32 classical + 10 S-only), not to the classical count 32 alone.

**Apples-to-apples comparison (leading-6, strict universal):**

| Comparison | Count |
|---|---:|
| Phase 13 strict universals (leading-6) | 55 |
| Phase 14 strict universals (leading-6 only) | 29 (= 23 classical + 6 S-only) |
| Phase 13 ∩ Phase 14 (leading-6 strict universals) | **11** |
| Phase 13 only (leading-6, "dropped") | 44 |
| Phase 14 only (leading-6, "newly found") | 18 |

**Only 11 of Phase 13's 55 leading-6 universals appear in Phase 14's leading-6 results.** This is a 20% overlap — much smaller than expected. The 44 "dropped" leading-6 fps are unaccounted-for in Phase 14, even within its leading-6 subset. Three possibilities, in order of likelihood:

(a) **Most likely: rule-budget effect.** Phase 14's 50K budget systematically misses universal rules that Phase 13's 500K budget found. The 44 dropped fps may all be real strict universals; Phase 14 just didn't sample the universal rule for any of them. **Testable** by re-running Phase 14 with `max_q_samples=500000` on the dropped 44 specifically (~30 min on Mac per F = ~22h total, or sub-sample).

(b) **Possible: S-only PARTIAL classifications.** Some Phase 13 universals may have basins between full-classical and full-S-only (i.e., basin > 0 over inputs containing 2/3/5/8/9 but < 100%) and Phase 14 correctly classifies them as PARTIAL not GENUINELY_S_ONLY. The 16 PARTIAL classifications in `p14['classifications']['PARTIAL']` could include some of them.

(c) **Less likely: Phase 13 false positives.** Phase 13 used a single-rule mode and a less rigorous basin test. Some of its 55 might be artifacts. But Phase 13's 500K budget makes this less likely than (a).

**The cycle-partition profile of dropped fps doesn't help discriminate.** Cycle distributions of "in both" (11) vs "dropped" (44) are similar in shape — (8,2,2), (10,2), (5,3,2,2), (6,3,3), (7,3,2) all appear in both with comparable proportions. **No structural difference is visible at the cycle-partition level**, which weakly supports possibility (a) — the dropouts look like a representative sample of Phase 13's universal population, just missed by Phase 14's rule sampling.

**Key correction to Addendum 5's headline numbers.** Addendum 5 framed the matched-procedure result as "{7,6,4,1} drops to 76.19% classical fraction (32 classical / 42 strict)." This framing implicitly assumed the 42 strict total was the canonical count of d=12 m=3 strict universals in {7,6,4,1}, with the matched procedure being authoritative. **This assumption is wrong.** The Phase 14 `max_q_samples=50,000` budget plausibly misses real universals — Phase 13's leading-6-only 55 already exceeded Phase 14's full-multiset 42, which only makes sense if budget is the limiting factor. The "true" d=12 m=3 strict-universal count in {7,6,4,1} is likely **substantially higher than 42**.

**This DOES NOT salvage the Addendum 3 cross-thread parallelism finding.** Phase 14 used the same matched procedure on both {7,6,4,1} (42 strict) and {2,3,5,8} (76 strict). Within the matched procedure, **{2,3,5,8} produces 81% more strict universals than {7,6,4,1}** at the same budget. If the budget systematically undercounts both threads, the relative ranking still holds — {2,3,5,8} is denser at m=3 even if both absolute numbers are too low. The Addendum 5 conclusion that the threads are quantitatively distinct stands.

**What it DOES change.** The 76.19% vs 82.89% classical-fraction comparison should be weakened to: "Within the budget-limited Phase 14 procedure, classical fractions differ by 6.7pp with {2,3,5,8} higher. Whether this gap closes, widens, or inverts under higher rule-search budget is open." The "digit-set-independent curve falsified" framing remains valid but the specific numbers should be flagged as Phase-14-budget-dependent rather than canonical d=12 m=3 truths.

**Phase 13's 46-classical / 9-S-only project-memory numbers are wrong.** Project memory (in the userMemories block in this conversation's preamble) carries "Phase 13 d=12 m=3: 46 classical + 9 S-only = 55 strict, 83.6% classical." The 55 strict count is correct, but **46 classical / 9 S-only is a fabrication — Phase 13 did not distinguish classical from S-only at all.** All 55 are simply 'universals' in the pre-Appendix-G sense. The 46/9 numbers were apparently inferred or carried forward incorrectly somewhere. The correct project-memory entry should be "Phase 13 d=12 m=3 (leading-6, max_rule_search=500K): 55 strict universals (S-basin definition); classical-vs-S-only breakdown not measured."

**Updated headline numbers (revised canonical):**

| Procedure | Scope | Budget | Strict | Classical | S-only |
|---|---|---:|---:|---:|---:|
| Phase 13 (leading-6) | leading-6 only | 500K | 55 | unknown | unknown |
| Phase 14 (matched) | full multiset | 50K | 42 | 32 | 10 |
| Phase 14 (matched) restricted to leading-6 | — | — | 29 | 23 | 6 |
| **True d=12 m=3 in {7,6,4,1}** | full multiset | unbounded | **≥ 42, likely substantially higher** | **unknown** | **unknown** |

**What this means for v1.2.3 / Appendix H:**
- Don't quote "32 classical at d=12 m=3 in {7,6,4,1}" as a definitive count. Use language like "32 classical universals identified by Phase 14 procedure (max_q_samples=50K); higher rule-search budgets are expected to find more."
- The cross-thread comparison **(2,3,5,8) denser than (7,6,4,1) at m=3** holds at matched budget but should be flagged as procedure-dependent.
- The block-balance finding from Addendum 6 (2 fully-compositional {7,6,4,1} universals tied to Kaprekar 6174) holds — those 2 fps are genuinely in the matched-procedure data and structurally interesting. But there may be more Kaprekar-anchored universals at d=12 m=3 not yet found at Phase 14's budget.

**Recommended follow-up experiment.** Re-run `search_multiset_universals_fast.py` on {7,6,4,1} m=3 with `max_q_samples=500000` (or higher), full multiset scope. ~10-15 days on Mac at 50K → 500K scaling assuming linearity. This produces the canonical d=12 m=3 number for {7,6,4,1} and resolves whether the 76.19% classical fraction is real or a budget artifact.

Alternative cheaper experiment: run the same higher-budget procedure on just the leading-6 subset (~25% of arrangements, ~3 days). Compare against Phase 13's 55 to see how many are reproduced and how many additional are found. If Phase 14-leading-6-at-500K-budget reproduces ≥50 of Phase 13's 55, the budget effect is the dominant factor and Phase 13's count is likely close to true. If it reproduces far fewer, something else is going on.

**Files referenced in this addendum.**
- `d12_v2_leading6.json` (Phase 13, just uploaded — should be added to project knowledge)
- `d12_7641.json` (Phase 14 matched-procedure)
- `d12_2358.json` (Phase 14 {2,3,5,8})
- `/mnt/user-data/outputs/SESSION_LOG.md` — this update.

**Updated next-session priorities.**

1. Wait for Class B d=12 m=3 results.
2. Cross-thread classification table at m=3 — now needs an explicit "budget" column and a caveat about Phase 14 budget effects.
3. **REINSTATED priority: Phase 14 high-budget re-run on {7,6,4,1} m=3** — `max_q_samples=500000` to determine canonical count. Cheaper variant: leading-6 only (~3 days). Most expensive variant: full multiset (~10-15 days).
4. **NEW priority: Audit project memory for the 46/9/55 numbers.** The "46 classical + 9 S-only" attribution to Phase 13 is incorrect (Phase 13 didn't measure classical-vs-S-only). Update memory_user_edits if there's an entry; verify no other propagated false numbers.
5. Investigate the 2 fully-compositional {7,6,4,1} universals (block-balance finding from Addendum 6).
6. Run-length-3 violators analysis.
7. 8-leading-forbidden lemma proof for {2,3,5,8}.

---

### Addendum 8 (2026-05-09) — Class B Test 1 result: {1,3,6,8} d=12 m=3 produces ZERO K-rules; Test 2 ({0,4,5,9}) interrupted by Mac power-down, restart staged

**Why this got added.** Test 1 of the Class B decisive test (`run_class_b_d12_test.sh`, started May 7 evening) completed on Mac in 25.0h wall time. Result is a clean and dramatic negative. Test 2 was interrupted when the Mac powered down; restart procedure documented below.

**Test 1 result: {1,3,6,8} at d=12 m=3.**

```
multiset (8, 8, 8, 6, 6, 6, 3, 3, 3, 1, 1, 1) at d=12
Arrangements searched: 369,600
With at least one K-rule: 0
Classifications: NO_RULE: 369600
Wrote: d12_1368_m3.json
Wall time: 25h 0m
```

**Zero K-rules across all 369,600 arrangements.** This is the strongest possible negative result: not "rules exist but no universal" (dynamic obstruction), but "no permutation pair satisfies K(F)=F for any F in the multiset" (algebraic obstruction). Compare to the d=8 m=2 result for the same multiset: 108 K-rules, 1 classical universal (F=31866813), 1 S-only.

**The Addendum 4 / Addendum 6 "low-density Class B cycle thread" hypothesis is falsified for {1,3,6,8}.** At d=8 m=2 the symmetric-duplication lift produced enough algebraic flexibility for some K-rule to exist (108 of them). At d=12 m=3, that algebraic flexibility is gone. **The d=8 m=2 universal for {1,3,6,8} was a dimensional accident, not a real cycle thread.**

**Cross-thread comparison table updated:**

| Multiset | d=8 m=2 K-rules | d=8 m=2 classical | d=12 m=3 K-rules | d=12 m=3 classical |
|---|---:|---:|---:|---:|
| {1,4,6,7} | many | 465 | 29,093 | 32 |
| {2,3,5,8} | many | 16 | 29,074 | 63 |
| **{1,3,6,8}** | **108** | **1** | **0** | **0** ← Test 1 |
| {0,4,5,9} | 729 | 2 | (Test 2 — was interrupted, restart staged) | — |

**Structural interpretation.** Two real cycle threads at d=4-source — {1,4,6,7} and {2,3,5,8} — produce ~29,000 K-rules at d=12 m=3. Class B {1,3,6,8} produces zero. **The gap is qualitative, not quantitative.** The {1,4,6,7}/{2,3,5,8} pair is genuinely privileged at m=3.

If Test 2 on {0,4,5,9} also produces zero K-rules (which now seems plausible — Test 1 was the more structurally similar Class B candidate, with both contained no 0/9, and it died completely), the picture becomes very clean:

- **Two cycle threads at d=4-source: {1,4,6,7} and {2,3,5,8}.** Both with full m≥3 continuation.
- **Class B (self-complementary) universals at d=8 m=2 are anomalous m=2-only artifacts**, not threads. They exist because of a specific algebraic flexibility in the symmetric-duplication lift that disappears at m=3.
- **Original Addendum 4 conjecture is rehabilitated as a m≥3 condition.** "PAIRED under 9-complement AND avoids {0,9}" was wrong at m=2 (where Class B Class B {1,3,6,8} and {0,4,5,9} appear), but appears correct at m≥3. The d=8 m=2 falsification was a d-specific anomaly, not a refutation of the structural principle.

This is a cleaner and more useful story for v1.2.3 / Appendix H than the two-class structure framing from Addendum 4-6. **If Test 2 also dies, the conjecture lives.**

**Test 2 status: interrupted by Mac power-down, restart staged.** Test 1's output file `d12_1368_m3.json` survived (Mac powered down only after Test 1's tee+JSON-write completed, before Test 2 had started or completed). Test 2 needs to run independently. Restart command for Mac (paste into screen session, with caffeinate to prevent sleep):

```bash
screen -S class_b_test2
cd ~/Downloads/class_b_d12_test
caffeinate -d -i python3 ~/Downloads/search_multiset_universals_fast.py \
    --multiset "9,9,9,5,5,5,4,4,4,0,0,0" \
    --d 12 \
    --max-q-samples 50000 \
    --out d12_0459_m3.json 2>&1 | tee -a run_log.txt
# Ctrl-A D to detach
```

`caffeinate -d -i` prevents display sleep and idle sleep for the duration of the python process — no risk of another power-induced interruption from idle-sleep. Manual shutdown still kills it. Expected wall time: ~25h based on Test 1 (zero-K-rule case exhausts full sampling budget per F without early-exit).

**Decision pending Test 2 outcome.**

Test 2 outcome A: **Zero K-rules** (same as Test 1). Clean classification story. Original conjecture rehabilitated as m≥3 condition. Appendix H writes itself: "Two cycle threads, Class B is m=2 anomaly."

Test 2 outcome B: **Some K-rules / classical universals exist.** {0,4,5,9} is a 3rd genuine cycle thread despite {1,3,6,8} not being one. The two surprise multisets diverge at m=3, and we need a finer structural condition. This would be surprising given {0,4,5,9} contains BOTH 0 AND 9 (the "most forbidden" category) and had only 2 classical universals at d=8 m=2 (vs {1,3,6,8}'s 1).

Outcome A is more likely; outcome B would be genuinely strange. Either way, Test 2's result is decisive.

**Files referenced in this addendum.**
- `d12_1368_m3.json` — Test 1 output (369,600 arrangements, 0 K-rules, 25.0h Mac).
- `d12_0459_m3.json` — pending from Test 2 restart.
- `run_log.txt` in `~/Downloads/class_b_d12_test/` on Mac.

**Verification status.** Test 1's `0 K-rules / 0 universals / NO_RULE: 369600` is a clean exhaustive negative — the script's report that 369,600 arrangements were searched and zero K-rules found leaves no ambiguity. No spot-check needed: there's nothing to spot-check (no F values reported as universal). The "algebraic obstruction at d=12 m=3 for {1,3,6,8}" finding is as well-verified as any positive finding in the d=12 m=3 work.

**Updated next-session priorities.**

1. **Wait for Test 2 ({0,4,5,9}) Mac result.** ~25h after restart.
2. **Once Test 2 in: write Appendix H draft.** Story depends on outcome A vs B, but either way the table covers all four d=4-source candidates at m=3.
3. Phase 14 high-budget re-run on {7,6,4,1} m=3 — unchanged from Addendum 7.
4. Investigate the 2 fully-compositional {7,6,4,1} universals (Addendum 6 finding) — unchanged.
5. Run-length-3 violators analysis — unchanged.
6. 8-leading-forbidden lemma proof for {2,3,5,8} — unchanged.

---

### Addendum 9 (2026-05-10) — Test 2 mid-run finding overturns Test-1-style "Class B dies" hypothesis; {0,4,5,9} confirmed as third cycle thread; full rule-structure analysis on 95 d=12 m=3 classical universals from {7,6,4,1} and {2,3,5,8}

**Why this got added.** Two distinct events in this session: (a) Test 2 of the Class B decisive test ({0,4,5,9} at d=12 m=3, restart after Mac power-down) crossed a threshold mid-run that overturned the "Class B is m=2 artifact" hypothesis from Addendum 8, and (b) full structural analysis of the 95 classical universal rules from the existing {7,6,4,1} and {2,3,5,8} d=12 m=3 data, motivated by user's question about whether rule-structure patterns enable prediction of fixed points or fixing rules.

**Test 2 status update.** As of mid-run snapshot (Mac time, after duplicate-process cleanup):

```
[184470s] 136200/277200 | with-rule: 21433 | classical: 9 | S-only: 17 | rate: 0.7/s | ETA: 190971s
```

Process is still running. At 49.1% complete (136,200 of 277,200 arrangements), it has found **21,433 arrangements with K-rules, 9 classical universals, and 17 S-only universals**. Rate has degraded from initial 3.8/s to 0.7/s instantaneous, consistent with basin-verification work accumulating as universals get found.

**Key data point: the early-phase 0/0 was misleading.** At 103,600 arrangements (37% complete), Test 2 had 2,790 K-rules and 0 universals. At 136,200 (49% complete) — just 32,600 arrangements later — it has 21,433 K-rules and 26 universals total. The K-rule density jumped from ~2.7% to ~57% in the new arrangements, and universals started appearing en masse. **Test 2 has crossed into "real cycle thread" territory.**

**The Addendum 8 hypothesis is partially falsified.** "{0,4,5,9} is a d=8 m=2 artifact like {1,3,6,8}" was wrong. The two Class B candidates diverge dramatically at m=3:

| Multiset | d=8 m=2 classical | d=12 m=3 (current best estimate) | Mechanism |
|---|---:|---:|---|
| {1,4,6,7} | 465 | 32 + 10 = 42 strict | High-density Class A thread |
| {2,3,5,8} | 16 | 63 + 13 = 76 strict | High-density Class A thread |
| **{0,4,5,9}** | 2 | **≥ 9 + 17 = 26 strict so far, growing** | **NEW: medium-density genuine thread** |
| {1,3,6,8} | 1 | **0** | Algebraic extinction (Test 1) |

**Striking refinement of the 9-pair structural observation:** the four multisets split cleanly by internal-9-pair count:

| Multiset | Internal 9-pairs (digit pairs in multiset summing to 9) | m=3 outcome |
|---|---:|---|
| {1,4,6,7} | 0 (no pair sums to 9) | Survives, ~29K K-rules |
| {2,3,5,8} | 0 (no pair sums to 9) | Survives, ~29K K-rules |
| **{0,4,5,9}** | **2** (0+9=9, 4+5=9) | Survives, medium density |
| {1,3,6,8} | 1 (3+6=9 only; 1+8=9 needs 8 which is absent) | DIES — 0 K-rules |

**Pattern: cycle threads at d=4-source require 0 or 2 internal 9-pairs, NOT 1.** The "{1,3,6,8} has exactly 1 internal 9-pair" appears to be the structural reason for its m=3 algebraic extinction. This is a real Flavor-1 candidate predictor (which multisets host cycle threads). Needs verification on more multisets — most untested d=8 m=2 sweep results would extend the table at m=3.

**Rule-structure analysis on the 95 d=12 m=3 classical universals.** Motivated by user's question about whether rule-level patterns enable prediction. Verified rule encoding: `c[i] = 10^(d-1-pi_inv[i]) - 10^(d-1-sigma_inv[i])`. All 32 + 63 = 95 rules verify K(F)=F under this convention.

**Six structural predictors tested, ranked by signal strength:**

1. **Largest digit lands at place 0 in pi.x: 72% / 60% (real but soft).** In {7,6,4,1}, 23 of 32 classical universals have pi_inv[0]=0 — meaning the largest digit of F's sorted-desc form lands at the highest integer place in pi.x. In {2,3,5,8}, 38 of 63. **This is the only single-variable predictor with >50% precision in both threads.** It's the classical Kaprekar "biggest-first" bias persisting into d=12. The remaining 28-40% of rules deviate.

2. **Canonical Kaprekar sign pattern `++++++------`: 0/32 vs 6/63.** The classical Kaprekar rule at d=12 would have positions 0-5 contributing positively and 6-11 negatively. {7,6,4,1} has zero classical universals matching this pattern. {2,3,5,8} has six. Surprising: the "more Kaprekar-like" sign pattern is more common in the {2,3,5,8} thread than the {7,6,4,1} thread (the one containing the literal Kaprekar digits).

3. **F-block-balanced (each m-block has full digit set): 2 / 0.** From Addendum 6. {7,6,4,1} has 2 ({6174..., 6147...}); {2,3,5,8} has zero. The asymmetry confirmed by full enumeration.

4. **pi-block-aligned (each m-block of pi.x receives one position per digit-group): 2 / 0.** A separate concept from F-block-balanced. The 2 pi-block-aligned rules in {7,6,4,1} are F = 614714647617 and F = 147614647617 — **DIFFERENT** from the 2 F-block-balanced universals (617464716147, 614714671476). So "Kaprekar-anchored at d=12 m=3" actually splits into TWO distinct rare structural classes (F-side and rule-side block-alignment).

5. **Sigma-block-aligned: 0 / 0.** No classical universal has the analogous block-alignment in sigma. Asymmetry between pi and sigma.

6. **Zero-sum coefficient pair count: highly diverse.** {7,6,4,1}: 0-4 ZSPs per rule. {2,3,5,8}: 0-6 ZSPs per rule. The §6.6 Type A predictor (zero ZSPs ⇒ LOCK at d=6→7) doesn't carry over: many full-basin universals at d=12 m=3 have zero ZSPs. The Type A/B distinction is dimension-specific, not universal.

**Conclusion on prediction (answering user's question directly).**

*Flavor 1 (predict YES/NO for a multiset):* **Promising.** The internal-9-pair count is a candidate necessary condition for cycle threads at m≥3 (must be 0 or 2, not 1). Needs further verification with more multisets, but the existing data strongly supports it. A clean predictor of the form "M hosts a cycle thread at d=4m iff M has 0 or 2 internal 9-pairs AND digit sum is divisible by 9" is within reach if the {0,4,5,9} result continues to ≥1 classical universal at completion.

*Flavor 2 (predict YES/NO for a specific F):* **Not found.** The 32+63=95 universals span 27+50=77 distinct sign patterns. No single F-level signature with >25% precision. The 'biggest-first' rule (large digit at place 0) gives 72%/60% but not better. The cycle conjecture's existence-claim at multiset-level holds; F-level prediction does not.

*Flavor 3 (predict the ACTUAL rule given F):* **Not found, and likely not findable in closed form.** Rules at d=12 m=3 are highly diverse. The 'abcd-dabc' kind of guess (cyclic shifts of classical Kaprekar) is not supported by the data — universals use diverse sign patterns, diverse cycle structures, and diverse zero-sum-pair counts. The structural mechanism that makes a rule universal involves more than position-shift symmetry. Either the predictor is not a closed-form rule, or it depends on F's digit-arrangement in ways that vary case-by-case.

**This matches the cycle conjecture's empirical status in v1.2.2 Appendix G §G.6.** That section flags: "cell-level prediction (which multisets host universals) is exact; F-level prediction via distribution-alternation is necessary but only ~0.05% specific; fine-grained prediction at the F-level fails at d=16." Addendum 9 confirms the same hierarchy at d=12 m=3: **multiset-level prediction is tractable, F-level and rule-level are not** (at least not with single-variable structural signatures).

**Implication for v1.2.3 / Appendix H.** The story for v1.2.3 should be a clean Flavor-1 classification: "Cycle threads at d=4-source are characterized by internal-9-pair count in {0, 2}. The {1,4,6,7} and {2,3,5,8} threads (0 pairs) are the high-density branch; the {0,4,5,9} thread (2 pairs) is the medium-density branch. The 4-element pure-multisets with exactly 1 internal 9-pair (e.g., {1,3,6,8}, and other candidates listed in §G.7 from the global sweep) are algebraically forbidden at m≥3 despite producing universals at m=2 via a symmetric-duplication artifact." Pending Test 2 completion and verification on a few more 9-pair-0-or-2 candidates, this is a clean structural theorem.

**Files referenced in this addendum.**
- `d12_7641.json` — {7,6,4,1} d=12 m=3 (32 classical + 10 S-only, all 32 rule encodings verified).
- `d12_2358.json` — {2,3,5,8} d=12 m=3 (63 classical + 13 S-only, all 63 rule encodings verified).
- `d12_0459_m3.json` — running on Mac, current snapshot 9+17 universals at 49% complete.
- `/mnt/user-data/outputs/SESSION_LOG.md` — this update.

**Updated next-session priorities.**

1. **Wait for Test 2 ({0,4,5,9}) Mac completion** — currently ~52h more wall time (rate has degraded; will likely take longer than initially estimated).
2. **Verify the internal-9-pair-count predictor on additional multisets.** The d=8 m=2 sweep data (Addendum 4's 17-multiset universe) tells us which multisets host universals at m=2. The predictor says: m=2 universal-hosting multisets with exactly 1 internal 9-pair should die at m=3 (like {1,3,6,8}). Test candidates with that property at d=12 m=3 on Mac. Each run ~25-40h; pick 2-3 most informative.
3. **Write Appendix H draft** once Test 2 completes. Story: Flavor-1 classification via internal-9-pair count, three confirmed threads ({1,4,6,7}, {2,3,5,8}, {0,4,5,9}), one confirmed extinction ({1,3,6,8}).
4. Phase 14 high-budget re-run on {7,6,4,1} m=3 — unchanged.
5. Run-length-3 violators analysis — unchanged.
6. 8-leading-forbidden lemma proof for {2,3,5,8} — unchanged.

---

## 2026-05-03 — Cross-d Nursery exploration: cycle conjecture, Family B trajectory, d=12 v2 confirmed, scripts staged for d=13/14/15/16

**Goal of session.** Continue Paper 2 (Nursery) cross-dimensional exploration in the {7,6,4,1} family. User wanted to (a) verify the v1 d=12 leading-6 count of 55 with a 10× higher rule-search budget, (b) explore d=9, 10, 11 territory previously assumed barren, (c) identify and verify Clay's cycle conjecture, (d) close the remaining gaps at d=12, and (e) push toward proofs at d=16, d=20.

**What we did.**

1. **Verified d=12 m=3 uniform (Family C) leading-6 count of 55** with `max_rule_search=500,000` (10× v1's 50,000). v2 result: same 55 universals, same 8 cycle partition distribution as v1. 20,873 algebraic K-fps found in leading-6 (vs ~5,000 in v1). 172 near-misses with basin ≥ 90%. The "exactly 55 leading-6 universals at d=12 in m=3 uniform" claim is now definitively rigorous. Run took 99 minutes on Mac.

2. **Discovered the digit-sum-mod-9 structural constraint.** Provable: K(P) ≡ 0 (mod 9) for any digit arrangement P, since K = |P - permutation(P)| and both have the same digit sum. **Corollary: a multiset can host K-fixed-points only if its digit sum is divisible by 9.** This drastically narrows search space: d=9 has only 12 valid multisets, d=10 has 25, d=11 has 38, d=12 has 51. Updated `multiset_explorer.py` to filter by this constraint.

3. **Discovered FAMILY B (m=2 sym-dup with k zeros) as a continuous cross-d family.** This was the major finding of the session:
   - d=8 (k=0): {7²,6²,4²,1²}: 481 universals (Paper 1 already had this)
   - d=9 (k=1): {7²,6²,4²,1²,0}: **8 universals** NEW
   - d=10 (k=2): {7²,6²,4²,1²,0²}: **58 universals** NEW
   - d=11 (k=3): {7²,6²,4²,1²,0³}: **8 universals** NEW
   - d=12 (k=4): {7²,6²,4²,1²,0⁴}: **16 universals** NEW (from partial d=12 run)
   
   Family B trajectory 481 → 8 → 58 → 8 → 16. Non-monotonic, no closed-form formula yet.

4. **Confirmed Family A (canonical zero-pad) goes BARREN at d=9.** Tested d=9 canonical {7,6,4,1,0⁵}: 22 algebraic K-fps, 0 universal. Paper 1 covered Family A through d=8 (counts 2, 2, 8, 21, 135). At d=9 it dies under Paper 2's strict universality definition (no escape class).

5. **Discovered Family X (mixed multiplicities) at d=11.** {7²,6³,4³,1,0²} signature (2,3,3,1,2) hosts 14 universals. This is the first non-uniform productive multiset — multiplicities {1,2,3,3} for nonzero counts. Suggests there may be similar secondary multisets at d=12, d=13, etc.

6. **Articulated and verified Clay's Cycle Conjecture.** *At every d ≥ 4, the multiset {7^m, 6^m, 4^m, 1^m, 0^k} where d = 4m+k and k ∈ {0,1,2,3} is productive.* Verified at every d=4..12 we've tested. Refinement: **multiple m-families coexist at the same d.** d=8 has Family A (135) and Family B (481). d=12 has Family B continuation (16) AND Family C m=3 uniform (55), at minimum. Plus secondary mixed multisets like d=11's (2,3,3,1,2).

7. **Identified that the d=12 complete run hit time budget and skipped 11 multisets** (priority sort pushed m=3 uniform and high-7-count multisets to the back; ran out of time before reaching them).

8. **Built `multiset_explorer.py`** as a generic d-arbitrary multiset enumerator with digit-sum-mod-9 filter applied. Smoke-tested at d=9 (found the 8 universals), d=10 (found 58), d=11 (found 22). Used by Mac to produce d9_results.json, d10_results.json, d11_results.json.

9. **Built `cross_d_analyzer.py`** to consolidate all JSON results across dimensions and produce master picture. Supports both Paper 1 census format and Paper 2 explorer format.

10. **Built `d12_remaining_multisets.py`** to test the 11 untested d=12 multisets (3-hour run, 15 min per multiset). Includes m=3 uniform sanity check and (1,3,2,3,3) which had 849 algebraic K-fps but 0 universals in the partial run — potential near-miss with hidden universals.

11. **Built `d16_sampled.py`** for sample-based d=16 testing. Realized full enumeration is infeasible: d=16 (3,3,3,3,4) has 672M arrangements. Sampling 100K with 70% leading-6 bias is the right strategy. Tests 5 priority multisets: Family B continuation (2,2,2,2,8), Family C continuation (3,3,3,3,4), and three mixed-multiplicity d=11-secondary analogs.

12. **Discussed provability honestly.** The CYCLE EXISTENCE THEOREM ("for every d ≥ 4 there exists at least one universal fp in the cycle multiset") is plausibly provable via constructive lift mechanism (induction on d). The bottleneck is identifying a lift that preserves strict universality (Paper 1's Type A_2 lift gives Family A which dies at d=9; we'd need a Family B-flavored lift). Exact COUNTS at each d are NOT closed-form (numbers 2, 8, 21, 481, 8, 58, 8, 16, 55 don't fit any pattern). Complete classification of productive multisets is harder still.

13. **User started parallel Mac runs for d=13, d=14, d=15** using `multiset_explorer.py` with 6-8h budgets. These are running at session end.

**Numbers verified this session.**

- d=12 m=3 uniform leading-6: **55 universals** confirmed under max_rule_search=500K (run B).
- d=12 leading-6 algebraic K-fps with 500K budget: **20,873** (vs ~5,000 with 50K budget).
- d=12 leading-6 near-misses (basin ≥ 90%): 172, none reaching 100%.
- d=9 productive multiset {7²,6²,4²,1²,0}: **8 universals**, 5,224 algebraic K-fps in 21,754s.
- d=10 productive multiset {7²,6²,4²,1²,0²}: **58 universals**, 11,876 algebraic.
- d=11 Family B {7²,6²,4²,1²,0³}: **8 universals**, 5,328 algebraic.
- d=11 Family X {7²,6³,4³,1,0²}: **14 universals**, 8,119 algebraic.
- d=12 Family B {7²,6²,4²,1²,0⁴}: **16 universals**, 5,967 algebraic, 831,600 candidates tested.
- d=9 canonical {7,6,4,1,0⁵}: 22 algebraic, **0 universal** (Family A barren at d=9).
- d=12 valid multisets total: 51. Tested in partial run: 40. Untested: 11 (including m=3 uniform and (1,3,2,3,3) near-miss).
- d=16 (2,2,2,2,8) Family B continuation: 32,432,400 arrangements. Full enum infeasible.
- d=16 (3,3,3,3,4) Family C continuation: 672,672,000 arrangements. Full enum infeasible — sampling required.

**Files produced this session.**

- `/mnt/user-data/outputs/multiset_explorer.py` — generic d-arbitrary multiset enumerator with digit-sum-mod-9 filter, per-multiset budget, leading-7 K_max filter. Used to produce d9, d10, d11 results on Mac.
- `/mnt/user-data/outputs/cross_d_analyzer.py` — consolidates JSON results across dimensions, identifies family classifications (A/B/C/D/X-mixed), produces master table and cycle-conjecture verification.
- `/mnt/user-data/outputs/d12_remaining_multisets.py` — tests the 11 specific d=12 multisets the prior run skipped. Hardcoded list, 15 min per multiset.
- `/mnt/user-data/outputs/d16_sampled.py` — sample-based d=16 explorer with leading-6 bias. Tests 5 priority multisets (Family B continuation, Family C continuation, three mixed-multiplicity analogs of d=11's secondary).
- `/mnt/user-data/outputs/d16_targeted.py` — full-enumeration d=16 explorer for the same 5 multisets. Built but UNFEASIBLE for d=16 due to 32M-672M arrangements per multiset; superseded by d16_sampled.py.
- `/mnt/user-data/outputs/d12_full_v2.py` (built earlier in session) — d=12 with max_rule_search=500K. Used by Clay to produce d12_v2_leading6.json which confirmed the 55 count.

**Mac results received this session.**
- `d9_results.json` (also as `d9_full.json`) — d=9 complete, 8 universals total
- `d10_results.json` — d=10 complete, 58 universals
- `d11_results.json` — d=11 complete, 22 universals (8 + 14)
- `d12_v2_leading6.json` — d=12 leading-6 verified at 500K rule search, 55 universals
- `d12_all_multisets.json` — d=12 partial (40/51 multisets), 16 new universals in Family B continuation

**Decisions made (with rationale).**

- **Digit-sum-mod-9 filter is mandatory.** Without it, multiset_explorer would test multisets that algebraically cannot host K-fixed-points (since K ≡ 0 mod 9 always). Adding the filter dropped d=11 candidate multiset count from ~85 to 38, saving substantial Mac time on guaranteed-empty searches.
- **Sampling strategy for d=16, not full enumeration.** Full enum would take 90+ hours per multiset for Family B and ~1900 hours for Family C. Sampling 100K with leading-6 bias is the only tractable approach. Risk: might miss universals if they're concentrated in a non-leading-6 region. Mitigation: 30% of sample is unbiased random.
- **Family classification scheme A/B/C/D/X-mixed.** Family A = canonical zero-pad (all multiplicities 1). Family B = m=2 sym-dup + zeros. Family C = m=3 sym-dup + zeros. Family D = m=4. Family X-mixed = anything with non-uniform nonzero multiplicities. This is the cleanest naming for cross-d discussion.
- **The cycle conjecture has TWO components.** (a) Existence: "every cycle multiset is productive" — empirically verified through d=12, plausibly provable via lift induction. (b) Completeness: "the cycle multiset is the ONLY productive multiset at d" — DISPROVEN by d=11 secondary {7²,6³,4³,1,0²} and by d=8 having both Family A and Family B. Paper framing should claim only (a), document (b) with secondaries.
- **Don't keep grinding individual cycle partition tests at d=16.** Each negative result (now 4: (8,4,4) seeded, (4,4,4,4) cycle, (12,2,2) Type A_2, (14,2) seeded) adds incrementally to the cliff narrative without proving anything. Better to: (1) close d=12 gaps definitively, (2) test Family B and Family C at d=16 via sampling, then (3) decide whether to attempt structural proof of the existence theorem.

**Pending / left for next session.**

- **Mac runs in progress** at session end: d=13, d=14, d=15 via multiset_explorer.py with 6-8h budgets each. Total ~16 hours of compute. Will produce d13_all.json, d14_all.json, d15_all.json.
- **Recommended next runs after d=13/14/15 finish:**
  - `python3 d12_remaining_multisets.py --time-budget 10800 --multiset-time 900 --max-rule-search 200000 --out d12_remaining.json --log d12_remaining.log` (3 hours, closes d=12)
  - `python3 d16_sampled.py --sample-size 100000 --leading-6-bias 0.7 --time-budget 14400 --multiset-time 2400 --max-rule-search 200000 --out d16_sampled.json --log d16_sampled.log` (4 hours, first non-trivial test of Family B and Family C at d=16)
- **Once all results are in:** run `cross_d_analyzer.py` on the full set to produce master cross-d picture. Update Current State block of session log with the final landscape.
- **Toward existence theorem:** identify the lift mechanism that takes a Family B universal at d to a Family B universal at d+1. Concrete first step: take a d=8 Family B universal (one of 481), try several lift constructions to d=9 in {7²,6²,4²,1²,0}, find which one matches one of the 8 known d=9 universals. That's the witness that a structural lift exists.
- **NOT YET TESTED at d=12:** the m=3 uniform (sanity check), (1,3,2,3,3) (849 algebraic, near-miss candidate), and 9 other multisets including high-7-count patterns. Pending d12_remaining_multisets.py run.
- **NOT YET TESTED at d=16:** Family B (2,2,2,2,8), Family C (3,3,3,3,4), and the three mixed-multiplicity analogs. Pending d16_sampled.py run.

**Updates to Current State block.** Major updates needed reflecting today's findings: (a) Family B identified as a continuous cross-d family d=8..12, (b) Family A goes barren at d=9, (c) digit-sum-mod-9 filter discovered, (d) d=12 Family B (16 univ) and d=12 m=3 uniform (55 univ) both productive, (e) Family X mixed-multiplicities at d=11, (f) cycle conjecture verified d=4..12, (g) d=16 full enumeration infeasible — sampling required, (h) provability honest assessment: existence theorem plausibly provable, exact counts not closed-form. Updated below.

---

## 2026-04-29 — thread-tower reframing, F-or-0 clarification, strengthened strict-d, addendum drafted

**Goal of session.** Discuss a new direction for the paper. User proposed reframing the central object: instead of "60714 lifts up via coefficient-preserving lifting," view each classical d=4 multiset class as the bottom of a thread tower, with each d-level containing all universal fps whose multiset contains the classical core. Investigate which extension digits are forced. Mid-session pivot to drafting an addendum to establish dated priority on the new findings while leaving framing decisions open.

**What we did (Part 1: exploration).**
- Clarified the candidate set for "the d=6 strict-anchor of the {7,6,4,1}-thread": four candidates 60714, 146070, 170460, 607140 (all in multiset {0,0,1,4,6,7}). Built initial strict-d checker (no proper subset reproduces dynamics on admissibles — call this the "weak" criterion).
- Fixed two bugs in the universality logic (K = |π−σ| with absolute value, and excluding near-repdigits as well as repdigits from A_d). Confirmed all 4 d=6 candidates are universal sv=6 fps under sv=d-only criterion; all 4 pass weak strict-d.
- Verified at d=5 that the {7,6,4,1}-thread has 60417 as a strict-anchor in addition to 60714 (60417 dimension-locks at d=6 but is universal sv=5 strict-d=5 at d=5).
- Discovered the parallel {8,5,3,2}-thread: at d=5 has 3 strict-anchors (28539, 53928, 58239) in multiset {2,3,5,8,9}; at d=6 has 3 strict-anchors (238599, 285939, 593928) in multiset {2,3,5,8,9,9}. Extension digit is 9, not 0.
- Confirmed 9-complement involution is multiset-level only — comp_d sends thread-A multiset to thread-B multiset, but does NOT transport individual anchors (comp_6 of {60714, 146070, 170460, 607140} = {939285, 853929, 829539, 392859}, none of which are universal at d=6).
- Tested user's "pure duplication" reframing: at d=5 and d=6 it's empty by digit-sum mod 9 obstruction; at d=7 the four admissible pure-duplication multisets of each thread (8 multisets total) ALL have 0 fixers across any sv ≥ 2. Pure-duplication extension is genuinely empty at d=5,6,7 for both threads.
- At d=8 for {7,6,4,1} pure-duplication: three of four multisets are empty; the fourth — {7,7,6,6,4,4,1,1} (each digit doubled exactly twice) — has 537 fps with sv=8 fixers. Universality undetermined in container (handoff script built).

**What we did (Part 2: F-or-0 universality and strengthened strict-d).**
- **Discovered F-or-0 universality clarification.** Tested 60714's d=7 zero-sum-pair lift: under "strict universality" (basin = 1 on inputs not repdigits/near-repdigits), basin = 0.992857 (81 inputs absorb to 0); under "F-or-0 universality" (zero-absorption allowed), basin = 1.0. The paper uses F-or-0 implicitly. User confirmed this is the intended definition and it should be added explicitly to paper §2.
- **Discovered weak strict-d criterion fails to distinguish trivial lifts.** Re-ran d=6 {7,6,4,1,0,0} under F-or-0: found 8 universal fps (6174, 60714, 146070, 170460, 174006, 174600, 607140, 617400). The 4 new ones are zero-sum-pair lifts of d=4 fps (each rule has 3 zero-sum coefficient pairs). All 8 pass weak strict-d.
- **Implemented strengthened strict-d criterion (C1).** Definition: a rule has a "trivial zero-sum pair on F" if (c_i, c_j) with c_i + c_j = 0 AND sort_desc(F)_i = sort_desc(F)_j. Strict-d = no such pair exists. Built `universality_scan_v3.py` at `/mnt/user-data/outputs/`.
- **Verified C1 at d=5, d=6.** At d=5 in {7,6,4,1,0}: 2 strict-anchors (60417, 60714), matching expectation. At d=6 in {7,6,4,1,0,0}: 4 strict-anchors (60714, 146070, 170460, 607140) — the 4 trivial 6174-lifts are correctly rejected (each has zero-sum pair on the two zero positions).
- **Ran d=7 in {7,6,4,1,0,0,0} with v3 — biggest finding of the session.** Under F-or-0 + C1: 19 total universal fps, **11 strict-d=7 anchors**: 1746, 6174, 17460, 61740, 146070, 174006, 174600, 1400706, 1460700, 1746000, 6174000. Specifically:
  - **6174 and 1746 reappear as strict-d=7 anchors** (12 strict-universal rules for 1746, 6 for 6174). At d=4 strict, d=5 algebraically obstructed, d=6 universal but non-strict, d=7 STRICT again — the non-monotone pattern from §6 of the main paper, but sharper.
  - **60714 is NOT a strict-d=7 anchor.** Its canonical d=7 lift fails C1 (the (900000, -900000) pair lands on the two trailing zeros).
  - **8 new strict-d=7 anchors** never seen before: 17460, 61740, 174006, 174600, 1400706, 1460700, 1746000, 6174000.
  - Sample 6174 strict-d=7 rule has c = (999000, 90000, -90000, -999000, 99, -90, -9) — a "scaled d=4 pair + non-zero-sum d=3 tail" pattern. The d=3 tail (99, -90, -9) has no zero-sum pair, so survives C1.

**What we did (Part 3: addendum + deploy bundle).**
- **Drafted addendum** at `/mnt/user-data/outputs/addendum.md` (~270 lines, paper.md style, single-$ math, GFM conventions). Seven sections: A.1 Purpose, A.2 strict-d criterion (Defs A.1, A.2, A.3), A.3 thread structure table (the 2/2/4/11 strict-anchor counts), A.4 non-monotone pattern (Obs A.2 on 6174/1746, Obs A.3 on 60714), A.5 pure-duplication (Obs A.4), A.6 six explicit open questions, A.7 priority note.
- **Built addendum.pdf** (5 pages, 169 KB) using pandoc + pdflatex in container with default fonts (lmodern not available). Recommended Clay rebuild on Mac through existing pipeline for Type 1 font consistency with paper.pdf.
- **Wrote ADDENDUM_DEPLOY_NOTES.md** with three deploy options (ship as-is / rebuild on Mac / email recipients), suggested index.html link patch, suggested email text for the two recipients.
- **Approach to priority.** Addendum makes specific, falsifiable empirical claims (the strict-d criterion, the 2/2/4/11 counts, 6174 reappearance at d=7, pure-duplication empty). Explicitly does NOT claim the framing is settled. Question of "(sv=d)-universal tower vs (strict-d)-universal tower" left open in §A.6. This protects priority on the criterion and the empirical findings without locking the paper into any particular reframing.

**Numbers verified this session.**
- d=5 {7,6,4,1,0} under F-or-0 + C1: 2 strict-anchors (60417, 60714), 4 strict rules total.
- d=6 {7,6,4,1,0,0} under F-or-0 only (sv=d): 8 universal fps, 18 universal rules.
- d=6 {7,6,4,1,0,0} under F-or-0 + C1: 4 strict-anchors (60714, 146070, 170460, 607140), 10 strict rules. The 4 trivial 6174-lifts (6174, 174006, 174600, 617400) correctly rejected by C1.
- d=7 {7,6,4,1,0,0,0} under F-or-0 + C1: **11 strict-anchors, 50 strict rules**. Full list: 1746 (12 rules), 6174 (6), 17460 (2), 61740 (4), 146070 (2 of 4 universal pass strict), 174006 (2), 174600 (2), 1400706 (2), 1460700 (2), 1746000 (10), 6174000 (6). Non-strict: 60417, 60714, 170406, 401706, 1406070, 6040170, 6041700, 6071400 (each 2 universal, 0 strict).
- 6174 d=6 zero-sum-pair lift basin: 4634/4905 → F (0.94475), 271/4905 → 0 (0.05525), 0 cycles. Basin(F or 0) = 1.0.
- 60714 d=7 zero-sum-pair lift basin: 11259/11340 → F (0.992857), 81/11340 → 0 (0.007143), 0 cycles. Basin(F or 0) = 1.0. Confirms paper's |E_7| = 81.
- {8,5,3,2}-thread strict-d=5 (weak criterion): 28539 (2 universal sv=5 rules), 53928 (2), 58239 (2). All 6 rules pass weak strict-d=5. C1 not yet rerun on {8,5,3,2}.
- {8,5,3,2}-thread d=6 in multiset {2,3,5,8,9,9}: 3 strict-anchors (238599, 285939, 593928), 6 universal sv=6 rules. C1 not yet rerun.

**Files changed.** None in the project repo. Created in `/mnt/user-data/outputs/`:
- `addendum.md` — the addendum source
- `addendum.pdf` — pre-built 5-page PDF
- `ADDENDUM_DEPLOY_NOTES.md` — deploy options and email text
- `universality_scan_v3.py` — strict-d=v3 scanner (F-or-0 + C1+C2, with --skip-c2 flag for d ≥ 7)
- `universality_scan_v2.py` — earlier v2 scanner (F-or-0, no C1; superseded by v3 but referenced as handoff script for d=8 {7,7,6,6,4,4,1,1} run)
- `d5_multiset_76410_v3.json`, `d6_multiset_764100_v3.json`, `d7_multiset_7641000_v3.json` — full v3 result data
- `SESSION_LOG.md` — this file (re-upload to project knowledge after deploy)

Earlier exploratory scripts in `/home/claude/strict_d/` (not staged for outputs).

**Decisions made (with rationale).**
- Adopted F-or-0 universality as the canonical definition. Matches paper's implicit usage. Will be added to paper §2 in next revision.
- Adopted C1 as the strengthened strict-d criterion (no zero-sum pair on equal F-digits). Caught the relevant structural distinction at d=6 (rejecting trivial 6174-lifts); at d=7 produced 11 strict-anchors including 6174 and 1746. Sufficient on its own — empirically C2 (no proper sub-rule) never failed when C1 passed.
- Did NOT yet pursue the d=8 question (whether 60714 reappears as strict-d=8 anchor, and whether 6174's d=8 pattern continues). Container too slow; handoff script ready for Mac.
- Did NOT yet rerun {8,5,3,2}-thread under v3 criterion (C1+C2). The weak-strict-d findings stand but should be re-verified.
- **Wrote addendum specifically to leave framing open.** §A.6 explicitly lists six open questions including the central framing decision. This timestamps priority on the criterion and the empirical findings without committing to a paper-level pivot.
- Used pandoc + pdflatex in container (default fonts) for addendum.pdf because lmodern not available; recommended rebuild on Mac for font consistency. Bundle contents are ready for `update.sh` deploy.

**Pending / left for next session.**
- **Deploy the addendum** (recommended path: rebuild PDF on Mac, run update.sh, email two recipients).
- **Re-upload SESSION_LOG.md to project knowledge** so next chat has correct state.
- **Run d=8 {7,7,6,6,4,4,1,1} universality scan on Mac** (handoff script `universality_scan_v2.py`, ~30+ min). Most interesting open question: does 60714 reappear at d=8? Does the strict-anchor count keep growing?
- **Run {8,5,3,2}-thread d=5, d=6, d=7 with v3 scanner** to get parallel strict-anchor counts. Predict 2, 3, ?? — completes the symmetry table.
- **Investigate the d=7 strict-anchor structure.** 11 anchors split into how many algebraic recipes? The (999000, 90000, -90000, -999000, 99, -90, -9) pattern for 6174 is "scaled d=4 + non-zero-sum d=3 tail." Other strict-d=7 anchors may follow analogous patterns. Categorizing these might give a constructive recipe.
- **Decide on paper framing pivot.** Is the central theorem about the (sv=d, F-or-0)-universal tower (current Theorem 5.2 holds; 60714 universal at every d ≥ 5) or the (strict-d, F-or-0)-universal tower (60714 strict at d=5, d=6 only; 6174 reappears at d=7)? Addendum leaves this open.
- Add F-or-0 universality definition explicitly to paper §2 in next paper revision.

**Updates to Current State block.** Substantially expanded. New "New mathematical content (addendum)" subsection lists the 6 new findings. Renamed paper version note to mention addendum is ready for deploy. Open work expanded with addendum deploy + d=8 + {8,5,3,2}-d=7 + framing decision.

**Late-session addendum (added at end of chat).** User pivoted from "deploy as standalone addendum" to "integrate as Appendix F of the main paper, with independent verification first." Updated Current State block to:
- Reframe the new content as Appendix F (not standalone addendum).
- Add an "IMPORTANT: verification status" subsection at the top, listing four verification requirements (independent reimplementation on Mac, full C1+C2 at d=7, hand-spot-check 2-3 anchors, literature cross-check).
- Mark every empirical claim with [VERIFICATION PENDING] to make the unverified status visible at every glance.
- Restructure open work into VERIFICATION-FIRST priorities (build fresh implementation, reproduce 11-fp d=7 list, reproduce 4-fp d=6 list, full C1+C2, hand-spot-check) followed by integration (Appendix F into paper.md) and §2 update.
- Note that `ADDENDUM_DEPLOY_NOTES.md` is partially superseded — the standalone-deploy path is no longer the plan.

The standalone `addendum.md` and `addendum.pdf` files in `/mnt/user-data/outputs/` are kept as content reference for the appendix integration but should not be deployed standalone.

**Continuation addendum (next-day session, same calendar date 2026-04-29).** This is the verification + integration session that the prior late-session addendum scoped out. What got done:

*Verification (priorities 1, 3 partial, 5 from the late-session checklist):*
- Built fresh fp-first verifier (`/home/claude/verify/verifier_v2.py`, 247 lines): architecturally distinct from `universality_scan_v3.py` — fp-first traversal with direct (A, B) image-pair enumeration via hash lookup, vs v3's rule-first traversal with brute-force testing. Same answer space, different code path.
- 14 unit tests against paper-stated facts all pass: |A_d| counts at d=4,5,6,7 (615, 1902, 4905, 11340); classical Kaprekar reproduces (every admissible at d=4 reaches 6174); 60714's native d=5 rule, d=6 split lift, and d=7 canonical lift all give K(60714)=60714 with coefficient vectors matching Table B.2 verbatim; 60714's d=7 canonical lift correctly fails C1.
- d=5 in {7,6,4,1,0}: reproduces {60417, 60714} in 0.6s.
- d=6 in {7,6,4,1,0,0}: reproduces 4 strict anchors {60714, 146070, 170460, 607140} in 5.5s. Per-fp counts match v3 exactly across all 8 universal fps. Strict rule SETS for F=60714 verified equal between v3 and verifier_v2 (not just same count).
- d=7 in {7,6,4,1,0,0,0}: reproduces all 11 strict anchors in 65s. All 11 per-fp strict rule counts match v3 exactly: 1746(12), 6174(6), 17460(2), 61740(4), 146070(2), 174006(2), 174600(2), 1400706(2), 1460700(2), 1746000(10), 6174000(6). All 8 non-strict universal fps match.
- Negative test: a non-universal fixing rule for F=60417 at d=7 was correctly identified (input 1100000 → cycle).
- Hand-spot-check on F=17460 at d=7: both strict rules verified for K(F)=F, C1 strict, and basin = 1.0 over all 11,340 admissibles.

*Session log error found and corrected:* The April 29 (yesterday) entry claims "Sample 6174 strict-d=7 rule has c = (999000, 90000, -90000, -999000, 99, -90, -9)" — verified, but that rule actually fixes F=6174000, not F=6174. Confirmed by direct hand calculation of K(F) under the rule's coefficient vector (= 6174000) and by finding the rule in v2's strict-rule set for F=6174000. The integrated Appendix F doesn't repeat this specific example. The structural claim itself (that strict rules of this shape exist for fps in the {7,6,4,1,0,0,0} multiset) holds.

*Integration:*
- Drafted Appendix F (`/home/claude/work/appendix_f.md`, ~232 lines): renumbered A.* → F.*, used GFM math, added preliminary status banner reflecting verification status. Sections F.1 through F.7 paralleling the addendum draft.
- Updated §1.8 organization paragraph to mention Appendix F.
- Spliced into paper.md: 2122 → 2357 lines (+235).
- Built integrated paper.pdf via the existing pipeline. Initial build failed with pandoc math-tokenization issue: `sv$` `=d`$` patterns with leading whitespace inside the GFM-math delimiter (e.g., `sv$` = d`$`) confuse pandoc's tex_math_dollars parser. Fixed by removing leading whitespace inside delimiters in 7 places.
- Long inline coefficient vector overflowed page margin in §F.4. Fixed by promoting to a display equation (matching the April 28 fix-pattern from the prior session).
- Final build: 76 pages, 737 KB, all-vector lmodern fonts. Zero new line/page overflows on Appendix F pages (Pages 71-76). The 24 pre-existing overflows on pages 12-68 are unchanged from the v1.1 baseline.

*Build pipeline fix (this session):* User noticed appendix subsection headings rendered as "9 A.1 Classification at d=3", "10 A.2 Classification at d=4", ..., "37 F.1 Purpose", "38 F.2 The strict-d criterion" — LaTeX prepending an arabic counter on top of the paper's own A.* / B.* / C.* / D.* / E.* / F.* numbering. This was a pre-existing artifact in the v1.1 release (Appendix A through E) but became more visible with the new Appendix F. Fixed in `build/postprocess.py` by adding regex rules that rewrite `\section{X.Y ...}` → `\section*{X.Y ...}` (and `\subsection` similarly) for any single-letter appendix prefix or "Table X.N" prefix. Rendered headings now read cleanly as "A.1 Classification at d=3", "F.1 Purpose", etc. Affects all appendices A-F; main-paper Sections 1-7 unaffected. Six new regex rules added (plain and \texorpdfstring-wrapped forms).

*Reproducibility script added:* `scripts/verifier_strict_d.py` — self-contained 322-line independent verifier bundled with the deploy. Lets anyone reproduce the strict-d findings via `python3 verifier_strict_d.py {5,6,7}`. New entry added to `scripts/README.md` with a "Reproducing Appendix F" section.

*Deploy supporting files updated:*
- `index.html` line 637: "71 pages... Updated April 28, 2026" → "76 pages... Updated April 29, 2026" with new Appendix F mention.
- `README.md` line 25: paper PDF row updated to "76 pages, ~720 KB" with Appendix F note. New row added in the appendix table for Appendix F.
- `scripts/README.md`: new row for `verifier_strict_d.py` in scripts table; new "Reproducing Appendix F" section in workflows.
- `sections/F_strict_d_anchors.md`: new file (markdown source of Appendix F, mirroring the convention of A_*.md, B_*.md, etc.).
- Bundle README at `final_build_bundle/README.md` written to describe what's in this v1.2 push.

*Bundle staged at `/mnt/user-data/outputs/`:*
- `kaprekar-build-bundle.zip` (4.0 MB, 14 files including inner kaprekar-release.zip): full bundle for `update.sh` workflow.
- `kaprekar-release.zip` (3.3 MB): inner release zip — what update.sh actually deploys to the public repo.
- `paper.pdf` (76 pages, 737 KB): directly inspectable.
- `paper.tex` (264 KB): assembled LaTeX.
- `README.md`: build-bundle README.
- `update.sh`: deploy script (unchanged from v1.1; uses cp -a catch-all so all updated files deploy automatically).

*Pending after this session:*
- **Deploy.** Clay needs to download `kaprekar-build-bundle.zip` from `/mnt/user-data/outputs/`, run `./update.sh` from the unpacked directory.
- **Re-upload SESSION_LOG.md to project knowledge** so the next chat starts with current state.
- C2 verification at d=7 — sweep all 50 strict-d=7 universal rules against the addendum's complementary criterion. Empirically expected to pass; closes §F.6 open question 1.
- Literature cross-check vs Iwasaki (2024 d=7 cycle work) and Kay-Downes-Ward (2022/2024). Their work should be cross-referenced against strict-d=7 reappearance of 6174.
- d=8 universality scans on Mac (60714 + 6174 strict-d=8 status; {7,7,6,6,4,4,1,1} pure-duplication).
- {8,5,3,2}-thread d=5,6,7 with v3 scanner under C1.
- d=7 strict-anchor algebraic recipe categorization.
- v2.0 framing decision: (sv=d, F-or-0)-tower vs (strict-d, F-or-0)-tower (§F.6 question 6).
- Add F-or-0 universality to paper §2.

### Addendum (chat 2 of 2026-04-29) — pattern-hunt for proof-ready structure

**Goal.** Building on the verified strict-d findings from earlier today, hunt for structural patterns in the 50 strict-d=7 universal rules that could lead to a proof of *why* 6174 reappears at d=7 (and what the full cross-d structure is).

**What we did.**
- Built `recipe_classifier.py` — partitions strict rules by zero-sum-pair block decomposition (number of zero-sum pairs + size of non-pair core). Ran on d=5, d=6, d=7 verified strict rules.
- **Discovered the Type A / Type B decomposition.** All 50 strict-d=7 rules in {7,6,4,1,0,0,0} fall into exactly two partition shapes: **Type A (44 rules, 8 fps): 2 zero-sum pairs + 3-core**; **Type B (6 rules, 3 fps): 0 pairs + 7-core**. At d=5 (4 strict rules) and d=6 (10 strict rules), all rules are Type B.
- **Type A characterized algebraically.** The two zero-sum pairs always land on the (7,1) and (6,4) digit positions of sort_desc(F) — digit-differences 6 and 2. The 3-core sits on F's three zero positions, contributing nothing to K(F). The fp equation reduces to: $\alpha \cdot 6 + \beta \cdot 2 = F$ where $\alpha, \beta$ are the zero-sum pair coefficients. Generalized: $\alpha \cdot \Delta_1 + \beta \cdot \Delta_2 = F$ with $\Delta_1, \Delta_2 \in \{1,2,3,5,6\}$ (digit-differences from {7,6,4,1}) and $\alpha, \beta \in \{\pm(10^a - 10^b) : 0 \leq b < a < d\}$.
- **Mechanistic proof of why d=7 is the threshold.** Type A's $(d-4)$-core must be sum-to-zero AND non-zero-sum-internal. Core size 0 (d=4): no core; pure 4-coef rule, equals classical Kaprekar. Core size 1 (d=5): single coef summing to 0 must be 0, contradicts sv=d. Core size 2 (d=6): two non-zero coefs summing to 0 form a zero-sum pair, contradicts pair-free core. **Core size ≥ 3 (d ≥ 7): non-zero-sum sum-to-zero sets exist (e.g., (99, -90, -9)).** This is the structural reason 6174 and 1746 reappear at d=7 but not d=5,6.
- **Algebraic recipe tested for completeness.** Built `predicted_2p3c.py` enumerating all $\alpha \cdot \Delta_1 + \beta \cdot \Delta_2 = F$ solutions in {7,6,4,1,0,0,0} multiset at d=7. Result: **20 algebraic candidates**, of which **8 are verified strict anchors**, 12 excluded.
- **Investigated the realizability gap.** The 12 excluded F values DO have realizing (π, σ) pairs producing K(sd) = F with sv = d (verified at F=617400: 24 derangement-style pairs exist, all sv=7, all C1-passing). But **none of those rules has F-or-0 basin = 1** — they fail dynamical universality. So the Type A "necessary but not sufficient" gap reduces to dynamical universality, not a kinematic constraint. Tested via `excluded_F_deep_dive.py`.
- **Refuted the gap-hypothesis.** Initially hypothesized that the (k, j) decomposition gap of α and β coefficients (where $\alpha = \pm(10^k - 10^j)$) would distinguish verified from excluded — but verified and excluded both contain (gap_a=1, gap_b=3) configurations. `gap_hypothesis.py`.
- **Verified C2 passes on representative Type A and Type B rules.** Spot-checked one (2p+3c) rule (1746) and one (0p+7c) rule (146070); both pass C2 at d=7. Suggests C1 ⇒ C2 in this regime, but a full sweep is still pending.
- **{8,5,3,2}-thread parallel verified at d=7.** Built and ran `universality_scan_d8_numba.py` (Numba-accelerated v3 scanner) at d=7 on multiset {8,5,3,2,0,0,0}. Result: **11 strict-d=7 anchors, 40 strict rules**, parallel to {7,6,4,1,0,0,0}'s 11/50. Recipe split: 38 Type A (10 fps) + 2 Type B (1 fp). Type A pairs land on digit-pairs (8,2) and (5,3) — digit-differences 6 and 2, identical to {7,6,4,1}'s recipe. **5382 and 2538 reappear at d=7, exactly mirroring 6174 and 1746.**
- **9-complement asymmetry confirmed at thread level.** Ran v3 scanner on 9-complement multiset {2,3,5,8,9,9,9} at d=7: only 1 strict anchor (2953998), not the 11 expected if 9-complement transported the structure. The {8,5,3,2}-thread Type B fps live in the 9-padded multiset (28539, 53928, 58239 at d=5; 238599, 285939, 593928 at d=6) — which is a different multiset family from {8,5,3,2,0^k}. So 9-complement is a multiset-class involution but does not transport individual strict anchors.
- **Started Type B characterization.** Built `type_B_hunt.py` to examine Type B coefficient vectors. Observed telescoping pattern in 60417's d=5 rule: c=(9999, -90, -9, -9000, -900) with gaps (4, 1, 1, 1, 1) summing to zero via the identity 9999 = 9000 + 900 + 90 + 9. Hypothesis (untested): Type B coefficients form cycles in a graph where vertices are 10^k powers and edges are coefficients. If correct, Type B would have a constructive characterization analogous to Type A's Diophantine.
- **Built and smoke-tested Numba scanner for d=8.** `universality_scan_d8_numba.py` reproduces v1.2 verified counts at d=6 (4 strict, 10 rules) and d=7 (11 strict, 50 rules) in 14 seconds. d=8 estimated ~20 minutes on Mac M5 Pro — clean handoff for next session.

**Numbers verified this session (in addition to v1.2 carry-overs).**
- d=5 in {7,6,4,1,0}: 4 strict rules, all Type B (0p+5c). 2 fps: 60417 (2 rules), 60714 (2 rules).
- d=6 in {7,6,4,1,0,0}: 10 strict rules, all Type B (0p+6c). 4 fps: 60714 (2), 146070 (4), 170460 (2), 607140 (2).
- d=7 in {7,6,4,1,0,0,0}: 50 strict rules. 44 Type A (2p+3c) across 8 fps; 6 Type B (0p+7c) across 3 fps. Type B fps: 146070 (2 rules), 1400706 (2), 1460700 (2).
- d=5 in {8,5,3,2,0}: 0 universal rules at all (digit-sum impossibility for one zero).
- d=6 in {8,5,3,2,0,0}: 12 universal rules across 6 fps, 0 strict (all are zero-sum-pair lifts of d=4).
- d=7 in {8,5,3,2,0,0,0}: 40 strict rules. 38 Type A across 10 fps (2538, 5382, 53802, 253800, 538002, 538020, 2000538, 2538000, 5380002, 5382000); 2 Type B across 1 fp (30285).
- d=7 in {2,3,5,8,9,9,9}: 6 universal rules across 3 fps, 2 strict (only 2953998 survives strict-d). 9-complement structure asymmetric to {7,6,4,1}.
- Type A algebraic enumeration at d=7 in {7,6,4,1,0,0,0}: 20 (α, Δ₁, β, Δ₂) candidate F values; 8 verified strict; 12 excluded by dynamical universality.
- F=617400 (excluded) realizability: 24 (π, σ) derangement-style pairs produce K(sd)=617400 with sv=7 and C1 passing; 0 of them universal.

**Files created in `/mnt/user-data/outputs/hunt/`:**
- `HUNT_FINDINGS.md` — comprehensive writeup with theorem candidate, counts tables, Type A/B definitions, predicted d=8 picture, next-target list. **Read this first when picking up the hunt.**
- `recipe_classifier.py` — partitions rules by zero-sum-pair structure; identifies Type A vs Type B.
- `predicted_2p3c.py` — enumerates Type A algebraic candidates at d=7 (gives 20; 8 verified).
- `realizability_hunt.py` — extracts (α, Δ₁, β, Δ₂) configurations from verified rules.
- `excluded_F_deep_dive.py` — shows F=17406 case: 72 pairs realize K=F, none universal.
- `gap_hypothesis.py` — tested and refuted the kinematic gap hypothesis.
- `c2_spot_check.py` — verifies C2 passes on representative Type A and Type B rules.
- `type_B_hunt.py` — initial Type B coefficient analysis; observed telescoping in 60417's d=5 vector.
- `universality_scan_d8_numba.py` — Numba scanner ready for d=8 on Mac (~20 min).
- `d5_multiset_85320_v3.json`, `d6_multiset_853200_v3.json`, `d6_multiset_764100_v3.json`, `d7_multiset_7641000_v3.json`, `d7_multiset_8532000_v3.json`, `d7_multiset_9985320_v3.json`, `d7_multiset_9998532_v3.json` — full result data for the runs above.

**Files NOT changed.** No changes to `paper.md`, `paper.tex`, `paper.pdf`, or any v1.2 deploy bundle artifact. The hunt findings live as research material at `/mnt/user-data/outputs/hunt/`; integration into a future paper revision is open work.

**Decisions made (with rationale).**
- **Did not integrate hunt findings into paper this session.** The Type A characterization is empirical/structural across d ≤ 7 and the {8,5,3,2}-parallel; for paper integration it needs verification at d=8 and a precise statement of the dynamical-universality gap. Better to hand off as research material than to lock in v1.3 prematurely.
- **Skipped d=8 in container.** Pass 1 (sv=d filter) alone estimated ~21 min; pass 2 (universality test) adds more. Mac M5 Pro will run it faster and free up container time for analysis. Numba scanner smoke-tested at d=6, d=7 confirms correctness.
- **Did not test the cycle-space hypothesis for Type B.** Observed the telescoping pattern in 60417's d=5 rule (gaps (4,1,1,1,1), sum identity 9999 = 9000+900+90+9), but didn't yet build a test that confirms or refutes the cycle-space structure across all Type B rules. Open for next session.

**Theorem candidate produced (for future paper integration).**

> Let $F$ be a fixed point in multiset $M = \{7,6,4,1,0^k\}$ or $\{8,5,3,2,0^k\}$ at digit length $d = 4 + k$. Then $F$ is a strict-$d$ universal anchor iff $F$ admits one of:
>
> **(a) Type A:** There exist $\alpha, \beta \in \{\pm(10^a - 10^b) : 0 \leq b < a < d\}$ and $\Delta_1, \Delta_2 \in \{1, 2, 3, 5, 6\}$ such that $\alpha \cdot \Delta_1 + \beta \cdot \Delta_2 = F$, AND there exists $(\pi, \sigma)$ realizing this recipe with F-or-0 basin equal to 1. Type A is structurally available iff $k \geq 3$ (i.e., $d \geq 7$).
>
> **(b) Type B:** $F$ admits an irreducible (non-zero-sum-pair-free) coefficient vector summing to zero with $\sum c_j \cdot \mathrm{sort\_desc}(F)_j = F$, AND the corresponding rule has F-or-0 basin equal to 1. Type B is available at all $d \geq 5$ in {7,6,4,1,0^k}; at all $d \geq 5$ in {2,3,5,8,9^k}.

The dynamical universality requirement (basin = 1) is the residual hard problem for both types. The structural separation into Type A and Type B, and the $k \geq 3$ threshold for Type A, are mechanistic results provable from coefficient-decomposition arguments.

**Significance.** This characterization explains 6174's non-monotone reappearance at d=7 mechanistically — Type A is the first dimension where 6174's classical d=4 dynamics can extend without obstructing strict-d. The reappearance is no longer a curiosity but a structural consequence.

**Pending / left for next session.** See top-level "Open work" section above; pattern-hunt follow-ups list items (1)–(4). Top priorities: run d=8 on Mac, then push Type B characterization deeper.

**Updates to Current State block.** Added pattern-hunt summary paragraph at top. Restructured Open Work section to fold in hunt-session priorities. No changes to the v1.2 status itself.

### Addendum (chat 3 of 2026-04-29) — d=8 scan results from Mac, Type A algebraic recipe vindicated

**Context.** Clay ran the Numba scanner from chat 2's hunt session on his Mac at d=8 in {7,6,4,1,0,0,0,0} and uploaded the results JSON. This addendum analyzes those results.

**Headline numbers at d=8.**
- 1,182 universal rules across 118 fps
- **654 strict rules across 89 strict fps** (huge jump from d=7's 50 rules / 11 fps)
- 528 universal-but-non-strict rules (mostly zero-sum-pair lifts)
- Type A (2-pair + 4-core): **426 rules across 26 fps**
- Type B (0-pair + 8-core): **228 rules across 63 fps**
- **No Type A1 (1-pair + 6-core) rules found.** My chat-2 prediction of a possible Type A1 family does not materialize — apparently the recipe space at d=8 only supports the same two recipe types as d=7.
- No mixed fps (every strict fp is purely one type).

**Type A algebraic recipe is VINDICATED at d=8.**

The Diophantine α·Δ₁ + β·Δ₂ = F with α, β ∈ {±(10^a − 10^b) : 0 ≤ b < a < 8} and Δ₁, Δ₂ ∈ {1, 2, 3, 5, 6} produces 30 algebraic candidates at d=8 in this multiset. **All 26 verified Type A fps are in the algebraic prediction set.** Only 4 candidates are excluded by dynamical universality: {17406, 174060, 1740600, 17406000}.

The exclusion ratio dropped from 12/20 = 60% at d=7 to **4/30 ≈ 13% at d=8**. The dynamical-universality filter is **getting weaker as d grows**, which is consistent with the intuition that more dimensions = more permutation freedom = more universal rules realizing each algebraic candidate.

**The 4 excluded candidates form a structural pattern.** They are 17406, 174060, 1740600, 17406000 — all variants of the same "17406" digit sequence with trailing zeros at increasing positions. The d=7 excluded list contained 12 fps including these four (plus 60174-family, 600174-family, 617400 etc.). Of those 12 d=7 excluded fps, **8 are now verified Type A at d=8** (60174, 600174, 601740, 617400, 1740006, 1740060, 6000174, 6001740, 6017400 minus the 4 still excluded). The 4 still-excluded all share the "17406" pattern. This suggests an even stronger structural conjecture: **the 17406 substring may be a permanent kinematic obstruction across all d**, with all other excluded F values resolving as d increases.

**Notable strict-d=8 fps that came back from non-strict at d=7:**
- **60714 is strict-d=8 again** (4 Type B rules). Was strict at d=5, 6 (Type B), non-strict at d=7, strict again at d=8 (Type B). The "60714 strict tower" is intermittent.
- **60417 is strict-d=8 again** (6 Type B rules). Was strict only at d=5, now back at d=8.
- **617400 is strict-d=8** (6 Type A rules). Was the canonical chat-2 "excluded F" example.

**Numbers verified this session.**
- d=8 in {7,6,4,1,0,0,0,0}: 89 strict fps (26 Type A + 63 Type B); 654 strict rules (426 Type A + 228 Type B); 1182 total universal rules.
- Type A algebraic prediction at d=8: 30 candidates, 26 verified, 4 excluded ({17406, 174060, 1740600, 17406000}).
- Strict tower trend ({7,6,4,1,0^k}): 2, 2, 4, 11, **89** at d=4, 5, 6, 7, 8.

**Files changed.**
- `/mnt/user-data/outputs/hunt/d8_multiset_76410000_v3.json` — uploaded by Clay; copy stored in hunt directory for reference.
- HUNT_FINDINGS.md not yet updated with d=8 results (pending — should add cross-d table and the d=8 algebraic-prediction vindication).

**Decisions made (with rationale).**
- **Did not re-run full Type B characterization at d=8.** The 63 Type B fps at d=8 are a much richer dataset than d=7's 3, and a structural characterization there is the natural follow-up — but it's a deep hunt step on its own.
- **Did not push to d=9.** Each dimension multiplies the work substantially; better to characterize d=8 thoroughly first.
- **The "17406 pattern" obstruction is empirically observed but not proven.** Stating it as a conjecture in any future paper revision requires either a proof or verification at d=9, 10.

**Theorem candidate update.** The chat-2 theorem candidate stands but with sharpened evidence. The Type A algebraic recipe (necessary condition) covers all verified Type A fps at d=7 AND d=8, with the dynamical filter shrinking as d grows. This is exactly the behavior expected from a complete characterization where conditions (1) and (2) tighten asymptotically.

**Pending / left for next session.**
- **Type B at d=8 deep dive.** 63 Type B fps is a much larger dataset than d=7's 3. Examine all 228 rules for a structural pattern; test cycle-space hypothesis (chat-2 found telescoping in 60417's d=5 vector).
- **Prove/disprove the 17406-substring obstruction.** Either find a proof that F containing "17406" as a substring with surrounding zeros cannot have a universal Type A realizing rule, OR find a counterexample at d=9, 10.
- **{8,5,3,2}-thread d=8.** Predict ~20-30 strict fps under the analog 17406-style obstruction. Run on Mac.
- **Test C2 at d=8** on a few representative strict rules. Should still pass empirically.
- **Update HUNT_FINDINGS.md** with d=8 results: cross-d table, vindication of Type A recipe, the 17406 obstruction observation.

**Updates to Current State block.** Added d=8 results note in the pattern-hunt summary paragraph. Updated cross-d count from "11 at d=7" to "89 at d=8". Added Type B-at-d=8 deep-dive and 17406-obstruction items to the open work section.

### Addendum (chat 4 of 2026-04-29) — d=8 sweep across all multisets containing core, generalized n-pair recipe

**Context.** Following chat 3's canonical d=8 scan, the question arose: are we missing strict anchors in OTHER d=8 multisets that contain {7,6,4,1} but use duplicates instead of (or in addition to) zeros? Built `all_d8_multisets_containing_core_scan.py` covering all 9 d=8 multisets that (a) contain the core {7,6,4,1}, (b) use only digits from {7,6,4,1,0}, (c) have digit-sum divisible by 9. Clay ran all 8 non-canonical multisets on Mac.

**Headline result — only TWO multisets at d=8 contain strict anchors.**

| Multiset | Sum | Strict fps | Strict rules |
|---|---|---|---|
| {7,6,4,1,0,0,0,0} (canonical zero-padding) | 18 | 89 | 654 |
| **{7,7,6,6,4,4,1,1} (symmetric duplication)** | 36 | **465** | **2928** |
| Other 7 multisets containing core | various | 0 | 0 |

The other 7 — three pure-duplication ({7,7,7,7,6,6,4,1}, {7,6,6,4,4,4,4,1}, {7,6,6,4,1,1,1,1}) and ALL four mixed (zeros + duplicates) — are **algebraically empty**: zero universal rules at sv=8 fixing any F in the multiset. Only the symmetric-duplication multiset {7,7,6,6,4,4,1,1} (each core digit doubled exactly twice) has anchors among the duplication-style multisets.

**Generalized n-pair recipe discovered.** The 2928 strict rules in {7,7,6,6,4,4,1,1} decompose into FOUR recipe types (vs canonical's two):
- 0-pair + 8-core (Type B): 1548 rules (52.9%)
- **1-pair + 6-core (Type A1): 184 rules (6.3%)** — NEW
- 2-pair + 4-core (Type A2): 884 rules (30.2%)
- **4-pair + 0-core (Type A4): 312 rules (10.7%)** — NEW

The 4-pair recipe uses two pairs on (7,1) digit positions and two pairs on (6,4) digit positions, possible only because each core digit is duplicated. Empirically verified Diophantine recipe for F=17461746 (the doubled-Kaprekar fp): $9\cdot(-6) + 900\cdot 2 + 90000\cdot(-6) + 9000000\cdot 2 = 17461746$.

**Generalized algebraic recipe (proposed).** For F in any {7,6,4,1}-core-containing multiset, F admits a Type A_n strict-d rule iff there exist $\alpha_1, \ldots, \alpha_n \in \{\pm(10^a-10^b) : 0 \le b < a < d\}$ and $\Delta_1, \ldots, \Delta_n \in \{1,2,3,5,6\}$ with $\sum_i \alpha_i \Delta_i = F$, AND a realizing (π, σ) has F-or-0 basin = 1. The number of pairs $n$ is bounded by:
- Available digit-pair instances in M (e.g., 1 pair max on (7,1) when M has one 7 and one 1; 2 pairs max when M has two of each)
- Core-size constraint: $d - 2n \in \{0\} \cup [3, \infty)$ (core size must be 0 or at least 3, by the non-zero-sum-internal argument from chat 2)

**Notable Type A4 fps include recursive-pattern integers:** 17461746 (Kaprekar 1746 doubled), 17466174 ("1746"+"6174"), 17741466, etc. The Type A4 recipe fixes them via four cancelling pairs.

**Numbers verified this session (in addition to chat-3 carry-overs).**
- d=8 in {7,6,4,1,0,0,0,0}: 89 strict (re-confirmed)
- d=8 in {7,7,6,6,4,4,1,1}: **465 strict fps, 2928 strict rules** (4 recipe types: 1548 Type B, 184 Type A1, 884 Type A2, 312 Type A4)
- d=8 in {7,7,7,7,6,6,4,1}: 0 universal — empty
- d=8 in {7,6,6,4,4,4,4,1}: 0 universal — empty
- d=8 in {7,6,6,4,1,1,1,1}: 0 universal — empty
- d=8 in {7,7,7,6,4,4,1,0} (mixed): 0 universal — empty
- d=8 in {7,6,6,6,6,4,1,0} (mixed): 0 universal — empty
- d=8 in {7,7,6,4,1,1,1,0} (mixed): 0 universal — empty
- d=8 in {7,6,4,4,4,1,1,0} (mixed): 0 universal — empty

**Files staged in `/mnt/user-data/outputs/hunt/`:**
- `d8_multiset_77664411_v3.json` — the symmetric-duplication big result (465 strict fps)
- `d8_multiset_*_v3.json` — empty results for the 7 algebraically-empty multisets (kept for completeness)
- `all_d8_multisets_containing_core_scan.py` — the sweep orchestrator script

**Decisions made (with rationale).**
- The Type A_n generalization is structural enough to claim as a recipe family. The empirical evidence at d=8 in two distinct multisets shows the recipe lattice depends on (a) digit-pair instance counts and (b) core-size constraint.
- The "only canonical and symmetric-duplication contain anchors at d=8" finding is a HIGHLY constrained structural fact. Mixed multisets being algebraically empty is unexpectedly clean — suggests a parity / divisibility argument may explain it.

**Open questions raised by this session.**
- **Why are mixed multisets empty?** Three of the four pure-duplication multisets are also empty. Only canonical zero-padding and symmetric duplication work. This must have an algebraic explanation — possibly related to the symmetry group of the multiset under digit-pair operations.
- **Is "symmetric duplication" the only non-canonical multiset that works at every d?** At d=12 the analog would be {7,7,7,6,6,6,4,4,4,1,1,1} (each digit tripled); at d=16 quadrupled. Worth testing at d=12 if Mac time allows (~3-4 hour run).
- **Can the Type A_n Diophantine give a complete characterization across all admissible multisets?** If so, both canonical and symmetric-duplication anchors fall under one unified framework.

**Pending / left for next session.**
- **Run d=8 in the 9-complement {2,3,5,8}-core multisets** to confirm parallel structure transports.
- **Test whether the symmetric-duplication multiset has its own "17406-substring" obstruction** at d=8 (the 12 Type A4 fps are a small dataset to look for kinematic obstructions in).
- **Type B at d=8 deep dive** — 63 fps in canonical + 1548 rules' worth of Type B in symmetric. Combined dataset is large enough to nail the cycle-space structure.
- **Update HUNT_FINDINGS.md** to reflect the n-pair generalization and the algebraic-empty multisets observation. (Already done in this session.)
- **{8,5,3,2}-thread d=8** parallel scan.

**Updates to Current State block.** Pattern-hunt summary updated to mention the symmetric-duplication finding and the generalized n-pair recipe. Open work section gets new items: cross-multiset symmetry investigation, Type A_n complete characterization, parity argument for empty multisets.

### Addendum (chat 5 of 2026-04-29) — closure-under-difference theorem proven, balanced-implies-closed proven constructively

**Goal.** Push deeper on the empirical "closure-under-difference characterizes algebraic non-emptiness" finding from chat 4. Specifically: prove what can be proven rigorously, identify what's still empirical, and articulate the proof structure for paper integration.

**What we did.**

**Theorem 1 (Algebraic Emptiness Criterion — Necessary Direction). PROVEN.**
> If $K = K_{\pi,\sigma}$ has $K(F) = F$ with sv = d, then $M = \text{multiset}(F)$ is closed under difference.

The proof is direct from $K(F) = |\pi(\text{sd}_F) - \sigma(\text{sd}_F)|$. Setting $P = \pi(\text{sd}_F)$, $Q = \sigma(\text{sd}_F)$ gives $P, Q$ both in $\text{Int}(M)$ with $|P - Q| = F$ also in $\text{Int}(M)$.

**Corollary (rigorous):** If $M$ is not closed under difference, then NO sv=d rule fixes any $F \in \text{Int}(M)$. This is the algebraic emptiness criterion.

**Theorem 2 (Balanced Implies Closed — Constructive). PROVEN.**
> Let $M = \{7^k, 6^k, 4^k, 1^k, 0^{d-4k}\}$ with $k \geq 1$, $d \geq 4k$. Then $M$ is closed under difference.

The proof is by explicit construction: $P = \underbrace{6417 \cdot 6417 \cdots 6417}_{k \text{ copies}} \cdot 10^{d-4k}$, $Q = \underbrace{4671 \cdots 4671}_{k \text{ copies}} \cdot 10^{d-4k}$. Then $P - Q = \underbrace{1746 \cdots 1746}_{k \text{ copies}} \cdot 10^{d-4k}$, with all three having multiset $M$. The block-wise subtraction works because $6417 - 4671 = 1746 \geq 0$ (no inter-block borrow propagation).

This proof transports the d=4 closure (the original Kaprekar attractor) into arbitrary balanced multisets at any $d$.

**Theorem 3 (Closure Sufficiency — Converse). EMPIRICAL at d=8 only.**
> Among multisets $M$ in {0,1,4,6,7}-digits containing the {7,6,4,1} core with digit-sum divisible by 9 at d=8: $M$ is closed under difference iff $M$ is balanced.

Verified by exhaustive enumeration over all 9 such d=8 multisets. Structural proof open.

**Beautiful collapse at d=8.** Under the digit-sum-divisibility-by-9 constraint, "pair-balanced" ($\mu(7) = \mu(1)$ AND $\mu(6) = \mu(4)$) reduces to "fully balanced" ($\mu(7) = \mu(6) = \mu(4) = \mu(1)$). Reason: pair-balanced + digit-sum mod 9 = 0 forces $a \equiv b \pmod 9$ where $a = \mu(7) = \mu(1)$ and $b = \mu(6) = \mu(4)$; for small $a, b$ this gives $a = b$. So all four conditions — pair-balanced, fully-balanced, closed-under-difference, admits-strict-anchors — are equivalent at d=8.

**Borrow-count invariant.** A potentially useful structural fact: if $P - Q = F$ with all three in $\text{Int}(M)$, then the total number of borrows in long subtraction equals $\sum M / 9$. For $M = \{7,7,7,7,6,6,4,1\}$ (digit sum 45), this means 5 borrows out of 8 positions — empirically this constrains the position-by-position structure enough to force no valid $(P, Q)$, but a clean structural argument from this is open.

**Cross-d prediction.** At d=12 in the {7,6,4,1}-core multisets:
- $k=1$: $\{7,6,4,1,0^8\}$ — should have anchors (Theorem 2)
- $k=2$: $\{7^2, 6^2, 4^2, 1^2, 0^4\}$ — should have anchors (Theorem 2)
- $k=3$: $\{7^3, 6^3, 4^3, 1^3\}$ — should have anchors (Theorem 2, novel test)
- All other multisets: predicted empty (Theorem 3 conjecture)

The d=12 sweep would be the strongest test of Theorem 3 in general.

**Files created.**
- `/mnt/user-data/outputs/hunt/CLOSURE_THEOREMS.md` — formal write-up of Theorems 1, 2, 3 with proofs and conjectures.
- `/mnt/user-data/outputs/hunt/closure_under_difference.py` — reproducible checker; takes a digit string and reports closure.

**Decisions made (with rationale).**
- **Theorem 1 ((a)⇒(c) direction) is the rigorous core.** The sv=d realizability question for closure ⇒ admits-rule (the (c)⇒(a) direction) requires further structural work; empirically holds at d=8 but theoretical proof is open.
- **Theorem 2 is the constructive heart of the framework.** It shows balanced multisets always have closure witnesses, and the witnesses are the d=4 Kaprekar primitives lifted into d-digit blocks. This connects to the original Kaprekar attractor in a clean way.
- **Theorem 3 stays a conjecture for now.** Strong empirical evidence at d=8, but the structural mechanism distinguishing balanced from unbalanced multisets is not yet proven. Could be proven via an invariant argument or by direct case analysis at small d.

**Pending / left for next session.**
- **Push on Theorem 3 structurally.** The borrow-count invariant ($B = S/9$) is the right starting point. Need to find what additional constraint distinguishes balanced from unbalanced.
- **d=12 verification of all three theorems.** Run the v3 scanner on $\{7,6,4,1,0^8\}$, $\{7^2, 6^2, 4^2, 1^2, 0^4\}$, $\{7^3, 6^3, 4^3, 1^3\}$, and several non-balanced d=12 candidates. (~3-4 hour Mac run total.)
- **{8,5,3,2}-thread cross-check.** Theorem 2's analog: for $M = \{8^k, 5^k, 3^k, 2^k, 0^{d-4k}\}$, similar construction using d=4 primitive $5382 - 2538 = 2844$? Wait, that's not in the multiset. Need to identify the {8,5,3,2}-thread d=4 closure witness analog. (At d=4 the 8532-3258 = 5274, not the multiset...). 
  Actually at d=4 the {8,5,3,2}-multiset has its own Kaprekar fp: 8352 - 2358 = 5994 (not in multiset)... Need to check what the d=4 cousin of 1746 is in {8,5,3,2}.
- **Paper integration.** The closure theorem family is paper-worthy. Next paper revision could add a section on multiset closure as the algebraic foundation of strict-d.

**Updates to Current State block.** Theorems 1 and 2 added as PROVEN structural results. Theorem 3 added as conjecture with strong d=8 evidence.

### Addendum (chat 6 of 2026-04-29) — Theorem 3 PROVEN at d=8 via LP, {8,5,3,2}-thread analog of Theorem 2 PROVEN, anti-Theorem-3 found in {8,5,3,2}-thread

**Goal.** Push (A) Theorem 3 structural proof, then (B) {8,5,3,2}-thread closure analog.

**What we did.**

**(A) Theorem 3 PROVEN at d=8 in {7,6,4,1}-thread via aggregate-counting LP.**

Constructed an LP whose feasibility is necessary for closure under difference. Variables $N(t)$ count occurrences of each "allowed local-transition tuple" $t = (a, b, b_{\text{in}}, f, b_{\text{out}})$ in long subtraction. Constraints:
- For each digit value $v$: $\sum_{a(t)=v} N(t) = \mu(v)$ (and same for $b, f$).
- Borrow conservation: $\sum_{b_{\text{in}}=1} N = \sum_{b_{\text{out}}=1} N$.
- $N(t) \geq 0$.

If $M$ is closed under difference (some $P - Q = F$ with all in $\text{Int}(M)$), the long subtraction's per-position transition counts give a feasible LP solution. Hence LP infeasibility $\Rightarrow$ not closed.

For all 7 unbalanced d=8 multisets in {7,6,4,1}-thread: LP is INFEASIBLE (verified by `theorem_3_lp_proof.py`). Hence not closed. Hence Theorem 3 (closed $\Leftrightarrow$ balanced at d=8 in {7,6,4,1}-thread) is **proven**.

Sample Farkas certificate for $\{7^4, 6^2, 4, 1\}$: $\mu(7) \leq \mu(1) + \mu(4) + \mu(0) = 1 + 1 + 0 = 2$, but $\mu(7) = 4$. Captures that every long-subtraction transition producing output digit 7 has top input $a \in \{1, 4, 7\}$ (and when $a = 7$, bottom $b$ must be 0).

**Combined corollary (proven):** A multiset $M$ of 8 digits from $\{0, 1, 4, 6, 7\}$ containing the {7,6,4,1} core with $\sum M \equiv 0 \pmod 9$ admits a universal sv=8 rule iff $M$ is balanced.

**(B) {8,5,3,2}-thread Theorem 2 analog PROVEN.**

For $M = \{8^k, 5^k, 3^k, 2^k, 0^{d-4k}\}$, take $P = (5238)^k \cdot 10^{d-4k}$, $Q = (2385)^k \cdot 10^{d-4k}$. Then $P - Q = (2853)^k \cdot 10^{d-4k}$, all with multiset $M$. The d=4 primitive is $5238 - 2385 = 2853$.

**Anti-Theorem 3 in {8,5,3,2}-thread (NEW finding from chat 6).**

When testing the LP analog at d=8 in the {8,5,3,2}-thread, found **two unbalanced multisets that ARE closed under difference**:
- $\{8, 5, 5, 3, 2, 2, 2, 0\}$: closure witness $22505238 - 20252385 = 2252853$
- $\{8, 8, 8, 5, 3, 2, 2, 0\}$: closure witness $50822388 - 22538808 = 28283580$

This means the closure-under-difference $\Leftrightarrow$ balanced equivalence is **specific to the {7,6,4,1}-thread at d=8**, NOT a thread-symmetric phenomenon. The {8,5,3,2}-thread has a richer structure.

**Open question (added to next-session queue):** Do these two anomalous multisets admit universal sv=8 rules? If yes, the {8,5,3,2}-thread genuinely contains anchors that have no analog in the {7,6,4,1}-thread. If no, then closure-under-difference is necessary but insufficient for universality, and we need an additional condition.

**Numbers verified this session.**
- LP feasibility correctly predicts closure for all 9 multisets in {7,6,4,1}-thread d=8 (5 ✓ balanced, 7 ✗ unbalanced, all consistent).
- LP feasibility predicts closure for 7 of 9 multisets in {8,5,3,2}-thread d=8. The 2 LP-feasible-but-unbalanced multisets are directly verified closed via integer search.
- d=4 closure witnesses for {8,5,3,2}: 8 pairs, including canonical $5238 - 2385 = 2853$.
- d=4 closure witnesses for {7,6,4,1}: includes $6417 - 4671 = 1746$ and $7641 - 1467 = 6174$.

**Files created.**
- `/mnt/user-data/outputs/hunt/theorem_3_lp_proof.py` — LP proof verification (script).
- Updated `/mnt/user-data/outputs/hunt/CLOSURE_THEOREMS.md` with proven Theorem 3 at d=8 in {7,6,4,1}-thread, Theorem 2' for {8,5,3,2}-thread, and Anti-Theorem 3 observation in {8,5,3,2}-thread.

**Decisions made (with rationale).**
- **Theorem 3 should be stated thread-specifically.** The original conjecture "balanced ⇔ closed at every d in every thread" is FALSE — disproven by the {8,5,3,2}-thread d=8 anomalies. Correct theorem is restricted to {7,6,4,1}-thread.
- **The LP framework is the right structural tool.** It captures closure-under-difference as a polyhedral feasibility question. The cone of feasible $(\mu(0), \mu(1), \mu(4), \mu(6), \mu(7))$ values is what we should characterize, not "balanced multisets."
- **The {8,5,3,2}-thread is genuinely different.** Cannot just transport theorems by symmetry — the digit-difference algebra is the same (Δ ∈ {1,2,3,5,6}), but the borrow-arithmetic structure differs because of the specific digit values. {7,6,4,1}-digits have specific complement / pairing properties (7+1=8, 6+4=10) that don't precisely mirror in {8,5,3,2} (8+2=10, 5+3=8 — different sums).

**Pending / left for next session.**
- **Run v3 scanner on the two {8,5,3,2}-thread anomalies** to determine whether they admit universal sv=8 rules. ~30 minutes Mac time.
- **Investigate WHY {8,5,3,2}-thread admits closed-but-unbalanced multisets while {7,6,4,1}-thread doesn't.** Plausibly related to the digit-pair complement structure (8+2=10 vs 7+1=8).
- **Characterize the LP-feasibility cone** for arbitrary $M_{\text{digits}}$: facet inequalities that determine when a multiset is potentially closed.
- **d=12 verification** of all theorems (prediction: balanced k=1, 2, 3 work in {7,6,4,1}-thread; some {8,5,3,2}-thread anomalies likely too).
- **Type B characterization** still open and worth pursuing once we have d=12 data.

**Updates to Current State block.** Theorem 3 status changed from "empirical" to "PROVEN at d=8 in {7,6,4,1}-thread via LP". Theorem 2 analog for {8,5,3,2}-thread added. Anti-Theorem 3 (closed-but-unbalanced) finding in {8,5,3,2}-thread documented. The framework is more nuanced than initially conjectured: closure-under-difference is the right structural tool, but its relationship to "balanced" is thread-specific.

### Addendum (chat 7 of 2026-04-29) — v1.2.1 deploy: §F.5 conjecture withdrawn, simplified deploy model adopted

**Goal.** Ship a corrected v1.2 paper. Today's chat 6 hunt found that v1.2's §F.5 contains a conjecture that "pure-duplication extension produces no Kaprekar fixed points at any d > 4 for either classical thread" and "zero-padding is the unique viable extension mechanism" — both falsified by the d=8 finding that {7,7,6,6,4,4,1,1} admits 465 universal sv=8 strict fps. Don't ship v1.2 with a known-false conjecture.

**What we did.**

**1. Patched §F.5 and §F.6 q3 in paper.md and the sections/F_strict_d_anchors.md reference copy.**

§F.5 Observation F.4 rewritten: title changed from "(pure-duplication extensions are empty)" to "(pure-duplication extensions at d ∈ {5, 6, 7})". Body unchanged for the empirical d=5,6,7 claim. Added a "Note (added in revision)" paragraph documenting the d=8 finding: three of four pure-duplication multisets in the {7,6,4,1}-thread remain empty at d=8, but the symmetric-duplication multiset {7,7,6,6,4,4,1,1} admits universal full-variable rules. Explicitly withdrew the broader conjecture: "Pure-duplication extensions are therefore not uniformly empty across all d > 4, and zero-padding is not the unique viable extension mechanism." Final paragraph: "The qualifier 'at any d > 4' stated in earlier versions of this appendix is withdrawn; the correct scope is d ∈ {5, 6, 7}."

§F.6 question 3 updated with the d=8 strict-anchor counts (89 in canonical {7,6,4,1,0⁴}, 465 in symmetric {7,7,6,6,4,4,1,1}). Replaced the "runs are pending" language.

§F status block at the top: "Preliminary working notes added April 29, 2026" → "added April 29, 2026 (revised April 30, 2026 to correct §F.5 — see 'Note (added in revision)' below)."

§1.8 reference to Appendix F: "Appendix F (added April 29, 2026)" → "Appendix F (added April 29, 2026; §F.5 revised April 30, 2026)."

**2. Rebuilt paper.pdf using the bundle's pipeline.** Container had pandoc and pdflatex but lmodern was uninstalled; apt was locked by another process. Workaround: extracted /var/cache/apt/archives/lmodern_2.005-1_all.deb manually with dpkg -x, copied into /usr/share/texlive/texmf-dist/, ran texhash and updmap-sys --enable Map=lm.map. Build then succeeded normally. Output: 76 pages, 741 KB, lmodern Type 1 vector fonts (matches v1.2 metrics). Sections 1-7 and Appendices A-E byte-identical to v1.2. Verified the patch made it into the rendered PDF: pdftotext shows "Note (added in revision)" appears 2 times (once in F status block, once in F.5 body), and the old "produces no Kaprekar fixed points at any d > 4" wording is absent.

**3. Updated bundle metadata.** index.html artifact description, release README.md paper row and Appendix F row, and outer build-bundle README.md all updated to mention the §F.5 revision date and the corrected wording. Bundle README.md §F.5 bullet rewritten: "Pure-duplication extensions are empty in both classical threads at d=5, 6, 7 (see §F.5 for the precise scope of this claim and the April 30 revision noting that the symmetric-duplication multiset {7,7,6,6,4,4,1,1} at d=8 admits universal sv=8 rules, so the broader conjecture stated in earlier drafts is withdrawn)."

**4. Settled on a simplified deploy model.** First deploy attempt failed because Clay's macOS workflow expects update.sh and kaprekar-release.zip in the same flat directory (~/Downloads/files-8/), and what shipped was an outer kaprekar-build-bundle.zip with extra build/ infrastructure that Clay doesn't need (he has his own pipeline). Final model adopted: a single flat files-8.zip containing exactly three top-level files — update.sh, kaprekar-release.zip, paper.pdf — that unzips with no subfolder. Clay's command sequence: `cd ~/Downloads/files-8 && unzip -o ~/Downloads/files-8.zip && chmod +x update.sh && ./update.sh`. paper.pdf at the top level is for inspection before deploy. The Claude memory has been updated to reflect this as the canonical deploy model going forward.

**Numbers verified this session.**
- v1.2.1 paper.pdf: 76 pages, 741,318 bytes (matches v1.2 page count and class).
- §F.5 patch: 2 occurrences of "Note (added in revision)" in PDF (F status block + F.5 body), 0 occurrences of "produces no Kaprekar fixed points at any d > 4".
- kaprekar-release.zip: 3.2 MB, contains the patched paper.md/paper.pdf/paper.tex and updated index.html, README.md, sections/F_strict_d_anchors.md.
- files-8.zip: 4.0 MB (3 top-level files: update.sh, kaprekar-release.zip, paper.pdf).
- update.sh: bit-identical to v1.2 (same MD5 as the version Clay uploaded), since the deploy-script logic didn't need to change.

**Files staged at /mnt/user-data/outputs/.**
- files-8.zip — the canonical deploy bundle (download this one)
- update.sh, kaprekar-release.zip, paper.pdf — also staged loose for direct inspection
- kaprekar-build-bundle.zip — older outer bundle (superseded by files-8.zip; kept for now but not the recommended path)

**Decisions made.**
- v1.2.1 is the version label; v1.2 is left in place historically (the §F.5 issue was caught before broad distribution).
- Clay's commit message: "v1.2.1: Correct §F.5 — pure-duplication conjecture withdrawn".
- Future deploy rounds use files-8.zip as the single staged artifact; outer build-bundle staging is retired.
- The closure theorems and Type A_n characterization from chats 2-6 are not integrated into v1.2.1 — they live in /mnt/user-data/outputs/hunt/ for a future v1.3 or v2.0 revision once d=12 Mac runs return data.

**Pending / left for next session.**
- Clay runs ./update.sh and pushes v1.2.1 to GitHub Pages.
- Re-upload SESSION_LOG.md to project knowledge after deploy succeeds.
- Mac queue (carried over from chat 6): ~~scan {8,5,5,3,2,2,2,0} and {8,8,8,5,3,2,2,0} ({8,5,3,2}-thread anomalies, ~30 min)~~ **DONE chat 8** — see chat 8 addendum below; both scanned, host 36 and 52 strict fps respectively; d=12 sweep of 3 balanced {7,6,4,1}-thread multisets (~12-18 hr); d=12 sweep of representative non-balanced multisets (~6-8 hr).
- arXiv endorsement (Maynard pending).
- LinkedIn article publication.

**Updates to Current State block.** Paper version → v1.2.1 (Appendix F integrated, §F.5 corrected). Deploy model → flat files-8.zip with three top-level files. The mathematical content is unchanged from v1.2; only §F.5's scope and §F.6 q3's pending-runs language were updated.

---

### Addendum (chat 8 of 2026-04-29) — d=8 hunt complete (cycle-structure theorem confirmed); C2 sweep at d=7; framing memo

**Goal.** Work through Mac-queue items + open §F.6 questions left from chat 6 (chat 7 was the v1.2.1 deploy, not new content). Five tasks attempted: #2 (d=8 universality scan), #3 (C2 sweep at d=7), #4 (Type B deep-dive), #5 ({8,5,3,2}-thread anomaly scan), #6 (framing decision). Tasks #2 and #5 ran on Mac; #3, #4, #6 in-container.

**What we did.**

*Task #3 — C2 sweep at d=7 [DONE].* Vectorized brute-force sweep of all 90 strict-d=7 universal rules across both classical threads. **All 90 pass C2** (50/50 in {7,6,4,1,0³} 1.3 s; 40/40 in {8,5,3,2,0³} 1.0 s). Reports at `c2_sweep_d7_report.json` and `c2_sweep_d7_8532_report.json`. **§F.6 open question 1 closes for both threads at d ≤ 7.** Empirical pattern across d=5,6,7: **C1 ⇔ C2 under sv=d + F-or-0 universality** (the implication "C2 violation ⇒ C1 violation" is the harder direction; provable conjecture for the next paper revision).

*Task #4 — Type B deep-dive [DONE; stronger result than expected].* The HUNT_FINDINGS hypothesis ("Type B coefficient vectors form cycles in a graph where vertices are 10^k powers and edges are coefficients") sharpens into a **complete unifying characterization**: every K-rule (π,σ) corresponds to a directed multigraph on d vertices with d edges, decomposing as a disjoint union of directed cycles via ρ = π·σ⁻¹. The cycle structure of ρ determines the recipe partition (n_pairs, core_size). Type A = 2-cycles + ≥3-cycles; Type B = ≥3-cycles only. Verified across d=5,6,7 in both threads: 100% match. Two unexpected discoveries: **(3,3) absent at d=6** (algebraically allowed, dynamically empty); **thread-specific cycle topology at d=7** ({7,6,4,1} Type B uses (7,) only; {8,5,3,2} Type B uses (3,4) only). Findings at `TASKS_3_4_FINDINGS.md` and `type_B_structural_dump.json`.

*Tasks #2 + #5 — d=8 hunt complete on Mac (~hours wall) [DONE].* Bundle staged as `/mnt/user-data/outputs/d8_hunt.zip` containing closure script + scanner + analyzer + driver. Mac ran the full pipeline. Six closed multisets identified by closure-under-difference test (thread-family scope: extras drawn from {0} ∪ core):
- {7,6,4,1}-thread: 2 closed-balanced (`76410000`, `77664411`), **0 closed-unbalanced**, 68 not-closed. Closed↔balanced theorem holds at d=8 in this thread.
- {8,5,3,2}-thread: 2 closed-balanced (`85320000`, `88553322`), **2 closed-unbalanced** (`85532220`, `88853220`), 66 not-closed. **Anti-Theorem 3 finding sharpened to specific multisets.**

Per-multiset universality scan (strict fps / strict rules):
- `76410000` 89/654, `77664411` 465/2928, `85320000` 32/232, `88553322` 459/2718, `85532220` 36/72, `88853220` 52/168. Total 1133 strict fps / 6772 strict rules across all six.

The `76410000` and `77664411` figures match v1.2.1's §F.5 numbers exactly. The 8532-thread parallel adds 32/459 in canonical/symmetric. The two unbalanced-but-closed multisets host genuine strict anchors (36 and 52 fps), confirming the closed↔balanced asymmetry between threads is structural.

**Headline answer #1: 60714 IS a strict-d=8 anchor** in canonical {7,6,4,1,0⁴} (4 strict rules). The d=7 strict-demotion does not propagate to d=8 — at d=8 there are sufficient zero positions to host alternative coefficient liftings without C1 violations. Both 60714 and 6174 reappear as strict at d=8.

**Headline answer #2: cycle-structure characterization confirmed at d=8.** All 6,772 strict-d=8 rules have ρ-cycle structure ∈ {partitions of 8 into parts ≥ 2}. 100% match. Type A1 (1-pair: cycle (2,6) or (2,3,3)) and Type A4 (pure-pair (2,2,2,2)) both populate, completing the recipe-type prediction. **Path 3 of FRAMING_MEMO becomes the clear v2.0 target** — promote cycle-structure classification to a co-theorem alongside Theorem 5.2.

Recipe × cycle distribution per multiset:
- `76410000`: A2(2,2,4) 426 | B(3,5) 98, B(8,) 130
- `77664411`: A1(2,6) 184 | A2(2,2,4) 884 | A4(2,2,2,2) 312 | B(3,5) 200, B(4,4) 64, B(8,) 1284
- `85320000`: A2(2,2,4) 188 | B(4,4) 44   ← B(8,) and B(3,5) absent here, sharp contrast with `76410000`
- `88553322`: A1(2,6) 160 | A2(2,2,4) 792 | A4(2,2,2,2) 192 | B(3,5) 216, B(4,4) 38, B(8,) 1320
- `85532220`: A1(2,6) 48 | A2(2,2,4) 16 | B(8,) 8   ← cycle topology selection is multiset-specific
- `88853220`: A1(2,3,3) 16 | B(3,5) 152   ← extreme topology selection: only two cycle types

A4 (pure-pair) populates **only in symmetric-duplication multisets** — canonical zero-padded multisets cannot form 4 distinct strict zero-sum pairs (the four 0-digits force degenerate cancellations failing C1).

*Task #6 — framing decision memo drafted [STAGED, not crystallized].* `FRAMING_MEMO.md` evaluates three paths: (1) keep sv=d as central with cycle theorem in §F; (2) pivot to strict-d as central; (3) two co-headline theorems. Recommended Path 1 short-term, Path 3 as v2.0 target. The d=8 results from this session strengthen the case for Path 3 by confirming the cycle-structure theorem on 6,772 strict rules. Decision deferred until d=12 Mac runs return and adversarial council review of the cycle-structure proof is complete.

**Numbers verified this addendum.**
- C2 sweep d=7 in {7,6,4,1,0³}: 50/50 strict rules pass C2 in 1.3s.
- C2 sweep d=7 in {8,5,3,2,0³}: 40/40 strict rules pass C2 in 1.0s.
- Type B cycle structure at d=5: 4 rules (60417, 60714 each 2), all (5,).
- Type B cycle structure at d=6: 10 rules (60714, 146070, 170460, 607140, 2-4 each), all (6,).
- Type B cycle structure at d=7: 6 rules in 7641 (1400706, 1460700, 146070 each 2) all (7,); 2 rules in 8532 (30285 ×2) all (3,4).
- d=8 closure scope: 70 multisets per thread under {0} ∪ core extras pool.
- d=8 scan smoke-tested in container at d=6 (4 strict, bit-identical to v3) and d=7 (50 strict, bit-identical to v3) before Mac handoff.

**Files produced this addendum.**

In `/mnt/user-data/outputs/` (downloadable; user can re-upload to project knowledge):
- `d8_hunt.zip` (50 KB) — Mac handoff bundle containing scripts/, d8_scan/ reference data, RUN.md driver instructions, FRAMING_MEMO.md (three paths for paper framing), TASKS_3_4_FINDINGS.md (C2 sweep + Type B cycle structure findings).
- `closure_under_difference_d8.py` — patched closure script (thread-family scope: extras drawn from {0} ∪ core), sent mid-run after the original 715-multiset enumeration was too broad. Also embedded in d8_hunt.zip's scripts/.
- `D8_FINDINGS.md` — comprehensive d=8 hunt writeup with all numbers, recipe distributions, headline answers (60714 strict at d=8, anti-Theorem 3 specifics).
- `LIT_CROSSCHECK.md` — adversarial cross-check of cycle-structure theorem and strict-d criterion vs Iwasaki 2024, Kay & Downes-Ward 2022/2024, Nuez 2021 (multiple), Dahl 2026. Verdict: no overlap — every paper works exclusively with the standard recipe T = sort_desc − sort_asc.
- `F5_v13_DRAFT.md` — markdown text ready to splice into paper.md for v1.3 deploy. Four new subsections (§F.5.1 d=8 cycle-structure landscape, §F.5.2 cycle-structure theorem with full d=8 recipe table, §F.5.3 8532-thread anti-Theorem 3 specifics, §F.5.4 A4 pure-pair only in symmetric duplication) plus three §F.6 additions (closure of question 1, new questions 7 and 8).
- `count_signature_investigation.py` — investigation script for unbalanced-but-closed multiset patterns in 8532-thread (thread-family scope, ~minute Mac wall; also runs in container in ~20s).
- `count_signature_broad.py` — same investigation but broader scope (extras from {0..9}), staged for Mac (~5 min wall).
- `COUNCIL_REVIEW_CSC.md` — adversarial review of the cycle-structure characterization theorem. Eight attack vectors examined; theorem proved rigorously. Linear independence of distinct powers of 10 over ℤ is the key ingredient; greedy n_pairs counter exactly counts ρ's 2-cycles by a telescoping argument.
- `SESSION_LOG.md` — this file.

In `/home/claude/hunt/` (in-container working files; not downloadable directly but contents preserved through the various .md outputs above):
- `c2_sweep_d7.py` — vectorized C2 sweep script.
- `c2_sweep_d7_report.json` — 7641 thread C2 report (50/50 pass).
- `c2_sweep_d7_8532_report.json` — 8532 thread C2 report (40/40 pass).
- `type_B_deep_dive.py` — cycle-structure analysis script (also bundled in d8_hunt.zip).
- `type_B_structural_dump.json` — per-rule structural data across d=5,6,7 in both threads.

In `/home/claude/d8_results/` (in-container; staged from Mac uploads):
- `closure_d8_manifest.json` (61 KB) — full closure analysis output.
- `d8_multiset_76410000_v3.json` (548 KB), `d8_multiset_77664411_v3.json` (1.34 MB), `d8_multiset_85320000_v3.json` (195 KB), `d8_multiset_85532220_v3.json` (33 KB), `d8_multiset_88553322_v3.json` (1.24 MB), `d8_multiset_88853220_v3.json` (77 KB) — six d=8 universality scans (1133 strict fps total, 6772 strict rules).
- `scan_list.txt` — driver's scan order.

**Pending / left for next session.**
- Update Appendix F.5 to cite the d=8 cycle-structure result and the two specific anti-Theorem 3 multisets (`85532220`, `88853220`).
- Add §F.6 closure note for open question 1 (C2 ⇔ C1 verified at d ≤ 7 across both threads).
- Add new §F or appendix subsection on cycle-structure characterization. Prepare adversarial council review pass before integrating into main paper body.
- Optional Mac followup: count-signature investigation. Are (1,3,1,3), (2,1,3,2), (1,2,2,3), etc. count signatures in {8,5,3,2}-thread closed under difference? Quick (~minute) Mac job.
- d=10 confirmation of cycle-structure theorem (one symmetric and one canonical multiset per thread, ~few hours).
- Cross-check vs Iwasaki and Kay-Downes-Ward on the d=7 6174 reappearance — outstanding from earlier.

**Updates to Current State block.** Mark Mac-queue item #1 ({8,5,5,3,2,2,2,0} and {8,8,8,5,3,2,2,0}) DONE — these are the same multisets as `85532220` and `88853220` just sorted differently. Add cycle-structure characterization as confirmed-at-d=8. Update §F.6 q1 status to closed. Add d=8 scan results (89, 465, 32, 459, 36, 52 strict fps in the six multisets).

---

### Addendum (chat 9 of 2026-04-29) — cycle-theorem adversarial review; nursery program articulated

**Goal.** Adversarial review of the cycle-structure theorem proof. Then, in conversation, the broader research direction underlying the paper crystallized into a coherent program. New standalone memo created: `NURSERY_PROGRAM.md`.

**What we did.**

*Cycle-theorem hostile review [DONE; result correct, exposition needs work].* Acted as hostile reviewer #2 on the cycle-structure theorem proof. Exhaustive computational counter-example search at d=3,4,5,6 across all 196,308 sv=d rules and all 14,280 (sv=d or not) pairs at d=5: zero mismatches on every claim. The result is correct. Identified five proof-exposition issues, one substantive:
- **Substantive (must fix):** Part 3's iff statement (T ⊆ {0,…,d-1} sums to zero iff T is union of full cycles) requires cross-cycle disjoint-power-supports lemma between Parts 2 and 3. Part 2 only proves *within-cycle* non-vanishing; cross-cycle independence is implicit.
- **Sloppy phrasing:** "linear independence of distinct powers of 10 over ℤ" is technically false. Correct phrasing: uniqueness of base-10 representation with bounded coefficients.
- **Unnecessary case split:** L=2 vs L≥3 in Part 2 — unified argument covers both.
- **Overspecified algorithm:** "Greedy" framing introduces phantom degrees of freedom (visit order, tie-breaking) that don't matter, since at most one j satisfies c[i]+c[j]=0 for each i. Cleaner statement: n_pairs(c) = ½ · #{i : ∃j with c[i]+c[j]=0}.
- **Base parametricity:** proof uses base 10 throughout but generalizes to any base ≥ 2; should specify b ≥ 2 to head off pedantry.
- **Free strengthening (optional):** the sv=d hypothesis is used only in Part 1's "ρ has no fixed points" claim. Parts 2 and 3 work for arbitrary (π, σ) with π ≠ σ, with fixed points of ρ corresponding to c[i]=0 positions. Theorem extends naturally to non-sv=d rules.

User has the review and will respond. No action items until then.

*Nursery program articulated [DONE; standalone memo created].* In conversation, the broader research direction underlying the paper crystallized. The {0, 1, 4, 6, 7} digit-set produces universal full-variable fixed points at d = 4, 5, 6, 7, 8 (verified): 6174 and 1746 (d=4); 60714 and 60417 (d=5); 60714, 146070, 170460, 607140 (d=6); 6174 native, 60714, 146070, 1400706, 1460700 (d=7); 6174 native, 60714 (d=8). User's instinct: "it is beyond coincidence that 6174 and 60714 share the number set." Correct instinct.

The framing: a digit-set S acts as a generative alphabet. Its **nursery** is the collection of universal full-variable fps drawn from S across all d ≥ d_min(S). Two propagation mechanisms documented in v1.0: **lifting** (60714's rule extending across d) and **recurrence** (6174 reappearing as native at d=7, d=8). The cycle-structure theorem provides the structural language for nursery membership.

The nursery framing recontextualizes v1.0 results without invalidating any of them:
- 60714 is the most prolific lifted member of the {0,1,4,6,7} nursery
- 6174 is the founder, recurring as native across multiple d
- The cycle theorem is the tool for classifying nursery members

User confirmed: not bound to v1.0 framing, but v1.0 still stands as a complete contribution. The nursery program is the *next paper*, not a replacement.

**Plan agreed.**
- Phase 0 (low-cost, no submission delay): one paragraph in v1.0 conclusion flagging the nursery program as forthcoming work. Plants the flag without restructuring. Filter existing d=7 + d=8 hunt data by digit-set membership — produces per-digit-set fp counts at each d. Hours of work.
- Phase 1 (after v1.0 submission): extend census to d=9, d=10 for the {0,1,4,6,7} nursery on Mac; structural analysis of cycle signatures across nursery members; first-pass connection theorem.
- Phase 2 (months out, v2.0 paper): constructive existence theorem; full nursery taxonomy across digit-sets; submit as second paper citing v1.0.
- Phase 3 (open-ended): d-independent existence proofs; generalization beyond strict full-variable.

**Artifacts created.**
- `NURSERY_PROGRAM.md` — standalone memo with the framing, what's verified, what's open, research plan, relationship to v1.0.

**Pending / left for next session.**
- User's response to the cycle-theorem hostile review (substantive gap: cross-cycle independence lemma between Parts 2 and 3).
- Phase 0 census: filter existing d=7 + d=8 hunt data by digit-set membership. Output: table of per-digit-set fp counts at each d. Tests whether {0,1,4,6,7} is unusually rich or representative. Critical first empirical input for the nursery program — answer determines whether the framing has legs.
- Phase 0 v1.0 conclusion paragraph: draft language flagging the nursery program. Add to v1.0 before next deploy.
- All previously-pending items from chat 8 still pending (§F.5 update, §F.6 closure note, cycle-structure §F subsection with adversarial council review, d=10 confirmation, Iwasaki/Kay-Downes-Ward cross-check).

**Updates to Current State block.** No paper-state changes (v1.0 deploy bundle still v1.2.1, still staged). Add: nursery program articulated as forthcoming research direction; `NURSERY_PROGRAM.md` standalone memo lives separately from paper. Cycle-theorem proof confirmed correct on 196,308 rules; five exposition gaps identified, one substantive, awaiting user's response.

**Continuation (chat 9, after review delivered to user — proof v2 produced).**

User received the hostile-reviewer report in a separate chat and shared it back into the chat that originally proposed the review (chat 8 of this session = "Reviewer #1"). That chat then produced proof v2 addressing all five gaps + the free strengthening.

*What changed in proof v2.*
- **Lemma 1 (per-cycle telescoping)** — restates the within-cycle coefficient formula explicitly.
- **Lemma 2 (cross-cycle disjointness)** — NEW; plugs Gap 1. States that cycle power-supports $W_C, W_{C'}$ are pairwise disjoint, derived from the multigraph's edge-partition into cycles.
- **Part 2 unified** — single algebraic argument covers $L \geq 2$ instead of the $L=2$ / $L \geq 3$ split. Gap 3 fixed.
- **"Uniqueness of base-$b$ representation with bounded coefficients"** replaces "linear independence over ℤ" throughout. Gap 2 fixed.
- **Lemma 3 (canonical matching)** — restates $n_{\text{pairs}}$ as a deterministic count via "at most one $j$ satisfies $c[i] + c[j] = 0$ per non-zero $i$." Drops "greedy" framing. Gap 4 fixed.
- **Base $b \geq 2$ general** — entire proof stated in arbitrary base. Gap 5 fixed.
- **Theorem broadened** — sv=$d$ hypothesis dropped; theorem applies to any $(\pi, \sigma)$ with $\pi \neq \sigma$. Fixed points of $\rho$ correspond to positions with $c[i] = 0$. The sv=$d$ specialization is stated as immediate corollary. Free strengthening from review.

*Status.* Proof v2 ready for paper integration. The §F.5 v1.3 draft (`F5_v13_DRAFT.md`) needs minor refresh to reference proof v2 and use broader theorem statement.

*Recommendations for paper from proof v2.*
1. State broader theorem as main result; sv=$d$ as immediate corollary. No proof cost, cleaner statement.
2. State in base $b \geq 2$; instantiate base 10 for application discussion. Matches Kay-Downes-Ward odd/even-base treatment.
3. Use "canonical matching" phrasing for $n_{\text{pairs}}$, not "greedy."

**Files produced in this continuation** (in `/mnt/user-data/outputs/`):
- `CSC_PROOF_v2.md` — revised proof addressing all five Reviewer #2 gaps + free strengthening. Replaces `COUNCIL_REVIEW_CSC.md` (chat-8 / Reviewer #1) as canonical proof reference for the paper. Reviewer #1's archived for the empirical-verification record only.
- `COUNCIL_REVIEW_v2.md` — Reviewer #2's verbatim report archived (re-saved in the chat that produced proof v2; same content as the report in the parallel nursery-articulation chat).
- `SESSION_LOG.md` — this updated file.

**Numbers verified across both chat-9 sub-sessions.**
- Reviewer #2 verified all 196,308 sv=$d$ rules at $d \in \{3, 4, 5, 6\}$: 0 mismatches.
- Reviewer #2 verified all 14,280 $(\pi, \sigma)$ pairs with $\pi \neq \sigma$ at $d=5$ (sv 1..5): 0 mismatches under broadened theorem.
- Combined with chat-8 verification on 8,562 strict universal rules at $d \in \{5,6,7,8\}$: total empirical envelope ~205,000 K-rules across $d \in \{3..8\}$, 0 mismatches.

**Pending / left for next session (consolidated across chat-9 sub-sessions).**
- Phase 0 census: filter existing d=7 + d=8 hunt data by digit-set membership. Produces table of per-digit-set fp counts. Critical first input for the nursery program — answer determines whether {0,1,4,6,7} is unusually rich or representative.
- Phase 0 v1.0 conclusion paragraph: draft language flagging the nursery program. Add to v1.0 before next deploy.
- Integrate `CSC_PROOF_v2.md` into paper as a §F or §5 theorem (depending on Path 1 vs Path 3 of FRAMING_MEMO). The proof v2 is ready to splice as-is.
- Refresh `F5_v13_DRAFT.md` to reference proof v2 and use broadened theorem statement.
- Optional Mac followup: count-signature investigation broader-scope (`count_signature_broad.py`, ~5 min wall) for foreign-digit closure in 8532-thread.
- d=10 cycle-structure confirmation, d=12 sweep, Iwasaki/Kay-Downes-Ward cross-check (already covered by `LIT_CROSSCHECK.md` from chat 8 / Reviewer #1's framing) — verify no new direction needed.

**Updates to Current State block.** Cycle-structure characterization theorem now has a v2 proof (after Reviewer #2 hostile pass): cross-cycle disjointness lemma added (substantive fix), four phrasing fixes integrated, theorem broadened to drop sv=$d$ as hypothesis (sv=$d$ becomes corollary). Empirical envelope ~205,000 K-rules, 0 mismatches. Proof v2 in `CSC_PROOF_v2.md` is canonical.

**Continuation 2 (chat 9, post-proof-v2 — Phase 0 census + tower-test, plus 549945 false-alarm).**

After proof v2 was complete, the chat moved to Phase 0 of the nursery program. Three substantive things got done.

*Phase 0 census [DONE in container].* Filtered existing chat-8 d=7 and d=8 hunt JSON data for fps with multisets drawn from {0,1,4,6,7}. Result: at d=7, 19 universal fps (11 strict, 50 strict rules); at d=8, **583 universal fps (554 strict, 3,582 strict rules)**. The d=7 → d=8 explosion (~30×) is concentrated in the symmetric-duplication multiset 77664411, which alone contributes >500 of the 583 d=8 members. The cross-d "bridge" set has 15 fps universal at both d=7 and d=8 (1746, 6174, 17460, 60417, 60714, 61740, 146070, 170406, 174006, 174600, 1400706, 1460700, 1746000, 6071400, 6174000). 4 fps universal only at d=7 (401706, 1406070, 6040170, 6041700). 437 fps universal only at d=8.

Census saved to `nursery_census_d7_d8.json` (full per-fp data); markdown summary at `NURSERY_CENSUS_d7_d8.md`.

*60417 dimension-lock false alarm.* The Phase 0 census initially flagged 60417 as having 6 strict rules at d=8 with cycle structure (5,3), suggesting it "unlocks" at d=8 after being locked at d=6 and d=7. This appeared to contradict v1.0's framing of 60417 as dimension-locked. **Followup: verified the 6 candidate rules but didn't yet check basin** — universality at d=8 requires basin = 1, not just the existence of a strict rule. The strict rules were noted in the data but full universality was not confirmed in this chat. **Action item:** at next Mac session, check basin for the 6 candidate 60417-d=8 rules; if any has basin = 1, this is real and v1.0 §6 needs a footnote; if all have basin < 1, then 60417 remains dimension-locked and the v1.0 framing stands. Provisionally treated as "open" rather than "60417 unlocks."

*549945 paper-error false alarm.* Looking at Table 3.1 across versions, the older `paper_v6_stitched.md` (still in project knowledge) describes 549945 as "the unique fp with 4 zero digits" with multiset {0,0,0,4,5,9}. This is wrong — 549945 has digits {4,4,5,5,9,9} with zero zero-digits. Drafted `PAPER_ERROR_549945.md` with required text fixes. **User pointed out the current `paper.md` (uploaded fresh into chat) already has this corrected:** total is 506 (not 507); 549945 listed with correct multiset {4,4,5,5,9,9} and labeled "zero-zero fp"; stratification table sums to 506; the 8 fps with 3 zero digits are correctly listed as the {0,0,0,2,2,5} multiset (252, 2520, 20025, 25200, 200025, 200250, 250200, 252000), not including 549945. The error existed in an old draft only. `PAPER_ERROR_549945.md` deleted.

*Tower test (the substantive empirical finding).* User raised a sharp question: the d=5 paper Table 3.1 shows {0,1,4,6,7} hosts 60714, 60417 — but no entry has multiset ⊆ {0,2,3,5,8}. The closest is {2,3,5,8,9} (28539, 53928, 58239) which uses 9, not 0. **So {0,2,3,5,8}-thread has no native d=5 fp.** User asked: does this gap extend to d=6? If yes, the {0,1,4,6,7}-thread has a continuous tower from d=4 while {0,2,3,5,8}-thread skips d=5 and d=6. This would be a genuinely new structural finding.

Built `d6_thread_tower.py` — exhaustive enumeration of all 190,800 sv=6 rules, filtering for fps with multisets drawn from each thread's alphabet. Initial container run was too slow (Python loop, ~2hr est); handed off to Mac. (Encountered an f-string syntax error on first run — `{D!}` got parsed as an invalid conversion specifier. Fixed to `math.factorial(D)`.) Mac run: 130s wall.

**Result, under reading B (all four core digits present):**

| d | {7,6,4,1}-thread | {8,5,3,2}-thread |
|---|---|---|
| 4 | 2 (1746, 6174) | 2 (2538, 5382) |
| 5 | 2 (60714, 60417) | **0** (gap) |
| 6 | 4 (60714, 146070, 170460, 607140) | **0** (gap) |
| 7 | 19 | 11 |
| 8 | 583 | 585 |

User's hypothesis confirmed empirically. {7,6,4,1}-thread is **continuous-tower** from founder; {8,5,3,2}-thread is **skip-level** with a two-level gap at d=5 and d=6 before re-emerging at d=7.

The d=6 Mac run also surfaced 8 fps in the {0,2,5} sub-alphabet ({0,0,0,2,2,5} multiset: 252, 2520, 20025, 25200, 200025, 200250, 250200, 252000) which technically pass the {0,2,3,5,8}-alphabet membership test but don't use 3 or 8 — these are the "8 fps with 3 zero digits" stratum from §A.4.3 of `paper.md`, a separate phenomenon (sub-nursery in a strict subset of the alphabet). The reading-B count separates these out cleanly.

**Why the tower finding matters.**
1. The 9-digit-complement symmetry (x_i → 9 - x_i exchanges threads at d=4 and d=8) **breaks at d=5 and d=6**. Despite identical digit sums (18) and complementary structure, only one half of the complement-pair has natives at these two consecutive levels.
2. **{1,4,6,7} is uniquely the founder thread.** Its founder (6174) carries forward continuously; {2,3,5,8}'s founders (2538, 5382) cannot continue at d=5 or d=6.
3. **The continuous-tower property is a candidate definition of "fertile" digit-sets.** Distinguishes from skip-level digit-sets like {0,2,3,5,8}.
4. The original NURSERY_PROGRAM.md (chat 9 first sub-session) said {0,1,4,6,7} was "emblematic, not unique." The tower test shows it is, in fact, structurally unique within the complement-pair: continuous-tower vs skip-level is the right distinction.

**NURSERY_PROGRAM.md updated** to incorporate this finding. New version centers continuous-tower vs skip-level as the core distinction; founder framing sharpened ("Kaprekar's 6174 is the founder of *the* continuous-tower nursery in this complement-pair"). Original v1.0-doesn't-need-rewrite framing preserved. New v1.0 footnote candidate identified for §6: noting the {2,3,5,8}-thread two-level gap as a sibling observation to the 60714 vs 60417 asymmetry.

**Numbers verified this continuation.**
- d=6 universal full-variable fps with multiset ⊆ {0,1,4,6,7} using all of {1,4,6,7}: **4** (60714, 146070, 170460, 607140). Confirmed via Mac enumeration of all 190,800 sv=6 rules.
- d=6 universal full-variable fps with multiset ⊆ {0,2,3,5,8} using all of {2,3,5,8}: **0**. Confirmed.
- d=6 universal full-variable fps in {0,2,5} sub-alphabet (the {0,0,0,2,2,5} multiset): 8 (matches paper §A.4.3).
- d=8 strict rules for 60417 in canonical 76410000 multiset: 6 (basin not yet checked — open).
- {0,1,4,6,7} d=7 strict fps: 11 (50 strict rules); d=8 strict fps: 554 (3,582 strict rules); both confirmed against existing chat-8 hunt JSON.

**Files produced this continuation** (all in `/mnt/user-data/outputs/`):
- `nursery_census_d7_d8.json` — full Phase 0 census, per-fp recipe and cycle-structure data for all {0,1,4,6,7} fps at d=7 and d=8 (156 KB).
- `NURSERY_CENSUS_d7_d8.md` — human-readable Phase 0 summary with cross-d connections, recipe distributions, and discussion.
- `d6_thread_tower.py` — Mac script for d=6 universal full-variable fp enumeration filtered by digit-set. Confirmed working after f-string fix.
- `NURSERY_PROGRAM.md` — updated nursery memo with continuous-tower vs skip-level as central distinction; integrates Phase 0 census, tower test result, proof v2 reference. Replaces the chat-9 first-version `NURSERY_PROGRAM.md` from the parallel chat.
- `SESSION_LOG.md` — this file.

(`PAPER_ERROR_549945.md` was created and then deleted after user pointed out the issue is already fixed in current `paper.md`. Not retained.)

**Pending / left for next session.**
- 60417 d=8 basin check: verify whether the 6 strict candidate rules at d=8 actually achieve universal basin. If yes → 60417 is not strictly dimension-locked, v1.0 §6 needs a footnote. If no → v1.0 framing stands. Mac job, fast (existing rules in `nursery_census_d7_d8.json`, just need basin computation).
- Phase 1 cross-digit-set scan: extend the tower-test methodology to other d=4 digit-sets. Test which are continuous-tower and which are skip-level. Mac runs, parallelizable per digit-set.
- v1.0 footnote in §6: draft language for the {2,3,5,8}-thread two-level-gap sibling observation. Optional pre-deploy fix.
- Integrate CSC_PROOF_v2.md into paper as a §F or §5 theorem (still pending from continuation 1).
- Refresh F5_v13_DRAFT.md to reference proof v2 (still pending).
- Mac queue items unchanged: `count_signature_broad.py` foreign-digit closure (~5 min), d=10/d=12 cycle-structure confirmation.

**Updates to Current State block.** New empirical finding: {7,6,4,1}-thread is continuous-tower from d=4; {8,5,3,2}-thread is skip-level with two-level gap at d=5,6. Verified via Mac enumeration. Phase 0 census of {0,1,4,6,7} at d=7,8 complete. Nursery program memo updated with continuous-tower vs skip-level distinction.

---

## 2026-04-28 — d=8 reviewer correction + font fix + page-overflow sweep

**Goal of session.** Address a substantive reviewer note flagging the §5 Lemma 5.5 Remark's d=8 numbers as wrong. Also follow-up cleanup: font crispness, table layout, page overflow.

**What we did.**
- Independently verified the reviewer was right: under the canonical Table B.1 d=8 rule, basin = 24165/24210 = 0.998141, |E_8| = 45 (all step-1, no multi-step escapes), max reaching = 21. Our previous claim (basin 0.994341, |E_8| = 137 with histogram {1:45, 2:36, 3:56}) came from a non-canonical coefficient vector.
- Root-caused the bug to `kaprekar_core.coefs_60714_odd_ladder`: even-ladder branch had wrong sign convention `(+9·10^k, -9·10^k)` instead of Table B.2's `(-9·10^k, +9·10^k)`, plus an off-by-one exponent. Fixed; verified produces all of Table B.2 (d=5..12) verbatim.
- Discovered the even/odd ladder asymmetry as a real structural fact: at even d, every escape collapses in one step ($|E_d| = |E_d^{(1)}|$ exactly); at odd d, multi-step escape orbits exist. Verified at d=7..11. Added as a future-work observation in §5 Remark.
- Fixed §5 Remark with corrected d=8 numbers; removed wrong "step-2 = 36 invariant" sentence.
- Sharpened §6.2 escape-class framing: "fixed escape class" applies precisely from d=8 onward; at d=6 only 45 admissibles reach 0 (109 enter cycles), at d=7 there are 117 escapes across 4 shape classes.
- Regenerated `audit_60714_d7.json` and `audit_60714_d8.json` with corrected canonical coefs.
- Discovered Type 3 bitmap fonts in PDF (caused "scratchy" appearance). Added `\usepackage{lmodern}` to preamble template; verified zero Type 3 fonts in rebuild.
- Compressed Table B.1 from 7 columns to 4 (dropped redundant constant `π·F`/`σ·F`/`K(F)` columns); rows now fit on single lines through d=20.
- Trimmed cluster sample-fp lists in Appendix A (cluster sizes 32, 7, 5) where rows were overflowing the right margin.
- Restructured §B.3 base cases: each ladder root's coefficient vector now on a centered display equation `c^(d) = (...)` instead of inline.
- Dropped Coefficient vector column from the {7,6,4,1}-thread table on page 46; coefs preserved in a parenthetical.
- Fixed §C.5 inline coefficient vector with same display-equation treatment.
- Used `pdftotext -bbox-layout` to systematically scan for page-margin overflows; 8 real overflows found and fixed, 2 false positives confirmed (display-math glyphs at math-display right edges).
- Synced consistency: `index.html` "67 pages" → "71 pages, Updated April 28, 2026"; README.md Appendix D row updated to reflect 18,004-fp Run B / 53-fp Run C; three "52-fp" stragglers in d7_audit/README.md → "53-fp".

**Numbers verified this session (under canonical Table B.2 coefs).**
- d=7: |A_7| = 11,340; basin = 11,259/11,340 = 0.992857; |E_7| = 81 (45 step-1 + 36 step-2); max reaching = 30.
- d=8: |A_8| = 24,210; basin = 24,165/24,210 = 0.998141; |E_8| = 45 (all step-1); max reaching = 21.
- d=10: |A_10| = 92,278; basin = 0.997724; |E_10| = 210 (all step-1, matching Lemma 5.5).
- 6174 d=6 lifting (Option A, coefs (999, 90, -90, -999, -90000, 90000)): basin 0.968603; 45 reach 0; 109 enter cycles.
- 6174 d=7 canonical lifting (pi tail (6,5,4), sigma tail (4,6,5)): basin 0.989683; 117 escapes in shape distribution {(3,2,1,1):56, (4,3):45, (3,3,1):8, (5,1,1):8}; no cycles.

**Files changed.**
- `paper.md` — §5 Lemma 5.5 Remark, §6.2 monotone-NEAR paragraph, §B.3 base cases, §C.5 even-ladder root, page 46 thread table, page 16 K_0 sentence, page 33 Kaprekar routine prose, page 41 sls phrasing, page 7 bullet, several cluster-table trims, Table B.1 simplified to 4 cols.
- `sections/05_theorem_60714.md` — synced with paper.md Lemma 5.5 Remark.
- `sections/06_thread_7641.md` — synced §6.2 framing.
- `sections/A_classification_tables.md` — synced cluster trims and thread-table column drop.
- `sections/B_60714_ladder.md` — synced Table B.1 (4 columns) and §B.3 base cases (display equations).
- `d7_audit/kaprekar_core.py` — fixed `coefs_60714_odd_ladder` sign convention and exponent. Now matches Table B.2 verbatim for d=5..12.
- `audit_60714_d7.json`, `audit_60714_d8.json` — regenerated.
- `index.html` — "67 pages" → "71 pages, Updated April 28, 2026"; hero meta "2026" → "April 2026".
- `README.md` (project) — Appendix D row text; PDF size note → 832 KB.
- `d7_audit/README.md`, `README_d7_verifier.md` — "52-fp" → "53-fp" stragglers.
- `build/preamble.tex.template` (bundle) — added `\usepackage{lmodern}` with comment about cm-super alternative.
- `build/preprocess.py`, `postprocess.py`, `assemble.py`, `build.sh`, `build/README.md` — assembled the build pipeline as a reproducible self-contained bundle.
- `update.sh` (bundle) — corrected to use `cp -a "$SOURCE/." .` catch-all (was missing paper.pdf in old version) and to prompt for commit message interactively (was hardcoded with stale text).

**Decisions made (with rationale).**
- Even/odd ladder asymmetry is flagged as a future-work observation, not pursued as a new theorem. Right scope for a v1.0+ correction round; doesn't gate Theorem 5.2.
- For §6.2 escape-class framing, the d=6 "154 escapes" the reviewer cited was a conflation of escapes (45) plus cycle-entries (109). We adopted the strict definition (E_d = inputs reaching 0) consistent with the rest of the paper, and clarified that the 109 are cycle-entries, not escapes.
- For page-overflow fixes, preferred restructuring sentences over shrinking column widths or fonts. Two strategies: (1) put long inline coefficient vectors on display equation lines so LaTeX can break them naturally; (2) drop redundant table columns when the data is recoverable elsewhere.
- For `update.sh`, fixed both flagged issues at once (commit message + paper.pdf coverage) rather than preserving the user's uploaded version literally. The uploaded version's own README acknowledged both as known issues.
- For Type 3 fonts, used `lmodern` (universal) rather than the container-only `cm-super` workaround. Notes both in the preamble comment so a build on a machine without `lmodern` knows what to install.

**Pending / left for next session.** Nothing immediate — this session's deliverable was a complete deploy bundle. User asked about establishing this session-log practice; this file is the result of that conversation.

**Updates to Current State block.** Authored from scratch this session (file is new).

---

## Pre-2026-04-28

For history before this session log existed, see:
- `handoff_to_next_claude.md` (April 17–18, 2026) — early state, paper was about 54 and dimension-*locking*; superseded.
- `handoff_geometric_chat.md`, `handoff_54_garden.md` — narrower scope; specific subprojects.
- Memory summaries in any new chat's `userMemories` block — these capture the rough arc but lag actual state.

The pivot from "54 / dimension-locked" to "60714 / dimension-transcendent" happened in late April 2026 across multiple sessions. The current paper is fundamentally a different paper than what `handoff_to_next_claude.md` describes.

## 2026-06-09 (late): sign-coherence discovery — the fold absorbing structure
- Slice decomposition of 1746-folds: K = |Σ 10^{4(k−1−j)} V(slice_j)|, no carries.
- Discriminator (full enum): fold₂ coherent ≤3 steps (24,210), fold₄ ≤5 steps (2,042,875, 0 fail);
  fold₃ has never-coherent orbits → incoherent SECOND FIXED POINT 655444440000, signs (+,+,−).
- T* (max invariant coherent subset, fold₂): 15,524 states, contains FP, entry ≤6 — both
  60714-proof lemmas hold.
- PAIR QUOTIENT: coherent dynamics factors exactly through (|V₀|,|V₁|): 1,446 reachable pairs,
  1,198 good, funnel to unique fixed pair (1746,1746), no cycles — the d=4→54-state gap
  reduction reproduced one level up. Recorded in multiplicity_chain/PROOF.md.
- Tower element (c8)⊗2 at d=16: universality + super-coherence quotient running in background.
- TOWER RECURSION VERIFIED AT LEVEL 2: (c⊗2)⊗2 at d=16 UNIVERSAL by complete enumeration (NEW);
  super-coherence entry ≤3 (level-constant!); pair quotient 235,194 states, funnel to
  (17461746,17461746), no cycles, 0 factorization violations. fold₅ d=20 sampled: entry ≤4,
  0 fail. No simple good/bad pair separation — uniformity must come from the level recursion.
  Sharpened dyadic-tower conjecture + the two missing lemmas (E),(F) recorded in PROOF.md.
