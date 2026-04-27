[← Back to paper](../README.md#table-of-contents) · [← Previous: 2. Framework](02_framework.md) · [Next: 4. Cross-check $`d = 5 \to d = 6`$ →](04_cross_check.md)

---

# 3. Classification of Universal Full-Variable Fixed Points at $`d \leq 6`$

This section presents the complete classification of universal full-variable fixed points at digit lengths $`d = 3, 4, 5, 6`$. The classification at each $`d`$ is obtained by exhaustive enumeration: every full-variable rule is tested against every admissible input, and the universal rules are identified. The counts are definitive; the full list of fixed points at $`d = 6`$ appears in Appendix A.

## 3.1 Method

At each digit length $`d`$, we enumerate the full-variable rules — ordered pairs $`(\pi, \sigma) \in S_d \times S_d`$ with $`\pi_i \neq \sigma_i`$ for every $`i`$ (Proposition 2.1) — and for each such rule we check:

1. Does the rule have at least one fixed point $`F \in A_d`$?
2. For each fixed point $`F`$, is the rule universal for $`F`$? That is, does every input $`n \in A_d`$ reach $`F`$ under iteration?

A rule is **universal at $`d`$** if both conditions hold. The set of **universal full-variable fixed points at $`d`$** is the set of integers $`F`$ arising as the attractor of some universal full-variable rule.

The enumerations are complete. At $`d = 6`$, the largest case we present, $`190{,}800`$ full-variable rules are tested against $`4{,}905`$ admissible digit multisets ($`999{,}450`$ admissible padded six-digit strings), a search that runs in hours on commodity hardware with the iteration-and-caching implementation described in Appendix A.

## 3.2 $`d = 3`$: no universal full-variable fixed points

At $`d = 3`$, there are $`12`$ full-variable rules (Proposition 2.1, $`3! \cdot D_3 = 6 \cdot 2 = 12`$).

**Theorem 3.1.** *No full-variable rule at $`d = 3`$ is universal for any fixed point.*

**Proof sketch.** Direct enumeration. For each of the $`12`$ rules, the iteration from any admissible $`d = 3`$ input enters a cycle of length $`\geq 2`$ or a non-universal fixed point. No rule admits a fixed point with basin covering all of $`A_3`$. Full computation in Appendix A.1.

**Remark on $`495`$.** The classical attractor $`495`$ does not appear here because the classical rule $`K_0`$ at $`d = 3`$ is not full-variable: its middle coefficient vanishes by the forced borrow chain (§1.1), giving $`\mathrm{sv}(K_0) = 2`$. $`495`$ is a fixed point of a rank-$`2`$ rule, outside the scope of Theorem 3.1. It reappears in Appendix §2.5 as a dimension-agnostic fixed point.

## 3.3 $`d = 4`$: four universal full-variable fixed points

At $`d = 4`$, there are $`216`$ full-variable rules (Proposition 2.1, $`4! \cdot D_4 = 24 \cdot 9 = 216`$).

**Theorem 3.2.** *There are exactly four universal full-variable fixed points at $`d = 4`$:*

$$F_4 = \{\, 1746,\; 2538,\; 5382,\; 6174 \,\}.$$

*These fixed points are reached by exactly $`8`$ universal full-variable rules in total (each fixed point reached by exactly $`2`$ universal rules, which are sign-flips of each other per Proposition 2.2).*

**Proof.** Exhaustive enumeration of $`216`$ rules against $`615`$ admissible digit multisets ($`9{,}630`$ admissible padded four-digit strings). For each universal rule, basin coverage of $`A_4`$ is verified directly. Full computation in Appendix A.2.

**Structure of the classification.** All four universal fixed points share the digit-sum property $`\sum_i f_i \equiv 0 \pmod 9`$. The integers $`6174`$ and $`1746`$ are digit-permutations of each other (both have multiset $`\{1, 4, 6, 7\}`$); $`2538`$ and $`5382`$ are digit-permutations of each other (multiset $`\{2, 3, 5, 8\}`$). These anagram clusters will recur in §3.4 and §6.

**Observation 3.1.** *The sum of the two fixed points in each anagram cluster is $`7920`$:*

$$6174 + 1746 = 7920, \qquad 2538 + 5382 = 7920.$$

This identity is a specific instance of reverse-pair structure at $`d = 4`$: if $`F`$ has digits summing to $`18`$, then $`F + \mathrm{reverse}(F)`$ takes a predictable form. We do not develop this further here; see [Nuez 2021] for parametric analysis of this phenomenon.

**Connection to the classical rule.** $`K_0`$ at $`d = 4`$ is full-variable (coefficient vector $`(999, 90, -90, -999)`$), and $`K_0`$ is one of the $`2`$ universal rules for $`6174`$. The classical Kaprekar theorem is thus recovered within our classification as a specific entry in Theorem 3.2.

## 3.4 $`d = 5`$: thirty-three universal full-variable fixed points

At $`d = 5`$, there are $`5{,}280`$ full-variable rules (Proposition 2.1, $`5! \cdot D_5 = 120 \cdot 44 = 5{,}280`$).

**Theorem 3.3.** *There are exactly $`33`$ universal full-variable fixed points at $`d = 5`$, reached collectively by $`66`$ universal full-variable rules. Each fixed point is reached by exactly $`2`$ universal rules (sign-flip pairs).*

**Proof.** Exhaustive enumeration of $`5{,}280`$ rules against $`1{,}902`$ admissible digit multisets ($`99{,}540`$ admissible padded five-digit strings). Full computation in Appendix A.3; the complete list of $`33`$ fixed points appears in Table 3.1 below.

**Classical rule does not appear.** The classical rule $`K_0`$ at $`d = 5`$ has coefficient vector $`(9999, \, 990, \, 0, \, -990, \, -9999)`$ — the middle coefficient vanishes by the forced borrow chain at odd digit length (§1.1). $`K_0`$ at $`d = 5`$ has $`\mathrm{sv} = 4`$, not $`5`$; it is not in the full-variable classification. The observation that "the classical Kaprekar routine fails at $`d = 5`$" is, in our framing, the observation that the classical rule at $`d = 5`$ is not even in the full-variable space — there is no contradiction to the existence of $`33`$ universal attractors in that space.

**Reverse-pair structure fails at odd $`d`$.** The classical rule is a specific "reverse-pair" rule ($`\sigma_i = \pi_{d-1-i}`$). At even $`d`$, reverse-pair rules can be full-variable; at odd $`d`$, they cannot — the middle position always satisfies $`\sigma_{(d-1)/2} = \pi_{(d-1)/2}`$, forcing $`\mathrm{sv} \leq d - 1`$. Consequently, all $`66`$ universal full-variable rules at $`d = 5`$ are *non-reverse-pair* — they have no mirror symmetry. This is a structural distinction from the classical case.

**Table 3.1.** *The $`33`$ universal full-variable fixed points at $`d = 5`$, grouped by digit multiset.*

| Multiset | Fixed points | Cluster size |
|:---|:---|:---:|
| $`\{0, 0, 0, 4, 5\}`$       | $`54`$                             | $`1`$ |
| $`\{0, 3, 3, 5, 7\}`$       | $`3753`$                           | $`1`$ |
| $`\{0, 1, 4, 6, 7\}`$       | $`60714`$, $`60417`$                 | $`2`$ |
| $`\{1, 2, 3, 4, 8\}`$       | $`18342`$, $`21834`$, $`24183`$, $`41832`$, $`42183`$ | $`5`$ |
| $`\{2, 3, 5, 8, 9\}`$       | $`28539`$, $`53928`$, $`58239`$         | $`3`$ |
| $`\{1, 5, 6, 7, 8\}`$       | $`16578`$, $`16758`$, $`17685`$, $`65781`$, $`67581`$ | $`5`$ |
| $`\{3, 4, 5, 7, 8\}`$       | $`37584`$, $`37854`$, $`38754`$, $`43758`$, $`43785`$, $`43875`$ | $`6`$ |
| $`\{1, 2, 4, 5, 6\}`$       | $`12456`$, $`14562`$, $`15642`$, $`16524`$, $`21456`$, $`24156`$, $`24561`$, $`41562`$, $`45612`$, $`45621`$ | $`10`$ |

*Total: $`33`$ fixed points across $`8`$ multiset clusters. Each fixed point is universal for exactly $`2`$ rules (sign-flip pair), giving $`66`$ universal rules total.*

**Observation 3.2.** *The $`\{0, 1, 4, 6, 7\}`$ multiset produces exactly two universal fixed points at $`d = 5`$: $`60714`$ and $`60417`$. These are the multiset twins featured in §6. Despite identical digit content, their native rules differ in a specific structural invariant (developed in §6) that predicts their contrasting cross-dimensional behavior.*

**Observation 3.3.** *The classical fixed points $`6174`$, $`1746`$, $`2538`$, $`5382`$ (from $`d = 4`$) do not appear at $`d = 5`$ even as fixed points of any full-variable rule — not merely as non-universal fixed points, but as non-fixed points. Exhaustive enumeration confirms: for each of these four integers padded to five digits, no full-variable rule at $`d = 5`$ satisfies $`K(F_{\text{padded}}) = F`$.*

**Observation 3.4 (effective rank within the full-variable classification).** *Two of the $`33`$ fixed points in Table 3.1 — namely $`54`$ and $`3753`$ — have effective rank at $`F`$ strictly less than their native algebraic rank:*

- *$`54`$ has sorted-descending form $`(5, 4, 0, 0, 0)`$ at $`d = 5`$; three of the five digits are zero. Its native sv$`=5`$ rule is $`\pi = (1, 2, 4, 3, 0), \sigma = (2, 0, 3, 4, 1)`$ with coefficient vector $`(-90, 99, 9000, -9000, -9)`$. Three of these five coefficients are paired with zero digits in the fixed-point equation, giving $`\mathrm{sv}_F(K_{54}) = 2 < 5 = \mathrm{sv}(K_{54})`$.*

- *$`3753`$ has sorted-descending form $`(7, 5, 3, 3, 0)`$ at $`d = 5`$; one digit is zero. Its native rule has $`\mathrm{sv}_F = 4 < 5`$.*

*These fixed points are genuinely in the full-variable classification — their native rules are algebraically rank-$`5`$ — but their effective rank at $`F`$ is reduced by absorption of coefficients at zero-digit positions. This is the mechanism that underlies coefficient-preserving lifting in §5, visible here at the root of the classification: a rule can be algebraically full-variable while being effectively lower-rank on a specific fixed point. The remaining $`31`$ fps in Table 3.1 all have no zero digits and therefore have $`\mathrm{sv}_F = \mathrm{sv} = 5`$.*

## 3.5 $`d = 6`$: five hundred and six universal full-variable fixed points

At $`d = 6`$, there are $`190{,}800`$ full-variable rules (Proposition 2.1, $`6! \cdot D_6 = 720 \cdot 265`$).

**Theorem 3.4.** *There are exactly $`506`$ universal full-variable fixed points at $`d = 6`$, reached collectively by $`1{,}174`$ universal full-variable rules.*

**Proof.** Exhaustive enumeration of $`190{,}800`$ full-variable rules against $`4{,}905`$ admissible digit multisets ($`999{,}450`$ admissible padded six-digit strings). Full enumeration data and the complete list of $`506`$ fixed points are in Appendix A.4.

**Remark on enumeration soundness.** The reproducibility script `classify_at_d.py` uses a candidate-filtering heuristic followed by full-basin verification of each candidate, which scales tractably to $`d = 6`$ but is not by itself a sound enumeration (a candidate fp could in principle be missed by the filter). The $`506`$ count was independently cross-verified against three sources that all agree: (i) a 3-day exhaustive enumeration on consumer hardware producing `results_db.json`, (ii) a no-shortcut sound enumeration on the verifier container, and (iii) the supplementary file `d6_fps.txt`, whose stratification by zero-digit count $`(205 + 240 + 53 + 8 = 506)`$ matches the table below. The three sources independently arrive at the same fixed-point set and the same count.

**Stratification by zero digit count.** The $`506`$ fixed points distribute as follows by the number of zero digits in each fixed point:

| Zero-digit count | Fixed-point count |
|:---:|:---:|
| $`0`$ | $`205`$ |
| $`1`$ | $`240`$ |
| $`2`$ | $`53`$  |
| $`3`$ | $`8`$   |
| **Total** | **$`506`$** |

This stratification matters for §5 and §6: fixed points with more zero digits admit more coefficient-preserving liftings to higher $`d`$, a phenomenon visible already at the $`d = 5 \to d = 6`$ boundary and developed in detail at §6.

**Note on the high-zero-count strata.** The $`8`$ fps with $`3`$ zero digits at $`d = 6`$ all share digit multiset $`\{0, 0, 0, 2, 2, 5\}`$: they are $`\{252, 2520, 20025, 25200, 200025, 200250, 250200, 252000\}`$. There are no universal full-variable fps at $`d = 6`$ with $`4`$ or more zero digits — the trivial fixed point $`F = 0`$ is excluded throughout this paper by the convention of §2 (Proposition 2.3). In particular, the fixed point $`549{,}945`$ has digit multiset $`\{4, 4, 5, 5, 9, 9\}`$ with no zero digits and does not appear in this stratification.

**Connection to classical Kaprekar at $`d = 6`$.** The classical rule $`K_0`$ at $`d = 6`$ has coefficient vector $`(999{,}999, \, 89{,}991, \, 8{,}991, \, -8{,}991, \, -89{,}991, \, -999{,}999)`$ after simplification. It is full-variable at $`d = 6`$ (all coefficients nonzero). [Dahl 2026] analyzes its basin: the rule is *not* universal at $`d = 6`$ — it produces a 7-cycle that attracts $`93.55\%`$ of inputs, with $`6.25\%`$ reaching $`F = 631{,}764`$ and $`0.20\%`$ reaching $`F = 549{,}945`$. The universal fixed points at $`d = 6`$ in our classification are attractors of *other* full-variable rules, not the classical one.

**Observation 3.4.** *The digit sum of every universal full-variable fixed point at $`d = 6`$ is divisible by $`9`$. The distribution of digit sums is strikingly bell-shaped about $`27`$ (the midpoint of the admissible range $`\{9, 18, 27, 36, 45\}`$):*

| Digit sum | Fixed-point count |
|:---:|:---:|
| $`9`$   | $`8`$   |
| $`18`$  | $`156`$ |
| $`27`$  | $`244`$ |
| $`36`$  | $`96`$  |
| $`45`$  | $`2`$   |
| **Total** | **$`506`$** |

This pattern reflects a general arithmetic fact about universal Kaprekar-type attractors: $`K(n) \equiv 0 \pmod 9`$ whenever $`n \in A_d`$, so fixed points satisfy $`F \equiv 0 \pmod 9`$. The bell-shape reflects the combinatorics of digit-multisets satisfying this modular constraint.

## 3.6 Summary

The classifications at $`d = 3, 4, 5, 6`$ are:

| $`d`$ | Full-variable rules | Universal fps | Universal rules |
|:---:|:---:|:---:|:---:|
| $`3`$ | $`12`$       | $`0`$   | $`0`$   |
| $`4`$ | $`216`$      | $`4`$   | $`8`$   |
| $`5`$ | $`5{,}280`$     | $`33`$  | $`66`$  |
| $`6`$ | $`190{,}800`$   | $`506`$ | $`1{,}174`$ |

Each classification is complete and reproducible; full enumeration scripts and data are in Appendix A.

**Why the count grows so quickly.** The growth in universal fixed-point count from $`0`$ at $`d = 3`$ to $`506`$ at $`d = 6`$ reflects two phenomena: (i) the space of full-variable rules grows factorially in $`d`$, providing more opportunities for fixed points, and (ii) integers with more digits have more admissible multisets, more potential rearrangements, and so more potential fixed-point equations to satisfy. The question of which of these $`506`$ fixed points at $`d = 6`$ arise as coefficient-preserving liftings from lower $`d`$, and which are genuinely new at $`d = 6`$, is the content of §4.

---

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: 2. Framework](02_framework.md) · [Next: 4. Cross-check $`d = 5 \to d = 6`$ →](04_cross_check.md)
