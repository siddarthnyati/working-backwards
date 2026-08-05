# Release decomposition

Read this before Stage 7. Output: `07-release-plan.md` and `jira-import.csv`.

## Vertical slices

A slice `R1…Rn` is **independently shippable** and **independently testable**. Both words
are load-bearing.

*Independently shippable* — it can go to production alone, behind a flag if necessary, and
leave the system in a coherent state. If R2 must ship the same day as R1 or something is
broken in between, they are one slice.

*Independently testable* — there is an observable outcome you can verify without the slices
after it existing. A slice you can only test once the whole feature is done isn't a slice.

**Vertical, not horizontal.** The common failure is slicing by layer: R1 the data model, R2
the API, R3 the UI. Each is shippable in a trivial sense and none delivers anything, so
value lands only at the end and every estimate is a guess until then.

Slice by **narrowing the customer scenario** instead:

| Horizontal (avoid) | Vertical (do this) |
|---|---|
| R1 schema, R2 service, R3 UI | R1 detect failure for one integration and log it |
| | R2 same detection across all integrations |
| | R3 surface the failure to the admin in the audit entry |
| | R4 enumerate historical events |

Each vertical slice touches every layer it needs to and produces something true end to end
for a narrower case. R1 above is genuinely useful alone: you learn the real failure rate.

Useful narrowing axes: one integration instead of all · detect-only before act · internal
visibility before customer-facing · one segment or region before general availability ·
manual trigger before automatic.

## Sequencing rules

1. **Discovery before delivery.** A slice that resolves an `[ASSUMED]` claim or an `UNKNOWN`
   goes before the slices whose shape depends on it. Cheap information first.
2. **Nothing depends on an OPEN blocker.** If a slice contains a requirement with a
   `Depends on: BLK-xx` where BLK-xx is OPEN, it is not schedulable. Put it in the plan,
   mark it `BLOCKED BY BLK-xx`, and do not give it a position in the sequence.
3. **A `SHAPE PENDING` requirement doesn't anchor a slice.** Slice around it.
4. **Prefer the ordering that makes the next decision cheapest**, not the one that shows the
   most progress.

## Slice record

```
R2 · Detection across all connected integrations
Requirements: REQ-D1, REQ-D2
Depends on: R1
Blocked by: —
Ships: propagation confirmation recorded for every integration on every deprovision event;
  no customer-facing change
Independently testable: yes
Test harness:
  - Integration test per connected integration: remove a user, assert a confirmation record
    exists within 60s
  - Fault injection: make one integration time out; assert the event is marked incomplete
    and names that integration
  - Backfill safety: assert no write path touches events predating the flag
Rests on assumption: REQ-D1 — that failures are detectable platform-side without polling
  (Q-06a, unanswered)
```

The test harness field is not decoration. Writing it is how you find out a slice isn't
actually testable alone, which is the main thing that goes wrong in decomposition.

## The dependency DAG

Emit it as text so it survives in a markdown file and a terminal:

```
R1 ──▶ R2 ──▶ R3
        │
        └───▶ R4 [BLOCKED BY BLK-06]
```

Plus an edge list, which is what a tool can read:

```
R1 -> R2
R2 -> R3
R2 -> R4
```

Two properties to check before writing it out:

- **It is acyclic.** A cycle means two slices are really one; merge them.
- **Every requirement appears in exactly one slice.** A requirement in no slice is unplanned
  work; a requirement in two slices means one of them isn't independently shippable. List
  any orphans explicitly rather than quietly dropping them.

## JIRA CSV column mapping

`scripts/export_jira.py` reads `06-requirements.md` and `07-release-plan.md` and writes
`jira-import.csv`. Columns:

| Column | Source | Notes |
|---|---|---|
| `Issue Type` | derived | `Epic` per slice, `Story` per requirement |
| `Summary` | REQ title / slice title | |
| `Description` | Statement + Source + Out of scope | Source line preserved verbatim — traceability has to survive the export or it dies at the import |
| `Acceptance Criteria` | Given/When/Then block | Newline-joined; map to your instance's field |
| `Epic Name` | slice title | Epic rows only |
| `Parent` | slice ID | Story rows only |
| `Labels` | `working-backwards`, `discovery`/`delivery`, `rests-on-assumption` | space-separated within the cell |
| `Priority` | blocker severity of anything it depends on, else `Medium` | |

Import notes worth stating in the plan, because they are where imports actually fail:

- Epic rows must precede their stories in row order.
- `Acceptance Criteria` is a custom field in most instances. If the target instance lacks
  it, the importer maps it into Description — the script does this when
  `--no-ac-field` is passed.
- Commas and newlines inside cells are quoted per RFC 4180. Anything emitting raw newlines
  without quoting will import as truncated rows, which looks like data loss.
- Blocked slices export with the `blocked` label and no sprint assignment. Don't silently
  drop them; a blocked epic in the backlog is the record of why the work stopped.

## Critic dimensions at this stage

5 (traceability) and 8 (template completeness). Dimension 5 here means every slice cites
requirements and every requirement lands in a slice — that reconciliation is the check.
