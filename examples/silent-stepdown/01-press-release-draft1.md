# Silent Step-Down — Draft 1

> **First draft, kept.** The critic returned REVISE on dimension 3 — see `DECISIONS.md`.
> The revised version is `01-press-release.md`. ¶ markers are load-bearing.

---

# Authentication you can hold us to

## When a merchant turns on 3-D Secure, every transaction is either authenticated or the merchant decides what happens next — nothing falls through silently.

**¶1** — **AMSTERDAM, 15 JANUARY 2027** — Today we are ending the silent fallback. Until
now, when an authentication request timed out, the gateway quietly retried the payment
without authentication and moved on. From today, every transaction records its
authentication outcome, merchants can see it, and merchants set the policy for what happens
when authentication cannot complete.

**¶2** — Merchants who enable 3-D Secure believe every eligible transaction is
authenticated. It is not. When the authentication service does not respond within 3 seconds,
the gateway steps the transaction down and processes it unauthenticated — roughly 31,400
times a quarter on the European corridor alone `[OBSERVED: gateway auth event log]`. No
field in reporting records that this happened `[OBSERVED: reporting schema]`. On those
transactions, fraud liability sits with the merchant instead of the issuer `[OBSERVED:
scheme liability-shift rules]`. We believe stepped-down transactions also carry more fraud,
though we have not measured it `[ASSUMED]`. `[NEEDS EVIDENCE: chargeback rate on
stepped-down vs authenticated transactions]`

**¶3** — From today, every transaction carries an authentication outcome — completed,
attempted, stepped down, or not attempted — in reporting and in the API. When a step-down
happens, the merchant sees it the same day, not at chargeback time.

**¶4** — Merchants currently have no way to detect this happening.

**¶5** — Merchants also gain a policy control: allow step-down, block it and fail the
payment, or require an explicit exemption. The default preserves today's behaviour, minus
the silence.

**¶6** — Customer quote:

> "We turned on 3DS for exactly one reason: the liability shift. Finding out some of our
> traffic was quietly running without it — and we were eating those chargebacks — would
> have been an unpleasant month."
> — payment operations lead, mid-market e-commerce merchant
> `[illustrative construction — not a real customer statement]`

**¶7** — Spokesperson quote:

> "A silent fallback made sense when the alternative was a failed payment. But a merchant
> who delegated fraud liability deserves to know when it lands back on them. Visibility
> first, then choice."
> — VP Product

**¶8** — **Getting started.** Nothing to enable for visibility — the authentication-outcome
field appears on every transaction from today. Policy controls are in gateway settings under
Authentication.

---

*Provenance summary: 4 observed · 0 reported · 1 assumed · 1 needs-evidence*
