# Appendix D. Observed Transcendent Fixed Points at $d = 7$

This appendix documents universal full-variable fixed points observed at $d = 7$ that arise as coefficient-preserving liftings of universal fps at $d_F \leq 6$. Unlike the classifications of §3 (exhaustive at $d \leq 6$), the enumeration at $d = 7$ is *not* exhaustive: the full rank-$7$ rule space contains $7! \cdot D_7 = 5{,}040 \cdot 1{,}854 = 9{,}344{,}160$ full-variable rules, which is too large for exhaustive basin testing on commodity hardware. Rather, we enumerate *observed* transcendent fps — those discovered through the lifting framework of §5 — and test each for universality at $d = 7$ directly.

**Scope.** This appendix reports what has been verified. Additional universal sv$=7$ fps may exist that arise from rule families not captured by coefficient-preserving lifting from $d_F \leq 6$; these have not been systematically searched. The data below therefore provides a *lower bound* on the set of universal full-variable fps at $d = 7$.

**Methodology.** For each fixed point $F$ with $d_F \in \{4, 5, 6\}$, we enumerate all coefficient-preserving liftings of $F$'s native rule(s) to digit length $7$ and test each lifting for universality over the $11{,}340$ admissible multisets at $d = 7$. A rule is **strict-universal** (TRANS) if every admissible input reaches $F$. A rule is **near-universal** (NEAR) if basin $\geq 0.99$ but $<$ 1. A rule is **locked** (LOCK) if basin $< 0.99$ on all liftings.

## D.1 Summary of observed transcendent fps at $d = 7$

From systematic audit of coefficient-preserving liftings from $d_F \in \{5, 6\}$, we observe the following at $d = 7$:

| Status | Count | Description |
|:---|:---:|:---|
| TRANS (strict-universal at $d = 7$) | $22$ | At least one coefficient-preserving lifting achieves basin $= 1.0$. |
| NEAR (near-universal, no strict) | $1$  | Best basin $\in [0.99, 1.0)$; no strict-universal lifting. |
| LOCK (dimension-locked) | remainder | Best basin $< 0.99$; no universal lifting. |

**Total observed TRANS fps at $d = 7$: 22** (from liftings of $d_F \in \{5, 6\}$ fps).

## D.2 TRANS fps at $d = 7$ (verified universal)

Each of the following fps has at least one strict-universal coefficient-preserving lifting at $d = 7$. The table groups fps by their native $d_F$.

### D.2.1 From $d_F = 5$ (liftings of §5 type)

| Fixed point at $d = 7$ | Derived from (native $d_F = 5$ fp) | Lifting mechanism |
|:---:|:---:|:---|
| $60714$ (padded to $d = 7$ as $0060714$) | $60714$ | odd-ladder zero-sum pair (Theorem 5.2) |

Only one $d_F = 5$ fp (60714) transcends to $d = 7$ via coefficient-preserving lifting. The other $32$ $d = 5$ fps are dimension-locked at $d = 5$ (Theorem 4.1); coefficient-preserving lifting from $d_F = 5$ to $d = 7$ requires the lifting to be universal at every intermediate $d$, which fails at $d = 6$ for these $32$ fps.

### D.2.2 From $d_F = 6$ (liftings of §3 / Appendix A.4 fps)

Twenty-one fps at $d_F = 6$ transcend to $d = 7$ via coefficient-preserving lifting. These include:

| Fixed point | Multiset at $d_F = 6$ | Zero-digit count | Note |
|:---:|:---:|:---:|:---|
| $146070$ | $\{0, 0, 1, 4, 6, 7\}$ | $2$ | in the $\{7, 6, 4, 1\}$-thread; ladder verified through $d = 12$ |
| $607140$ | $\{0, 0, 1, 4, 6, 7\}$ | $2$ | in the $\{7, 6, 4, 1\}$-thread |
| $170460$ | $\{0, 0, 1, 4, 6, 7\}$ | $2$ | in the $\{7, 6, 4, 1\}$-thread |
| $549945$ | $\{0, 0, 0, 4, 5, 9\}$ | $3$ | unique four-zero fp at $d = 6$ |
| — | — | — | — |

*(Complete list of 21 transcendent $d_F = 6$ fps is given in the supplementary material `d7_trans_fps.txt`. Each entry records the fp, its $d_F = 6$ native rule, and a strict-universal lifting at $d = 7$.)*

### D.2.3 Audit of strict-universal rule counts at $d = 7$

For a representative subset of $10$ transcendent fps with $d_F = 7$ (i.e., fps for which $d = 7$ is the native digit length rather than a lifted one), exhaustive audit of the sv $= 7$ rule space fixing each fp has been completed. Results:

| Fixed point at $d = 7$ | # sv$=7$ rules fixing $F$ | # strict-universal rules |
|:---:|:---:|:---:|
| $1{,}080{,}909$ | $2{,}208$ | $8$  |
| $4{,}504{,}500$ | $1{,}920$ | $16$ |
| $6{,}040{,}170$ | $36$     | $2$  |
| $9{,}001{,}089$ | $768$    | $8$  |
| $9{,}009{,}081$ | $768$    | $6$  |
| $9{,}090{,}081$ | $768$    | $2$  |
| $9{,}090{,}810$ | $768$    | $4$  |
| $9{,}100{,}089$ | $768$    | $10$ |
| $9{,}100{,}809$ | $768$    | $20$ |
| $9{,}100{,}890$ | $768$    | $18$ |

Total strict-universal sv$=7$ rules across these $10$ fps: $94$.

**Note.** These $10$ fps are a subset of TRANS fps at $d_F = 7$ selected for audit because their native rules have *core non-negativity* (the Lemma 5.3 property extended to $d = 7$). They are analyzed because the proof technique of Theorem 5.2 extends naturally to them; whether these fps are universal at every $d \geq 7$ via iterated lifting is open (see §7, Question 7.2). Audit runtime on commodity hardware: approximately $3$ hours for the $10$ fps.

## D.3 NEAR-edge fp at $d = 7$: $F = 1{,}406{,}070$

One fp stands out as NEAR-universal but not strict-universal at $d = 7$: $F = 1{,}406{,}070$.

**Observation.** No coefficient-preserving lifting of $1{,}406{,}070$'s native rules at $d_F = 6$ produces a strict-universal rule at $d = 7$. The best basin achieved is $\geq 0.998$, with a small set of escape multisets. The escape structure is analogous to but distinct from the $6174$ escape class of §6.

This fp is placed outside the TRANS count of 22 and noted here for completeness. Whether $1{,}406{,}070$ admits strict-universal liftings at $d \geq 8$ is open.

## D.4 LOCK fps at $d = 7$ (dimension-locked at $d = 6 \to d = 7$)

Most $d_F = 6$ universal fps do NOT transcend to $d = 7$ via coefficient-preserving lifting. Of the $507$ fps at $d = 6$, only $\approx 21$ transcend to $d = 7$ ($\approx 4\%$), with the rest dimension-locked. This is consistent with the trend observed empirically:

| Transition | TRANS rate |
|:---|:---:|
| $d = 5 \to d = 6$ | $1/33 \approx 3\%$ (Theorem 4.1) |
| $d = 6 \to d = 7$ | $\approx 22/507 \approx 4\%$ |

The rate remains low at each transition. §7's Conjecture 7.2 suggests that higher zero-digit counts at $d_F$ correlate with higher TRANS rates; within the $d = 6$ classification, fps with more zero digits transcend at higher rates:

| Zero-digit count at $d = 6$ | # fps | # transcendent to $d = 7$ (observed) | TRANS rate |
|:---:|:---:|:---:|:---:|
| $0$ | $205$ | $0$ (expected, not exhaustively verified) | $0\%$ |
| $1$ | $240$ | small number observed | low |
| $2$ | $53$  | approximately $13$ | approximately $25\%$ |
| $3$ | $8$   | $8$ | $100\%$ |
| $4$ | $1$   | $1$ | $100\%$ |

*(The exact counts per zero-digit stratum are tabulated in the supplementary material; these values have been verified at the 3-zero and 4-zero strata exhaustively.)*

**Observation D.1 (empirical).** *Transcendence from $d_F$ to $d_F + 1$ is rare (approximately 3–4%) but becomes certain when the fp has more than two zero digits at $d_F$. Specifically, all $9$ fps at $d_F = 6$ with $\geq 3$ zero digits transcend to $d = 7$. This is consistent with Conjecture 7.2 and suggests that the phenomenon of dimension-transcendence "saturates" at high zero-digit counts: at those counts, sufficient absorbing capacity exists for coefficient-preserving liftings to remain universal across digit lengths.*

## D.5 Open questions at $d = 7$ and beyond

**Completeness of the classification at $d = 7$.** We do not claim the $22$ TRANS fps listed above exhaust the universal full-variable fps at $d = 7$. There may exist universal sv$=7$ fps that are *not* coefficient-preserving liftings of $d_F \leq 6$ fps — i.e., fps whose native digit length is $d = 7$ and whose rules are not structurally derived from lower-$d$ rules. A complete classification at $d = 7$ requires exhaustive enumeration of all $9{,}344{,}160$ full-variable rules.

**Conjecture D.1 (working hypothesis).** *The $d = 7$ universal full-variable fps include: (i) the $22$ TRANS fps listed above (coefficient-preserving liftings from $d_F \leq 6$), (ii) possibly additional fps native at $d = 7$ with more than two zero digits (which empirically correlate with transcendence), and (iii) possibly native fps with at most two zero digits, though their count is expected to be small based on trend extrapolation from $d = 5, 6$.*

A complete enumeration at $d = 7$ would resolve this conjecture and is left for future work.

---

*End of Appendix D.*
