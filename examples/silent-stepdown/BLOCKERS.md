# Blockers — Silent Step-Down

Questions with owners, never findings. Status changed only by the user; all six are OPEN.

| ID | Category | Sev | Ask (short) | Owner role | Blocks | Status |
|---|---|---|---|---|---|---|
| BLK-01 | LEGAL | high | Breach + restitution exposure for historical step-downs | legal counsel | REQ-D3, R4 | OPEN |
| BLK-02 | REGULATORY | high | SCA position of an unauthenticated EEA txn with no exemption | compliance lead | REQ-DP4, R3 | OPEN |
| BLK-03 | SECURITY | high | Can induced timeouts farm the step-down as a 3DS bypass | fraud / security lead | REQ-D2 | OPEN |
| BLK-04 | DEPENDENCY | high | Who owns the timeout budget — provider SLA position | partnerships + platform leads | Q-15, timeout design | OPEN |
| BLK-05 | DATA | high | Do join keys survive retention — historical enumeration | data platform lead | REQ-D3, R4 | OPEN |
| BLK-06 | COMMERCIAL | medium | Who owns the conversion-vs-liability trade at launch | commercial lead | R3 comms | OPEN |

---

```
BLK-01 · LEGAL · severity: high
Surfaced by: IFAQ-01, EFAQ-05
Ask: Did our merchant agreements commit us to authenticate when instructed — and do
     merchants who lost fraud chargebacks on silently stepped-down transactions have a
     restitution claim against us?
Owner role: legal counsel
Blocks: REQ-D3, R4
Status: OPEN
```

```
BLK-02 · REGULATORY · severity: high
Surfaced by: RFAQ-01
Ask: An EEA transaction we processed without authentication and without claiming an
     exemption — whose SCA compliance failure is that in the chain, and is it reportable
     to any party?
Owner role: compliance lead
Blocks: REQ-DP4, R3
Status: OPEN
```

```
BLK-03 · SECURITY · severity: high
Surfaced by: IFAQ-03
Ask: Can an attacker deliberately induce authentication timeouts — endpoint degradation,
     timing — and use the step-down as an on-demand 3DS bypass? Has it already happened?
Owner role: fraud / security lead
Blocks: REQ-D2 (acting on classification)
Status: OPEN
```

```
BLK-04 · DEPENDENCY · severity: high
Surfaced by: IFAQ-05
Ask: Does the authentication provider contract carry a latency SLA, are they inside it,
     and who therefore owns the 3-second budget — us or them?
Owner role: partnerships lead + platform engineering lead
Blocks: Q-15 (timeout design), the cost allocation of any fix
Status: OPEN
```

```
BLK-05 · DATA · severity: high
Surfaced by: IFAQ-07, EFAQ-05
Ask: Within the 13-month auth-log retention, do the join keys exist to match historical
     step-downs to specific chargebacks — or is restitution evidentially foreclosed?
Owner role: data platform lead
Blocks: REQ-D3, R4
Status: OPEN
```

```
BLK-06 · COMMERCIAL · severity: medium
Surfaced by: IFAQ-09, EFAQ-06
Ask: When merchants can see and block step-downs, some will choose liability over
     conversion. Who owns that trade — its pricing implications and its merchant
     communication — before R3 makes it real?
Owner role: commercial lead
Blocks: R3 launch comms
Status: OPEN
```

*Five high, one medium — the medium is deliberate: BLK-06 blocks a communication, not a
capability or an obligation. Severity is about what waits, not how alarming it sounds.*
