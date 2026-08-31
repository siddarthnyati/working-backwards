# Requirements — Empty Workspace

Every requirement cites the artifact above it. One rests on the session's load-bearing
assumption; one is shape pending behind three blockers.

## Discovery requirements (D)

```
REQ-D1 · Instrument the invite funnel end to end
Source: PR ¶3 / IFAQ-07
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: Every invite records attempted, sent, accepted, and first-action events with workspace, actor, and timestamps — including attempts abandoned before send.
Acceptance criteria:
  GIVEN a user opens the invite composer and closes it without sending
  WHEN  the session ends
  THEN  an attempted event exists with no sent event, attributable to that workspace
  AND   a full send-accept-act sequence produces all four events in order
Out of scope: showing funnel data to customers
Depends on: —
```

```
REQ-D2 · Baseline members-with-action, not members
Source: 05-telemetry.md / PR ¶1
Provenance: [OBSERVED] × 1
Statement: The Day-14 Multiplayer Rate is computable per cohort, counting only members with at least one action.
Acceptance criteria:
  GIVEN a cohort with invited members who never acted
  WHEN  D14MR is computed
  THEN  those members do not count toward multiplayer status
  AND   the report states cohort size and period
Out of scope: setting the target (Q-04)
Depends on: REQ-D1
```

```
REQ-D3 · Holdback experiment on the causal claim
Source: PR ¶2 / IFAQ-02
Provenance: [OBSERVED] × 1, [ASSUMED] × 1 → RESTS ON ASSUMPTION
Statement: A randomized holdback cohort retains the old first-run, and day-30 retention is compared against the invite-first cohort.
Acceptance criteria:
  GIVEN assignment at workspace creation
  WHEN  cohorts are compared at day 30
  THEN  the readout states effect size, confidence interval, and cohort sizes
  AND   if the experiment is underpowered at current volume, the readout says so rather than extending silently
Conditional on: BLK-04 — if volume cannot power it in a quarter, the design changes (longer window, or a proxy endpoint) and the PR's causal framing stays [ASSUMED]
Out of scope: acting on the result
Depends on: REQ-D1, BLK-04
Status: SHAPE PENDING
```

## Delivery requirements (DP)

```
REQ-DP1 · Invite step in first-run setup
Source: PR ¶1 / PR ¶3
Provenance: [OBSERVED] × 1
Statement: Workspace setup includes an invite step — email chips, send, or skip — between naming and first content.
Acceptance criteria:
  GIVEN a user on the invite step
  WHEN  they select Skip for now
  THEN  setup continues immediately with no confirmation dialog
  AND   sending invites and skipping reach the same next screen
Out of scope: contact import (REQ-DP3)
Depends on: REQ-D1
```

```
REQ-DP2 · Template gallery replaces the blank empty state
Source: PR ¶5 / EFAQ-04
Provenance: [OBSERVED] × 1
Statement: A new workspace opens on a template gallery; each card creates a working pre-populated page; Start empty is always present.
Acceptance criteria:
  GIVEN a brand-new workspace
  WHEN  the owner opens it first
  THEN  the gallery renders with Start empty as the final card
  AND   opening a template creates content without replacing anything
  AND   a template load failure falls back to the blank canvas with a retry (F3)
Out of scope: template authoring by customers; localisation (Q-08)
Depends on: —
```

```
REQ-DP3 · Contact import
Source: PR ¶3 / EFAQ-03 / RFAQ-02
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: Where privacy, regulatory and security review permit, users can import contacts to populate the invite composer.
Conditional on: BLK-01 (lawful basis, non-user retention), BLK-02 (invite email classification), BLK-06 (OAuth scope and token storage). The button ships disabled with a "pending review" tooltip until all three resolve.
Acceptance criteria:
  GIVEN all three blockers resolve permissive
  WHEN  a user imports contacts
  THEN  only selected addresses are retained, and non-selected contact data is discarded at session end
Out of scope: everything until the blockers resolve
Depends on: BLK-01, BLK-02, BLK-06
Status: SHAPE PENDING
```

```
REQ-DP4 · Invite composer available from anywhere
Source: PR ¶3 / PR ¶4
Provenance: [OBSERVED] × 2
Statement: The composer opens from the sidebar on every screen and shows per-invite status: sent, opened, joined, bounced.
Acceptance criteria:
  GIVEN an invite whose email bounced
  WHEN  the inviter opens the composer
  THEN  that invite shows bounced with a resend action (F1)
  AND   a server-side send failure is shown and preserves the entered addresses (F5)
Out of scope: bulk CSV invite
Depends on: REQ-D1
```

```
REQ-DP5 · The never-nag rule
Source: EFAQ-02 / 03-demo-spec.md F4
Provenance: [OBSERVED] × 1
Statement: Skipping the invite step is one click, gates nothing, and triggers no scheduled re-prompt anywhere in the product.
Acceptance criteria:
  GIVEN a user who skipped the invite step
  WHEN  they use the product for 30 days
  THEN  no surface re-prompts them to invite on any schedule
  AND   the composer remains one click away in the sidebar throughout
Out of scope: lifecycle marketing email (owned elsewhere — and constrained by BLK-02)
Depends on: REQ-DP1
```

---

## Flagged

**Rests on assumption**

| REQ | Assumed claim | Question | Owner role |
|---|---|---|---|
| REQ-D3 | C5 — teammates cause retention | Q-05 (power) → then the readout itself | data & analytics lead |

**Shape pending**

| REQ | Blocked by | The fork |
|---|---|---|
| REQ-D3 | BLK-04 | Powered → clean causal readout. Underpowered → longer window or proxy, and ¶2 stays [ASSUMED] |
| REQ-DP3 | BLK-01, BLK-02, BLK-06 | Permissive → import ships. Restrictive → the disabled button is removed, not left as vaporware |

## Out of scope — candidates

- **Invite incentives** — wanted by EFAQ-05; blocked conceptually by BLK-05 and logically
  by REQ-D3: paying for a behaviour not yet shown causal is paying for a metric.
- **Re-engagement email to solo workspace owners** — a retention campaign, not onboarding;
  nothing upstream asks for it, and BLK-02 constrains it anyway.

---

*8 requirements · 3 discovery · 5 delivery · 0 unsourced · 1 resting on assumption · 2 shape pending*
