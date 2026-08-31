# Context elicitation

Read this when a session starts at tier 0 and the user has nothing to put in `wb/context/`.

## Why this exists

Most of the context a session needs is not in a document anywhere — it is in the user's
head, tacit and unwritten. "Bring your own context" fails the majority of users if the only
way to bring it is to already have it written down. The elicitation interview extracts it:
ten minutes of questions, written to `wb/context/elicited.md`, and the session runs at
tier 1 against the user's own answers.

Offer it once, after intake questions and before Stage 0 output:

> You're at tier 0 — no context pack. Two options: proceed (strategic fit and feasibility
> become questions for named humans), or answer a 10-minute interview and I'll build you a
> starter context pack from your own knowledge. It won't be as good as real documents, and
> it will say so — but it turns "not evaluable" into "evaluable against what you told me."

Never require it. Never re-offer it after a decline.

## The interview

One slot at a time, in this order — stop the moment the user wants to stop, and keep what
you have. For each slot, ask the questions, then read back what you wrote before moving on.

**1 · Strategy (unlocks dimension 4)**
- What is the company's stated priority this cycle — in whatever words leadership uses?
- Who said it, where? (all-hands, a memo, a goal doc, your manager, your inference)
- What is the company explicitly *not* doing right now?

**2 · Metrics (grounds Stage 5)**
- What number does your team get judged on? What is it today, roughly?
- Is that number written down with a definition, or does everyone just "know" it?

**3 · What exists today (grounds dimension 3 and Stage 3)**
- Has anything like this been tried before here? What happened to it?
- What do the affected users do today instead — including "nothing" and "a spreadsheet"?

**4 · Ownership (gives blockers real owners)**
- For each area this touches: who owns it? A name or team, not a diagram.
- Where do you genuinely not know who owns something? (That answer is a finding, not a gap
  in the interview.)

**5 · Constraints (feeds the regional/internal FAQs)**
- Any contracts, certifications, or regulatory regimes you know apply — even vaguely?
- Any deadline or mandate with a date on it?

**6 · Evidence (upgrades the problem paragraph)**
- What data have you personally seen that makes this a problem? Where does it live?
- What do you believe about this problem that you have never actually checked?

That last question is the most valuable one in the interview. Ask it slowly.

## Provenance rules — what makes this honest instead of circular

- Every answer is tagged `[REPORTED: the user — <their role>]`, never `[OBSERVED]`. The
  user *telling you* the strategy is testimony, not a document.
- When the user hedges ("I think", "probably", "as far as I know"), write the claim as
  `[ASSUMED]` and say you did. Do not average hedged answers into confident ones.
- Answers to "what do you believe but haven't checked" are recorded under a heading
  **Declared assumptions** — they are the user pre-registering their blind spots, and
  Stage 6 flags any requirement resting on them exactly as it would any other `[ASSUMED]`.
- Write the pack to `wb/context/elicited.md` with a header stating: elicited, from whom
  (role), when, and in one line what a real document would add. Set the session tier to 1
  and record the pack as self-reported in `session.json` and `CONFIDENCE.md`.

## What an elicited pack does and does not buy

- Dimension 4 can now *cite* — "aligned with what you told me the priority is
  `[REPORTED: you]`" — and every such citation carries the self-reported marker. It is
  better than "not evaluable" and weaker than a real strategy doc, and both halves of that
  sentence go in `CONFIDENCE.md`.
- Blocker owner roles resolve to the names/teams the user gave, instead of generic titles.
- **Blockers still do not close.** Testimony does not answer legal, privacy, regulatory,
  security, data, or commercial questions — it only addresses them better. The elicited
  pack changes who the questions name, never whether they exist.
- The critic treats a conflict between the user's artifact and the user's own elicited
  answers exactly like a conflict with a document: cite the line, ask which is right.
