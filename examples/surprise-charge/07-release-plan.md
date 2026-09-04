# Release plan — The Surprise Charge

## Slices

```
R1 · Measure the fury
Requirements: REQ-D1
Depends on: —
Blocked by: —
Ships: the surprise join — Surprise Rate and the silent-surprised proxy computable per cohort. Dark.
Independently testable: yes
Test harness:
  - Seeded cohort computes Surprise Rate with stated sizes
  - M4 proxy joins charge → inactivity → month-2 churn
Why first: the baseline exists before anything changes, so every later claim is measurable against it. No meeting required.
```

```
R2 · No-surprise surfaces
Requirements: REQ-DP2, REQ-DP4
Depends on: —
Blocked by: —
Ships: the day-12 banner and honest receipts. In-app only — no email infra, no vendor risk.
Independently testable: yes
Test harness:
  - Banner renders day 12+ with date, price, both actions
  - Every receipt carries next renewal date, price, cancel link
```

```
R3 · The reminder + the experiment
Requirements: REQ-DP1, REQ-D2
Depends on: R1
Blocked by: BLK-01, BLK-05
Ships: the T-48h email with the holdback experiment attached — the readout that ends the finance argument.
Independently testable: yes
Test harness:
  - Ordering guarantee: send precedes charge by ≥48h (M1)
  - Send failure is logged, never silent (F5)
  - Holdback assignment is random and recorded at trial start
```

```
R4 · One-tap cancel, everywhere
Requirements: REQ-DP3, REQ-DP5
Depends on: R2
Blocked by: BLK-02
Ships: one-tap cancel from all three surfaces; the parity rule asserted in CI per market.
Independently testable: yes
Test harness:
  - Cancel completes in one screen from reminder, banner, receipt
  - Parity assertion: cancel steps ≤ subscribe steps per market config
```

## Dependency DAG

```
R1 ──▶ R3   [BLOCKED BY BLK-01 · BLK-05]

R2 ──▶ R4   [BLOCKED BY BLK-02]
```

Edge list:
```
R1 -> R3
R2 -> R4
```

Checks: acyclic · 7/7 requirements in exactly one slice · no orphans · no duplicates.

## Not schedulable

| Slice | Blocked by | Owner | What unblocks |
|---|---|---|---|
| R3 | BLK-01 | finance lead | Co-designing the holdback — one meeting |
| R3 | BLK-05 | platform lead | Owning the send-before-charge ordering |
| R4 | BLK-02 | compliance lead | The per-market cancel-method memo |

R1 and R2 start today. Both halves of the argument get better off R1 alone.

## Export

`jira-import.csv` — 4 epics, 7 stories.
