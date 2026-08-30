# Questions — Silent Step-Down

The deliverable: the interrogation list for the six people who hold the context.

**15 open · 1 with no owner assigned.**

| ID | Stage | Question | Ask | Status |
|---|---|---|---|---|
| Q-01 | 1 | Must-be-true: is the timeout observable per-path so the outcome can be recorded before any retry? | platform engineering lead | OPEN |
| Q-02 | 1 | Must-be-true: will payment-ops leads read a daily digest, or does this need to land in their existing tooling? | **no owner identified** | OPEN |
| Q-03 | 1 | Must-be-true: is induced timeout actually exploitable (C8)? | fraud / security lead | OPEN |
| Q-04 | 2, 6 | Do stepped-down transactions carry more fraud (C5)? | fraud analytics lead | OPEN |
| Q-05 | 0 | Can historical step-downs be matched to chargebacks (C7)? | data platform lead | OPEN |
| Q-06 | 2 | Does the launch framing constitute an admission? | legal counsel | OPEN |
| Q-07 | 2, 3 | Does the distinct decline reason survive acquirer response-code mapping? | platform engineering lead | OPEN |
| Q-08 | 2 | Who helps merchants price block-vs-allow? | commercial lead | OPEN |
| Q-09 | 2 | Is 31,400/quarter the total or the observable floor? | platform engineering lead | OPEN |
| Q-10 | 2 | What does support say about historical cost on day one? | support lead | OPEN |
| Q-11 | 2 | Which exemption, if any, applies going forward? | compliance lead | OPEN |
| Q-12 | 2 | Do any markets prohibit step-down outright? | compliance lead | OPEN |
| Q-13 | 2 | Residency constraints on the new outcome records? | privacy counsel | OPEN |
| Q-14 | 3 | Digest recipient: configured contact or account owner? | merchant-experience lead | OPEN |
| Q-15 | 5 | Is 3 seconds the right timeout — and who owns the budget? | platform + partnerships (BLK-04 first) | OPEN |

## From the critic — dimension 4 (strategic fit)

```
Q-16 · The rationale in ¶7 is merchant trust ("deserves to know"). Is trust the frame the
       company would fund this under, versus the defensive frame (regulatory and
       restitution exposure)? The two imply different sequencing: trust ships R2 first and
       loudly; defence ships R4 first and quietly.
Raised by: dimension 4 at Stage 1
Ask: your VP
Why it isn't evaluable here: no strategy document. I can see a rationale is stated; which
  frame the company operates under is not knowable from the artifact.
Affects: launch comms, slice ordering
Status: OPEN
```

## The unowned question

**Q-02** — whether a daily digest gets read is a merchant-behaviour question. Support hears
complaints, merchant-experience designs surfaces, commercial owns relationships; none of
them owns "do ops leads act on what we send them." An ownership map would name a research
function. Tier 0 cannot. It sits under PR ¶3's central promise ("the merchant sees it the
same day") and is flagged in the readiness doc.
