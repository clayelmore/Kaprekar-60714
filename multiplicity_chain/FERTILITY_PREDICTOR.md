# ⚠️ CORRECTION (2026-06-03, same day) — READ FIRST

**The claim below that "fertile ⟺ desc−asc=6174 ∧ mod-9" is FALSE as a statement about
general fertility.** Counterexample: **{0,4,5,9}** has **152 universals** (76 classical + 76
S-only) at d=12 m=3 — it is highly fertile — yet desc−asc(9540−0459)=9081 ≠ 6174.

The error: {0,4,5,9} was mis-labeled "extinct" by trusting a **stale (May 18) session-log
note** that predated the {0,4,5,9} m=3 run (which completed May 29 with 152 universals).

**What is actually true (the corrected, narrower, exhaustively-verified claim):**

> A 4-digit set admits the **pair-symmetric universal *construction*** (σ pair-swaps π's
> digit-blocks) **⟺ (D₀−D₃, D₁−D₂) = (6,2) ⟺ desc−asc = 6174 ∧ mod-9 ⟺ {1,4,6,7} or {2,3,5,8}.**
> Verified exhaustively over all 24 mod-9 sets.

This explains **why the pair-symmetric search only worked for {1,4,6,7}/{2,3,5,8}** — it does
NOT characterize general fertility. Sets like {0,4,5,9} are fertile via **non-pair-symmetric**
rules (found by general search, not the pair-symmetric construction).

**The general "Flavor-1" fertility question — which sets host *any* universals at all m —
REMAINS OPEN.** This document resolves only the pair-symmetric sub-question.

Everything below should be read with "fertile" replaced by "admits the pair-symmetric
construction."

---

# The Fertility Predictor — Which Digit-Sets Host a Multiplicity Chain

*Resolves the "Flavor-1 predictor" question left open in the session log. Found 2026-06-03
by treating the problem as a code-cracking / use-all-examples exercise (the golden-ratio, π,
and Fibonacci-rotation hypotheses were tested and **falsified** — see bottom).*

---

## The result

> **A 4-digit set $S$ hosts universal fixed points across the multiplicity chain $S^m$ at
> $d=4m$ if and only if**
> 1. $\mathrm{desc}(S) - \mathrm{asc}(S) = 6174$ (its classical Kaprekar step *is* 6174), **and**
> 2. $\mathrm{digitsum}(S) \equiv 0 \pmod 9$.
>
> **Exactly two sets in base 10 satisfy both: $\{1,4,6,7\}$ and $\{2,3,5,8\}$.**

## Status of each half

- **Condition 2 (mod 9): PROVEN NECESSARY.** Every Kaprekar difference is a permutation
  minus a permutation of the same digits, hence $\equiv 0 \pmod 9$. A fixed point $F=K(F)$
  therefore satisfies $F\equiv 0$, so $\mathrm{digitsum}(S)\equiv 0 \pmod 9$.
- **Condition 1 (desc−asc = 6174): empirical discriminator, strong structural backing.**
  12 of the 210 four-digit sets generate 6174 under desc−asc; only **2** of those are also
  mod-9. Those 2 are exactly the fertile threads.

## Verification (7 cases, 0 exceptions)

| set | desc−asc | mod-9 | predicted | observed |
|---|---:|:---:|---|---|
| {1,4,6,7} | 6174 | ✓ | fertile | fertile (m=1..6) |
| {2,3,5,8} | 6174 | ✓ | fertile | **fertile** (d=12: 3 universals, 100% basin) |
| {0,4,5,9} | — | ✓ | extinct | extinct (near at m=3) |
| {1,3,6,8} | — | ✓ | extinct | extinct |
| {0,1,8,9} | — | ✓ | extinct | extinct |
| {0,3,6,9} | 9261 | ✓ | extinct | **extinct** (d=12: 0 candidates) |
| (210−… non-mod-9) | — | ✗ | extinct | (no fixed points possible) |

Note all three previously-known extinct sets {0,4,5,9}, {1,3,6,8}, {0,1,8,9} satisfy mod-9
(digit-sum 18) yet fail condition 1 — so **condition 1 is exactly what discriminates fertile
from extinct among the mod-9 sets.**

## Why it works — the (6,2) coefficient signature

The pair-symmetric rule on a sorted set $D_0>D_1>D_2>D_3$ (pairing $D_0\!\leftrightarrow\!D_3$,
$D_1\!\leftrightarrow\!D_2$) has block-sum form
$$K = (D_0-D_3)\,S_0 + (D_1-D_2)\,S_1.$$
- {1,4,6,7}: $(D_0-D_3,\,D_1-D_2) = (7-1,\,6-4) = (6,2)$.
- {2,3,5,8}: $(8-2,\,5-3) = (6,2)$ — **identical**.

Both fertile sets induce the *same* coefficient pair $(6,2)$, which is exactly the 6174
signature: $6174 = 999\cdot 6 + 90\cdot 2$. So the two fertile threads are the **same
dynamical system** (relabel the digits), and proving universality for one proves it for both.
A set is fertile iff its $(D_0-D_3, D_1-D_2)$ equals $(6,2)$ **and** it is mod-9 — i.e. iff it
is a mod-9 "6174-generator."

**Consequence:** the entire multiplicity-chain universality phenomenon is **6174-specific**.
It is not a generic feature of digit-sets; it occurs only for the two sets whose Kaprekar step
is 6174 itself.

## Relation to the universality proof

This answers *which* sets are fertile (the Flavor-1 question). It does **not** by itself prove
universals persist at every $m$ within a fertile set (the monotone–acyclic open problem in
`PROOF.md`). But it sharpens that problem: there is effectively **one** system to analyze
(coefficients $(6,2)$, i.e. 6174), and both fertile digit-sets are the same problem.

## Ideas tested and FALSIFIED (recorded for honesty)

- **Golden ratio / π in digit ratios**: no relationship (7/4≈√3 is coincidence, and √3 is
  neither φ nor π). Negative.
- **π / golden-ratio / Fibonacci digit-derived permutations** as the universal *rules*: the
  universal $\pi_{\mathrm{inv}}$ match constant-derived permutations no better than random
  (6/16, equal to random max). Negative.
- **Genuine 3D geometry**: the structure is essentially **1-dimensional** (the gap line
  $\{1,2,3\}$ with middle gap 2) intersected with the mod-9 lattice. No real 3D content was
  found; none was invented.

---

## EXHAUSTIVE CONFIRMATION (2026-06-03) — all 24 mod-9 sets

Since mod-9 is *proven necessary*, the only fertility candidates are the **24** four-digit sets
with digit-sum ≡ 0 (mod 9). Every one was tested at d=12 (m=3) via pair-symmetric search:

| outcome | count | sets |
|---|---:|---|
| FERTILE — (p,q)=(6,2), desc−asc=6174 | **2** | {1,4,6,7}, {2,3,5,8} |
| extinct — (p,q)≠(6,2) | **22** | all others |

**0 exceptions across all 24.** This is no longer a 7-case predictor — it is an **exhaustive
classification of base-10**.

### The mechanism (and a route to a full proof)
Every one of the 22 extinct sets produced **zero candidates** — i.e., the pair-symmetric rule's
output K *never lands on the set's own multiset* unless (p,q)=(6,2). So the predictor's content
is really:

> **Structural claim (verified, proof open):** the pair-symmetric rule on a 4-digit set
> $\{D_0>D_1>D_2>D_3\}$ has a fixed point with multiset $\{D_0,D_1,D_2,D_3\}^m$ **only if**
> $(D_0-D_3,\,D_1-D_2) = (6,2)$.

This reduces the fertility theorem to a statement about the **digit structure of
$K = 6S_0+2S_1$ vs other $pS_0+qS_1$** — a finite, arithmetic question, not a dynamical one.
Proving it would make the fertility predictor a complete theorem (the mod-9 half is already
proven). The $(6,2)$ value is exactly the 6174 signature ($6174 = 999\cdot6 + 90\cdot2$).

### Bottom line
The multiplicity chain exists for **exactly two** four-digit sets, both carrying the 6174
coefficient signature $(6,2)$. The phenomenon is 6174-specific, exhaustively, across base 10.
