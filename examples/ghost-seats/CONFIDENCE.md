# Confidence — Ghost Seats

Rewritten after every stage. This is the final state, after Stage 8.

Read it as a to-do list, because that is what it is.

```
SESSION CONFIDENCE · ghost-seats · after Stage 8 · 2026-08-05
Claims:        4 observed · 1 reported · 2 assumed · 2 unknown   (intake ledger C1–C9)
Derived:       9 further [UNKNOWN] values downstream — every Stage 5 baseline and target,
               and three limits in the documentation
Requirements:  12 total · 2 resting on assumptions · 2 shape pending · 1 unsourced and flagged
Release:       4 slices · 2 schedulable · 2 not schedulable
Questions:     20 open · 2 with no owner assigned
Blockers:      6 open (6 high · 0 medium · 0 low)
Context pack:  absent — strategic fit and feasibility were not evaluated
```

The last line is the one that governs the rest. This session ran deliberately at tier 0.

## Not evaluated, and why

| Dimension | Why | What would make it evaluable |
|---|---|---|
| 4 · Strategic fit | No strategy or vision document supplied. On draft 1 the critic could see that a rationale was *absent* — absence is a presence check. It could not say whether the rationale added in the revision is the right one. | A strategy or vision doc in `wb/context/` |
| 6 · Falsifiability | No prior PRDs, no post-mortems, no latency data, no ownership map. The three must-be-true claims under the press release were emitted as questions; two of them have no owner. | Answers from the named roles — and an ownership map so the unowned two get one |
| Stage 5 baselines | No metric definitions and no telemetry export. Nothing has ever measured propagation, so every baseline is `[UNKNOWN]` rather than estimated. See the override in `DECISIONS.md`. | A telemetry export, or R1 shipping |
| Blocker owner roles | No ownership map, so owners resolve to generic titles. BLK-05's owner is literally "platform lead and partnerships lead, jointly," which is a restatement of the blocker rather than an assignment. | An ownership map / team boundaries doc |

## What each missing document would have unlocked

| Drop in… | And this becomes possible | In this session, specifically |
|---|---|---|
| Strategy or vision doc | Dimension 4 cites a line instead of asking a question | Q-04 closes. The draft-1 finding still fires — the rationale was absent either way — but the revision could have been checked instead of merely stated. |
| Metric definitions + baselines | Stage 5 targets are grounded; the north star is validated, not invented | Q-06 and Q-15 close. The Stage 5 override becomes unnecessary. |
| Prior PRDs or post-mortems | "What exists today" gets answered; you stop re-proposing something already rejected | Q-16 likely closes — integration retention behaviour is the kind of thing a prior post-mortem records. |
| Ownership map / team boundaries | Blocker owner roles resolve to actual teams instead of generic titles | BLK-05 gets an owner instead of a joint restatement. Q-19 and Q-20 get owners. This is the highest-value single document for this session. |
| Contracts, DPAs, regulatory constraints | The regional FAQ cites real obligations, not generic regimes | BLK-02, BLK-03 and BLK-04 still route to counsel — that never changes — but they would cite the clause and the control number instead of describing the shape of the question. Counsel gets a five-minute question rather than a research task. |
| Telemetry export or support tickets | The problem paragraph carries `[OBSERVED]` instead of `[ASSUMED]` | C7 ("most customers never discovered this") is testable directly against ticket volume. Q-08 closes and REQ-DP5 stops resting on an assumption. |

## The honest read

Two of twelve requirements rest on assumptions. Two more have no settled shape. Two of four
release slices cannot be scheduled. Twenty questions are open and two of them have nobody to
ask.

That is not a weak session — it is an accurate one for a problem found in data, spanning six
roles, with no owner and no context pack. A version of this document showing three open
questions and a confident go/no-go would have been a better screenshot and a worse artifact.

The single most useful next action out of this session is not to answer a question. It is to
assign Q-19 and Q-20 to somebody, and to get one person named as the owner of BLK-05.

See `examples/ghost-seats-with-context/` for Stages 1 and 2 of the same problem run with a
strategy document present.
