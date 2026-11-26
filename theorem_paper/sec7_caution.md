## A caution about small bases

The theorems of Sections 3 and 4 hold in every base $b \geq 3$, and those of Section 5 in every even base, because they were proved there. This section records two examples in which a rule passes complete enumeration in every small base tested and fails in large bases. The two examples were found by computation and are first described as computed. Propositions 7.1 and 7.3 then prove that each rule fails in every base of an infinite range. The examples are not offered as evidence of any general law.

### A cycle that scales with the base

The six-letter rule $\mathtt{EABDFC} - \mathtt{DFCEAB}$ is a half-swap rule on the same pairing as $R_3$, and at length $6$ it is universal with endpoint $(b-1)(b^3-1)$ in every base from $3$ to $80$ by complete enumeration (a proof for every base, along the lines of Section 3, is in the project notes and is not reproduced here). One way to extend it to length $8$ keeps the coefficients of the letters $\mathtt{A}$ to $\mathtt{E}$, gives the two new gaps the weights $b^6 - b$ and $b^7 - b$, and changes the last coefficient from $b - b^4$ to $b - b^7$. The result is
$$\mathtt{GFEABDHC} - \mathtt{HGDFCEAB}.$$
This rule is universal at length $8$ in every base from $3$ to $26$, by complete enumeration of all digit multisets. In base $50$ it is not: the sorted digit strings
$$\begin{aligned}(48,45,29,21,2,1,1,0) &\to (49,47,34,31,18,16,1,0) \\ &\to (37,37,33,14,13,12,1,0) \to (49,46,25,12,10,4,1,0)\end{aligned}$$
form a cycle of period $4$. The cycle belongs to a family. For $b$ a multiple of $5$ put $t = b/5$; then
$$(4t-3,\; 3t+7,\; 3t+3,\; 2t-6,\; 2t-7,\; t+2,\; 1,\; 0)$$
lies on a cycle of period $4$ in every base $b = 55, 60, \dots, 2000$ and in the bases $2500$, $10000$, and $100005$ (direct iteration in each of these $393$ bases; base $50$ is the same family with two digits tied). Proposition 7.1 below proves this for every base $5t$ with $t \geq 10$. Divided by $b$, the cycle tends to a fixed orbit with coordinates in fifths. Complete enumeration in the bases $3$ to $26$ does not see it.

### A cycle that does not depend on the base

The second example is inside the family of Section 5. The ten-digit half-swap rule
$$\mathtt{AFEJBGIDHC} - \mathtt{GIDHCAFEJB}$$
is universal in every base from $3$ to $13$ and in base $16$ (complete enumeration). In the notation of Section 5, its state after one step is a multiset of five deficits. The three states
$$(13,13,15,25,31) \to (1,1,6,17,38) \to (4,4,18,21,36) \to (13,13,15,25,31)$$
form a cycle in every base from $77$ to $1200$, and in the bases $100003$, $1000003$, and $1000000007$: the same deficits, whatever the base. The largest deficit on the cycle is $38$, so the cycle cannot exist until $b \geq 77$; from there on it is always present in the range tested, and Proposition 7.3 below proves that it is present in every base $b \geq 77$. In digits, five letters sit a fixed distance below $b-1$ and five a fixed distance above $0$, so a random string in a large base is almost never near it. This rule had passed random sampling in bases $97$, $200$, and $640$.

### What the examples show

Two different mechanisms appear: a cycle whose digits grow in proportion to $b$, and a cycle whose deficits are constant in $b$. In both cases the rule is universal in every small base that was tried. For the half-swap family the second mechanism suggests a base-free object: a map on tuples of nonnegative integers (the deficits) that does not mention $b$. Lemma 7.2 below makes this precise and proves it: for each state, once the base is large compared with the deficits, the next state is given by a map that does not involve $b$.

The conclusion is narrow. For rules of this kind, agreement in every base from $3$ to $26$ (complete enumeration), or in sampled bases up to $640$, is not evidence of universality in every base. The only rules in this paper asserted to be universal in every base are those of Theorems 3.3 and 4.16, and they are asserted because they are proved. The rest of this section proves the two failures.
