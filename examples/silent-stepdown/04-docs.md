# Authentication outcomes — documentation draft

Drafted from the approved PR and external FAQ. One section could not be written; recorded
at the bottom rather than around.

## What this does

Every transaction now carries an `authentication_outcome` field: `completed`, `attempted`,
`stepped-down`, or `not-attempted`, with a reason and timestamp. When authentication cannot
complete, your policy decides what happens. Source: PR ¶3 / PR ¶5.

## Before you start

Nothing required. The field appears on all transactions from launch. Policy controls need
account-admin permission. Source: PR ¶8.

## Reading the field

| Value | Means | Liability note |
|---|---|---|
| `completed` | Authentication succeeded | Liability shift applies per scheme rules |
| `attempted` | Authentication attempted; transaction did not proceed unauthenticated | — |
| `stepped-down` | Processed without authentication after a timeout, per your policy | Liability generally sits with you — public scheme rules |
| `not-attempted` | Authentication not requested (not enabled / out of scope) | — |

## Setting your policy

Settings → Authentication → On timeout: **Allow** (default — today's behaviour, visible),
**Block** (fail the payment with decline reason `authentication unavailable`), or
**Require exemption** (see "could not be written yet").

Before choosing Block, request your merchant-level step-down count — that number is your
conversion exposure. Source: EFAQ-04.

## Troubleshooting

| Symptom | Likely cause | What to do |
|---|---|---|
| Sudden spike of `stepped-down` in one hour | Authentication provider incident (digest groups it) | No action; monitor the incident line |
| `authentication unavailable` declines rising | Your policy is Block and timeouts increased | Review the digest; consider timeout trend before switching policy |
| A stepped-down transaction got a fraud chargeback | Liability likely yours on that transaction | Dispute data is in the record; see your agreement for anything further |

## Could not be written yet

**"Require exemption" — which exemption, and when is it available?**
Whether an exemption flag can or must be applied to a stepped-down EEA transaction is a
compliance determination that has not been made. Until it is, this policy option cannot be
documented — or shipped. → BLK-02 · Ask: compliance lead

**"How far back can I see outcomes?"**
Historical enumeration is unresolved. → BLK-05 · Ask: data platform lead
