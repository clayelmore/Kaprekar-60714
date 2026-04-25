[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix C. Support lemmas](C_support_lemmas.md) · [Next: Appendix E. 6174 audit at $`d = 8, 9`$ →](E_6174_audit.md)

---

# Appendix D. Transcendent Fixed Points at $`d = 7`$

This appendix documents universal full-variable fixed points observed at $`d = 7`$ that arise as coefficient-preserving liftings of universal fps at $`d_F \leq 6`$. The classification at $`d = 7`$ is *not* exhaustive: the full rank-$`7`$ rule space contains $`7! \cdot D_7 = 5{,}040 \cdot 1{,}854 = 9{,}344{,}160`$ full-variable rules, which is too large for exhaustive basin testing on commodity hardware. We therefore enumerate observed transcendent fps — those discovered through the lifting framework of §5 — and test each for universality at $`d = 7`$ directly.

**Scope.** This appendix reports what has been verified. Additional universal sv$`=7`$ fps may exist outside the lifting framework; these have not been systematically searched. The data below provides a *lower bound* on the set of universal full-variable fps at $`d = 7`$.

**Methodology.** For each fixed point $`F`$ with at least three zero digits at $`d = 7`$, we enumerate all coefficient-preserving liftings of $`F`$'s native rule(s) and test each lifting for universality over the $`11{,}340`$ admissible multisets at $`d = 7`$. A rule is **strict-universal** (TRANS) if every admissible input reaches $`F`$. A rule is **near-universal** (NEAR) if basin $`\geq 0.99`$ but $`< 1`$. A rule is **dimension-locked** (LOCK) if no lifting achieves basin $`\geq 0.99`$.

The audit was completed in 2026-04-23 over approximately $`24{,}300`$ seconds of compute time across 22 candidate fps.

## D.1 Summary of observed transcendent fps at $`d = 7`$

| Status | Count | Description |
|:---|:---:|:---|
| TRANS, **Case 1** (core $`\geq 0`$) | $`10`$ | At least one coefficient-preserving lifting achieves basin $`= 1.0`$; the native rule has a non-negative core function (Lemma 5.3 analog at $`d = 7`$). |
| TRANS, **Case 2** (bounded-deficit core) | $`11`$ | At least one strict-universal lifting; core can be negative but bounded. |
| **NEAR-edge** (no strict, basin $`\to 1`$) | $`1`$  | No strict-universal lifting; best basin $`\approx 0.9999`$. |
| Total observed transcendent fps | $`22`$ | (10 Case 1 + 11 Case 2 + 1 NEAR-edge) |

The Case 1 / Case 2 / NEAR-edge classification is the same framework that organizes §6's audit at $`d_F = 6`$, extended to $`d_F = 7`$. A detailed structural framework for these cases is the subject of forthcoming work and is not developed here.

## D.2 The 10 TRANS fps with core non-negativity (Case 1)

These ten fps have native rules at $`d = 7`$ for which the core function (the analog of Lemma 5.3 at $`d = 7`$) is non-negative on sorted-descending inputs. The proof technique of Theorem 5.2 extends to these fps directly.

| Fixed point | # strict-universal rules | Cycle signatures observed |
|:---:|:---:|:---|
| $`1{,}080{,}909`$ | $`8`$  | $`(2, 2, 3), (2, 5), (3, 4)`$ |
| $`4{,}504{,}500`$ | $`16`$ | $`(2, 2, 3)`$ |
| $`6{,}040{,}170`$ | $`2`$  | $`(2, 5)`$ |
| $`9{,}001{,}089`$ | $`8`$  | $`(2, 2, 3), (2, 5)`$ |
| $`9{,}009{,}081`$ | $`6`$  | $`(2, 2, 3), (2, 5)`$ |
| $`9{,}090{,}081`$ | $`2`$  | $`(2, 5)`$ |
| $`9{,}090{,}810`$ | $`4`$  | $`(2, 2, 3), (2, 5)`$ |
| $`9{,}100{,}089`$ | $`10`$ | $`(2, 2, 3), (2, 5), (3, 4)`$ |
| $`9{,}100{,}809`$ | $`20`$ | $`(2, 2, 3), (2, 5)`$ |
| $`9{,}100{,}890`$ | $`18`$ | $`(2, 2, 3), (2, 5)`$ |

**Total strict-universal rules across Case 1: $`94`$.**

All ten share the digit count $`(d - \text{nonzero digits}) = (7 - 4) = 3`$ zero digits, consistent with Observation D.1 below.

## D.3 The 11 TRANS fps with bounded-deficit core (Case 2)

These eleven fps have native rules at $`d = 7`$ for which the core function can be negative but is bounded below by $`-10^6`$. The argument of Theorem 5.2 generalizes with a modified bound: instead of one-step closure to $`T_d`$, these rules achieve at most two-step closure.

| Fixed point | # strict-universal rules | Cycle signatures observed | Best $`\mathrm{core}_{\min}`$ |
|:---:|:---:|:---|:---:|
| $`146{,}070`$    | $`4`$  | $`(7), (2, 5)`$               | $`-89{,}100`$ |
| $`445{,}005`$    | $`8`$  | $`(2, 2, 3), (7), (3, 4)`$    | $`-89{,}991`$ |
| $`445{,}050`$    | $`10`$ | $`(2, 2, 3), (2, 5)`$         | $`-8{,}910`$ |
| $`545{,}040`$    | $`2`$  | $`(2, 5)`$                    | $`-818{,}910`$ |
| $`1{,}009{,}089`$ | $`2`$  | $`(2, 5)`$                    | $`-89{,}910`$ |
| $`1{,}009{,}098`$ | $`4`$  | $`(2, 5), (3, 4)`$            | $`-891`$ |
| $`1{,}400{,}706`$ | $`2`$  | $`(7)`$                       | $`-899{,}991`$ |
| $`4{,}450{,}500`$ | $`12`$ | $`(2, 2, 3), (2, 5)`$         | $`-89{,}100`$ |
| $`4{,}455{,}000`$ | $`10`$ | $`(2, 2, 3), (2, 5)`$         | $`-89{,}910`$ |
| $`4{,}545{,}000`$ | $`8`$  | $`(2, 2, 3)`$                 | $`-8{,}910`$ |
| $`8{,}090{,}901`$ | $`2`$  | $`(2, 5)`$                    | $`-8{,}991`$ |

**Total strict-universal rules across Case 2: $`64`$.**

The "bounded-deficit threshold" for Case 2 at $`d_F = 7`$ is $`|\mathrm{core}_{\min}| < 10^{d_{F} - 1} = 10^6`$. All 11 fps satisfy this bound, with the loosest case ($`545{,}040`$) at $`|\mathrm{core}_{\min}| = 818{,}910 < 10^6`$.

## D.4 The NEAR-edge fp: $`F = 1{,}406{,}070`$

One fp in the audit is genuinely *near-universal* but not strict-universal at $`d = 7`$:

| Property | Value |
|:---|:---|
| Multiset | $`\{0, 0, 0, 1, 4, 6, 7\}`$ (3 zeros, in the $`\{7, 6, 4, 1\}`$-thread) |
| # strict-universal rules at $`d = 7`$ | $`0`$ |
| Best basin | $`\approx 0.9999`$ |
| Audit runtime | $`315`$ seconds |

**Characterization.** No coefficient-preserving lifting of $`1{,}406{,}070`$'s native rules achieves basin $`= 1.0`$ at $`d = 7`$. The best lifting falls just short, with a small escape class — analogous to but distinct from the $`6174`$ escape class of §6.

The fp is in the same multiset $`\{7, 6, 4, 1, 0, 0, 0\}`$ as $`146{,}070`$, $`607{,}140`$, $`170{,}460`$, and the lifted form of $`60{,}714`$ — that is, in the $`\{7, 6, 4, 1\}`$-thread of §6. Among these threads at $`d = 7`$, $`1{,}406{,}070`$ is the unique NEAR-edge: the others are all strict-universal (Case 2). The mechanism distinguishing $`1{,}406{,}070`$ is structurally analogous to the $`60{,}714`$-vs-$`60{,}417`$ asymmetry analyzed at §6 and §7.

**Open question.** Whether $`1{,}406{,}070`$ admits a strict-universal coefficient-preserving lifting at any $`d \geq 8`$ is open. The basin shortfall of $`\approx 0.0001`$ at $`d = 7`$ is small enough that ladder extension could plausibly close the gap, but no proof or empirical check has been completed.

## D.5 Cycle signatures observed

The cycle signature of a permutation pair $`(\pi, \sigma)`$ records the cycle decomposition of the permutation $`\pi \cdot \sigma^{-1}`$. Across the 22 transcendent fps at $`d = 7`$, four signatures appear:

| Signature | Case 1 fps | Case 2 fps | Observation |
|:---:|:---:|:---:|:---|
| $`(2, 2, 3)`$ | $`6`$ of $`10`$ | $`3`$ of $`11`$ | Most common; appears in both cases |
| $`(2, 5)`$    | $`9`$ of $`10`$ | $`8`$ of $`11`$ | Second most common; appears in both |
| $`(3, 4)`$    | $`2`$ of $`10`$ | $`2`$ of $`11`$ | Appears in both — does *not* force LOCK |
| $`(7,)`$      | $`0`$ of $`10`$ | $`1`$ of $`11`$ | Only in Case 2; rare |

**Note on $`(3, 4)`$.** The signature $`(3, 4)`$ is the natural structural analog at $`d_F = 7`$ of $`(3, 3)`$ at $`d_F = 6`$ (factoring $`7`$ as $`3 + 4`$ rather than $`6`$ as $`3 + 3`$). At $`d_F = 6`$, signature $`(3, 3)`$ uniformly produces dimension-locked rules. At $`d_F = 7`$, signature $`(3, 4)`$ does *not* uniformly lock: four of the 22 transcendent fps include $`(3, 4)`$ in their signature set. The factorization mechanism that locks $`(3, 3)`$ at $`d_F = 6`$ does not generalize to $`(3, 4)`$ at $`d_F = 7`$.

**Note on $`(7,)`$.** The single-cycle signature $`(7,)`$ appears only at $`1{,}400{,}706`$ and is the rarest. Its appearance in a Case 2 fp suggests that single-cycle signatures do not preclude transcendence at $`d_F = 7`$, in contrast to the $`d_F = 5 \to d_F = 6`$ classification where single-cycle signatures correlated with dimension-locking.

## D.6 The LOCK boundary at $`d = 7`$

The Case 1 / Case 2 / NEAR-edge framework accounts for all 22 transcendent fps audited. The LOCK boundary at $`d = 7`$ — the criterion under which a $`d_F = 7`$ universal full-variable fp fails to admit any coefficient-preserving lifting at $`d = 8`$ — is *not* characterized by these data, because the audit was restricted to fps with three zero digits.

**Open.** Two structural questions remain:

1. *Are there universal full-variable fps at $`d = 7`$ with $`\leq 2`$ zero digits that are dimension-locked at $`d = 7 \to d = 8`$?* This requires extending the audit to lower-zero-count strata, which the existing audit infrastructure cannot reach without exhaustive enumeration of the rank-$`7`$ rule space.
2. *What is the LOCK criterion at $`d_F = 7`$?* At $`d_F = 6`$, signature $`(3, 3)`$ provides a clean criterion (Theorem 6.1 part 4). The corresponding criterion at $`d_F = 7`$ — if one exists — does *not* reduce to signature $`(3, 4)`$, as the data above show.

These are noted as open questions in §7.

## D.7 Cross-dimensional behavior

| Transition | Universal fps | Observed transcendent | Rate |
|:---|:---:|:---:|:---:|
| $`d = 4 \to d = 5`$ | $`4`$ at $`d = 4`$ | $`0`$ at $`d = 5`$ | $`0\%`$ |
| $`d = 5 \to d = 6`$ | $`33`$ at $`d = 5`$ | $`1`$ at $`d = 6`$ ($`60{,}714`$) | $`3\%`$ |
| $`d = 6 \to d = 7`$ | $`506`$ at $`d = 6`$ | $`\approx 21`$ at $`d = 7`$ | $`\approx 4\%`$ |
| $`d = 7 \to d = 8`$ | $`\geq 22`$ at $`d = 7`$ | $`\geq 22`$ extending via lifting | $`\geq 96\%`$ |

**Observation D.1 (empirical).** *Transcendence from $`d_F`$ to $`d_F + 1`$ is rare at low $`d_F`$ (3–4%) but becomes near-certain at higher $`d_F`$, particularly for fps with $`\geq 3`$ zero digits. Specifically, all $`22`$ TRANS fps audited at $`d_F = 7`$ have exactly $`3`$ zero digits. The trend is consistent with Conjecture 7.2: dimension-transcendence is enabled by absorbing capacity, and absorbing capacity grows with both $`d_F`$ and zero-digit count.*

**Note on the 4-zero stratum at $`d = 6`$.** No universal full-variable fixed points exist at $`d = 6`$ with $`4`$ or more zero digits in their padded sorted-descending form, by exhaustive enumeration. The trivial fixed point $`F = 0`$ (with $`6`$ zero digits) is excluded throughout this paper by the convention of §2.

## D.8 Reproducibility

The audit data is recorded in:

- `dF7_summary_complete.json` — 22-fp summary with cases, rule counts, signatures, and core bounds.
- `dF7_bounded_deficit_scan.json` — per-fp coefficient-vector data for Case 2 fps.
- `dF7_cycle_sig_scan.json` — per-fp signature inventory.

These files are included in the supplementary materials. The audit script (`dF7_audit.py`, derived from `verify_60714_ladder.py` with $`d_F = 7`$ specialization) is in `scripts/`.

---

*End of Appendix D.*

---

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix C. Support lemmas](C_support_lemmas.md) · [Next: Appendix E. 6174 audit at $`d = 8, 9`$ →](E_6174_audit.md)
