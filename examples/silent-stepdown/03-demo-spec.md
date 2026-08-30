# Demo spec — Silent Step-Down

An alignment device. Narratable end to end; the failure states are the argument.

## Surface

| Surface | What changes | Source |
|---|---|---|
| Transaction record (reporting + API) | New field `authentication_outcome`: completed · attempted · stepped-down · not-attempted, with timestamp and reason | PR ¶3 |
| Same-day step-down digest | Daily notification to payment-ops contacts listing stepped-down transactions | PR ¶3 |
| Gateway settings → Authentication | Policy control: allow / block / require-exemption. Default: allow | PR ¶5 |

## Primary flow

1. Shopper pays; gateway sends the authentication request.
2. Authentication completes → outcome `completed`, as today.
3. Authentication exceeds the timeout → the gateway consults the merchant's policy —
   **before** any retry, on every path.
4. Policy `allow` → transaction proceeds unauthenticated; outcome `stepped-down`, reason
   `auth-timeout`; appears in that day's digest.
5. Policy `block` → payment fails with the distinct decline reason `authentication
   unavailable`; outcome `attempted`; digest row shows the blocked attempt.
6. Merchant reviews the digest the same day, not at chargeback time.

Source: PR ¶3 / PR ¶5.

## Failure states

| # | What fails | What the merchant sees | Source |
|---|---|---|---|
| F1 | Authentication times out, policy allow | `stepped-down` on the record + digest row, same day | PR ¶3 |
| F2 | Timeout cluster (provider incident) | Digest groups them under one incident line — an outage reads as an outage, not 400 separate alarms | IFAQ-06 |
| F3 | Blocked step-down retried by merchant retry logic | Distinct decline reason is machine-readable so retry systems can back off; docs state it | IFAQ-06 |
| F4 | The policy-consultation call itself fails | Fail toward recording: outcome `stepped-down / policy-unavailable`. Never silent, never `completed` by default | PR ¶3 |
| F5 | Suspicious timeout pattern (possible induced step-down) | Flagged in digest as `pattern: review`; detection heuristic is discovery work, not a promise | IFAQ-03 |

F4 is the design principle: the current defect is silence rendered as success, and the fix
must not contain its own copy of it.

## What this deliberately does not show

No fraud scoring, no automatic blocking of suspicious patterns (F5 flags; it does not act —
BLK-03 is unresolved), and no historical view (BLK-05). Say so in the demo before someone
asks.

## Open questions surfaced

- → Q-07 · Is `authentication unavailable` distinguishable end-to-end through every
  acquirer response-code mapping? · Ask: platform engineering lead
- → Q-14 · Does the digest go to a configured contact or the account owner by default? ·
  Ask: merchant-experience lead
