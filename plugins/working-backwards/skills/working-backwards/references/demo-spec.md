# Demo spec

Read this before Stage 3. Output: `03-demo-spec.md`.

## What this stage is for

An alignment device, not a design deliverable. The press release is prose, and prose can
hide a hole; a demo script cannot. If you cannot narrate the experience end to end —
screens or API surface, step by step, including what the user sees when things fail — you
do not yet understand the product, and it is cheaper to find that out here than in a
design review.

## Required structure

1. **Surface** — the screens or API endpoints that change, each with what changes and a
   `Source:` citation to the PR paragraph or FAQ answer that demands it. A surface with no
   source is scope creep wearing pixels.
2. **Primary flow** — numbered steps, each in the form *actor does X → sees Y*. If a step
   has no visible outcome, either find the outcome or cut the step.
3. **Failure states** — a table: what fails · exactly what the user sees · source. This is
   the section that earns the stage. Rules:
   - Distinguish *can't-know* from *failed*. An upstream outage and a genuine failure must
     never render the same way, or users learn to ignore the signal within a month.
   - **Silence never renders as success.** If the mechanism you are specifying did not run,
     the surface says so. The most common defect this pipeline meets is silence rendered as
     success; do not rebuild it inside the fix.
   - A blocked capability ships *visibly absent* — a disabled control with an honest reason
     ("pending privacy review") beats an invisible gap, because it makes the roadmap legible
     without shipping the risk.
4. **What this deliberately does not show** — the scope boundary, stated out loud. Name the
   thing viewers will assume is included and isn't, and say which blocker or decision keeps
   it out. A demo that lets someone infer a capability creates a commitment nobody made.
5. **Open questions surfaced** — anything the narration could not settle, as `Q-nn` entries
   with owner roles.

## The narration test

Before writing the file, narrate the demo aloud, start to finish, as if presenting. Every
place you improvise or wave a hand is a hole in the spec. Write those down — they are the
stage's real findings.

## Good vs bad failure state

**Bad:** "If the invite fails, the user is notified." — Which failure? Notified where, when,
saying what? Can they act on it?

**Good:** "Invite email bounces → status chip 'bounced — check address' on that row of the
composer, visible next open, with a resend action." — Observable, located, actionable.

## What the critic checks here

Dimensions 5, 7, 8. Traceability means every surface and failure state cites upstream.
Completeness means the scope-boundary section exists — a demo spec without one gets REVISE,
because the boundary is where demos create accidental commitments.
