# Demo spec — Ghost Seats

An alignment device, not a design deliverable.

## Surface

Two existing surfaces gain fields. Nothing new is built.

| Surface | What changes | Source |
|---|---|---|
| Audit entry for a removal | A confirmation block: one row per connected integration, each with an outcome and a timestamp | PR ¶3 |
| Access-review export | A column per removal — `complete`, `incomplete`, or `unverifiable` — plus the names of any integrations that did not confirm | PR ¶3 |
| Affected-account report (new page, historical view) | A date-ranged list of removals that cannot be confirmed complete | PR ¶7 · **shape depends on BLK-06** |

The third one is drawn dashed in any diagram of this. It is specified here because the press
release promised it, and it is marked because Stage 6 cannot yet say what it is.

## Primary flow

1. Admin removes a user from the workspace → the removal happens locally, as today.
2. Platform sends a membership check to each connected integration.
3. Each integration responds, or does not, within 60 seconds.
4. All responded and all confirm removal → the audit entry shows **complete**, with a
   per-integration timestamp.
5. Any did not respond, or responded that the user is still present → the audit entry shows
   **incomplete** and names the integration.
6. A late confirmation arriving after 60 seconds moves the entry to complete and records
   both timestamps — so a slow integration reads as latency, not as a failure.

Source: PR ¶3 / EFAQ-08

## Failure states

These are the part worth arguing about. A demo spec with only a happy path has not been read
by anyone who operates the system.

| # | What fails | What the admin sees | Source |
|---|---|---|---|
| F1 | An integration responds that the user is still present | `incomplete` · integration named · "still has access as of <time>" | PR ¶3 |
| F2 | An integration does not respond within 60 seconds | `incomplete` · integration named · "no response" — and the entry updates itself if a response arrives later | EFAQ-08 |
| F3 | An integration is having an outage | Distinguished from F2 and labelled `unverifiable — provider unavailable`, **not** `incomplete` | IFAQ-11 |
| F4 | An integration exposes no way to read membership at all | `unverifiable — not supported by this integration`, stated once at connection time and not repeated per removal | IFAQ-12 · **BLK-05** |
| F5 | The confirmation mechanism itself fails | The entry says the check did not run. It never says `complete` by default. | IFAQ-08 |

F3 is the one that came out of the internal FAQ and it is the one that decides whether this
feature is trusted. If a partner's routine outage produces the same red state as a genuine
retained-access failure, admins learn to ignore the red state within a month, and we will
have built a worse version of nothing. Source: IFAQ-11 / Q-02.

F5 is a design principle rather than a screen: silence must never render as success. The
current defect is exactly that failure, and rebuilding it inside the fix would be a
particular kind of embarrassing.

F4 has no agreed treatment because BLK-05 is open. What is drawn here is a placeholder.

## What this deliberately does not show

No remediation. The admin is told which integration did not confirm; they are not offered a
"force removal" button. Ghost Seats reports, it does not act.

This boundary is deliberate and it is the one most likely to disappoint in a demo — the
first question anyone asks after seeing F1 is "so can I fix it from here?" The answer is no,
and the reason is that forcing a revocation into a third-party system requires write access
and an agreed contract that BLK-05 has not established yet. Say this out loud in the demo
rather than letting someone infer it. Source: EFAQ-02.

## Open questions this surfaced

- → Q-02 · How do we distinguish an integration outage from a propagation failure, from the
  platform side? · Ask: platform engineering lead
- → Q-14 · If an integration can be checked but not written to, is `unverifiable` an
  acceptable permanent state for that integration, or does it disqualify it from being
  connected? · Ask: partnerships lead
