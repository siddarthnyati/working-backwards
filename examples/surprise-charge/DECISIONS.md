# Decisions — The Surprise Charge

The first run under the interrogation protocol: challenge log at intake, gate questions
at every stage. One REVISE, resolved; no overrides.

---

```
CRITIC · Stage 0 · 00-intake.md · 2026-08-31
Structural: 1 PASS · 2 PASS · 8 PASS
VERDICT: PASS
Note: the interrogation did the work before the judge arrived — the verbatim first
statement was a feature request ("we need reminder emails"); four challenges later the
problem is an observed cohort with a kill condition. Challenges 5–6 unused.
```

```
GATE · Stage 0
Q: Is the customer a list-of-ten yet?
A: "Yes — billing join × last-activity date. I can pull the actual list."
```

---

```
CRITIC · Stage 1 · 01-press-release-draft1.md · 2026-08-31
Structural
  1 Customer specificity ....... REVISE
  2 Evidence presence .......... PASS
  3 Alternative named .......... PASS
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive: 4 → Q-04 · 6 → Q-01, Q-02

VERDICT: REVISE
Instruction: ¶2 opens "Everyone hates surprise charges." Everyone is not a customer — the
intake already did this work and the press release threw it away. Rewrite ¶2 around the
forgot-cohort (stopped opening by day 3, charged on day 14), with its numbers and their
tags. The narrower the person, the sharper the paragraph.
```

```
CRITIC · Stage 1 · 01-press-release.md (revised) · 2026-08-31
  1 Customer specificity ....... PASS — ¶2 now names the cohort and its three observed numbers
VERDICT: PASS
```

```
GATE · Stage 1
Q: Which sentence are you least sure of?
A: "'Cancelling takes one tap' — some markets may prescribe more steps." → carried to Q-02/BLK-02.
Q: Would a team reorganise a quarter around the subheading?
A: "Support would. Finance wouldn't — which is why REQ-D2 exists."
```

---

```
CRITIC · Stage 2 · FAQs · 2026-08-31
Structural: 2 PASS · 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS
Note: IFAQ-01 is the honest one — it puts the finance disagreement on the record as the
project's actual content, instead of hiding it in hallway conversations.
```

```
GATE · Stage 2
Q: Which blocker do you already suspect the answer to — and are you avoiding asking?
A: "BLK-02. I suspect some markets already require this notice, which makes us late, not
   generous. Asking anyway is the point."
```

---

```
CRITIC · Stage 3 · 03-demo-spec.md · 2026-08-31
Structural: 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS
Note: F5 (a failed reminder send never silently suppresses or excuses the charge) is the
spec refusing to create a new silent failure while fixing an old one.
```

```
GATE · Stage 3
Q: What will viewers assume this includes that it doesn't?
A: "A win-back discount in the cancel flow. It's excluded and the boundary section says so."
```

---

```
CRITIC · Stage 4 · 04-docs.md · 2026-08-31
Structural: 3 PASS · 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS — the past-charges answer is honestly unwritable (BLK-03) and says so.
```

---

```
CRITIC · Stage 5 · 05-telemetry.md · 2026-08-31
Structural: 2 PASS · 5 PASS · 8 PASS
VERDICT: PASS
```

```
GATE · Stage 5
Q: Which metric would you quietly game if your bonus depended on it?
A: "Reminder open rate — send at 9am Tuesday and call it engagement." → the north star
   counts surprises, not opens, because of this answer.
Q: Which PR claim ships unmeasured?
A: "C6 — reviews hurting conversion. It's out of the launch narrative entirely."
```

---

```
CRITIC · Stage 6 · 06-requirements.md · 2026-08-31
Structural: 1 PASS · 2 PASS · 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS
```

```
GATE · Stage 6
Q: Which requirement do you want most — does its source demand it, or merely permit it?
A: "The win-back discount. Nothing upstream demands it. It went to candidates, and I'm
   a little annoyed, which probably means the rule is working."
```

---

```
CRITIC · Stage 7 · 07-release-plan.md · 2026-08-31
Structural: 5 PASS · 8 PASS
VERDICT: PASS — 7/7 requirements in exactly one slice; two slices start today.
```

```
GATE · Stage 7
Q: If you could only ship R1, is it still worth doing?
A: "Yes — the baseline alone changes the finance conversation from beliefs to numbers."
```

---

```
CRITIC · Stage 8 · 08-readiness.md · 2026-08-31
Structural: 2 PASS · 5 PASS · 8 PASS
VERDICT: PASS
```

```
GATE · Stage 8
Q: If this fails, which of the top three will it have been?
A: "Finance never agrees to the experiment and R3 dies in a meeting loop. Which is why
   the ask is one co-design meeting, not approval of my beliefs."
```
