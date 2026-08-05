# Blockers — Ghost Seats

Every entry is a question with an owner role, never a finding. `Status` is changed only by
the user, and nothing in this session changed one — all six are `OPEN` because the skill has
no path by which it resolves its own question.

Six blockers, surfaced by the FAQ stage, before a single requirement was written.

| ID | Category | Sev | Ask (short) | Owner role | Blocks | Status |
|---|---|---|---|---|---|---|
| BLK-01 | SECURITY | high | Real exposure window per integration, not 90 days inherited from two | security lead | REQ-D5, R4 | OPEN |
| BLK-02 | PRIVACY | high | Is retained access after revocation a reportable processor failure | privacy counsel / DPO | REQ-DP5, R4 | OPEN |
| BLK-03 | LEGAL | high | What do our DPAs commit us to, and what is owed for occurrences already past | legal counsel | REQ-DP5, R4 | OPEN |
| BLK-04 | REGULATORY | high | Have we been attesting to a SOC 2 control that does not operate as described | compliance lead | — (no requirement; changes severity and disclosure) | OPEN |
| BLK-05 | DEPENDENCY | high | Who owns the integration contract, and which integrations expose a membership read | platform engineering lead + partnerships lead | REQ-D3, REQ-DP9, R3 | OPEN |
| BLK-06 | DATA | high | Can the affected population be enumerated retroactively, or only forward | platform engineering lead | REQ-D6, REQ-DP5, R4 | OPEN |

All six are high severity. That is unusual and it is not inflation — each one either blocks a
release slice or changes what is owed to customers, which is the definition the taxonomy
uses. BLK-04 blocks no requirement and is still high, because it changes the readiness
recommendation and the disclosure position.

---

```
BLK-01 · SECURITY · severity: high
Surfaced by: IFAQ-07
Ask: What is the actual interval between a failed propagation and the loss of cached read
     access, for each connected integration — and is 90 days a ceiling or just the number we
     found on the two we examined?
Owner role: security lead
Blocks: REQ-D5, R4
Status: OPEN
```

```
BLK-02 · PRIVACY · severity: high
Surfaced by: RFAQ-01, RFAQ-02
Ask: When a controller instructs removal and we do not propagate it to a sub-processor, does
     the retained read access constitute a failure of our processor obligations — is it
     reportable, on what clock, and by whom?
Owner role: privacy counsel / DPO
Blocks: REQ-DP5, R4
Status: OPEN
```

```
BLK-03 · LEGAL · severity: high
Surfaced by: IFAQ-04, IFAQ-06, EFAQ-10
Ask: What do our standard and negotiated DPAs commit us to on revocation timeliness, what is
     our exposure for the occurrences that have already happened, and what are we obliged to
     tell affected customers and on what clock?
Owner role: legal counsel
Blocks: REQ-DP5, R4
Status: OPEN
```

```
BLK-04 · REGULATORY · severity: high
Surfaced by: RFAQ-06
Ask: Our SOC 2 report attests to logical access controls including timely revocation. Does
     the observed behaviour mean the control has not operated as described — and if so, what
     is owed to the auditor and to customers holding that report?
Owner role: compliance lead / SOC 2 control owner
Blocks: — no requirement, but it changes severity across the readiness recommendation and
        the disclosure position in BLK-03
Status: OPEN
```

```
BLK-05 · DEPENDENCY · severity: high
Surfaced by: IFAQ-10, IFAQ-12
Ask: Who is accountable for the integration contract — platform or partnerships — and, per
     integration, does it expose anything from which removal can be confirmed?
Owner role: platform engineering lead and partnerships lead, jointly
Blocks: REQ-D3, REQ-DP9, R3
Status: OPEN
```

```
BLK-06 · DATA · severity: high
Surfaced by: IFAQ-14
Ask: Can the affected population be enumerated retroactively from data we or the integrations
     hold, or only from the instrumentation date forward?
Owner role: platform engineering lead
Blocks: REQ-D6, REQ-DP5, R4
Status: OPEN
```

---

*Two of these — BLK-05 and BLK-06 — were surfaced by the internal FAQ questions the brief's
own guidance flags as the highest-yield ones: "who owns the system this depends on" and "can
we enumerate the affected population retroactively." They are also the two that reshape the
release plan. The FAQ stage paid for itself here.*
