# Platform strategy 2026

*Fictional document, written for the `working-backwards` worked example. It exists so the
example can show what a single strategy doc in `wb/context/` changes about a run. It
describes no real company.*

Owner: VP Platform · Reviewed: January 2026 · Next review: January 2027

---

## Where we are

We closed 2025 with the majority of new revenue coming from customers above 500 seats, up
from roughly a third two years earlier. That shift happened faster than we planned for and
most of our operating assumptions still belong to the self-serve business we used to be.

The pattern in lost deals at that size is consistent and it is not about features. We lose on
security review. Deals stall in a questionnaire, or in a request for evidence we can produce
but cannot produce quickly, or in a clause our standard agreement does not accommodate. We
win the evaluation and lose the procurement.

## The three pillars for 2026

**1 · Depth over breadth.** We are not adding new product surfaces this year. The integration
catalogue stays roughly where it is; the work is making what exists carry enterprise weight.
New surfaces get proposed constantly and the answer this year is no.

**2 · Trust and auditability.** Everything an enterprise buyer needs to satisfy their own
compliance function — access controls that demonstrably work, evidence they can hand to an
auditor without us in the room, and honest limits stated up front rather than discovered in a
questionnaire. This is the pillar we are furthest behind on and the one the lost-deal pattern
points at.

The specific commitment: **by the end of 2026, a customer should be able to answer any
question their auditor asks about our platform using artifacts they can generate themselves.**
Today most of those questions come to us, and some of them we answer with more confidence
than our systems actually support.

**3 · Self-serve efficiency.** The self-serve business funds the enterprise investment and it
has to keep getting cheaper to run. Roughly two-thirds of engineering investment this year is
weighted to self-serve automation and cost, with the remaining third to pillars 1 and 2.

That ratio is the real constraint on everything in this document, and it is where the
arguments will happen. Work that serves pillar 2 competes for the smaller share.

## What we are explicitly not doing in 2026

- New integration types beyond the current catalogue
- A separate enterprise SKU — we are making the existing product enterprise-credible instead
- Anything that requires renegotiating the standard integration agreement at scale, which is
  a 2027 conversation and needs partnerships to have an owner first

## How to argue with this document

If a proposal serves pillar 2 and fits in the one-third, it is aligned and the conversation
is about sequencing.

If a proposal serves pillar 2 and needs more than the one-third, it needs to displace
something and the proposal has to say what.

If a proposal requires changing the integration agreement, it does not fit this year as
written. Say so in the proposal rather than discovering it in review — a proposal that
acknowledges the constraint and asks for an exception is a conversation; one that ignores it
is a rewrite.

## Known gaps in this document

- We have no ownership map for the integration layer. Platform and partnerships have
  overlapping claims and this has cost us twice.
- "Trust and auditability" is not measured. There is no metric behind pillar 2 and there
  should be.
