# Working Backwards

## A Claude Skill that runs Amazon's Working Backwards process end to end and terminates in engineer-ready requirements — not a press release you still have to translate.

**5 August 2026** — Working Backwards is available today as an installable Claude Skill. It runs
Amazon's PR/FAQ discovery process as a nine-stage gated pipeline: press release, external and
internal and regional FAQs, demo spec, docs, telemetry, requirements with acceptance criteria,
vertical release slices with a dependency graph, and a readiness recommendation. A critic reviews
every stage before the next unlocks. Every requirement cites the press release paragraph or FAQ
answer it derives from. The last artifact is a JIRA-importable CSV.

It is MIT licensed, works with or without any knowledge of your company, and tells you plainly
what it could not evaluate.

**[See it running →](https://siddarthnyati.github.io/working-backwards)**

---

## The problem

Amazon's Working Backwards is the best-known product discovery method in the industry, and it is
genuinely excellent at one job: deciding *whether* something is worth building. It stops there. By
design — Colin Bryar and Bill Carr are explicit that the PR/FAQ ends in a go/no-go and Agile picks
up afterward.

That handoff is where the method dies in most companies. A PM writes a beautiful PR/FAQ, leadership
nods, and then the PM opens a blank epic and starts from zero — because nothing in a PR/FAQ is
shaped like a user story, an acceptance criterion, or a release plan. The narrative gets admired and
shelved. Two weeks later the epic reads exactly like every other epic and none of the customer
thinking survived the trip.

Most orgs are not Amazon. They run an issue tracker, a wiki, sprint ceremonies, and a template
somebody wrote years ago. They need the discovery rigor *and* the downstream artifacts, and the gap
between them is where PM time actually goes.

There's a second problem, and it's the one that decides whether a tool like this is useful or just
fast at producing slop. Working Backwards works at Amazon because the PR/FAQ is a **meeting**
mechanism — fifteen minutes of silent reading, forty minutes of cross-functional interrogation,
repeated over months. A solo user plus a model replaces the document and not the room. Run naively,
you get a beautifully structured artifact chain resting on invented numbers, and the traceability
rule traces cleanly back to a fabrication.

## The solution

Three things, and they are the whole pitch.

**It doesn't stop at the PR/FAQ.** The pipeline ends in vertical release slices — each
independently shippable and independently testable — with a dependency DAG and a CSV your tracker
can import. You end with something engineering can pick up.

**Every requirement traces to a paragraph.** Each one cites its source: `Source: PR ¶3 / IFAQ-07`.
A requirement that can't cite anything isn't customer-derived, and it gets flagged rather than
silently accepted. This is the single mechanism that stops scope creep, because scope creep is
precisely "a requirement with no source."

**A critic gates every stage — and knows what it can't judge.** Six dimensions are structural
(customer specificity, evidence presence, alternative named, traceability, clarity, template
completeness) and get a real verdict: PASS, REVISE, BLOCK. Two are substantive (strategic fit,
falsifiability) and *never* get a verdict — only a question and the role who can answer it. A critic
that returns confident judgments on things it cannot know is worse than no critic, because it
simulates a review meeting without the knowledge that made review meetings valuable.

You can override any verdict. The override goes to `DECISIONS.md` with the critic's reasoning and
your justification, and then the skill proceeds without arguing. That log is what makes the decision
defensible six months later.

Alongside those: provenance tags (`[OBSERVED]`, `[REPORTED]`, `[ASSUMED]`, `[UNKNOWN]`) that
propagate down the chain, a hard rule against inventing figures, blockers that are always questions
with an owner and never findings, and a `CONFIDENCE.md` that tells you what the session doesn't know.

> "I ran it on a platform defect I'd already written a ticket for. The internal FAQ asked who owned
> the integration contract, and the honest answer was that nobody did — which was the actual reason
> the work had stalled twice. It took eleven minutes to find and I'd been looking at it for a month."
>
> — a product manager
> `[illustrative construction — the skill's own rule about labelling invented quotes applies to its README]`

> "The critic rejected my first press release for describing a defect instead of explaining why
> leadership should care. That was correct and uncomfortable, and the sentence I wrote to fix it
> ended up in every stakeholder brief for the initiative. A critic nobody fears is decorative."
>
> — Siddarth Nyati, author

## Getting started

```bash
/plugin marketplace add siddarthnyati/working-backwards
/plugin install working-backwards
```

Or drop the skill in directly, with no plugin machinery:

```bash
cp -r plugins/working-backwards/skills/working-backwards ~/.claude/skills/
```

Then just describe a problem. The skill asks for the trigger, the customer segment, the evidence,
and the constraint; picks a run mode; tells you which context tier it's operating at and what it
therefore can't evaluate; and starts.

---

# FAQ

## External

**What does this actually produce?**
Thirteen-plus artifacts in `wb/<session-id>/`: intake, press release, three FAQ banks, demo spec,
docs, telemetry plan, requirements, release plan, readiness — plus `BLOCKERS.md`, `DECISIONS.md`,
`QUESTIONS.md`, `CONFIDENCE.md`, `jira-import.csv` and `session.json`. See
[`examples/ghost-seats/`](examples/ghost-seats/) for a complete real run, and
[`examples/silent-stepdown/RUNBOOK.md`](examples/silent-stepdown/RUNBOOK.md) for a second run
with the exact prompt used at every stage.

**Do I have to run all nine stages?**
No, and you shouldn't. Three modes. **Full** (0–8) for a new capability with no clear owner.
**Targeted** (0, 1, 2-internal, 5, 6, 7) when scope is known and alignment is the problem.
**Lightweight** (0, 1, 2-internal, 6) for compliance or mandate work where the *what* is fixed and
you need clean requirements — under an hour. The skill states which stages it's skipping and why,
and you can upgrade mid-run.

**Does it work outside Claude Code?**
Yes. Download `dist/working-backwards.skill` and upload it on Claude.ai. The scripts
(`init_session.py`, `export_jira.py`) need a filesystem, but every stage works without them.

**What does it cost me?**
It's MIT licensed and free. The real cost is time: Full mode is 4–8 hours across sessions, and it
should be — that's a discovery process, not a generator.

**Does it need access to my company's documents?**
No. It works at tier 0 with nothing, and gets materially sharper with each thing you give it. Drop
files in `wb/context/`, attach them to the conversation, or point an MCP server at your wiki. When a
document is present the critic cites it by name; when it's absent the skill says so explicitly and
downgrades the relevant dimensions to questions. Nothing silently degrades.

**How much does context actually change things?**
Less than you'd hope, and in a useful direction. In the worked example, one two-page strategy
document closed four questions, opened one, sharpened two — and closed **zero blockers**. Six
blockers before, six after. No document converts a legal, privacy, or regulatory determination into
a document lookup. What context buys is a better-specified argument, not a verdict.

**Where is this *not* useful?**
Single-team, well-understood, already-aligned work. That's a ticket, not a discovery session. Nine
stages on a two-day change is how people conclude the method is overkill and never come back.

## Internal

**Why not just prompt for a PRD?**
You can, and for a small well-understood change you should. What a prompt doesn't give you: stage
gating (you can't skip ahead past a failed review), resumable session state, a citation rule enforced
across artifacts written days apart, provenance that propagates from an intake claim into a flagged
requirement, and an override log. The difference between a prompt and a skill is that a session that
can't resume is just a long prompt.

**What happens when the critic is wrong?**
Override it. The skill writes the failed dimension, the critic's reasoning and your justification to
`DECISIONS.md`, then proceeds and does not re-litigate. This happens in the worked example: the
critic flags Stage 5 for empty baselines, and it's right by its own rule — but the baseline was
genuinely unknowable before instrumentation existed, and filling it in would have meant inventing a
figure. Both positions are on the record.

**Isn't an AI critic just going to pass everything?**
That's the failure mode the rubric is written against, and it's why the rubric ships with a pass
example, a fail example, and a concrete rewrite instruction for each dimension, plus a calibration
section naming the two ways critics degrade — softening ("could benefit from additional supporting
data" is a PASS in a REVISE costume) and drifting substantive. In the worked example the critic
returns REVISE three times and fires on the one requirement everybody wanted.

Honest limitation: **the critic is a prompt, not a model.** It's consistent, not calibrated. There's
no held-out set of human-labelled press releases behind it. The next version needs one so the rubric
can be measured rather than asserted.

**Does this replace discovery, or the review meeting?**
Neither, and claiming otherwise would be the thing this repo argues against. It produces the
questions you take to the people who hold the context, plus the structure that survives their
answers. It cannot assess feasibility, market size, legal exposure, or strategic fit, and it says so
in its own first response.

The honest framing is that this is **one seat in the room** — the outsider who hasn't inherited your
blind spots. Institutional context isn't purely an asset; it's also how a team stops asking whether
the thing is worth building at all. The reason a senior hire is valuable in month one is precisely
that they don't know yet.

**What works with zero context, specifically?**
Five things. **The question set** — Amazon's FAQ bank is public and generalizes, because it derives
from the shape of shipping something rather than from any one company. **Extraction** — the PM
already holds the context; it's tacit and unwritten, and failing "customer specificity" requires no
knowledge of your customers, only noticing you wrote a role where a segment belongs. **Sorting known
from assumed** — nobody does this unprompted, and two weeks later you can't tell which of your own
beliefs came from data. **Anti-anchoring** — left alone, a PM writes the requirements they'd already
decided on and back-fills a justification; customer → problem → hostile questions → *then*
requirements makes that structurally harder. **Mechanical conversion** — Given/When/Then, vertical
slices, DAG, CSV.

**Why does the worked example look so unfinished?**
Because it was run deliberately without a context pack, and that's the honest degraded case: tags
throughout, a visible `[NEEDS EVIDENCE]` placeholder, two assumptions propagating into flagged
requirements, twenty open questions and two with nobody to ask. A press release studded with tags
looks weaker than a confident one. That's the trade, taken on purpose. The audience for this repo is
product people who have been burned by confident generated documents.

**Where did this come from?**
I ran three Working Backwards sessions on real platform problems using an AI pipeline my employer
had built internally. I didn't build that pipeline. What I did was run it hard enough to learn where
the method creates value and where it wastes your afternoon — and then build my own open version,
because the method is Amazon's and public, and the pipeline pattern is reproducible by anyone.

What those sessions taught me is in the design: the FAQ stage is a risk-discovery engine rather than
a documentation chore; the critic is the product and it has to be willing to fail things; and not
every problem needs all nine stages, or people will run the full thing once, find it heavy, and
never run it again.

---

## What's in here

```
plugins/working-backwards/skills/working-backwards/
  SKILL.md                    the pipeline, the gating, the traceability rule
  references/                 press release · FAQ banks · critic rubric ·
                              requirements format · release decomposition ·
                              blocker taxonomy
  assets/templates/           every artifact type
  scripts/                    init_session.py · export_jira.py ·
                              verify_sources.py  (stdlib only)
examples/ghost-seats/                complete Full-mode run, no context pack
examples/ghost-seats-with-context/   Stages 1–2 again, with one strategy doc
examples/silent-stepdown/            second full run (payments-shaped) — RUNBOOK.md
                                     records the exact prompt used at every stage
docs/index.html                      the interactive site
```

## Attribution

Working Backwards is Amazon's method, described publicly by **Colin Bryar and Bill Carr** in
*Working Backwards: Insights, Stories, and Secrets from Inside Amazon* (2021). This repository is an
independent open implementation of the public method, adding the critic gate, provenance tagging,
and the requirements and release-decomposition stages. It is not affiliated with or endorsed by
Amazon.

Ghost Seats is fictional and bears no relation to any real company, product, or dataset.

MIT licensed. See [LICENSE](LICENSE).
