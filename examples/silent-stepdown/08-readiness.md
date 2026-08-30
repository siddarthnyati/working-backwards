# Readiness — Silent Step-Down

```
SESSION CONFIDENCE · silent-stepdown · after Stage 8 · 2026-08-30
Claims:        4 observed · 1 reported · 2 assumed · 2 unknown   (intake C1–C8)
Requirements:  9 total · 1 resting on assumption · 2 shape pending · 0 unsourced
Release:       4 slices · 2 schedulable · 2 not schedulable
Questions:     16 open · 1 with no owner assigned
Blockers:      6 open (5 high · 1 medium · 0 low)
Context pack:  absent — strategic fit and feasibility were not evaluated
```

## Recommendation

**GO WITH CONDITIONS — R1 and R2 only.**

R1 and R2 are unblocked and together deliver ¶3's promise: every transaction records its
authentication outcome and the merchant sees it the same day. R1 also produces the number
every open question needs — the true step-down floor and the latency profile.

R3 is one compliance determination away from two different products (with or without
require-exemption). R4 is one retention answer away from existing or not. Neither should be
estimated yet.

**Separately and urgently:** BLK-03 is not a launch blocker — it is a today question. If
induced timeouts are exploitable, that is a live fraud channel independent of anything this
initiative ships. It should be answered this week regardless of the go/no-go.

## Open blockers by severity

### High
| ID | Ask | Owner role | Blocks |
|---|---|---|---|
| BLK-01 | Breach + restitution exposure for historical step-downs | legal counsel | R4 |
| BLK-02 | SCA position of unauthenticated EEA transactions, no exemption claimed | compliance lead | R3 |
| BLK-03 | Induced-timeout bypass — exploitable? already exploited? | fraud / security lead | REQ-D2, and possibly everything |
| BLK-04 | Provider SLA — who owns the timeout budget | partnerships + platform | timeout design |
| BLK-05 | Do join keys survive retention | data platform lead | R4 |

### Medium
| BLK-06 | Conversion-vs-liability trade ownership at launch | commercial lead | R3 comms |

## Assumptions that must hold

| # | Assumption | What breaks if false | Check |
|---|---|---|---|
| C5 | Stepped-down transactions carry more fraud | The restitution narrative weakens and ¶2's implication comes out of the launch copy; the transparency case stands regardless | M6, after BLK-05 |
| C6 | Timeouts are provider latency, not our budget | If our budget is simply too tight, the cheapest fix is a number change and the provider conversation is unnecessary | M2 percentiles vs contract, after BLK-04 |
| Q-01 | Timeout observable per-path before retry | REQ-D1's "before authorization proceeds" is not implementable as written | platform engineering, one look |
| Q-02 | Ops leads act on a daily digest | R2 ships visibility nobody consumes — the silent failure reproduced one layer up | unowned — assign first |

## Top three reasons this fails

1. **BLK-02 resolves against step-down entirely.** If unauthenticated EEA processing cannot
   be made compliant even flagged, "allow" is not offerable in the largest affected
   corridor, and the product becomes block-by-default — a different launch with a real
   conversion cost. Most likely material outcome, least dramatic.
2. **The digest goes unread (Q-02).** Visibility without behaviour change reproduces the
   original failure with better logging. The unowned question sits under the central
   promise.
3. **BLK-03 turns out bad and late.** If the bypass is exploitable and discovered mid-build,
   everything reprioritises around fraud containment and this plan is shelved half-shipped.

## What would change this recommendation

1. **BLK-03, this week** — fraud/security lead. Independent of the initiative.
2. **BLK-02** — compliance lead. Forks R3 into one of two products.
3. **An owner for Q-02** — smaller than answering it; someone must be accountable for
   whether the digest works.

Three asks. One is urgent regardless of whether this ships.
