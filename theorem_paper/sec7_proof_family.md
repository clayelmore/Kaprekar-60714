### The cycle family, proved

This subsection proves that the family of the first example, the rule $\mathtt{GFEABDHC} - \mathtt{HGDFCEAB}$, has a cycle of period $4$ in every base $b = 5t$ with $t \geq 10$; this supersedes the computed range quoted there. In this subsection $t = b/5$, and the letter $\mathtt{H}$ always denotes the eighth letter $s_7$ of the rule's words, not the bound $H$ of Section 3. For $b = 5t$ define the four sorted digit strings
$$\begin{aligned}
X_1 &= (4t-3,\; 3t+7,\; 3t+3,\; 2t-6,\; 2t-7,\; t+2,\; 1,\; 0),\\
X_2 &= (5t-1,\; 5t-4,\; 3t-5,\; t+2,\; t,\; 4,\; 1,\; 0),\\
X_3 &= (5t-2,\; 5t-5,\; 3t-1,\; 2t+1,\; 2,\; 1,\; 1,\; 0),\\
X_4 &= (5t-1,\; 5t-3,\; 3t+4,\; 3t+1,\; 2t-2,\; 2t-4,\; 1,\; 0).
\end{aligned}$$
Each is listed as $(s_0, \dots, s_7) = (\mathtt{A}, \dots, \mathtt{H})$.

**Proposition 7.1.** *(Proven.) Let $b = 5t$ with $t \geq 10$, and let $K$ be the map of the rule $\mathtt{GFEABDHC} - \mathtt{HGDFCEAB}$ in base $b$. Then $X_1, X_2, X_3, X_4$ are sorted digit strings in base $b$, and the sorted digits of $K(X_1)$, $K(X_2)$, $K(X_3)$, $K(X_4)$ are $X_2$, $X_3$, $X_4$, $X_1$ respectively. The four strings are distinct, so the rule has a cycle of period exactly $4$ in every base $b = 5t \geq 50$ and is not universal in any of these bases. In base $50$ the first two digits of $X_1$ coincide, $X_1 = (37,37,33,14,13,12,1,0)$, and the cycle is the base-$50$ cycle displayed in the first example of this section, which starts at $X_3$. The bound $t \geq 10$ is sharp: for $t \leq 9$ the entries listed for $X_1$ are not in descending order, since $(4t-3) - (3t+7) = t - 10 < 0$.*

*Proof.* Throughout, $t$ is an integer and $b = 5t$.

*The two words.* Number the places $k = 7, 6, \dots, 0$ from the most significant. Word 1 carries the letters $\mathtt{G}, \mathtt{F}, \mathtt{E}, \mathtt{A}, \mathtt{B}, \mathtt{D}, \mathtt{H}, \mathtt{C}$ at these places and word 2 carries $\mathtt{H}, \mathtt{G}, \mathtt{D}, \mathtt{F}, \mathtt{C}, \mathtt{E}, \mathtt{A}, \mathtt{B}$. Let $d_k$ be the digit of word 1 at place $k$ minus the digit of word 2 at place $k$:
$$\begin{aligned}
d_7 &= \mathtt{G}-\mathtt{H}, & d_6 &= \mathtt{F}-\mathtt{G}, & d_5 &= \mathtt{E}-\mathtt{D}, & d_4 &= \mathtt{A}-\mathtt{F},\\
d_3 &= \mathtt{B}-\mathtt{C}, & d_2 &= \mathtt{D}-\mathtt{E}, & d_1 &= \mathtt{H}-\mathtt{A}, & d_0 &= \mathtt{C}-\mathtt{B}.
\end{aligned}$$
Then $W = (\text{word } 1) - (\text{word } 2) = \sum_{k=0}^{7} d_k\, b^k$.

*Borrows.* Choose $\kappa_0, \dots, \kappa_6 \in \{0, 1\}$, put $\kappa_{-1} = \kappa_7 = 0$, and set
$$e_k \;=\; d_k + b\,\kappa_k - \kappa_{k-1} \qquad (0 \leq k \leq 7).$$
Here $\kappa_k = 1$ means that place $k$ borrows $1$ from place $k+1$. The sum telescopes:
$$\sum_{k=0}^{7} e_k b^k \;=\; \sum_{k=0}^{7} d_k b^k + \sum_{k=0}^{6} \kappa_k b^{k+1} - \sum_{k=1}^{7} \kappa_{k-1} b^{k} \;=\; W, \tag{1}$$
an identity of polynomials in $t$ for any choice of the $\kappa_k$. If moreover $0 \leq e_k \leq b-1$ for every $k$ and some $e_k \geq 1$, then (1) is the base-$b$ expansion of $W$, so $W > 0$, the image of the string is $|W| = W$, and its digits are $e_0, \dots, e_7$. Its sorted digits are the $e_k$ in descending order.

*Step 0: the four strings are valid.* A string $(s_0, \dots, s_7)$ is a sorted digit string in base $b$ exactly when the nine numbers $b-1-s_0$, $s_0-s_1$, ..., $s_6-s_7$, $s_7$ are all nonnegative. For the four strings they are:

| quantity | $X_1$ | $X_2$ | $X_3$ | $X_4$ |
|---|---|---|---|---|
| $b-1-s_0$ | $t+2$ | $0$ | $1$ | $0$ |
| $s_0-s_1$ | $t-10$ | $3$ | $3$ | $2$ |
| $s_1-s_2$ | $4$ | $2t+1$ | $2t-4$ | $2t-7$ |
| $s_2-s_3$ | $t+9$ | $2t-7$ | $t-2$ | $3$ |
| $s_3-s_4$ | $1$ | $2$ | $2t-1$ | $t+3$ |
| $s_4-s_5$ | $t-9$ | $t-4$ | $1$ | $2$ |
| $s_5-s_6$ | $t+1$ | $3$ | $0$ | $2t-5$ |
| $s_6-s_7$ | $1$ | $1$ | $1$ | $1$ |
| $s_7$ | $0$ | $0$ | $0$ | $0$ |

Every entry is either a nonnegative constant or of the form $at + c$ with $a > 0$, hence nondecreasing in $t$. The entries $t+2$, $t+9$, $t+1$, $2t+1$, $2t-1$, $t+3$ are nonnegative for all $t \geq 1$. The others are nonnegative exactly in the following ranges: $t - 10 \geq 0$ for $t \geq 10$; $t - 9 \geq 0$ for $t \geq 9$; $2t - 7 \geq 0$ (in $X_2$ and in $X_4$) and $t - 4 \geq 0$ for $t \geq 4$; $2t - 5 \geq 0$ for $t \geq 3$; $2t - 4 \geq 0$ and $t - 2 \geq 0$ for $t \geq 2$. Hence $X_2$ and $X_4$ are valid for $t \geq 4$, $X_3$ for $t \geq 2$, and $X_1$ for $t \geq 10$; all four are valid for $t \geq 10$. The only constraint that binds at $t = 10$ is $s_0 - s_1 = t - 10$ for $X_1$, and it fails for every $t \leq 9$. In particular all entries of all four strings lie in $[0, b-1]$ for $t \geq 10$.

*Steps 1 to 4.* For each step the table lists, place by place, the difference $d_k$ (obtained by substituting the letters of the current string into the formulas above), the borrow $\kappa_k$, the resulting digit $e_k$, and the letter of the next string that $e_k$ equals. In each table the letter row is a permutation of $\mathtt{A}, \dots, \mathtt{H}$, so the eight digits $e_k$ are the entries of the next string, as a multiset. By Step 0 they lie in $[0, b-1]$ and their descending order is the next string, for $t \geq 10$. At least one digit is at least $1$ (the digit $e_7 = 1$ in Steps 1, 2, 4 and $e_6 = 5t - 1$ in Step 3), so the remark after (1) applies. Where two entries of the next string are equal (the two $1$s of $X_3$, and $\mathtt{A} = \mathtt{B} = 37$ of $X_1$ at $t = 10$), either letter may be read; the multiset is the same.

*Step 1: $X_1 \to X_2$.* Here $\mathtt{A} = 4t-3$, $\mathtt{B} = 3t+7$, $\mathtt{C} = 3t+3$, $\mathtt{D} = 2t-6$, $\mathtt{E} = 2t-7$, $\mathtt{F} = t+2$, $\mathtt{G} = 1$, $\mathtt{H} = 0$. Places $0$, $1$, $5$ borrow.

| place $k$ | $7$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ | $0$ |
|---|---|---|---|---|---|---|---|---|
| $d_k$ | $1$ | $t+1$ | $-1$ | $3t-5$ | $4$ | $1$ | $3-4t$ | $-4$ |
| $\kappa_k$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ | $1$ | $1$ |
| $e_k$ | $1$ | $t$ | $5t-1$ | $3t-5$ | $4$ | $0$ | $t+2$ | $5t-4$ |
| letter of $X_2$ | $\mathtt{G}$ | $\mathtt{E}$ | $\mathtt{A}$ | $\mathtt{C}$ | $\mathtt{F}$ | $\mathtt{H}$ | $\mathtt{D}$ | $\mathtt{B}$ |

$$\begin{aligned}
W_1 &= 93750t^7 + 15625t^6 - 1250t^5 - 3125t^4\\
&\quad + 500t^3 + 5t^2 + 15t - 4 \;>\; 0.
\end{aligned}$$

*Step 2: $X_2 \to X_3$.* Here $\mathtt{A} = 5t-1$, $\mathtt{B} = 5t-4$, $\mathtt{C} = 3t-5$, $\mathtt{D} = t+2$, $\mathtt{E} = t$, $\mathtt{F} = 4$, $\mathtt{G} = 1$, $\mathtt{H} = 0$. Places $0$, $1$, $5$ borrow.

| place $k$ | $7$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ | $0$ |
|---|---|---|---|---|---|---|---|---|
| $d_k$ | $1$ | $3$ | $-2$ | $5t-5$ | $2t+1$ | $2$ | $1-5t$ | $-2t-1$ |
| $\kappa_k$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ | $1$ | $1$ |
| $e_k$ | $1$ | $2$ | $5t-2$ | $5t-5$ | $2t+1$ | $1$ | $0$ | $3t-1$ |
| letter of $X_3$ | $\mathtt{F}$ | $\mathtt{E}$ | $\mathtt{A}$ | $\mathtt{B}$ | $\mathtt{D}$ | $\mathtt{G}$ | $\mathtt{H}$ | $\mathtt{C}$ |

$$\begin{aligned}
W_2 &= 78125t^7 + 46875t^6 - 3125t^5 - 2875t^4\\
&\quad + 125t^3 + 25t^2 + 3t - 1 \;>\; 0.
\end{aligned}$$

*Step 3: $X_3 \to X_4$.* Here $\mathtt{A} = 5t-2$, $\mathtt{B} = 5t-5$, $\mathtt{C} = 3t-1$, $\mathtt{D} = 2t+1$, $\mathtt{E} = 2$, $\mathtt{F} = \mathtt{G} = 1$, $\mathtt{H} = 0$. Places $0$, $1$, $5$, $6$ borrow.

| place $k$ | $7$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ | $0$ |
|---|---|---|---|---|---|---|---|---|
| $d_k$ | $1$ | $0$ | $1-2t$ | $5t-3$ | $2t-4$ | $2t-1$ | $2-5t$ | $4-2t$ |
| $\kappa_k$ | $0$ | $1$ | $1$ | $0$ | $0$ | $0$ | $1$ | $1$ |
| $e_k$ | $0$ | $5t-1$ | $3t+1$ | $5t-3$ | $2t-4$ | $2t-2$ | $1$ | $3t+4$ |
| letter of $X_4$ | $\mathtt{H}$ | $\mathtt{A}$ | $\mathtt{D}$ | $\mathtt{B}$ | $\mathtt{F}$ | $\mathtt{E}$ | $\mathtt{G}$ | $\mathtt{C}$ |

$$\begin{aligned}
W_3 &= 78125t^7 - 6250t^6 + 6250t^5 - 1625t^4\\
&\quad - 450t^3 - 50t^2 + 8t + 4 \;>\; 0.
\end{aligned}$$

*Step 4: $X_4 \to X_1$.* Here $\mathtt{A} = 5t-1$, $\mathtt{B} = 5t-3$, $\mathtt{C} = 3t+4$, $\mathtt{D} = 3t+1$, $\mathtt{E} = 2t-2$, $\mathtt{F} = 2t-4$, $\mathtt{G} = 1$, $\mathtt{H} = 0$. Places $0$, $1$, $5$ borrow.

| place $k$ | $7$ | $6$ | $5$ | $4$ | $3$ | $2$ | $1$ | $0$ |
|---|---|---|---|---|---|---|---|---|
| $d_k$ | $1$ | $2t-5$ | $-t-3$ | $3t+3$ | $2t-7$ | $t+3$ | $1-5t$ | $7-2t$ |
| $\kappa_k$ | $0$ | $0$ | $1$ | $0$ | $0$ | $0$ | $1$ | $1$ |
| $e_k$ | $1$ | $2t-6$ | $4t-3$ | $3t+3$ | $2t-7$ | $t+2$ | $0$ | $3t+7$ |
| letter of $X_1$ | $\mathtt{G}$ | $\mathtt{D}$ | $\mathtt{A}$ | $\mathtt{C}$ | $\mathtt{E}$ | $\mathtt{F}$ | $\mathtt{H}$ | $\mathtt{B}$ |

$$\begin{aligned}
W_4 &= 109375t^7 - 81250t^6 - 7500t^5 + 2125t^4\\
&\quad - 850t^3 + 50t^2 + 3t + 7 \;>\; 0.
\end{aligned}$$

In each step the displayed polynomial equals $\sum_k d_k b^k$ with $b = 5t$, and its positivity for $t \geq 10$ is the positivity established after (1); it is not needed separately. Each $W_i$ vanishes at $t = 1/5$, that is, it is divisible by $b - 1$, as Lemma 2.3(a) requires.

*Period and non-universality.* The four strings are distinct for $t \geq 10$: the first digit of $X_1$ is $4t - 3$, below the first digits $5t-1$, $5t-2$, $5t-1$ of the others; $X_3$ has first digit $5t-2$ and $X_2$, $X_4$ have $5t-1$; and $X_2$, $X_4$ differ in their second digits $5t-4$ and $5t-3$. Let $x$ be any string whose sorted digits are $X_1$. By Steps 1 to 4 the sorted digits of $K(x), K^2(x), K^3(x), K^4(x)$ are $X_2, X_3, X_4, X_1$. Since $K$ depends only on the letters, that is, on the sorted digits, and $K^4(x)$ has the same sorted digits as $x$, we get $K^5(x) = K(x)$. The strings $K(x), \dots, K^4(x)$ have four different multisets of digits, so they are four distinct strings, and they form a cycle of $K$ of length $4$. A string $F$ with $K(F) = F$ has the same sorted digits as its image, while consecutive strings on the orbit of $x$ do not, so no string on this orbit is fixed and the orbit never reaches a fixed string. Since $X_1$ is not a repdigit ($s_0 = 4t - 3 > 0 = s_7$), the rule is not universal in base $b$ (Definition 2.2). $\blacksquare$

A computer-algebra check accompanies the proof: it verifies the identity (1), the differences, digits, and expansions $W_1, \dots, W_4$ in each table as polynomial identities in $t$, each inequality of Step 0 from its stated threshold, and the sharpness of each threshold; it also iterates the rule directly on strings, from the two words, in every base $b = 5t$ with $10 \leq t \leq 2000$.

**Below the threshold** *(Computed)*. For $4 \leq t \leq 9$ (bases $20$ to $45$) the entries of $X_2$, $X_3$, $X_4$ are still valid and the computations of Steps 2, 3, and 4 still hold: the digits of $K(X_4)$ are the eight entries listed for $X_1$, all in $[0, b-1]$. But they are no longer in that order, since $3t + 7 > 4t - 3$ (and further entries are out of order for $t \leq 8$), so the sorted digits of $K(X_4)$ form a different string, and direct iteration shows that its orbit ends at the fixed point whose sorted digits are $(b-1, b-1, b-2, 1, 0, 0, 0, 0)$, in each of these six bases. For $t \leq 3$ some listed entries are negative or out of order already in $X_2$. So the family gives a cycle exactly for $t \geq 10$, and the base-$50$ cycle is its first member.
