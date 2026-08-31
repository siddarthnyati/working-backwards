# Intake — Empty Workspace

Session: `empty-workspace` · Mode: `full` · Date: 2026-08-30

> **Fictional worked example.** An invented team-collaboration SaaS; no real company or
> dataset. This is the run that drives the site's walkthrough — chosen because the problem
> and its artifacts are UI-shaped, so every stage has something you can see.

## Trigger

Product analytics on new-workspace cohorts: **61% of new workspaces never gain a second
member within 14 days** `[OBSERVED: product analytics, six-month signup cohort]`.
Single-member workspaces churn at **5.4× the rate** of workspaces with three or more members
by day 30 `[OBSERVED: retention cohort analysis]`.

The invite screen sits three clicks deep in workspace settings `[OBSERVED: current IA]`.
Nothing measures how many people *try* to invite and give up — invite attempts are not
instrumented `[UNKNOWN]`.

## Customer

**Segment:** team leads at 5–50-person companies who create a workspace self-serve,
intending to bring their team — not solo users, not enterprise rollouts with an admin
doing provisioning.

**List-of-ten test:** query signups where company-size field is 5–50 AND the workspace name
contains a company or team name AND the creator's role field is lead/manager. All three
fields exist at signup. `[OBSERVED]`

**Not this product's customer:** deliberate solo users (a solo workspace is a valid
outcome, not a failure), and enterprise-provisioned seats (they never see first-run).

## Evidence

| # | Claim | Tag | Source |
|---|---|---|---|
| C1 | 61% of new workspaces never gain a second member in 14 days | `[OBSERVED]` | product analytics, 6-month cohort |
| C2 | Single-member workspaces churn 5.4× by day 30 | `[OBSERVED]` | retention cohorts |
| C3 | The invite screen is three clicks deep in settings | `[OBSERVED]` | current IA |
| C4 | New users say the workspace "felt empty / didn't know where to start" | `[REPORTED]` | CS lead, onboarding NPS verbatims |
| C5 | Getting a teammate in *causes* retention (not just correlates) | `[ASSUMED]` | — the 5.4× is correlation; teams that were going to stick may simply invite more |
| C6 | Invite emails will actually reach inboxes at current deliverability | `[ASSUMED]` | — no bounce/complaint data reviewed |
| C7 | How many users attempt an invite and fail or abandon | `[UNKNOWN]` | not instrumented → Q-03 |
| C8 | Whether signup volume gives an invite-experiment enough statistical power | `[UNKNOWN]` | → Q-05 |

C5 is the load-bearing assumption of the whole initiative: if teammates don't cause
retention, this is a vanity funnel. It is tagged at the door and tracked to Stage 6.

## Constraint

None external. Growth wants it this quarter `[REPORTED: growth lead]` — a preference, not
a mandate.

## Who must agree

VP Product · growth lead (both claim the onboarding surface — see BLK-03) · privacy counsel
(contact import) · compliance (invite email rules) · security (OAuth scopes) · data lead
(experiment design).

## Context tier

**Tier:** `0 · none` — `wb/context/` absent.
**Therefore not evaluable:** dimension 4 (strategic fit) and dimension 6 (falsifiability)
degrade to questions; the growth-vs-product ownership question routes to the VP without an
ownership map to cite.

## Mode selection

**Mode:** Full (0–8). New first-run surface, two teams claiming it, one load-bearing causal
assumption, live privacy/regulatory edges on contact import. **Stages skipped:** none.
