# Telemetry — Empty Workspace

If the PR claims it, telemetry must measure it — or the claim comes out. Several baselines
here are already observed; the two that matter most are not, and one of them is the point
of the whole initiative.

## North star

**Metric:** Day-14 Multiplayer Rate (D14MR)

**Definition:** Of workspaces created in the period, the percentage with ≥2 members who
have each taken ≥1 action by day 14. Membership without action is seat inflation, not a
team — the second clause is what keeps this metric honest.

**Measures the claim:** PR ¶1 — "begins with teammates in the room."

**Baseline:** 39% have a second *member*; members-with-action baseline `[UNKNOWN]` until R1
instruments actions-by-member. **Target:** set after one full cohort post-R1 — a target
before the honest baseline would be a number someone gets held to for no reason. → Q-04

## Input metrics

| # | Metric | Measures | Baseline | Exists? |
|---|---|---|---|---|
| M1 | Invite funnel: attempted → sent → accepted → first-action | PR ¶3 "the full invite funnel is measured" | `[UNKNOWN]` — attempts not instrumented (C7) | No — R1 builds it |
| M2 | Invite-screen discovery (% of new workspaces opening composer, week 1) | PR ¶4 "<4% find it" | 4% `[OBSERVED]` | Yes |
| M3 | Skip rate on the first-run invite step | EFAQ-02 (the never-nag rule needs a health check: a 95% skip rate means the step is noise) | n/a — new | No |
| M4 | Template adoption (% of new workspaces opening ≥1 template) | PR ¶5 | n/a — new | No |
| M5 | Bounce + spam-complaint rate on invite sends | C6, IFAQ-06 | `[UNKNOWN]` | Partially — vendor dashboard, unreviewed |
| M6 | **The experiment:** day-30 retention, invite-first cohort vs holdback | PR ¶2's `[ASSUMED]` causal claim, PR ¶7 "ships with its own experiment" | 5.4× correlational gap `[OBSERVED]` | No — REQ-D3, gated by BLK-04 power question |

## Claims we cannot currently measure

| PR claim | Why | Decision |
|---|---|---|
| ¶2 — teammates *cause* retention | Correlation observed; causation needs M6's holdback | The claim stays tagged [ASSUMED] in the PR until M6 reads out. Launch copy may cite the 5.4× as correlation only. |
| ¶6 quote — "we were back in the old tool by Friday" | Illustrative construction; churn *reasons* are not instrumented | Labelled, stays labelled |

## Questions raised

- → Q-04 · What is the D14MR target, and who signs it off? · Ask: VP Product (after BLK-03)
- → Q-05 · Does signup volume power a holdback experiment in one quarter? · Ask: data lead (BLK-04)
