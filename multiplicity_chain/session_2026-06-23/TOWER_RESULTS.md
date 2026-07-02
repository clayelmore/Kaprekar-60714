# Session 2026-06-23 — Attack on Conjecture 6.6 (the dyadic 1746 tower)

Target: the iterated 2-fold of c = (9, −900, 900, −9) is universal at d = 2^{j+2} for every j.
Route: Open Problem 7.2's two uniformities, (E) bounded coherence entry and (F) the funnel.
Everything below verified against the engine conventions (K(n) = |Σ c_i s_i|, sorted-descending).

## 1. PROVEN — the Sign Lemma (new)

Let V_j be the level-j tower form (V_0 = 9(x0−x3) − 900(x1−x2); V_{j+1}(x) = 10^{d_j} V_j(x_even) + V_j(x_odd), d_j = 4·2^j). For every j ≥ 0 and sorted x of length d_j:

    V_j(x) < 0  ⟺  x[2^j] > x[2^{j+1}]
    V_j(x) = 0  ⟺  x is constant (repdigit)
    V_j(x) > 0  otherwise.

Moreover M_j := max|V_j| ≤ 10^{d_j} − 1 (exactly: M_0 = 8019, M_{j+1} = M_j(10^{d_j}+1)).

*Proof.* Base: V_0 = 9(x0−x3) − 900(x1−x2); if x1 > x2 then V_0 ≤ 81 − 900 < 0; if x1 = x2
then V_0 = 9(x0−x3) ≥ 0, zero iff constant. Induction: the bound gives
M_{j+1} ≤ (10^{d_j}−1)(10^{d_j}+1) = 10^{d_{j+1}}−1, so when V_j(even) ≠ 0 the top term
dominates strictly and sign V_{j+1} = sign V_j(even). The even slice y has y[2^j] = x[2^{j+1}],
y[2^{j+1}] = x[2^{j+2}]: if x[2^{j+1}] > x[2^{j+2}] the IH gives V_j(y) < 0, hence V_{j+1} < 0.
If equal and V_j(y) > 0, done. If V_j(y) = 0 the IH forces y constant, and sortedness then
forces x0 = x1 = ⋯ = x_{d_{j+1}−2} (each odd rank is squeezed between equal even ranks);
the odd slice is (x0,…,x0,x_last) whose critical pair is equal and interior, so
V_{j+1} = V_j(odd) ≥ 0 with equality iff x is constant. ∎

Verified: 0 violations over ALL sorted states at levels 0, 1, 2 (715 + 24,310 + 2,042,975)
and 120,000 adversarial/random states at level 3.

Consequence: the sign of the entire 2^{j+2}-digit form is decided by comparing TWO digits.

## 2. PROVEN — Plateau characterization of incoherence (new, uniform in j)

State x at level j+1 (length 8·2^j), a := 2^{j+1}, b := 2^{j+2}. x is top-incoherent
(slice values strictly opposite in sign) iff exactly one of:

  Type A:  x_a = x_{a+1} = ⋯ = x_b > x_{b+1},  even slice non-constant
  Type B:  x_a > x_{a+1} = ⋯ = x_{b+1},        odd slice non-constant

*Proof.* Apply the Sign Lemma to each slice: the even slice's critical pair is (x_a, x_b),
the odd's is (x_{a+1}, x_{b+1}); sortedness collapses the interval between equal ranks. ∎

Verified exactly: 6,006/24,310 incoherent at level 1, 251,940/2,042,975 at level 2,
0 mismatches. Incoherence = a "critical plateau" of length 2^{j+1}+1 in the second
quarter of the sorted string, with a strict drop at the prescribed end.

## 3. PROVEN — (E) at levels 1 and 2, sharp bound 3, by abstract families (new)

Level 1 (d=8). An incoherent state is Type A or B; writing the three gaps
  A: P = x0−x6 ≥ 1, Q = x3−x5 ≥ 1, R = x1−x7 (Q ≤ R ≤ 9), image K = 9P·10^4 − 9(100Q−R)
  B: Q = x2−x4 ≥ 1, R = x0−x6 (≥Q), P = x1−x7 ≥ 1,        image K = 9(100Q−R)·10^4 − 9P
(the formulas follow from the Sign Lemma + plateau; verified with 0 mismatches on all
6,006 incoherent states). The image depends on the THREE gaps only: an abstract family of
405 + 405 = 810 values. Direct check: 744 images already coherent, 62 need one more step,
4 need two. Since 0 < K < 10^6, the padded image always has both zero and nonzero digits —
never a repdigit. Hence: every non-repdigit d=8 state is top-coherent within 3 steps and
never passes through a repdigit en route. (Matches the full 24,310-state enumeration: max 3.)

Level 2 (d=16). Same schema, seven gaps (e0,e1,e2; f0,f1,f2,f3):
  Type A: A = 9e0·10^4 + 9e1 − 900e2 > 0, B = 10^4(9f0−900f1) + 9f2 − 900f3 < 0,
          K = 10^8·A + B; Type B mirrored.
Formulas verified on all 251,940 incoherent states (0 mismatches). Abstract family
2 × 1,247,400 = 2,494,800 members: all coherent within 2 further steps
(distribution A: 1,218,586 / 27,603 / 1,211; B: 1,219,751 / 27,171 / 478). Values satisfy
0 < K < 10^{15}, so no repdigit images. Bound 3 again — sharp, same as level 1.

## 4. PROVEN — a gap in Open Problem 7.2's reduction, and its repair (new)

**The gap.** OP 7.2 claims (E) + (F) ⟹ Conjecture 6.6, where (F) is the funnel property
of the coherent pair quotient. But Computed 6.8's funnel was verified on the 1,202 pairs
whose orbits NEVER exit coherence; 262 reachable pairs exit. A cycle passing through both
coherent and incoherent states ("mixed cycle") is excluded by neither hypothesis: its
coherent arcs leave the partial quotient's domain before returning, so (F) never sees it,
and (E) is silent on what happens after entry. (E)+(F) as stated do not imply universality.

**The repair — the return-map quotient.** For a coherent state, the image multiset is
digits(|A|) ⊎ digits(|B|), a function of the pair alone; so the entire future of a coherent
state is determined by its pair. Define T̂(pair) = the pair of the FIRST top-coherent state
on the forward orbit of the assembled image ((E) makes T̂ total). 

**Theorem R.** Fix a tower level. Suppose (E'): every non-repdigit state becomes top-coherent
within a finite bound, never passing through a repdigit en route; and (F̂): T̂ is total on the
reachable coherent pairs, has no repdigit excursions, has the folded pair (W,W) as its unique
fixed pair, and has no cycle of period ≥ 2. Then the tower element is universal.

*Proof.* The state space is finite, so an admissible orbit ends in a periodic set C. By (E')
and (F̂)'s no-repdigit clauses the orbit never meets a repdigit or 0, so C consists of
admissible states. By (E'), C contains a coherent state s* with pair p*; the successive
coherent states around the cycle give a T̂-orbit returning to p*, i.e. a T̂-cycle. By (F̂)
that cycle is the fixed pair (W,W), so the state after s* is the assembled fixed point F,
and C = {F}. Every admissible orbit ends at F. ∎

**Verification of (F̂) — complete at both enumerable levels:**
  level 1: T̂ total on all 1,464 coherent pairs (the 262 "exiting" pairs included),
           0 repdigit excursions, unique fixed pair (1746, 1746), acyclic.
  level 2: T̂ total on all 235,212 pairs, 0 excursions, unique fixed pair
           (17461746, 17461746), acyclic.

With §3, this gives a complete quotient-route proof of universality at levels 1 and 2 —
consistent with (and independent of) the known full enumerations.

## 5. EVIDENCE — level 3 (d = 32)

Using the plateau characterization to CONSTRUCT incoherent d=32 states directly:
60,000 constructed incoherent states (types A and B, all plateau values): every one
top-coherent within 3 steps (59,740 in one, 259 in two, 1 in three) — the same sharp
bound proven at levels 1–2. 50,000 random states: max 2. 
Conjecture (E-uniform): coherence entry within 3 steps at EVERY level.

## 6. NEGATIVE RESULTS (honest)

- Window reduction fails: image coherence at level 2 does NOT depend only on the top
  half-chunks of A and |B| (921 of 1,710 coarse groups have mixed outcomes), nor on
  (e0, f0, f1) (450/450 mixed). The abstract-family size therefore grows with the level
  (~10^13 at level 3): the finite-check method proves (E) at levels 1–2 but cannot reach
  level 3. A uniform (E) proof needs a genuine carry-and-block argument.
- Simple monovariants on T̂ all fail: |A−F|+|B−F|, max|·−F|, multiset distance to F²,
  and |A−B|+|A+B−2F| are each violated hundreds of times at level 1 (445–787 of 1,463
  non-fixed pairs) and tens of thousands of times at level 2 — the certificate-cost wall
  standing exactly where Theorem R relocates it, on the funnel property of T̂.
- A grace note: the slowest coherence-entering states at level 1 (entry time 3) descend
  from the abstract images 445545 and 445554 — digit content pure {4,5} — the
  {4,5,9}-shadow of Section 5 surfacing even inside the entry dynamics.

## 7. STATE OF CONJECTURE 6.6 AFTER THIS SESSION

  PROVEN:   the reduction (E')+(F̂) ⟹ universality (Theorem R — repairing OP 7.2);
            (E') at levels 1, 2 with sharp bound 3; (F̂) at levels 1, 2 (complete).
  EVIDENCE: (E') at level 3 with the same bound 3; universality of the level-3 element
            (alphabet + 200k sample, from the paper).
  OPEN:     (E'_j) for j ≥ 3 (conjectured bound 3, uniform); (F̂_j) for j ≥ 3 — the pair
            systems outgrow enumeration and the certificate-cost obstruction stands.

Conjecture 6.6 is now equivalent to two uniformities over a PROVEN reduction; before this
session the reduction itself had a hole. The entry half (E') is proven at two levels by a
method whose failure to generalize is precisely located (§6).
