# Blocker taxonomy

Read this when the FAQ stage starts producing blockers — usually Stage 2, occasionally
Stage 5 or 6.

## The rule that governs this file

**A blocker is a question, never a finding.**

You cannot discover legal exposure, assess regulatory risk, or determine feasibility. You
can notice that a question exists, phrase it so the right person can answer it in five
minutes, and name that person's role.

`Status` is only ever changed by the user. There is no path by which you mark your own
question resolved. A blocker you closed yourself is worse than one you never raised, because
the user stops looking at it.

Write blockers as an **Ask**, not an assertion:

| Don't write | Write |
|---|---|
| "This violates GDPR erasure obligations." | "Does retained read access after revocation constitute a failure of our erasure obligations, and is it reportable?" |
| "SOC 2 control CC6.2 is invalidated." | "Does this behaviour fall under the access-revocation criteria we attested to, and if so does it need disclosure at the next audit?" |
| "The integration team owns this." | "Which team owns the integration contract — platform or partnerships? The FAQ surfaced no clear answer." |

The left column is a claim you cannot support. The right column is useful to someone.

## Record format

```
BLK-03 · PRIVACY · severity: high
Surfaced by: RFAQ-02
Ask: Does retained read access after revocation constitute a failure of our erasure
     obligations, and is it reportable?
Owner role: privacy counsel / DPO
Blocks: REQ-D4, REQ-DP1
Status: OPEN
```

- **ID** — `BLK-<n>`, permanent, cited by requirements and release slices.
- **Category** — one of the seven below. Pick the primary one; note a secondary in the Ask
  if it genuinely spans two.
- **Severity** — `high` blocks a release slice or changes what you owe customers ·
  `medium` blocks a requirement's shape · `low` needs answering before GA but nothing waits
  on it. Severity is about what waits, not about how alarming it sounds.
- **Surfaced by** — the FAQ ID. If a blocker has no surfacing question, it arrived by
  assertion, which is the thing this file exists to prevent.
- **Owner role** — a role, never a person. "Privacy counsel," "platform engineering lead,"
  "the partnerships PM." If you cannot name a role, write `no owner identified` and count it
  in `CONFIDENCE.md` — an unowned blocker is its own finding.
- **Blocks** — REQ and R ids. Empty at Stage 2 and filled in at Stage 6; go back and
  populate it.
- **Status** — `OPEN` until the user changes it. You write `OPEN`. Always.

## The seven categories

### `LEGAL`
Contractual exposure, liability, what customers were promised, disclosure obligations.

- What do our existing contracts and DPAs already commit us to here?
- What is our exposure for occurrences that already happened, before this ships?
- Does shipping this constitute an admission about the prior state?
- Are we obliged to notify affected customers, and on what clock?

### `PRIVACY`
Data protection regimes, lawful basis, consent, erasure, transfers, controller/processor
roles.

- What personal data flows through this and on what lawful basis?
- Can we honour an erasure request end to end after this ships? Could we before?
- Does this create a new processor relationship or a new cross-border transfer?
- Is this failure reportable to a supervisory authority, and on what clock?

### `REGULATORY`
Sector rules, mandates, certification, attestation.

- Does an existing certification (SOC 2, ISO 27001, sector equivalent) have a control this
  touches?
- Does the current behaviour invalidate a control we have already attested to?
- Does any sector regulation apply to a subset of customers?
- Is there a mandate with a fixed date driving this?

### `SECURITY`
Access, retention, attack surface, blast radius.

- What access does this need that nothing currently has?
- What is the exposure window in the current failure, precisely — start to end?
- What is the retention profile of anything new we store?
- If this component is compromised, what does the attacker reach?

### `DEPENDENCY`
Another team owns it — or, more often, nobody does.

- Who owns the system this depends on, and have they agreed to the work?
- Is there a contract or integration agreement with a third party that constrains this?
- What already exists that does part of this, and who maintains it?
- What is the failure mode when the dependency is unavailable?

The most valuable version of this question is "who owns it," because "two teams,
partially" is extremely common and never surfaces on its own.

### `DATA`
Can we measure the thing at all.

- Can we enumerate the affected population — retroactively, or only going forward?
- Do we have a baseline for the metric the press release implies?
- Is the data we'd need retained long enough to answer the question?
- Does answering this require data we do not control?

`DATA` blockers are the ones people skip because they feel like engineering detail. They
are usually the ones that change the plan, because "we can only measure going forward"
rewrites the discovery slices.

### `COMMERCIAL`
Pricing, margin, partner economics, packaging.

- Is this included, an add-on, or usage-priced — and who decides?
- What does it cost to run per unit, and does that change the margin on the plan it lands in?
- Does this change a partner's economics or an existing revenue share?
- What are we not doing instead?

## Blockers file

`BLOCKERS.md` opens with a table for scanning, then the full records:

```
| ID | Category | Sev | Ask (short) | Owner role | Blocks | Status |
|---|---|---|---|---|---|---|
| BLK-01 | SECURITY | high | Exposure window for retained access | security lead | REQ-D1 | OPEN |
```

Sort by severity, then by ID. Update `Blocks` after Stage 6 and `08-readiness.md` groups by
severity for the go/no-go.

## What a blocker is not

- **Not a task.** "Build the confirmation handler" is a requirement.
- **Not a risk register entry.** "This might be hard" has no owner and no ask.
- **Not resolved by reasoning about it.** If you find yourself writing an Ask and then
  answering it two lines later, you have written an FAQ answer tagged `OPEN`, not a blocker.
