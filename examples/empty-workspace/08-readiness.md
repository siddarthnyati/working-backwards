# Readiness — Empty Workspace

```
SESSION CONFIDENCE · empty-workspace · after Stage 8 · 2026-08-30
Claims:        5 observed · 1 reported · 2 assumed · 2 unknown   (intake C1–C8)
Requirements:  8 total · 1 resting on assumption · 2 shape pending · 0 unsourced
Release:       4 slices · 1 schedulable today · 3 blocked
Questions:     11 open · 0 with no owner assigned
Blockers:      6 open (4 high · 2 medium)
Context pack:  absent — strategic fit and feasibility were not evaluated
```

## Recommendation

**GO — on R1 today. Everything else has a named conversation in front of it.**

R1 (instrument the funnel) needs no meeting, no lawyer, and no owner ruling — and it
produces the number every other decision needs: how many people already try to invite and
abandon. It also arms the experiment that tests the assumption the initiative rests on.

R2 and R3 are one decision away — BLK-03 is an ownership dispute, not a hard problem.
R4 carries the entire privacy/regulatory/security surface and should not be estimated
until counsel answers.

## Open blockers by severity

### High
| ID | Ask | Owner role | Blocks |
|---|---|---|---|
| BLK-01 | Lawful basis + non-user contact retention | privacy counsel | R4 |
| BLK-02 | Invite email classification per market | compliance lead | R4 |
| BLK-03 | Who owns the onboarding surface | VP Product | R2, R3 |
| BLK-04 | Experiment power at current volume | data & analytics lead | R4 |

### Medium
| BLK-05 | Invite incentives — value vs gaming | commercial lead | candidates only |
| BLK-06 | Address-book OAuth scope exposure | security lead | R4 |

## Assumptions that must hold

| # | Assumption | What breaks if false | Check |
|---|---|---|---|
| C5 | Teammates cause retention | The initiative improves a dashboard, not the business; incentives (BLK-05) become pure margin loss | REQ-D3 holdback — the readout is the check |
| C6 | Invite emails reach inboxes | R3's funnel leaks at "sent," and the never-nag rule means no second chance | Q-06 — vendor bounce data, one afternoon |
| Q-02 | First-run is the right invite moment | Skip rate (M3) pegs high and the step becomes noise | M3 after R3; wording test Q-07 |

## Top three reasons this fails

1. **BLK-03 stays disputed.** The two easiest slices sit behind an ownership question.
   The last collision shipped conflicting experiments; this one would stall instead. A
   failure by meeting, not by engineering — the most likely and the least dramatic.
2. **The experiment reads out null.** C5 falls, and the honest response is to stop at R3
   and cancel incentives — which requires having promised in advance to believe the
   readout. ¶7's "ships with its own experiment" line is that promise; hold it.
3. **Import ships anyway, under pressure, before counsel answers.** The disabled button
   becomes an enabled button in a hurry. Three blockers exist precisely to make that
   require three named people saying yes in writing.

## What would change this recommendation

1. **BLK-03, from the VP** — one name. Unblocks R2 and R3 the same day.
2. **Q-06, from platform engineering** — one afternoon with the vendor dashboard.
3. **BLK-04, from the data lead** — power math before anyone promises a readout date.

One decision, one afternoon, one calculation. R1 needs none of them.
