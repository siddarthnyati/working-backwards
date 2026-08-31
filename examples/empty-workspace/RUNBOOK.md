# Runbook — Empty Workspace

The run that drives the site's walkthrough (siddarthnyati.github.io/working-backwards).
The exact prompt for every stage is rendered on the site itself, stage by stage; the
generic reusable versions live in the skill at `references/stage-prompts.md`.

Shape of this run, against the other two examples:

| | ghost-seats | silent-stepdown | empty-workspace |
|---|---|---|---|
| Domain | B2B SaaS platform defect | payments gateway | SaaS onboarding (UI-heavy) |
| Stage 1 critic | PASS + substantive question changed the doc anyway | REVISE, dim 3 (no alternative named) | REVISE, dim 2 (untagged causal claim) |
| Override | 1 (Stage 5, honest) | 0 | 0 |
| Signature mechanism | scope-creep catch (REQ-DP9) | slice-reconciliation catch | [ASSUMED] tag surviving intake → PR → experiment requirement → readiness |
| Schedulable at readiness | R1, R2 | R1, R2 | R1 only — and the blocked slices name their meetings |

Verify traceability any time:

```
python plugins/working-backwards/skills/working-backwards/scripts/verify_sources.py examples/empty-workspace
```
