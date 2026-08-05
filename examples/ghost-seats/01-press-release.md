# Ghost Seats

> Revision of `01-press-release-draft1.md`, made in response to `Q-04`. The critic returned
> PASS on all six structural dimensions and raised a question the author acted on anyway.
> See `DECISIONS.md`.
>
> Changed: ¶1 (rationale added), ¶6 (spokesperson quote rewritten to carry the why-now).
> Everything else is unchanged from draft 1.
>
> Paragraph markers `¶n` are load-bearing — requirements cite them.

---

# Revocation you can prove

## When an IT admin removes a user, every connected integration confirms the removal within 60 seconds — or the admin finds out which one didn't.

**¶1** — **SEATTLE, 12 NOVEMBER 2026** — Today we are making user removal verifiable. When
an administrator removes someone from a workspace, the platform now confirms that every
connected third-party integration has actually dropped that person's access, and records the
result on the audit entry. If an integration does not confirm, the administrator sees which
one, and when. Every enterprise customer who signs a data processing agreement with us is
already relying on that confirmation existing. Until today it did not, and the audit log we
give them to prove it says the opposite.

**¶2** — Removing a user has always been a silent operation. The admin clicks remove, the
audit log records it, and everyone assumes it propagated. It does not always. Deprovisioning
fails to reach at least one connected integration in roughly 4,200 accounts per quarter
`[OBSERVED: deprovisioning event log, four-quarter export]`, and nothing surfaces when it
happens — there is no error path in the propagation handler and no field on the audit entry
that would carry one `[OBSERVED: propagation handler and audit log schema]`. The removed
person keeps read access to synced documents for as long as the integration's cache holds
them, which on the two integrations we examined is 90 days `[OBSERVED: documented sync-cache
retention]`, and we are assuming the same of the others `[ASSUMED]`. Administrators find out
during an access review, if they find out at all `[REPORTED: two enterprise support leads]`.
`[NEEDS EVIDENCE: how many removed users actually opened a document during a retained-access
window, and what they opened]`

**¶3** — Ghost Seats closes the loop. Every deprovisioning event now waits on a confirmation
from each connected integration. Confirmations that arrive within 60 seconds mark the event
complete. Anything that does not arrive marks the event incomplete and names the integration
that failed, on the audit entry the admin already reads and in the access-review export they
already run.

**¶4** — Today an administrator has two options and both are bad. They can open each
connected integration and search for the removed person by hand, which does not scale past a
handful of integrations and gets skipped for the departures nobody remembers. Or they can
trust the audit log, which records the local removal and not the propagation — so it is
confidently wrong in exactly the cases that matter. There is no third option today, which is
why the failure has been invisible for as long as it has.

**¶5** — Customer quote:

> "Before this, if someone asked me to prove a contractor no longer had access, I opened
> three consoles and searched for their name. I did that for the departures I remembered.
> The audit log said they were gone, and I believed it."
> — IT administrator, mid-market B2B SaaS customer
> `[illustrative construction — not a real customer statement]`

**¶6** — Spokesperson quote:

> "We sell an audit log as evidence. An audit log that records an intention rather than an
> outcome is not evidence, and every customer who has ever handed one to their auditor was
> handing over something we had not actually verified. That is the reason this is the work
> we are doing now and not next year — not the 4,200 accounts, which is a number that will
> be smaller next quarter either way, but the fact that we have been asking customers to
> trust a record we couldn't stand behind."
> — VP Product

**¶7** — **Getting started.** Nothing to turn on. The next time an administrator removes a
user, the audit entry for that removal shows a confirmation line for each connected
integration. Administrators who want the historical view can request an affected-account
report from the access-review page.

---

*Provenance summary: 4 observed · 1 reported · 1 assumed · 1 needs-evidence*

*Note on ¶1 and ¶6: the rationale added here is the author's, supplied after the critic
observed it was absent. The critic did not and could not supply it, and has no basis to
judge whether it matches the company's actual strategy — see `Q-04` in `QUESTIONS.md`, which
remains OPEN.*
