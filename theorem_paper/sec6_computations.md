## Computations

This section collects the machine results. Each is **Computed**: a finite enumeration, complete unless the word "sampled" appears. None is used in a proof in Sections 3 to 5; they test the proofs and describe the family of Section 5 in base $10$. Scripts and outputs are linked from the project page given in Methods and provenance.

### Tests of Theorems 3.3 and 4.16

The rules $R_n$ and $M_n$ were coded from Definitions 3.2 and 4.3 as printed and run on every digit multiset of the given length.

| rule | lengths | bases | result |
|---|---|---|---|
| $R_n$, $n = 3, 4, 5, 6$ | $6, 8, 10, 12$ | $3, 4, 5, 7, 10$ | all reach $(b-1)(b^n-1)$ |
| $M_n$, $n = 3, 4, 5$ | $7, 9, 11$ | $3, 4, 5, 7, 10$ | all reach $(b-1)(b^{n+1}-1)$ |

The largest case is $293{,}930$ multisets ($n = 6$, $b = 10$). The most steps observed in base $10$ are $6, 5, 4, 4$ for $R_3, \dots, R_6$ and $5, 7, 4$ for $M_3, M_4, M_5$. The reduced maps of Sections 3 and 4 (the formulas for $V$ and for the next state in cases (G) and (Z)) agree with the direct rule on every state for $n = 3$ to $6$ (even lengths) and $n = 3$ to $8$ (odd lengths) in every base from $3$ to $12$. Iterating the reduced maps from every state reaches $\tau$ in all bases tried: for $R_3$ in bases $3$ to $201$, with at most $12$ reduced steps and a longest bad run of $9$ (at $b = 199$), against the proved bound $(b+7)/2 = 103$; for $M_n$ in bases $3$ to $40$ ($n = 3, 4, 5$), $3$ to $32$ ($n = 6$), $3$ to $26$ ($n = 7$), and $3$ to $22$ ($n = 8$). No bad run exceeded its proved bound. Counting from an arbitrary state, which need not be the first image of a string, the step count $H + 3$ of Theorem 4.16 ($n$ odd) is attained at $b = 3$, and the run bound $2H - 2$ of Lemma 4.15 is attained at $b = 5$. At $b = 5$ the count used in the proof for $n$ odd (one more than the first $t$ with $S_t = \tau$) equals $H + 3 = 5$, but $F$ itself is reached after $4$ applications; over all strings the most steps for $M_3$ are $3$ and $4$ in these two bases. For $M_4$ the longest bad runs grow linearly with the base: $4$, $8$, $14$, $18$ at $b = 10, 20, 30, 40$, against the bounds $6$, $16$, $26$, $36$.

An earlier, independent set of programs ran the combined statement of Theorem 4.17 on every digit multiset for every length $L = 6$ to $13$ in every base $b = 3$ to $16$ (about $145$ million multisets), with no exception.

### The half-swap family in base 10

Theorem 5.9 reduces each half-swap rule in base $10$ to a table of $\binom{n+4}{n}$ states: $35$, $70$, $126$ at $6$, $8$, $10$ digits. Running the criterion on every half-swap rule of each length, with rules counted up to the global sign, gives the following.

| digits | rules covering every gap | universal rules | endpoints |
|---|---|---|---|
| $4$ | $8$ | $0$ | $0$ |
| $6$ | $240$ | $12$ | $6$ |
| $8$ | $14{,}208$ | $520$ | $136$ |
| $10$ | $1{,}355{,}520$ | $71{,}390$ | $9{,}524$ |

At ten digits there are $99{,}999$ possible values of $m$; $35{,}020$ of them are fixed by some rule and $9{,}524$ are the endpoint value of a universal rule. Examples of endpoints are $16748325$, $01239876$, and $6870031299$. Every endpoint in the family is a block of digits followed by its digit complement.

Class C (Definition 5.10): among rules that cover every gap there are none at $6$ or $8$ digits, and $5{,}590$ rules with $688$ endpoints at $10$ digits. By Theorem 5.13 each of these is the first member of a sequence of universal rules, one at every even length from $10$ on. The criterion itself was compared with complete enumeration of all digit multisets on $360$ randomly drawn half-swap rules (drawn with replacement, so with repeats; half of the draws universal) in bases $4$, $6$, and $10$ at $6$ and $8$ digits: the verdicts and the endpoints agree in every case. As a test of the lifting theorem, $400$ class-C rules were lifted twice in all four orders ($2{,}400$ distinct rules, $800$ at $12$ digits and $1{,}600$ at $14$): every one has the predicted endpoint by its state table, and for the rule of Example 5.16 the two lifts at $12$ digits and the four at $14$ digits were also confirmed on every digit multiset ($293{,}930$ and $817{,}190$ multisets).

### Half-swap rules across bases

At $6$ and $8$ digits, $12$ and $112$ half-swap rules are universal in every base from $7$ to $13$ and in base $16$ (complete census), and show no failure on any state in bases $22$, $31$, $50$, and $97$ (at $8$ digits in base $200$, on a random sample of $300{,}000$ states). In the odd bases $31$ and $97$ this check of states is not a proof of universality there (Section 5, Limits). Their endpoints are $6$ and $24$ arrangements of the one digit multiset consisting of $b-2$, $1$, $n-1$ digits $b-1$, and $n-1$ zeros. The rule $R_n$ is one of them at each length. One other, $\mathtt{EABDFC} - \mathtt{DFCEAB}$ at $6$ digits, has a proof along the lines of Section 3 in the project notes, not reproduced here. For the rest, universality in every base is not proved (Open problem 6).

At $10$ digits the picture is different. $25{,}350$ rules are universal in all of the bases $7$ to $13$ and $16$. Sampling in further bases ($313$ to $3467$, and states near the corner of small deficits) finds cycles for some of them, including the second rule of Section 7 (Proposition 7.3), which had passed sampling in bases $97$, $200$, and $640$. A sample cannot certify the rest. We make no claim about which of them, apart from $R_5$, are universal in every base.

### Sampled targets

To see how often a number can be an endpoint, random targets were drawn in base $10$ and rules fixing the target were tested by complete enumeration: all of them when there are at most $20{,}000$, and a sample otherwise. Targets are $L$-digit strings with digit sum divisible by $9$, not repdigits; $300$ per length for $L \leq 10$ and $200$ per length above.

| $L$ | targets satisfying Lemma 2.3(b) | universal rule found |
|---|---|---|
| $6$ | $54$ | $2$ |
| $7$ | $102$ | $13$ |
| $8$ | $108$ | $28$ |
| $9$ | $144$ | $83$ |
| $10$ | $165$ | $142$ |
| $11$ | $124$ | $115$ |
| $12$ | $150$ | $148$ |
| $13$ | $148$ | $146$ |

Each rule found is a complete enumeration at its length and is a fact about that one target. The trend with $L$ is an observation on a sample. It is the reason for stating the inverse problem (Open problem 1) and is not evidence for any particular answer to it. Two examples outside the half-swap family: $5445$ at $9$ digits is the endpoint of $\mathtt{HDCGFIEBA} - \mathtt{ICDHGBAEF}$, and $1657575000000$ at $13$ digits is the endpoint of $\mathtt{BACEGFJIMHLKD} - \mathtt{CGHBDAFLKIMJE}$, both in base $10$ by complete enumeration.
