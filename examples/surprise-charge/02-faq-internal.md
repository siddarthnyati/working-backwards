# Internal FAQ — The Surprise Charge

Hostile versions. Four blockers surfaced here.

```
IFAQ-01 · Finance · BLOCKER
Q: Some of those "forgot" charges convert into paying customers who stay. If we remind
   everyone, how much revenue are we handing back — and are you asking me to approve a
   number you can't state?
A: Exactly the honest tension: C5 (reminders reduce conversion) is finance's belief, mine
   is the opposite, and neither has data. REQ-D2 is the holdback experiment that settles
   it. Until it reads out, no one states a number.
   → BLK-01 · COMMERCIAL · severity high · Owner role: finance lead · Status: OPEN
```

```
IFAQ-02 · Platform · BLOCKER
Q: The reminder must land BEFORE the charge. Billing runs on a vendor webhook; email has
   its own queue. Who owns the guarantee that T-48h means T-48h?
A: Nobody today — the send-before-charge ordering crosses two vendors and no team owns
   the pair.
   → BLK-05 · DEPENDENCY · severity medium · Owner role: platform engineering lead · Status: OPEN
```

```
IFAQ-03 · Data · BLOCKER
Q: The refunders are the ones angry enough to act. How many charged users are surprised
   and silent — and churn at month 2 with the same fury and no ticket?
A: Unknown (C7), and it decides how big this problem actually is. Measurable from
   charge → no-activity → month-2-churn joins, if we build them.
   → BLK-04 · DATA · severity medium · Owner role: analytics lead · Status: OPEN
```

```
IFAQ-04 · Legal · BLOCKER
Q: If we announce "the trial that ends politely," what does that say about the charges we
   already took from people who forgot — and do auto-renewal rules in some markets already
   require the notice we weren't sending?
A: Both halves route to counsel. The second half changes this from improvement to
   remediation in some markets.
   → BLK-03 · LEGAL · severity high · Owner role: legal counsel · Status: OPEN
   → BLK-02 (regulatory half, raised at RFAQ-01)
```

```
IFAQ-05 · Metrics · OPEN
Q: What stops this becoming an engagement-washing exercise — big open rates, no fewer
   angry customers?
A: The north star counts surprises, not opens. See 05-telemetry.md, and the gate answer
   recorded in DECISIONS.md — the author named open rate as the metric they'd game.
   → Q-05 · Ask: analytics lead
```

---
*1 OPEN · 4 BLOCKER · 0 ANSWERED — tier-0 run*
*Blockers raised here: BLK-01, BLK-03, BLK-04, BLK-05*
