# Stage prompts

Set prompts for driving the pipeline one stage at a time. Read this when the user asks how
to run a stage well, or wants a prompt to paste.

Why per-stage prompts instead of one mega-prompt: stage gating is the mechanism. A single
"do all nine stages" prompt produces all the artifacts in one pass and reviews nothing —
which is a different, worse tool. Each stage below has three roles:

- **The author** — the skill producing the artifact. The author prompt is what the user pastes.
- **The critic** — the same model, re-invoked against `critic-rubric.md` after the artifact
  exists. The critic prompt is deliberately separate so review is a fresh read, not a
  self-congratulation appended to generation.
- **The gate** — the human decision that unlocks the next stage: accept, revise, or override.
  The skill never takes this decision.

Every author prompt ends the same way on purpose: *do not continue to the next stage.*

---

## Before Stage 0 — the elicitation interview (tier 0 only)

**Author prompt**
> I have no documents to give you. Run the context elicitation interview from
> references/context-elicitation.md — one slot at a time, read back what you write, tag
> everything as reported-by-me, and put my "believed but never checked" answers under
> Declared assumptions. Write wb/context/elicited.md and tell me what a real document
> would still add.

**Gate** — skim `elicited.md` before Stage 0 begins. It is your own testimony about to be
used as context; correct it now or it propagates.

## Stage 0 — Intake

**Author prompt**
> Run the working-backwards skill, Stage 0 only. The problem: <what happened, who noticed,
> what evidence exists>. Tag every claim [OBSERVED] with its source, [REPORTED] with the
> role, [ASSUMED], or [UNKNOWN]. Push back once if my customer is "everyone." Recommend a
> mode and say which stages it skips. Check wb/context/ and state the tier you are operating
> at and what you therefore cannot evaluate. Do not write the press release.

**Critic prompt**
> Review 00-intake.md against dimensions 1, 2 and 8 of the critic rubric. Is this a problem
> statement or a solution wearing a problem costume? Name the claim doing the most work with
> the least provenance.

**Gate** — is the customer a segment you could build a list of ten from? If not, nothing
downstream is worth generating. (Every later gate also asks that stage's two thinking
questions — see the gate table in references/interrogation.md — and your answers are
recorded in DECISIONS.md beside the verdict.)

## Stage 1 — Press release

**Author prompt**
> Stage 1. Write the press release from 00-intake.md: heading, subheading, dated summary,
> problem in the customer's voice, solution, what customers use today and why it falls
> short, one labelled illustrative customer quote, a spokesperson quote that carries the
> why-now, getting started. One page. Carry every provenance tag inline. Where I gave you
> no number, write [NEEDS EVIDENCE: …] — do not invent one. Number the paragraphs ¶1–¶7;
> requirements will cite them. Do not write the FAQs.

**Critic prompt**
> Review 01-press-release.md against all eight dimensions. For 1–3, 5, 7, 8 return
> PASS / REVISE / BLOCK with the specific sentence to change. For 4 and 6, emit questions
> with owner roles to QUESTIONS.md — never a verdict. Would a team reorganise a quarter
> around this subheading? If the honest answer is no, say so.

**Gate** — the valuable-destination test. A ho-hum press release is discarded here, not
improved by a better FAQ.

## Stage 2 — FAQs

**Author prompt**
> Stage 2. Write the external, internal and regional FAQ banks from the approved press
> release, using references/faq-banks.md. Ask the hostile version of every internal
> question, in the voice of the leader who would ask it. Tag every answer ANSWERED, OPEN or
> BLOCKER. Every BLOCKER gets a record in BLOCKERS.md — category, severity, Ask, owner
> role, Status: OPEN. You never resolve one. If the internal bank surfaces nothing
> uncomfortable, rewrite it — it wasn't honest.

**Critic prompt**
> Review the three banks. Are answers tagged ANSWERED actually sourced, or are they OPEN in
> costume? Does any blocker assert a finding instead of asking a question? Count the
> blockers with no owner role.

**Gate** — read BLOCKERS.md before continuing. If a blocker changes what the product *is*,
go back to Stage 1 now while it's cheap.

## Stage 3 — Demo spec

**Author prompt**
> Stage 3. Read references/demo-spec.md first. Describe the experience concretely:
> surfaces, the primary flow step by step — and produce both outputs: 03-demo-spec.md
> (the system of record) and 03-demo.html (the leadership one-pager, from
> assets/templates/03-demo.html),
> and the failure states — what fails, and exactly what the user sees. Prose can hide a
> hole; a demo script can't. Include a "what this deliberately does not show" section so
> the demo doesn't promise what the requirements won't fund.

**Critic prompt**
> Review 03-demo-spec.md on dimensions 5, 7, 8. Is every failure state traceable to a PR
> claim or FAQ answer? Could someone narrate this demo end to end without improvising?

**Gate** — if you can't narrate it, you don't understand the product yet.

## Stage 4 — Docs

**Author prompt**
> Stage 4. Read references/docs.md first. Draft the customer-facing documentation from
> the approved PR and external FAQ:
> what it does, before you start, how to use it, failure behaviour, limits, troubleshooting.
> Where a paragraph won't come, do not write around it — record it under "could not be
> written yet" with the blocker or question behind it. That list is the deliverable.

**Critic prompt**
> Review 04-docs.md on 3, 5, 7, 8. Is the doc an honest complexity meter — would the
> integration section's length scare off the customer it's for? Are the gaps explicit
> [UNKNOWN]s or silent omissions?

**Gate** — every "could not be written yet" entry is a product gap. Assign each one.

## Stage 5 — Telemetry

**Author prompt**
> Stage 5. Read references/telemetry.md first. Define the north star and input metrics
> before requirements exist. Each metric
> ties to a specific press release claim by paragraph number. State instrumentation points
> and whether each exists today. Baselines you don't have are [UNKNOWN], not estimates.
> Close with the list of PR claims that cannot currently be measured — each is a decision:
> instrument it, or cut the claim.

**Critic prompt**
> Review 05-telemetry.md on 2, 5, 8. Does any metric measure nothing the PR claims? Does
> any PR claim have no metric and no entry in the unmeasurable list? Is any baseline a
> plausible-looking invention?

**Gate** — for each unmeasurable claim: instrument, or cut. Deciding neither is deciding
to ship an unverifiable promise.

## Stage 6 — Requirements

**Author prompt**
> Stage 6. Write the requirements from everything above, using
> references/requirements-format.md. Every requirement carries Source: citing a PR
> paragraph or FAQ answer, Given/When/Then criteria, out-of-scope, and dependencies.
> Grouped Discovery (D) and Delivery (DP). Any requirement whose source chain touches an
> [ASSUMED] claim is flagged RESTS ON ASSUMPTION. Any requirement you want to write that
> has no source goes in the Flagged section — do not delete it and do not source-wash it.

**Critic prompt**
> Review 06-requirements.md on 1, 2, 5, 7, 8. Check every Source: line points at something
> that exists. The unsourced requirement you most expect: the one everybody asked for in
> the demo. Find it.

**Gate** — for each flagged requirement: find its real source, push it upstream into the
PR (and re-run the Stage 1 critic), or move it to candidates. Never silently accept.

## Stage 7 — Release decomposition

**Author prompt**
> Stage 7. Cut the requirements into vertical slices — each independently shippable and
> independently testable, narrowed by customer scenario, not by layer. Per slice: the
> requirements it carries, what ships, the test harness, what blocks it. Emit the DAG and
> the edge list. A slice depending on an OPEN blocker is marked not schedulable, with the
> owner who can unblock it. Then run scripts/export_jira.py.

**Critic prompt**
> Review 07-release-plan.md on 5 and 8. Reconcile: every requirement in exactly one slice,
> orphans declared with reasons, DAG acyclic. Is any "slice" actually a layer?

**Gate** — the schedulable slices are what you can commit to. Committing a date to a
blocked slice is committing to a shape nobody has agreed.

## Stage 8 — Readiness

**Author prompt**
> Stage 8. Read references/readiness.md first. Write the go/no-go: the CONFIDENCE block
> first, open blockers by severity,
> assumptions that must hold and what breaks if they don't, requirements resting on
> assumptions, top three reasons this fails (most likely first, not most dramatic), and
> the smallest set of answers that would change the recommendation. If the honest
> recommendation is "not yet decidable," write that.

**Critic prompt**
> Review 08-readiness.md on 2, 5, 8. Does the recommendation follow from the artifact, or
> from optimism? A GO sitting on unanswered high-severity blockers fails this review.

**Gate** — yours. The skill has given you the agenda, not the decision.

---

## Overrides, at any stage

> I'm overriding the critic on dimension <n>. My justification: <why the rule doesn't
> apply here>. Record it in DECISIONS.md and proceed. Do not re-litigate.

The record is the mechanism. An override with a written justification is defensible in six
months; a quiet click-through is not.

## Resuming

> Resume the working-backwards session in wb/<session-id>/. Read session.json, tell me the
> current stage, the open blockers, and what the critic said last. Then continue.
