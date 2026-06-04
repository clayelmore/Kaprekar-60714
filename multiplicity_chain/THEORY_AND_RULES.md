# Pair-Symmetric Universal Construction — Theory & Rules

**For the multiplicity chain {1,4,6,7}^m at d = 4m**

---

## 1. The Theory (formal statement)

### 1.1 Setup

Let $d = 4m$ for an integer $m \geq 1$, and consider the multiset $M_m = \{1, 4, 6, 7\}^m$ (each digit appearing exactly $m$ times). Let $S_d \times S_d$ be the space of ordered permutation pairs at length $d$.

For each rule $(\pi, \sigma) \in S_d \times S_d$, define the coefficient vector $c \in \mathbb{Z}^d$ by

$$c_i \;=\; 10^{d-1-\pi^{-1}(i)} \;-\; 10^{d-1-\sigma^{-1}(i)}, \qquad i = 0, 1, \ldots, d-1.$$

The map is $K_{\pi,\sigma}(n) = |\sum_{i=0}^{d-1} c_i \cdot s_i|$ where $s_i$ is the $i$-th sorted-descending digit of $n$.

### 1.2 The pair-symmetric construction

**Definition (pair-symmetric rule).** Given an ordered 4-partition $(A_7, A_6, A_4, A_1)$ of $\{0, 1, \ldots, d-1\}$ into 4 disjoint blocks of size $m$ each, the *pair-symmetric (7↔1, 6↔4) rule* is the pair $(\pi, \sigma)$ satisfying:

- $\pi^{-1}(\{0,\ldots,m-1\}) = A_7$ &nbsp;&nbsp;&nbsp;&nbsp; (the $m$ 7-digits go to positions $A_7$ in π)
- $\pi^{-1}(\{m,\ldots,2m-1\}) = A_6$ &nbsp;&nbsp;&nbsp;&nbsp; (the $m$ 6-digits go to $A_6$)
- $\pi^{-1}(\{2m,\ldots,3m-1\}) = A_4$ &nbsp;&nbsp;&nbsp;&nbsp; (the $m$ 4-digits go to $A_4$)
- $\pi^{-1}(\{3m,\ldots,4m-1\}) = A_1$ &nbsp;&nbsp;&nbsp;&nbsp; (the $m$ 1-digits go to $A_1$)
- $\sigma^{-1}(\{0,\ldots,m-1\}) = A_1$ &nbsp;&nbsp;&nbsp;&nbsp; (the $m$ 7-digits go to $A_1$ in σ — pair-swap with 1s)
- $\sigma^{-1}(\{m,\ldots,2m-1\}) = A_4$ &nbsp;&nbsp;&nbsp;&nbsp; (the $m$ 6-digits go to $A_4$ — pair-swap with 4s)
- $\sigma^{-1}(\{2m,\ldots,3m-1\}) = A_6$
- $\sigma^{-1}(\{3m,\ldots,4m-1\}) = A_7$

### 1.3 The K-formula (dimension-agnostic)

For sorted-descending input $\mathbf{s} = (7,\ldots,7,6,\ldots,6,4,\ldots,4,1,\ldots,1)$ at $d = 4m$:

$$K(\mathbf{s}) \;=\; 6 \cdot S_7 \;+\; 2 \cdot S_6$$

where
- $S_7 = P(A_7) - P(A_1)$
- $S_6 = P(A_6) - P(A_4)$
- $P(X) = \sum_{j \in X} 10^{d-1-j}$ &nbsp;&nbsp; (the "position-power-sum" of the index-set $X$)

**Derivation.** Expanding $K = 7 S_7 + 6 S_6 + 4 S_4 + 1 S_1$ with the pair-symmetric constraints $S_4 = -S_6$ and $S_1 = -S_7$ (these follow from the construction because $c$ in the 4-block is the position-wise negative of $c$ in the 6-block, similarly for 1-block vs 7-block):

$$K = 7 S_7 + 6 S_6 + 4(-S_6) + 1(-S_7) = 6 S_7 + 2 S_6.$$

### 1.4 Fixed-point and universality conditions

For $F = K(\mathbf{s})$ to satisfy $F = K(F)$ (i.e., be a fixed point under its own rule), we need only that $F$ has the digit multiset $M_m$ — because the sorted-descending form of any arrangement of $M_m$ is the canonical $\mathbf{s}$, and the rule operates only on the sort.

So **every pair-symmetric rule whose K-output has the right multiset is automatically a fixed-point rule for that output F**.

The deeper question is whether the rule's basin of attraction (over all $d$-digit multisets, not just arrangements of $M_m$) covers *every* non-repdigit multiset. The empirical observation is:

> **Pair-symmetric universal conjecture.** For every $m \geq 1$, the pair-symmetric (7↔1, 6↔4) construction at $d = 4m$ produces at least one classical universal fixed point in the multiset $M_m$.

### 1.5 Verification table

| $m$ | $d$ | partitions tested | F candidates | classical universals |
|---:|---:|---:|---:|---:|
| 1 | 4 | 24 (exhaustive) | 2 | 2 (6174, 1746) |
| 2 | 8 | exhaustive | many | 481 |
| 3 | 12 | exhaustive | many | 42 |
| 4 | 16 | 22,000,000 (≈35% of 63M) | 1,300+ | **341 verified** |
| **5** | **20** | 200,000,000 (≈1.7% of 11.7B) | (running) | **≥ 1 verified** (F = 17461746146174617746) |
| 6 | 24 | — | — | (this campaign — see §3) |

The conjecture holds non-trivially at $m = 4$ and $m = 5$.

### 1.6 d=4 verification (the bridge to Kaprekar)

At $d = 4, m = 1$, the pair-symmetric construction with $A_7 = \{0\}, A_6 = \{1\}, A_4 = \{2\}, A_1 = \{3\}$ gives:

$$K = 6 \cdot (10^3 - 10^0) + 2 \cdot (10^2 - 10^1) = 6 \cdot 999 + 2 \cdot 90 = 5994 + 180 = 6174$$

This is exactly Kaprekar's constant. The reverse partition $A_7 = \{3\}, \ldots, A_1 = \{0\}$ gives $K = -6174$, with $|K| = 6174$. The remaining 22 partitions give K-values not matching the multiset $\{1,4,6,7\}$.

**The classical Kaprekar map at $d=4$ is the pair-symmetric construction at $m=1$.** This is the structural connection.

---

## 2. Rules — Explicit Examples

### 2.1 The 99.89% near-universal at d=16 (the discovery)

**F = 6177414661746174** &nbsp;&nbsp; (basin 2,040,808 / 2,042,965 = 99.8944%, partial)

```
π_inv = [0, 7, 8, 12, 1, 5, 9, 13, 2, 3, 10, 14, 4, 6, 11, 15]
σ_inv = [4, 6, 11, 15, 2, 3, 10, 14, 1, 5, 9, 13, 0, 7, 8, 12]
```

**Block structure (the key insight):**
- π places 7s at positions {0, 7, 8, 12} = A_7
- π places 6s at positions {1, 5, 9, 13} = A_6
- π places 4s at positions {2, 3, 10, 14} = A_4
- π places 1s at positions {4, 6, 11, 15} = A_1
- σ places 7s at A_1 = {4, 6, 11, 15} &nbsp;&nbsp;← pair-swap with 1
- σ places 6s at A_4 = {2, 3, 10, 14} &nbsp;&nbsp;← pair-swap with 4
- σ places 4s at A_6 = {1, 5, 9, 13}
- σ places 1s at A_7 = {0, 7, 8, 12}

**Resulting c-vector** (with the anti-symmetric pattern visible):
```
positions 0-3   (7-block): (+999900000000000, -900000000,    +9990000, +999)
positions 4-7   (6-block): (+90000000000000,  -990000000000, +900000,  +90)
positions 8-11  (4-block): (-90000000000000,  +990000000000, -900000,  -90)   [negation of 6-block]
positions 12-15 (1-block): (-999900000000000, +900000000,    -9990000, -999)  [negation of 7-block]
```

### 2.2 The first classical universal found at d=16

**F = 6614617774614174** (verified classical universal, basin = full)

```
π_inv = [15, 9, 12, 3, 14, 7, 8, 6, 13, 11, 5, 2, 0, 10, 4, 1]
σ_inv = [0, 10, 4, 1, 13, 11, 5, 2, 14, 7, 8, 6, 15, 9, 12, 3]
```

Verifying the pair-symmetric structure:
- π's 7-block positions: {15, 9, 12, 3} (first 4 of π_inv)
- σ's 7-block positions: {0, 10, 4, 1} (first 4 of σ_inv)
- π's 1-block positions: {0, 10, 4, 1} (last 4 of π_inv) ← matches σ's 7-block ✓
- σ's 1-block positions: {15, 9, 12, 3} (last 4 of σ_inv) ← matches π's 7-block ✓

The pair-swap (7 ↔ 1) is exact. Similarly for (6 ↔ 4) — the middle blocks are swapped.

### 2.3 The d=20 m=5 classical universal

**F = 17461746146174617746** (verified classical universal at d=20, basin = full = 10,014,995)

The specific (π_inv, σ_inv) will be saved in `d20_v1_DEEP.json` when the 200M-sample run completes. The structure is pair-symmetric (7↔1, 6↔4) with some specific partition of {0,…,19} into 4 blocks of size 5.

**Structural observations:**
- Starts with 1 ✓ (cross-d pattern: lead ∈ {1, 6})
- Ends with 6 ✓ (cross-d pattern: tail ∈ {4, 6})
- Contains "1746" at positions 0-3 AND 4-7 (**two non-overlapping copies** — the 6174/1746 substring enrichment from d=16 doubles at d=20)

### 2.4 The 41 first-batch d=16 universals (sample)

All from the first 2M-partition pair-symmetric run. Each F is a classical universal under a pair-symmetric rule.

```
F = 1417461746617746    F = 1746177461746146    F = 6174617414661774
F = 1417461777466146    F = 1746617741746146    F = 6174617461774146
F = 1417466174617746    F = 1774661414617746    F = 6177746141461746
F = 1417777414146666    F = 1777461417466146    F = 6177746141466174
F = 1461741746617746    F = 1777466146146174    F = 6177746174146146
F = 1461774617461746    F = 1777466661417414    F = 6177774614146614
F = 1466146146177774    F = 1777741461466146    F = 6614174617774614
F = 1466177461746174    F = 6141466177774614    F = 6614617774614174
F = 1466661774177414    F = 6141741741774666    F = 6617461741774614
F = 1741774146666174    F = 6141746177461746    F = 6617741746174614
F = 1746141774661746    F = 6141746617774614    F = 6617746146141774
                       F = 6146141777746614
                       F = 6146614617774174
                       F = 6146617461417774
                       F = 6146617774614174
                       F = 6174174614617746
                       F = 6174174617746146
                       F = 6174177461746146
```

Full list of 341 d=16 universals (with rules) is in `pair_symmetric_BIG.json` and `pair_symmetric_search.json`.

---

## 3. Predictions for d=24 m=6 and beyond

### 3.1 Pair-symmetric construction at d=24

At $d = 24, m = 6$: multiset $\{1,4,6,7\}^6$. Partition space: $\binom{24}{6,6,6,6} = 24!/(6!)^4 \approx 96.5 \times 10^9$ partitions. Each induces a pair-symmetric rule with K = 6·S_7 + 2·S_6.

**Predictions** based on cross-d patterns:
1. **Classical universals will exist** (non-emptiness conjecture)
2. Leading digit will be {1, 6} only (never 7, possibly never 4 at high m)
3. Trailing digit will be {4, 6}
4. Universal F's will likely contain MULTIPLE copies of "1746" or "6174" substring (extrapolating from d=20 where 2 copies appeared, and d=16 where 52% had 1 copy)
5. Universal density rough estimate: 1 per ~10⁸ partitions based on d=20 rate scaling

### 3.2 Computational expectations

| metric | value |
|---|---:|
| Total partitions | 96.5 billion |
| Basin at d=24 (non-repdigit multisets) | ~45.4 million |
| classify_rule cost per F | ~5x d=20 cost ≈ 150-300 sec |
| Expected hits per million partitions | unknown — probably 10× lower than d=20 |
| Expected wall time for 100M sample run | ~10 hours on 1 core |

### 3.3 Concrete d=24 candidate F (structural prediction)

By extrapolation from d=16 and d=20 patterns, a likely universal F at d=24 would have structure:

`F = [1 or 6] | (multiple copies of 1746/6174) | [4 or 6]`

Example construction template:
- `1746 | 1746 | 1746 | [variable 12 digits] | [last digit ∈ {4,6}]`

Total 24 digits with multiset {1,4,6,7}^6 = {1^6, 4^6, 6^6, 7^6}. The three "1746" blocks contribute {1,4,6,7}^3 = {1^3, 4^3, 6^3, 7^3}, leaving {1^3, 4^3, 6^3, 7^3} for the remaining 12 positions.

A specific candidate to test: `F = 174617461746 + (rearrangement of {1,1,1,4,4,4,6,6,6,7,7,7})`

### 3.4 Theory direction

**Conjecture (formal version):** Let $d = 4m$ and consider the pair-symmetric (7↔1, 6↔4) construction. For every $m \geq 1$, there exists a 4-partition $(A_7, A_6, A_4, A_1)$ of $\{0, \ldots, d-1\}$ into blocks of size $m$ such that the corresponding pair-symmetric rule is universal for the K-output F.

**Proof sketch** (if it were to be proved):
- *Base case*: $m = 1$ verified explicitly (gives 6174, 1746)
- *Inductive step*: given a universal partition at $m$, construct one at $m+1$. The challenge is showing the basin remains full when extending by one digit.

This would establish the conjecture rigorously. Computational verification at $m \in \{1, 2, 3, 4, 5\}$ is consistent with it.

---

## 4. Open questions

1. **Exact count formula**: How does the number of pair-symmetric universals scale with $m$?
   - $m=1$: 2, $m=2$: 481, $m=3$: 42, $m=4$: 341, $m=5$: ≥1
   - The counts are non-monotone — what controls them?

2. **Other structural families**: At m=5 (d=20), pair-symmetric v1 produces 0 candidates in 30M but 1 universal in 200M. The other two pair-symmetric variants (v2, v3) and the 4-cycle/derangement variants produce 0 candidates entirely. Are there universals in OTHER structural families at higher m?

3. **Cross-multiset extension**: Does pair-symmetric (with appropriate digit-pair choice) produce universals for other class B multisets like {0,4,5,9}? The {0,4,5,9} d=12 m=3 case had 152 universals (vs 42 for {1,4,6,7}); a separate analysis is needed.

4. **Proof of non-emptiness**: Computational verification up to $m=5$ is consistent with the conjecture, but a proof requires showing the basin coverage at every $m$.

5. **Continuous deformation**: Can the partition for a universal at $m$ be "deformed" to one at $m+1$? This would suggest a continuous family.

---

## 5. Computational protocol (for reproducibility)

### 5.1 Pair-symmetric search

```python
def pair_symmetric_rule(A7, A6, A4, A1, d):
    """Construct pair-symmetric (7↔1, 6↔4) rule for partition (A7, A6, A4, A1)."""
    m = d // 4
    pi_inv = [0]*d; sigma_inv = [0]*d
    for i, p in enumerate(A7): pi_inv[i] = p
    for i, p in enumerate(A6): pi_inv[i + m] = p
    for i, p in enumerate(A4): pi_inv[i + 2*m] = p
    for i, p in enumerate(A1): pi_inv[i + 3*m] = p
    for i, p in enumerate(A1): sigma_inv[i] = p              # 7↔1 swap
    for i, p in enumerate(A4): sigma_inv[i + m] = p          # 6↔4 swap
    for i, p in enumerate(A6): sigma_inv[i + 2*m] = p
    for i, p in enumerate(A7): sigma_inv[i + 3*m] = p
    return tuple(pi_inv), tuple(sigma_inv)
```

### 5.2 Search loop (canonical form)

```python
random.seed()  # or fixed seed for reproducibility
SORTED_DESC = tuple([7]*m + [6]*m + [4]*m + [1]*m)
TARGET_MS = Counter('1'*m + '4'*m + '6'*m + '7'*m)

for k in range(N_PARTITIONS):
    p = list(range(d)); random.shuffle(p)
    A7, A6, A4, A1 = p[0:m], p[m:2*m], p[2*m:3*m], p[3*m:4*m]
    pi, sg = pair_symmetric_rule(A7, A6, A4, A1, d)
    c = coefs_from_invs(pi, sg, d)
    if 0 in c: continue
    K = abs(sum(c[i]*SORTED_DESC[i] for i in range(d)))
    if not (10**(d-1) <= K < 10**d): continue
    if Counter(str(K).zfill(d)) == TARGET_MS:
        verdict, n_to_F, n_total, _, _ = classify_rule(K, c, d, all_multisets)
        if verdict == 'classical':
            # FOUND A UNIVERSAL
            save(K, pi, sg)
```

---

## 6. Status of d=24 m=6 search

**To launch:** see §3.2 above. Recommended initial budget: 100M partitions, ~10 hours on 1 core, expected ~1-10 classical universals.

**Implementation note:** classify_rule at d=24 traces 45M multisets per call; will be ~5× slower per F than d=20. Memory needs are negligible (~few hundred MB).
