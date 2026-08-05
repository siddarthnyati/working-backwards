# Ghost Seats, with one document in `wb/context/`

The same problem as `examples/ghost-seats/`, run again with a single fictional strategy
document present. **Stages 1 and 2 only** — enough to show the contrast, and the contrast is
the argument for the whole guardrail design.

Nothing else changed. Same trigger, same customer, same evidence, same press release input.
One file: `wb/context/2026-platform-strategy.md`, two pages.

## What one document bought

| | No context (`examples/ghost-seats/`) | With one strategy doc |
|---|---|---|
| Critic dimension 4 | `Q-04 · Does this rationale match the current strategy? · Ask: your VP · Not evaluable from the document alone.` | Cites pillar 2 by name, quotes the commitment line it aligns with, and quotes the budget-ratio line it conflicts with |
| The draft-1 finding | Rationale absent — the critic could see the absence | **Unchanged.** Absence is a presence check either way |
| Press release ¶1 | Rationale supplied by the author, unverifiable | Rationale can be written against a stated commitment, and its conflict is stated with it |
| IFAQ-03 "what are we not doing instead" | `Q-08 · Ask: your VP` | Answered from the document — and the answer is uncomfortable |
| IFAQ-10 "who owns the integration contract" | `BLK-05 · no clear answer` | **Still BLK-05.** The strategy doc names the gap and does not close it |
| Questions raised at Stages 1–2 | 17 | 13 |
| Blockers raised at Stage 2 | 6 | 6 |

**Six blockers either way.** That is the honest headline. Context makes the question list
shorter and sharper; it does not make the hard questions go away, because the hard questions
are for counsel and for engineering, not for a document.

## The finding the document produced

The interesting result is not that dimension 4 turned green. It didn't.

The strategy doc says trust and auditability is pillar 2 — so Ghost Seats is aligned. The
same document says two-thirds of engineering investment is weighted to self-serve, and that
work requiring changes to the integration agreement "does not fit this year as written."
Ghost Seats needs the second thing.

So the critic can now report a **conflict inside an alignment**, which is a more useful thing
to walk into a VP's office with than either "aligned" or "not evaluable." That is what a
context pack actually buys: not a verdict, a better-specified argument.

The critic still does not rule. It cites and contrasts. `Q-04` is closed and replaced by
`Q-04b`, which is a sharper question with the same owner.

## Files

```
wb/context/2026-platform-strategy.md   the input
00-intake.md                           tier 1 declared, mode selection
01-press-release.md                    ¶1 and ¶6 written against the strategy
02-faq-internal.md                     three answers that were questions before
02-faq-regional.md                     unchanged in substance — no legal docs supplied
DECISIONS.md                           the dimension-4 review, side by side with tier 0
QUESTIONS.md                           13 open, and which four closed
CONFIDENCE.md                          tier 1
session.json
```

Stages 3–8 were not run. They would not add to the contrast.
