# Requirements — Silent Step-Down

Every requirement cites the artifact above it. One rests on an assumption; two are shape
pending. No unsourced requirements survived to this file — one was pushed upstream at
Stage 6 review instead (see `DECISIONS.md`, Stage 7 note).

## Discovery requirements (D)

```
REQ-D1 · Record an authentication outcome on every transaction
Source: PR ¶3 / IFAQ-07
Provenance: [OBSERVED] × 2
Statement: Every transaction records exactly one authentication outcome — completed, attempted, stepped-down, or not-attempted — with a reason code and timestamp, written before authorization proceeds.
Acceptance criteria:
  GIVEN a transaction whose authentication call exceeds the timeout
  WHEN  the gateway continues processing on any path
  THEN  an outcome of stepped-down with reason auth-timeout is recorded before the authorization is sent
  AND   no code path reaches authorization with no outcome recorded
Out of scope: showing the field to merchants (REQ-DP1)
Depends on: —
```

```
REQ-D2 · Distinguish incident timeouts from suspicious timeout patterns
Source: 03-demo-spec.md F2 / IFAQ-03
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: Step-down events are classifiable as provider-incident (clustered, provider-wide) or pattern-suspicious (concentrated by merchant, card range, or timing), and the classification is recorded.
Acceptance criteria:
  GIVEN a window containing a provider-wide timeout cluster and an unrelated single-merchant timeout series
  WHEN  classification runs
  THEN  the cluster is labelled provider-incident and the series is labelled pattern-suspicious
  AND   pattern-suspicious events are flagged for review, not auto-blocked
Out of scope: acting on the classification (BLK-03 unresolved)
Depends on: REQ-D1, BLK-03
```

```
REQ-D3 · Enumerate historical step-downs and join to chargebacks
Source: EFAQ-05 / IFAQ-07
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: For the retained log window, produce per-merchant step-down counts joined to fraud chargebacks on those transactions.
Acceptance criteria:
  GIVEN the retained auth event log and chargeback records
  WHEN  the join is computed for a merchant and date range
  THEN  the output lists stepped-down transactions and their chargeback outcomes, or states that the range predates retained data
Conditional on: BLK-05 — if join keys do not survive, this becomes counts-only, and REQ-DP6 (restitution input) loses its evidentiary basis
Out of scope: any restitution decision (BLK-01)
Depends on: BLK-05
Status: SHAPE PENDING
```

```
REQ-D4 · Measure the fraud differential on stepped-down transactions
Source: PR ¶2 / IFAQ-04
Provenance: [ASSUMED] × 1 → RESTS ON ASSUMPTION
Statement: Report chargeback rate on stepped-down versus authenticated transactions over a comparable period (metric M6).
Acceptance criteria:
  GIVEN the chargeback join exists for a full quarter
  WHEN  M6 is computed
  THEN  the report states both rates, the population sizes, and the period
  AND   if the differential is not significant, claim C5 is marked refuted in the session record
Out of scope: causal attribution
Depends on: REQ-D3
```

## Delivery requirements (DP)

```
REQ-DP1 · Expose the authentication outcome to merchants
Source: PR ¶3 / EFAQ-02
Provenance: [OBSERVED] × 2
Statement: The authentication outcome, reason, and timestamp appear on the transaction record in reporting and the API for every transaction from launch.
Acceptance criteria:
  GIVEN a transaction with outcome stepped-down
  WHEN  the merchant retrieves it via reporting or API
  THEN  the outcome, reason and timestamp are present and match the recorded event
Out of scope: historical backfill (REQ-D3)
Depends on: REQ-D1
```

```
REQ-DP2 · Same-day step-down digest
Source: PR ¶3 / 03-demo-spec.md F2
Provenance: [OBSERVED] × 1
Statement: Merchants with at least one step-down in a day receive a digest within 24 hours, with provider incidents grouped into a single line.
Acceptance criteria:
  GIVEN 400 step-downs caused by one provider incident and 3 unrelated ones
  WHEN  the digest is generated
  THEN  it shows one incident line covering the 400 and three individual rows
Out of scope: real-time webhooks; alert thresholds
Depends on: REQ-D1, REQ-D2
```

```
REQ-DP3 · Merchant step-down policy
Source: PR ¶5 / EFAQ-04
Provenance: [OBSERVED] × 1
Statement: Merchants can set on-timeout policy to allow or block; the gateway consults it before any unauthenticated retry on every path; default is allow.
Acceptance criteria:
  GIVEN a merchant with policy block
  WHEN  an authentication call times out
  THEN  the payment fails with decline reason authentication-unavailable and outcome attempted
  AND   with policy allow, the transaction proceeds and records stepped-down
Out of scope: the require-exemption option (REQ-DP4)
Depends on: REQ-D1
```

```
REQ-DP4 · Exemption-flagged step-down for EEA transactions
Source: RFAQ-02 / PR ¶5
Provenance: [OBSERVED] × 1, [UNKNOWN] × 1
Statement: Where a compliance determination permits it, stepped-down EEA transactions carry the determined exemption flag.
Conditional on: BLK-02 — which exemption, whether any applies, and whether the option exists at all are compliance determinations not made here
Acceptance criteria:
  GIVEN the compliance determination names an applicable exemption
  WHEN  a step-down occurs on an in-scope transaction under policy require-exemption
  THEN  the transaction carries that exemption flag and records it in the outcome reason
Out of scope: jurisdictions where step-down is not offerable (Q-12)
Depends on: BLK-02, REQ-DP3
Status: SHAPE PENDING
```

```
REQ-DP5 · Never a silent path
Source: PR ¶1 / 03-demo-spec.md F4
Provenance: [OBSERVED] × 1
Statement: No code path processes a transaction unauthenticated without a recorded outcome and a policy consultation; failure of the policy service itself records policy-unavailable.
Acceptance criteria:
  GIVEN the policy service is unreachable
  WHEN  an authentication call times out
  THEN  the transaction records stepped-down with reason policy-unavailable
  AND   a code-path audit shows no branch reaching authorization without a recorded outcome
Out of scope: changing the default policy under failure
Depends on: REQ-D1, REQ-DP3
```

---

## Flagged

**Rests on assumption**

| REQ | Assumed claim | Question | Owner role |
|---|---|---|---|
| REQ-D4 | C5 — stepped-down transactions carry more fraud | Q-04 | fraud analytics lead |

**Shape pending**

| REQ | Blocked by | The fork |
|---|---|---|
| REQ-D3 | BLK-05 | Join survives → restitution input exists. Doesn't → counts only, and BLK-01 is argued without evidence |
| REQ-DP4 | BLK-02 | Exemption exists → third policy option ships. Doesn't → the option is removed from PR ¶5 and settings |

## Out of scope — candidates

- **Restitution mechanism** (credit memos for historical chargebacks) — wanted by EFAQ-05,
  but it is a legal decision with a data dependency, not a requirement. Becomes one only if
  BLK-01 resolves toward restitution. Cited: EFAQ-05 / BLK-01.
- **Auto-blocking pattern-suspicious traffic** — wanted the moment F5 exists; withheld
  until BLK-03 says the pattern is real (REQ-D2 flags only, on purpose).

---

*9 requirements · 4 discovery · 5 delivery · 0 unsourced · 1 resting on assumption · 2
shape pending*
