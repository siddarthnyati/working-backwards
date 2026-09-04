# Demo spec — The Surprise Charge

Three surfaces, one rule: the user always knows what happens next.

## Screen 1 · The reminder email (T-48h before first charge)

Subject: "Your trial ends Thursday — keep it or cancel in one tap."
Body: price, charge date, two equal buttons: **Keep my plan** · **Cancel now** (one tap,
done, confirmation inline). No guilt copy, no "we'll miss you."

## Screen 2 · The in-app banner (day 12 onward)

"Trial ends in 2 days — you'll be charged $12 on Apr 3." Same two buttons. The banner is
the backstop for the unopened email (F1). Dismissible; returns daily until decided.

## Screen 3 · One-tap cancel + the receipt

Cancel: one screen, one tap, immediate confirmation, data kept 30 days for easy return.
Receipt (every charge): amount, **next renewal date and price**, and a cancel link.

## Failure states

| # | What fails | What the user sees | Source |
|---|---|---|---|
| F1 | Reminder email unopened or bounced | The in-app banner is the backstop; receipt still carries next-renewal | PR ¶3 |
| F2 | Charge fails at renewal | Plain retry notice with date — same no-surprise rule applies to dunning | PR ¶5 |
| F3 | User cancels, wants back | Resubscribe restores everything within 30 days | PR ¶5 |
| F4 | A market requires a different cancel method | Per-market flow, still never more steps than signup | RFAQ-02 |
| F5 | Reminder send fails upstream | The charge is NOT suppressed silently; the miss is logged and visible in ops (never pretend it sent) | IFAQ-02 |

## What this deliberately does not show

No win-back discounts in the cancel flow (that's a retention program, and nothing upstream
asks for it). No proactive refunds for past charges — BLK-03 owns that question. No
reminder for renewals beyond the first (scoped to the forgot-cohort's moment of harm).

## Open questions surfaced

- → Q-06 · (carried) per-market cancel method rules · Ask: compliance lead
- → Q-07 · Does the banner cannibalise the email's measured effect (attribution)? · Ask: analytics lead
