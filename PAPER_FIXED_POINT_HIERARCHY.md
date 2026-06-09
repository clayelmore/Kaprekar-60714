# A Hierarchy of Fixed Points in Generalized Kaprekar Routines

**Working outline for a new (non-narrative, structural) paper.**
Organizing principle: classify *every* fixed point of generalized (permutation-pair) Kaprekar
rules by a single ladder of strengthening conditions — from the degenerate floor where
"everything zeros out," up to dimension-transcendent universals. Place the famous objects
(495, 6174, 60714, the {1,4,6,7}^m universals) at their correct rung.

---

## 0. Common framework (one definitions section)
A digit length d; a rule is an ordered pair (π,σ) ∈ S_d×S_d, acting on n by sorting its digits
descending to s=(s_0≥…≥s_{d-1}) and forming K_{π,σ}(n) = |Σ_i c_i s_i|, where
c_i = 10^{d-1-π^{-1}(i)} − 10^{d-1-σ^{-1}(i)}, Σ c_i = 0. The classical Kaprekar rule is
(descending, ascending). Two invariants do all the work:
- **sv(K) = #{i : c_i ≠ 0}** — algebraic surviving variables (rank of the rule).
- **sv_F(K) = #{i : c_i ≠ 0 and f_i ≠ 0}** — effective rank *at* a fixed point F (its nonzero digits).

The paper's ladder is a sequence of strictly stronger properties a fixed point can have.

---

## THE LADDER

### L0 — Collapse ("everything zeros out")
K sends (almost) every input to 0. Always true on repdigits; true everywhere for degenerate rules.
The floor: no nontrivial dynamics. *Role in paper:* baseline; motivates excluding repdigits and
defines the arena.

### L1 — Bare fixed point
K(F)=F, but the basin is trivial (F essentially isolated). Abundant and uninteresting.
*Star example:* **"6174 repeated m times"** (6174, 61746174, 617461746174, …) — a fixed point at
every d=4m by a one-line geometric-series identity (7641−1467=6174 stamped m times), yet for m≥3
it is *dynamically isolated* — the "cheat": a lift of the d=4 solution with no high-d content.
*Role:* shows that being a fixed point is cheap and says nothing about dynamics.

### L2 — Proper attractor
K(F)=F with a positive-density basin but not the whole space (a "partial"). The vast middle.
*Examples:* the ~10⁸ partial fixed points found at d=16, basins ranging from a handful to 99.9%.
*Role:* the generic case; separates "fixed" from "universal."

### L3 — Universal but rank-deficient (the "interior cancels" family)
Every non-repdigit input reaches F, but via a rule with **sv_F < d**: interior coefficients cancel,
so the universality really comes from a lower-rank operation in disguise.
*Star examples:* **45, 450, 495** at d=3 — the middle digit cancels (K = 99·(a−c), sv=2). The
"dimension-agnostic" family that persists across d precisely *because* the interior zeros out.
This is the user's "everything 0s out like 45."
*Role:* universality without genuine d-dimensional structure — the first genuinely interesting,
but still "degenerate," rung.

### L4 — Full-variable (native) universal
Universal AND **sv = d**: every sorted position participates; the fixed point cannot be produced by
a lower-d lift. The first "real" rung.
*Root:* **6174** (d=4, the classical Kaprekar constant — the unique full-variable universal there).
*Census (exhaustive, this program):* 33 at d=5, 507 at d=6; on the multiplicity multiset {1,4,6,7}^m:
2, 481, 42, 341 full-variable universals at d=4,8,12,16.
*Role:* the proper object of study; everything below is preamble, everything above is structure
*across* dimensions.

### L5 — Dimension-transcendent
A single F (or explicit F-family) that is L4 (full-variable universal) at **infinitely many** digit
lengths, the rules connected by an explicit lifting. Two realizations, both rooted at 6174:

- **(a) Zero-padding axis — 60714 [PROVEN].** Universal at every d≥5 under coefficient-preserving
  zero-sum-pair liftings (Paper 1's theorem). The lifting works because *zero digits* create an
  absorbing set with bounded reaching time and an exact reduction to d−2. The flagship.
  Companion non-monotone behaviour: 6174 itself is universal at d=4 and d=7 but not d=5,6.

- **(b) Multiplicity axis — {1,4,6,7}^m at d=4m [CONJECTURED; verified m≤5].** Duplicate each digit
  m-fold instead of padding zeros. Full-variable universals exist at every tested m (2/481/42/341/≥1/≥1
  for m=1..6); the witness count *explodes* (≈3K→18M→250M for m=3,4,5). The m=2 case 61746174 is the
  clean "two parallel Kaprekars"; for m≥3 the universals are necessarily *scrambled* (no block
  decomposition). Highlighted universals: 61746174 (m=2), and e.g. F=6617774146174614 (m=4).

*Why (a) is proven and (b) is not — the paper's structural punchline:* the zero-padding axis has a
**conceptual absorbing set (the zeros)**; the multiplicity axis has none. We prove (this program):
universal ⟺ unique-fixed-point ∧ acyclic (a finite-state lemma); the obstruction to (b) is a
finite, alphabet-external cycle family whose structure *changes with m*, defeating every uniform
technique. Deepest diagnosis: even the base case — classical d=4 convergence — has **no polynomial
Lyapunov certificate below degree 9** (proven by LP), i.e. no low-complexity *mechanism*; so the
multiplicity conjecture inherits a base case that is "true without a structural reason," and a proof
needs either a conceptual proof of d=4 or a non-constructive (counting) existence argument.

---

## Suggested section order
1. Framework & the two invariants (sv, sv_F).
2. The ladder L0–L5 (definitions + the placement table below).
3. L3 in depth: the cancellation family (45/450/495) and dimension-agnosticism.
4. L4 census at d=3..6 and on the multiplicity multisets (tables).
5. L5(a): 60714 and the zero-padding transcendence theorem (cite/recap Paper 1).
6. L5(b): the multiplicity chain — existence results, the witness-count growth, the
   universal⟺unique-fp∧acyclic reduction, and the precise open problem.
7. The base-case obstruction (no low-degree Lyapunov for d=4) and what a proof would require.
8. Open problems: the zero-free absorbing filtration; the all-m conjecture; second-moment existence.

## Placement table (the paper's spine, one figure)
| Rung | Condition | Canonical examples | Status |
|---|---|---|---|
| L0 | K → 0 | repdigits | trivial |
| L1 | K(F)=F, basin trivial | 6174-repeated (m≥3) | the "cheat" |
| L2 | positive-density basin | generic partials | generic |
| L3 | universal, sv_F < d | 45, 450, 495 | dimension-agnostic |
| L4 | universal, sv = d | 6174; 60714,60417; multiplicity universals | the real objects |
| L5a | L4 at all d via zero-pad | **60714** | PROVEN |
| L5b | L4 at all d=4m via multiplicity | **{1,4,6,7}^m universals** (61746174, …) | conjectured, verified m≤5 |

## Tone
Structural/encyclopedic, not "we discovered." Each rung gets a definition, a theorem or census,
and one or two named inhabitants. 60714 and the multiplicity universals are the two summits;
45/495 are the instructive degenerate floor of "interesting."
