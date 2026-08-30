# Internal FAQ — Silent Step-Down

Hostile versions, in the voice of the leader who would ask. Four of six blockers surfaced
here.

## Legal

```
IFAQ-01 · Legal · BLOCKER
Q: Our merchant agreements say we provide 3-D Secure authentication. If we skipped it
   silently, have we been in breach — and do merchants who lost chargeback disputes on
   stepped-down transactions have a restitution claim?
A: Not evaluable here; the agreements are not in this session. The exposure predates the
   fix and is not repaired by shipping it. Flagging the second-order version too: our own
   reporting is the evidence a merchant's lawyer would request.
   → BLK-01 · LEGAL · severity high · Owner role: legal counsel · Status: OPEN
```

```
IFAQ-02 · Legal/GTM · OPEN
Q: Does launching "authentication you can hold us to" admit the prior state was
   indefensible?
A: A determination for counsel. The launch copy cannot be written until it lands.
   → Q-06 · Ask: legal counsel
```

## Security and fraud

```
IFAQ-03 · Fraud · BLOCKER
Q: If a timeout triggers an unauthenticated retry, can an attacker deliberately induce
   timeouts — degrade the authentication endpoint, or time requests to its known slow
   windows — and route fraud around 3DS at will?
A: Unknown, and it is the question that changes the severity of everything. If the fallback
   is farmable, this is not a transparency gap; it is an open bypass. C8 in the intake.
   → BLK-03 · SECURITY · severity high · Owner role: fraud / security lead · Status: OPEN
```

```
IFAQ-04 · Fraud · OPEN
Q: Do stepped-down transactions actually carry more fraud, or are we assuming it?
A: Assumed (C5). Measurable only after the chargeback join exists — BLK-05 gates it.
   → Q-04 · Ask: fraud analytics lead
```

## Engineering and platform

```
IFAQ-05 · Engineering · BLOCKER
Q: The 3-second timeout budget — who owns it? Our contract with the authentication
   provider: does it commit them to a latency SLA, and are they inside it?
A: Unknown. If the provider is contractually inside their SLA, the timeouts are our budget
   being too tight; if there is no SLA, we built a liability-shifting fallback on top of an
   unbounded dependency. Different fixes, different payers (C6 is assumed, not known).
   → BLK-04 · DEPENDENCY · severity high · Owner role: partnerships lead + platform
     engineering lead · Status: OPEN
```

```
IFAQ-06 · Engineering · OPEN
Q: When we block step-down and fail the payment, is the decline distinguishable from an
   ordinary decline — for the merchant AND the shopper's bank?
A: Design constraint for Stage 3. A blocked step-down that reads as a generic decline will
   be retried blindly by merchant retry logic, which recreates the timeout load.
   → Q-07 · Ask: platform engineering lead
```

## Data

```
IFAQ-07 · Data · BLOCKER
Q: Can we enumerate historical step-downs and join them to the chargebacks they produced —
   or does log retention already foreclose restitution?
A: Unknown. Auth event logs retain 13 months [OBSERVED: log config]; chargeback records
   longer. Whether the join keys survive is not known. Every restitution and measurement
   question sits behind this.
   → BLK-05 · DATA · severity high · Owner role: data platform lead · Status: OPEN
```

```
IFAQ-08 · Data · OPEN
Q: Is the 31,400/quarter figure the whole problem, or the observable part?
A: The export counts step-downs the log recorded. A fallback path that predates the current
   logging would not appear. Treat 31,400 as a floor. → Q-09 · Ask: platform engineering lead
```

## Commercial

```
IFAQ-09 · Commercial · BLOCKER
Q: If merchants block step-down, our authorization rate drops. Whose number is that, and
   are we prepared for merchants to choose liability over conversion at scale?
A: The honest tension in the whole initiative: the silent fallback exists because it
   protects a metric we report. Making it visible and optional means some merchants will
   choose the other side of the trade. Someone owns pricing that reality.
   → BLK-06 · COMMERCIAL · severity medium · Owner role: commercial lead · Status: OPEN
```

## Operations

```
IFAQ-10 · Support · OPEN
Q: What does merchant support say on day one when a merchant asks "how much did this cost
   me historically"?
A: Nothing to say until BLK-01 and BLK-05 resolve. Support will be asked in week one.
   → Q-10 · Ask: support lead
```

---

*Tag counts: 6 OPEN · 4 BLOCKER · 0 ANSWERED — tier-0 run; the agreements, contracts and
retention configs that would answer these are exactly what a context pack would hold.*

*Blockers raised here: BLK-01, BLK-03, BLK-04, BLK-05, BLK-06*
