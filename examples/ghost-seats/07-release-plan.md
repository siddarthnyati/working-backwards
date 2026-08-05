# Release plan — Ghost Seats

Four vertical slices. Two are schedulable today. Two are not, and saying so is the output of
this stage — six open blockers should produce a plan that is half blocked, and a plan that
isn't is a plan that quietly picked answers.

Slices are cut by narrowing the customer scenario, not by layer. R1 is not "the data model";
it is the whole path, end to end, for one integration.

## Slices

```
R1 · Confirmation recorded for the highest-volume integration
Requirements: REQ-D1
Depends on: —
Blocked by: —
Ships: every deprovisioning event on the highest-volume integration carries a recorded confirmation outcome and timestamp. No customer-facing change.
Independently testable: yes
Test harness:
  - Remove a user; assert a confirmation result exists within 60s with outcome and timestamp
  - Fault injection: hold the integration's response past the window; assert a no-response outcome is recorded rather than nothing
  - Assert no write path touches events predating the flag
  - Assert the recorded outcome is not surfaced anywhere in the product yet
Rests on assumption: —
Why first: it is the cheapest way to learn the real failure rate, and the real rate is the input to almost every open question. Ships dark on purpose.
```

```
R2 · The admin sees it
Requirements: REQ-DP1, REQ-DP3
Depends on: R1
Blocked by: —
Ships: the audit entry for a removal shows per-integration confirmation state, names any integration that did not confirm, and never renders an unrun check as complete.
Independently testable: yes
Test harness:
  - Confirmed and unconfirmed events render their correct states and integration names
  - A confirmation arriving after first render updates state on next view
  - Code-path test: with no confirmation record present, assert no path renders complete
  - Accessibility and export parity check on the new entry block
Rests on assumption: —
Why second: this is the smallest thing that delivers the press release's promise to a real admin, for one integration. Everything after it is breadth or history.
```

```
R3 · All connected integrations, with honest coverage
Requirements: REQ-D2, REQ-D3, REQ-D4, REQ-DP2, REQ-DP4
Depends on: R2
Blocked by: BLK-05
Ships: confirmation across every connected integration; unreachable distinguished from failed; integrations that cannot be checked stated as such at connection and counted in the denominator; revocation state in the access-review export; a real propagation-rate baseline.
Independently testable: yes
Test harness:
  - Per integration type: confirm, still-present, and unreachable each produce the correct distinct outcome
  - An integration with no membership read produces unverifiable-not-supported and appears in the rate denominator
  - Export carries all four states and names responsible integrations
  - Connection-time coverage statement appears once, not per removal
  - Rate computation over a seeded period matches a hand-computed figure
Rests on assumption: —
Not schedulable: BLK-05 has no owner. Until platform and partnerships agree who changes the integration contract, REQ-D3 cannot be specified — and REQ-DP2 and REQ-DP4 both read from it.
```

```
R4 · Account for what already happened
Requirements: REQ-D5, REQ-D6, REQ-DP5
Depends on: R1
Blocked by: BLK-01, BLK-02, BLK-03, BLK-06
Ships: the real exposure window per integration; a retrospective report of events that cannot be confirmed complete; notification to the customers it identifies.
Independently testable: yes
Test harness:
  - Per-integration retention values are either cited or explicitly unknown; assert no value is inherited across integrations
  - Report over a seeded historical range lists unconfirmable events and states where the range predates available data
  - Notification is issued once per workspace and the fact is recorded
Rests on assumption: REQ-D5 rests on C6 (Q-16) · REQ-DP5 rests on C7 (Q-08)
Not schedulable: four open blockers, three of them determining whether this slice exists in this shape at all. REQ-D6 and REQ-DP5 are both SHAPE PENDING. This is the slice that carries the session's actual risk, and it is the one that cannot be estimated.
```

## Dependency DAG

```
R1 ──▶ R2 ──▶ R3  [BLOCKED BY BLK-05]
 │
 └───▶ R4          [BLOCKED BY BLK-01, BLK-02, BLK-03, BLK-06]
```

Edge list:
```
R1 -> R2
R2 -> R3
R1 -> R4
```

Checks:

- **Acyclic:** yes.
- **Every requirement in exactly one slice:** all except REQ-DP9, below.
- **Duplicated requirements:** none.

**Orphan requirements (in no slice):** REQ-DP9 — deliberately. It has no source (see
`06-requirements.md`, Flagged) and unsourced work does not get scheduled. It exports with an
`unsliced` label rather than being dropped, so the backlog shows it was considered and held.

**Duplicated requirements:** none.

## Not schedulable

| Slice | Blocked by | Owner role | What unblocks it |
|---|---|---|---|
| R3 | BLK-05 | platform engineering lead + partnerships lead, jointly | An owner for the integration contract, and a per-integration answer on whether a membership read exists |
| R4 | BLK-06 | platform engineering lead | Whether historical integration state is reconstructable at all |
| R4 | BLK-01 | security lead | The real exposure window, per integration, rather than 90 days inherited from two |
| R4 | BLK-02 | privacy counsel / DPO | Whether this is a reportable failure |
| R4 | BLK-03 | legal counsel | What our DPAs commit us to, and what is owed for occurrences already past |

R1 and R2 are schedulable now and together they deliver the press release's central claim
for one integration. That is the honest read of this plan: there is real work that can start
this week, and the half of the initiative that carries the exposure cannot be planned until
five people answer five questions.

## Export

`jira-import.csv` generated by `scripts/export_jira.py`.

4 epics, 12 stories. Epic rows precede their stories. `Source:` lines are preserved verbatim
in Description — traceability has to survive the export or it dies at the import. Blocked
slices carry the `blocked` label and inherit priority from the severity of the blockers they
depend on; they are exported rather than dropped, because a blocked epic sitting in the
backlog is the record of why the work stopped.
