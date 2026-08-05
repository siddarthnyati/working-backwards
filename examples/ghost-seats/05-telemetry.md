# Telemetry — Ghost Seats

The rule: if the press release claims it, telemetry must be able to measure it — or the
claim comes out of the press release. Baselines we do not have are `[UNKNOWN]`, not
estimates.

Every baseline in this session is `[UNKNOWN]`. That is not an oversight; there is no
propagation-confirmation field today, so the current propagation rate has never been
measured. It has been inferred from the failures we happened to notice. See IFAQ-15.

## North star

**Metric:** Revocation Propagation Rate (RPR)

**Definition:** Of all deprovisioning events in the period, the percentage for which every
connected integration returned a confirmation of removal within 60 seconds of the local
removal event.

Denominator is every deprovisioning event, including those on integrations that cannot be
checked — those count against the rate. A metric that excludes the cases it cannot see is
the same mistake as the audit log.

**Measures the claim:** PR ¶1 / PR ¶3 — "every connected integration confirms the removal
within 60 seconds — or the admin finds out which one didn't."

**Baseline:** `[UNKNOWN]` — not measurable before instrumentation exists.
**Target:** `[UNKNOWN]` — setting a target before the baseline is known would be inventing
a figure, which is the thing this pipeline is most concerned with not doing. → Q-15
**Target provenance:** `[UNKNOWN]`

## Input metrics

| # | Metric | Definition | Measures PR claim | Baseline | Target | Instrumentation point |
|---|---|---|---|---|---|---|
| M1 | Propagation latency p95 | Local removal event → confirmation received, per integration, 95th percentile | PR ¶3 ("within 60 seconds") | `[UNKNOWN]` | `[UNKNOWN]` | Confirmation handler, on receipt |
| M2 | Silent-failure count | Deprovisioning events where at least one integration neither confirmed nor errored inside the window | PR ¶2 ("nothing surfaces when it happens") | `[UNKNOWN]` — the 4,200/quarter figure is a different measurement, derived from log analysis after the fact, not a live count | `[UNKNOWN]` | Confirmation handler, on window expiry |
| M3 | Admin-visible error rate | Removals surfaced to an admin as incomplete, as a share of all removals | PR ¶3 ("the admin finds out which one didn't") | 0 — no error path exists today `[OBSERVED]` | n/a — this should rise, and a target would be meaningless | Audit entry render |
| M4 | Unverifiable share | Removals where at least one integration could not be checked at all | PR ¶3, implicitly | `[UNKNOWN]` | Should fall as BLK-05 resolves | Connection registry + confirmation handler |
| M5 | Time to admin remediation | Incomplete state → the integration subsequently reporting the user removed | PR ¶3, downstream | n/a — no such state exists today | `[UNKNOWN]` | Confirmation handler, on state change |

M3 is worth reading twice. Its baseline is genuinely zero and its success condition is that
it goes up, because today the number is zero for the wrong reason. Any dashboard that colours
this metric red on an increase will be wrong for the first quarter.

M4 exists because of the demo spec. Without it, an integration that cannot be checked would
quietly improve the north star by not appearing in it — the same failure mode, rebuilt in
the metric.

## Instrumentation

| Point | Event | Fields | Owner role | Exists today? |
|---|---|---|---|---|
| Deprovisioning handler | `deprovision.local.completed` | event id, workspace, user, timestamp | platform engineering | Yes |
| Confirmation dispatch | `deprovision.check.sent` | event id, integration, timestamp | platform engineering | No |
| Confirmation receipt | `deprovision.check.result` | event id, integration, outcome, timestamp | platform engineering | No |
| Window expiry | `deprovision.window.closed` | event id, per-integration outcome, overall state | platform engineering | No |
| Audit entry render | `audit.entry.viewed` | event id, state shown | platform engineering | Partially — the entry is rendered; the state field is new |

Four of five instrumentation points do not exist. That is the honest sizing of Stage 5 for
this problem: the telemetry is most of the discovery work, which is why the release plan
leads with it.

## Claims we cannot currently measure

Each row is a decision: instrument it, or cut the claim.

| PR claim | Why unmeasurable | Options |
|---|---|---|
| PR ¶2 — "keeps read access for up to 90 days" | We observe the integrations' documented cache retention, not actual access. Whether a removed user opened anything is not visible to us at all. | Cut the implication of harm, or ask integrations for access logs (a partnerships and privacy question, not an engineering one) → Q-10 |
| PR ¶2 — the `[NEEDS EVIDENCE]` line on how many removed users actually opened a document | Same reason. This is the number the press release most wants and the one we are least able to get. | Leave the placeholder visible. Do not replace it with the 4,200 figure, which counts something else. |
| PR ¶1 — "every enterprise customer … is already relying on that confirmation existing" | This is a claim about customer belief, not system behaviour. No telemetry reaches it. | Route to research or to the renewals lead → Q-08 |

The third row is the rationale added in the revision. It is worth noticing that the sentence
which fixed the strategic-fit question is also the sentence telemetry cannot support — the
critic's question and the measurement rule are pointing at the same soft spot from different
directions.

## Questions raised

- → Q-15 · What is an acceptable propagation rate, and who decides? A target set before the
  baseline exists is a number someone will be held to for no reason. · Ask: platform
  engineering lead and your VP · Not evaluable from the document alone.
- → Q-10 · Can we obtain, or should we want, evidence of what removed users actually
  accessed? · Ask: partnerships lead and privacy counsel · Not evaluable from the document
  alone.
- → Q-09 · Is there any historical data from which a retroactive baseline could be
  computed? · Ask: platform engineering lead · Also BLK-06.
