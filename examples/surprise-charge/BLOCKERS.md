# Blockers — The Surprise Charge

| ID | Category | Sev | Ask (short) | Owner role | Blocks | Status |
|---|---|---|---|---|---|---|
| BLK-01 | COMMERCIAL | high | What does the reminder cost in conversions — co-design the experiment | finance lead | REQ-D2, R3 | OPEN |
| BLK-02 | REGULATORY | high | Where is the reminder already an obligation; what cancel methods are prescribed | compliance lead | REQ-DP3, R4 | OPEN |
| BLK-03 | LEGAL | high | Past surprise charges: exposure, and does the launch framing admit fault | legal counsel | launch comms, EFAQ-04 | OPEN |
| BLK-04 | DATA | medium | Size the silent-surprised population (C7) | analytics lead | M4 interpretation | OPEN |
| BLK-05 | DEPENDENCY | medium | Who owns the send-before-charge ordering across two vendors | platform engineering lead | REQ-DP1, R3 | OPEN |

---

```
BLK-01 · COMMERCIAL · severity: high
Surfaced by: IFAQ-01
Ask: Finance believes reminders reduce trial→paid conversion; product believes they don't.
     Neither has data. Will finance co-design the holdback experiment so the readout is
     binding on both sides?
Owner role: finance lead
Blocks: REQ-D2, R3
Status: OPEN
```

```
BLK-02 · REGULATORY · severity: high
Surfaced by: RFAQ-01, RFAQ-02
Ask: In which of our markets do auto-renewal notice or click-to-cancel style rules
     (public categories) already require what we're designing — and which prescribe the
     cancellation method?
Owner role: compliance lead
Blocks: REQ-DP3, R4 — and possibly the timeline, everywhere the answer is "already required"
Status: OPEN
```

```
BLK-03 · LEGAL · severity: high
Surfaced by: IFAQ-04, EFAQ-04
Ask: For charges already taken from users who forgot: is there exposure, do we owe
     proactive refunds, and does "the trial that ends politely" framing admit prior fault?
Owner role: legal counsel
Blocks: launch communications, the EFAQ-04 answer
Status: OPEN
```

```
BLK-04 · DATA · severity: medium
Surfaced by: IFAQ-03
Ask: How many charged users are surprised but silent — no refund, no ticket, churn at
     month 2 (C7)? The refunders are only the ones angry enough to act.
Owner role: analytics lead
Blocks: interpreting M4; the true size of the problem
Status: OPEN
```

```
BLK-05 · DEPENDENCY · severity: medium
Surfaced by: IFAQ-02
Ask: The reminder must provably precede the charge across a billing vendor and an email
     queue that don't know about each other. Who owns that ordering guarantee?
Owner role: platform engineering lead
Blocks: REQ-DP1, R3
Status: OPEN
```
