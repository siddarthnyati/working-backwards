# Demo spec — Empty Workspace

An alignment device. This one is genuinely visual — three screens carry the whole feature.

## Screen 1 · First-run, step 2 of 3: "Who do you work with?"

- Email chip input, autofocused. Typing shows a chip per address; role defaults to member.
- Primary action: **Send invites & continue**. Secondary, equally visible: **Skip for now**
  — one click, no confirmation dialog, no guilt copy.
- An **Import from contacts** button is present but disabled, with a tooltip:
  "Coming soon — pending privacy review." The button ships disabled deliberately: it makes
  the roadmap visible without shipping the risk (BLK-01).
- Nothing on this screen gates anything. Source: PR ¶1 / PR ¶3 / EFAQ-02.

## Screen 2 · The empty state, replaced

Before: blank canvas + "Create your first document."
After: a template gallery —

| Card | Contents on open |
|---|---|
| Project tracker | Pre-populated board: 3 example tasks, owner column, due column |
| Team wiki | Home page with headings and a "how we work" stub |
| Meeting notes | Dated page + recurring template |
| Start empty | The old blank canvas — always last, never removed |

One click opens a working page. Source: PR ¶5 / EFAQ-04.

## Screen 3 · Invite composer, from anywhere

Sidebar button → same composer as first-run. Shows invite status per person:
sent · opened · joined · bounced. Source: PR ¶3.

## Failure states

| # | What fails | What the user sees | Source |
|---|---|---|---|
| F1 | Invite email bounces | Status chip "bounced — check address," visible in composer, not buried in email logs | PR ¶3 |
| F2 | Invitee already has an account elsewhere | They join this workspace with their existing login; inviter sees "joined" | PR ¶3 |
| F3 | Template fails to load | Fall back to blank canvas with a retry — never a dead first screen | EFAQ-04 |
| F4 | User skips invite step | No re-prompt on a schedule; composer stays one click away in the sidebar | EFAQ-02 |
| F5 | Send fails server-side | Composer says so and keeps the chips; a silent drop here recreates the original invisibility | PR ¶4 |

## What this deliberately does not show

No contact import (BLK-01, BLK-02, BLK-06 — the disabled button is the honest version).
No invite incentives (BLK-05). No re-engagement emails to the inviter — that is a
retention campaign, not onboarding, and nothing upstream asks for it.

## Open questions surfaced

- → Q-07 · Does "Skip for now" copy affect skip rate? Wording is testable but only after
  R1 instruments the funnel. · Ask: growth lead (pending BLK-03 ownership)
- → Q-08 · Template languages (carried from RFAQ-03).
