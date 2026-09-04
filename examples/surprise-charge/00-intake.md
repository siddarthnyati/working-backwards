# Intake — The Surprise Charge

Session: `surprise-charge` · Mode: `full` · Date: 2026-08-31

> **Fictional worked example**, and the first run under the interrogation protocol — the
> challenge log below is the stage's proof of work.

## The problem as first stated (verbatim)

> "We need to send trial-ending reminder emails — people are getting charged without
> realizing and it's killing us in reviews."

## The challenge log — 4 of 6 used

```
CHALLENGE 1 of 6 · costume scan
It pushed: "Reminder emails are the fix. What did you OBSERVE before you concluded it?"
I answered: the refund log — 38% of last quarter's refunds cite "forgot to cancel /
didn't know I'd be charged." And "surprise charge" is the #1 ticket category in week 3
of every cohort.
→ problem restated as an observation, not a feature request.

CHALLENGE 2 of 6 · enumerable customer
It pushed: "'Trial users' is a bare role. Who exactly? Could you name ten?"
I answered: trial users who never opened the app after day 3 AND still got charged on
day 14 — the forgot-cohort. Billing join × activity log; two queryable fields.
→ accepted. Deliberate cancellers and active converters are NOT the customer.

CHALLENGE 3 of 6 · causality scan
It pushed: "You said they refund BECAUSE they feel tricked. The refunds are observed.
The feeling is its own claim."
I answered: fair — reviews say "tricked" [REPORTED: review verbatims], the causal link
stays [ASSUMED].

CHALLENGE 4 of 6 · number hygiene
It pushed: "'Killing us in reviews' — any data connecting reviews to conversion?"
I answered: none. Tagged [ASSUMED] and I'll stop saying it in meetings.

Challenges 5–6: unused. Kill-condition question answered without pushback (below).
```

## Customer

**Segment:** trial users who stopped opening the app by day 3 and were charged at day 14
— the forgot-cohort. **List-of-ten:** billing events joined to last-activity date; both
fields exist. `[OBSERVED]`

**Not the customer:** users who deliberately cancel (working as intended) and active users
who convert (happy path).

## Evidence

| # | Claim | Tag | Source |
|---|---|---|---|
| C1 | 38% of refunds cite "forgot to cancel / didn't know" | `[OBSERVED]` | refund log, last quarter |
| C2 | "Surprise charge" is the #1 ticket category in week 3 of each cohort | `[OBSERVED]` | support ticket tags |
| C3 | 71% of eventual refunders never opened the app after trial day 3 | `[OBSERVED]` | activity × billing join |
| C4 | Refunders' reviews say "tricked" and "scam" | `[REPORTED]` | review verbatims via support lead |
| C5 | Reminding people before the charge will reduce trial→paid conversion | `[ASSUMED]` | — finance's fear; never measured |
| C6 | Bad reviews are hurting conversion | `[ASSUMED]` | — no data connects them |
| C7 | How many charged users are surprised but never refund (the silent-angry) | `[UNKNOWN]` | → Q-03 |

**The kill condition** (asked, answered without challenge): if refunders would have churned
at renewal anyway, reminders only move the churn earlier — and the fury is the only thing
we remove. That would still justify R2 (clarity) but not R3 (the reminder program).

**Declared assumptions:** "I believe reminders won't hurt net revenue. Finance believes the
opposite. Neither of us has data — that disagreement is the actual project."

## Constraint

None hard. Auto-renewal and click-to-cancel rules are tightening in several markets
(public regulatory categories — a tailwind, not a mandate with a date).

## Context tier

**Tier 0** — nothing in `wb/context/`. Dimensions 4 and 6 degrade to questions; the
market-rules questions route to compliance without clause citations.

## Mode

**Full (0–8).** The finance-vs-product disagreement makes this discovery, not a ticket.
