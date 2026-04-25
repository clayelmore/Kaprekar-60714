[← Back to paper](../README.md#table-of-contents) · [← Previous: 1. Introduction](01_introduction.md) · [Next: 3. Classifications at $`d \leq 6`$ →](03_classifications.md)

---

# 2. Framework

This section establishes the formal objects, notation, and basic properties used throughout the paper. Everything here is definitional and verifiable; no substantive claims are made in this section.

## 2.1 Sorted-descending digit sequences

Throughout, $`d \geq 2`$ is a fixed digit length (the digit length will vary between sections but is fixed within each statement). For a non-negative integer $`n < 10^d`$, the **padded digit string** of $`n`$ at length $`d`$ is the sequence $`(n_{d-1}, n_{d-2}, \ldots, n_1, n_0)`$ where $`n_j`$ is the digit at place $`10^j`$, padding with leading zeros as needed. Thus $`n = \sum_{j = 0}^{d-1} 10^j \, n_j`$.

The **sorted-descending form** of $`n`$ at length $`d`$ is the tuple $`x(n) = (x_0, x_1, \ldots, x_{d-1})`$ obtained by sorting the padded digit string in non-increasing order, so $`x_0 \geq x_1 \geq \cdots \geq x_{d-1}`$. For example, at $`d = 5`$ with $`n = 12345`$, the padded digit string is $`(1, 2, 3, 4, 5)`$ and the sorted-descending form is $`(5, 4, 3, 2, 1)`$.

An integer $`n`$ is a **repdigit** at length $`d`$ if all digits of its padded form are equal, i.e., $`x_0 = x_{d-1}`$. An integer is a **near-repdigit** at length $`d`$ if its sorted-descending form has one digit appearing $`d - 1`$ or $`d`$ times (the $`d`$-case coincides with repdigit). All classical Kaprekar analyses exclude repdigits; our convention additionally excludes near-repdigits. This follows standard usage in the literature [Prichett 1981, Dahl 2026] and is necessary in our setting because near-repdigits can produce degenerate trajectories under coefficient-preserving liftings, discussed at §5.6. The **admissible input set** at length $`d`$, denoted $`A_d`$, is the set of non-repdigit, non-near-repdigit $`d`$-digit integers.

## 2.2 Permutation-pair rules

Let $`S_d`$ be the symmetric group on $`\{0, 1, \ldots, d-1\}`$. Given an ordered pair $`(\pi, \sigma) \in S_d \times S_d`$ with $`\pi \neq \sigma`$, define the **permutation-pair rule** $`K_{\pi, \sigma}: \mathbb{Z}_{\geq 0} \to \mathbb{Z}_{\geq 0}`$ by

$$K_{\pi, \sigma}(n) = \left| \pi \cdot x(n) - \sigma \cdot x(n) \right|,$$

where, for any permutation $`\tau \in S_d`$ and tuple $`x = (x_0, \ldots, x_{d-1})`$,

$$\tau \cdot x \;=\; \sum_{i = 0}^{d-1} 10^{\tau_i} \, x_i.$$

Thus $`\tau \cdot x`$ is the integer obtained by placing the sorted-descending digit $`x_i`$ at the $`10^{\tau_i}`$ place.

**The classical rule.** The classical Kaprekar rule $`K_0`$ at digit length $`d`$ corresponds to $`\pi = (d-1, d-2, \ldots, 1, 0)`$ (descending) and $`\sigma = (0, 1, \ldots, d-2, d-1)`$ (ascending). At $`d = 4`$, $`K_0(n) = \alpha(n) - \beta(n)`$ with $`\alpha(n) = \pi \cdot x(n) = \sum_i 10^{d-1-i} x_i`$ arranging sorted-descending digits in their own order, and $`\beta(n) = \sigma \cdot x(n) = \sum_i 10^i x_i`$ arranging them in reverse.

**Coefficient expansion.** Let $`r(i) = \tau^{-1}(i)`$ denote the preimage of place $`i`$ under a permutation $`\tau`$ — that is, the sorted-descending position that contributes to the $`10^i`$ place of $`\tau \cdot x`$. Then

$$\tau \cdot x \;=\; \sum_{i = 0}^{d-1} 10^i \, x_{\tau^{-1}(i)}.$$

Equivalently,

$$K_{\pi, \sigma}(n) \;=\; \left| \sum_{i = 0}^{d-1} c_i \, x_i \right|,$$

where the **coefficient vector** $`c = (c_0, \ldots, c_{d-1})`$ is given by

$$c_i \;=\; 10^{\pi_i} - 10^{\sigma_i}.$$

**Sum-zero constraint.** Since $`\{\pi_i\}_{i=0}^{d-1}`$ and $`\{\sigma_i\}_{i=0}^{d-1}`$ are each permutations of $`\{0, 1, \ldots, d-1\}`$, we have $`\sum_i 10^{\pi_i} = \sum_i 10^{\sigma_i} = \frac{10^d - 1}{9}`$. Therefore $`\sum_i c_i = 0`$ identically. This will be important in §5.

**Three equivalent representations.** Throughout the paper we freely switch between three representations of a permutation-pair rule, and it is useful to see them side by side. We use the classical rule at $`d = 4`$ as the running example.

Assign letters $`a, b, c, d`$ to the sorted-descending positions: $`a = x_0`$ (the largest digit), $`b = x_1`$, $`c = x_2`$, $`d = x_3`$ (the smallest). A string of letters then denotes an integer: reading left-to-right from the highest place to the lowest, each letter specifies which sorted-descending position contributes that digit.

For the classical Kaprekar rule at $`d = 4`$, the three representations are:

(i) **Letter string:** $`\;K_0(n) = \mathrm{abcd} - \mathrm{dcba}`$.

(ii) **Permutation pair:** $`\;\pi = (3, 2, 1, 0)`$ and $`\sigma = (0, 1, 2, 3)`$.

(iii) **Coefficient vector:** $`\;c = (c_0, c_1, c_2, c_3) = (999, \, 90, \, -90, \, -999)`$.

**Worked example.** Take $`n = 6174`$. Its sorted-descending form is $`x(n) = (x_0, x_1, x_2, x_3) = (7, 6, 4, 1)`$. Using the letter-string form, $`\pi \cdot x = \mathrm{abcd} = 7641`$ and $`\sigma \cdot x = \mathrm{dcba} = 1467`$, so $`K_0(6174) = |7641 - 1467| = 6174`$. Using the coefficient-vector form, $`K_0(6174) = 999 \cdot 7 + 90 \cdot 6 - 90 \cdot 4 - 999 \cdot 1 = 6993 + 540 - 360 - 999 = 6174`$. Both computations give the same answer, and both confirm that $`6174`$ is a fixed point of $`K_0`$ at $`d = 4`$.

The three representations encode the same information. The letter string is the most legible: reading $`\mathrm{abcd} - \mathrm{dcba}`$ makes immediately clear that the rule is "digits in descending order minus digits in ascending order," Kaprekar's original statement. The permutation pair $`(\pi, \sigma)`$ is the formal definition used in proofs. The coefficient vector $`c = (c_0, \ldots, c_{d-1})`$ with $`c_i = 10^{\pi_i} - 10^{\sigma_i}`$ is the most useful for algebraic manipulation, because it reduces the rule to a linear expression in the sorted-descending digits.

For rules arising in §5 and §6 (the $`60714`$ lifting family and the $`6174`$ cross-dimensional pattern), we will use whichever representation is most convenient for the context, and Appendix B provides a complete table of all three for $`60714`$'s ladder at each $`d \in \{5, 6, \ldots, 20\}`$.

## 2.3 Algebraic rank

The **algebraic rank** (or **surviving-variable count**) of a rule $`K_{\pi, \sigma}`$ is

$$\mathrm{sv}(K_{\pi, \sigma}) \;=\; \bigl|\{\,i : c_i \neq 0\,\}\bigr| \;=\; \bigl|\{\,i : \pi_i \neq \sigma_i\,\}\bigr|.$$

The rule is **full-variable** at digit length $`d`$ if $`\mathrm{sv} = d`$ — equivalently, if the map $`i \mapsto (\pi_i, \sigma_i)`$ has $`\pi_i \neq \sigma_i`$ for every $`i`$.

**Proposition 2.1 (derangement characterization of full-variable).** *A rule $`K_{\pi, \sigma}`$ at digit length $`d`$ is full-variable if and only if $`\sigma \circ \pi^{-1}`$ is a derangement of $`\{0, 1, \ldots, d-1\}`$.*

**Proof.** $`\mathrm{sv} = d`$ means $`\pi_i \neq \sigma_i`$ for all $`i`$. Equivalently, setting $`j = \pi_i`$ and $`\rho = \sigma \circ \pi^{-1}`$, this says $`\rho(j) \neq j`$ for all $`j`$ — precisely that $`\rho`$ is a derangement. $`\square`$

**Rule counts by rank.** The total number of ordered pairs $`(\pi, \sigma)`$ with $`\pi \neq \sigma`$ is $`d! \, (d! - 1)`$. The number of full-variable rules is $`d! \, D_d`$, where $`D_d`$ is the number of derangements of $`d`$ elements. For small $`d`$:

| $`d`$ | $`d! \, (d! - 1)`$ (all rules) | $`d! \, D_d`$ (full-variable) |
|:---:|:---:|:---:|
| 2 | 2      | 2      |
| 3 | 30     | 12     |
| 4 | 552    | 216    |
| 5 | 14{,}280  | 5{,}280   |
| 6 | 517{,}680 | 190{,}800 |

## 2.4 Universality and fixed points

A **fixed point** of $`K_{\pi, \sigma}`$ at length $`d`$ is an integer $`F \in A_d`$ with $`K_{\pi, \sigma}(F) = F`$. A fixed point $`F`$ is **universal** for $`K_{\pi, \sigma}`$ at length $`d`$ if, for every admissible input $`n \in A_d`$, the orbit $`n, K(n), K^2(n), \ldots`$ reaches $`F`$ in finitely many steps. A rule is **universal for $`F`$ at $`d`$** if it satisfies both conditions.

**Example (classical).** The classical rule $`K_0`$ at $`d = 4`$ is universal for $`F = 6174`$ [Kaprekar 1955]. It reaches $`6174`$ within at most seven iterations for every admissible input.

**Example (dimension-agnostic).** At $`d = 3`$, the classical rule $`K_0`$ has coefficient vector $`(99, \, 0, \, -99)`$ — the middle coefficient vanishes by the forced borrow chain of §1.1 — so $`\mathrm{sv}(K_0) = 2`$. The classical rule at $`d = 3`$ is *not* full-variable. It is universal for $`F = 495`$, but $`495`$ is a fixed point of a rank-$`2`$ rule, not a rank-$`3`$ rule.

## 2.5 Native digit length

For an integer $`F`$, its **native digit length** $`d_F`$ is the smallest $`d`$ such that $`F`$ is a universal full-variable fixed point of some rule at digit length $`d`$. If $`F`$ admits no universal full-variable rule at any $`d`$, it has no native digit length in our sense.

**Example.** At $`d = 4`$, the set of fixed points with native digit length $`4`$ is $`\{1746, 2538, 5382, 6174\}`$ (see §3). Each is a universal full-variable fixed point at $`d = 4`$ under some rule; for $`6174`$, the rule is classical, but the other three arise from non-classical permutation pairs.

**Dimension-agnostic fixed points.** Integers such as $`45`$ (universal at every $`d \geq 2`$ under low-rank rules derived from classical reverse-pair structure), $`495`$ (universal at $`d = 3`$ under $`K_0`$), and $`450`$ (universal at $`d = 3`$ under a cousin of the classical rule) are *not* in our full-variable classification because their rules have $`\mathrm{sv} < d`$ at every $`d`$ where they appear. These integers are fixed points of *rank-reducing* rules, where forced borrow chains or structural cancellations reduce the effective input count below $`d`$. They persist across digit lengths through this dimensional reduction.

Our full-variable classification excludes these by design: we study only rules with $`\mathrm{sv} = d`$, where every sorted-descending position contributes nontrivially. The dimension-agnostic family deserves independent study, but is outside the scope of this paper. See §1.1 for the structural derivation of the middle-digit cancellation that produces $`495`$'s rank-$`2`$ status.

## 2.6 Effective rank at a fixed point

For a fixed point $`F`$ with sorted-descending form $`(f_0, f_1, \ldots, f_{d-1})`$ at length $`d`$, and for a rule $`K_{\pi, \sigma}`$ with coefficient vector $`c`$, the **effective rank at $`F`$** is

$$\mathrm{sv}_F(K_{\pi, \sigma}) \;=\; \bigl|\{\,i : c_i \neq 0 \text{ and } f_i \neq 0\,\}\bigr|.$$

Thus $`\mathrm{sv}_F`$ counts coefficients of the rule that *land on nonzero digits of $`F`$*. If $`F`$ has $`z`$ zero digits in its sorted-descending form, then $`\mathrm{sv}_F \leq d - z`$ for any rule.

Effective rank plays a structural role in §4 and §5. Coefficients paired with zero digits of $`F`$ vanish in the computation of $`K(F)`$, so the fixed-point equation $`K(F) = F`$ is determined only by the coefficients paired with nonzero digits. This is why coefficient-preserving lifting (defined in §5) can introduce large new coefficients at positions corresponding to $`F`$'s zero digits without disturbing $`F`$'s fixed-point status.

## 2.7 Basic properties

We collect two basic properties used without comment throughout the rest of the paper.

**Proposition 2.2 (sign-flip symmetry).** *If $`K_{\pi, \sigma}`$ is universal for $`F`$ at length $`d`$, so is $`K_{\sigma, \pi}`$, with the same basin. The coefficient vector of $`K_{\sigma, \pi}`$ is the negation of that of $`K_{\pi, \sigma}`$.*

**Proof.** The rule is $`K_{\pi, \sigma}(n) = |\pi \cdot x(n) - \sigma \cdot x(n)|`$. Swapping $`\pi`$ and $`\sigma`$ negates the argument of the absolute value, which leaves the rule invariant. $`\square`$

In consequence, universal rules come in sign-flipped pairs. Throughout the paper, when we report "the number of universal full-variable rules for $`F`$," we count ordered pairs unless explicitly noted; the number of geometrically distinct rules is half of this.

**Proposition 2.3 (repdigit invariance).** *For any rule $`K_{\pi, \sigma}`$ and any repdigit input $`r`$ (e.g., $`11111`$ at $`d = 5`$), $`K_{\pi, \sigma}(r) = 0`$. Moreover, $`K_{\pi, \sigma}(0) = 0`$. Thus $`0`$ is a fixed point of every rule.*

**Proof.** If all digits of $`r`$ are equal to some value $`v`$, then $`\pi \cdot x(r) = v \cdot \sum_i 10^{\pi_i} = v \cdot (10^d - 1)/9`$, and $`\sigma \cdot x(r)`$ has the same value. Their difference is zero. $`\square`$

Proposition 2.3 is why we exclude repdigits from the admissible input set: they provide no nontrivial dynamics and add a trivial fixed point $`0`$ to every rule's fixed-point set. Near-repdigits, excluded for similar reasons, can also produce trajectories that collapse to $`0`$ under coefficient-preserving liftings. The standard convention in Kaprekar analysis is to restrict attention to "generic" inputs with at least two distinct digit values, and we follow this.

## 2.8 Summary of notation

For reference:

| Symbol | Meaning |
|:---|:---|
| $`d`$ | digit length |
| $`n`$ | a $`d`$-digit integer (possibly with leading zeros) |
| $`x(n) = (x_0, \ldots, x_{d-1})`$ | sorted-descending form of $`n`$, with $`x_0 \geq x_1 \geq \cdots`$ |
| $`A_d`$ | admissible inputs at length $`d`$ (non-repdigit, non-near-repdigit) |
| $`\pi, \sigma`$ | permutations in $`S_d`$ |
| $`K_{\pi, \sigma}`$ | permutation-pair rule |
| $`K_0`$ | classical rule (descending minus ascending) |
| $`c_i = 10^{\pi_i} - 10^{\sigma_i}`$ | coefficient at sorted-descending position $`i`$ |
| $`\mathrm{sv}(K)`$ | algebraic rank (number of nonzero coefficients) |
| $`\mathrm{sv}_F(K)`$ | effective rank at $`F`$ (nonzero coefficients paired with nonzero digits of $`F`$) |
| $`F`$ | a fixed point |
| $`d_F`$ | native digit length of $`F`$ |
| $`(f_0, \ldots, f_{d-1})`$ | sorted-descending form of $`F`$ at length $`d`$ |

---

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: 1. Introduction](01_introduction.md) · [Next: 3. Classifications at $`d \leq 6`$ →](03_classifications.md)
