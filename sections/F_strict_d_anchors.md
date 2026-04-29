# Appendix F. Strict-$`d`$ Anchors and the $`\{7, 6, 4, 1\}`$-Thread Tower

*Status: Preliminary working notes added April 29, 2026. The classifications and
counts in §F.3 and §F.4 are computational findings established by two
independent enumerations: the original `universality_scan_v3.py` run and a
fresh from-scratch verifier (`verifier_v2.py`, fp-first traversal with direct
$`(A, B)`$ image-pair enumeration) that reproduces every count exactly. The
strict-$`d`$ criterion of §F.2 is well-defined and exactly captures the
distinction we use; whether it is the right central object for a future
revision of the main paper, and whether the reported $`d = 7`$ counts extend
to higher $`d`$, are explicitly left open in §F.6.*

## F.1 Purpose

The main paper establishes that $`60714`$ is a universal full-variable fixed
point at every digit length $`d \geq 5`$ under the coefficient-preserving
lifting family of §5 (Theorem 3). That result is unchanged.

The notion of universality used throughout the main paper admits absorption to
$`0`$: a rule $`K`$ is universal for fixed point $`F`$ at digit length $`d`$
iff every input in $`A_d`$ (the admissible inputs, excluding repdigits and
near-repdigits) iterates under $`K`$ either to $`F`$ or to $`0`$, with no input
entering a non-$`\{F, 0\}`$ cycle. Inputs that absorb to $`0`$ are the
structurally characterized escape class of §5 (Lemma 5.1, Lemma 5.2). The
present appendix makes this convention explicit and uses the abbreviation
**F-or-0 universality** when the distinction matters.

This appendix introduces a strengthened criterion — *strict at $`d`$* — that
distinguishes rules whose dynamics genuinely involve all $`d`$ coefficient
positions on $`F`$ from rules that are zero-sum-pair extensions of
lower-dimensional rules. Under the strict criterion, the cross-dimensional
structure of the $`\{7, 6, 4, 1\}`$-thread is substantially richer than
reported in the main paper, and the classical Kaprekar constants $`6174`$ and
$`1746`$ acquire strict-anchor status at $`d = 7`$ — a finding consistent
with, but sharper than, the cross-dimensional pattern of $`6174`$ described in
§6.

## F.2 The strict-$`d`$ criterion

Let $`K = K_{\pi, \sigma}`$ be a universal full-variable rule for $`F`$ at
digit length $`d`$, with coefficient vector
$`c = (c_0, c_1, \ldots, c_{d-1})`$, and let $`(x_0, x_1, \ldots, x_{d-1})`$
denote $`F`$'s sorted-descending form padded to $`d`$ positions.

***Definition F.1*** *(trivial zero-sum pair on $`F`$).* A pair of indices
$`(i, j)`$ with $`i < j`$ is a *trivial zero-sum pair on $`F`$* if
$`c_i + c_j = 0`$ and $`x_i = x_j`$. Such a pair contributes
$`c_i x_i + c_j x_j = c_i (x_i - x_j) = 0`$ to $`K(F)`$, so the fixed-point
equation $`K(F) = F`$ is unchanged if the pair is removed: the rule's action
on $`F`$ itself is reproduced by a $`(d-2)`$-coefficient sub-rule.

***Definition F.2*** *(strict at $`d`$).* A universal full-variable rule
$`K`$ for $`F`$ at digit length $`d`$ is *strict at $`d`$* if its coefficient
vector has no trivial zero-sum pair on $`F`$ in the sense of Definition F.1.

***Definition F.3*** *(strict-$`d`$ anchor).* A fixed point $`F`$ is a
*strict-$`d`$ anchor* if $`F`$ is a universal full-variable fixed point at
digit length $`d`$ and admits at least one strict-at-$`d`$ universal rule.

The main paper's results are stated in terms of universal fps; that is, fps
admitting any universal full-variable rule. Strict-$`d`$ anchors are the
subset of universal fps for which the universality is not achieved purely by
zero-sum-pair extension on equal-digit positions of $`F`$.

## F.3 The {7,6,4,1}-thread under strict-$`d`$

We applied the strict-$`d`$ criterion exhaustively at digit lengths
$`d = 5, 6, 7`$ to all universal full-variable fps in the relevant
zero-padded extensions of $`\{7, 6, 4, 1\}`$.

***Observation F.1*** *(strict-$`d`$ anchors of the $`\{7, 6, 4, 1\}`$-thread).*
The strict-$`d`$ anchors at digit lengths $`d \leq 7`$ are:

| $`d`$ | Multiset | Strict-$`d`$ anchors | Count |
|---|---|---|---|
| 4 | $`\{7,6,4,1\}`$ | $`1746`$, $`6174`$ | 2 |
| 5 | $`\{7,6,4,1,0\}`$ | $`60417`$, $`60714`$ | 2 |
| 6 | $`\{7,6,4,1,0,0\}`$ | $`60714`$, $`146070`$, $`170460`$, $`607140`$ | 4 |
| 7 | $`\{7,6,4,1,0,0,0\}`$ | (see below) | 11 |

The full $`d = 7`$ list is:

> $`1746`$, $`6174`$, $`17460`$, $`61740`$, $`146070`$, $`174006`$, $`174600`$,
> $`1{,}400{,}706`$, $`1{,}460{,}700`$, $`1{,}746{,}000`$, $`6{,}174{,}000`$.

The $`d = 6`$ classification reproduces the four-fp set highlighted in §6.2.3
of the main paper. The $`d = 7`$ classification is new in this appendix.

The verification is computational. For each $`d \in \{5, 6, 7\}`$ we
enumerated all sv$`=d`$ rules fixing each integer in the multiset, tested
each fixer for universality (under the F-or-0 convention), and tested each
universal rule for the strict-$`d`$ criterion of Definition F.2. The
classification was carried out by two independently developed scanners:
`universality_scan_v3.py` (rule-first traversal) and `verifier_v2.py`
(fp-first traversal, fresh from-scratch implementation). Both scanners
produce the same lists at $`d = 5, 6, 7`$, the same rule-counts per fp, and
the same actual rule sets where checked. Source code and JSON outputs are
provided as supplementary material.

## F.4 The non-monotone strict-anchor pattern

***Observation F.2*** *(non-monotone strict-anchor pattern of $`6174`$ and
$`1746`$).* The classical Kaprekar fixed points $`6174`$ and $`1746`$ are
strict-$`d`$ anchors at $`d = 4`$ and $`d = 7`$, but not at $`d = 5`$ or
$`d = 6`$. Specifically:

- *At $`d = 5`$:* neither $`6174`$ nor $`1746`$ admits any sv$`=5`$ rule
  satisfying $`K(F) = F`$ (algebraic obstruction). This matches §1.4 of the
  main paper.
- *At $`d = 6`$:* both $`6174`$ and $`1746`$ admit universal sv$`=6`$ rules
  under the F-or-0 convention, but every such rule is a zero-sum-pair
  extension of the classical $`d = 4`$ rule on the two zero positions. Under
  Definition F.2 these rules are non-strict.
- *At $`d = 7`$:* $`6174`$ admits $`6`$ strict-$`d = 7`$ universal rules and
  $`1746`$ admits $`12`$. The rules engage all seven coefficient positions in
  non-trivial pairings, with no pair summing to zero on equal digits of $`F`$.

This pattern was previewed in §6 of the main paper as the *cross-dimensional
fingerprint* of $`6174`$ (universal at $`d = 4`$ and near-universal at
$`d \geq 7`$, obstructed at $`d = 5, 6`$), but stated in terms of universality
rather than strict anchorhood. The strict-$`d`$ criterion sharpens the
observation: $`6174`$'s reappearance at $`d = 7`$ is not a quirk of a
particular lifting family but a structural feature — $`6174`$ is a
strict-$`d`$ anchor at $`d = 7`$ in the same sense it is at $`d = 4`$.

***Observation F.3*** *(strict-anchor status of $`60714`$ and $`60417`$ at
$`d = 7`$).* Both $`60714`$ and $`60417`$ admit universal sv$`=7`$ rules at
$`d = 7`$ under the F-or-0 convention, but every such rule contains a trivial
zero-sum pair on $`F`$. Under Definition F.2, $`60714`$ and $`60417`$ are not
strict-$`d`$ anchors at $`d = 7`$.

For $`60714`$, the canonical lifting of §5 of the main paper has coefficient
vector

$$c = (9900,\; 9,\; 90,\; -9000,\; -999,\; 900000,\; -900000).$$

The pair $`(900000, -900000)`$ at indices $`5, 6`$ lands on the two trailing
zero positions of the sorted-descending form
$`\mathrm{sort\_desc}(60714) = (7, 6, 4, 1, 0, 0, 0)`$. Both positions hold
digit $`0`$, so the pair contributes zero on $`F`$, and the fixed-point
equation is reproduced by the five-coefficient sub-rule at indices
$`\{0, 1, 2, 3, 4\}`$ — which is precisely the $`d = 5`$ rule.

This observation is consistent with the main paper's Theorem 3: $`60714`$ is
a universal full-variable fp at every $`d \geq 5`$. The strengthening is that
for $`d \geq 7`$, the lifting is non-strict by Definition F.2; the genuinely
$`d`$-dimensional dynamics of $`60714`$ live at $`d = 5`$ and $`d = 6`$.

## F.5 Pure-duplication extensions

The main paper considers only zero-padded extensions of multisets across
$`d`$. We tested the alternative — *pure-duplication extension*, where the
digits added at $`d > 4`$ are drawn from the classical core itself (e.g.,
$`\{7, 7, 6, 4, 1\}`$ at $`d = 5`$).

***Observation F.4*** *(pure-duplication extensions are empty).* Let
$`M = \{7, 6, 4, 1\}`$ be the $`d = 4`$ classical multiset. For
$`d \in \{5, 6\}`$, every multiset of the form $`M \cup S`$ with $`S`$
drawn from $`M`$ has digit sum $`18 + |S| \cdot \bar{m}`$ where $`\bar{m}`$
ranges over averages of multisets of $`M`$. No such sum is divisible by $`9`$
for $`|S| \in \{1, 2\}`$; consequently no universal fp exists in these
multisets at $`d = 5, 6`$. For $`d = 7`$, four pure-duplication multisets are
admissible by digit sum — namely
$`\{7,7,7,6,4,4,1\}`$, $`\{7,7,6,4,1,1,1\}`$,
$`\{7,6,6,6,6,4,1\}`$, $`\{7,6,4,4,4,1,1\}`$
— and exhaustive enumeration over all sv$`\geq 2`$ rules at $`d = 7`$
produces zero rule-fp pairs satisfying $`K(F) = F`$ in any of the four. The
same result holds for $`\{8, 5, 3, 2\}`$ at $`d = 5, 6, 7`$. We conjecture, on
this evidence, that pure-duplication extension produces no Kaprekar fixed
points at any $`d > 4`$ for either classical thread.

This identifies zero-padding as the *unique* viable extension mechanism for
the $`\{7, 6, 4, 1\}`$-thread (and, by the analog with $`9`$ in place of
$`0`$, for the $`\{8, 5, 3, 2\}`$-thread). The thread structure is not just
one extension among several — it is forced.

## F.6 Open questions

This appendix reports observations; it does not settle them.

1. *Is the strict-$`d`$ criterion of Definition F.2 the right structural
   object?* The criterion captures the zero-sum-pair-on-equal-digits structure
   that distinguishes trivial lifts from genuinely $`d`$-dimensional rules.
   A complementary criterion (no proper sub-rule reproduces dynamics on all
   admissibles) was tested empirically at $`d = 5, 6`$ and never failed when
   Definition F.2 was satisfied; we expect the two are equivalent for the
   rules in scope here, but have not proved this. A full $`d = 7`$
   verification of the complementary criterion is pending.

2. *Why do $`6174`$ and $`1746`$ reappear as strict-$`d`$ anchors at $`d = 7`$
   but not at $`d = 5, 6`$?* The non-monotone pattern admits a candidate
   explanation in terms of the $`d = 7`$ rule space's allowance for
   three-position non-zero-sum tails, which the $`d = 5, 6`$ rule spaces do
   not accommodate. A precise statement and proof are open.

3. *Strict-anchor count at $`d = 8, 9, \ldots`$?* The $`d = 7`$ count is
   $`11`$ — substantially larger than the $`d = 6`$ count of $`4`$. Whether
   the strict-anchor count continues to grow with $`d`$, stabilizes, or
   oscillates is open. Computational reach at $`d = 8`$ is feasible on
   Apple M-series hardware; runs are pending.

4. *Parallel structure for the $`\{8, 5, 3, 2\}`$-thread.* Strict-$`d`$
   anchor counts at $`d = 5, 6`$ are $`3, 3`$ (versus $`2, 4`$ for
   $`\{7, 6, 4, 1\}`$). The asymmetric widths between threads, despite both
   threads sharing digit sum $`18`$ at $`d = 4`$, is structural and not yet
   explained. The $`d = 7`$ analog for the $`\{8, 5, 3, 2\}`$-thread is
   pending.

5. *Are there other classical multiset cores beyond $`\{7,6,4,1\}`$ and
   $`\{8,5,3,2\}`$?* These are the only two universal multisets at $`d = 4`$.
   Whether the strict-anchor tower formalism extends to threads anchored at
   $`d > 4`$ (e.g., among the $`33`$ universal fps at $`d = 5`$) is open.

6. *Relation to the main paper's Theorem 3.* The main paper proves $`60714`$
   universal at every $`d \geq 5`$. Under Definition F.2 of this appendix,
   $`60714`$ is strict-universal at $`d = 5, 6`$ only; the lifts at
   $`d \geq 7`$ are non-strict. The main paper's theorem remains correct
   under its own (sv$`=d`$, F-or-0) framework. The reframing question —
   whether the central object of the theory is the
   (sv$`=d`$)-universal tower or the strict-$`d`$-universal tower — is not
   settled here.

## F.7 Reproducibility note

The results of this appendix are reproducible from the supplementary scripts.
The main scanner is `universality_scan_v3.py`; the independent verifier is
`verifier_v2.py`. Both produce JSON outputs containing per-fp rule counts and
the explicit list of strict-$`d`$ rules for each anchor. Total wall-time on
2024-era commodity hardware: under three minutes for the complete
$`d \in \{5, 6, 7\}`$ scan.

---

*End of Appendix F.*
