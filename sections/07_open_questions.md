[← Back to paper](../README.md#table-of-contents) · [← Previous: 6. The $`\{7, 6, 4, 1\}`$-thread](06_thread_7641.md) · [Next: Appendix A. Classification tables →](A_classification_tables.md)

---

# 7. Open Questions and Conjectures

The results of §3–§6 establish a specific empirical and structural picture at digit lengths $`d \leq 9`$ for the multiset thread $`\{7, 6, 4, 1\}`$, with a full theorem (§5, Theorem 5.2) covering $`60714`$ at every $`d \geq 5`$. Several natural questions extend beyond what we have proven; we collect them here.

## 7.1 Dimension-locking as a general phenomenon

Theorem 4.1 established that $`32`$ of $`33`$ universal full-variable fixed points at $`d = 5`$ are dimension-locked at $`d = 5`$ — no rank-$`6`$ rule at $`d = 6`$ is universal for them. The natural generalization is:

**Conjecture 7.1 (effective rank bound at cross-dimensional universality).** *Let $`F`$ be a universal full-variable fixed point at native digit length $`d_F`$, and suppose $`K`$ is a full-variable rule at some $`d \neq d_F`$ that is universal for $`F`$. Then $`\mathrm{sv}_F(K) < d`$ — that is, the effective rank of $`K`$ at $`F`$ is strictly less than the algebraic rank.*

Informally: when a fixed point appears at a non-native digit length, it always does so through a rule whose effective rank at $`F`$ is strictly reduced — some of the rule's coefficients are "absorbed" by $`F`$'s zero digits and do not contribute to the computation $`K(F) = F`$.

**Status.** Verified exhaustively at $`d = 6`$ for all $`33`$ $`d = 5`$ fixed points (Theorem 4.1 and the associated enumeration). For $`60714`$, Theorem 5.2's construction automatically satisfies the conjecture at every $`d \geq 6`$: the coefficient-preserving lifting has $`\mathrm{sv}_F = 4 < d`$ at every $`d \geq 6`$. For $`6174`$, the liftings at $`d = 7, 8, 9`$ similarly satisfy $`\mathrm{sv}_F \leq d - 3 < d`$. The conjecture has not been tested at $`d > 6`$ for the other $`32`$ dimension-locked $`d = 5`$ fixed points or for fps native at $`d = 6`$.

**Formal verification of Conjecture 7.1 at $`d \geq 7`$ is open.** Verifying it at a specific $`d \geq 7`$ for a specific fixed point $`F`$ reduces to exhaustive enumeration over rank-$`d`$ rules satisfying $`K(F_{(d)}) = F`$, checking that all such rules have $`\mathrm{sv}_F < d`$. The enumeration is tractable at $`d = 7`$ (several million rules per fixed point) and becomes computationally demanding at $`d \geq 8`$.

## 7.2 The structural invariant and dimensional fate

Observation 6.2 records the empirical unification of $`60714`$, $`60417`$, and $`6174`$ through the $`\mathrm{sum\_locked\_spans}`$ invariant. The natural formal statement is:

**Conjecture 7.2 (structural invariant controls dimensional fate).** *For a universal full-variable fixed point $`F`$ with native digit length $`d_F`$ and native rule $`K_F`$, the cross-dimensional behavior of $`F`$ at $`d > d_F`$ is controlled by $`\mathrm{sum\_locked\_spans}(K_F)`$ and the number of zero digits of $`F`$ at $`d`$. Specifically:*

- *If $`\mathrm{sum\_locked\_spans}(K_F)`$ is small relative to the number of absorbing positions at $`d`$, a coefficient-preserving lifting exists that is universal for $`F`$ at $`d`$.*
- *If the invariant is large relative to the absorbing capacity, either no lifting exists (algebraic obstruction) or liftings exist but no one is universal (dynamic obstruction).*

**Status.** Purely conjectural. The empirical pattern holds for $`60714`$, $`60417`$, $`6174`$; whether it holds for arbitrary universal full-variable fixed points at $`d_F = 4, 5, 6`$ has not been systematically tested. A positive resolution would give a quantitative criterion for predicting cross-dimensional transcendence from the native rule alone, obviating the need for direct enumeration at each candidate $`d`$.

## 7.3 Other multiset clusters

**Question 7.1.** *Which digit multisets support universal full-variable fixed points at three or more consecutive native digit lengths?*

The $`\{7, 6, 4, 1\}`$ thread is the only such example in our classification at $`d \leq 6`$. The other $`d = 4`$ multiset $`\{2, 3, 5, 8\}`$ produces fps at $`d = 4`$ but not at $`d = 5, 6`$. Several $`d = 5`$ multisets have analogues at $`d = 4`$ or $`d = 6`$ but not at both.

Extending the search to $`d \geq 7`$ would require either a full classification at $`d = 7`$ (the $`d = 7`$ enumeration of $`9{,}344{,}160`$ full-variable rules is computationally demanding; see Appendix D) or a more structural argument for which multisets can support cross-dimensional threads.

**Question 7.2.** *Is there an analogue of $`60714`$ at higher native digit lengths — a fixed point $`F`$ with native $`d_F = 7`$ or $`d_F = 8`$ that is universal at every $`d \geq d_F`$ via a coefficient-preserving lifting?*

Such fixed points would constitute a second (or third, etc.) dimension-transcendent attractor family. Observed data at $`d_F = 6`$ and $`d_F = 7`$ (Appendix D) contain several candidates that transcend to $`d + 1`$, but none has been proven to lift uniformly to every higher $`d`$ as $`60714`$ does.

## 7.4 Other bases

All results in this paper concern base $`10`$. The analogous framework in base $`b \geq 2`$ would replace $`10^{\pi_i}`$ with $`b^{\pi_i}`$ in the coefficient expansion of §2.2 and otherwise proceed identically.

**Question 7.3.** *For each base $`b`$, does there exist a universal full-variable fixed point at some native digit length that is universal at every $`d \geq d_F`$ via a coefficient-preserving lifting?*

At base $`10`$, the answer is yes, demonstrated by $`60714`$. For small bases ($`b = 2, 3, \ldots`$), the analogous classification would produce different specific fixed points, and the structural mechanism of coefficient-preserving lifting would apply with appropriate modifications. The related literature [Kay 2024, Peterson 2008] addresses the classical Kaprekar rule at other bases; our framework has not been systematically extended.

## 7.5 The $`6174`$ pattern at $`d \geq 10`$

Theorem 6.1 establishes $`6174`$'s behavior at $`d = 4, 5, \ldots, 9`$. The pattern at $`d = 8, 9`$ (near-universal with $`45`$-input escape class) is expected to continue at $`d \geq 10`$: the escape class structure is $`d`$-independent (same multiset shape at each $`d`$), while the admissible input set grows, so the basin fraction asymptotes to $`1`$.

**Question 7.4.** *Is $`6174`$ strict-universal at any $`d \geq 10`$?*

Empirical extrapolation suggests no: at each $`d \geq 8`$, the $`45`$-input escape class persists, and no coefficient-preserving lifting eliminates it. A proof (or disproof) of this pattern at some specific large $`d`$ would complete the $`6174`$ pattern to an arbitrary horizon. At the structural level, proving that the $`45`$-input escape class is genuinely stable under all coefficient-preserving liftings is an algebraic question on the coefficient vectors' action on multisets of the form $`(X, X, X, X, 0, \ldots, 0)`$.

## 7.6 The depth of the escape class

Lemma 5.2.2 gives a closed form for $`|E_d^{(1)}|`$ — the number of step-$`1`$ collapse inputs at digit length $`d`$. The full escape class $`E_d`$ is the backward orbit of $`B_d \cap A_d`$, and at $`d \leq 11`$ exhaustive enumeration confirms that every orbit in $`E_d`$ reaches $`0`$ in at most $`4`$ iterations. The natural question:

**Question 7.6.** *Is there a uniform-in-$`d`$ bound on the multi-step depth of $`E_d`$? Does $`|E_d| / |A_d| \to 0`$ as $`d \to \infty`$?*

Combinatorially, $`|E_d^{(1)}|`$ grows polynomially in $`d`$ (specifically as $`O(d^{d_0 - 1})`$ via Lemma 5.2.2) while $`|A_d|`$ grows as $`O(d^9)`$ with much larger constant; the basin fraction $`1 - |E_d|/|A_d|`$ should approach $`1`$, but no proof is provided here.

## 7.7 Beyond universal full-variable fixed points

The full-variable constraint $`\mathrm{sv} = d`$ excludes dimension-agnostic fixed points like $`45`$, $`495`$, $`450`$ (§2.5). These fixed points exhibit their own cross-dimensional behavior through rank-reducing rules, which we have not addressed.

**Question 7.5.** *Is there a useful cross-dimensional theory for fixed points of rank-reducing rules ($`\mathrm{sv} < d`$)?*

The dimension-agnostic family is the simplest case: these fixed points persist across all digit lengths by construction. A more interesting question is whether there are non-full-variable rules whose cross-dimensional behavior mirrors $`60714`$'s full-variable universality — say, rules with $`\mathrm{sv} = d - 1`$ that produce universal fixed points at every $`d`$ in some range. We leave this open.

## 7.8 Concluding remarks

The central result of this paper is Theorem 5.2: $`60714`$ is a universal full-variable fixed point at every digit length $`d \geq 5`$, under an explicit coefficient-preserving lifting. This is the first explicitly constructed cross-dimensional persistence result in the generalized Kaprekar family. The supporting results — the classifications of §3, the uniqueness of §4, and the $`6174`$ cross-dimensional pattern of §6 — place this theorem in a structural context that raises more questions than it answers. Conjectures 7.1 and 7.2 and Questions 7.1–7.6 together outline a program for understanding cross-dimensional behavior in the generalized family: which fixed points transcend, under what structural conditions, and with what mechanism.

The methodology of the paper — exhaustive enumeration at each digit length, combined with structural proof on the cases the enumeration distinguishes — has been effective at $`d \leq 6`$ for the full rule space and at $`d \leq 9`$ for targeted verification of specific fps. Extending this methodology to $`d \geq 7`$ for the full rule space, or to $`d \geq 10`$ for $`6174`$, is the natural next step.

---

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: 6. The $`\{7, 6, 4, 1\}`$-thread](06_thread_7641.md) · [Next: Appendix A. Classification tables →](A_classification_tables.md)
