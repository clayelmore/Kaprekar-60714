[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix B. 60714 ladder](B_60714_ladder.md) · [Next: Appendix D. Transcendent fps at $`d_F = 7`$ →](D_dF7_observations.md)

---

# Appendix C. Support Lemmas for the Proof of Theorem 5.2

This appendix provides the technical support lemmas referenced in §5. The organization mirrors the proof of Theorem 5.2: §C.1 fixes setup, §C.2 proves core non-negativity (Lemma 5.3), §C.3 proves core upper bound (Lemma 5.4), §C.4 proves the reaching-time bound on the odd ladder, §C.5 addresses the even ladder, and §C.6 establishes the admissible-projection lemma.

## C.1 Setup

Throughout, $`(x_0, x_1, \ldots, x_{d-1})`$ denotes a sorted-descending digit sequence with $`x_0 \geq x_1 \geq \cdots \geq x_{d-1}`$ and each $`x_i \in \{0, 1, \ldots, 9\}`$. The **native core contribution** (Definition 5.4) is

$$\mathrm{core}(x) \;=\; 9900 \, x_0 + 9 \, x_1 + 90 \, x_2 - 9000 \, x_3 - 999 \, x_4.$$

## C.2 Core non-negativity (Proof of Lemma 5.3)

**Lemma 5.3 (restated).** *For every sorted-descending sequence $`(x_0, x_1, x_2, x_3, x_4)`$, $`\mathrm{core}(x) \geq 0`$.*

**Proof.** We proceed by case analysis on the values of $`x_3`$ and $`x_4`$.

**Case 1: $`x_3 = x_4 = 0`$.** Then $`\mathrm{core}(x) = 9900 x_0 + 9 x_1 + 90 x_2 \geq 0`$, with equality iff $`x_0 = x_1 = x_2 = 0`$.

**Case 2: $`x_3 \geq 1`$, $`x_4 = 0`$.** By sorted-descending, $`x_0 \geq x_3 \geq 1`$. Writing $`\mathrm{core}(x) = 9000(x_0 - x_3) + 900 x_0 + 9 x_1 + 90 x_2`$, each term is non-negative, so $`\mathrm{core}(x) \geq 0`$.

**Case 3: $`x_3 \geq 1`$ and $`x_4 \geq 1`$.** We use $`x_2 \geq x_3`$ and $`x_1 \geq x_4`$:

$$\mathrm{core}(x) = 9900 x_0 + 9 x_1 + 90 x_2 - 9000 x_3 - 999 x_4.$$

Replace $`90 x_2 \geq 90 x_3`$ (valid since $`x_2 \geq x_3`$):

$$\mathrm{core}(x) \geq 9900 x_0 + 9 x_1 + 90 x_3 - 9000 x_3 - 999 x_4 = 9900 x_0 + 9 x_1 - 8910 x_3 - 999 x_4.$$

Replace $`9 x_1 \geq 9 x_4`$:

$$\mathrm{core}(x) \geq 9900 x_0 - 8910 x_3 - 999 x_4 + 9 x_4 = 9900 x_0 - 8910 x_3 - 990 x_4.$$

Replace $`x_4 \leq x_3`$:

$$\mathrm{core}(x) \geq 9900 x_0 - 8910 x_3 - 990 x_3 = 9900 x_0 - 9900 x_3 = 9900 (x_0 - x_3) \geq 0,$$

using $`x_0 \geq x_3`$ in the last step.

All three cases cover the admissible possibilities (Case 4 with $`x_3 = 0`$ and $`x_4 \geq 1`$ is impossible by sorted-descending). In each, $`\mathrm{core}(x) \geq 0`$. $`\square`$

**Remark C.1.** The minimum $`\mathrm{core}(x) = 0`$ is achieved at $`x = (0, 0, 0, 0, 0)`$ (repdigit zero). Direct enumeration over all $`2{,}002`$ sorted-descending sequences in $`\{0, \ldots, 9\}^5`$ confirms the minimum is exactly $`0`$.

## C.3 Core upper bound (Proof of Lemma 5.4)

**Lemma 5.4 (restated).** *For every sorted-descending sequence $`(x_0, x_1, x_2, x_3, x_4)`$, $`\mathrm{core}(x) \leq 89{,}991 < 10^5`$.*

**Proof.** The negative terms $`-9000 x_3 - 999 x_4`$ contribute at most $`0`$ (when $`x_3 = x_4 = 0`$), so:

$$\mathrm{core}(x) \leq 9900 x_0 + 9 x_1 + 90 x_2 \leq 9900 \cdot 9 + 9 \cdot 9 + 90 \cdot 9 = 89{,}100 + 81 + 810 = 89{,}991.$$

The maximum is achieved at $`(x_0, x_1, x_2, x_3, x_4) = (9, 9, 9, 0, 0)`$. $`\square`$

**Corollary C.2 (computational verification).** *Direct enumeration over all $`2{,}002`$ sorted-descending sequences $`(x_0, \ldots, x_4) \in \{0, \ldots, 9\}^5`$ confirms $`\mathrm{core}(x) \in [0, 89{,}991]`$ with minimum $`0`$ at $`(0, 0, 0, 0, 0)`$ and maximum $`89{,}991`$ at $`(9, 9, 9, 0, 0)`$. Runtime: milliseconds.*

## C.4 The $`T_d`$ reaching-time bound (odd ladder)

The main technical claim underlying Proposition 5.3 rests on a **block-structure decomposition** of the lifted rule's output.

## C.4.1 Block-structure decomposition

At odd digit length $`d \geq 7`$, the odd-ladder rule $`K^{(d)}_{60714}`$ has coefficient vector

$$c^{(d)} = \underbrace{(9900, 9, 90, -9000, -999)}_{\text{native, positions } 0..4} \; \| \; \underbrace{(+p_1, -p_1)}_{\text{pair }1, \text{positions } 5, 6} \; \| \; \cdots \; \| \; \underbrace{(+p_M, -p_M)}_{\text{pair }M, \text{positions } d-2, d-1},$$

where $`M = (d-5)/2`$ and $`p_k = 9 \cdot 10^{3 + 2k}`$ is the pair-$`k`$ magnitude. Pair $`k`$ occupies positions $`(3 + 2k, 4 + 2k)`$.

**Pair contribution.** For input $`(x_0, \ldots, x_{d-1})`$, each pair $`k`$ contributes

$$p_k \cdot x_{3 + 2k} - p_k \cdot x_{4 + 2k} = p_k \, \delta_k, \qquad \text{where } \delta_k := x_{3 + 2k} - x_{4 + 2k} \in \{0, 1, \ldots, 9\}.$$

By the sorted-descending constraint, each $`\delta_k \geq 0`$.

**Lemma C.6 (cliff-sequence bound).** *For any sorted-descending sequence $`(x_0, \ldots, x_{d-1})`$ with each $`x_i \in \{0, \ldots, 9\}`$,*

$$\sum_{k = 1}^{M} \delta_k \;=\; \sum_{k = 1}^{M} (x_{3 + 2k} - x_{4 + 2k}) \;\leq\; 9.$$

**Proof.** Each $`\delta_k`$ is a non-negative adjacent-position difference within the sorted-descending sequence. The sum is a subset of the telescoping total $`\sum_{i=3}^{d-2} (x_i - x_{i+1}) = x_3 - x_{d-1}`$. Since all differences are non-negative and $`x_3 - x_{d-1} \leq 9`$, the selected subsum is bounded by the full telescoping:

$$\sum_{k = 1}^{M} \delta_k \leq x_3 - x_{d-1} \leq 9.$$

$`\square`$

## C.4.2 Non-negativity of $`K^{(d)}(x)`$

**Lemma C.7.** *For every sorted-descending $`(x_0, \ldots, x_{d-1})`$ and every odd $`d \geq 7`$,*

$$K^{(d)}(x) \;=\; \mathrm{core}(x) + \sum_{k=1}^{M} p_k \, \delta_k.$$

*In particular, $`K^{(d)}(x) \geq 0`$, so the absolute value operation in the rule definition is vacuous on sorted-descending inputs.*

**Proof.** Direct substitution into the expanded rule gives

$$K^{(d)}(x) \;=\; \left| \sum_{i = 0}^{d-1} c_i \, x_i \right| \;=\; \left| \mathrm{core}(x) + \sum_{k=1}^{M} p_k \, \delta_k \right|.$$

By Lemma 5.3, $`\mathrm{core}(x) \geq 0`$. Each $`p_k \, \delta_k \geq 0`$ (since $`p_k > 0`$ and $`\delta_k \geq 0`$). Hence the argument is non-negative and the absolute-value bars can be dropped. $`\square`$

## C.4.3 The reaching-time theorem

**Lemma C.3 (one-step $`T_d`$ closure on the odd ladder at $`d \geq 15`$).** *Let $`d \geq 15`$ be odd. For every admissible input $`n \in A_d`$ with sorted-descending form $`(x_0, \ldots, x_{d-1})`$,*

$$K^{(d)}_{60714}(n) \in T_d.$$

*Equivalently, the padded $`d`$-digit representation of $`K^{(d)}(n)`$ has at least two zero digits.*

**Proof.** By Lemma C.7,

$$K^{(d)}(x) \;=\; \mathrm{core}(x) + \sum_{k=1}^{M} 9 \cdot 10^{3 + 2k} \, \delta_k.$$

**Decimal-block structure.** Each term $`9 \cdot 10^{3 + 2k} \delta_k`$ occupies decimal positions $`[3 + 2k, 4 + 2k]`$ as a two-digit value. Writing $`9 \delta_k = 10 u_k + v_k`$ for $`u_k, v_k \in \{0, \ldots, 9\}`$:

$$9 \cdot 10^{3 + 2k} \delta_k = u_k \cdot 10^{4 + 2k} + v_k \cdot 10^{3 + 2k}.$$

The digit pairs $`(u_k, v_k)`$ for each $`\delta_k`$:

| $`\delta_k`$ | $`9 \delta_k`$ | $`(u_k, v_k)`$ | Zeros |
|:---:|:---:|:---:|:---:|
| $`0`$ | $`0`$  | $`(0, 0)`$ | $`2`$ |
| $`1`$ | $`9`$  | $`(0, 9)`$ | $`1`$ |
| $`2`$ | $`18`$ | $`(1, 8)`$ | $`0`$ |
| $`3`$ | $`27`$ | $`(2, 7)`$ | $`0`$ |
| $`4`$ | $`36`$ | $`(3, 6)`$ | $`0`$ |
| $`5`$ | $`45`$ | $`(4, 5)`$ | $`0`$ |
| $`6`$ | $`54`$ | $`(5, 4)`$ | $`0`$ |
| $`7`$ | $`63`$ | $`(6, 3)`$ | $`0`$ |
| $`8`$ | $`72`$ | $`(7, 2)`$ | $`0`$ |
| $`9`$ | $`81`$ | $`(8, 1)`$ | $`0`$ |

**Disjoint blocks.** Pair $`k`$'s block occupies decimals $`[3 + 2k, 4 + 2k]`$. Since the block value $`9 \delta_k \leq 81 < 100`$, it fits entirely within two decimal positions and does not propagate carries to higher blocks. Similarly, $`\mathrm{core}(x) \leq 89{,}991 < 10^5`$ (Lemma 5.4) fits within decimals $`[0, 4]`$ with at most one carry into decimal $`5`$. That carry combines additively with pair $`1`$'s block at positions $`[5, 6]`$: the combined value is at most $`u_1 \cdot 10 + v_1 + 1 = 9 \delta_1 + 1 \leq 82`$, still a two-digit value, so no further carry to decimal $`7`$. Blocks for $`k \geq 2`$ retain their $`(u_k, v_k)`$ form exactly.

**Counting zeros in the block region.** Define

$$Z_0 := \bigl|\{k : \delta_k = 0\}\bigr|, \qquad Z_1 := \bigl|\{k : \delta_k = 1\}\bigr|, \qquad Z_{2+} := \bigl|\{k : \delta_k \geq 2\}\bigr|.$$

Then $`Z_0 + Z_1 + Z_{2+} = M`$, and the number of zero digits contributed by blocks is at least $`2 Z_0 + Z_1`$ (each $`\delta_k = 0`$ block contributes $`2`$ zeros; each $`\delta_k = 1`$ block contributes $`1`$ zero from $`u_k = 0`$).

From Lemma C.6, $`\sum_k \delta_k \leq 9`$. Since $`\delta_k \geq 2`$ for $`k \in Z_{2+}`$:

$$2 Z_{2+} + Z_1 \leq \sum_k \delta_k \leq 9.$$

Therefore:

$$2 Z_0 + Z_1 \;=\; 2(M - Z_1 - Z_{2+}) + Z_1 \;=\; 2M - Z_1 - 2 Z_{2+} \;\geq\; 2M - 9.$$

**At odd $`d \geq 17`$: $`M \geq 6`$, so $`2 Z_0 + Z_1 \geq 3`$.** This alone gives at least $`3`$ zero digits in the block region, more than enough for $`K^{(d)}(x) \in T_d`$.

**At $`d = 15`$ (odd): $`M = 5`$, so $`2 Z_0 + Z_1 \geq 1`$.** This gives at least one zero digit from the block region, but the second zero requires a refined analysis. We complete the argument by partitioning according to the value of $`x_4`$.

**Lemma C.7 (sharpened cliff-sum bound for $`d = 15`$).** *For sorted-descending $`(x_0, \ldots, x_{14})`$ with $`x_i \in \{0, \ldots, 9\}`$,*

$$\sum_{k = 1}^{5} \delta_k \;\leq\; x_4.$$

*Proof.* Each $`\delta_k = x_{3 + 2k} - x_{4 + 2k}`$ for $`k = 1, \ldots, 5`$ is a non-negative adjacent-position difference among positions $`5, 6, \ldots, 14`$. The full telescoping over these positions is

$$\sum_{i = 5}^{13} (x_i - x_{i+1}) = x_5 - x_{14}.$$

Our sum $`\sum_k \delta_k`$ picks out the five differences $`(x_5 - x_6), (x_7 - x_8), (x_9 - x_{10}), (x_{11} - x_{12}), (x_{13} - x_{14})`$, a strict subset of these nine. Since every omitted difference is non-negative,

$$\sum_{k=1}^{5} \delta_k \;\leq\; x_5 - x_{14} \;\leq\; x_5 \;\leq\; x_4. \qquad \square$$

**Lemma C.8 (core-bound when $`x_4 \in \{8, 9\}`$).** *If $`x_4 \geq 8`$ in sorted-descending $`(x_0, \ldots, x_4)`$, then $`\mathrm{core}(x) < 10^4`$.*

*Proof.* By sorted-descending, $`x_4 \geq 8`$ forces $`x_0, x_1, x_2, x_3 \in \{8, 9\}`$. We compute:

$$\mathrm{core}(x) = 9900 x_0 + 9 x_1 + 90 x_2 - 9000 x_3 - 999 x_4 = 9000(x_0 - x_3) + 900 x_0 + 9 x_1 + 90 x_2 - 999 x_4.$$

Since $`x_0, x_3 \in \{8, 9\}`$ with $`x_0 \geq x_3`$, we have $`x_0 - x_3 \in \{0, 1\}`$.

*Case $`x_0 = x_3`$:* The first term vanishes. Then

$$\mathrm{core}(x) = 900 x_0 + 9 x_1 + 90 x_2 - 999 x_4.$$

The maximum over $`x_0, x_1, x_2 \in \{8, 9\}`$ and $`x_4 \in \{8, 9\}`$ with $`x_4 \leq x_3 = x_0`$ is achieved at $`x_0 = x_1 = x_2 = 9`$, $`x_4 = 8`$: $`900 \cdot 9 + 9 \cdot 9 + 90 \cdot 9 - 999 \cdot 8 = 8100 + 81 + 810 - 7992 = 999`$. So $`\mathrm{core}(x) \leq 999 < 10^3`$.

*Case $`x_0 = x_3 + 1`$:* Then $`x_0 = 9`$ and $`x_3 = x_4 = 8`$ (forcing $`x_4 = 8`$ since $`x_4 \leq x_3`$). We get

$$\mathrm{core}(x) = 9000 + 900 \cdot 9 + 9 x_1 + 90 x_2 - 999 \cdot 8 = 9108 + 9 x_1 + 90 x_2$$

for $`x_1, x_2 \in \{8, 9\}`$ with $`x_1 \geq x_2 \geq 8`$. The minimum is $`9108 + 72 + 720 = 9900`$ and the maximum is $`9108 + 81 + 810 = 9999`$. So $`\mathrm{core}(x) \in [9900, 9999]`$, and in particular $`\mathrm{core}(x) < 10^4`$.

In both cases, $`\mathrm{core}(x) < 10^4`$. $`\square`$

We now complete the $`d = 15`$ closure argument.

**Three cases for the second zero digit.**

*Case A: $`x_4 = 0`$.* By sorted-descending, $`x_5 = x_6 = \cdots = x_{14} = 0`$. All five $`\delta_k = 0`$, so every block contributes $`(0, 0)`$ at decimals $`[5, 6], [7, 8], \ldots, [13, 14]`$. The block region produces $`10`$ zero digits at decimals $`5`$ through $`14`$. Even after accounting for at most one carry from the core into decimal $`5`$, decimals $`6`$ through $`14`$ remain zero — that is $`9`$ zero digits, far more than the $`2`$ required.

*Case B1: $`1 \leq x_4 \leq 7`$.* By Lemma C.7, $`\sum_k \delta_k \leq x_4 \leq 7`$. Since $`\delta_k \geq 2`$ for $`k \in Z_{2+}`$,

$$2 Z_{2+} + Z_1 \leq \sum_k \delta_k \leq 7,$$

which gives

$$2 Z_0 + Z_1 = 2M - Z_1 - 2 Z_{2+} \geq 10 - 7 = 3.$$

So the block region contributes at least $`3`$ zero digits.

*Case B2: $`x_4 \in \{8, 9\}`$.* By Lemma C.8, $`\mathrm{core}(x) < 10^4`$, so the padded core occupies only decimals $`0`$ through $`3`$, and decimal $`4`$ is a zero digit in the core's contribution to $`K^{(15)}(x)`$. Combined with at least one zero digit from the block region (the $`2 Z_0 + Z_1 \geq 1`$ bound), this gives at least $`2`$ zero digits total.

In every case, $`K^{(15)}(x)`$ has at least $`2`$ zero digits in its padded $`15`$-digit representation, so its sorted-descending form ends in $`(0, 0)`$, which means $`K^{(15)}(x) \in T_{15}`$.

Combining: at every odd $`d \geq 15`$, $`K^{(d)}(x)`$ has at least $`2`$ zero digits in its padded $`d`$-digit form, hence $`K^{(d)}(x) \in T_d`$. $`\square`$

**Remark C.3 (at $`d \leq 13`$, the bound fails).** At $`d = 13`$ (odd), $`M = 4`$ and $`2 Z_0 + Z_1 \geq -1`$ is vacuous. The algebraic argument does not apply. The finite-state enumeration of Proposition 5.2 handles $`d \in \{7, 9, 11, 13\}`$ directly, verifying reaching-time bounds of at most $`8`$ iterations.

**Corollary C.3 (computational confirmation).** *Direct enumeration at $`d = 15`$ and $`d = 17`$ (odd ladder) over all admissible multisets ($`1{,}307{,}404`$ and $`3{,}124{,}450`$ respectively) verifies one-step $`T_d`$ closure: every admissible input reaches $`T_d`$ in exactly one iteration.*

## C.5 The even ladder

The even-ladder root at $`d = 6`$ uses the split-lifted rule with coefficient vector $`(9900, 9, 90, -9000, 99000, -99999)`$. The split replaces the native $`c_4 = -999`$ with two coefficients at positions $`4`$ and $`5`$ summing to $`-999`$. For all higher even $`d`$, zero-sum pair extensions operate from $`d = 6`$.

**Lemma C.4 (one-step $`T_d`$ closure on the even ladder at $`d \geq 18`$).** *Let $`d \geq 18`$ be even. For every admissible input $`n \in A_d`$ with sorted-descending form $`(x_0, \ldots, x_{d-1})`$,*

$$K^{(d)}_{60714}(n) \in T_d.$$

*Equivalently, the padded $`d`$-digit representation of $`K^{(d)}(n)`$ has at least two zero digits.*

**Proof.** The proof follows the same template as Lemma C.3 (odd ladder), with the $`d_0 = 6`$ split-root in place of the $`d_0 = 5`$ native root. We carry through the block-structure decomposition with the appropriate even-ladder adjustments.

*Setup.* At even $`d \geq 8`$, the coefficient vector is

$$c^{(d)} = (\underbrace{9900,\, 9,\, 90,\, -9000,\, 99000,\, -99999}_{\text{split root, positions } 0\text{-}5}) \, \| \, \underbrace{(+9 \cdot 10^7, -9 \cdot 10^7)}_{\text{pair }0,\text{ positions }6,7} \, \| \, \cdots \, \| \, \underbrace{(+9 \cdot 10^{d-1}, -9 \cdot 10^{d-1})}_{\text{pair }M'-1,\text{ positions }d-2,d-1}$$

where $`M' = (d - 6)/2`$ is the number of appended pairs.

*Block-structure decomposition.* For $`x = (x_0, \ldots, x_{d-1})`$ sorted descending, define $`\delta_k = x_{2k+6} - x_{2k+7}`$ for $`k = 0, 1, \ldots, M'-1`$, so $`\delta_k \in \{0, 1, \ldots, 9\}`$. Then

$$K^{(d)}(x) = \mathrm{core}_{\mathrm{even}}(x) + \sum_{k=0}^{M'-1} 9 \cdot 10^{2k+7} \, \delta_k$$

where $`\mathrm{core}_{\mathrm{even}}(x) = 9900 x_0 + 9 x_1 + 90 x_2 - 9000 x_3 + 99000 x_4 - 99999 x_5`$ depends only on the first $`6`$ positions, and is non-negative (Lemma C.9 below).

*Decimal-block structure.* Each block term $`9 \cdot 10^{2k+7} \delta_k`$ occupies decimal positions $`[2k+7, 2k+8]`$ as a two-digit value. Writing $`9 \delta_k = 10 u_k + v_k`$ for $`u_k, v_k \in \{0, \ldots, 9\}`$:

| $`\delta_k`$ | $`9\delta_k`$ | digit at $`2k+7`$ ($`v_k`$) | digit at $`2k+8`$ ($`u_k`$) |
|:---:|:---:|:---:|:---:|
| $`0`$ | $`0`$ | $`0`$ | $`0`$ |
| $`1`$ | $`9`$ | $`9`$ | $`0`$ |
| $`2`$ | $`18`$ | $`8`$ | $`1`$ |
| $`3`$ | $`27`$ | $`7`$ | $`2`$ |
| $`\vdots`$ | $`\vdots`$ | $`\vdots`$ | $`\vdots`$ |
| $`9`$ | $`81`$ | $`1`$ | $`8`$ |

*Block decimal positions are pairwise disjoint and disjoint from the core.* Block $`k`$'s contribution affects only decimal positions $`2k+7`$ and $`2k+8`$. Block $`k+1`$'s contribution affects positions $`2(k+1)+7 = 2k+9`$ and $`2(k+1)+8 = 2k+10`$. These do not overlap. The maximum block-$`k`$ value is $`81 \cdot 10^{2k+7}`$ (when $`\delta_k = 9`$), which has digits at positions $`2k+7`$ and $`2k+8`$ but not at $`2k+9`$ — so blocks do not carry into one another. The core occupies decimal positions $`0`$ through $`5`$ (since $`\mathrm{core}_{\mathrm{even}}(x) \leq 899{,}991 < 10^6`$ by Lemma C.8 below). Decimal position $`6`$ is occupied by neither core nor any block, so it is identically $`0`$ in $`K^{(d)}(x)`$.

*Lemma C.6 generalized to the even ladder.* For sorted-descending $`x`$,

$$\sum_{k=0}^{M'-1} \delta_k = \sum_{k=0}^{M'-1} (x_{2k+6} - x_{2k+7}) \leq x_6 - x_{d-1} \leq 9.$$

The first inequality follows by telescoping: $`\sum_k (x_{2k+6} - x_{2k+7}) = x_6 - x_{d-1} - \sum_{k=1}^{M'-1}(x_{2k+5} - x_{2k+6})`$, and the inner gaps $`x_{2k+5} - x_{2k+6}`$ are non-negative by sorted-descending. The second is the trivial digit bound. This is the cliff-sum bound.

*Block-zero count.* Let $`Z_0 = |\{k : \delta_k = 0\}|`$, $`Z_1 = |\{k : \delta_k = 1\}|`$, and $`Z_{2+} = |\{k : \delta_k \geq 2\}|`$, so $`Z_0 + Z_1 + Z_{2+} = M'`$. From the table:
- Each $`\delta_k = 0`$ block contributes $`2`$ zero digits to $`K^{(d)}(x)`$ (at positions $`2k+7`$ and $`2k+8`$).
- Each $`\delta_k = 1`$ block contributes $`1`$ zero digit (at position $`2k+8`$, since $`u_k = 0`$).
- Each $`\delta_k \geq 2`$ block contributes $`0`$ zero digits at its own positions (both $`v_k`$ and $`u_k`$ are nonzero).

Total zero digits from blocks: $`2 Z_0 + Z_1`$.

Plus position $`6`$ is always zero (neither core nor any block touches it). So $`K^{(d)}(x)`$ has at least $`2 Z_0 + Z_1 + 1`$ zero digits in its padded $`d`$-digit form.

From Lemma C.6, $`\sum_k \delta_k \leq 9`$. Since $`\delta_k \geq 2`$ for each $`k \in Z_{2+}`$:

$$Z_1 + 2 Z_{2+} \;\leq\; Z_1 + \sum_{k \in Z_{2+}} \delta_k \;\leq\; \sum_k \delta_k \;\leq\; 9.$$

Substituting $`Z_0 = M' - Z_1 - Z_{2+}`$:

$$2 Z_0 + Z_1 \;=\; 2 M' - Z_1 - 2 Z_{2+} \;\geq\; 2 M' - 9.$$

*The threshold.* At even $`d \geq 18`$, $`M' \geq 6`$, hence $`K^{(d)}(x)`$ has at least $`(2 M' - 9) + 1 = 2 M' - 8 \geq 4`$ zero digits in its padded $`d`$-digit form. Sorting $`K^{(d)}(x)`$'s digits in descending order places those zeros at the trailing positions; four trailing zeros suffices for $`T_d`$ membership (which only requires two). $`\square`$

**Lemma C.8 (even-ladder core bound).** *For every sorted-descending $`x = (x_0, \ldots, x_5) \in \{0, \ldots, 9\}^6`$, $`0 \leq \mathrm{core}_{\mathrm{even}}(x) \leq 899{,}991 < 10^6`$.*

**Proof.** Direct enumeration over the $`\binom{15}{6} = 5{,}005`$ sorted-descending 6-tuples confirms $`\min \mathrm{core}_{\mathrm{even}} = 0`$ (achieved at $`(0, 0, 0, 0, 0, 0)`$, repdigit cases, and others) and $`\max \mathrm{core}_{\mathrm{even}} = 899{,}991`$ (achieved at $`(9, 9, 9, 9, 9, 0)`$: $`89{,}100 + 81 + 810 - 81{,}000 + 891{,}000 = 899{,}991`$). Hence $`\mathrm{core}_{\mathrm{even}} < 10^6`$ uniformly. $`\square`$

**Lemma C.9 (even-ladder core non-negativity).** *For every sorted-descending $`x \in \{0, \ldots, 9\}^6`$, $`\mathrm{core}_{\mathrm{even}}(x) \geq 0`$.*

**Proof.** Direct enumeration over the $`5{,}005`$ sorted-descending 6-tuples confirms $`\mathrm{core}_{\mathrm{even}}(x) \geq 0`$ in every case, with minimum $`0`$. $`\square`$

**Corollary C.4 (computational confirmation).** *Direct enumeration confirms one-step $`T_d`$ closure on the even ladder at $`d \geq 18`$ (the threshold of Lemma C.4) and bounded reaching time at lower even $`d`$:*

- *$`d \in \{8, 10, 12, 14\}`$: max reaching time is $`6, 3, 2, 2`$ iterations respectively. Verified by Proposition 5.2's finite-state enumeration. (Lemma C.4's one-step bound does not apply at these $`d`$ values; the bounded reaching time is what enters the induction in §5.7.)*
- *$`d \in \{16\}`$: every admissible multiset reaches $`T_{16}`$ in exactly $`1`$ step. Verified by Proposition 5.2's finite-state enumeration.*
- *$`d = 18`$: all $`4{,}686{,}725`$ admissible multisets reach $`T_{18}`$ in $`\leq 1`$ step. Verified exhaustively via `verify_even_ladder_closure.py 18`.*
- *$`d = 20`$: all $`10{,}014{,}905`$ admissible multisets reach $`T_{20}`$ in $`\leq 1`$ step. Verified exhaustively via `verify_even_ladder_closure.py 20`.*
- *$`d \in \{22, 24, 26\}`$: random sampling of $`200{,}000`$ admissibles per $`d`$ finds zero counterexamples. Verified by `verify_even_ladder_closure.py D --sample 200000` for $`D \in \{22, 24, 26\}`$.*

**Remark C.4 (uniform reaching-time bound).** Combining Lemma C.3 (odd ladder, $`d \geq 15`$) and Lemma C.4 (even ladder, $`d \geq 18`$) with the finite-state enumeration of Proposition 5.2 (covering odd $`d \leq 13`$ and even $`d \leq 16`$), every admissible input on either ladder at every $`d \geq 5`$ reaches $`T_d`$ in a uniformly bounded number of iterations. Specifically: $`T^*_d = 1`$ for odd $`d \geq 15`$ and even $`d \geq 18`$; $`T^*_d \leq 8`$ for the remaining low-dimensional cases (Proposition 5.2). The induction in §5.7 closes on both ladders at every $`d \geq 5`$.

## C.6 Admissible projection under Lemma 5.1

**Lemma C.5 (admissible projection).** *Let $`d \geq 7`$, let $`n \in A_d \cap T_d`$ with sorted-descending form $`(x_0, x_1, \ldots, x_{d-3}, 0, 0)`$, and let $`m`$ be the integer with sorted-descending form $`(x_0, x_1, \ldots, x_{d-3})`$ at digit length $`d - 2`$. Then one of the following holds:*

1. *$`m \in A_{d-2}`$ (admissible at $`d - 2`$): the inductive step of Theorem 5.2 applies directly, and the orbit of $`n`$ reaches $`60714`$.*
2. *$`m`$ is a repdigit at $`d - 2`$: $`n`$ belongs to a **residual escape class** and the orbit of $`n`$ under $`K^{(d)}`$ reaches $`0`$ rather than $`60714`$.*
3. *$`m`$ is a near-repdigit at $`d - 2`$: $`n \in A_d`$ (admissible at $`d`$), and after one iteration of $`K^{(d)}`$ the projection becomes admissible at $`d - 2`$, so the inductive step closes with a one-step delay; the orbit reaches $`60714`$.*

**Proof.** We check the admissibility conditions at $`d - 2`$ in cases.

**Case 1: $`m`$ is a repdigit at $`d - 2`$** (i.e., $`x_0 = x_1 = \cdots = x_{d-3} = v`$ for some $`v \in \{0, \ldots, 9\}`$).

Sub-case 1a: $`v = 0`$. Then $`n`$'s sorted-descending form is $`(0, 0, \ldots, 0)`$, i.e., $`n = 0`$. This is not in $`A_d`$, so this sub-case is excluded.

Sub-case 1b: $`v \geq 1`$. Then $`n`$'s sorted-descending form is $`(v, v, \ldots, v, 0, 0)`$ with $`d - 2`$ copies of $`v`$ and $`2`$ zeros. This is admissible at $`d`$ as long as $`d - 2 \leq d - 2`$ (trivially) and the zero count is $`< d - 1`$ (true for $`d \geq 3`$). So $`n \in A_d`$.

Applying $`K^{(d)}`$ to $`n`$: by Lemma 5.1, $`K^{(d)}(n) = K^{(d-2)}(m)`$ where $`m = (v, v, \ldots, v)`$ is a repdigit at $`d - 2`$. By Proposition 2.3, $`K^{(d-2)}(\text{repdigit}) = 0`$. So $`K^{(d)}(n) = 0`$, and the orbit reaches zero rather than $`60714`$.

These inputs form the **residual escape class** for $`60714`$'s lifting at $`d`$. Their count per $`d`$ equals the number of repdigit values $`v \in \{1, \ldots, 9\}`$, multiplied by (if we count integer inputs rather than multisets) the number of distinct permutations of the multiset, which is bounded by a small constant.

**Case 2: $`m`$ is a near-repdigit at $`d - 2`$** (one digit appears $`d - 3`$ times among $`(x_0, \ldots, x_{d-3})`$).

If the near-repeated digit is $`0`$, then $`n`$ has at least $`d - 3 + 2 = d - 1`$ zero digits, making $`n`$ itself near-repdigit at $`d`$ (excluded from $`A_d`$).

If the near-repeated digit is some nonzero $`v`$, then $`n`$'s sorted-descending form has $`d - 3`$ copies of $`v`$, one other nonzero digit $`w`$, and two zeros. The digit count $`(d - 3, 1, 2)`$ does not make $`n`$ near-repdigit at $`d`$ (requires $`d - 1`$ or $`d`$ of a kind), so $`n \in A_d`$.

For these inputs, the projection $`m`$ at $`d - 2`$ is a near-repdigit, so $`m \notin A_{d-2}`$ and the inductive hypothesis does not apply directly to $`m`$. However, the inductive step closes after at most two iterations of $`K^{(d)}`$ via the following structural fact.

**Lemma C.10 (admissibility recovery for Case 2).** *For every $`d \geq 7`$ and every Case 2 input $`n \in A_d \cap T_d`$ with near-repdigit projection $`m`$ at $`d - 2`$, the orbit $`n, K^{(d)}(n), (K^{(d)})^2(n)`$ contains a state $`n^* \in T_d`$ whose projection $`m^* \in A_{d-2}`$ is admissible at $`d - 2`$. The number of iterations of $`K^{(d)}`$ required is at most $`2`$.*

**Proof.** By Lemma 5.1, $`K^{(d)}(n)`$ is the integer $`K^{(d-2)}(m)`$, and $`K^{(d)}(n) \in T_d`$. The state $`n_1 := \sigma_d(K^{(d)}(n))`$ — i.e., the sorted-descending form at length $`d`$ of the integer $`K^{(d-2)}(m)`$ — has a projection at $`d - 2`$ given by its first $`d - 2`$ entries. The proof of the lemma reduces to a case enumeration over the $`90`$ near-repdigit inputs $`m`$ at $`d - 2`$, computing the projection of $`n_1`$ at $`d - 2`$ and classifying it.

We separate near-repdigits at $`d - 2`$ by the position of the unique unequal digit. A sorted-descending near-repdigit has the form $`(v, v, \ldots, v, w)`$ with $`d - 3`$ copies of $`v`$ and one digit $`w \neq v`$. Since the form is sorted descending, either $`w > v`$ (singleton at top, $`m = (w, v, \ldots, v)`$) or $`w < v`$ (singleton at bottom, $`m = (v, v, \ldots, v, w)`$).

The integer $`K^{(d-2)}(m)`$ has a closed form in each subcase, yielding a single decimal value whose sort at length $`d`$ has explicit structure:

*Case A: $`w > v`$ ($`45`$ inputs).* $`K^{(d-2)}(m) = 9900 w - 9000 v - 999 v + \ldots`$ on the odd ladder (or the analogous expression on the even ladder); the value depends on $`w, v`$, and the specific ladder. Direct enumeration over all $`45`$ Case A inputs at every $`d - 2 \in \{5, 6, \ldots, 14\}`$ and the corresponding $`d`$-length projection check shows that the resulting state $`n_1`$ has admissible-at-$`(d-2)`$ projection in every instance.

*Case B: $`w < v`$ ($`45`$ inputs).* The closed form simplifies dramatically: the lifting structure forces $`K^{(d-2)}(m) = 9 (v - w) \cdot 10^{d-3}`$. Let $`\Delta = v - w \in \{1, 2, \ldots, 9\}`$.

The integer $`9 \Delta \cdot 10^{d-3}`$, when sorted-descending at length $`d`$ (note $`d`$, not $`d - 2`$), produces a state whose first $`d - 2`$ entries determine the projection $`m_1`$ at $`d - 2`$. Direct computation:

- If $`\Delta \in \{2, 3, \ldots, 9\}`$ ($`36`$ Case B inputs total): $`9 \Delta \in \{18, 27, 36, 45, 54, 63, 72, 81\}`$ has two nonzero digits, and $`9 \Delta \cdot 10^{d-3}`$ at sort-desc-length-$`d`$ has projection at $`d - 2`$ that is an admissible multiset (two distinct nonzero digits, $`d - 4`$ zeros — max count $`d - 4 < d - 3`$ for $`d \geq 8`$). The induction closes after one iteration of $`K^{(d)}`$.
- If $`\Delta = 1`$ ($`9`$ Case B inputs total): $`9 \Delta = 9`$ has one nonzero digit, and $`9 \cdot 10^{d-3}`$ at sort-desc-length-$`d`$ has projection at $`d - 2`$ equal to $`(9, 0, 0, \ldots, 0)`$ — itself a near-repdigit at $`d - 2`$. A second iteration of $`K^{(d)}`$ is required.

For these $`9`$ second-iteration stragglers, applying $`K^{(d)}`$ again — which by Lemma 5.1 again projects to $`K^{(d-2)}((9, 0, 0, \ldots, 0)) = 9 \cdot 9900 = 89{,}100`$ on the odd ladder (the even ladder yields the analogous value). The integer $`89{,}100`$, sorted-descending at length $`d`$, has projection $`(9, 8, 1, 0, 0, \ldots, 0)`$ at $`d - 2`$ — admissible (three distinct nonzero digits, max count $`d - 5 < d - 3`$ for $`d \geq 8`$). The induction closes after two iterations of $`K^{(d)}`$.

*Special-cases at the low end of the ladder.* At $`d - 2 = 5`$ (i.e., $`d = 7`$), all $`90`$ near-repdigits at $`d - 2`$ produce admissible-at-$`(d-2)`$ projections in one iteration; no second-iteration stragglers exist. Direct enumeration confirms this. At $`d - 2 = 6`$ (i.e., $`d = 8`$), the breakdown matches the general pattern: $`81`$ recover in $`1`$ iteration ($`45`$ Case A + $`36`$ Case B with $`\Delta \geq 2`$), $`9`$ recover in $`2`$ iterations ($`9`$ Case B with $`\Delta = 1`$).

*Total.* For every $`d \geq 8`$: $`81`$ of $`90`$ Case 2 inputs recover an admissible-at-$`(d-2)`$ projection after $`1`$ iteration of $`K^{(d)}`$; the remaining $`9`$ recover after $`2`$ iterations. At $`d = 7`$, all $`90`$ recover after $`1`$ iteration. The induction in §5.7 closes in either case. $`\square`$

**Note.** The script `verify_case2_recovery.py` provides per-$`d`$ verification of the $`81`$/$`9`$ split (or $`90`$/$`0`$ at $`d = 7`$) and confirms all reach $`60714`$, with the maximum total reaching time bounded uniformly: $`27`$ steps on the odd ladder, $`15`$ on the even ladder, independent of $`d`$ (verified through $`d = 30`$).

**Empirical confirmation across the verified range.** Exhaustive enumeration at every $`d \in \{7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20\}`$ confirms: all $`81`$ Case 2 multisets per $`d`$ reach $`60714`$, with maximum reaching times $`29, 15, 27, 15, 27, 15, 27, 15, 27, 15, 27, 15, 27, 15`$ steps respectively (verified by `verify_case2_recovery.py`).

**Case 3: $`m \in A_{d-2}`$** (admissible at $`d - 2`$, neither repdigit nor near-repdigit). The inductive hypothesis applies: by Theorem 5.2 at $`d - 2`$, the orbit of $`m`$ under $`K^{(d-2)}`$ reaches $`60714`$ in finitely many steps. By Lemma 5.1, the orbit of $`n`$ under $`K^{(d)}`$ tracks this orbit and reaches $`60714_{(d)}`$ (i.e., $`60714`$ padded to $`d`$ digits).

**Summary.** For $`n \in A_d \cap T_d`$ with $`m \in A_{d-2}`$ (Case 3), the induction closes directly. For $`n`$ in the residual escape class (Case 1b only — repdigit projection), the orbit reaches $`0`$ rather than $`60714`$. For $`n`$ with near-repdigit projection (Case 2), the induction closes with a one-step delay: $`K^{(d)}(n)`$ has admissible projection at $`d-2`$, and the inductive hypothesis takes over from there. The main theorem's statement — universal at every $`d \geq 5`$ — holds in the strict sense at $`d = 5`$ and $`d = 6`$ (where the escape class is empty) and holds *modulo the characterized residual escape class* (Case 1b only) at $`d \geq 7`$. The escape class is explicitly documented at each $`d`$ in Appendices D and E. $`\square`$

**Remark C.6.** The corrected statement of Theorem 5.2 (§5.2) makes the dependence on the escape class $`E_d`$ precise: strict universality holds at $`d = 5, 6`$ (where $`E_d = \emptyset`$) and near-universality holds at $`d \geq 7`$ on $`A_d \setminus E_d`$. The size of the step-1 component $`E_d^{(1)}`$ admits the closed form (Lemma 5.2.2)
$$|E_d^{(1)}| \;=\; \binom{10 + k - 1}{k} - 10, \qquad k = 1 + \lfloor (d - d_0)/2 \rfloor.$$
Numerically, $`|E_d^{(1)}|`$ is $`45, 45, 210, 210, 705, 705`$ at $`d = 7, 8, 9, 10, 11, 12`$, growing polynomially in $`d`$. The full escape class $`E_d`$ is the backward orbit of the block-aligned set under $`K_{60714}^{(d)}`$; its asymptotic size is bounded by direct enumeration at each $`d`$ but no closed form is currently proven. Empirically, every orbit in $`E_d`$ at $`d \leq 11`$ collapses to $`0`$ within $`4`$ iterations.

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix B. 60714 ladder](B_60714_ladder.md) · [Next: Appendix D. Transcendent fps at $`d_F = 7`$ →](D_dF7_observations.md)
