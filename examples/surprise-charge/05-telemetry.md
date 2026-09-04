# Telemetry — The Surprise Charge

## North star

**Surprise Rate** — of first charges in a cohort, the % followed within 7 days by a refund
request or a "surprise/didn't know" support ticket.

**Why this and not open rates:** the gate question caught it — the author named reminder
open rate as the metric they'd game ("send at 9am, call it engagement"). Opens measure the
email; the Surprise Rate measures the fury. **Baseline: computable today** from existing
refund + ticket data `[OBSERVED]` — this metric works before anything ships, which is what
makes the experiment honest.

**Measures:** PR ¶1 "nobody gets charged by surprise."

## Input metrics

| # | Metric | Measures | Baseline |
|---|---|---|---|
| M1 | Reminder delivered ≥48h before charge (the ordering guarantee) | PR ¶3 / BLK-05 | n/a — new |
| M2 | Cancel-before-charge rate, forgot-cohort | PR ¶3 | `[UNKNOWN]` until R1 join exists |
| M3 | Trial→paid conversion, reminded vs holdback | C5 — the finance question | 5-quarter history `[OBSERVED]` |
| M4 | Silent-surprised proxy: charged → no activity → month-2 churn | C7 / BLK-04 | `[UNKNOWN]` — R1 builds the join |

## The experiment (M3)

Randomized holdback on the reminder for one cohort. Readout: net revenue at day 60,
reminded vs not — effect size, CI, cohort sizes, or an explicit under-power declaration.
This is the artifact that ends the finance-vs-product argument with a number instead of a
meeting. Gated by BLK-01 (finance co-owns the design — deliberately).

## Claims we cannot measure

| Claim | Decision |
|---|---|
| C6 — bad reviews cost conversions | Not instrumentable honestly (attribution soup). The claim stays [ASSUMED] and OUT of the launch narrative — the case stands on refunds and tickets alone. |
