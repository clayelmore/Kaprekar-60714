[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix C. Support lemmas](C_support_lemmas.md) · [Next: Appendix E. 6174 audit at $`d = 8, 9`$ →](E_6174_audit.md)

---

# Appendix D. Universal Full-Variable Fixed Points at $`d = 7`$

This appendix documents the classification of universal full-variable fixed points at $`d = 7`$ and the cross-dimensional outcomes for the two-zero $`d = 6`$ stratum tested at $`d = 7`$. Two complementary enumerations underlie the data:

- **Run B (exhaustive classification at $`d = 7`$).** Sound exhaustive enumeration over all $`9{,}344{,}160 = 7! \cdot D_7`$ full-variable rules at $`d = 7`$, identifying every universal full-variable fixed point. Numba-accelerated, approximately $`45`$ seconds wall-time on commodity hardware.
- **Run C (cross-dimensional outcome verification).** For each of the $`53`$ two-zero $`d = 6`$ universal fps, exhaustive enumeration of all rank-$`7`$ rules fixing the fp with exact basin computation. Approximately one hour wall-time.

A held-out validation set of $`12`$ additional $`d = 6`$ fps (drawn from $`0`$-zero, $`1`$-zero, $`2`$-zero, and $`3`$-zero strata) is used in §D.3 to validate the Type A LOCK characterization beyond the two-zero stratum. The complete computational pipeline, including the audit package `d7_audit/`, is provided as supplementary material (§1.7.1).

## D.1 Universal full-variable fps at $`d = 7`$

Run B identifies **$`18{,}004`$ universal full-variable fixed points at $`d = 7`$**, attained by $`49{,}292`$ universal rules. Zero-stratification:

| Zero count | Universal fixed points |
|:---:|:---:|
| $`0`$ | $`7{,}541`$ |
| $`1`$ | $`8{,}125`$ |
| $`2`$ | $`1{,}996`$ |
| $`3`$ | $`316`$ |
| $`4`$ | $`19`$ |
| $`5`$ | $`7`$ |

The $`21`$ strict-universal $`d = 7`$ fps catalogued in earlier drafts of this Appendix (under "Case 1" and "Case 2") all appear in the Run B catalog with rule-count metadata matching exactly. The earlier draft also listed $`F = 1{,}406{,}070`$ as a "NEAR-edge" case; this fp does not appear in the Run B catalog of strict-universal fps because its best basin at $`d = 7`$ is below the strict-universal threshold (basin $`\approx 0.9999 < 1`$), confirming the earlier NEAR-edge characterization.

## D.2 Cross-dimensional outcomes: the two-zero $`d = 6`$ stratum

Of the $`506`$ universal full-variable fixed points at $`d = 6`$, exactly $`53`$ have multiset structure with two trailing zeros at $`d = 6`$ (equivalently, three trailing zeros when padded to $`d = 7`$). Run C performs exhaustive outcome verification for these $`53`$ fps at $`d = 7`$, classifying each as TRANS (best basin $`\geq 0.99`$), NEAR (basin in $`[0.95, 0.99)`$), LOCK (basin $`< 0.95`$), or algebraic obstruction (no fixing rule exists).

**Result.** $`43`$ TRANS, $`2`$ NEAR, $`8`$ LOCK. Of the $`8`$ LOCK fps, $`4`$ are Type A LOCK and $`4`$ are Type B LOCK in the sense of §6.6. The $`43`$ TRANS comprise $`42`$ strict-universal (basin $`= 1`$) plus $`F = 60714`$ (basin $`= 0.992857`$, NEAR-strict by the threshold of §1.4).

**Strict-transcendence rate** for the two-zero $`d = 6`$ stratum at $`d = 7`$: $`43/53 \approx 81.1\%`$. Including NEAR cases the rate is $`45/53 \approx 84.9\%`$. Earlier estimates based on the smaller $`21`$-fp strict-universal subset (table D.7 of the prior draft) suggested cross-dimensional rates near $`96\%`$; the corrected figure for the full $`53`$-fp stratum is lower, though still high enough to justify the qualitative claim that cross-dimensional transcendence is "common at higher $`d_F`$."

The full verified outcomes table:

| $`F`$ | Outcome | Best basin | Type | Valid rules | Rules $`\geq 0.99`$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $`4{,}545`$ | TRANS | $`1.000000`$ | – | $`1{,}920`$ | $`12`$ |
| $`7{,}191`$ | NEAR | $`0.984568`$ | – | $`432`$ | $`0`$ |
| $`8{,}919`$ | TRANS | $`1.000000`$ | – | $`768`$ | $`14`$ |
| $`8{,}991`$ | TRANS | $`1.000000`$ | – | $`1{,}632`$ | $`68`$ |
| $`9{,}189`$ | TRANS | $`1.000000`$ | – | $`1{,}344`$ | $`8`$ |
| $`9{,}225`$ | LOCK | $`0.884215`$ | B | $`216`$ | $`0`$ |
| $`10{,}899`$ | TRANS | $`1.000000`$ | – | $`1{,}632`$ | $`16`$ |
| $`17{,}019`$ | LOCK | $`0.574250`$ | A | $`192`$ | $`0`$ |
| $`37{,}017`$ | LOCK | $`0.860582`$ | A | $`192`$ | $`0`$ |
| $`44{,}505`$ | TRANS | $`1.000000`$ | – | $`1{,}920`$ | $`4`$ |
| $`52{,}605`$ | LOCK | $`0.563404`$ | B | $`288`$ | $`0`$ |
| $`54{,}450`$ | TRANS | $`1.000000`$ | – | $`1{,}920`$ | $`10`$ |
| $`60{,}714`$ | TRANS | $`0.992857`$ | – | $`36`$ | $`4`$ |
| $`67{,}023`$ | LOCK | $`0.868783`$ | B | $`36`$ | $`0`$ |
| $`80{,}919`$ | TRANS | $`1.000000`$ | – | $`1{,}584`$ | $`30`$ |
| $`80{,}991`$ | TRANS | $`1.000000`$ | – | $`768`$ | $`26`$ |
| $`81{,}099`$ | TRANS | $`1.000000`$ | – | $`768`$ | $`8`$ |
| $`89{,}019`$ | TRANS | $`1.000000`$ | – | $`2{,}208`$ | $`20`$ |
| $`90{,}819`$ | TRANS | $`1.000000`$ | – | $`2{,}112`$ | $`4`$ |
| $`90{,}918`$ | TRANS | $`1.000000`$ | – | $`1{,}344`$ | $`4`$ |
| $`91{,}809`$ | TRANS | $`1.000000`$ | – | $`1{,}440`$ | $`6`$ |
| $`98{,}091`$ | TRANS | $`1.000000`$ | – | $`1{,}440`$ | $`16`$ |
| $`100{,}899`$ | TRANS | $`1.000000`$ | – | $`2{,}400`$ | $`46`$ |
| $`108{,}099`$ | TRANS | $`1.000000`$ | – | $`1{,}440`$ | $`18`$ |
| $`109{,}809`$ | TRANS | $`1.000000`$ | – | $`1{,}296`$ | $`4`$ |
| $`146{,}070`$ | TRANS | $`1.000000`$ | – | $`108`$ | $`4`$ |
| $`170{,}460`$ | LOCK | $`0.922928`$ | B | $`36`$ | $`0`$ |
| $`180{,}909`$ | TRANS | $`1.000000`$ | – | $`1{,}440`$ | $`6`$ |
| $`189{,}009`$ | TRANS | $`1.000000`$ | – | $`2{,}784`$ | $`8`$ |
| $`190{,}089`$ | TRANS | $`1.000000`$ | – | $`2{,}208`$ | $`22`$ |
| $`190{,}809`$ | TRANS | $`1.000000`$ | – | $`768`$ | $`30`$ |
| $`445{,}005`$ | TRANS | $`1.000000`$ | – | $`1{,}920`$ | $`10`$ |
| $`445{,}050`$ | TRANS | $`1.000000`$ | – | $`1{,}920`$ | $`12`$ |
| $`504{,}450`$ | TRANS | $`1.000000`$ | – | $`1{,}920`$ | $`14`$ |
| $`544{,}500`$ | TRANS | $`1.000000`$ | – | $`1{,}920`$ | $`12`$ |
| $`607{,}140`$ | NEAR | $`0.985450`$ | – | $`36`$ | $`0`$ |
| $`700{,}191`$ | TRANS | $`1.000000`$ | – | $`432`$ | $`2`$ |
| $`701{,}901`$ | LOCK | $`0.816755`$ | A | $`192`$ | $`0`$ |
| $`707{,}130`$ | LOCK | $`0.916314`$ | A | $`384`$ | $`0`$ |
| $`719{,}100`$ | TRANS | $`1.000000`$ | – | $`432`$ | $`2`$ |
| $`809{,}091`$ | TRANS | $`1.000000`$ | – | $`2{,}880`$ | $`24`$ |
| $`809{,}109`$ | TRANS | $`1.000000`$ | – | $`2{,}208`$ | $`16`$ |
| $`810{,}909`$ | TRANS | $`1.000000`$ | – | $`2{,}976`$ | $`10`$ |
| $`890{,}091`$ | TRANS | $`1.000000`$ | – | $`768`$ | $`14`$ |
| $`900{,}891`$ | TRANS | $`1.000000`$ | – | $`768`$ | $`24`$ |
| $`901{,}890`$ | TRANS | $`1.000000`$ | – | $`1{,}440`$ | $`6`$ |
| $`908{,}091`$ | TRANS | $`1.000000`$ | – | $`2{,}208`$ | $`28`$ |
| $`908{,}109`$ | TRANS | $`1.000000`$ | – | $`2{,}304`$ | $`18`$ |
| $`908{,}190`$ | TRANS | $`1.000000`$ | – | $`2{,}112`$ | $`14`$ |
| $`908{,}901`$ | TRANS | $`1.000000`$ | – | $`1{,}536`$ | $`36`$ |
| $`909{,}081`$ | TRANS | $`1.000000`$ | – | $`2{,}976`$ | $`34`$ |
| $`910{,}089`$ | TRANS | $`1.000000`$ | – | $`768`$ | $`44`$ |
| $`910{,}809`$ | TRANS | $`1.000000`$ | – | $`2{,}208`$ | $`14`$ |

The "Type" column is $`-`$ for TRANS/NEAR fps; A or B for LOCK fps per the §6.6 classification. The "Rules $`\geq 0.99`$" column counts $`d = 7`$ fixing rules whose basin meets the strict-universal threshold of §1.4.

## D.3 Held-out validation of the Type A LOCK characterization

To validate the Type A characterization (Definition 6.3) beyond the two-zero stratum, we ran the verifier on $`12`$ additional $`d = 6`$ universal fps drawn from $`0`$-zero, $`1`$-zero, $`2`$-zero, and $`3`$-zero strata ($`3`$ each):

| $`F`$ | Stratum at $`d = 6`$ | Outcome at $`d = 7`$ | Type | zsp rules / total rules at $`d = 7`$ |
|:---:|:---:|:---:|:---:|:---:|
| $`112{,}743`$ | $`0`$-zero | LOCK | A | $`0 / 32`$ |
| $`284{,}679`$ | $`0`$-zero | LOCK | B | $`6 / 16`$ |
| $`477{,}936`$ | $`0`$-zero | (algebraic obstruction) | – | $`0 / 0`$ |
| $`11{,}736`$ | $`1`$-zero | LOCK | A | $`0 / 16`$ |
| $`175{,}086`$ | $`1`$-zero | LOCK | B | $`8 / 12`$ |
| $`386{,}064`$ | $`1`$-zero | LOCK | A | $`0 / 16`$ |
| $`4{,}545`$ | $`2`$-zero | TRANS | – | $`1{,}344 / 1{,}920`$ |
| $`89{,}019`$ | $`2`$-zero | TRANS | – | $`1{,}248 / 2{,}208`$ |
| $`544{,}500`$ | $`2`$-zero | TRANS | – | $`1{,}344 / 1{,}920`$ |
| $`252`$ | $`3`$-zero | TRANS | – | $`1{,}152 / 4{,}224`$ |
| $`20{,}025`$ | $`3`$-zero | TRANS | – | $`1{,}152 / 4{,}224`$ |
| $`200{,}025`$ | $`3`$-zero | TRANS | – | $`1{,}152 / 4{,}224`$ |

The Type A predictor was tested blind on this held-out set: $`3`$ of $`12`$ fps ($`112{,}743`$, $`11{,}736`$, $`386{,}064`$) were predicted Type A LOCK based solely on their absence of zsp rules at $`d = 7`$. All three predictions matched the verified LOCK outcomes. No false positives occurred (no Type A prediction fired on any of the $`6`$ TRANS records or $`2`$ Type B LOCK records).

The held-out result confirms that Type A LOCK is not specific to the two-zero stratum; it is a general structural mechanism applicable across multiple zero-count strata at $`d = 6 \to d = 7`$. Combined with Run C, the Type A predictor has $`7`$ correct predictions out of $`7`$ across $`65`$ total verified records, with zero false positives.

## D.4 Cycle signatures at $`d = 7`$

The cycle signature of a permutation pair $`(\pi, \sigma)`$ records the cycle decomposition of $`\pi \cdot \sigma^{-1}`$. Among the $`53`$ Run C fps, four signatures appear among fixing rules: $`(2, 2, 3)`$, $`(2, 5)`$, $`(3, 4)`$, and $`(7,)`$. The signature $`(3, 4)`$ — the natural structural analog at $`d_F = 7`$ of $`(3, 3)`$ at $`d_F = 6`$ — does *not* uniformly produce LOCK rules: $`9`$ of the $`53`$ fps include $`(3, 4)`$ in their signature set and TRANS, while $`5`$ include $`(3, 4)`$ and LOCK. The factorization mechanism that locks $`(3, 3)`$ at $`d_F = 6`$ (Theorem 6.1 part 4) does not generalize directly to $`(3, 4)`$ at $`d_F = 7`$.

A refined cycle-signature pattern does hold (§6.7, observation 4): fps whose fixing-rule space is restricted to only the long-cycle signatures $`\{(3, 4), (7,)\}`$ uniformly LOCK at $`d = 7`$ ($`4`$ of $`4`$ in Run C). All four cases are also Type A LOCK by Observation 6.3, which suggests the cycle-signature restriction is a *consequence* of the more fundamental zsp absence rather than an independent classifier.

## D.5 Cross-dimensional behavior

| Transition | Universal fps | Strict TRANS | Rate |
|:---|:---:|:---:|:---:|
| $`d = 4 \to d = 5`$ | $`4`$ at $`d = 4`$ | $`0`$ at $`d = 5`$ | $`0\%`$ |
| $`d = 5 \to d = 6`$ | $`33`$ at $`d = 5`$ | $`1`$ at $`d = 6`$ ($`60{,}714`$) | $`3\%`$ |
| $`d = 6 \to d = 7`$ (two-zero stratum) | $`53`$ | $`43`$ | $`81\%`$ |
| $`d = 6 \to d = 7`$ (held-out 12-fp set) | $`11`$ (excluding alg. obstruction) | $`6`$ | $`55\%`$ |

**Observation D.1 (revised, empirical).** *Cross-dimensional transcendence from $`d_F`$ to $`d_F + 1`$ rises sharply with the zero-digit count of $`F`$'s padded multiset. Within the two-zero $`d = 6`$ stratum tested at $`d = 7`$, the strict-transcendence rate is $`43/53 \approx 81\%`$. Within the broader held-out set spanning $`0`$-zero through $`3`$-zero strata, the rate falls to $`6/11 \approx 55\%`$, with $`0`$-zero and $`1`$-zero fps disproportionately LOCK or algebraically obstructed. The trend is consistent with Conjecture 7.2: dimension-transcendence is enabled by absorbing capacity, which grows with both $`d_F`$ and zero-digit count.*

**Note on the 4-zero stratum at $`d = 6`$.** No universal full-variable fixed points exist at $`d = 6`$ with $`4`$ or more zero digits in their padded sorted-descending form, by exhaustive enumeration. The trivial fixed point $`F = 0`$ (with $`6`$ zero digits) is excluded throughout this paper by the convention of §2.

## D.6 Reproducibility

The complete data underlying this appendix is reproducible from the supplementary `d7_audit/` package (§1.7.1):

- `classify_d7_full.py` reproduces Run B (the $`18{,}004`$-fp classification at $`d = 7`$). Wall-time: $`\approx 45`$ s.
- `d7_outcome_verifier.py` reproduces Run C (cross-dimensional outcomes for the two-zero $`d = 6`$ stratum). Wall-time: $`\approx 1`$ hour.
- `audit_60714_d7.py` and `audit_60714_d8.py` reproduce the empirical confirmation of Lemma 5.5 at $`d = 7`$ and $`d = 8`$ (cf. §5 Remark). Wall-time: $`\approx 3`$ s each.

Per-fp data is recorded in `d7_classification.json` (Run B output) and `d7_verified_outcomes.json` (Run C output), both included as supplementary files. The earlier `dF7_summary_complete.json` is retained for reference; its $`21`$-fp strict-universal listing is a strict subset of Run B's $`18{,}004`$-fp catalog.

---

*End of Appendix D.*

---

[← Back to paper](../README.md#table-of-contents) · [← Previous: Appendix C. Support lemmas](C_support_lemmas.md) · [Next: Appendix E. 6174 audit at $`d = 8, 9`$ →](E_6174_audit.md)
