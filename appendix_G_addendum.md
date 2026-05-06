---

# Appendix G. Classical-scope correction and confirmation of the cycle thread at $`m = 4`$

*Status: Preliminary working notes added May 4–5, 2026. This appendix reports
four findings developed after release of paper version 1.2.1: a methodological
correction to the universality definition, re-verification of the paper's
results under the corrected definition, empirical confirmation that the cycle
thread continues to $`m = 4`$, and a refinement of the conjecture's lift
mechanism.*

*None of the corrections invalidate prior results in the paper. They strengthen
and extend them.*

## G.1 Purpose

The original verifier in this paper tested universality against an
$`S`$-restricted input basin — that is, the set of non-repdigit $`d`$-digit
multisets whose digits lie in the alphabet $`S = \{0, 1, 4, 6, 7\}`$. This
restriction was inherited from the search infrastructure originally designed
to *find* fixed points (whose digits naturally lie in $`S`$) but was
inadvertently applied to *test* universality.

Classical Kaprekar universality, as the term is conventionally used in the
literature on the digit-rearrangement function
$`K(n) = \mathrm{sort\_desc}(n) - \mathrm{sort\_asc}(n)`$, requires the basin
of $`K`$-iteration to include every non-repdigit $`d`$-digit input — that is,
all multisets of digits drawn from $`\{0, 1, \ldots, 9\}`$ except repdigits.

This appendix (a) clarifies the distinction, (b) re-verifies the paper's
results under the corrected definition, and (c) reports new empirical results
that extend the cycle thread to $`m = 4`$.

## G.2 Strict $`K`$-rules and classical universality

Throughout the paper, a $`K`$-rule at dimension $`d`$ is a pair
$`(\pi, \sigma)`$ of permutations of $`\{0, 1, \ldots, d-1\}`$ giving the
coefficient vector
$`c[i] = 10^{d-1-\pi^{-1}[i]} - 10^{d-1-\sigma^{-1}[i]}`$ for
$`i = 0, \ldots, d-1`$. The map $`K_{\pi, \sigma}`$ is then defined on a
multiset $`m_0 \geq m_1 \geq \cdots \geq m_{d-1}`$ by
$`K(m) = \left|\sum_i c[i]\, m_i\right|`$.

We restate the technical conditions used throughout the paper, with terminology
pinned down as follows.

***Definition G.1*** *(strict $`K`$-rule).* A $`K`$-rule $`(\pi, \sigma)`$ at
dimension $`d`$ is *strict* if $`c[i] \neq 0`$ for every
$`i \in \{0, \ldots, d-1\}`$. Equivalently, $`\pi^{-1}[i] \neq \sigma^{-1}[i]`$
at every position. A non-strict rule is *deficient*: some position contributes
nothing to $`K(m)`$.

***Definition G.2*** *(strict universal).* A fixed point $`F`$ at dimension
$`d`$ is a *strict universal* if there exists a strict $`K`$-rule
$`(\pi, \sigma)`$ such that $`K(F) = F`$ and every $`S`$-admissible
non-repdigit $`d`$-digit multiset converges to $`F`$ under iteration of
$`K_{\pi, \sigma}`$.

***Definition G.3*** *(classical universal).* A fixed point $`F`$ at dimension
$`d`$ is a *classical universal* if there exists a strict $`K`$-rule under
which every non-repdigit $`d`$-digit multiset (digits drawn from
$`\{0, 1, \ldots, 9\}`$) converges to $`F`$.

***Definition G.4*** *(genuinely $`S`$-only).* A strict universal $`F`$ is
*genuinely $`S`$-only* if no strict $`K`$-rule for $`F`$ is classical-universal.
The terminology emphasizes that the property is intrinsic to $`F`$, not an
artifact of which rule was sampled in the search.

Every classical universal is a strict universal. The converse may fail: a
strict universal may be genuinely $`S`$-only. The two notions agree at $`d = 4`$
but diverge at higher $`d`$ in a small minority of cases, as documented below.

## G.3 Re-verification of v1.2.1 results under classical scope

A classical-scope verifier (described in §G.7 below) was applied to the strict
universals catalogued in the paper. The results are summarized in Table G.1.

***Table G.1.*** *Re-verification of the paper's published universal counts in
classical scope.*

| Dimension | Strict universals (paper v1.2.1) | Classical universals | Genuinely $`S`$-only |
|---|---:|---:|---:|
| $`d = 4`$ | $`2`$ | $`2`$ ($`100\%`$) | $`0`$ |
| $`d = 5`$ | $`33`$ | $`33`$ ($`100\%`$) | $`0`$ |
| $`d = 6`$ | $`506`$ | confirmed; classical | $`0`$ known |
| $`d = 8`$, $`m = 2`$ | $`481`$ | $`\mathbf{465}`$ ($`96.7\%`$) | $`\mathbf{16}`$ ($`3.3\%`$) |
| $`d = 12`$, $`m = 3`$ | $`55`$ | $`\mathbf{46}`$ ($`83.6\%`$) | $`\mathbf{9}`$ ($`16.4\%`$)\* |

\* *Upper bound: the $`d = 12`$ file recorded one $`K`$-rule per $`F`$. With
multi-rule census (as performed at $`d = 8`$, where $`64\%`$ of single-rule
"S-only" universals admit a different rule that is classical), the genuine
$`S`$-only count at $`d = 12`$ is expected to be lower.*

The $`16`$ genuinely $`S`$-only universals at $`d = 8`$, $`m = 2`$ exhibit a
striking pairing structure: they pair into multiset siblings, with each pair
sharing the same digit multiset and differing by a digit transposition. For
example: $`16464717`$ and $`16446717`$; $`61771446`$ and $`61477146`$;
$`66177144`$ and $`66147714`$. The pattern is consistent with the genuinely
$`S`$-only universals being structurally related rather than scattered. Their
basin coverage in classical scope ranges from $`99.1\%`$ to $`99.9\%`$ — the
missed inputs converge to alternative fixed points whose digit multisets lie
outside $`S`$ (typically containing digits $`2`$, $`3`$, $`5`$, $`8`$, or $`9`$).

The principal result of the paper — that $`60714`$ admits a coefficient-
preserving lifting universal on $`A_d \setminus E_d`$ at every $`d \geq 5`$ —
is unchanged under the classical-scope correction. All $`60714`$ ladder
universals are classical-universal at every tested
$`d \in \{5, 6, 7, 8, 9, 10, 11\}`$.

## G.4 Confirmation of the cycle thread at $`m = 4`$

A search at $`d = 16`$, $`m = 4`$ (multiset $`\{7^4, 6^4, 4^4, 1^4\}`$) was
conducted using the candidates predicted by inserting a $`\{7, 6, 4, 1\}`$
block into known $`d = 12`$, $`m = 3`$ universals. The search produced
$`5`$ strict universals from $`9{,}426`$ candidates passing
distribution-alternation and density filters. Two of these are
classical-universal:

***Theorem G.1*** *(empirical, $`d = 16`$, $`m = 4`$).* The fixed points

$$F_1 = 6{,}471{,}467{,}417{,}167{,}416, \qquad F_2 = 6{,}467{,}717{,}446{,}711{,}614$$

are each absorbed by every non-repdigit $`16`$-digit multiset under their
respective strict $`K`$-rules. Total basin: $`2{,}042{,}965`$ multisets;
iteration count for $`F_1`$: minimum $`1`$, maximum $`50`$, mean $`25.9`$.

The remaining three strict universals at $`d = 16`$, $`m = 4`$ are genuinely
$`S`$-only:

$$\{\,6{,}474{,}646{,}711{,}711{,}476;\ \ 6{,}467{,}714{,}467{,}117{,}416;\ \ 6{,}467{,}716{,}714{,}471{,}146\,\}$$

with classical basins of $`2{,}042{,}708`$, $`2{,}042{,}903`$, and
$`2{,}041{,}321`$ respectively. Each loses a small fraction of inputs
($`62`$ to $`1{,}644`$ multisets out of $`2{,}042{,}965`$) to alternative
fixed points whose digit multisets lie completely outside $`S`$. The
alternative fixed points include $`F' = 6{,}576{,}637{,}809{,}610{,}377`$
(multiset $`\{0^3, 1, 3, 5, 6^3, 7^3, 8, 9\}`$) and
$`F' = 6{,}468{,}613{,}468{,}216{,}515`$ (multiset containing digits
$`\{1^3, 2, 3, 4^2, 5^2, 6^4, 8\}`$).

Combined with the paper's existing results at $`m = 1, 2, 3`$, this confirms
that the cycle thread $`\{7^m, 6^m, 4^m, 1^m, 0^k\}`$ at $`d = 4m + k`$
produces classical universals at every tested $`m \in \{1, 2, 3, 4\}`$.

## G.5 Asymmetric lift behavior

Two cross-dimensional lift mechanisms were tested at the
$`d = 15 \to d = 16`$ and $`d = 12 \to d = 16`$ transitions. The mechanisms
behave differently:

**Family B** *(zero-insertion lift).* Predictions generated by inserting a
single zero into the multiset of a known $`d = 15`$, $`m = 3`$, $`k = 3`$
universal, yielding $`d = 16`$, $`m = 3`$, $`k = 4`$ candidates. A Mac search
of $`731`$ candidates produced **$`0`$ strict universals** and $`0`$
algebraic $`K`$-fixed points.

**Family D** *(block-$`\{7, 6, 4, 1\}`$-insertion lift).* Predictions
generated by inserting a length-$`4`$ block at various positions in
$`d = 12`$, $`m = 3`$ universals, yielding $`d = 16`$, $`m = 4`$ candidates.
A Mac search of $`9{,}426`$ filter-passing candidates produced **$`5`$ strict
universals**, of which $`2`$ are classical-universal (Theorem G.1 above).

The asymmetry refines the cycle conjecture's interpretation. The conjecture
predicts that the multiset $`\{7^m, 6^m, 4^m, 1^m, 0^k\}`$ at
$`d = 4m + k`$ contains classical universals; it does not predict that those
universals are obtained by lifting universals from lower dimensions. None of
the $`5`$ universals at $`d = 16`$, $`m = 4`$ is the literal block-insertion of
a known $`d = 12`$, $`m = 3`$ universal; rather, they are independently
algebraic objects whose existence the block-lift heuristic correctly *predicts
the existence of* (without identifying the specific arrangements).

The Family B negative result confirms that zero-insertion lifts do not produce
universals as a generic mechanism. Apparent zero-insertion successes at lower
dimensions (e.g., the $`60714`$ ladder) succeed via coefficient-preserving
algebra, not via simple structural insertion.

## G.6 Distribution-alternation as a candidate filter

The distribution-alternation conjecture (paper §F.5) states that universal
$`F`$ values satisfy specific alternation patterns in their decimal digits. We
tested this as a *predictive* filter at $`d = 16`$, $`m = 4`$.

Of the $`9{,}426`$ candidates passing the distribution-alternation filter
(density $`\geq 0.75`$ and no Kaprekar-long-runs), $`5`$ produced strict
universals. Of the candidates *failing* the filter, none were tested (by
design), so we cannot rule out additional universals among the $`3{,}229`$
filtered-out candidates.

Among the $`5`$ universals discovered:

- $`1`$ is in the high-density (density $`= 1.0`$) bucket of $`1{,}536`$
  candidates: $`0`$ of $`1{,}536`$ universals — i.e., the high-confidence
  prediction returned $`0`$ universals.
- $`1`$ is in the medium-confidence bucket of $`2{,}220`$ candidates:
  $`1`$ of $`2{,}220 = 0.045\%`$.
- $`4`$ are in the low-confidence bucket of $`5{,}670`$ candidates:
  $`4`$ of $`5{,}670 = 0.071\%`$.

This distribution is inverted from what the filter's confidence rankings
predicted. The fine-grained predictor (density $`= 1.0`$, no
Kaprekar-long-runs) did not identify a single universal at $`d = 16`$,
$`m = 4`$. The four lower-density universals show $`F`$-arrangements with
adjacent same-digit runs of length $`2`$, contradicting the perfect-alternation
hypothesis at this dimension.

We restate the predictor's empirical status:

- **Cell-level**: the cycle conjecture correctly identifies *which multisets*
  host universals at every $`m`$ tested.
- **$`F`$-level within a cell**: the distribution-alternation filter is
  necessary (almost all universals satisfy it) but only $`\sim 0.05\%`$
  specific (most filter-passing $`F`$ values are not universal).
- **Fine-grained**: the conjunction "density $`= 1.0`$ + no Kaprekar-long-runs"
  is *not* a positive predictor at $`d = 16`$. The tightest signature
  predicted no universals; the actual universals appeared in less-restrictive
  buckets.

The conjecture's existence claim is supported. The conjecture's predictive
content for individual $`F`$ values requires further work.

## G.7 Methods note: classical-scope verification

Three scripts were developed for the corrected verification:

1. `audit_full_basin.py` — given a single $`(F, \pi^{-1}, \sigma^{-1})`$,
   iterates $`K`$ from every non-repdigit $`d`$-digit multiset and reports
   whether $`F`$ is a classical universal. Caching makes this fast: at
   $`d = 16`$, the full basin of $`2{,}042{,}965`$ multisets is processed in
   approximately $`13`$ seconds on a 2026-vintage laptop.

2. `reverify_classical_all_rules.py` — given a JSON of $`(F, \mathrm{rule})`$
   pairs, classifies each $`F`$ as classical, genuinely $`S`$-only, or partial.
   For each $`F`$, all available strict rules are tested before declaring
   genuinely $`S`$-only.

3. `verify_d16_familyD_classical.py` — corrected production verifier for new
   searches, using full-basin scope rather than $`S`$-restricted scope.

The scripts are pure-stdlib Python, fully self-contained, and reproducible.
They are deposited at the project's GitHub repository alongside the released
paper.

## G.8 Open questions raised by this appendix

1. **$`F`$-level prediction within a cell.** What property distinguishes the
   $`5`$ strict universals from the other $`9{,}421`$
   distribution-alternation-passing candidates at $`d = 16`$, $`m = 4`$?
   Cycle structure does not separate them; density does not;
   Kaprekar-long-runs does not.

2. **Why the high-density predictor failed at $`d = 16`$.** The conjecture's
   tightest signature (density $`= 1.0`$, no Kaprekar-long-runs) returned zero
   universals at $`d = 16`$, $`m = 4`$, while less-restrictive buckets
   returned all five. What changes between $`d = 12`$ (where the
   high-density signature held) and $`d = 16`$ (where it does not)?

3. **Characterization of the $`16`$ genuinely $`S`$-only universals at
   $`d = 8`$, $`m = 2`$.** They pair into multiset siblings. What algebraic
   property generates the pairing? Are they explained by a single mechanism
   distinct from the classical-universal majority?

4. **Whether the cycle thread is specific to the digit set
   $`\{1, 4, 6, 7\}`$.** Independent searches in other digit sets are in
   progress. Preliminary results (forthcoming) suggest that at least one
   other digit set produces classical universals at $`m = 2`$, with the
   $`\{1, 4, 6, 7\}`$ thread being notably denser at small $`m`$.

5. **Alternative attractors absorbing the missing inputs of genuinely
   $`S`$-only universals.** At $`d = 16`$, the $`3`$ genuinely $`S`$-only
   universals lose inputs to fixed points like
   $`6{,}576{,}637{,}809{,}610{,}377`$ whose digits include
   $`\{0, 3, 5, 7, 8, 9\}`$. Are these alternative fixed points themselves
   universals over their own multisets? This is testable.

## G.9 Acknowledgments

The classical-scope correction was identified during ongoing work in
2026-05. The scope error and the corrected definitions are reported here for
the first time.

The Mac runs reported in this appendix were performed on a 2026 Apple Silicon
laptop using pure-Python implementations of $`K`$-iteration with caching,
totaling approximately $`9`$ hours of compute time (Family D verifier:
$`7.9`$ hours; reverification of $`d = 8, 12, 16`$ universals: $`1.0`$ hour
combined).

---

*End of Appendix G.*

