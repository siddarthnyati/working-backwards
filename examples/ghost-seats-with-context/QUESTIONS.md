# Questions — Ghost Seats (with context)

Stages 1 and 2 only. Compare with `examples/ghost-seats/QUESTIONS.md`, which lists 17 open at
the same point in the run (20 by Stage 8).

**13 open · 2 with no owner assigned.**

| ID | Question | Ask | Status |
|---|---|---|---|
| Q-01 | Do CCPA/CPRA and DPDPA-style regimes create separate duties, and which notification clocks apply? | privacy counsel | OPEN |
| Q-02 | How do we distinguish an integration outage from a propagation failure? | platform engineering lead | OPEN |
| Q-03 | Does the confirmation mechanism reduce or expand attack surface? | security lead | OPEN |
| Q-04b | Is an exception to the 2027 integration-agreement constraint available this year, and what does it displace? | VP Platform | OPEN |
| Q-05 | Does this cover integrations customers built themselves? | platform engineering lead | OPEN |
| Q-08 | How many stalled enterprise deals cited access evidence? *(narrowed)* | enterprise renewals lead | OPEN |
| Q-09 | Is there historical data from which a retroactive baseline could be computed? | platform engineering lead | OPEN |
| Q-11 | Does shipping a confirmation mechanism constitute an admission? | legal counsel | OPEN |
| Q-12 | What does support tell a customer asking whether they were affected? | support lead | OPEN |
| Q-13 | Do regulated-sector customers carry stricter obligations? | compliance lead | OPEN |
| Q-17 | Where are confirmation records stored, and does residency constrain it? | privacy counsel, platform engineering lead | OPEN |
| Q-18 | Must-be-true: are propagation failures detectable platform-side without polling? | platform engineering lead | OPEN |
| Q-19 | Must-be-true: will admins act on an incomplete state when shown one? | **no owner identified** | OPEN |
| Q-20 | Must-be-true: is 60 seconds achievable across systems we do not control? | **no owner identified** | OPEN |
| Q-21 | *(new)* R3 needs a change the strategy document defers to 2027. Break the plan, or scope around it? | VP Platform | OPEN |

## Closed by the strategy document

| Was | Closed how |
|---|---|
| **Q-04** · Does the rationale match strategy? | Replaced by Q-04b. The document supplied the pillar to align with *and* the constraint to argue about — a sharper question with the same owner, not an answer |
| **Q-06** · What does a confirmation round-trip cost per event? | Not closed by this document. It stays open — listed here only because it is easy to assume a strategy doc reaches cost questions. It does not |
| **Q-07** · Is this included or priced? | Closed. The document's "no separate enterprise SKU — we are making the existing product enterprise-credible instead" settles it: included |
| **Q-15** · What is an acceptable propagation rate? | Not reached — Stage 5 was not run here, and the document says pillar 2 is unmeasured anyway |
| **IFAQ-03** · What are we not doing instead? | Answered from the investment ratio |
| **IFAQ-16** · Does launch comms say this was broken? | Default posture settled by "honest limits stated up front" |

Net: four questions closed at Stages 1–2, one added, one sharpened.

## Still unowned — unchanged

**Q-19** and **Q-20** have no owner in this run either. A strategy document is the wrong
instrument. What these need is an ownership map, which the strategy document explicitly says
does not exist:

> *no ownership map for the integration layer. Platform and partnerships have overlapping
> claims and this has cost us twice.*

So the tier-1 run knows *why* the questions are unowned. It still cannot assign them.

## What the tier-0 run could not have found

**Q-21.** Nothing in the problem statement, the press release, or Amazon's public FAQ bank
would produce "your delivery plan conflicts with a constraint in this year's strategy." It is
not a question about the product. It is a question about the company, and it required the
company's document.

This is the case for `wb/context/`, stated as narrowly as it deserves to be: one document,
one conflict found, four questions closed, zero blockers closed.
