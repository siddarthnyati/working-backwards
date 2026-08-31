# Readiness

Read this before Stage 8. Output: `08-readiness.md`.

## What this stage is for

The go/no-go — and the honest ledger of what the session still does not know. This artifact
is what a sponsor reads. It must be decidable-from, not merely informative.

## Required structure, in order

1. **The confidence block first.** Claims by provenance · requirements (total, resting on
   assumptions, unsourced) · slices (schedulable vs not) · questions (open, unowned) ·
   blockers by severity · context-pack status. The reader gets the epistemic state before
   the recommendation, so the recommendation can be weighed.
2. **Recommendation** — GO / GO WITH CONDITIONS / NO-GO / NOT YET DECIDABLE, with scope.
   - Scope the GO to what is actually unblocked ("GO on R1 and R2 only"). A GO covering
     slices that sit on open blockers fails review, because it silently answers questions
     that belong to counsel or compliance.
   - Distinguish "recommendation to start work" from "recommendation to fund the
     initiative" when the second turns on unevaluable dimensions — say which one you are
     making.
   - NOT YET DECIDABLE is a legitimate recommendation. A verdict manufactured out of open
     questions is the failure mode this whole pipeline exists to prevent.
3. **Open blockers by severity** — high before medium before low, with owner and what each
   blocks.
4. **Assumptions that must hold** — each with: what breaks if false, the requirements
   affected, and how to check. The assumptions here must be the ones tagged at intake and
   carried — this section is where propagation pays off, not where new assumptions appear.
5. **Top three reasons this fails** — *most likely first, not most dramatic*. The honest
   list usually leads with something boring: an ownership dispute, a retention window, a
   metric nobody reads. Resist ranking by vividness.
6. **What would change this recommendation** — the smallest set of answers that moves it,
   each with its owner. This is the ask; make it small enough to act on this week
   ("one decision, one afternoon, one calculation" is the right size).

## Rules

- Nothing is resolved here. Blockers keep their user-owned `Status: OPEN`; unknowns stay
  unknown. Readiness reports the state; it does not tidy it.
- If a blocker is urgent *independently of the initiative* (a live exposure, not a launch
  dependency), say so separately and plainly — burying a today-problem in a launch list is
  how it waits for the launch.
- Requirements flagged `RESTS ON ASSUMPTION` and `SHAPE PENDING` are listed by name. The
  reader must be able to see the shape of the risk in one place.

## What the critic checks here

Dimensions 2, 5, 8 — and the one review question that matters most: *does the
recommendation follow from the artifact, or from optimism?* Cross-check the GO scope
against the blocker table; any slice inside the GO that a HIGH blocker blocks is a fail.
