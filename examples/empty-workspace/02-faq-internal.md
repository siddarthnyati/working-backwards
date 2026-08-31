# Internal FAQ — Empty Workspace

Hostile versions, in the voice of the leader who would ask. Four blockers surfaced here.

## Product / Growth

```
IFAQ-01 · Ownership · BLOCKER
Q: Growth runs first-run experiments; product owns onboarding surfaces. Both roadmaps
   claim this quarter's activation work. Who owns the invite step — and who owns the
   number it moves?
A: No clear answer, which is itself the answer — the last two onboarding changes shipped
   twice, once per team, and conflicted. This initiative needs a single owner before R2.
   → BLK-03 · DEPENDENCY · severity high · Owner role: VP Product · Status: OPEN
```

```
IFAQ-02 · The causal claim · BLOCKER
Q: The 5.4× retention gap is a correlation. Teams that were always going to stick around
   invite more. If we ship all of this and activation moves but retention doesn't, what
   did we spend the quarter on?
A: Exactly the right question and the reason REQ-D3 exists: a holdback experiment ships
   WITH the feature, not after it. Whether current signup volume gives the experiment
   enough power is unknown.
   → BLK-04 · DATA · severity high · Owner role: data & analytics lead · Status: OPEN
```

## Privacy

```
IFAQ-03 · Contact import · BLOCKER
Q: Importing a user's address book means holding personal data of people who never signed
   up for anything. What is our lawful basis, how long do we keep non-user contacts, and
   can we honour a deletion request from someone who was never our user?
A: Not evaluable here. This gates REQ-DP3 entirely — the import button ships disabled
   until counsel answers.
   → BLK-01 · PRIVACY · severity high · Owner role: privacy counsel · Status: OPEN
```

## Security

```
IFAQ-04 · OAuth scope · OPEN → BLOCKER
Q: Contact import means requesting address-book scopes and storing the tokens. What does
   an attacker get if that store is compromised — and are we widening scope for a feature
   whose value is unproven (see IFAQ-02)?
A: Not evaluable here; the scope request is real attack-surface expansion resting on an
   [ASSUMED] value claim. Security review before any token is stored.
   → BLK-06 · SECURITY · severity medium · Owner role: security lead · Status: OPEN
```

## Commercial

```
IFAQ-05 · Incentives · BLOCKER
Q: If we pay for invites — seats, discounts — what stops incentive-farming, and does a
   discount for behaviour that correlated with retention anyway just give margin away?
A: Not evaluable here, and it depends on IFAQ-02's answer: paying for a behaviour you
   haven't shown to be causal is paying for a metric.
   → BLK-05 · COMMERCIAL · severity medium · Owner role: commercial lead · Status: OPEN
```

## Engineering / Ops

```
IFAQ-06 · Deliverability · OPEN
Q: Invite emails only work if they arrive. What is our current bounce and spam-complaint
   rate, and does a spike in invite volume put our sending domain at risk?
A: Unknown — C6 is assumed. The email vendor relationship and domain reputation need a
   look before R3 scales send volume.
   → Q-06 · Ask: platform engineering lead
```

```
IFAQ-07 · Measurement · OPEN
Q: Do we even know today how many people try to invite and fail?
A: No. Invite attempts are not instrumented (C7). This is why R1 ships first and dark —
   the funnel gets measured before the funnel gets moved.
   → Q-03 · Ask: data & analytics lead
```

---

*Tag counts: 3 OPEN · 4 BLOCKER · 0 ANSWERED — tier-0 run.*
*Blockers raised here: BLK-01, BLK-03, BLK-04, BLK-05, BLK-06*
