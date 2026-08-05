# Regional FAQ — Ghost Seats (with context)

**Unchanged from `examples/ghost-seats/02-faq-regional.md`. Every entry, every tag, every
blocker.**

This file exists to say that.

The supplied context is a strategy document. It has nothing to say about erasure obligations
under GDPR-style regimes, about whether retained access is reportable, about what our DPAs
commit us to, or about whether a SOC 2 control has operated as described. So the regional
bank produced exactly the same questions and exactly the same two blockers — BLK-02 and
BLK-04 — as the tier-0 run.

## Why this is the honest half of the demo

The temptation in an example like this is to show context improving everything at once, which
would misrepresent what context does. Context is not a general-purpose upgrade. It is
specific: a strategy document answers strategy questions, and it answers nothing else.

The unlock table in `CONFIDENCE.md` is not decoration — it is a statement about which
document reaches which dimension. To move anything in this file you would need:

| To change… | You would need in `wb/context/` |
|---|---|
| RFAQ-01, RFAQ-02 → cite a clause | Your standard DPA and the negotiated variants |
| RFAQ-06 → cite a control | The current SOC 2 control narrative |
| RFAQ-05 → answer residency | The data-residency commitments by customer tier |
| RFAQ-07 → scope the sector question | Customer segmentation by regulated sector |

And even with all four, BLK-02, BLK-03 and BLK-04 would **still be OPEN and still route to
counsel**. What would change is that counsel receives a five-minute question citing a clause
number instead of a research task describing the shape of a problem.

That is the ceiling on what any context pack can do for this class of question, and it is
worth being clear about it: no amount of documentation converts a legal determination into a
document lookup.
