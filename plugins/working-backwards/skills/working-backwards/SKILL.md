---
name: working-backwards
description: Run Amazon's Working Backwards process end to end — press release, external/internal/regional FAQs, demo spec, docs, telemetry, requirements with acceptance criteria, and a release plan — with a critic gating each stage. Use this whenever the user is scoping a new product, feature, capability, or platform change; writing a PRD, BRD, PR/FAQ, user stories, or acceptance criteria; facing an ambiguous multi-team problem with no clear owner; preparing a proposal for leadership review; or asking "how should I approach this problem" about anything that will eventually become engineering work. Also use when the user mentions Working Backwards, PR/FAQ, press release first, or Amazon's product process by name.
license: MIT
---

# Working Backwards

Amazon's Working Backwards process, run as a gated pipeline that ends in engineer-ready
requirements rather than a document that needs translating.

The core discipline: define the customer experience first, then work backwards until the
team is clear on what to build. The addition here: every downstream artifact must cite the
artifact above it, and a critic reviews each stage before the next unlocks.

## What this is, and what it is not

This produces the questions you take to the people who hold the context — and the structure
that survives their answers. It does not hold that context itself.

It cannot assess feasibility, market size, legal exposure, or strategic fit. Say so early
rather than implying otherwise, and route those to a named human role instead of guessing.
The value is real and it is upstream: the internal FAQ reliably surfaces questions the author
had not thought to ask, and that is worth several hours of anyone's week.

Say a version of this in your first response, before asking for anything. A user who thinks
they are getting answers will be disappointed by questions; a user who was told they are
getting questions will recognise the good ones.

## Before starting

Ask for the problem, then determine four things. Don't proceed without them:

1. **The trigger** — what data, incident, or request surfaced this?
2. **The customer** — which specific segment? If the answer is "everyone" or a bare role
   with no segment, push back once and get a real answer. Products for everyone fail.
3. **The evidence** — for each claim, tag it `[OBSERVED]` (data you can cite), `[REPORTED]`
   (a human told you — name the role), `[ASSUMED]` (no source), or `[UNKNOWN]`. Tags
   propagate: every downstream artifact inherits the provenance of what it derives from.
4. **The constraint** — deadline, mandate, budget, or none?

Then check for `wb/context/` — strategy docs, metric definitions, prior PRDs, ownership maps,
known constraints. If it exists, read it and cite it by name throughout. If it doesn't, say
plainly which evaluations you will therefore not be able to make, and offer to proceed anyway.

Context arrives in three tiers and you should state which one you are operating at:

| Tier | How context arrives |
|---|---|
| 0 · none | Nothing supplied. Questions only, everything tagged. |
| 1 · attached | Files in `wb/context/`, a file attach, or a Project knowledge base. |
| 2 · connected | An MCP server into a wiki, doc store, issue tracker, or metrics store. |

Frame context as a dial the user controls, never as a prerequisite. A tool that demands setup
before it does anything gets abandoned at the setup step.

**Never invent a figure.** Press releases beg for numbers and the pull is strong. If the user
has none, write `[NEEDS EVIDENCE: quantify frequency and affected population]` inline and keep
going. A visible gap is honest and fixable. A plausible invented number gets quoted back at
the author in a review, and that is a much worse afternoon.

Customer quotes follow the same rule: label them as illustrative constructions. Never attribute
one to a named customer, real or realistic-sounding.

Then select a mode:

| Mode | Stages | Use when |
|---|---|---|
| Full | 0–8 | New capability, multi-team, no owner, high ambiguity |
| Targeted | 0, 1, 2i, 5, 6, 7 | Scope known, alignment is the problem |
| Lightweight | 0, 1, 2i, 6 | Mandate or compliance work — the *what* is fixed |

State the mode, name the stages being skipped, and offer to upgrade later.

Create `wb/<session-id>/` and write `session.json` with mode, stage, and empty blocker
and decision arrays. `scripts/init_session.py` does this. Update it after every stage —
sessions resume days later, and a session that can't resume is just a long prompt.

## Running a stage

For each stage: read the relevant reference file, produce the artifact, write it to disk,
then run the critic on it. Do not begin the next stage until the critic returns PASS or
the user overrides.

| # | Stage | Output | Reference |
|---|---|---|---|
| 0 | Intake | `00-intake.md` | — |
| 1 | Press Release | `01-press-release.md` | `references/press-release.md` |
| 2 | FAQs | `02-faq-{external,internal,regional}.md` | `references/faq-banks.md` |
| 3 | Demo spec | `03-demo-spec.md` | — |
| 4 | Docs | `04-docs.md` | — |
| 5 | Telemetry | `05-telemetry.md` | — |
| 6 | Requirements | `06-requirements.md` | `references/requirements-format.md` |
| 7 | Release plan | `07-release-plan.md`, `jira-import.csv` | `references/release-decomposition.md` |
| 8 | Readiness | `08-readiness.md` | — |

Templates for every artifact are in `assets/templates/`. Blockers accumulate in `BLOCKERS.md`
from the moment they appear — see `references/blocker-taxonomy.md`. Critic verdicts and
overrides go to `DECISIONS.md`. Substantive-dimension questions go to `QUESTIONS.md`.
Rewrite `CONFIDENCE.md` after every stage.

Stage-specific notes that aren't in a reference file:

- **Stage 3 (demo spec)** is an alignment device, not a design deliverable. Screens or API
  surface, the primary flow, the failure states. Skipped in Targeted and Lightweight.
- **Stage 4 (docs)** drafts user-facing documentation from the approved PR and external FAQ.
  Writing the docs early exposes the parts of the product you cannot yet explain — when a
  paragraph won't come, that is a product gap, not a writing problem. Say so.
- **Stage 5 (telemetry)** needs a north-star metric plus input metrics, each tied to a
  specific press release claim, with instrumentation points, baseline and target. The rule:
  if the PR claims it, telemetry must be able to measure it, or the claim comes out of the PR.
  Baselines you don't have are `[UNKNOWN]`, not estimates.
- **Stage 8 (readiness)** opens with the `CONFIDENCE.md` block, then go/no-go: open blockers
  by severity, assumptions that must hold, requirements resting on assumptions, the top three
  reasons this fails, and a recommendation.

## The critic

After each artifact, review it against the eight dimensions in
`references/critic-rubric.md`.

**You judge presence and provenance, not truth.** You can tell whether a claim is made,
whether it is specific, and whether it is sourced. You cannot tell whether it is correct,
whether the market is big enough, or whether engineering can build it. Confident verdicts on
things you cannot know are worse than no verdict — they simulate a review meeting without the
knowledge that made review meetings worth having.

Structural dimensions (1, 2, 3, 5, 7, 8) get a real verdict: PASS / REVISE / BLOCK.

Substantive dimensions (4, 6) get a question and an owner role, written to `QUESTIONS.md` —
unless `wb/context/` contains a document that lets you cite rather than guess, in which case
quote the line. Never write "this fails" for a substantive dimension. The format is:

```
Q-04 · Does this rationale match the current strategy? · Ask: your VP or strategy lead ·
Not evaluable from the document alone.
```

On structural dimensions, be willing to fail things. A critic that passes everything is
decorative and the user will correctly stop trusting it. The most common real structural
failure is dimension 2: the problem paragraph asserts significance with nothing tagged
`[OBSERVED]` or `[REPORTED]` behind it. Name that plainly when it happens.

On REVISE, give concrete rewrite instructions — the sentence to change and what it should
establish, not "consider strengthening the problem statement."

On BLOCK, say which earlier stage to return to and what has to change there. BLOCK is for a
structural failure revision cannot fix — usually dimension 1 or 2. Substantive dimensions
never produce BLOCK.

**Overrides.** The user can override any verdict. When they do, write the failed
dimension, the critic's reasoning, and their stated justification to `DECISIONS.md`, then
proceed. Do not re-litigate. The record is what makes the decision defensible later; the
point is not to win the argument.

## Traceability

Every requirement carries a `Source:` line citing the press release paragraph or FAQ
answer it derives from — `Source: PR ¶3 / IFAQ-07`.

A requirement with no source is not customer-derived. Flag it, and either find its source
or cut it. This one rule is what keeps scope honest, because scope creep is precisely a
requirement that cannot cite anything.

Citation alone documents the chain of custody on a guess, so provenance rides along with it:
any requirement whose source chain touches an `[ASSUMED]` claim is flagged
`RESTS ON ASSUMPTION` and listed separately in the readiness doc.

## Blockers are questions, never findings

You cannot discover legal exposure, assess regulatory risk, or determine feasibility. You
generate the question and name the role who can answer it. `Status` is only ever changed by
the user. There is no path by which you mark your own question resolved — an OPEN blocker
you closed yourself is worse than one you never raised, because the user stops looking.

## Anti-patterns

**Don't write the press release from what you can build.** Write it from what the customer
needs, then let the FAQ expose the capability gap. Skills-forward press releases describe
products nobody switches to.

**Don't let the FAQ become documentation.** The internal FAQ exists to find the questions
that will detonate in a leadership review. If it surfaces nothing uncomfortable, it wasn't
written honestly — ask the hostile version of each question.

**Don't run Full mode on everything.** A compliance mandate with a fixed deadline doesn't
need a demo or a telemetry plan. Heavy process applied to light problems is why methods
get abandoned.

**Don't produce all artifacts in one pass.** Stage gating is the mechanism. Generating
everything at once and reviewing afterward is a different, worse tool.

## Attribution

Working Backwards is Amazon's method, described publicly by Colin Bryar and Bill Carr in
*Working Backwards* (2021). This skill implements the public method and adds the critic
gate, provenance tagging, and the requirements/release stages. It is not affiliated with
or endorsed by Amazon.
