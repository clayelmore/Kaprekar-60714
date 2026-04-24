# Dimension-Transcendent Attractors in Generalized Kaprekar Routines

---

## Abstract

The classical Kaprekar routine at four digits iterates $K(n) = \alpha(n) - \beta(n)$, where $\alpha(n)$ and $\beta(n)$ are the integers formed by arranging $n$'s digits in descending and ascending order. For every non-repdigit four-digit input, the orbit converges in at most seven steps to the fixed point $6174$. Generalizing the construction to arbitrary digit length $d$, the analogous rule converges to $495$ at $d = 3$ but fails at $d = 5$: orbits enter cycles rather than fixed points.

This failure is commonly described as a peculiarity of five-digit arithmetic. We argue that it is instead a peculiarity of the specific subtraction rule. The classical "descending minus ascending" construction is one specific point in a space of $d! \cdot (d! - 1)$ ordered permutation-pair rules at each digit length, and its behavior across $d$ is not uniform: the algebraic rank of the classical rule is $d$ at $d = 4$ but strictly less than $d$ at $d = 3$ and $d = 5$ because of forced middle-digit cancellation. The failure at $d = 5$ reflects the classical rule being rank-$4$ there, not a failure of Kaprekar convergence.

When we classify all permutation-pair rules at each digit length, universal full-variable fixed points exist at $d = 4$, $d = 5$, and $d = 6$. We complete this classification exhaustively at $d \leq 6$, identifying $33$ universal fixed points at $d = 5$ and $507$ at $d = 6$. We then ask which fixed points extend from one digit length to the next: if $F$ is a universal full-variable fixed point at digit length $d$, does some rule at $d + 1$ also have $F$ as a universal fixed point?

Among the $33$ universal fixed points at $d = 5$, exactly one — $F = 60714$ — is a universal full-variable fixed point at $d = 6$. The remaining $32$ are dimension-locked at $d = 5$: no full-variable rule at $d = 6$ attracts them universally. Moreover, for $60714$ we construct an explicit family of permutation-pair rules at each $d \geq 5$, connected by a coefficient-preserving lifting recipe, and prove:

**Theorem.** *$60714$ is a universal full-variable fixed point at every digit length $d \geq 5$, under the coefficient-preserving lifting family constructed in §5.*

This is, to our knowledge, the first rigorously dimension-transcendent attractor in the generalized Kaprekar family. The classical Kaprekar constant $6174$ exhibits a related but non-monotone cross-dimensional fingerprint, proven here: universal at $d = 4$ (native) and $d = 7$, with algebraic obstruction at $d = 5$, dynamic obstruction at $d = 6$, and near-universal lifting at $d = 8$ and $d = 9$. $60714$, $6174$, and $60417$ share the digit multiset $\{7, 6, 4, 1\}$ and are unified under a single structural invariant — $\mathrm{sum\_locked\_spans}$ — that determines each fixed point's cross-dimensional behavior.

---

## §1. Introduction

### 1.1 Kaprekar's routine and the middle-digit cancellation

In 1949, D. R. Kaprekar observed a striking property of four-digit integers in base ten [Kaprekar 1955]. For any four-digit $n$ with at least two distinct digits, let $\alpha(n)$ be the integer formed by arranging $n$'s digits in descending order, and $\beta(n)$ the integer formed by arranging them in ascending order. Iterating

$$K(n) = \alpha(n) - \beta(n)$$

produces a sequence that converges to $6174$ within at most seven steps, regardless of starting value.

At three digits, the analogous construction converges to $495$. At five digits, it fails: every non-repdigit orbit enters one of three cycles rather than reaching a fixed point [Prichett 1981]. This failure is typically described as a peculiarity of five-digit arithmetic. We argue that it reveals something deeper about the classical rule itself.

Expand $K$ at $d = 3$ algebraically. For sorted-descending digits $(a, b, c)$ with $a \geq b \geq c$ and at least two distinct digits, $K(a, b, c) = \overline{abc} - \overline{cba}$. The subtraction's borrow pattern is forced: the ones place $c - a$ borrows; the middle place becomes $b - b - 1 = -1$ after the borrow and must borrow again; the hundreds place becomes $a - c - 1$ after the second borrow. The result simplifies to

$$K(a, b, c) = 99 \, (a - c),$$

which depends on only $a$ and $c$. The middle digit $b$ cancels identically. Algebraically, $K$ at $d = 3$ has coefficient vector $(-99, \, 0, \, 99)$: the coefficient on the middle position is exactly zero.

This is not a computational observation — it is a structural fact about the classical construction. At every odd digit length, the classical rule's center-position coefficient vanishes through the same forced borrow chain. The classical rule at $d = 3$ is *not* a rank-$3$ object; it is a rank-$2$ object wearing rank-$3$ clothes. The classical rule at $d = 5$ is likewise rank-$4$, not rank-$5$. The failure of the classical rule to produce fixed-point convergence at $d = 5$ is therefore not surprising once one asks about rank-$5$ rules: the classical rule *isn't one*.

This observation opens the question we pursue in this paper. If the classical rule is a specific algebraic construction whose rank varies with $d$, and if convergence properties depend on rank, then the natural object of study is not the classical rule across $d$ but *the space of all rearrangement-subtraction rules* at each $d$. The classical rule is one specific point in that space. The question becomes: which integers are universal fixed points, which rules attract them, and how do the rules relate across digit lengths?

### 1.2 Permutation-pair rules

Let $n$ be a positive integer padded to $d$ digits, and let $\mathrm{sort\_desc}(n) = (x_0, x_1, \ldots, x_{d-1})$ denote its sorted-descending digit sequence, with $x_0 \geq x_1 \geq \cdots \geq x_{d-1}$. Given any ordered pair of permutations $\pi, \sigma \in S_d$ with $\pi \neq \sigma$, the **permutation-pair rule** is

$$K_{\pi, \sigma}(n) = \bigl| \pi \cdot \mathrm{sort\_desc}(n) - \sigma \cdot \mathrm{sort\_desc}(n) \bigr|,$$

where $\pi \cdot (x_0, \ldots, x_{d-1})$ denotes the integer $\sum_{i} 10^{d-1-i} x_{\pi_i}$ — the digits rearranged by $\pi$. The classical rule is $\pi = (0, 1, \ldots, d-1)$ and $\sigma = (d-1, d-2, \ldots, 0)$ (descending minus ascending), which we denote $K_0$.

Every permutation-pair rule expands linearly in the sorted-descending digits:

$$K_{\pi, \sigma}(n) = \left| \sum_{i=0}^{d-1} c_i \, x_i \right|,$$

where the integer coefficients $c_i$ depend only on $(\pi, \sigma)$ and satisfy $\sum_i c_i = 0$. Specifically, $c_i = 10^{d-1-\pi^{-1}(i)} - 10^{d-1-\sigma^{-1}(i)}$. Define the **algebraic rank** (or **surviving-variable count**) of the rule:

$$\mathrm{sv}(K_{\pi, \sigma}) = \#\{ i : c_i \neq 0 \}.$$

The rule is **full-variable** at digit length $d$ if $\mathrm{sv} = d$ — every sorted-descending position participates nontrivially in the output. The classical rule is full-variable at $d = 4$ (coefficient vector $(999, 90, -90, -999)$) but not at odd $d$, where the middle-position coefficient vanishes by the cancellation of §1.1.

A rule $K$ is **universal** for a fixed point $F$ at digit length $d$ if $K(F) = F$ and every non-repdigit $d$-digit input iterates to $F$ under $K$. We adopt the standard basin convention excluding repdigits (multisets with one distinct digit) and near-repdigits (multisets where one digit appears $d - 1$ or $d$ times); these degenerate inputs are excluded from Kaprekar-style convergence analysis throughout the literature [Prichett 1981, Dahl 2026].

### 1.3 The organizing question

Fix an integer $F$. Define its **native digit length** $d_F$ to be the smallest $d$ at which $F$ is a universal full-variable fixed point of some rule $K_{\pi, \sigma}$ at $d$. If $F$ has no native digit length in this sense, it is outside the scope of this paper.

The organizing question is then:

> *For a fixed point $F$ with native digit length $d_F$, does $F$ remain a universal full-variable fixed point at any digit length $d > d_F$? If so, what is the structural relationship between the rule at $d_F$ and the rule at $d$?*

The first part of this question has an immediate affirmative answer for one class of fixed points: the dimension-agnostic family (including $45$, $495$, $450$) whose rules have $\mathrm{sv} < d$ at every $d$. These fixed points persist across digit lengths precisely because their rules cancel interior digits, reducing to lower-rank operations. We discuss them in §2.5 and exclude them from the full-variable classification by the $\mathrm{sv} = d$ constraint.

Among *full-variable* fixed points, the question is considerably sharper. The classical result says: at $d = 4$, the classical rule $K_0$ is full-variable (rank $4$) and universal for $6174$. But $K_0$ at $d = 5$ has rank $4$, not $5$, so it is not even in the $\mathrm{sv} = 5$ space at $d = 5$; the question of whether $6174$ is a universal *full-variable* fixed point at $d = 5$ is not the question of whether $K_0$ converges there. It is the question of whether any rank-$5$ rule, anywhere in the $14{,}280$-rule space at $d = 5$, has $6174$ (padded to $06174$) as a universal fixed point. The answer, exhaustively verified in §3 and §4, is no: no rank-$5$ rule even has $6174$ as a fixed point at $d = 5$.

The full-variable universal fixed points at $d = 5$ are thirty-three specific integers — none of them $6174$. Among these thirty-three, the question of §1.3 becomes: which extend to $d = 6$ as universal rank-$6$ fixed points? Which further extend to $d = 7$, $d = 8$, and beyond?

### 1.4 On method: from brute enumeration to structural proof

A word on how this investigation proceeded. The classical Kaprekar routine has an elegance accessible to anyone who can subtract: arrange the digits in descending order, arrange them in ascending order, subtract, iterate. Convergence to $6174$ is a surprise that anyone can verify with a calculator, and the rule requires no definition beyond ordinary arithmetic. Any generalization in the spirit of this result should ideally preserve some comparable transparency.

Our approach proceeds in the opposite order. We did not begin with a structural hypothesis about which integers ought to be dimension-transcendent attractors. We began with brute-force enumeration: at each digit length $d$, compute the universal full-variable fixed points by testing every permutation-pair rule exhaustively against every non-repdigit input. At $d = 3$, $4$, $5$, $6$ this enumeration is tractable — the largest, $d = 6$, requires testing $190{,}800$ full-variable rules against $999{,}900$ inputs, a search that runs in hours on commodity hardware but is impractical to organize, verify, and iterate on without automated scaffolding. From the resulting lists of fixed points, we asked the cross-dimensional question empirically: which fixed points at $d$ reappear at $d + 1$?

The enumerations themselves, the data-structuring of the resulting fixed-point catalogues, and the systematic probe of structural hypotheses against the empirical evidence were conducted in collaboration with AI research tools (principally Anthropic's Claude), used as a working partner for code generation, numerical verification, adversarial review of proposed structural claims, and iterative hypothesis testing. We document this collaboration explicitly because the paper's empirical foundation would not have been practical to produce without it, and because the methodological pattern — exhaustive brute search, pattern recognition on the output, proposed structural explanation, adversarial re-testing, repeat — is one we believe is increasingly relevant to exploratory mathematics.¹

#### 1.4.1 The 54 → 60714 discovery arc

To make the method concrete, we describe the specific discovery process that led to this paper's main theorem. An early candidate for dimension-transcendence was $F = 54$. At $d = 2$ under the classical rule, $54$ is a universal fixed point. At $d = 5$, the full-variable classification (§3) finds $54$ as one of $33$ universal fps under a specific rank-$5$ rule — the rule $\pi = (1, 2, 4, 3, 0), \sigma = (2, 0, 3, 4, 1)$ with coefficient vector $(-90, 99, 9000, -9000, -9)$. Initial empirical work suggested $54$ as a natural candidate for the dimension-transcendence story, since it appears at both $d = 2$ and $d = 5$.

Closer examination revealed a structural complication. $54$'s sorted-descending form at $d = 5$ is $(5, 4, 0, 0, 0)$ — three of the five digits are zero. In the native rule at $d = 5$, three of the five coefficients are paired with these zero digits and contribute nothing to $K(F) = F$. The effective rank of the rule at $F$ — what we formalize in §2.6 as $\mathrm{sv}_F$ — is $2$, not $5$. $54$ is algebraically an sv$=5$ fixed point, but structurally it inherits its fixed-point status from a rank-$2$ algebraic operation on $(5, 4)$ with the other three positions absorbing coefficients that cancel internally. The fixed-point equation $K(54) = 54$ at $d = 5$ is effectively the same equation as at $d = 2$, dressed up to occupy $d = 5$ without adding new structural content.

This observation sharpened the question. A genuine dimension-transcendent fixed point would need $\mathrm{sv}_F = d_F$ — all coefficients of its native rule contributing to $K(F) = F$ through nonzero digits. Among the $33$ fixed points at $d = 5$, we searched for fixed points with no zero digits (so that $\mathrm{sv}_F = 5$ automatically). Exhaustive enumeration at $d = 5 \to d = 6$ then identified the unique fixed point satisfying this criterion that also extends to $d = 6$ via a coefficient-preserving lifting: $F = 60714$. The existence of a lifting at $d = 6$ is automatic by a structural argument (Proposition 5.1); the nontrivial content is that the lifting is *universal* at $d = 6$ and, we prove, at every $d \geq 5$.

The paper's main theorem is thus the answer to a question that the $54$ counterexample forced us to formulate precisely: among universal full-variable fixed points with $\mathrm{sv}_F = d_F$ at their native digit length, which admit universal coefficient-preserving liftings at every higher digit length?

#### 1.4.2 Conclusion

This methodological sequence — exhaustive empirical search, identification of counterexamples that refine the question, structural proof on the refined target — is explicit rather than disguised. The classical Kaprekar routine is elegant because its rule is stated in a single sentence; the result we present here is structural in a different sense. The rule varies with $d$ (via coefficient-preserving lifting), the construction is explicit, the proof is finite-state-plus-algebraic, and the fixed point $60714$ is distinguished not by aesthetic priority but by being the one case where the proof closes out uniformly across all $d \geq 5$.

¹ A companion article discussing this methodology and its broader implications for collaborative mathematical research will appear separately.

### 1.5 The main results

This paper answers the following:

**Theorem 1 (Classification, §3).** *The universal full-variable fixed points at digit lengths $d \leq 6$ are as follows:*

- *$d = 3$: no universal full-variable fixed points. ($30$ rank-$3$ rules enumerated exhaustively.)*
- *$d = 4$: four universal full-variable fixed points — $1746$, $2538$, $5382$, $6174$. ($552$ rank-$4$ rules enumerated exhaustively.)*
- *$d = 5$: thirty-three universal full-variable fixed points. ($14{,}280$ rank-$5$ rules enumerated exhaustively.)*
- *$d = 6$: five hundred and seven universal full-variable fixed points. ($517{,}680$ rank-$6$ rules enumerated exhaustively.)*

The classifications at each $d$ are complete, reproducible, and definitive. Full tables appear in Appendix A.

**Theorem 2 (Cross-dimensional cross-check, §4).** *Of the thirty-three universal full-variable fixed points at $d = 5$, exactly one — $F = 60714$ — is a universal full-variable fixed point at $d = 6$ under some rule. The remaining thirty-two are dimension-locked at $d = 5$: no rank-$6$ rule at $d = 6$ is universal for any of them.*

The proof is by exhaustive computation: for each of the thirty-three fixed points, we enumerate all rank-$6$ rules fixing $F$ (padded to six digits), test each for universality, and observe that $60714$ alone admits a universal rule.

**Theorem 3 (Dimension-transcendence of $60714$, §5).** *$F = 60714$ is a universal full-variable fixed point at every digit length $d \geq 5$, under an explicit family of coefficient-preserving lifting rules derived from its native rule at $d = 5$.*

The lifting family consists of two ladders: an odd ladder $d = 5, 7, 9, \ldots$ and an even ladder $d = 6, 8, 10, \ldots$. At each step of each ladder, the rule at $d$ is obtained from the rule at $d - 2$ by appending a pair of coefficients summing to zero. The coefficients at positions corresponding to $60714$'s nonzero digits are preserved throughout; the coefficients at positions corresponding to $60714$'s zero digits absorb the structural content of the lifting.

The proof reduces to two lemmas. Lemma 5.1 (structural) establishes that the set of inputs with two trailing zeros in their sorted-descending form is invariant under any zero-sum pair lifting, with the lifted rule acting on this set as the base rule at $d - 2$ on the non-tail digits. Lemma 5.2 (the main analytic content) establishes that every non-quasi-repdigit orbit at $d \geq 7$ reaches the tail-two-zeros absorbing set in a bounded number of iterations. Lemma 5.2 is proved by two complementary techniques: exhaustive finite-state enumeration over digit multisets at $d = 7, 8, \ldots, 16$ (approximately $25$ million multisets, zero exceptions), and a $d$-independent algebraic argument at $d \geq 17$ (odd) and $d \geq 18$ (even) based on core non-negativity under sorted-descending inputs (Lemmas C1, C2 in Appendix C). Together with direct verification at the ladder roots $d = 5$ and $d = 6$, the two lemmas yield universality at every $d \geq 5$ by induction along each ladder.

**Theorem 4 (The $\{7, 6, 4, 1\}$-thread, §6).** *The digit multiset $\{7, 6, 4, 1\}$ (with zero padding as needed) is the support of universal full-variable fixed points at three distinct digit lengths: $d = 4$ ($6174$, $1746$), $d = 5$ ($60714$, $60417$), and $d = 6$ ($60714$, $146070$, $170460$, $607140$). The classical Kaprekar constant $6174$ has a verified cross-dimensional fingerprint:*

- *$d = 4$: strict-universal (native).*
- *$d = 5$: algebraic obstruction — no rank-$5$ rule fixes $6174$.*
- *$d = 6$: dynamic obstruction — four rank-$6$ rules fix $6174$, best basin $0.969$.*
- *$d = 7$: strict-universal via the coefficient-preserving lifting $(efgabcd, fgedcba)$.*
- *$d = 8$, $d = 9$: near-universal, with a constant escape class of $45$ multisets of the form $(X, X, X, X, 0, 0, \ldots)$; basin asymptotes to $1$ as $d$ grows.*

*$60714$, $6174$, and $60417$ are unified under a structural invariant, the $\mathrm{sum\_locked\_spans}$ of their native rules — taking values $5$, $8$, $7$ respectively — which empirically controls the number of absorbing (zero-digit) positions at which a coefficient-preserving lifting succeeds. This unification is empirical, not proven.*

### 1.6 Why $60714$ is the uniquely complete case

Theorem 3 establishes $60714$ as universal at every $d \geq 5$ via an explicit construction, with the proof closing out through a combination of finite-state verification at low $d$ and a $d$-independent algebraic argument at high $d$. No other fixed point is shown to admit a universal rule at every $d$ in its range.

Other universal fixed points exhibit cross-dimensional transcendence in partial forms:

- $6174$ transcends at $d = 4$, $d = 7$, and (near-universally) at $d = 8$, $d = 9$, with algebraic or dynamic obstruction at $d = 5, 6$.
- $146070$ and $607140$ (both in the $\{7, 6, 4, 1\}$-thread, native at $d = 6$) transcend to $d = 7$ via the same coefficient-preserving machinery; $146070$'s ladder extension is verified through $d = 12$.
- Among the $507$ universal fixed points at $d = 6$, empirical surveys indicate transcendence to $d = 7$ is *common*, not rare, at higher native digit lengths. These surveys are tabulated in Appendix D but not proven as theorems in this paper.

$60714$'s distinction is therefore not "uniqueness as a transcendent fixed point" (many other fixed points transcend partially) but **uniqueness as the proven case**: the only fixed point for which a uniform lifting construction is established rigorously at every $d$ in its range. The structural contrast with $6174$ and $60417$ in §6 clarifies why $60714$ succeeds uniformly while other fixed points in its thread do not.

### 1.7 Relation to existing literature

The literature on Kaprekar routines generalizes the classical construction along three principal axes, each distinct from ours.

The first varies the base while fixing the classical rule. Prichett, Ludington, and Lapenta (1981) [Prichett 1981] and subsequent work by Peterson and Pulapaka (2008), Devlin and Zeng (2021), and Kay and Downes-Ward (2022, 2024) [Kay 2024] classify classical-rule fixed points and cycles across integer bases.

The second axis fixes the classical rule but varies structural properties of the fixed points. Iwasaki (2024) [Iwasaki 2024] partitions classical-rule Kaprekar fixed points across digit lengths into five disjoint sets composed of blocks drawn from $\{495, 6174, 36, 123456789, 27, 875421, 09\}$ via Diophantine constraints.

The third axis is information-theoretic. Dahl (2026) [Dahl 2026] studies classical-rule entropy contraction on coarse-grained digit-gap coordinates.

All three axes fix the classical rule and vary structural or algebraic properties of its action. Closest to our framework is the three-paper series of Nuez (2021/2022) [Nuez 2021], who develops a parametric formulation of the classical rule using symmetric-digit differences and catalogues the transformation functions acting on these parameters. Our parametric observations at the classical rule — in particular, the middle-digit cancellation at odd digit lengths (§1.1) — are special cases of Nuez's framework, and we credit him accordingly. Our axis of generalization is distinct: we fix the base at ten and vary the rule across the full space of ordered permutation pairs at each digit length, reaching $33$ universal full-variable fixed points at $d = 5$ that do not appear in any classical-rule analysis.

The systematic classification of universal full-variable fixed points at $d \leq 6$, the formulation of the cross-dimensional question in terms of permutation-pair liftings, and the proof of Theorem 3 at every $d \geq 5$ are, to our knowledge, all new.

### 1.8 Organization

§2 establishes the formal framework: permutation-pair rules, algebraic rank, universal fixed points, native digit length, and effective rank at $F$. §3 presents the exhaustive classifications at $d = 3, 4, 5, 6$. §4 proves Theorem 2 (the $d = 5 \to d = 6$ cross-check). §5 develops the coefficient-preserving lifting framework and proves Theorem 3. §6 develops the $\{7, 6, 4, 1\}$-thread and proves Theorem 4. §7 is a short discussion of open questions. Appendices A–E contain the full classification tables, the $60714$ ladder through $d = 20$, the proofs of the support lemmas, observed transcendent fixed points at $d = 7$ (non-exhaustive, honestly labeled), and the $6174$ $d = 8, 9$ audit details.
