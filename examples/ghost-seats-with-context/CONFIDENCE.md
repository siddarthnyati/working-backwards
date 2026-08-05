# Confidence — Ghost Seats (with context)

State after Stage 2. Stages 3–8 were not run.

```
SESSION CONFIDENCE · ghost-seats-ctx · after Stage 2 · 2026-08-05
Claims:        4 observed · 1 reported · 2 assumed · 2 unknown   (intake ledger C1–C9)
Questions:     13 open · 2 with no owner assigned
Blockers:      6 open (6 high · 0 medium · 0 low)
Context pack:  1 document — strategic fit evaluable; feasibility, legal, privacy and
               regulatory still not evaluated
```

Side by side with the tier-0 run at the same point:

```
                        tier 0        tier 1
Questions open            17            13
Questions unowned          2             2
Blockers open              6             6
Dimension 4          not evaluable   cited, not adjudicated
Dimension 6          not evaluable   not evaluable
```

## Still not evaluated, and why

| Dimension | Why | What would fix it |
|---|---|---|
| 6 · Falsifiability | No latency data, no post-mortems, no ownership map. Unchanged from tier 0. | Answers from the named roles; an ownership map for Q-19 and Q-20 |
| Legal / privacy / regulatory | A strategy document says nothing about DPAs, erasure obligations, or SOC 2 controls | DPAs, the control narrative — and counsel, who a document never replaces |
| Feasibility | Nothing here reaches whether the platform can detect propagation failure | Platform engineering lead |
| Stage 5 baselines | Not run. No metric definitions supplied, and the strategy document itself says pillar 2 is unmeasured | A telemetry export |

## What the one document bought

| Effect | Detail |
|---|---|
| Dimension 4 moved from a question to a citation | Cites pillar 2 by name, quotes the commitment line and the conflicting budget line |
| A conflict became visible | R3 needs the integration-agreement change the plan defers to 2027. Invisible at tier 0 |
| Four questions closed | Q-04 (→ Q-04b), Q-07, IFAQ-03, IFAQ-16 |
| One blocker got evidence | BLK-05's ownership gap is now cited to a document that says it has cost the company twice |
| Zero blockers closed | Six before, six after |

## What would move the rest

In descending order of what each would buy for *this* session:

| Drop in… | Would close |
|---|---|
| **Ownership map / team boundaries** | Owners for Q-19 and Q-20. Possibly an owner for BLK-05, which is the highest-value single unlock in the session |
| Standard DPA + negotiated variants | BLK-03 gets a clause number. Still routes to counsel |
| SOC 2 control narrative | BLK-04 cites a control ID. Still routes to compliance |
| Telemetry export or support tickets | Tests claim C7 directly, so REQ-DP5 stops resting on an assumption |
| Metric definitions and baselines | Q-06 and Q-15; grounds the Stage 5 targets |
| Prior PRDs or post-mortems | Q-16 — integration retention behaviour |

## The honest read

One document at Stages 1–2: four questions closed, one opened, one sharpened, zero blockers
resolved.

That ratio is the thing to take away, and it points both ways. Context is worth supplying —
four fewer meetings, and one conflict caught before a review rather than in one. And context
is not a substitute for the six people who have to answer the six blockers, none of whom
were replaced by a document and none of whom ever will be.

A tool that told you otherwise would be the thing this repo is arguing against.
