# Requirements

Format and rules: `references/requirements-format.md`.
Every requirement cites the artifact above it. A requirement with no `Source:` is flagged,
not silently accepted.

## Discovery requirements (D)

```
REQ-D1 · <title>
Source: PR ¶<n> / IFAQ-<n>
Provenance: [OBSERVED] × <n>, [ASSUMED] × <n>  → RESTS ON ASSUMPTION (omit line if none)
Statement: <one sentence, present tense, testable>
Acceptance criteria:
  GIVEN <state before anything happens>
  WHEN  <exactly one action by exactly one actor>
  THEN  <observable from outside the system>
Out of scope: <what a reasonable reader would assume this covers and it does not>
Depends on: <REQ ids / BLK ids, or —>
```

## Delivery requirements (DP)

```
REQ-DP1 · <title>
Source:
Statement:
Acceptance criteria:
Out of scope:
Depends on:
```

---

## Flagged

**No source — not customer-derived**
| REQ | Title | Disposition |
|---|---|---|

**Rests on assumption**
| REQ | Assumed claim | Question | Owner role |
|---|---|---|---|

**Shape pending**
| REQ | Blocked by | How the shape changes with each answer |
|---|---|---|

## Out of scope — candidates
Ideas with no current source. Kept visible; deleting them makes people stop offering them.

- <idea> — would need <what> in the press release to be in scope
