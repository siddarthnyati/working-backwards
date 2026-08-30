# Telemetry — Silent Step-Down

If the PR claims it, telemetry must measure it — or the claim comes out. Unlike the
ghost-seats session, several baselines here are observable today, because the auth event
log already exists. The chargeback-side baselines are not.

## North star

**Metric:** Silent Step-Down Count (SSC)

**Definition:** Transactions processed without authentication where no recorded policy
decision preceded the fallback, per quarter. Success is zero — not because step-downs end,
but because every one becomes deliberate and visible.

**Measures the claim:** PR ¶1 — "nothing falls through silently."

**Baseline:** ~31,400/quarter, EEA corridor `[OBSERVED: auth event log]` — a floor, not a
total (IFAQ-08).
**Target:** 0 within one quarter of R3 · **Target provenance:** definitional — the silent
path is removed by construction, so the metric verifies the construction rather than hopes.

## Input metrics

| # | Metric | Measures PR claim | Baseline | Instrumentation point |
|---|---|---|---|---|
| M1 | Auth timeout rate (timeouts / auth requests) | PR ¶2 | `[OBSERVED]` — computable from existing log | exists |
| M2 | Auth latency p95, per provider endpoint | PR ¶2 | `[OBSERVED]` | exists |
| M3 | Step-down visibility lag (event → merchant-visible) | PR ¶3 "the same day" | n/a — field doesn't exist; target < 24h | new: reporting pipeline |
| M4 | Policy adoption (merchants on non-default policy) | PR ¶5 | 0 by definition | new: settings service |
| M5 | Blocked-attempt conversion cost (failed payments under Block) | EFAQ-04 | `[UNKNOWN]` until R3 | new: decline-reason counter |
| M6 | Chargeback rate, stepped-down vs authenticated | PR ¶2 `[ASSUMED]` claim C5 | `[UNKNOWN]` — gated by BLK-05 join | new: chargeback join |

## Claims we cannot currently measure

| PR claim | Why | Decision |
|---|---|---|
| ¶2 — stepped-down transactions carry more fraud | No chargeback join exists (BLK-05) | Keep the `[NEEDS EVIDENCE]` placeholder in the PR; M6 resolves it or the claim comes out before launch copy is written |
| ¶6 quote — "we were eating those chargebacks" | Same join | Same decision — the quote is illustrative and labelled, but launch copy must not assert it as measured |

## Questions raised

- → Q-15 · Is 3 seconds the right timeout at all? M2 tells us where the provider actually
  sits; the budget decision needs an owner. · Ask: platform engineering lead + partnerships
- → Q-04 · (carried) fraud differential — resolves via M6 after BLK-05.
