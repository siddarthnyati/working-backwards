# Requirements — Ghost Seats

Every requirement cites the artifact above it. Sources point at `01-press-release.md`
paragraph markers, FAQ IDs, demo-spec failure states, and blocker IDs — all of which exist
in this directory and are checkable.

Two requirements rest on assumptions that entered at Stage 0 and propagated the whole way
down. They are listed in **Flagged** and again in `08-readiness.md`. This is the point of
carrying provenance alongside traceability: REQ-D5 cites a real paragraph in a real press
release, and the claim in that paragraph has no source.

## Discovery requirements (D)

```
REQ-D1 · Record a confirmation result per integration per deprovisioning event
Source: PR ¶3 / IFAQ-14
Provenance: [OBSERVED] × 2
Statement: For every deprovisioning event, the platform records for each connected integration whether that integration confirmed removal, and the time the result arrived.
Acceptance criteria:
  GIVEN a workspace with a connected integration that supports a membership read
  WHEN  an admin removes a user
  THEN  a confirmation result is recorded for that integration with an outcome and a timestamp
  AND   the result is recorded whether the outcome is confirmed, still-present, or no-response
Out of scope: showing any of this to an admin (REQ-DP1); integrations that expose no membership read (REQ-D3)
Depends on: —
```

```
REQ-D2 · Distinguish an unreachable integration from a failed propagation
Source: 03-demo-spec.md F3 / IFAQ-11
Provenance: [OBSERVED] × 1
Statement: A confirmation result records unreachable and still-present as different outcomes, and the platform never reports the first as the second.
Acceptance criteria:
  GIVEN a connected integration that is returning transport errors
  WHEN  an admin removes a user and the integration cannot be reached inside the window
  THEN  the result is recorded as unverifiable-provider-unavailable, not as incomplete
  AND   a subsequent successful check on the same event overwrites it with the real outcome
Out of scope: retry policy and backoff; alerting on provider outages
Depends on: REQ-D1
```

```
REQ-D3 · Enumerate which connected integrations can be checked at all
Source: IFAQ-12 / EFAQ-03
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: The platform holds, per integration type, whether a membership read is available, and treats absence of that capability as a stated limitation rather than a passing check.
Acceptance criteria:
  GIVEN an integration type with no membership read available
  WHEN  a deprovisioning event occurs on a workspace using it
  THEN  the result is recorded as unverifiable-not-supported
  AND   that integration is excluded from the numerator and included in the denominator of the propagation rate
Out of scope: building membership reads for integrations that lack them; renegotiating integration contracts
Depends on: BLK-05
```

```
REQ-D4 · Establish a propagation-rate baseline
Source: PR ¶3 / IFAQ-15 / 05-telemetry.md
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: Once confirmation results exist, the platform reports Revocation Propagation Rate over a period, with unverifiable events counted in the denominator.
Acceptance criteria:
  GIVEN confirmation results have been recorded for a full reporting period
  WHEN  the propagation rate is computed for that period
  THEN  the rate counts every deprovisioning event in the denominator including unverifiable ones
  AND   the report states the period and the number of events it covers
Out of scope: setting a target (Q-15, unanswered); any retroactive baseline (REQ-D6)
Depends on: REQ-D1, REQ-D3
```

```
REQ-D5 · Determine the real exposure window per integration
Source: PR ¶2 / IFAQ-07
Provenance: [OBSERVED] × 1, [ASSUMED] × 1 → RESTS ON ASSUMPTION
Statement: For each connected integration, the platform records the documented interval between a failed propagation and the loss of cached read access.
Acceptance criteria:
  GIVEN a connected integration type
  WHEN  its cache retention behaviour is recorded
  THEN  the recorded value is either a documented interval with a citation, or explicitly unknown
  AND   no integration carries a value inherited from a different integration
Out of scope: changing any integration's retention; measuring actual access during the window (Q-10)
Depends on: BLK-01
```

> **Why this is flagged.** PR ¶2 says the window is 90 days. That figure is `[OBSERVED]` for
> two integrations and `[ASSUMED]` (claim C6) for every other one. The press release reads as
> though 90 days is the number. If it is wrong for a third integration — shorter or unbounded
> — the severity in `08-readiness.md` changes and so does BLK-01. The last acceptance
> criterion exists specifically to stop the assumption being re-made during implementation.

```
REQ-D6 · Produce a retrospective affected-account report
Source: PR ¶7 / IFAQ-14 / EFAQ-06
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: An operator can request, for a date range, the deprovisioning events that cannot be confirmed complete.
Acceptance criteria:
  GIVEN historical deprovisioning events exist for a workspace
  WHEN  an operator requests an affected-account report for a date range
  THEN  the report lists every event in range that cannot be confirmed complete
  AND   where the range predates available data, the report says so rather than returning an empty result
Conditional on: BLK-06 — if historical integration state cannot be reconstructed, this becomes "report from the instrumentation date forward only," PR ¶7 has to be rewritten, and REQ-DP5 loses its input entirely
Out of scope: notifying the customers it identifies (REQ-DP5)
Depends on: BLK-06, REQ-D1
Status: SHAPE PENDING
```

## Delivery requirements (DP)

```
REQ-DP1 · Show confirmation state on the audit entry
Source: PR ¶3 / EFAQ-05
Provenance: [OBSERVED] × 1
Statement: The audit entry for a removal shows each connected integration with its confirmation outcome and timestamp.
Acceptance criteria:
  GIVEN a deprovisioning event with one integration confirmed and one not responding
  WHEN  an admin opens the audit entry for that removal
  THEN  the entry shows an incomplete state and names the integration that did not respond
  AND   a confirmation arriving after the entry was first rendered updates the state on next view
Out of scope: remediating from the entry (see Flagged, REQ-DP9); email or webhook notification
Depends on: REQ-D1
```

```
REQ-DP2 · Carry revocation state into the access-review export
Source: PR ¶3 / EFAQ-05
Provenance: [OBSERVED] × 1
Statement: Each removal in the access-review export carries its confirmation state and the names of any integrations that did not confirm.
Acceptance criteria:
  GIVEN a date range containing removals in each of the four states
  WHEN  an admin runs the access-review export for that range
  THEN  every row carries one of complete, incomplete, unverifiable-provider-unavailable, or unverifiable-not-supported
  AND   rows that are not complete name the integrations responsible
Out of scope: changing the export's existing columns or file format
Depends on: REQ-D1, REQ-D2, REQ-D3
```

```
REQ-DP3 · Never render an unrun check as complete
Source: 03-demo-spec.md F5 / PR ¶2
Provenance: [OBSERVED] × 1
Statement: Where the confirmation mechanism did not run, the audit entry says so and does not display a complete state.
Acceptance criteria:
  GIVEN the confirmation mechanism did not execute for a deprovisioning event
  WHEN  an admin opens the audit entry for that removal
  THEN  the entry states that the check did not run
  AND   no code path renders complete in the absence of a recorded confirmation result
Out of scope: alerting engineering when the mechanism fails
Depends on: REQ-DP1
```

> The current defect is precisely "silence rendered as success." Rebuilding it inside the fix
> is the specific failure this requirement exists to prevent, which is why the second
> criterion is written against the code path rather than against the screen.

```
REQ-DP4 · State coverage at connection time
Source: 03-demo-spec.md F4 / 04-docs.md
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: When an admin connects or reviews an integration, the platform states whether removals through it can be confirmed.
Acceptance criteria:
  GIVEN an integration type with no membership read available
  WHEN  an admin connects it or views its settings
  THEN  the platform states that removals through this integration cannot be confirmed
  AND   this is stated once at connection and in settings, not repeated on every removal
Out of scope: preventing the connection
Depends on: REQ-D3
```

```
REQ-DP5 · Notify customers identified as affected
Source: EFAQ-10 / IFAQ-06
Provenance: [OBSERVED] × 1, [ASSUMED] × 1 → RESTS ON ASSUMPTION
Statement: Customers identified by the affected-account report are notified, through a channel and on a timeline set by legal counsel.
Acceptance criteria:
  GIVEN the affected-account report has identified a set of workspaces
  WHEN  the notification defined by BLK-03 is issued
  THEN  each identified workspace receives it once, with the events and date range that apply to them
  AND   the fact and time of notification is recorded per workspace
Conditional on: BLK-03 (what is owed), BLK-02 (whether it is reportable), BLK-06 (whether the population can be named at all). All three OPEN. The content, the channel, and whether this requirement exists at all are not decidable here.
Out of scope: everything about the notification's content
Depends on: BLK-02, BLK-03, BLK-06, REQ-D6
Status: SHAPE PENDING
```

> **Why this is flagged.** Claim C7 — "most affected customers have never discovered this" —
> is `[ASSUMED]`. It is the premise that makes this a proactive notification rather than a
> response to complaints already in the queue. If C7 is false, some customers already know
> and the communication problem is a different one that started earlier. The assumption
> reached here through EFAQ-10 and IFAQ-02, and nothing along the way tested it.

---

## Flagged

**No source — not customer-derived**

```
REQ-DP9 · Force removal from the audit entry
Source: NONE — FLAGGED, not customer-derived
Statement: An admin can trigger removal in a non-confirming integration directly from the audit entry.
Depends on: BLK-05
```

> This is the first thing anyone asks for after seeing the demo, and nothing above it asks
> for it. The press release deliberately stops at reporting (PR ¶3), and EFAQ-02 states the
> boundary out loud. It is kept here rather than deleted, and it is not in a release slice.
>
> The honest fix, if it belongs, is upstream: put remediation in the press release, re-run
> the Stage 1 critic, and let it flow down with a source. That costs a re-review, which is
> exactly why people would rather add it here — and exactly why the rule exists.

| REQ | Title | Disposition |
|---|---|---|
| REQ-DP9 | Force removal from the audit entry | Held. Not in a slice. Needs a press-release source or it stays out. |

**Rests on assumption**

| REQ | Assumed claim | Question | Owner role |
|---|---|---|---|
| REQ-D5 | C6 — the 90-day cache window applies to all integrations, not just the two examined | Q-16 · What is each integration's actual retention? | platform engineering lead, partnerships lead |
| REQ-DP5 | C7 — most affected customers have never discovered this | Q-08 · Is there support or renewal evidence that any customer already knows? | support lead, enterprise renewals lead |

**Shape pending**

| REQ | Blocked by | How the shape changes with each answer |
|---|---|---|
| REQ-D6 | BLK-06 | Reconstructable → report as written in PR ¶7. Not reconstructable → forward-only report, PR ¶7 rewritten, REQ-DP5 loses its input |
| REQ-DP5 | BLK-02, BLK-03, BLK-06 | Reportable → regulated clock and content. Not reportable but contractually owed → customer comms on our timeline. Neither → the requirement does not exist |

## Out of scope — candidates

- **Force removal from the audit entry** (REQ-DP9) — would need remediation in PR ¶3 and a
  resolved BLK-05 before it could be scoped.
- **Alerting engineering on confirmation-mechanism failure** — implied by REQ-DP3's second
  criterion but not derivable from any customer-facing source. Operational, and it belongs
  to whoever runs the service.
- **Evidence of what removed users actually accessed during a window** — the number PR ¶2
  most wants. Blocked upstream by Q-10, which is a partnerships and privacy question rather
  than a requirement.

---

*12 requirements · 6 discovery · 6 delivery · 1 unsourced and flagged · 2 resting on
assumptions · 2 shape pending*
