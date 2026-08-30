# External FAQ — Silent Step-Down

```
EFAQ-01 · Scope · ANSWERED
Q: What does this do, in one sentence?
A: Every transaction now records whether it was authenticated — and when authentication
   can't complete, you decide what happens instead of the gateway deciding silently.
   Source: PR ¶1.
```

```
EFAQ-02 · Reporting · ANSWERED
Q: Where do I see the authentication outcome?
A: A new field on every transaction, in reporting and the API: completed, attempted,
   stepped-down, or not-attempted. Historical backfill is a separate question — see
   EFAQ-07. Source: PR ¶3.
```

```
EFAQ-03 · Adoption · ANSWERED
Q: Do I have to change my integration?
A: No. The field is additive. Policy controls are optional and default to current
   behaviour. Source: PR ¶8.
```

```
EFAQ-04 · Policy · ANSWERED
Q: What happens if I block step-down and authentication times out?
A: The payment fails with a distinct decline reason, visibly. That is the trade you are
   choosing: conversion risk in exchange for guaranteed authentication. The conversion cost
   at current timeout rates is measurable before you switch — ask for your merchant-level
   step-down count. Source: PR ¶5.
```

```
EFAQ-05 · Liability · BLOCKER
Q: I've been eating chargebacks on transactions you stepped down. Do you owe me?
A: The sharpest question a merchant will ask, and not answerable here. It depends on what
   the merchant agreement promised, and on whether historical step-downs can be matched to
   specific chargebacks.
   → BLK-01 · LEGAL · severity high · Owner role: legal counsel · Status: OPEN
   → BLK-05 · DATA · severity high · Owner role: data platform lead · Status: OPEN
```

```
EFAQ-06 · Commercial · OPEN
Q: Will blocking step-down cost me sales?
A: Yes, by definition — some timeouts are legitimate transactions. How much is merchant-
   specific and measurable from your own step-down volume. Who owns helping merchants make
   that trade is open.
   → Q-08 · Ask: commercial lead
```

```
EFAQ-07 · History · OPEN
Q: Can I see which of my past transactions were stepped down?
A: Unknown. Depends whether historical events can be reconstructed — see BLK-05. Forward
   from launch, always. Source: PR ¶3 / EFAQ-05.
```

---

*Tag counts: 4 ANSWERED · 2 OPEN · 1 BLOCKER*
