[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix D. Transcendent fps at $`d_F = 7`$](D_dF7_observations.md)

---

# Appendix E. Audit of $`6174`$ at $`d = 8, 9`$

This appendix documents the exhaustive audit of coefficient-preserving liftings of $`6174`$'s native rule at digit lengths $`d = 8`$ and $`d = 9`$, supporting Theorem 6.1 in §6.

## E.1 Setup

The native rule of $`6174`$ at $`d_F = 4`$ is the classical Kaprekar rule $`K_0`$: $`\pi = (3, 2, 1, 0)`$, $`\sigma = (0, 1, 2, 3)`$, coefficient vector $`c^{(4)} = (999, 90, -90, -999)`$. The sorted-descending form of $`6174`$ at $`d = 4`$ is $`(7, 6, 4, 1)`$ with no zero digits, so every native coefficient lands on a nonzero digit: $`\mathrm{sv}_F(K_0) = \mathrm{sv}(K_0) = 4`$.

When we pad $`6174`$ to $`d = 8`$, the sorted-descending form becomes $`(7, 6, 4, 1, 0, 0, 0, 0)`$. The four zero positions (indices $`4, 5, 6, 7`$) become the "absorbing" positions for coefficient-preserving lifting: new coefficients at these positions multiply zero digits and do not affect $`K(F) = F`$.

**Coefficient-preserving lifting at $`d = 8`$.** A rule $`K`$ at $`d = 8`$ with coefficient vector $`c = (c_0, c_1, c_2, c_3, c_4, c_5, c_6, c_7)`$ is a coefficient-preserving lifting of $`K_0`$ if $`c_i = c_i^{(4)}`$ for $`i \in \{0, 1, 2, 3\}`$ — that is, if the first four coefficients are exactly $`(999, 90, -90, -999)`$. By Proposition 5.1, any such rule satisfies $`K(6174_{(8)}) = 6174`$.

Given the native constraint $`c_i = c_i^{(4)}`$ at positions $`0, 1, 2, 3`$, the permutations $`\pi`$ and $`\sigma`$ are forced at those positions: $`\pi_0 = 3, \sigma_0 = 0`$, $`\pi_1 = 2, \sigma_1 = 1`$, $`\pi_2 = 1, \sigma_2 = 2`$, $`\pi_3 = 0, \sigma_3 = 3`$. The remaining positions $`4, 5, 6, 7`$ are freely assignable, subject to:

- $`(\pi_4, \pi_5, \pi_6, \pi_7)`$ is a permutation of $`\{4, 5, 6, 7\}`$: $`4! = 24`$ choices.
- $`(\sigma_4, \sigma_5, \sigma_6, \sigma_7)`$ is a permutation of $`\{4, 5, 6, 7\}`$: $`24`$ choices.
- $`\pi_i \neq \sigma_i`$ for $`i \in \{4, 5, 6, 7\}`$ (derangement at the tail): $`D_4 = 9`$ choices given $`\pi`$.

**Total liftings at $`d = 8`$:** $`24 \cdot 9 = 216`$.

**Analogous setup at $`d = 9`$.** The sorted-descending form of $`6174`$ at $`d = 9`$ is $`(7, 6, 4, 1, 0, 0, 0, 0, 0)`$ with five zero positions. Coefficient-preserving liftings preserve $`c^{(4)}`$ at positions $`0, 1, 2, 3`$ and freely assign $`\pi, \sigma`$ at positions $`4, 5, 6, 7, 8`$. Total count:

$$5! \cdot D_5 = 120 \cdot 44 = 5{,}280.$$

## E.2 Audit results

## E.2.1 At $`d = 8`$

Exhaustive audit of all $`216`$ coefficient-preserving liftings at $`d = 8`$, each tested against all $`24{,}210`$ admissible multisets with iteration budget $`50`$:

| Status | Count |
|:---|:---:|
| Strict-universal (basin $`= 1.0`$) | $`0`$ |
| Near-universal (basin $`\geq 0.99`$) | $`15`$ |
| Sub-near ($`0 \leq`$ basin $`< 0.99`$) | $`201`$ |
| Best basin | $`0.998141`$ |

Runtime: approximately $`150`$ seconds on commodity hardware.

**Best lifting (representative).** Among the two liftings achieving the maximum basin $`0.998141`$ (a sign-flip pair), one has permutations

$$\pi = (3, 2, 1, 0, 5, 7, 6, 4), \qquad \sigma = (0, 1, 2, 3, 6, 4, 5, 7),$$

with coefficient vector

$$c = (999,\; 90,\; -90,\; -999,\; -900{,}000,\; 9{,}990{,}000,\; 900{,}000,\; -9{,}990{,}000).$$

Verification: $`K(6174_{(8)}) = |999 \cdot 7 + 90 \cdot 6 - 90 \cdot 4 - 999 \cdot 1 + 0 + 0 + 0 + 0| = |6993 + 540 - 360 - 999| = 6174`$. $`\checkmark`$

## E.2.2 Escape characterization at $`d = 8`$

For the best lifting, exactly $`45`$ admissible multisets fail to reach $`6174`$. All $`45`$ have the form of **two four-of-a-kind groups**: sorted-descending $`(X, X, X, X, Y, Y, Y, Y)`$ for some pair $`X > Y \geq 0`$.

There are exactly $`\binom{10}{2} = 45`$ such digit pairs $`(X, Y)`$ with $`X > Y \geq 0`$, accounting for all $`45`$ escape multisets.

**Complete list of escape multisets at $`d = 8`$** (listed as sorted-descending tuples):

$`(1, 1, 1, 1, 0, 0, 0, 0), \; (2, 2, 2, 2, 0, 0, 0, 0), \; \ldots, \; (9, 9, 9, 9, 0, 0, 0, 0)`$ — the $`9`$ multisets with $`Y = 0`$.

$`(2, 2, 2, 2, 1, 1, 1, 1), \; (3, 3, 3, 3, 1, 1, 1, 1), \; \ldots, \; (9, 9, 9, 9, 1, 1, 1, 1)`$ — the $`8`$ multisets with $`Y = 1`$.

$`\vdots`$

$`(9, 9, 9, 9, 8, 8, 8, 8)`$ — the $`1`$ multiset with $`Y = 8`$.

**Total: $`9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45`$ multisets.**

**Why these escape.** Each escape multiset $`(X, X, X, X, Y, Y, Y, Y)`$ has only two distinct digit values, with exactly four copies of each. Applied to the best lifting:

$$K(X^4 Y^4) = |c_0 \cdot X + c_1 \cdot X + c_2 \cdot X + c_3 \cdot X + c_4 \cdot Y + c_5 \cdot Y + c_6 \cdot Y + c_7 \cdot Y|$$
$$= |(c_0 + c_1 + c_2 + c_3) \cdot X + (c_4 + c_5 + c_6 + c_7) \cdot Y|$$
$$= |(999 + 90 - 90 - 999) \cdot X + (-900{,}000 + 9{,}990{,}000 + 900{,}000 - 9{,}990{,}000) \cdot Y|$$
$$= |0 \cdot X + 0 \cdot Y| = 0.$$

The first four coefficients sum to $`0`$ (since $`K_0`$ has sum-zero structure), and the last four coefficients sum to $`0`$ (by the coefficient-preserving lifting construction). When the input has only two distinct values, the rule's action collapses algebraically to zero.

This is not a feature of the specific best lifting — it is a structural consequence of sum-zero constraints on coefficient-preserving liftings. Every coefficient-preserving lifting at $`d = 8`$ maps every four-of-a-kind-paired multiset to $`0`$.

## E.2.3 At $`d = 9`$

Exhaustive audit of all $`5{,}280`$ coefficient-preserving liftings at $`d = 9`$, each tested against all $`48{,}520`$ admissible multisets with iteration budget $`60`$:

| Status | Count |
|:---|:---:|
| Strict-universal (basin $`= 1.0`$) | $`0`$ |
| Near-universal (basin $`\geq 0.99`$) | $`302`$ |
| Best basin | $`0.999073`$ |

Runtime: approximately $`60`$ minutes on commodity hardware.

## E.2.4 Escape characterization at $`d = 9`$

For the best lifting at $`d = 9`$, the $`45`$ escape multisets have the same structural form as at $`d = 8`$, extended with trailing zeros. Specifically: sorted-descending $`(X, X, X, X, Y, Y, Y, Y, 0)`$ for $`X > Y \geq 0`$ (when $`Y \geq 1`$) or $`(X, X, X, X, 0, 0, 0, 0, 0)`$ (when $`Y = 0`$). There are again $`\binom{10}{2} = 45`$ such multisets.

**The escape count is independent of $`d`$.** The $`45`$-multiset structural form is preserved across $`d = 8, 9`$ and is expected to continue at $`d \geq 10`$: at higher $`d`$, the escape multisets are obtained by appending trailing zeros to the $`d = 8`$ escape forms.

## E.3 Asymptotic behavior

**Basin growth.** The escape count at $`d = 8, 9`$ is fixed at $`45`$. The admissible multiset count grows with $`d`$:

| $`d`$ | # admissible multisets | # escapes | basin (best) |
|:---:|:---:|:---:|:---:|
| $`8`$ | $`24{,}210`$ | $`45`$ | $`0.998141`$ |
| $`9`$ | $`48{,}520`$ | $`45`$ | $`0.999073`$ |
| $`10`$ | expected $`\sim 92{,}000`$ | expected $`45`$ | expected $`\sim 0.9995`$ |
| $`\cdots`$ | $`\cdots`$ | $`\cdots`$ | $`\cdots`$ |
| $`d \to \infty`$ | $`\to \infty`$ | $`45`$ | $`\to 1`$ |

**Asymptotic claim.** The best-lifting basin for $`6174`$ approaches $`1`$ as $`d \to \infty`$. Formally, if the $`45`$-escape structural form persists at all $`d \geq 8`$, then

$$\text{best basin at } d = 1 - \frac{45}{|A_d|} = 1 - O(10^{-d/9}).$$

The constant-count escape class means the ratio $`45 / |A_d|`$ decays as $`|A_d|`$ grows, which for admissible multisets at digit length $`d`$ grows combinatorially.

**Strict-universal at any $`d \geq 8`$?** Audit at $`d = 8, 9`$ finds $`0`$ strict-universal liftings. Whether any $`d \geq 10`$ admits a strict-universal coefficient-preserving lifting of $`6174`$ remains open. The structural argument of §E.2.2 suggests the answer is no: the four-of-a-kind-paired escape class is algebraically forced by sum-zero on the native and appended coefficients, and appears in every coefficient-preserving lifting.

## E.4 Conjectural extension

**Conjecture E.1.** *For every $`d \geq 8`$, the $`45`$-multiset escape class persists at $`6174`$'s coefficient-preserving liftings, and no coefficient-preserving lifting is strict-universal. The best basin asymptotes to $`1`$ monotonically.*

Resolving Conjecture E.1 requires a structural argument at general $`d`$ beyond the direct audit at $`d = 8, 9`$. The algebraic proof of the $`45`$-multiset escape class's persistence (that it is forced by sum-zero constraints regardless of which coefficient-preserving lifting is chosen) is outlined in §E.2.2 and could likely be extended to all $`d`$, but we do not pursue this here.

---

*End of Appendix E.*

---

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix D. Transcendent fps at $`d_F = 7`$](D_dF7_observations.md)
