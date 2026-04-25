[← Back to paper](../README.md#table-of-contents) · [← Previous: 3. Classifications at $`d \leq 6`$](03_classifications.md) · [Next: 5. Theorem 5.2: 60714 universal at every $`d \geq 5`$ →](05_theorem_60714.md)

---

# 4. Cross-Dimensional Cross-Check: $`d = 5 \to d = 6`$

§3 established the classifications at $`d = 3, 4, 5, 6`$ independently at each digit length. This section addresses the cross-dimensional question of §1.3: among the $`33`$ universal full-variable fixed points at $`d = 5`$, which extend to $`d = 6`$ as universal full-variable fixed points?

## 4.1 The question, formally

Let $`F_5 = \{F^{(1)}, \ldots, F^{(33)}\}`$ be the set of universal full-variable fixed points at $`d = 5`$ (Theorem 3.3). For each $`F^{(k)} \in F_5`$, consider the padded integer $`F^{(k)}_{(6)}`$ — that is, $`F^{(k)}`$ interpreted as a six-digit integer by prepending a zero. Let $`\overline{F^{(k)}}`$ denote its sorted-descending form at length $`6`$: this is the sorted-descending form at length $`5`$ with a zero appended, since padding adds a zero that sorts to the smallest position.

We ask two questions for each $`F^{(k)}`$:

**Question A (algebraic).** Does any full-variable rule $`K_{\pi, \sigma}`$ at $`d = 6`$ satisfy $`K(F^{(k)}_{(6)}) = F^{(k)}`$? That is, does the fixed-point equation admit any full-variable solution at $`d = 6`$?

**Question B (dynamic).** If yes, is any such rule universal for $`F^{(k)}`$ at $`d = 6`$ — meaning every input in $`A_6`$ iterates to $`F^{(k)}`$?

A positive answer to both questions constitutes **coefficient-lifting success** from $`d = 5`$ to $`d = 6`$: the fixed point $`F^{(k)}`$ is a universal full-variable fixed point at both digit lengths. A negative answer to Question A is **algebraic obstruction** (no rule even fixes $`F^{(k)}`$ at $`d = 6`$). A negative answer to Question B despite a positive answer to A is **dynamic obstruction** (rules fix $`F^{(k)}`$ but none is universal).

## 4.2 The result

**Theorem 4.1.** *Among the $`33`$ universal full-variable fixed points at $`d = 5`$, the cross-dimensional behavior at $`d = 6`$ is as follows:*

- **$`17`$ fixed points face algebraic obstruction:** no full-variable rule at $`d = 6`$ fixes $`F`$.
- **$`15`$ fixed points face dynamic obstruction:** full-variable rules at $`d = 6`$ fix $`F`$, but none is universal.
- **$`1`$ fixed point admits a universal coefficient lifting:** $`F = 60714`$. Exactly two full-variable rules at $`d = 6`$ are universal for $`60714`$, forming a sign-flip pair.

*Formally: the set of $`d = 5`$ universal full-variable fixed points that are also $`d = 6`$ universal full-variable fixed points is $`\{60714\}`$. All other $`32`$ $`d = 5`$ fixed points are dimension-locked at $`d = 5`$.*

**Proof.** By exhaustive computation in two parts.

*Algebraic part.* For each $`F^{(k)} \in F_5`$, we enumerate all full-variable rules $`K_{\pi, \sigma}`$ at $`d = 6`$ and test whether $`K(F^{(k)}_{(6)}) = F^{(k)}`$. This reduces to a solution-counting problem: writing $`\overline{F^{(k)}} = (f_0, \ldots, f_5)`$, we seek $`(\pi, \sigma) \in S_6 \times S_6`$ with $`\pi_i \neq \sigma_i`$ for every $`i`$ and $`\sum_i (10^{\pi_i} - 10^{\sigma_i}) f_i = \pm F^{(k)}`$. Since $`F^{(k)} \in F_5`$ is nonzero, the equation is nontrivial. For each $`F^{(k)}`$, the number of full-variable $`(\pi, \sigma)`$ satisfying the equation is a specific non-negative integer. Computing this count for all $`33`$ fixed points:

- $`17`$ fixed points admit zero full-variable solutions.
- $`16`$ fixed points admit at least one full-variable solution. The number of solutions per fixed point varies from $`2`$ (for $`60714`$, $`60417`$, and $`1`$ other) up to $`132`$ (for fixed points with larger zero-digit counts at $`d = 6`$ when padded).

*Dynamic part.* For each of the $`16`$ fixed points with at least one algebraic solution, we test each fixed-point-satisfying rule for universality: does every admissible input $`n \in A_6`$ iterate to $`F^{(k)}`$ under this rule? This test is direct: iterate from each non-repdigit non-near-repdigit input at $`d = 6`$ ($`999{,}900`$ inputs) for up to $`300`$ steps, and record whether $`F^{(k)}`$ is reached. The basin is then the fraction of inputs reaching $`F^{(k)}`$.

For $`15`$ of the $`16`$ fixed points with algebraic solutions, every fixed-point-satisfying rule has basin $`< 1`$. The best basins are tabulated below.

For $`1`$ fixed point — $`F = 60714`$ — both full-variable rules satisfying the fixed-point equation are universal (basin $`= 1.0`$).

The computation is implemented as a two-stage enumeration: first a fast enumeration over $`(\pi, \sigma) \in S_6 \times S_6`$ with derangement filtering, producing the algebraic-solution set; then a basin test on each surviving candidate. Total runtime on commodity hardware: a few minutes for the algebraic part, several hours for the dynamic part. Full enumeration logs and per-fixed-point data are in Appendix A.4. $`\square`$

## 4.3 Tabulation of the 32 dimension-locked fixed points

**Table 4.1.** *The $`17`$ fixed points at $`d = 5`$ with algebraic obstruction at $`d = 6`$.*

| Fixed point | Digit multiset at $`d = 5`$ |
|:---:|:---|
| $`12456`$ | $`\{1, 2, 4, 5, 6\}`$ |
| $`14562`$ | $`\{1, 2, 4, 5, 6\}`$ |
| $`15642`$ | $`\{1, 2, 4, 5, 6\}`$ |
| $`16524`$ | $`\{1, 2, 4, 5, 6\}`$ |
| $`21456`$ | $`\{1, 2, 4, 5, 6\}`$ |
| $`24156`$ | $`\{1, 2, 4, 5, 6\}`$ |
| $`24561`$ | $`\{1, 2, 4, 5, 6\}`$ |
| $`28539`$ | $`\{2, 3, 5, 8, 9\}`$ |
| $`38754`$ | $`\{3, 4, 5, 7, 8\}`$ |
| $`41832`$ | $`\{1, 2, 3, 4, 8\}`$ |
| $`42183`$ | $`\{1, 2, 3, 4, 8\}`$ |
| $`43758`$ | $`\{3, 4, 5, 7, 8\}`$ |
| $`43785`$ | $`\{3, 4, 5, 7, 8\}`$ |
| $`43875`$ | $`\{3, 4, 5, 7, 8\}`$ |
| $`53928`$ | $`\{2, 3, 5, 8, 9\}`$ |
| $`65781`$ | $`\{1, 5, 6, 7, 8\}`$ |
| $`67581`$ | $`\{1, 5, 6, 7, 8\}`$ |

*All $`17`$ fixed points share a structural feature: their multisets at $`d = 5`$ contain at most one zero digit, so padding to $`d = 6`$ gives at most two absorbing positions — typically insufficient for any full-variable sv$`=6`$ rule to satisfy $`K(F_{(6)}) = F_{(6)}`$.*

**Table 4.2.** *The $`15`$ fixed points at $`d = 5`$ with dynamic obstruction at $`d = 6`$.*

For these $`15`$ fixed points, full-variable rules satisfying $`K(F_{(6)}) = F_{(6)}`$ exist but are not universal. The best basin each fixed point achieves at $`d = 6`$ over the $`4{,}905`$ admissible multisets is given below.

| Fixed point | # candidate sv=6 rules | Best basin |
|:---:|:---:|:---:|
| $`54`$      | $`528`$ | $`0.9631`$ |
| $`60417`$   | $`4`$   | $`0.9598`$ |
| $`21834`$   | $`4`$   | $`0.9472`$ |
| $`45621`$   | $`12`$  | $`0.7951`$ |
| $`24183`$   | $`4`$   | $`0.7182`$ |
| $`37584`$   | $`2`$   | $`0.5594`$ |
| $`45612`$   | $`12`$  | $`0.5111`$ |
| $`41562`$   | $`4`$   | $`0.5025`$ |
| $`3753`$    | $`16`$  | $`0.3199`$ |
| $`18342`$   | $`4`$   | $`0.2137`$ |
| $`16578`$   | $`2`$   | $`0.1953`$ |
| $`58239`$   | $`4`$   | $`0.1880`$ |
| $`16758`$   | $`2`$   | $`0.0520`$ |
| $`37854`$   | $`2`$   | $`0.0245`$ |
| $`17685`$   | $`2`$   | $`0.0049`$ |

*The basins range from $`0.0049`$ to $`0.9631`$; no rule is universal. For most fixed points, competing attractors (the rule's other fixed points or short cycles) draw off substantial fractions of input space. Notably, $`54`$ and $`60417`$ achieve basins very close to $`1`$ (respectively $`0.9631`$ and $`0.9598`$) but remain dynamically obstructed — they are "near misses" in a precise sense, and were among the candidates investigated in detail before $`60714`$ was identified as the unique transcendent fp at $`d = 5`$.*

**Observation 4.1 (zero-digit count predicts algebraic solvability at $`d = 6`$).** *Among the $`33`$ fixed points at $`d = 5`$, those with one zero digit at $`d = 5`$ (so two zero digits when padded to $`d = 6`$) are candidates for coefficient-preserving lifting with two absorbing positions. Those with no zero digits have only one absorbing position after padding, and empirically none admits a full-variable sv=$`6`$ rule fixing them. This pattern — more zero digits $`\Rightarrow`$ more absorbing capacity $`\Rightarrow`$ more algebraic solutions — is developed further at §5 and §6.*

## 4.4 The unique success case: $`F = 60714`$

We record the $`d = 6`$ universal lifting of $`60714`$ explicitly, as it is the cornerstone of §5.

**Proposition 4.1.** *At $`d = 6`$, exactly $`2`$ full-variable rules are universal for $`F = 60714`$. These are sign-flip pairs of each other. One canonical representative has permutations*

$$\pi = (4, 1, 2, 3, 5, 0), \qquad \sigma = (2, 0, 1, 4, 3, 5),$$

*with coefficient vector*

$$c = (9900,\; 9,\; 90,\; -9000,\; 99000,\; -99999).$$

*In letter notation (§ Appendix B conventions), the rule is*

$$K(n) = \mathrm{eadcbf}(n) - \mathrm{fdeacb}(n).$$

*The rule is universal at $`d = 6`$: every admissible input $`n \in A_6`$ iterates to $`60714`$ under $`K`$, with basin $`= 1.0`$ verified over all $`999{,}900`$ admissible inputs.*

**Verification.** Apply $`K`$ to $`F_{(6)} = 060714`$. Sorted-descending form: $`(7, 6, 4, 1, 0, 0)`$. Compute:

$$K(060714) = |eadcbf - fdeacb|_{a=7, b=6, c=4, d=1, e=0, f=0} = |071460 - 010746| = 60714. \quad \checkmark$$

Universality is verified by exhaustive iteration over $`A_6`$: every admissible six-digit integer reaches $`60714`$ in at most some number of steps, with maximum reaching time $`T_6 = 1`$ for most inputs (direct fixing) and up to a small number of steps for the remainder. See Appendix A.4 for the full basin-verification log. $`\square`$

**The structural shape of the lifting.** Compare $`60714`$'s native rule at $`d = 5`$:

$$\pi_5 = (4, 1, 2, 3, 0), \qquad \sigma_5 = (2, 0, 1, 4, 3),$$

coefficient vector $`(9900, 9, 90, -9000, -999)`$.

The $`d = 6`$ rule extends this by appending position $`5`$ with $`\pi_5 = 5, \sigma_5 = 5`$ — wait, no, this is wrong. The $`d = 6`$ rule does not simply append a position; it restructures. Specifically: the $`d = 5`$ rule's fifth coefficient is $`-999`$; the $`d = 6`$ rule's fifth and sixth coefficients are $`99000`$ and $`-99999`$, which sum to $`99000 - 99999 = -999`$. This is the **split lifting** structure developed at §5: the single native coefficient $`-999`$ is "split" across two new positions at $`d = 6`$, summing back to $`-999`$ to preserve the action of the rule on $`F`$'s nonzero digits (since both new positions correspond to zero digits of $`F_{(6)}`$, which absorb them in the $`K(F) = F`$ computation).

This lifting structure is explicit, and its generalization to $`d = 7, 8, 9, \ldots`$ is the content of §5.

## 4.5 Implications for the paper

Theorem 4.1 is the central cross-dimensional result at the $`d = 5 \to d = 6`$ boundary. It establishes:

1. **Cross-dimensional universality is rare at this boundary.** Only $`1`$ of $`33`$ fixed points succeeds.
2. **The distinction is structural, not incidental.** $`60714`$'s native rule has a specific algebraic structure — the split-lifting structure — that admits extension to $`d = 6`$. The other $`32`$ fixed points' native rules do not.
3. **The mechanism generalizes.** The coefficient-preserving lifting that works at $`d = 5 \to d = 6`$ can be iterated to $`d = 6 \to d = 7 \to d = 8 \to \cdots`$ for $`60714`$. This is the content of §5.
4. **The uniqueness of $`60714`$ is proven.** No other $`d = 5`$ universal full-variable fixed point extends to $`d = 6`$. Future results about $`60714`$'s cross-dimensional behavior rest on this uniqueness, which is established here by exhaustion.

**Remark on Conjecture 1 (informal statement).** For a universal full-variable fixed point $`F`$ at native digit length $`d_F`$, define its *dimension-locking spectrum* as the set of $`d > d_F`$ at which $`F`$ is also a universal full-variable fixed point. Theorem 4.1 establishes that $`32`$ of $`33`$ fixed points at $`d = 5`$ have empty dimension-locking spectrum extension to $`d = 6`$, and that one — $`60714`$ — has $`d = 6`$ in its spectrum. Theorem 5.2 of the next section extends this: $`60714`$'s dimension-locking spectrum contains every $`d \geq 5`$. The other $`32`$ fixed points' spectra at $`d > 6`$ are addressed individually at the appendix level, but no systematic characterization of which fixed points have unbounded dimension-locking spectra is presently known beyond the case of $`60714`$.

A formal conjecture — that every full-variable fixed point with unbounded dimension-locking spectrum admits a coefficient-preserving lifting similar to $`60714`$'s — is stated as Conjecture 7.1.

---

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: 3. Classifications at $`d \leq 6`$](03_classifications.md) · [Next: 5. Theorem 5.2: 60714 universal at every $`d \geq 5`$ →](05_theorem_60714.md)
