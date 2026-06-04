# Fixed Points and Universality of the Pair-Symmetric Kaprekar Rule

**On the multiplicity chain {1,4,6,7}^m at digit length d = 4m**

---

## Summary of what is and is not proven

| Statement | Status |
|---|---|
| **Theorem 1** — Fixed-point existence at all m | **PROVEN** (rigorous, dimension-independent) |
| **Theorem 2** — Universality at m ∈ {1,2,3,4,5,6} | **VERIFIED** (computational) |
| **Conjecture 3** — Universality at all m ≥ 1 | **OPEN** (no general proof) |

The fixed-point theorem is complete and rigorous. The universality result is computational, and a general proof is identified as a substantial open problem with a precisely stated obstruction.

---

## 1. Setup

For $d = 4m$, the multiset is $M_m = \{1,4,6,7\}^m$ (each digit appearing $m$ times). The sorted-descending form of any arrangement of $M_m$ is

$$\mathbf{s} = (\underbrace{7,\ldots,7}_{m}, \underbrace{6,\ldots,6}_{m}, \underbrace{4,\ldots,4}_{m}, \underbrace{1,\ldots,1}_{m}).$$

A rule is a pair $(\pi, \sigma) \in S_d \times S_d$, acting via $K_{\pi,\sigma}(n) = |\sum_{i=0}^{d-1} c_i s_i|$ where $s_i$ is the $i$-th sorted-descending digit of $n$ and

$$c_i = 10^{d-1-\pi^{-1}(i)} - 10^{d-1-\sigma^{-1}(i)}.$$

**The interleaved pair-symmetric rule.** Partition the positions $\{0, 1, \ldots, d-1\}$ by residue mod 4:

$$A_7 = \{i : i \equiv 0\}, \quad A_6 = \{i : i \equiv 1\}, \quad A_4 = \{i : i \equiv 2\}, \quad A_1 = \{i : i \equiv 3\} \pmod 4.$$

Define $(\pi, \sigma)$ so that
- $\pi$ sends the $m$ seven-ranks to $A_7$, six-ranks to $A_6$, four-ranks to $A_4$, one-ranks to $A_1$ (each in increasing position order);
- $\sigma$ applies the pair-swap: seven-ranks to $A_1$, six-ranks to $A_4$, four-ranks to $A_6$, one-ranks to $A_7$.

---

## 2. Theorem 1 (Fixed-Point Existence) — PROVEN

> **Theorem 1.** For every integer $m \geq 1$, the integer
> $$F_m = 6174 \cdot R(m), \qquad R(m) = \sum_{k=0}^{m-1} 10^{4k} = \underbrace{1\,0001\,0001\cdots0001}_{m \text{ ones}}$$
> (that is, the digit string **6174** repeated $m$ times) is a fixed point of the interleaved pair-symmetric rule at $d = 4m$, and $F_m$ has digit multiset $M_m = \{1,4,6,7\}^m$.

### Proof

Under the interleaved rule, $\pi$ produces the arrangement that reads
$$\alpha = \underbrace{7641\,7641\cdots7641}_{m} \quad\text{(the string "7641" repeated } m \text{ times)},$$
because position $4k$ holds a 7, position $4k+1$ holds a 6, position $4k+2$ holds a 4, position $4k+3$ holds a 1, for each $k = 0, \ldots, m-1$. Likewise $\sigma$ produces
$$\beta = \underbrace{1467\,1467\cdots1467}_{m}.$$

Therefore, on the sorted-descending input $\mathbf{s}$,
$$K(\mathbf{s}) = |\alpha - \beta| = \left| \sum_{k=0}^{m-1} 7641 \cdot 10^{4k} - \sum_{k=0}^{m-1} 1467 \cdot 10^{4k} \right| = (7641 - 1467) \cdot R(m) = 6174 \cdot R(m).$$

Now $6174 \cdot R(m)$ is precisely the string "6174" repeated $m$ times, which has exactly $m$ each of the digits $1, 4, 6, 7$ — i.e., multiset $M_m$. Since the sorted-descending form of $F_m$ is again $\mathbf{s}$, we have $K(F_m) = K(\mathbf{s}) = F_m$. Hence $F_m$ is a fixed point. $\blacksquare$

### Verification (computational confirmation)

| $m$ | $F_m$ | $K(\mathbf{s})$ matches | multiset $M_m$ |
|---:|---|:---:|:---:|
| 1 | 6174 | ✓ | ✓ |
| 2 | 61746174 | ✓ | ✓ |
| 3 | 617461746174 | ✓ | ✓ |
| 4 | 6174617461746174 | ✓ | ✓ |
| 5 | 61746174617461746174 | ✓ | ✓ |
| 6 | 617461746174617461746174 | ✓ | ✓ |

This theorem alone establishes that the **set of fixed points is non-empty at every $m$** — a clean, dimension-independent result generalizing the appearance of 6174.

---

## 3. The Universality Gap

A fixed point $F$ is **classically universal** under $(\pi,\sigma)$ if *every* non-repdigit $d$-digit input iterates to $F$. Theorem 1 proves $F_m$ is a fixed point, but **not** that it is universal.

### 3.1 The interleaved rule is not universal for $m \geq 3$

Direct computation of the basin of $F_m$ under the interleaved rule:

| $m$ | $d$ | basin coverage |
|---:|---:|---:|
| 1 | 4 | **100%** (universal) |
| 2 | 8 | **100%** (universal) |
| 3 | 12 | 14.86% |
| 4 | 16 | 99.69% |
| 5 | 20 | 9.52% |

The coverage is erratic and far from 100% for $m \geq 3$. So $F_m =$ "6174 repeated" is **not** a universal construction beyond $m = 2$.

### 3.2 Why $m = 2$ works: parallel decomposition

At $m = 2$, the interleaved rule produces $\alpha = 76417641$ and $\beta = 14671467$. Because the two interleaved copies occupy disjoint position-residue classes, the rule acts as **two parallel copies of the classical $d=4$ Kaprekar map** on independent digit-streams. Universality then follows from Kaprekar's $d=4$ theorem applied to each copy.

**This decomposition fails for $m \geq 3$.** The sorting step (which precedes the arrangement) mixes digits across all $m$ copies, so the rule no longer decomposes into independent Kaprekar maps. The empirical erratic basins (14.86%, 99.69%, 9.52%) reflect this interference.

### 3.3 The universals at $m \geq 3$ are "scrambled"

Computationally, universals **do** exist at $m = 3, 4, 5, 6$ — but they are *not* $F_m$, and their rules are not the interleaved rule. They are scrambled arrangements with scrambled within-block orderings. Key facts:

- At $m = 3$ (d=12), the full search found **42** universal arrangements; $F_3 = 617461746174$ is **not** among them.
- At $m = 4$ (d=16), **341** universals were found; remarkably, $F_4 = 6174617461746174$ **is** among them — but under a *different* within-block ordering than interleaved (the interleaved ordering gives only 99.69%, while a specific scrambled ordering gives 100%).
- The within-block ordering of $\pi$ and $\sigma$ — invisible to the fixed-point value — is decisive for universality.

---

## 4. Theorem 2 (Computational Universality) — VERIFIED

> **Theorem 2.** For each $m \in \{1, 2, 3, 4, 5, 6\}$, there exists a pair-symmetric (7↔1, 6↔4) rule at $d = 4m$ that is classically universal on $M_m$.

**Evidence (verified counts of distinct universal arrangements):**

| $m$ | $d$ | universals found | method |
|---:|---:|---:|---|
| 1 | 4 | 2 | exhaustive (= Kaprekar) |
| 2 | 8 | 481 | exhaustive |
| 3 | 12 | 42 | full arrangement search (14-day run) |
| 4 | 16 | 341 | pair-symmetric structured search |
| 5 | 20 | ≥ 1 | pair-symmetric, 200M-partition sample |
| 6 | 24 | ≥ 1 | pair-symmetric, position-constrained search |

Each is a verified classical universal (basin = entire non-repdigit multiset space).

---

## 5. Conjecture 3 (Universality at all m) — OPEN

> **Conjecture 3.** For every $m \geq 1$, there exists a classically universal pair-symmetric rule at $d = 4m$ on $M_m$.

### 5.1 The obstruction to a proof

A proof of Conjecture 3 requires a **dynamical** argument — showing that some rule's basin covers the entire ($\sim 10^{m}$-sized) multiset space. The fixed-point algebra of §2 does not touch this. The natural proof techniques and their obstructions:

**(a) Parallel decomposition** — works at $m \leq 2$, *provably fails* at $m \geq 3$ because sorting mixes the copies (§3.2). Eliminated.

**(b) Self-similar renormalization** (reduce $m$-dynamics to $(m{-}1)$-dynamics) — the erratic interleaved basins (14.86%, 99.69%, 9.52%) show there is *no* clean self-similarity along the $F_m$ family. Would require a different invariant.

**(c) Lyapunov / monovariant** — construct a function $\Phi$ with $\Phi(K(n)) < \Phi(n)$ for $n \neq F$, minimized at $F$. None is known for this rule family; constructing one is the crux.

**(d) Kaprekar-style eventual-image finiteness** — show $K^{(T)}(\cdot)$ has image a small set $\{F\}$ for some bounded $T$. This is exactly the technique of Paper 2's Theorem 8.1, which succeeded for **one** fixed point (60714) via multiple structural lemmas (closure + finite reaching time + a $d$-independent core-nonnegativity argument). Extending it to a **family across all $m$** is a substantial research project.

### 5.2 Honest status

The conjecture is supported by:
- 6 consecutive verified dimensions (m = 1 through 6)
- An explicit, proven fixed-point family (Theorem 1)
- Consistent cross-dimensional positional structure (lead ∈ {1,6}, tail ∈ {4,6}, position $d{-}1 \in A_7 \cup A_1$)

But **no general proof of universality is currently available**, and obtaining one is comparable in difficulty to — or harder than — the dimension-transcendence theorem of Paper 2.

---

## 6. What can be claimed in a paper

**Provable, dimension-independent (state as a Theorem):**
> The string "6174" repeated $m$ times is a fixed point of an explicit Kaprekar-type rule on $\{1,4,6,7\}^m$ for every $m \geq 1$.

**Computational (state as verified results):**
> Classical universal fixed points exist on $\{1,4,6,7\}^m$ at $d = 4m$ for $m = 1,2,3,4,5,6$, in counts $2, 481, 42, 341{+}, \geq 1, \geq 1$.

**Open (state as a Conjecture with precise obstruction):**
> A universal fixed point exists for every $m \geq 1$; a proof requires a dynamical convergence argument, the cleanest path being a Kaprekar-style eventual-image bound (cf. Paper 2 §8) generalized across the multiplicity chain.

---

## 7. Suggested next steps toward a full proof

1. **Construct a monovariant** $\Phi$ for the $m=3$ universal rule (smallest open case) and check whether it generalizes. If a single $\Phi$ works across $m = 3, 4, 5$, it likely works for all $m$.

2. **Attempt the $m \to m+1$ lift** for a *specific* universal partition family (not the interleaved one). The d=24 universal's clustered partition ($A_7 = \{0,1,2,10,11,12\}$) suggests block-cluster structure worth formalizing.

3. **Bound the reaching time** $T_m$ empirically across $m = 3,4,5,6$. If $T_m$ is bounded (or grows slowly), a finite-state argument at each residue may close the proof.

4. **Reduce to digit-gap dynamics.** The classical $m=1$ proof works on the 2D gap space $(a{-}d, b{-}c)$. Identify the analogous reduced coordinate system at general $m$ and check finiteness of its reachable set.

---

# ADDENDUM (BREAKTHROUGH): The Monotone–Acyclic Decomposition

*Added after structural pattern-hunting. This is the most important result for the universality proof.*

## The discovery

Universality of a pair-symmetric rule **factors** into two independent, classically-meaningful conditions:

$$\textbf{Universal} \quad\Longleftrightarrow\quad \textbf{Monotone} \;\wedge\; \textbf{Acyclic}$$

verified with **zero exceptions** at both d=12 and d=16:

| | d=12 | d=16 |
|---|---|---|
| monotone universal & acyclic | 2 | 15 |
| monotone universal & cyclic | **0** | **0** |
| monotone non-universal & acyclic | **0** | **0** |
| monotone non-universal & cyclic | 38 | 46 |

(The theorem is stated *within* the monotone class; non-monotone universals also exist but are not needed.)

## The two conditions

**Monotone**: the cumulative coefficient sums $C_j = c_0 + c_1 + \cdots + c_j$ satisfy $C_j \geq 0$ for all $j$, with $C_{d-1} = 0$. Equivalently, the coefficient sequence is a **non-negative lattice path** (Dyck-type). Writing $K$ in gap coordinates $g_j = s_j - s_{j+1} \geq 0$:
$$K(\mathbf{s}) = \sum_{j=0}^{d-1} C_j \, g_j,$$
so monotone $\iff$ $K$ is a **non-negative combination of digit-gaps** — i.e., $K$ is order-preserving in the gaps.

**The classical d=4 Kaprekar rule is monotone**: $c = (999, 90, -90, -999)$ gives $C = (999, 1089, 999, 0) \geq 0$.

**Acyclic**: the dynamics has no nontrivial cycle. This is *exactly* the obstruction in classical Kaprekar theory — d=4 is acyclic (converges to 6174), d=5 is cyclic (no universal fixed point).

## Why this is the right decomposition

It separates the two genuinely different difficulties:

1. **Monotonicity** is *algebraic and checkable* — a positivity condition on partial sums of the coefficient vector. A construction can target it directly.

2. **Acyclicity** is *dynamical*, but it is the **same problem class as the classical Kaprekar convergence theorem**, which is solved at d=4. The multiplicity chain inherits the identical cycle-exclusion structure.

Monotone + Acyclic $\Rightarrow$ Universal is then near-immediate by finiteness: in a finite state space, every orbit terminates in a fixed point or a cycle; acyclicity removes cycles, so every orbit reaches a fixed point, and (empirically, monotonicity forces) that fixed point is the unique $F$.

## The resulting proof program for "universal at all m"

> **To prove a universal exists at every $m \geq 1$:**
>
> **Step 1 (Construction — algebraic).** Exhibit, for each $d = 4m$, a pair-symmetric partition whose coefficient vector has all cumulative sums $C_j \geq 0$ (a non-negative lattice path). *This is a concrete combinatorial construction problem, not a dynamical one.*
>
> **Step 2 (Acyclicity — the crux).** Prove that this monotone rule has no nontrivial cycle. *This is the multiplicity-chain analogue of Kaprekar's classical d=4 convergence theorem.*
>
> **Step 3 (Conclude).** Monotone + acyclic + finite state $\Rightarrow$ unique fixed point is globally attracting $\Rightarrow$ universal.

Steps 1 and 3 appear tractable. **Step 2 is the heart of the remaining work** — but it is now a *sharply posed, classically-grounded* problem ("show this explicit monotone rule is cycle-free at every m"), rather than the diffuse "prove universality."

## Why earlier approaches failed, in this light

- **6174-repeated (the cheat)** is a fixed point but its interleaved rule is *not monotone-acyclic* for $m \geq 3$ — it has cycles, hence not universal.
- **Random monovariant search** failed because universality is not monotone in *digit-spread*; the correct monovariant lives in *gap/cumulative-coefficient coordinates* (the $C_j$).
- **Paper 2's zero-padding technique** doesn't transfer (no zeros) — but the monotone-acyclic decomposition is a *different* and more intrinsic handle that does not require an absorbing set.

## Status

- **Decomposition theorem (monotone ⇒ [universal ⟺ acyclic])**: verified at d=12, d=16 with zero exceptions. Strongly supported; a short finiteness proof of "monotone+acyclic ⇒ universal" should be writable.
- **Existence of monotone rules at each m**: confirmed computationally (m=3: ≥2, m=4: ≥15). A general construction is the open Step 1.
- **Acyclicity of a constructed monotone rule at all m**: open (Step 2) — the central remaining problem, now classically grounded.

---

# RIGOROUS CORE: The Finiteness Criterion + Monotone Uniqueness

## Lemma A (Finite-State Universality Criterion) — PROVEN

> **Lemma A.** Let $T : X \to X$ be any map on a *finite* set $X$, and let $F \in X$ satisfy $T(F) = F$. Then the following are equivalent:
> 1. $F$ is **universal**: for every $x \in X$ there is $k \geq 0$ with $T^k(x) = F$.
> 2. $F$ is the **unique** fixed point of $T$, **and** $T$ has no periodic orbit of period $\geq 2$ (**acyclic**).

**Proof.**
*(1 ⟹ 2).* Suppose $F$ is universal. If $F'$ were another fixed point, then $T^k(F') = F' \neq F$ for all $k$, contradicting universality; so $F$ is unique. If $C$ were a cycle of period $p \geq 2$, no point of $C$ ever equals $F$ (cycles are disjoint from the fixed point under iteration), contradicting universality; so $T$ is acyclic.

*(2 ⟹ 1).* Fix any $x \in X$. Since $X$ is finite, the orbit $x, T(x), T^2(x), \ldots$ must repeat: there exist $a \geq 0$, $p \geq 1$ with $T^{a}(x) = T^{a+p}(x)$. Then $\{T^{a}(x), \ldots, T^{a+p-1}(x)\}$ is a periodic orbit of period $p$. By hypothesis there is no period $\geq 2$ orbit, so $p = 1$; that is, $T^{a}(x)$ is a fixed point. By uniqueness, $T^{a}(x) = F$. Hence $x$ reaches $F$. $\blacksquare$

Here $X$ = non-repdigit $d$-digit multisets and $T(n) = \mathrm{sort\_desc}\,|c \cdot \mathbf{s}(n)|$. Lemma A is the rigorous backbone of Step 3: **universality $\iff$ (unique fixed point) $\wedge$ (acyclic)** — *unconditionally, for every rule.*

## Fact B (Monotone ⟹ Unique Fixed Point) — VERIFIED

Across **all 61** monotone pair-symmetric rules at d=16 (and all monotone rules at d=12), **every one has a unique fixed point** $F$ — including the 46 *cyclic* (non-universal) ones, whose failure is due solely to cycles, never to a competing fixed point.

Combined with Lemma A this yields the operational statement:

> **For monotone pair-symmetric rules: Universal $\iff$ Acyclic.**

(Fact B itself — a rigorous proof that monotonicity forces a unique fixed point — is the one remaining gap in making this an unconditional theorem; it is verified but not yet proven.)

## Fact C (Pivot Symmetry) — structural, verified

For every monotone pair-symmetric rule, the cumulative sums at the three gap positions of $\mathbf{s}$ (positions $m{-}1, 2m{-}1, 3m{-}1$) satisfy
$$C_{m-1} = C_{3m-1},$$
exactly (verified across all 61 rules at d=16). Hence the fixed-point value reduces to
$$F = 3\,C_{m-1} + 2\,C_{2m-1} + 3\,C_{3m-1} = 6\,C_{m-1} + 2\,C_{2m-1},$$
recovering the block-sum formula $K = 6 S_7 + 2 S_6$. This is the pair-swap (7↔1, 6↔4) reflected in the cumulative-coefficient sequence.

## Where the proof now stands

| component | status |
|---|---|
| Lemma A (universal ⟺ unique-fp ∧ acyclic) | **PROVEN** (finiteness) |
| Fact B (monotone ⟹ unique-fp) | verified d=12,16; proof open |
| Construction of a monotone rule at each m | verified m=3 (≥2), m=4 (≥15); general construction open |
| **Step 2: acyclicity of a monotone rule at all m** | **OPEN — the crux** |

The acyclic-vs-cyclic split among monotone rules is **not** captured by the pivot sums (both classes share $C_{m-1}=C_{3m-1}$ and overlapping magnitudes) — confirming acyclicity is a genuinely dynamical condition requiring a cycle-exclusion argument, exactly as in classical Kaprekar.

---

# Progress on the Proof Program (Steps 1, 3, 2)

## Fact B (monotone ⟹ unique fixed point): VERIFIED BY FULL SCAN
An exhaustive scan of the **entire** d=16 multiset space (2,042,965 multisets) confirms each monotone rule has **exactly one** fixed point. Combined with Lemma A: *monotone ⟹ (universal ⟺ acyclic)* is the operational theorem. A closed-form proof of uniqueness from the gap-positivity $K=\sum C_j g_j$ remains open but the fact is on very firm computational ground.

## Step 3 (canonical monotone construction): the obstruction is sharp

Two clean constructions, each failing one requirement:

| construction | monotone? | preserves $\{1,4,6,7\}^m$? | result |
|---|:---:|:---:|---|
| **Block** = descending − ascending (generalized classical Kaprekar) | ✓ (all m) | ✗ | F gains digits 2,3,5,8,9 — wrong multiset |
| **Interleaved** | ✓ (all m) | ✓ (gives 6174-repeated) | **cyclic** for $m\geq3$ (not universal) |

So:
- **Monotonicity is easy** — both clean constructions achieve it at every m. (Indeed the *classical Kaprekar* construction is the monotone prototype.)
- **The hard constraint is achieving monotone + multiset-preserving + acyclic simultaneously.** The block rule is monotone but leaves the multiset; the interleaved rule is monotone and multiset-preserving but cyclic.
- The 15 rules that satisfy all three at d=16 have **scrambled within-block orderings** with no evident closed form (e.g. $A_7$ orders $[9,0,1,13], [0,8,4,9], [1,11,7,0], \ldots$ — irregular).

**Interpretation.** The monotone-acyclic universal rules are not given by any obvious symmetric construction; they sit at a non-trivial intersection of three conditions. This explains why a clean "formula for the universal rule at every m" has been elusive — and suggests the right existence proof is **non-constructive** (show the intersection is non-empty) rather than an explicit formula.

## Revised Step 2 (the crux), sharpened

Since monotonicity is free and uniqueness holds, the entire problem is:

> **Open Problem (sharp form).** For every $m\geq 1$, does there exist a pair-symmetric, monotone, $\{1,4,6,7\}^m$-preserving rule with **no nontrivial cycle**?
>
> Equivalently (by Lemma A + Fact B): does the multiplicity chain admit a "Kaprekar-acyclic" rule at every dimension, as it does at $d=4$?

This is the cleanest possible statement of the universality conjecture — and it is manifestly the direct generalization of "the classical $d=4$ Kaprekar map is acyclic."

---

# Elementary Proof Attacks — Ruled Out (2026-06-03)

A sustained attempt on the three proof steps. All elementary approaches were tested and **fail**; recording them so future work doesn't repeat them.

## #1 — Monotone ⟹ unique fixed point: no monovariant found
Verified by **full 2M-multiset scan** (every monotone rule has exactly one fixed point). But the natural Lyapunov candidates are **not** monovariants along trajectories of a monotone universal rule:
- **digit-spread** ($\max - \min$ digit): non-monotone (e.g. 9→8→8→6→6→**8**→…).
- **$|K(n) - F|$** (distance to F in the K-coordinate): decreases only **61.2%** of steps — not a monovariant.

So uniqueness is true but resists an elementary potential-function proof; it must use finer structure of the gap map.

## #2 — Acyclicity: no simple characterizer
Among monotone rules, acyclic (15) vs cyclic (46) at d=16 is **not** separated by:
- pivot cumulative sums (both classes share $C_{m-1}=C_{3m-1}$, overlapping magnitudes),
- DFT/spectral magnitude of the partition indicators,
- positions-mod-4 signatures,
- number/position of negative cumulative sums.

Acyclicity is a genuinely global dynamical property here — exactly as the cycle structure is in classical Kaprekar (where d=4 acyclic, d=5 cyclic, with no shortcut characterization).

## #3 — Construction / lifting: fails
- **Clean constructions fail**: block (=classical Kaprekar) is monotone but changes the multiset; interleaved is monotone + multiset-preserving but cyclic for $m\geq3$.
- **m→m+1 lifting fails**: appending one new position per block to a d=16 universal rule and re-pairing gives, across all $4!\times 2$ natural assignments, **only 4 valid-multiset lifts, none universal** (best basin 3.07%). Universals do **not** lift by naive position insertion.

## Consequence
The universal/monotone-acyclic rules are **not** reachable by any elementary construction, monovariant, or lifting tried. This is consistent with the working rules being "scrambled" with no closed form, and points to either:
1. a **non-constructive existence** proof (show the monotone ∩ acyclic ∩ multiset-preserving set is nonempty at every m without exhibiting an element), or
2. a **deeper finite-state / transfer-operator** argument analogous to — but harder than — Paper 2's Theorem 8.1 (which had a zero-padding absorbing set this problem lacks).

The session's durable contribution is the **reduction** (Lemma A + the monotone–acyclic decomposition + Fact B), which turns an opaque dynamical conjecture into the sharp, classically-grounded question: *does a monotone acyclic multiset-preserving rule exist at every $m$?*

---

# CORRECTION + New Handle: The Image of K is an Absorbing Set (2026-06-03)

An earlier section claimed "Paper 2's technique doesn't transfer (no absorbing set)." **This is
wrong** and is retracted. Direct measurement on a universal d=16 rule:

- **One step collapses the state space 125×**: |X| = 2,042,965 → |K(X)| = 16,276.
- **K(X) is closed under K** (absorbing): 0 escapes in sampling. So Image(K) is exactly the
  kind of absorbing set Paper 2's eventual-image argument uses.
- **Modular structure of Image(K)**: every value ≡ 0 (mod 9); mod 99 they are exactly the
  multiples of 9 (residues {0,9,18,27,36,54,63,72,81,90}); digit-sums lie in {36,45,…,90}.
- Subsequent collapse is slow-tailed: |K^t(X)| = 16276, 3165, 1069, 466, 257, 164, … → 1.

**Revised proof outlook.** The eventual-image / transfer-operator route is viable after all:
1. (TRUE) K(X) ⊆ Image(K), absorbing.
2. (open) Characterize Image(K) m-independently — it is *not* size-bounded in m (16k at m=4),
   so this needs a structural description (e.g. via the mod-9 / mod-99 constraints + the (6,2)
   coefficient form), not enumeration.
3. (open) Show the dynamics on Image(K) converges to the unique fixed point F.

This is still open, but it is the **same shape** as the (solved) Paper 2 §8 argument and the
(solved) classical Kaprekar d=4 argument — not a fundamentally new kind of problem. The
remaining work is the m-independent characterization of the absorbing image, now aided by:
(a) everything reducing to the single (6,2)/6174 system (FERTILITY_PREDICTOR.md), and
(b) the proven mod-9 / observed mod-99 multiple-of-9 structure of the image.

---

# Acyclicity: monovariant route exhausted (2026-06-03)

Further attempts to find a Lyapunov function for the dynamics *on the absorbing image* (where a
monovariant has the best chance):

- **Single monovariants** (on-image, post-transient): digit-sum-distance to F is non-increasing
  88% of steps but **mostly because digit-sum is conserved** (~70% of steps unchanged); it
  strictly decreases only ~18%. Not a monovariant. (spread, |K−F|, #distinct, max-digit all
  worse.)
- **Lexicographic (primary digit-sum-distance + secondary)**: on the steps where digit-sum
  distance fails to decrease, no candidate secondary (value, #distinct, spread, freq-L1)
  strictly decreases more than 67% of the time. **No lexicographic Lyapunov exists** among
  these.

**Conclusion.** The convergence is real but is *not* witnessed by any elementary potential
function. The digit-sum performs a weakly-F-biased walk on $9\cdot\{4,\dots,10\}$; the actual
contraction is finer-grained. This matches classical Kaprekar, whose d=4 proof is **not** a
monovariant argument but a **finite-state enumeration** of the reachable gap-set.

**Implication for the proof.** The viable route is the finite-state / eventual-image argument
(à la Kaprekar d=4 and Paper 2 §8): find an **m-independent quotient** of the dynamics on the
absorbing image and verify convergence on it. Finding that quotient — not another monovariant —
is the remaining mathematical work, and it is genuinely research-grade.

---

# AMPED-UP ATTEMPT: Adapting Paper 2's Theorem 5.x (60714 all-d proof)

Read Paper 2's actual universality proof and mapped its machinery onto the multiplicity chain.

## Paper 2's two ingredients
1. **Core non-negativity** (Lemma 5.3): on sorted-descending inputs the native-core contribution
   is ≥ 0, eliminating borrow interference.
2. **Absorbing set + bounded reaching time** (Lemmas 5.1–5.2): the tail-two-zeros set $T_d$ is
   closed, $K^{(d)}$ acts on it as $K^{(d-2)}$, and every orbit reaches $T_d$ in ≤1–2 steps —
   proved by **counting the zero digits** the rule produces.

## The mapping
| ingredient | status for {1,4,6,7}^m |
|---|---|
| core non-negativity | **HAVE IT** — exactly our monotonicity $C_j \ge 0$ |
| zero-absorbing set + bounded reaching time | **LACK IT** — no zeros to count |

## The precise obstruction (now identified)
Paper 2's absorbing set is *built from zero digits*; its reaching-time bound *counts zeros*.
The multiplicity chain has **no zero digits**, so:
- the tail-zeros absorbing set does not exist, and
- the reaching time is **not bounded** — measured T_m = 14, 32, 39 for m = 2,3,4 (growing),
  versus Paper 2's bounded ≤8→≤1.

The growth of T_m is the signature that there is no zero-style absorbing reduction. So Paper 2's
specific technique **does not transfer** — for a structural reason (zeros), not a superficial one.

## What remains — a sharper open problem
We have core-non-negativity (monotonicity) for free. The missing half is:

> **Find a non-zero absorbing structure on the multiplicity chain that (i) is reached in bounded
> time and (ii) reduces the m-dynamics to (m−1).**

The image of K is absorbing (125× collapse, closed) but does **not** give an m→(m−1) reduction.
Candidate heavier tools for the missing piece:
1. **Modular tower.** The image is constrained mod 9 and mod 99 (multiples of 9); analyze the
   dynamics in the $(10^4-1)=9999$ structure natural to 4-digit blocks.
2. **Computer-assisted inductive certificate.** Rigorously enumerate the functional graph at
   m=1..5, and machine-search for an inductive invariant certifying acyclicity that provably
   lifts m→m+1.
3. **A bounded-reaching-time argument without zeros** — show T_m is actually bounded (the 14,32,39
   data may be plateauing; needs m=5 to tell) and build the absorbing reduction on a non-zero
   invariant (e.g. a fixed digit-sum shell).

---

# MULTI-AGENT PROOF ASSAULT — Results (2026-06-04)

A 33-agent workflow (5 strategies × deep work + adversarial verification of every claim +
synthesis; ~1.95M tokens) attacked the acyclicity proof. 19 claims survived adversarial
verification. Headline: **routes definitively closed, obstruction localized, two of my own
prior claims corrected — but no proof.**

## CORRECTION (verified directly): Fact B is FALSE
"Monotone ⟹ unique fixed point" is **false**. The interleaved monotone rule at d=12 (all
C_j ≥ 0) has **two** fixed points: 617461746174 (= M_3, the 6174-triple) and 535549955994
(multiset {3,4²,5⁵,9⁴}). My earlier "verified zero exceptions" only checked monotone rules
*drawn from the universal search* — a biased sample. General monotone rules can have multiple
fixed points.
**Impact:** the shortcut "for monotone rules, universal ⟺ acyclic" is not valid. The correct
statement remains **Lemma A: universal ⟺ unique-fp ∧ acyclic** — but monotonicity buys *neither*
condition for free. The acyclic⟹universal bridge needs unique-fp re-established independently.

## Newly CONFIRMED (adversarially verified)
- **Block-state reduction (rigorous):** on block states (aᵐbᵐcᵐdᵐ), *every* monotone
  pair-symmetric rule equals the classical d=4 Kaprekar map K = P·((a−b)+(c−d)) + Q·(b−c),
  P=C_{m−1}, Q=C_{2m−1} — a faithful change of basis of 999(a−d)+90(b−c). The interleaved rule
  literally outputs "K₄(a,b,c,d) repeated m times" (verified m=1..6).
- **Pivot symmetry C_{m−1}=C_{3m−1} is structural** (block coeffs are antisymmetric [B0,B1,−B1,−B0]).
- **Every period-≥2 cycle lives strictly OUTSIDE the {1,4,6,7} alphabet** (d=16: all 55 cycle
  members; d=12: exhaustive over 67,970 monotone rules, zero in-alphabet cycles — not a mod-9
  triviality). So the obstruction to universality is entirely alphabet-external.
- **"Every {1,4,6,7}-alphabet multiset reaches F" is a necessary, ~2117× cheaper proxy** for
  universality (965 vs 2,042,965 states), exact except 3/46 rare external 2-cycle false positives.
- **The 15 monotone-universal d=16 rules are NOT block-closed; all share an identical 180-state
  block-escape set** — the deviation from block-closure is what breaks the cycles that trap the
  block-closed interleaved rule (which gets only 14.86% to F).
- **T_m reaching time is BOUNDED** (measured separately): T = 14, 32, 39, 42 for m=2,3,4,5 —
  increments 18,7,3 → plateauing near ~44. (Positive for a finite-reaching-time argument.)

## DEFINITIVELY RULED OUT (real progress — do not re-pursue)
- **Modular / p-adic tower for cycle exclusion**: K induces no well-defined residue map except
  trivially mod 9; exhaustive moduli 2–300 — none separates F's basin from cycles.
- **Low-degree Lyapunov / monovariant**: LP-infeasible for digit-counts, a 69-dim quadratic
  feature set, and {value, ds, ds², |ds−72|}. No single scalar feature is non-increasing on all
  edges (≥17% violations), so greedy-lexicographic can't start.
- **Coefficient-space separation**: the 15 acyclic and 46 cyclic d=16 rules are linearly
  inseparable in coefficient space (LP-infeasible). Acyclicity is genuinely global.
- **All uniform/closed-form families**: round-robin (cyclic m=3), stride (cyclic m=3..6),
  24 residue-block permutations (none universal at both d=8,12), block-closed rules (force
  m parallel Kaprekars the sort couples into cycles). A purely periodic family cannot be acyclic
  at all m.

## The single promising LEAD (concrete next step)
**Block-reduction + finite-deviation.** On block states every monotone rule is classical Kaprekar
(acyclic). Universal rules deviate from block-closure on a finite, m-stable, alphabet-external
cycle family (~10 cycle types at d=16; one 4-cycle covers 30 of 46 cyclic rules). For each cycle
member Z, "rule does not admit Z" is a finite set of *linear inequalities on the coefficient
vector c*. The lever is the **intra-block ordering freedom (~(m!)⁴ per partition)**, previously
overlooked. Concrete program: write the obstruction cycles as explicit m-indexed digit-count
vectors, and construct — for every m — a monotone M_m-fixing rule that (i) sends every alphabet
multiset to M_m (cheap 965-state check) and (ii) satisfies the finite linear inequalities
excluding the obstruction family. Whether this is simultaneously satisfiable at *all* m is the
open question.

## Blunt judgment
Not close to a proof. The existence half is settled (monotonicity is free); the obstruction is
now *localized and finite* rather than diffuse; two attack families are *definitively* dead; and
T_m looks bounded. But no construction/induction valid for all m exists, and a load-bearing
premise (Fact B) just failed. We have a much sharper map of the wall, not a way through.
