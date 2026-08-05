# Questions — Ghost Seats

Output of the substantive critic dimensions (4 · strategic fit, 6 · falsifiability) and of
every FAQ answer that could not be answered from the document alone.

This file is the deliverable. It is the list you take to the six people who hold the context,
and it is what the session produced that a blank JIRA epic would not have.

**20 open · 2 with no owner assigned.**

| ID | Stage | Question | Ask | Status |
|---|---|---|---|---|
| Q-01 | 2 | Do CCPA/CPRA and DPDPA-style regimes create separate duties, and which notification clocks apply? | privacy counsel | OPEN |
| Q-02 | 2, 3 | How do we distinguish an integration outage from a propagation failure, from our side? | platform engineering lead | OPEN |
| Q-03 | 2 | Does the confirmation mechanism reduce or expand attack surface? | security lead | OPEN |
| Q-04 | 1 | Does the stated rationale match current strategy? | VP / strategy lead | OPEN |
| Q-05 | 2 | Does this cover integrations customers built themselves against our API? | platform engineering lead | OPEN |
| Q-06 | 2 | What does a confirmation round-trip cost per event, at volume? | platform engineering lead | OPEN |
| Q-07 | 2 | Is this included in the plan, or priced? | pricing lead | OPEN |
| Q-08 | 2, 6 | Is there any evidence a customer already knows about this? | enterprise renewals lead, support lead | OPEN |
| Q-09 | 2, 5 | Is there historical data from which a retroactive baseline could be computed? | platform engineering lead | OPEN |
| Q-10 | 5 | Can we obtain — and should we want — evidence of what removed users actually accessed? | partnerships lead, privacy counsel | OPEN |
| Q-11 | 2 | Does shipping a confirmation mechanism constitute an admission, and what does launch comms say? | legal counsel | OPEN |
| Q-12 | 2 | What does support tell a customer who calls asking whether they were affected? | support lead | OPEN |
| Q-13 | 2 | Do regulated-sector customers carry stricter access-control obligations? | compliance lead | OPEN |
| Q-14 | 3 | Is a permanent `unverifiable` state acceptable for an integration, or does it disqualify it? | partnerships lead | OPEN |
| Q-15 | 5 | What is an acceptable propagation rate, and who decides? | platform engineering lead, VP | OPEN |
| Q-16 | 6 | What is each integration's actual cache retention? | platform engineering lead, partnerships lead | OPEN |
| Q-17 | 2 | Where are confirmation records stored, and does any residency commitment constrain it? | privacy counsel, platform engineering lead | OPEN |
| Q-18 | 1 | Must-be-true: are propagation failures detectable platform-side without polling each integration? | platform engineering lead | OPEN |
| Q-19 | 1 | Must-be-true: will admins act on an incomplete state when they see one? | **no owner identified** | OPEN |
| Q-20 | 1 | Must-be-true: is a 60-second window achievable across systems we do not control? | **no owner identified** | OPEN |

---

## From the critic — dimension 4 (strategic fit)

```
Q-04 · Does "we sell an audit log as evidence, and it recorded an intention rather than an
       outcome" match the current strategy, and is this the right quarter for it?
Raised by: dimension 4 at Stage 1
Ask: your VP or strategy lead
Why it isn't evaluable here: no strategy or vision document was supplied. On draft 1 the
  rationale was absent and I could see that — absence is a presence check. On the revision the
  rationale is present, and whether it is the right one is not something a document can tell
  me. I can confirm it is stated. I cannot confirm it is true.
Affects: PR ¶1, PR ¶6 — and, downstream, whether this is funded at all
Status: OPEN
```

## From the critic — dimension 6 (falsifiability)

Three claims in the press release have to be true for it to hold. None of them is checkable
from the document.

```
Q-18 · For the central claim to work, propagation failures must be detectable from the
       platform side without polling each integration on a schedule. Is that true of all
       currently connected integrations?
Raised by: dimension 6 at Stage 1
Ask: platform engineering lead
Why it isn't evaluable here: I have not seen the integration contracts, the codebase, or the
  latency profile. Asserting feasibility here would be decoration.
Affects: PR ¶3, REQ-D1, REQ-D3, R1, R3
Status: OPEN
```

```
Q-19 · For the incomplete state to matter, admins must act on it when shown. Is there any
       evidence that admins act on existing warnings in this surface?
Raised by: dimension 6 at Stage 1
Ask: no owner identified — support or design research would be the guess, and a guess at an
  owner is worse than saying so
Why it isn't evaluable here: this is a behavioural claim about a population I have no data on.
Affects: PR ¶3, REQ-DP1, REQ-DP2, R2
Status: OPEN
```

```
Q-20 · For the subheading to hold, 60 seconds must be achievable across systems we do not
       control. What is the current response profile of the connected integrations?
Raised by: dimension 6 at Stage 1
Ask: no owner identified — platform engineering could measure it, but whether an integration
  is contractually obliged to meet a latency target is a partnerships question and the owner
  depends on which of those the answer turns out to be
Why it isn't evaluable here: no latency data, no integration contracts.
Affects: subheading, PR ¶3, M1, R3
Status: OPEN
```

---

## Questions with no owner

**Q-19 and Q-20.**

An unowned question is its own finding, and both of these sit under load-bearing sentences —
the subheading and the central promise of ¶3. `08-readiness.md` names them, and the honest
first action out of this session is to assign them rather than to answer them.

The reason they are unowned is worth stating: with an ownership map in `wb/context/`, both
would have resolved to a team. This is one of the concrete costs of the tier-0 run.

---

## What a context pack would have closed

Of the 20 questions here, roughly six would not have needed asking:

| Question | Closed by |
|---|---|
| Q-04 | a strategy or vision doc — dimension 4 would cite a line instead of asking |
| Q-06, Q-15 | metric definitions and baselines |
| Q-09 | a telemetry export |
| Q-16 | integration documentation or prior post-mortems |
| Q-19, Q-20 | an ownership map — these would at least have owners |

The other fourteen are questions for humans regardless of how much documentation exists,
which is the honest shape of this stage: context makes the list shorter and sharper. It does
not make it empty.
