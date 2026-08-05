# Decisions — Ghost Seats

Critic verdicts and overrides, in order. This log is what makes a decision defensible in a
review six months later.

Nine reviews. Three REVISE verdicts, one override, one revision made voluntarily on a PASS.

---

```
CRITIC · Stage 0 · 00-intake.md · 2026-08-05
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... PASS
  8 Template completeness ...... PASS

VERDICT: PASS
Note on dimension 1: "IT and workspace administrators at 200–5,000-seat B2B SaaS customers
with three or more integrations connected, subject to a periodic access review" is a segment
you could build a list from, and the intake says which two fields you would query. That is
the standard. An earlier phrasing — "admins who need better deprovisioning" — would have
been a role, not a segment, and would have blocked.
Note on dimension 2: four claims tagged [OBSERVED] with named sources, one [REPORTED] with a
role. Two [ASSUMED] and two [UNKNOWN] are declared rather than hidden, which is what this
dimension rewards.
```

---

```
CRITIC · Stage 1 · 01-press-release-draft1.md · 2026-08-05
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... PASS
  3 Alternative named .......... PASS
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive (questions, not verdicts → QUESTIONS.md)
  4 Strategic fit .............. Q-04 raised
  6 Falsifiability ............. Q-18, Q-19, Q-20 raised

VERDICT: PASS

Q-04, in full:
  The document describes the defect accurately and never says why the company should spend a
  quarter fixing it now rather than next year. ¶1 states what shipped. ¶6, whose job is the
  why-now, restates the subheading in different words — "deprovisioning should be verifiable,
  not assumed" is the product, not the reason to fund it.
  I can see the rationale is absent. I cannot tell you what the right one is, and I have no
  strategy document to check a candidate against.
  Ask: your VP or strategy lead.
  Not evaluable from the document alone.
```

```
REVISION ON A PASS · Stage 1 · 2026-08-05
The critic did not require this. The author revised in response to Q-04.

Author's note: "It passed. Every box was ticked and the document was still wrong in the way
that matters — I'd written an incident report with a launch date on it. The question was
correct and uncomfortable and I nearly clicked through it."

Changed: ¶1 gained the rationale. ¶6 was rewritten to carry the why-now.
Unchanged: everything else.
Both drafts are kept: 01-press-release-draft1.md and 01-press-release.md.

Q-04 remains OPEN. The revision supplied a rationale; nothing has confirmed it is the right
one. The critic has no more basis to judge the second version than the first.
```

```
CRITIC · Stage 1 · 01-press-release.md (revised) · 2026-08-05
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... PASS
  3 Alternative named .......... PASS
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive
  4 Strategic fit .............. Q-04 remains OPEN — rationale now stated, not adjudicated
  6 Falsifiability ............. Q-18, Q-19, Q-20 remain OPEN

VERDICT: PASS
Note: the sentence added to ¶1 is a claim about what customers believe. Stage 5 later found
it is also the one claim in the press release that no telemetry can reach. Recorded here
because the two findings are the same soft spot seen from different directions.
```

---

```
CRITIC · Stage 2 · 02-faq-{external,internal,regional}.md · 2026-08-05
Structural
  2 Evidence presence .......... PASS
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive
  6 Falsifiability ............. Q-01 … Q-17 raised across the three banks

VERDICT: PASS
Note: zero ANSWERED tags in the internal and regional banks. That is not a failure of the
artifact — it is the accurate consequence of a tier-0 run, and it is stated at the foot of
both files rather than papered over. Six blockers raised, all OPEN, all with owner roles.
An internal FAQ with no BLOCKER tags would have failed this review; this one is the opposite
problem and it is the honest one.
```

---

```
CRITIC · Stage 3 · 03-demo-spec.md · 2026-08-05
Structural
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... REVISE

VERDICT: REVISE
Instruction: The spec has no scope boundary. F1 shows an admin being told an integration
still has access, and a reader will assume they can act on it from there — the press release
does not promise that and EFAQ-02 says so explicitly. Add a "what this deliberately does not
show" section stating that Ghost Seats reports and does not remediate, and say why: forcing
a revocation into a third-party system needs write access and an agreed contract, which
BLK-05 has not established.
Resolution: section added. Re-reviewed → PASS.
```

---

```
CRITIC · Stage 4 · 04-docs.md · 2026-08-05
Structural
  3 Alternative named .......... PASS
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS

VERDICT: PASS
Note: two sections are recorded under "could not be written yet" rather than written around.
Under dimension 8, an explicit gap is complete and a TBD is not — these are explicit, each
names the blocker behind it, and one of them ("which of your integrations are covered")
is a question no earlier stage had been forced to answer. Writing the docs early earned its
place on that one.
```

---

```
CRITIC · Stage 5 · 05-telemetry.md · 2026-08-05
Structural
  2 Evidence presence .......... REVISE
  5 Traceability ............... PASS
  8 Template completeness ...... PASS

VERDICT: REVISE
Instruction: The north star and four of five input metrics carry [UNKNOWN] baselines and
[UNKNOWN] targets. A metric plan in which nothing is measured asserts a measurement
capability with nothing observed behind it. Either supply a baseline for RPR from existing
data, or state in the artifact that the baseline is not merely missing but unobtainable
before instrumentation exists — the dimension is satisfied by the second, and not by silence.
```

```
OVERRIDE · Stage 5 · dimension 2 (evidence presence) · 2026-08-05
Critic said: The north star and four of five input metrics carry [UNKNOWN] baselines and
[UNKNOWN] targets; a metric plan in which nothing is measured asserts a measurement
capability with nothing observed behind it.

User justification: "The critic is right by its own rule and wrong about this artifact. The
baseline is unknowable — there is no confirmation field today, so the propagation rate has
never been measured by anyone. Filling it in would mean inventing a figure, which is the one
thing this pipeline exists to stop. Every [UNKNOWN] here already carries the reason it is
unknown and the question that would resolve it. That is the finding, not a defect in the
document, and R1 exists precisely to turn it into an [OBSERVED]. Proceeding to Stage 6."

Proceeded to Stage 6. Not re-litigated.
```

> The override is the mechanism working, not failing. The critic applied its rule correctly;
> the user had context the rule does not encode; the disagreement is now on the record with
> both positions, and a reviewer in six months can see that the empty baselines were a
> decision rather than an omission.

---

```
CRITIC · Stage 6 · 06-requirements.md · 2026-08-05
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... PASS
  5 Traceability ............... REVISE
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive
  6 Falsifiability ............. Q-16 raised

VERDICT: REVISE
Instruction: REQ-DP9 ("force removal from the audit entry") cites nothing. Nothing above it
asks for it — PR ¶3 stops at reporting and EFAQ-02 states that boundary deliberately. Either
point it at a source, or move it out of the requirement set and into a flagged section, and
keep it out of the release plan. If you believe it belongs, the honest fix is upstream: add
remediation to the press release, re-run the Stage 1 critic, and let it flow down with a
source. That costs a re-review.
Resolution: moved to Flagged with "Source: NONE — FLAGGED, not customer-derived", excluded
from all release slices, and listed under Out of scope — candidates. Not deleted.
Re-reviewed → PASS.
```

> This is the scope-creep mechanism firing on the one requirement that everybody wants. It
> is the first thing anyone asks for after seeing the demo, and it has no customer source.
> The rule did not stop it being considered — it stopped it being scheduled.

---

```
CRITIC · Stage 7 · 07-release-plan.md · 2026-08-05
Structural
  5 Traceability ............... PASS
  8 Template completeness ...... PASS

VERDICT: PASS
Note: reconciliation passes — 11 of 12 requirements appear in exactly one slice, none in
two, and the twelfth (REQ-DP9) is declared as an orphan with a reason rather than dropped.
DAG is acyclic. Two of four slices are marked not schedulable, which is the correct output
of a plan sitting on six open blockers.
```

---

```
CRITIC · Stage 8 · 08-readiness.md · 2026-08-05
Structural
  2 Evidence presence .......... PASS
  5 Traceability ............... PASS
  8 Template completeness ...... PASS
Substantive
  6 Falsifiability ............. no new questions; Q-18, Q-19, Q-20 carried forward

VERDICT: PASS
Note on the recommendation: "GO WITH CONDITIONS, on R1 and R2 only" is supported by the
artifact — the two unblocked slices deliver the central claim for one integration and the
conditions are named. A recommendation of GO on the whole initiative would have failed this
review, because four of the six blockers are unanswered and three of them determine whether
R4 exists in its current shape.
```
