# FAQ banks

Read this before Stage 2. Three banks: external, internal, regional.

**Contents**
- [How to run this stage](#how-to-run-this-stage)
- [The seven reviewer questions](#the-seven-reviewer-questions)
- [External bank](#external-bank)
- [Internal bank](#internal-bank)
- [Regional bank](#regional-bank)
- [Answer format and tags](#answer-format-and-tags)

---

## How to run this stage

The internal FAQ is a **risk-discovery engine**, not a documentation chore. It is the stage
that pays for the whole pipeline: it reliably surfaces questions the author had not thought
to ask, before a single requirement is written.

Three rules for getting that value:

1. **Ask the hostile version.** Not "how do we handle data retention" but "when a customer's
   regulator asks us to prove we deleted something, what do we show them, and what happens
   if we can't?" The polite version of a question produces a polite answer that hides the
   blocker.
2. **Answer in the voice of the person who'd ask.** The finance question should sound like
   finance. Adopting the voice is what makes you generate the follow-up they'd actually ask.
3. **An FAQ with no `BLOCKER` tags was not written honestly.** Every real initiative has
   something uncomfortable in it. If you finish the internal bank with nothing tagged, go
   back and ask the version of each question that assumes the initiative fails.

Numbering: `EFAQ-01`, `IFAQ-01`, `RFAQ-01`. Requirements cite these IDs, so they are stable
once written — append, don't renumber.

In Targeted and Lightweight modes only the internal bank runs (`2i`).

---

## The seven reviewer questions

Bryar and Carr's evaluation set. Run these against the press release before writing the
banks — they determine which questions actually matter here.

1. Is the customer clearly defined?
2. Is the problem clearly defined?
3. Does the solution actually address the problem?
4. Would customers change their behaviour to adopt it?
5. On which dimension is it better, cheaper, or faster — and by how much?
6. Is the payback big enough to be worth doing?
7. What constraints must be solved before this can exist?

Questions 5, 6 and 7 are substantive: you cannot answer them, you can only sharpen them and
name who can. Route them to `QUESTIONS.md`.

---

## External bank

What press, customers, and prospects ask. Public-facing; the answers should be ones you'd
put on a website.

**Product and scope**
- What exactly does this do, in one sentence?
- Who is it for, and who is it explicitly not for?
- What does it not do that people will assume it does?
- How is this different from what we already offer?

**Adoption**
- What do I have to do to turn it on?
- Do I have to change anything I'm doing today?
- What happens to my existing data and configuration?
- Is there a migration, and who does the work?

**Commercial**
- What does it cost? Is it included, an add-on, or usage-priced?
- Does this change my current bill?
- Is it available on my plan?

**Trust and operations**
- What happens when it fails? What do I see?
- What are the limits — rate, volume, size, latency?
- How is it supported, and what's the response commitment?
- Where is my data, and who can see it?

**Timeline**
- When is it available, and where?
- Is there a beta, and how do I get in?

Prune ruthlessly to the ones this initiative actually raises. A generic external FAQ is
filler and dimension 8 shouldn't reward it.

---

## Internal bank

The one that matters. Group by the leader who would ask.

**Finance**
- What does this cost to build, and to run per unit of usage?
- What revenue does it protect or create, and how would we know?
- What are we not doing instead?
- If this works perfectly, what line on a financial statement changes?

**Legal**
- What do our customer contracts and DPAs already commit us to here?
- If the failure this fixes has already occurred, what is our exposure for the past
  occurrences?
- Does shipping this constitute an admission about the prior state?
- What do we have to tell customers, and when?

**Security**
- What is the attack surface this adds or removes?
- What access does this need that nothing currently has?
- What is the retention profile of anything new we store?
- If this component is compromised, what does the attacker get?

**Privacy**
- What personal data flows through this, and on what lawful basis?
- Can we honour an erasure request end to end after this ships?
- Does this create a new processor relationship or a new transfer?
- What do we log, and for how long, and is that defensible?

**Engineering and platform**
- Who owns the system this depends on, and have they agreed?
- What already exists that does part of this?
- What is the failure mode when a downstream dependency is unavailable?
- What is the rollback story?

**Operations and support**
- What new ticket type does this create, and who resolves it?
- What does support tell a customer when it fails?
- What runbook does this need on day one?

**Data**
- Can we measure the thing the press release claims?
- Can we enumerate the affected population — retroactively, or only going forward?
- What is the baseline, and do we have it today?

**Go-to-market**
- Who has to be told, and what do we say to customers already affected?
- Does this change the sales conversation, and does the field need training?

**The three that surface the most blockers**, in practice:
- *Can we enumerate the affected population retroactively?* — almost always `DATA`.
- *Who owns the system this depends on?* — almost always `DEPENDENCY` when the answer is
  "two teams, partially."
- *What is our exposure for the occurrences that already happened?* — almost always `LEGAL`.

---

## Regional bank

Jurisdictional questions. Named regulations here are public law, cited as categories — you
are generating the question, never an opinion on compliance.

**Data protection**
- Where is the data stored and processed, and does any region require it stay local?
- Under GDPR-style regimes, what is the lawful basis, and who is controller vs processor?
- Under CCPA/CPRA-style regimes, does this touch a "sale" or "share" definition?
- Under DPDPA-style regimes, what consent notice is required and in what languages?
- Does an erasure request propagate everywhere this feature sends data?

**Sector rules**
- Does any sector regulation apply to a subset of customers (health, financial, public
  sector, education)?
- Does an existing certification (SOC 2, ISO 27001, sector equivalents) have a control this
  touches — and does the current behaviour invalidate a control we have already attested?
- Are there financial-services rules on access, audit, or strong authentication that apply?

**Operational and localisation**
- What are the breach or incident notification clocks in each jurisdiction, and who starts
  them?
- Does any market require local support, local language, or local entity involvement?
- Do any customer contracts include jurisdiction-specific commitments that differ from the
  global default?

Each of these produces a question and an owner role. None produces a compliance conclusion.
"We are compliant" is not a sentence you can write.

---

## Answer format and tags

Every answer carries exactly one tag.

| Tag | Meaning |
|---|---|
| `ANSWERED` | The answer is known and stated, with provenance. |
| `OPEN` | Needs an answer; nothing blocks on it yet. |
| `BLOCKER` | Something downstream cannot proceed until a named role answers this. |

```
IFAQ-07 · Privacy · BLOCKER
Q: If a removed user retains read access to synced documents for up to 90 days, is that a
   failure of our erasure and access-revocation obligations, and is it reportable?
A: Not evaluable here. This is a determination for privacy counsel, and the answer changes
   what we owe customers about occurrences that have already happened.
   → BLK-02 · PRIVACY · severity high · Owner role: privacy counsel / DPO · Status: OPEN
```

```
IFAQ-05 · Data · OPEN
Q: Can we enumerate the affected population retroactively?
A: Going forward, yes — the propagation handler can emit a confirmation event
   `[ASSUMED: no handler exists today, so this is a design claim, not an observation]`.
   Retroactively is unknown; it depends whether historical events are recoverable from the
   integrations' own logs, which we do not control.
   → Q-11 · Ask: platform engineering lead + each integration partner
```

Rules:

- A `BLOCKER` tag always creates a record in `BLOCKERS.md` with an owner role, a severity,
  and what it blocks. See `blocker-taxonomy.md`.
- Never change a blocker's `Status`. Only the user does that.
- `ANSWERED` requires provenance. An answer tagged `ANSWERED` with `[ASSUMED]` inside it is
  actually `OPEN` — say so.
- Answers may say "not evaluable here." That is a legitimate answer and it is better than a
  confident wrong one.
