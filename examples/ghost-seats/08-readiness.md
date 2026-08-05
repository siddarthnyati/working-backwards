# Readiness — Ghost Seats

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

## Recommendation

**GO WITH CONDITIONS — on R1 and R2 only.**

R1 and R2 are unblocked, independently shippable, and together they deliver the press
release's central claim for one integration. R1 also produces the measurement that most of
the open questions are waiting on, which makes starting it the cheapest way to make the rest
of this decidable.

R3 and R4 are not decidable from this document and should not be estimated. Four of the six
blockers are unanswered in a way that changes what those slices are, not merely when they
ship. Committing a date to R4 in particular would be committing to a shape nobody has agreed.

**This is not a recommendation on whether to fund the initiative.** That turns on Q-04 and
on BLK-03 and BLK-04, none of which are evaluable here. It is a recommendation on what can
start while those are answered.

## Open blockers by severity

### High

| ID | Category | Ask | Owner role | Blocks |
|---|---|---|---|---|
| BLK-01 | SECURITY | Real exposure window per integration — is 90 days a ceiling or the number we happened to find? | security lead | REQ-D5, R4 |
| BLK-02 | PRIVACY | Is retained access after revocation a reportable failure of processor obligations, and on what clock? | privacy counsel / DPO | REQ-DP5, R4 |
| BLK-03 | LEGAL | What do our DPAs commit us to, and what is owed for occurrences already past? | legal counsel | REQ-DP5, R4 |
| BLK-04 | REGULATORY | Have we been attesting to a SOC 2 control that has not operated as described? | compliance lead | disclosure position; severity across the board |
| BLK-05 | DEPENDENCY | Who owns the integration contract, and which integrations expose a membership read? | platform + partnerships leads | REQ-D3, R3 |
| BLK-06 | DATA | Can the affected population be enumerated retroactively, or only forward? | platform engineering lead | REQ-D6, REQ-DP5, R4 |

### Medium
None.

### Low
None.

Six high and nothing below is worth a second look, and it holds. Each one either blocks a
release slice or changes what is owed to customers. Nothing was inflated to look serious and
nothing was downgraded to make the count more comfortable.

## Assumptions that must hold

| # | Assumption | What breaks if false | Requirements affected | How to check |
|---|---|---|---|---|
| C6 | The 90-day cache window applies to all connected integrations, not just the two examined | The exposure window is wrong in PR ¶2, BLK-01's severity changes, and an integration with unbounded caching would make this materially worse than described | REQ-D5 | Read each integration's documented retention. Cheap. Nobody has done it. → Q-16 |
| C7 | Most affected customers have never discovered this | Some customers already know, and the communication problem started before this session did — proactive notification becomes a response to a queue that already exists | REQ-DP5 | Search support tickets for access-review disputes; ask the renewals lead → Q-08 |
| Q-18 | Propagation failures are detectable platform-side without polling every integration | The central claim in PR ¶3 is not deliverable as written, and R1 is a different piece of work | REQ-D1, REQ-D3 | Platform engineering lead, one conversation |
| Q-20 | 60 seconds is achievable across systems we do not control | The subheading comes out of the press release | subheading, PR ¶3, M1 | Latency profile of connected integrations |

C6 and C7 are the two that propagated all the way from intake into flagged requirements
without anything testing them along the way. That is the mechanism working: they are visible
here because they were tagged at Stage 0 and carried, not because anyone remembered them.

## Requirements resting on assumptions

| REQ | Assumed claim in its source chain |
|---|---|
| REQ-D5 · Determine the real exposure window per integration | C6 — 90 days inherited from two integrations to all of them |
| REQ-DP5 · Notify customers identified as affected | C7 — most affected customers have never discovered this |

## Requirements with no settled shape

| REQ | Blocked by | Decision the answer forces |
|---|---|---|
| REQ-D6 · Retrospective affected-account report | BLK-06 | Whether PR ¶7 survives as written |
| REQ-DP5 · Notify affected customers | BLK-02, BLK-03, BLK-06 | Whether this requirement exists at all |

## Top three reasons this fails

1. **BLK-06 comes back "going forward only."** The affected-account report cannot be built as
   promised, PR ¶7 has to be rewritten, REQ-DP5 loses its input, and the question customers
   care about most — *was I affected* — becomes permanently unanswerable. This is the most
   likely of the three and it is not the most dramatic, which is why it is first.

2. **Admins learn to ignore the incomplete state.** If provider outages (F3) render the same
   way as genuine retained access (F1), the signal is noise within a quarter and we have
   built a worse version of nothing. Q-19 has no owner, which means nobody is currently
   accountable for finding out whether this is already true of existing warnings in this
   surface.

3. **BLK-05 stays unowned.** Platform and partnerships each have a reason it is the other's,
   R3 never becomes schedulable, and the feature ships covering one integration while the
   press release describes all of them. This is a failure by stalling rather than by
   decision, and it is the hardest kind to notice happening.

## Questions with no owner

**Q-19** — will admins act on an incomplete state when shown one?
**Q-20** — is 60 seconds achievable across systems we do not control?

Both sit under load-bearing sentences: Q-20 under the subheading, Q-19 under the central
promise of ¶3. Neither has anyone to ask, and the reason is the absent ownership map.

Assigning these is a smaller action than answering them and it is the one to take first.

## What would change this recommendation

The smallest set of answers that moves this. This is the ask.

1. **An owner for BLK-05.** One name, not two. This unblocks R3 and half the coverage story.
2. **BLK-06, from the platform engineering lead.** One conversation. It determines whether R4
   exists in its current shape and whether PR ¶7 is honest.
3. **Q-04, from the VP.** Whether the rationale in ¶1 and ¶6 is the right one, and whether
   this is the quarter. Everything above is execution; this one is whether to execute.

Three conversations. Two of them under thirty minutes.

---

*Ran at context tier 0, deliberately. See `CONFIDENCE.md` for what each missing document
would have bought, and `examples/ghost-seats-with-context/` for the same problem's first two
stages with a strategy document present.*
