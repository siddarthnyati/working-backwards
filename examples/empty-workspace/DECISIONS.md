# Decisions — Empty Workspace

Verdicts in order. One REVISE, resolved by revision; no overrides in this run.

---

```
CRITIC · Stage 0 · 00-intake.md · 2026-08-30
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... PASS
  8 Template completeness ...... PASS
VERDICT: PASS
Note: "team leads at 5–50-person companies who create a workspace self-serve, intending to
bring their team" — with three queryable signup fields — is a segment. "Users who don't
invite" would have been a behaviour, not a customer, and would have blocked. C5 (causation)
and C6 (deliverability) flagged as the assumptions that will propagate.
```

---

```
CRITIC · Stage 1 · 01-press-release-draft1.md · 2026-08-30
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... REVISE
  3 Alternative named .......... PASS
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive
  4 Strategic fit .............. Q-09 raised
  6 Falsifiability ............. Q-01, Q-02 raised

VERDICT: REVISE
Instruction: ¶2 writes "Teams that don't invite churn because they never experience
collaboration" — a causal claim wearing no tag, sitting beside two correlational
observations that don't establish it. This is the most common real structural failure and
it is load-bearing here: the entire initiative rests on that "because." Tag the correlation
[OBSERVED], the causation [ASSUMED] with a pointer to the experiment that would settle it,
and add the [NEEDS EVIDENCE] marker for un-instrumented invite attempts. Do not soften the
paragraph — sharpen its honesty.
```

```
CRITIC · Stage 1 · 01-press-release.md (revised) · 2026-08-30
  2 Evidence presence .......... PASS — the causal claim now carries [ASSUMED — C5] and
    cites REQ-D3 as the experiment that would settle it; the attempts gap is visible.
All other dimensions unchanged.
VERDICT: PASS
Note: ¶7's spokesperson quote gained "this ships with its own experiment, not just its own
dashboard" in revision — the author folding the critic's finding into the narrative rather
than just the tags. That sentence is now the initiative's best defence in review.
```

---

```
CRITIC · Stage 2 · 02-faq-{external,internal,regional}.md · 2026-08-30
Structural: 2 PASS · 5 PASS · 7 PASS · 8 PASS
Substantive: 6 → Q-03…Q-08 raised
VERDICT: PASS
Note: IFAQ-02 is the honest one — it asks what the quarter was spent on if activation moves
and retention doesn't. EFAQ-02 (the dark-pattern question) produced a requirement (REQ-DP5)
rather than a reassurance, which is the correct disposition for a promise.
```

---

```
CRITIC · Stage 3 · 03-demo-spec.md · 2026-08-30
Structural: 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS
Note: the disabled "Import from contacts" button is the spec's best decision — the roadmap
made visible without shipping the risk, and honest about why ("pending privacy review").
F5 guards the meta-failure: a silent send-failure would recreate the original invisibility
inside the fix.
```

---

```
CRITIC · Stage 4 · 04-docs.md · 2026-08-30
Structural: 3 PASS · 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS
Note: contact import documented as not-writable, citing BLK-01. One section, one blocker,
zero hedged paragraphs pretending otherwise.
```

---

```
CRITIC · Stage 5 · 05-telemetry.md · 2026-08-30
Structural: 2 PASS · 5 PASS · 8 PASS
VERDICT: PASS
Note: the north star counts members-with-action, not members — the metric refuses its own
gaming vector. M3 (skip rate) instruments the never-nag promise's health. M6 is the
experiment the press release now cites; no override needed anywhere because nothing
unmeasured was stated as measured.
```

---

```
CRITIC · Stage 6 · 06-requirements.md · 2026-08-30
Structural: 1 PASS · 2 PASS · 5 PASS · 7 PASS · 8 PASS
Substantive: 6 → Q-11 carried onto REQ-D3
VERDICT: PASS
Note: invite incentives arrived wanting to be a requirement and left as a candidate citing
EFAQ-05/BLK-05 — with the stated logic that paying for an unproven-causal behaviour is
paying for a metric. All 16 citations resolve.
```

---

```
CRITIC · Stage 7 · 07-release-plan.md · 2026-08-30
Structural: 5 PASS · 8 PASS
VERDICT: PASS
Note: reconciliation clean — 8/8 requirements in exactly one slice, DAG acyclic. R1 as the
only meeting-free slice is the plan's honest headline. BLK-03 blocking the two easiest
slices is correctly surfaced as an ownership problem, not an engineering one.
```

---

```
CRITIC · Stage 8 · 08-readiness.md · 2026-08-30
Structural: 2 PASS · 5 PASS · 8 PASS
VERDICT: PASS
Note: GO on R1 alone, conditions on the rest, is supported. A recommendation that included
R4 would have failed — it sits on four open blockers, three of them legal-shaped.
```
