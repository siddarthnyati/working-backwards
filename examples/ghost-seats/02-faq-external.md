# External FAQ — Ghost Seats

What press, customers, and prospects ask. Answers you would put on a website.
Pruned to what this initiative actually raises.

## Product and scope

```
EFAQ-01 · Scope · ANSWERED
Q: What does Ghost Seats do, in one sentence?
A: When you remove someone from your workspace, we confirm that every connected integration
   has dropped their access — and tell you which one didn't if any didn't. Source: PR ¶1.
```

```
EFAQ-02 · Scope · ANSWERED
Q: What does it not do that people will assume it does?
A: It does not force the removal through. If an integration doesn't confirm, we tell you;
   we do not retry indefinitely or reach into the integration to revoke on your behalf.
   Remediation is still yours. This boundary is deliberate and it is the one most likely to
   disappoint — see 03-demo-spec.md, "what this deliberately does not show."
```

```
EFAQ-03 · Scope · OPEN
Q: Does this cover integrations I built myself against your API?
A: Not evaluable here. It depends whether a custom integration exposes anything the platform
   can read a confirmation from, which is the same question as IFAQ-12.
   → Q-05
```

## Adoption

```
EFAQ-04 · Adoption · ANSWERED
Q: What do I have to do to turn it on?
A: Nothing. Confirmation runs on every deprovisioning event from the day it ships. Source: PR ¶7.
```

```
EFAQ-05 · Adoption · ANSWERED
Q: Does this change anything I do today?
A: The audit entry gains a confirmation line per integration and the access-review export
   gains a column. No existing workflow changes. Source: PR ¶3.
```

```
EFAQ-06 · Adoption · OPEN
Q: What happens to removals that already happened before this shipped?
A: There is an affected-account report for the historical view, but how far back it can
   reach is not yet known — it depends on whether the integrations retained the data needed
   to reconstruct it. Source: PR ¶7 / IFAQ-14.
   → Q-09
```

## Commercial

```
EFAQ-07 · Commercial · OPEN
Q: What does it cost? Is it included?
A: Not decided. This is a correctness property of a feature customers already pay for, which
   is an argument for including it — but that is a pricing decision, not a technical one.
   → Q-07 · Ask: pricing lead
```

## Trust and operations

```
EFAQ-08 · Trust · ANSWERED
Q: What happens when an integration is slow rather than broken?
A: Confirmations arriving after 60 seconds still land; the event moves from incomplete to
   complete when the confirmation arrives, and the audit entry shows both timestamps. A slow
   integration is visible as latency, not as a failure. Source: PR ¶3 / 03-demo-spec.md F2.
```

```
EFAQ-09 · Trust · ANSWERED
Q: What do you store about the confirmation?
A: The event, the integration, the outcome, and the timestamp. No document content and no
   information about what the removed user accessed. Source: 05-telemetry.md.
```

```
EFAQ-10 · Trust · BLOCKER
Q: Has this been happening to my workspace, and were you going to tell me?
A: This is the question with the sharpest edge and it does not have an answer yet. Whether
   affected customers are notified, on what timeline, and by whom is a determination for
   legal counsel — and it partly depends on whether we can enumerate who was affected at all.
   → BLK-03 · LEGAL · severity high · Owner role: legal counsel · Status: OPEN
   → BLK-06 · DATA · severity high · Owner role: platform engineering lead · Status: OPEN
```

## Timeline

```
EFAQ-11 · Timeline · OPEN
Q: When is it available?
A: The dated launch in the press release is a working target, not a commitment. Three of the
   six open blockers are high severity and two of them change what ships.
```

---

*Tag counts: 6 ANSWERED · 4 OPEN · 1 BLOCKER*
