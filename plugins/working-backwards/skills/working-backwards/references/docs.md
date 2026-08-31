# Docs

Read this before Stage 4. Output: `04-docs.md`.

## What this stage is for

Draft the customer-facing documentation *before anything is built*, from the approved press
release and external FAQ only. Two things come free:

1. **The interface contract has to exist early.** You cannot document a flow whose steps
   are undecided — so writing forces the decisions, at draft cost instead of build cost.
2. **The doc is an honest complexity meter.** If "getting started" runs twelve steps,
   customers will not adopt the thing, and you learned that before engineering spent a
   sprint on it.

## Required structure

What it does (one paragraph, cited to the PR) · Before you start · How to use it, stepwise ·
What you'll see when something fails (from the demo spec's failure states) · Limits ·
Troubleshooting table · **Could not be written yet**.

## The rule that makes this stage honest

**Where a paragraph won't come, do not write around it.** Record it under "could not be
written yet" with the blocker or question behind it. A paragraph that stalls is a product
gap, not a writing problem — and the list of stalled paragraphs is this stage's actual
deliverable. In practice this section reliably surfaces one question no earlier stage was
forced to answer (in the worked examples: "which integrations are covered?" and "what will
contact import be allowed to do?").

Rules for the gaps:
- Each entry names the blocker or `Q-nn` that keeps it unwritable, and its owner role.
- `[UNKNOWN]` in a limits table is a complete answer. "TBD" is not — it records that
  someone stopped typing.
- Never document a capability whose shape depends on an open blocker "optimistically."
  A doc that guesses becomes a commitment the review never approved.

## Voice

Second person, present tense, the customer's vocabulary — no internal system names, no
codenames. If a sentence cannot be read aloud to a customer on a support call, it does not
belong in this file.

## What the critic checks here

Dimensions 3, 5, 7, 8. Dimension 3 here means the doc meets users where they are — it
acknowledges what they do today (the workaround, the old tool) when relevant to migration.
Dimension 8 treats an explicit gap as complete and a silent omission as failure.
