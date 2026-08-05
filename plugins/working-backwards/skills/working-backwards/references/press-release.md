# Press release

Read this before Stage 1. One page. Written as if it already launched.

## The seven components, in order

| # | Component | What it must accomplish |
|---|---|---|
| 1 | Heading | Name the product in a way the customer would recognise. Not the project codename, not the internal system. If the customer wouldn't say it, it isn't the heading. |
| 2 | Subheading | One sentence naming the customer segment and the benefit. This is the sentence that gets quoted back at you, so make it the one you'd defend. |
| 3 | Summary paragraph | City, outlet, dated launch. Then what shipped and why it matters, in three or four sentences. Written for someone who reads only this paragraph — because most people will. |
| 4 | Problem paragraph | In the customer's voice, not the company's. What goes wrong, how often, who it happens to, what it costs them. Every claim carries a provenance tag. |
| 5 | Solution paragraph(s) | What the customer does now, what they see, and — critically — what they use today and why it falls short. |
| 6 | Customer quote | A named-role customer describing the change in their own words. Labelled as an illustrative construction. |
| 7 | Spokesperson quote | Why the company built it. This is where the strategic rationale lives, and it is the paragraph most often missing. |
| 8 | Getting started | What a customer literally does first. One or two sentences. |

Eight rows for "seven components" because getting-started is conventionally counted with
the quotes. Keep all eight.

## Customer-backwards vs skills-forward

**Skills-forward** starts from what the team can already build and works out toward a
customer who might want it. It reads fluently, passes internal review easily, and describes
a product nobody switches to — because the customer's actual problem was never the input.

**Customer-backwards** starts from a specific customer's specific problem and works back to
what would have to exist. It is uncomfortable to write, because halfway through you discover
you cannot build the thing the customer needs. That discovery is the point, and it is
cheaper here than in month four.

The tell: if the solution paragraph could have been written before the problem paragraph,
it was.

## The valuable-destination test

Bryar and Carr's framing: a great press release defines a destination valuable enough that
the organisation will solve hard problems to reach it. A ho-hum press release describes a
destination nobody will fight for — and the correct response is to discard it before writing
the FAQ, not to write a better FAQ.

Applied concretely: read the subheading and ask whether a team would reorganise a quarter
around it. If the honest answer is no, the press release is not weak — the idea is.

## Two contrasting examples

### Ho-hum — discard before the FAQ

> **Improved deprovisioning diagnostics**
> *Admins can now view a detailed log of deprovisioning events.*
>
> A new log page shows each deprovisioning event with a timestamp and status, giving
> administrators improved visibility into user removal across the platform.

Why this should be discarded: it delivers a log to someone who did not know they had a
problem. The destination — "there is a page you can go look at" — is not worth a quarter.
Nobody switches vendors for it. Writing an FAQ against this produces a smaller version of
the same document.

Note also that it solves the *company's* problem (we can now prove what happened) while
appearing to solve the customer's.

### Forcing — worth the hard problem

> **Revocation you can prove**
> *When an IT admin removes a user, every connected system confirms the removal within 60
> seconds — or the admin finds out which one didn't.*
>
> Removing a user has always been a silent operation. The admin clicks remove, the audit log
> records it, and everyone assumes it propagated. When it doesn't, nothing surfaces — the
> access stays live and the log still says the user is gone.

Why this forces the hard problem: "or the admin finds out which one didn't" commits to
detecting a failure the platform currently cannot see. You cannot write that sentence and
then ship a log page. The FAQ will immediately ask how you detect a failure in a system you
don't control, and that question is exactly the one worth having early.

The rule of thumb: a good press release contains at least one sentence that makes an
engineer wince.

## Provenance in the press release

Tags appear inline and survive into the published artifact. This looks unpolished and it is
supposed to.

> Deprovisioning events silently fail to propagate to at least one connected integration in
> roughly 4,200 accounts per quarter `[OBSERVED: platform event log export]`. Admins report
> discovering this only during access reviews `[REPORTED: two enterprise support leads]`. We
> believe most affected customers never discover it at all `[ASSUMED]`.

Where a number is wanted and absent:

> `[NEEDS EVIDENCE: quantify frequency and affected population]`

Never resolve one of these by writing a plausible figure. The gap is the honest artifact.

## The customer quote

Format:

> "Before this, I had to open three consoles and search for the person by hand every time
> someone left. I did it for the departures I remembered." — IT administrator, mid-market
> B2B SaaS customer
> `[illustrative construction — not a real customer statement]`

The label is not optional. An unlabelled invented quote is the single most quotable
fabrication in the whole pipeline, and it will be read as research.

A quote that only restates the benefit ("This is a great improvement to our workflow") is
doing no work. The good ones describe the old behaviour in enough detail that a reader
recognises it.

## Common failures at this stage

- **The problem paragraph is written in the company's voice.** "We have identified a gap in
  our propagation layer" is not the customer's problem; the customer does not know the
  propagation layer exists.
- **The spokesperson quote restates the subheading.** Its job is the *why now* — the reason
  this is worth funding this quarter. If it doesn't say that, dimension 4 will surface it.
- **No alternative named.** There is always a current behaviour. Find it.
- **A number with no tag.** Every figure carries provenance or it comes out.
