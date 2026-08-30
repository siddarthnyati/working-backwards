# Runbook — how this session was actually driven

Ghost Seats shows the pipeline's depth. This file shows its **operation**: the exact prompt
used at each stage, what the stage's author-agent did, and what the critic said. The
generic, reusable versions of these prompts live in the skill at
`references/stage-prompts.md`.

Three roles repeat at every stage:

| Role | Who | Does |
|---|---|---|
| **Author** | the skill | produces the stage artifact, carries provenance, writes to disk |
| **Critic** | the skill, re-invoked against `references/critic-rubric.md` | PASS / REVISE / BLOCK on structural dimensions; questions with owners on substantive ones |
| **Gate** | the human | accepts, sends back, or overrides — the skill never takes this decision |

To reproduce the setup:

```
python plugins/working-backwards/skills/working-backwards/scripts/init_session.py \
  silent-stepdown --mode full
```

---

## Stage 0 — Intake

**Prompt**
> Run the working-backwards skill, Stage 0 only. The problem: our gateway's auth event log
> shows that when a 3-D Secure call times out after 3 seconds, the transaction is retried
> without authentication and nothing records that this happened — about 31,400 times a
> quarter on the European corridor. Merchants can't see it; fraud liability on those
> transactions sits with them. Tag every claim. Push back if my customer is too broad.
> Recommend a mode. Do not write the press release.

**What the author did** — separated eight claims into 4 `[OBSERVED]` / 1 `[REPORTED]` /
2 `[ASSUMED]` / 2 `[UNKNOWN]`; rejected "merchants" as the customer and forced the
three-field segment (3DS enabled + EEA volume + recent fraud chargeback); recommended Full
mode off six-roles-no-owner.

**Critic** — PASS. Noted the two assumptions that will propagate: C5 (fraud differential)
and C6 (whose latency causes the timeouts).

**Gate** — accepted. → [`00-intake.md`](00-intake.md)

---

## Stage 1 — Press release

**Prompt**
> Stage 1. Write the press release from the intake. Customer's voice, provenance tags
> inline, no invented figures — where there's no number, [NEEDS EVIDENCE]. Number the
> paragraphs. Do not write the FAQs.

**What the author did** — wrote the launch as if shipped: visibility + policy control.
Kept the one wanted-but-absent number as a visible gap (`[NEEDS EVIDENCE: chargeback rate
on stepped-down vs authenticated]`).

**Critic — REVISE, dimension 3.** Draft ¶4 said *"Merchants currently have no way to
detect this happening"* — the rubric's literal fail case. There is always a current
behaviour: chargeback reconciliation, months later, one lost dispute at a time. The
instruction named the sentence and what it had to establish.

**Gate** — revised ¶4, re-reviewed → PASS. Substantive output: Q-16 (which frame funds
this — trust or defence?), Q-01/Q-02/Q-03 (must-be-trues).
→ [`01-press-release-draft1.md`](01-press-release-draft1.md) · [`01-press-release.md`](01-press-release.md)

---

## Stage 2 — FAQs (external · internal · regional)

**Prompt**
> Stage 2. Three banks, hostile versions, in the voice of the leader who would ask. Tag
> every answer. Every BLOCKER gets an owner role and stays OPEN — you resolve nothing.

**What the author did** — 21 questions across the banks. Six blockers surfaced, all
question-shaped: legal restitution, SCA position, induced-timeout bypass, provider SLA,
retention join, conversion-trade ownership. Zero ANSWERED tags — tier 0 means the
agreements and contracts that would answer them aren't in the session.

**Critic** — PASS. Called out IFAQ-09 as the honest one: it names the initiative's internal
tension — the silent fallback exists because it protects a metric the platform reports.

**Gate** — accepted; read BLOCKERS.md before continuing. This is where the session earned
its keep: **six blockers before a single requirement existed.**
→ [`02-faq-internal.md`](02-faq-internal.md) et al., [`BLOCKERS.md`](BLOCKERS.md)

---

## Stage 3 — Demo

**Prompt**
> Stage 3. Narrate the experience end to end — surfaces, primary flow, failure states,
> and what the demo deliberately does not show. If you can't narrate it, say where you
> can't and why.

**What the author did** — six-step flow; five failure states. F4 is the load-bearing one:
if the policy service itself fails, the outcome records `policy-unavailable` — the spec
refusing to contain a copy of the defect it fixes. F2 makes a provider outage read as one
incident, not 400 alarms.

**Critic** — PASS. → [`03-demo-spec.md`](03-demo-spec.md)

---

## Stage 4 — Docs

**Prompt**
> Stage 4. Customer-facing docs from the PR and external FAQ. Where a paragraph won't
> come, record it under "could not be written yet" with the blocker behind it.

**What the author did** — full doc, plus two unwritable sections: the require-exemption
policy (BLK-02 — a doc that can't be written is a feature that can't ship) and the
historical view (BLK-05).

**Critic** — PASS. → [`04-docs.md`](04-docs.md)

---

## Stage 5 — Telemetry

**Prompt**
> Stage 5. North star and input metrics, each tied to a PR paragraph. Baselines you don't
> have are [UNKNOWN]. Close with the claims you cannot measure — each is instrument-or-cut.

**What the author did** — north star: **Silent Step-Down Count → 0** (deliberate-by-
construction, verified not hoped). Six input metrics; M1/M2 baselines `[OBSERVED]` from the
existing auth log; M6 (the fraud differential) honestly gated on BLK-05.

**Critic** — PASS, no override needed. The deliberate contrast with Ghost Seats: **the
pipeline's output tracks the state of the org's evidence, not the author's confidence.**
Same skill, same rubric — different org reality, different verdict.
→ [`05-telemetry.md`](05-telemetry.md)

---

## Stage 6 — Requirements

**Prompt**
> Stage 6. Requirements with Source: lines, Given/When/Then, D/DP grouping. Anything whose
> source chain touches [ASSUMED] gets flagged. Anything with no source goes to Flagged —
> don't delete it, don't source-wash it.

**What the author did** — 9 requirements. REQ-D4 flagged `RESTS ON ASSUMPTION` (C5).
REQ-D3 and REQ-DP4 marked `SHAPE PENDING` with the fork each blocker forces. The
restitution mechanism — proposed during drafting — went to candidates instead of the
numbered set: it cites a wish, not a decision.

**Critic** — PASS. All 20 citations resolve. → [`06-requirements.md`](06-requirements.md)

---

## Stage 7 — Release decomposition

**Prompt**
> Stage 7. Vertical slices, narrowed by scenario. Reconcile: every requirement in exactly
> one slice, orphans declared, DAG acyclic. Mark blocked slices not-schedulable with the
> owner who unblocks them. Then run export_jira.py.

**What the author did** — first cut placed REQ-DP4 in both R2 and R3, so R2 could claim
"EEA-complete."

**Critic — REVISE, dimension 5.** A requirement in two slices means one of them isn't
independently shippable. Moved wholly into R3; R2 ships visibility only. Re-reviewed →
PASS. Reconciliation: 9/9 exactly once, DAG acyclic, 4 epics + 9 stories exported.

**Gate** — accepted. This is the check that exists because "one requirement, two epics" is
how double-counted scope enters a tracker unnoticed.
→ [`07-release-plan.md`](07-release-plan.md) · [`jira-import.csv`](jira-import.csv)

---

## Stage 8 — Readiness

**Prompt**
> Stage 8. Confidence block first, blockers by severity, assumptions that must hold, top
> three reasons this fails (most likely first), and the smallest set of answers that would
> change the recommendation. If it's not decidable, say so.

**What the author did** — **GO WITH CONDITIONS on R1+R2 only**, with one escalation the
stage numbering doesn't capture: BLK-03 (induced-timeout bypass) is a *today* question
regardless of the go/no-go — if the fallback is farmable, it's a live fraud channel now.

**Critic** — PASS. A GO covering R3 would have failed: two open blockers shape what R3 is.
→ [`08-readiness.md`](08-readiness.md)

---

## The tally

| | |
|---|---|
| Stages run | 9 of 9 (Full mode) |
| Critic verdicts | 7 PASS · 2 REVISE (both resolved by revision) · 0 overrides |
| Blockers | 6 OPEN — 5 high, 1 medium — all question-shaped, all owned |
| Requirements | 9 · 0 unsourced · 1 resting on assumption · 2 shape pending |
| Schedulable today | R1, R2 |
| The unowned question | Q-02 — will anyone read the digest — sitting under the central promise |

Two runs, one skill: ghost-seats shows a substantive question changing a document the
structural rubric had passed, and an override done honestly. This run shows the structural
rubric failing a draft outright, and the reconciliation check catching double-counted
scope. Neither run resolves its own blockers. That is the design.
