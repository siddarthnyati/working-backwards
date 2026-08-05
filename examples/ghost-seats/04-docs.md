# Verifying user removal — documentation draft

Drafted from `01-press-release.md` and `02-faq-external.md`. Two sections could not be
written; they are recorded at the bottom rather than written around, because a paragraph
that will not come is a product gap and not a writing problem.

---

## What this does

When you remove someone from your workspace, we check every connected integration to confirm
they no longer have access, and record the result on the audit entry for that removal.

If an integration confirms within 60 seconds, the removal is marked complete for that
integration. If it does not, the removal is marked incomplete and we name the integration.
Source: PR ¶1, PR ¶3.

## Before you start

Nothing to enable. Confirmation runs on every removal from the day it is available on your
workspace. You need the permissions you already have to view audit entries. Source: PR ¶7.

## How to use it

1. Remove a user as you do today.
2. Open the audit entry for that removal.
3. Read the confirmation block. Each connected integration appears with one of four states:

| State | Means |
|---|---|
| **Complete** | The integration confirmed this user no longer has access, at the time shown. |
| **Incomplete** | The integration reported the user still has access, or did not respond within 60 seconds. The integration is named. |
| **Unverifiable — provider unavailable** | The integration could not be reached. This is not the same as incomplete; it means we do not know. |
| **Unverifiable — not supported** | This integration does not expose a way for us to check. |

4. For a periodic access review, use the access-review export. Each removal in the range
   carries its state and the names of any integrations that did not confirm.

## What to do when a removal is incomplete

Open that integration and remove the user's access there directly.

Ghost Seats reports; it does not remediate. We tell you which integration did not confirm,
and the removal in that system is yours to perform. Source: EFAQ-02.

## What you'll see when something fails

Nothing silently succeeds. If the check itself does not run, the entry says so — it will
never show complete by default. Source: 03-demo-spec.md F5.

## Limits

| | |
|---|---|
| Confirmation window | 60 seconds. Later confirmations still land and update the entry. |
| Integrations covered | `[UNKNOWN]` — depends which integrations expose a membership read. See BLK-05. |
| Historical range | `[UNKNOWN]` — see "could not be written yet." |
| Retention of confirmation records | `[UNKNOWN]` — not yet decided. See RFAQ-05. |
| What we store | Event, integration, outcome, timestamp. No document content, and nothing about what the removed user accessed. Source: EFAQ-09. |

## Troubleshooting

| Symptom | Likely cause | What to do |
|---|---|---|
| A removal shows incomplete and names an integration | The integration did not drop access, or did not answer | Remove access in that integration directly, then re-check the entry |
| A removal shows unverifiable — provider unavailable | The integration was unreachable | Re-check later; the entry updates when a confirmation arrives |
| An integration never appears in the confirmation block | It does not expose a membership read | `[UNKNOWN — see "could not be written yet"]` |
| A removal shows complete but the user still has access | Should not occur; the integration confirmed removal | Contact support — this would mean an integration confirmed something untrue |

---

## Could not be written yet

Two sections stalled. Each is a product gap.

**"How far back does the affected-account report go?"**
The press release promises a historical view (PR ¶7) and this documentation cannot say what
it covers, because nobody knows whether the data needed to reconstruct it exists. Every way
of phrasing this either overpromises or advertises the gap.
→ BLK-06 · Ask: platform engineering lead

**"Which of your integrations are covered?"**
This is the first question a reader will have and the documentation cannot answer it. It
needs a list, and the list requires knowing which integrations expose a membership read —
which is BLK-05. Until then the docs describe a capability whose scope is unstated, which is
the shape of a feature that generates support tickets on day one.
→ BLK-05 · Ask: platform engineering lead and partnerships lead

*Writing the docs before building was worth it for the second one. "Which integrations does
this cover" never came up in Stages 1–3 as a question anyone had to answer, and it is the
one a customer asks first.*
