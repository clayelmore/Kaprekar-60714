# Venue Selection Memo

Prepared April 26, 2026. **Revised** April 26, 2026 to add primary-source
citations after v8 council review flagged unsourced AI-policy claims.

## TL;DR — Recommended path

1. **arXiv post first.** Within 1-2 days.
2. **Submit to Experimental Mathematics.** Strongest natural fit. Governed by
   the standard Taylor & Francis AI policy (transparency + acknowledgment;
   author retains accountability).
3. **OEIS submission** referencing the arXiv preprint.
4. If Experimental Mathematics rejects on framing grounds, **fall back to
   Journal of Integer Sequences** (JIS), which has the most operationally
   detailed AI policy in mathematics publishing today and which fits the
   OEIS-adjacent flavor of the paper.

All AI-policy claims below are **directly quoted from primary sources**
fetched April 26, 2026. The quotation marks indicate verbatim text from the
journal's own page; sources cited in footnotes.

## Three viable venues, ranked

### 1. Experimental Mathematics — recommended primary target

- **Publisher:** Taylor & Francis (since 2010; founded 1992 by Epstein, Levy,
  Peters).
- **Editor-in-chief (Wikipedia, retrieved 2026-04-26):** Alexander Kasprzyk
  (University of Nottingham).
- **Mission statement (publisher's About page):** "Original papers featuring
  formal results inspired by experimentation, conjectures suggested by
  experiments, and data supporting significant hypotheses." Founded
  specifically because traditional journals were reluctant to accept
  experimental-mathematics work regardless of merit.

**AI policy** (governed by the publisher-wide Taylor & Francis policy at
[taylorandfrancis.com/our-policies/ai-policy/](https://taylorandfrancis.com/our-policies/ai-policy/)
and the journal-specific Author Services authorship guidance at
[authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/](https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/)).
The relevant verbatim text from the publisher policy:

> "Authors are accountable for the originality, validity, and integrity of the
> content of their submissions. In choosing to use Generative AI tools,
> journal authors are expected to do so responsibly and in accordance with our
> journal editorial policies on authorship and principles of publishing
> ethics... [T]hese tools, where used appropriately and responsibly, have the
> potential to augment research outputs..."

> "AI tools must not be listed as an author. Authors must, however,
> acknowledge all sources and contributors included in their work. Where AI
> tools are used, such use must be acknowledged and documented appropriately."

And from the Author Services page:

> "Please add a statement in the Methods or Acknowledgments section which
> includes: The full name of the tool used (with version number). How it was
> used. The reason for use."

The publisher policy also notes that *"some journals may not allow use of
Generative AI tools beyond language improvement, therefore authors are
advised to consult with the editor of the journal prior to submission."*
Experimental Mathematics does not (as of 2026-04-26) appear to publish a
journal-specific override. Standard practice would be to follow the
publisher policy plus a brief pre-submission inquiry to the editor if any
specific AI-tool use is unusual.

- **Open access:** Hybrid (Open Select). APC if author wants OA; otherwise no
  charge.
- **Quartile:** Q1 in Mathematics (miscellaneous) per SCImago. SJR 0.718.
- **Why this is the strongest fit:** The paper's structure — exhaustive
  enumeration at d ≤ 6, computational discovery of 60714, lifting machinery
  proven analytically, conjecture about basin density — is exactly what the
  journal exists to publish. The mission statement explicitly welcomes
  "conjectures suggested by experiments." Conjecture 7.6 (Basin Density
  Conjecture) and Open Questions 7.1-7.5 fit naturally. The integer-led
  framing is acceptable here.

### 2. Journal of Integer Sequences (JIS) — strong fallback

- **Publisher:** University of Waterloo. Editor-in-chief: Jeffrey Shallit.
- **Open access:** Yes. No APCs, no submission charges. Volunteer editorial
  board.

**AI policy** (verbatim from
[cs.uwaterloo.ca/journals/JIS/](https://cs.uwaterloo.ca/journals/JIS/),
fetched 2026-04-26):

> "Do not use ChatGPT, Grok, Gemini, or any LLM (large language model) to
> write the text (the actual English words) of your paper. If you are unsure
> about English usage, an LLM may be helpful in pointing out deficiencies,
> but the words of your paper must be your own."

> "It is permissible to use an LLM to help locate references in the
> literature, but you must check each suggested reference to ensure it
> actually exists and is appropriate in the context."

> "It is permissible to use an LLM to suggest proof techniques or proofs, but
> then you must give explicit credit to the LLM, within the text of your
> paper, for these suggestions. Be sure to carefully check the details of any
> suggested proofs. Treat attributions the way you would any human author."

> "Use of these AI tools without explicit and detailed delineation of their
> role in the paper will result in immediate rejection. Depending on the
> severity of the offense, you could also get a lifetime ban from the
> Journal."

The JIS policy is structurally **two clauses**: a strict prohibition on LLM
prose-writing, plus a permissible-with-credit clause for proof techniques.
The "immediate rejection / lifetime ban" enforcement is for hidden use, not
for disclosed use under the permissible clause.

- **Operational implications for this paper:** The paper's prose is the
  author's own (LLM was not used to produce the paper's English). LLM was
  used (a) for proof-correctness review against the paper's verification
  scripts, (b) for prose editing of mathematical statements (catching the
  v3, v6, v8 enumeration errors), and (c) for code review. JIS would
  classify (a) and possibly (b) as "suggesting proof techniques or proofs"
  and would require explicit credit in the paper text. The recommended
  acknowledgments paragraph (below) handles this.
- **Scope fit:** "A new integer sequence and its nontrivial interesting
  properties" is one of the listed paper types. Lemma 5.2.2's sequence is
  a new integer sequence with closed form and combinatorial origin. JIS is
  the natural home for the sequence result and an acceptable home for the
  broader paper.
- **Caveat:** Smaller venue (h-index 39 vs Experimental Mathematics' similar
  range). Median 197 days from submission to final decision (per JIS's
  current backlog statement, Volume 28).

### 3. Integers (Electronic Journal of Combinatorial Number Theory) — DO NOT SUBMIT

**AI policy** (verbatim from
[math.colgate.edu/~integers/submit.html](https://math.colgate.edu/~integers/submit.html),
fetched 2026-04-26):

> "Use of AI (artificial intelligence): Integers will not consider any article
> that makes use of artificial intelligence in producing mathematics, computer
> code, bibliographic information, or other content. This does not apply to
> the use of basic tools to improve the presentation, such as grammar and
> spelling."

This disqualifies the paper. Even charitable interpretations of "basic
tools to improve presentation" do not cover the v3 C.9 deletion, the v4
Lemma C.10 introduction, or the v5/v6/v7/v8 corrections — these were
material edits to mathematical content, suggested through the
proof-correctness review loop. Don't submit here.

## Other venues considered, not recommended for this paper

- **Journal of Number Theory (Elsevier):** Higher prestige than Experimental
  Mathematics but more conservative in framing. Would push back on
  integer-led presentation. Better suited to a hypothetical v9 with
  structural framing led; not appropriate for current v7-v8.
- **Forum of Mathematics, Sigma:** Q1 venue, theorem-heavy. The
  conjecture-heavy nature of §7 doesn't fit.
- **arXiv-only (no journal):** Real option if peer review is not the
  priority. Not recommended here because the paper has been adversarially
  reviewed eight times by AI; an additional independent expert review
  through a peer-review venue is high-value.

## On AI-collaboration disclosure

Whatever venue you target, the paper should include an explicit note about
AI-tool usage. Drafting language for an Acknowledgments paragraph:

> "The mathematical content of this paper was developed by the author. Claude
> (Anthropic; Claude Opus 4.6 / 4.7, accessed 2025-2026) was used as a
> collaboration tool: as a sounding board for proof structure, as a
> proof-correctness reviewer (running computational checks against claimed
> enumerations), and for prose editing of mathematical statements. Eight
> rounds of adversarial review by separate Claude instances surfaced (and
> corrected) defects in Lemma C.9's parenthetical algebraic decomposition,
> Lemma C.10's enumeration counts, and the OEIS submission's binomial
> argument. The proof-correctness review process is summarized in the public
> commit history at <github URL>. All theorems, lemmas, conjectures, proofs,
> and computational results are the author's. The author takes full
> responsibility for the paper's content, including any remaining errors."

This language is honest about how the work was developed without
overclaiming the AI's contribution. It satisfies both the T&F transparency
requirement (full tool name with version, how used, reason for use) and the
JIS explicit-credit requirement (acknowledged role in proof technique
suggestions, with author retaining accountability).

## Concrete recommended sequence

Today (April 26):

1. Push the v8-corrected bundle (this commit).
2. Add the AI-collaboration disclosure paragraph to the paper's Acknowledgments
   section.
3. Convert paper from Markdown to LaTeX for arXiv (one-time effort).

Within 1-3 days:

4. Post arXiv preprint. Get DOI.

Within 1 week of arXiv post:

5. Submit to Experimental Mathematics, citing arXiv DOI. The paper's
   Methods/Acknowledgments includes the AI-tool disclosure required by T&F
   policy.
6. Submit OEIS sequence (B_NEW first) with paper as reference.

If Experimental Mathematics rejects (estimated 3-6 months):

7. Light revision based on referee comments.
8. Resubmit to JIS as the integer-sequence-focused fallback. The
   acknowledgments paragraph already includes the "explicit credit to the
   LLM, within the text of the paper" that JIS's policy requires.

## Notes on the framing critique (recurring across reviews)

The critique that the paper leads with the integer 60714 rather than the
structural framework has been Major-but-not-blocking across all eight review
rounds. Different venues will weight this differently:

- Experimental Mathematics: integer-led framing acceptable
- JIS: integer-led framing fine (the integer sequence is the focus)
- Journal of Number Theory: would likely push back
- Forum of Mathematics, Sigma: would likely push back

Because Experimental Mathematics and JIS both accept integer-led framing,
no rewrite is needed for the recommended path. If the paper goes to JNT or
similar later, a §1 rewrite to lead with rank-4 reframing would be in
order.

## Sources (all verified 2026-04-26)

- Taylor & Francis AI Policy: https://taylorandfrancis.com/our-policies/ai-policy/
- Taylor & Francis Author Services - Authorship: https://authorservices.taylorandfrancis.com/editorial-policies/defining-authorship-research-paper/
- Journal of Integer Sequences submission page: https://cs.uwaterloo.ca/journals/JIS/
- Integers submission page: https://math.colgate.edu/~integers/submit.html
- Experimental Mathematics About: https://www.tandfonline.com/journals/uexm20

## v8 council review acknowledgment

The v8 council review correctly flagged that the previous version of this
memo (a) did not cite primary sources for AI policies and (b) characterized
the JIS policy in ways that could not be reconciled with the canonical text
without seeing both clauses together. This revision quotes both venues
verbatim from primary sources, and the "permissible-with-credit" clause is
shown alongside the "immediate rejection / lifetime ban" enforcement clause
so a reader can see how they fit together.

Where the previous memo characterized JIS as "the most operationally clear
AI-collaboration policy in mathematics publishing today," that
characterization is retained in this revision because, with both clauses in
view, JIS does provide more operational specificity than other venues
(Integers' flat ban is operationally clear but excludes the paper; T&F
policy is permissive but less operationally specific to proof-technique
suggestions).
