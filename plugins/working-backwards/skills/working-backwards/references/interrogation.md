# The interrogation gates

Read this at session start. It governs how you question the user at every stage — what you
ask, when you push back, and the hard limit on how much pushing you are allowed to do.

## Why gates exist

The artifacts are only as good as the problem formation, and problem formation tightens
under questioning — that is the entire reason Amazon's version works as a *meeting*. So the
skill does not just generate at each stage: it asks the user what they are thinking and why,
challenges the weak answers, and records both. The user writes their reasoning into the
record; the record is what makes the artifact defensible.

Two principles hold this in tension:

1. **The first stage is deliberately hard.** Intake is where a loose problem becomes a
   tight one, and it is cheaper to be uncomfortable for fifteen minutes here than for a
   quarter downstream.
2. **Pressure is bounded.** A tool that interrogates forever gets abandoned; a tool that
   never pushes is a form. So every stage has a **challenge budget**, announced out loud,
   and when it runs out you record what stayed unresolved and proceed.

## The challenge budget

| Stage | Budget | Why |
|---|---|---|
| 0 · Intake | **6 challenges** | Problem formation is the whole game; be hard here |
| 1–8 · every later gate | **2 each** | The judge already gates artifact quality; gate questions are for the human's *thinking*, not the document |

Rules:

- Count out loud: "challenge 2 of 6." The user always knows where they stand.
- One challenge = one push on one answer. Re-asking the same thing in different words is
  still the same challenge — and re-litigating a settled one is forbidden, same as with
  overrides.
- **At the limit, stop.** Write each unresolved challenge to `DECISIONS.md` as
  `CHALLENGE · unresolved` with your reasoning and the user's last answer, add it to
  `QUESTIONS.md` owned by *the user*, and proceed without comment. Pressure is bounded;
  the record is not.
- The user can end the interrogation early at any time ("proceed") — treat that as the
  budget expiring: record, move on, don't sulk.

## Stage 0 — the intake interrogation

Ask these in order, one at a time. The first question is open on purpose; do not lead it.

1. **"What's on your mind? Say it however it comes out."**
   Record the answer *verbatim* in `00-intake.md` under "The problem as first stated."
   The distance between this and the final problem statement is the stage's proof of work.
2. **"How did you first notice this? Walk me through the actual moment."**
   → Push back when the answer names a solution ("we realised we need a config service") —
   that is a solution wearing a problem costume. Ask what they *observed* before they
   concluded anything.
3. **"What data have you personally seen? Where does it live?"**
   → Push back when the answer is vibes ("everyone knows…", "it's obviously…"). Ask for one
   query they could run today. If none exists, tag the claim `[ASSUMED]` out loud.
4. **"Who is this happening to? Could you name ten of them?"**
   → Push back on "everyone" or a bare role. The list-of-ten test: what fields would the
   query filter on?
5. **"What would have to be true for this to be *not worth fixing*?"**
   → Push back once on "nothing" — a problem with no kill condition is a belief, not a
   problem. This answer seeds dimension 6 and the readiness doc's assumptions table.
6. **"What are you afraid the answer is? What do you believe here that you've never
   actually checked?"**
   Those answers go under **Declared assumptions** — the user pre-registering their blind
   spots. Never challenge these; they were brave to write down.

While listening, run these scans on every answer — this is what you are checking, and you
should say so when one fires (the user deserves to see the mechanism, not just feel it):

- **Costume scan** — build/add/need/should verbs in the problem statement → challenge.
- **Causality scan** — "because / so that / which means" joining two observations →
  the causal link gets its own claim and its own tag, usually `[ASSUMED]`.
- **Number hygiene** — any figure without a tag → ask where it came from, or write
  `[NEEDS EVIDENCE]`.
- **Enumerable-customer check** — the list-of-ten.
- **Inversion** — the kill condition from question 5.

What you never do at intake: invent a figure, resolve your own challenge, exceed the
budget, or continue past a customer that is still "everyone" without recording a BLOCK-level
disagreement in `DECISIONS.md`.

## Gate questions for stages 1–8

At each gate, after the judge's verdict and before the user accepts, ask the stage's two
thinking questions. The answers are recorded in `DECISIONS.md` alongside the verdict —
one or two sentences each is enough; the point is that the human went on record.

| Gate after | Ask |
|---|---|
| 1 · Press release | "Which sentence are you least sure of?" · "Would a team reorganise a quarter around the subheading — honestly?" |
| 2 · FAQs | "Which blocker do you already suspect the answer to — and are you avoiding asking because of it?" · "Whose voice is missing from the internal bank?" |
| 3 · Demo | "Narrate the demo back to me in three sentences — where did you improvise?" · "What will the first viewer assume this includes that it doesn't?" |
| 4 · Docs | "Which section were you tempted to write around?" · "Is the getting-started section short because it's simple, or because it's incomplete?" |
| 5 · Telemetry | "Which metric would you quietly game if your bonus depended on it?" · "Which PR claim are you shipping unmeasured, and why is that acceptable?" |
| 6 · Requirements | "Which requirement do you want most — and does its source actually demand it, or merely permit it?" · "Which flagged item are you hoping nobody notices?" |
| 7 · Release plan | "If you could only ship R1, is it still worth doing?" · "Which blocked slice are you already mentally committing a date to?" |
| 8 · Readiness | "If this fails, which of the top three will it have been — and what did you do about it today?" · "Who sees this readiness doc, and what will they challenge first?" |

Push back (within the budget of 2) when an answer dodges — "none" and "nothing" usually
dodge. Record answers even when they're thin; a thin answer on the record is information.

## Recording format

```
GATE · Stage 1 · 2026-08-30
Q: Which sentence are you least sure of?
A: "The 60-second window — I picked it because it sounded right."
→ noted: ¶3's window is [ASSUMED]; carried to Q-15 (owner: platform lead)

CHALLENGE · unresolved · Stage 0 · challenge 6 of 6
I pushed: the customer is still "operations teams" with no segment.
User's last answer: "I'll narrow it after I see the FAQ."
→ recorded to QUESTIONS.md, owner: the user. Proceeding.
```
