# Requirements format

Read this before Stage 6. This stage is where the pipeline stops being a narrative and
starts being something engineering can pick up.

## The block

```
REQ-D1 · Detect propagation failure per connected integration
Source: PR ¶4 / IFAQ-12
Provenance: [OBSERVED] × 1, [ASSUMED] × 1 → RESTS ON ASSUMPTION
Statement: The platform records, for each deprovisioning event, whether each connected
  integration confirmed removal, and marks the event incomplete if any did not.
Acceptance criteria:
  GIVEN a workspace with three connected integrations
  WHEN  an admin removes a user and integration B does not confirm within 60 seconds
  THEN  the deprovisioning event is recorded as incomplete and names integration B
Out of scope: retroactive detection for events that occurred before this ships (see REQ-D4)
Depends on: BLK-05
```

Field by field:

**ID** — `REQ-D<n>` for Discovery, `REQ-DP<n>` for Delivery. IDs are permanent once written;
release slices and blockers cite them.

**Source** — the press release paragraph or FAQ answer this derives from. Mandatory. See
[sourcing](#the-sourcing-rule).

**Provenance** — the tags carried by the claims in the source chain. If any is `[ASSUMED]`,
append `RESTS ON ASSUMPTION` and list the requirement separately in `08-readiness.md`.
Traceability without provenance just documents the chain of custody on a guess.

**Statement** — one sentence, present tense, testable. If you need "and" twice, it is two
requirements.

**Acceptance criteria** — Given/When/Then. See below.

**Out of scope** — what a reasonable reader would assume this covers and it does not. This
field prevents more argument than any other, and it is the one people skip.

**Depends on** — REQ ids and BLOCKER ids. A requirement depending on an OPEN blocker cannot
be scheduled; Stage 7 needs to know that.

## Given/When/Then

The criteria are the handoff. Written well, an engineer can build from them and a tester can
verify without asking you anything.

**GIVEN** is state, not action. The world before anything happens. Include the parts that
matter to the outcome and nothing else.

**WHEN** is exactly one action by exactly one actor. Two whens is two scenarios.

**THEN** is observable — something a person or a test can see from outside the system. "The
event is recorded as incomplete and names integration B" is observable. "The system knows
integration B failed" is not; knowing is not observable.

**Good**
```
GIVEN an admin has removed a user and all integrations confirmed within 60 seconds
WHEN  the admin opens the audit entry for that removal
THEN  the entry shows a complete status and lists each integration with its confirmation time
```

**Bad**
```
GIVEN the system is working correctly
WHEN  deprovisioning happens
THEN  it works properly and the admin is informed
```
Why: "working correctly" is unspecified state, "deprovisioning happens" has no actor,
"properly" is not observable, and "informed" doesn't say through what surface.

Cover, at minimum: the happy path, the failure this requirement exists to handle, and the
boundary (what happens at exactly 60 seconds, at zero integrations, at the limit).

## Discovery vs Delivery

**Discovery (D)** — requirements whose purpose is to find out something you don't know:
instrumentation, enumeration, a measurement you need before you can size the real work.
Ships first, usually cheap, and frequently changes what the DP requirements should be.

**Delivery (DP)** — requirements that change the customer's experience.

The split matters because D requirements are how you avoid building the wrong DP. In a
problem with a lot of `[ASSUMED]` claims, expect more D than DP, and say so — a plan that is
mostly discovery is the correct plan for a poorly understood problem, not a weak one.

## The sourcing rule

Every requirement cites the artifact above it. A requirement that cannot cite anything is
not customer-derived, and "a requirement with no source" is a fairly precise definition of
scope creep.

When you find one, three options in order of preference:

1. **Find its real source.** Often it exists and just wasn't written down.
2. **Push it upstream.** If it belongs, the customer need belongs in the press release. Add
   it there, re-run the Stage 1 critic, and let it flow down. This is the honest fix and it
   is rarer than it should be because it costs a re-review.
3. **Move it to "Out of scope — candidates."** Keep it visible. Deleting good ideas makes
   people stop offering them; a candidates section costs nothing.

Never silently accept an unsourced requirement. Flag it in the artifact:

```
REQ-DP7 · Bulk export of admin audit history
Source: NONE — FLAGGED, not customer-derived
```

## When the source is a blocker, not an answer

Common and worth handling explicitly. A blocker is an open question, so a requirement
derived from one is conditional — its shape depends on an answer you don't have.

Write it, cite the blocker, and state the conditionality:

```
REQ-D4 · Enumerate accounts affected before this ships
Source: IFAQ-05 / BLK-06
Statement: The platform produces a list of deprovisioning events since a given date where
  at least one integration cannot be confirmed to have removed access.
Conditional on: BLK-06 — if historical integration logs are unavailable, this requirement
  becomes "enumerate going forward only" and the customer-notification requirement
  (REQ-DP3) changes shape with it.
Depends on: BLK-06
Status: SHAPE PENDING
```

`SHAPE PENDING` is honest and useful: Stage 7 can slice around it, and the readiness doc can
list it under "assumptions that must hold." What you must not do is pick the convenient
branch and write the requirement as if the question were settled.

## Grouping and ordering

Order within each group by dependency, not importance — the reader should be able to read
top to bottom without a forward reference. Where two requirements are mutually independent,
order by which one a slice needs first.

Close the artifact with:

- **Out of scope — candidates**: unsourced ideas, kept visible.
- **Flagged**: requirements with no source, or resting on assumptions, listed together so
  the reader sees the shape of the risk in one place.

## Critic dimensions at this stage

1 (customer specificity), 2 (evidence presence), 5 (traceability), 7 (clarity), 8 (template
completeness), plus 6 (falsifiability) as questions. Dimension 5 is the one that bites here
and it should — an unsourced requirement is exactly what this stage exists to catch.
