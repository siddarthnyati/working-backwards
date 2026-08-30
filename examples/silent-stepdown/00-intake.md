# Intake — Silent Step-Down

Session: `silent-stepdown` · Mode: `full` · Date: 2026-08-30

> **Fictional worked example.** An invented card-payments gateway; no real company, scheme
> program, or dataset. This run exists to demonstrate the pipeline on a payments-shaped
> problem, with the exact prompt used at every stage recorded in `RUNBOOK.md`.

## Trigger

Analysis of gateway authentication events found a silent fallback path: when the 3-D Secure
authentication call does not return within the 3-second timeout, the gateway retries the
authorization **without** authentication data and continues as if nothing happened.
`[OBSERVED: gateway auth event log, two-quarter export]`

Roughly 31,400 transactions per quarter follow this path on the European corridor.
`[OBSERVED: same export]` No field in merchant-facing reporting records whether
authentication was completed, attempted, or skipped — so the fallback is invisible to the
merchant. `[OBSERVED: reporting schema]`

On non-authenticated transactions, fraud chargeback liability generally sits with the
merchant rather than the issuer. The merchant is carrying liability they believe they
delegated. `[OBSERVED: scheme liability-shift rules, public]`

## Customer

**Segment:** payment operations leads at mid-market e-commerce merchants processing on this
gateway with 3-D Secure enabled and meaningful European card volume — the population that
(a) turned authentication on deliberately and (b) reconciles chargebacks monthly.

**List-of-ten test:** query merchants with 3DS enabled AND >20% EEA issuer volume AND at
least one fraud chargeback in the last quarter. All three fields exist. `[OBSERVED]`

**Not this product's customer:** merchants without 3DS enabled (they chose no
authentication; nothing is silent about it), and shoppers (they never see any of this).

## Evidence

| # | Claim | Tag | Source |
|---|---|---|---|
| C1 | ~31,400 silent step-downs per quarter, EEA corridor | `[OBSERVED]` | gateway auth event log |
| C2 | No merchant-facing field records authentication outcome | `[OBSERVED]` | reporting schema |
| C3 | The fallback fires on a 3s authentication timeout | `[OBSERVED]` | gateway code path |
| C4 | Merchants discover this only through chargeback disputes, if at all | `[REPORTED]` | two merchant-support leads |
| C5 | Stepped-down transactions carry a higher fraud rate than authenticated ones | `[ASSUMED]` | — plausible, never measured here |
| C6 | The timeouts are caused by the authentication provider's latency, not by the gateway | `[ASSUMED]` | — provider status-page anecdotes, no joined data |
| C7 | Historical step-downs can be matched to the chargebacks they caused | `[UNKNOWN]` | → Q-05 |
| C8 | An attacker could deliberately induce timeouts to route around authentication | `[UNKNOWN]` | → Q-03 |

C5 and C6 are the assumptions that propagate. C5 underlies the restitution question; C6
underlies who pays to fix it. C8 is the one that changes the severity of everything if true.

## Constraint

None external. No regulator letter, no scheme mandate, no deadline. Found in data.

## Who must agree

Legal counsel · compliance lead · fraud/security lead · platform engineering lead ·
partnerships (authentication provider contract) · commercial lead. Six roles, no owner.

## Context tier

**Tier:** `0 · none` — `wb/context/` absent.
**Therefore not evaluable:** dimension 4 (strategic fit) and dimension 6 (falsifiability)
degrade to questions; blocker owners resolve to generic titles; the merchant-agreement and
scheme-program questions route to counsel without clause citations.

## Mode selection

**Mode:** Full (0–8). New capability, six roles, live regulatory surface, two load-bearing
assumptions. **Stages skipped:** none.
