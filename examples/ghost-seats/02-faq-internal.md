# Internal FAQ — Ghost Seats

The risk-discovery stage. Questions are written in the hostile version and in the voice of
the leader who would ask them. Four of the six blockers in this session surfaced here.

Numbering is stable — requirements cite these IDs.

## Finance

```
IFAQ-01 · Finance · OPEN
Q: What does this cost to build, and what does it cost to run per deprovisioning event?
A: Build is not estimable from this document. Run cost is a confirmation round-trip per
   integration per removal, so it scales with removals × integrations rather than with seats
   — which is a different shape from most of what we bill for, and worth knowing before
   anyone prices it. Volume is not in this session.
   → Q-06 · Ask: platform engineering lead
```

```
IFAQ-02 · Finance · OPEN
Q: What revenue does this protect, and how would we know?
A: The honest answer is that nobody has lost a renewal over this yet, because almost nobody
   knows it is happening `[ASSUMED — C7]`. That makes the revenue case a story about what
   happens when a customer does find out, and the size of that story is not something this
   document can establish.
   → Q-08 · Ask: your VP or the enterprise renewals lead
```

```
IFAQ-03 · Finance · OPEN
Q: What are we not doing instead?
A: Not evaluable here. There is no roadmap in this session.
   → Q-08 (same ask)
```

## Legal

```
IFAQ-04 · Legal · BLOCKER
Q: What do our existing customer DPAs already commit us to on revocation timeliness — and
   have we been in breach of that commitment for as long as this has been happening?
A: Not evaluable here. Our standard DPA is not in this session and the customer-negotiated
   variants certainly aren't. The question matters more than the feature does: if a
   timeliness clause exists, the exposure predates anything we ship and is not fixed by
   shipping.
   → BLK-03 · LEGAL · severity high · Owner role: legal counsel · Status: OPEN
```

```
IFAQ-05 · Legal · OPEN
Q: Does shipping a confirmation mechanism constitute an admission that the previous state
   was defective?
A: A determination for counsel, not for this document. Flagging it because the answer
   changes the launch communication and possibly the launch date, and because it is the
   kind of question that arrives late and expensively if nobody asks it early.
   → Q-11 · Ask: legal counsel
```

```
IFAQ-06 · Legal · BLOCKER
Q: What are we obliged to tell customers who were already affected, and on what clock?
A: Not evaluable here. It depends on BLK-03 (what we promised), on BLK-02 (whether this is
   reportable), and on BLK-06 (whether we can even name the affected customers). Three
   dependencies is why this one is the schedule risk rather than the engineering.
   → BLK-03 · LEGAL · severity high · Owner role: legal counsel · Status: OPEN
```

## Security

```
IFAQ-07 · Security · BLOCKER
Q: What is the actual exposure window — from revocation to loss of access — and is 90 days
   the ceiling or just the number we happened to find?
A: We examined two integrations and both document a 90-day sync-cache retention
   `[OBSERVED]`. We are assuming the rest are the same `[ASSUMED — C6]` and that assumption
   is doing a lot of work: it sizes the entire exposure. It could be shorter. It could be
   unbounded on an integration that caches until eviction.
   → BLK-01 · SECURITY · severity high · Owner role: security lead · Status: OPEN
```

```
IFAQ-08 · Security · OPEN
Q: What access does the confirmation mechanism need that nothing currently has, and what
   does an attacker get if it is compromised?
A: A read on membership state per integration, which is narrower than the write access
   deprovisioning already holds — so this plausibly reduces rather than expands surface.
   "Plausibly" is doing work there and a security lead should confirm it rather than accept
   the reasoning.
   → Q-03 · Ask: security lead
```

## Privacy

```
IFAQ-09 · Privacy · OPEN
Q: Can we honour an erasure request end to end today — and could we before?
A: Almost certainly not, on the same mechanism: if a removal doesn't propagate, an erasure
   instruction has no more reason to. The regional FAQ takes this one because the answer is
   jurisdictional. See RFAQ-01.
   → BLK-02 (raised at RFAQ-01)
```

## Engineering and platform

```
IFAQ-10 · Engineering · BLOCKER
Q: Who owns the integration contract — platform or partnerships? Not who works on it. Who
   is accountable when it changes.
A: The FAQ surfaced no clear answer, which is itself the answer. Platform owns the
   propagation handler. Partnerships owns the commercial relationship. The contract that
   defines what an integration must expose sits between them, and this initiative needs
   somebody to change it.
   → BLK-05 · DEPENDENCY · severity high · Owner role: platform engineering lead and
     partnerships lead, jointly — Status: OPEN
```

```
IFAQ-11 · Engineering · OPEN
Q: What is the failure mode when an integration is unavailable rather than refusing?
A: Unavailable and failed have to be distinguishable or the admin gets an alarm every time
   a partner has an incident, learns to ignore it, and we have built a worse version of
   nothing. This is a design constraint on Stage 3 and it comes from asking the hostile
   version of an ops question.
   → Q-02 · Ask: platform engineering lead
```

```
IFAQ-12 · Engineering · BLOCKER
Q: Does every connected integration actually expose something we can read a confirmation
   from — and what do we do about the ones that don't?
A: Unknown for all but the two examined. If an integration exposes no membership read, the
   press release's central claim is not deliverable for that integration and the honest
   product is "confirmed for these, unverifiable for those," which is a materially different
   thing to announce.
   → BLK-05 · DEPENDENCY · severity high · Owner role: platform engineering lead and
     partnerships lead — Status: OPEN
```

## Operations and support

```
IFAQ-13 · Support · OPEN
Q: What does support tell a customer who calls and asks whether they were affected?
A: There is no answer to give until BLK-06 resolves. Worth stating plainly because support
   will be asked this on day one of the launch, not later.
   → Q-12 · Ask: support lead
```

## Data

```
IFAQ-14 · Data · BLOCKER
Q: Can we enumerate the affected population retroactively, or only going forward?
A: Going forward, yes — a confirmation record can be written from the moment the handler
   emits one. Retroactively is unknown and depends on data held by the integrations, which
   we do not control. This is the single question that most changes the plan: if the answer
   is "going forward only," the affected-account report in PR ¶7 cannot be built as
   described and the customer-notification question loses its input.
   → BLK-06 · DATA · severity high · Owner role: platform engineering lead · Status: OPEN
```

```
IFAQ-15 · Data · OPEN
Q: Do we have a baseline for the north-star metric?
A: No. There is no propagation-confirmation field today, so the current propagation rate is
   not measured — it is inferred from failures we happened to detect. The baseline is
   `[UNKNOWN]` and Stage 5 records it as such rather than estimating it.
   → Q-09 · Ask: platform engineering lead
```

## Go-to-market

```
IFAQ-16 · GTM · OPEN
Q: Does the launch communication say this was broken?
A: It has to say something, and what it says depends on IFAQ-05 and BLK-03. Noting here so
   it does not get discovered in the week of launch.
   → Q-11 (same ask)
```

---

*Tag counts: 10 OPEN · 6 BLOCKER · 0 ANSWERED*

*Zero ANSWERED is unusual and it is real: this session ran with no context pack, so almost
nothing in the internal bank could be answered from the document alone. With a strategy doc,
an ownership map, and a DPA template in `wb/context/`, IFAQ-03, IFAQ-04 and IFAQ-10 would
have been answerable rather than raised.*

*Blockers raised here: BLK-01, BLK-03, BLK-05, BLK-06*
