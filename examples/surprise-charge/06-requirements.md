# Requirements — The Surprise Charge

7 requirements. One rests on the session's central assumption; two are shape pending.

## Discovery requirements (D)

```
REQ-D1 · Build the surprise join
Source: PR ¶2 / IFAQ-03
Provenance: [OBSERVED] × 2
Statement: Charges join to refunds, "surprise" tickets, and activity history, so Surprise Rate and the silent-surprised proxy compute per cohort.
Acceptance criteria:
  GIVEN a cohort with charges, refunds, tickets and activity data
  WHEN  the join runs
  THEN  Surprise Rate and M4 compute with cohort sizes stated
Out of scope: dashboards
Depends on: —
```

```
REQ-D2 · The reminder holdback experiment
Source: PR ¶7 / IFAQ-01
Provenance: [OBSERVED] × 1, [ASSUMED] × 1 → RESTS ON ASSUMPTION
Statement: A randomized holdback cohort receives no reminder; net revenue at day 60 is compared, reminded vs holdback.
Acceptance criteria:
  GIVEN random assignment at trial start
  WHEN  the day-60 readout runs
  THEN  it states effect size, confidence interval and cohort sizes — or declares itself underpowered rather than extending silently
Conditional on: BLK-01 — finance co-owns the design, or the readout settles nothing
Out of scope: acting on the result
Depends on: REQ-D1, BLK-01
Status: SHAPE PENDING
```

## Delivery requirements (DP)

```
REQ-DP1 · The T-48h reminder
Source: PR ¶3 / EFAQ-03
Provenance: [OBSERVED] × 1
Statement: One email, at least 48 hours before the first charge, stating price and date, with equal keep and one-tap-cancel actions.
Acceptance criteria:
  GIVEN a trial reaching day 12
  WHEN  the reminder sends
  THEN  it precedes the charge by ≥48h (M1 records the ordering)
  AND   a send failure is logged and visible — never silently absorbed (F5)
Out of scope: reminders for later renewals
Depends on: REQ-D1, BLK-05
```

```
REQ-DP2 · The in-app backstop banner
Source: PR ¶3 / 03-demo-spec.md F1
Provenance: [OBSERVED] × 1
Statement: From day 12, an in-app banner states the charge date and price with the same two actions, until the user decides.
Acceptance criteria:
  GIVEN a trial user with the email unopened
  WHEN  they open the app on day 12+
  THEN  the banner shows date, price, keep, and one-tap cancel
Out of scope: push notifications
Depends on: —
```

```
REQ-DP3 · One-tap cancel
Source: PR ¶5 / RFAQ-02
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: Cancelling from reminder, banner, or receipt is one screen and one tap, confirmed immediately, data retained 30 days.
Conditional on: BLK-02 / Q-06 — markets that prescribe a cancel method get a per-market flow, still never more steps than signup
Acceptance criteria:
  GIVEN a user in the default flow
  WHEN  they tap cancel from any of the three surfaces
  THEN  cancellation completes on that screen with inline confirmation
Out of scope: win-back offers
Depends on: BLK-02
Status: SHAPE PENDING
```

```
REQ-DP4 · Receipts that prevent the next surprise
Source: PR ¶5 / EFAQ-04
Provenance: [OBSERVED] × 1
Statement: Every receipt shows amount, next renewal date, next price, and a cancel link.
Acceptance criteria:
  GIVEN any successful charge
  WHEN  the receipt renders
  THEN  next renewal date, price and a cancel link are present
Out of scope: dunning redesign (F2 copy only)
Depends on: —
```

```
REQ-DP5 · The parity rule
Source: EFAQ-02 / 03-demo-spec.md F4
Provenance: [OBSERVED] × 1
Statement: Cancelling never requires more steps than subscribing did, in any market, on any surface.
Acceptance criteria:
  GIVEN the subscribe flow takes N steps in a market
  WHEN  the cancel flow is measured in that market
  THEN  its step count is ≤ N, asserted in CI per market config
Out of scope: nothing — this rule has no exceptions
Depends on: REQ-DP3
```

---

## Flagged

| REQ | Flag | Why |
|---|---|---|
| REQ-D2 | RESTS ON ASSUMPTION | C5 — the finance fear, unmeasured; the requirement exists to measure it |
| REQ-D2, REQ-DP3 | SHAPE PENDING | BLK-01 (experiment design), BLK-02 (per-market cancel) |

## Out of scope — candidates

- **Win-back discount in the cancel flow** — wanted the moment the demo was seen; cites
  nothing upstream. The judge held it at the door: "does its source demand it, or merely
  permit it?" It goes upstream into a PR revision, or nowhere.
- **Proactive refunds for past charges** — BLK-03's call, not a requirement yet.

*7 requirements · 2 discovery · 5 delivery · 0 unsourced*
