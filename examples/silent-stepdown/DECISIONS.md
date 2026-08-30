# Decisions — Silent Step-Down

Verdicts in order. Two REVISE verdicts, both resolved by revision; no overrides in this run
(the ghost-seats example shows the override path).

---

```
CRITIC · Stage 0 · 00-intake.md · 2026-08-30
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... PASS
  8 Template completeness ...... PASS
VERDICT: PASS
Note: "merchants" alone would have failed dimension 1. The three-field list-of-ten query
(3DS enabled AND EEA volume AND recent fraud chargeback) is what a segment looks like.
```

---

```
CRITIC · Stage 1 · 01-press-release-draft1.md · 2026-08-30
Structural
  1 Customer specificity ....... PASS
  2 Evidence presence .......... PASS
  3 Alternative named .......... REVISE
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive
  4 Strategic fit .............. Q-16 raised
  6 Falsifiability ............. Q-01, Q-02, Q-03 raised

VERDICT: REVISE
Instruction: ¶4 reads "Merchants currently have no way to detect this happening." That is
the literal fail case for dimension 3 — there is always a current behaviour. Merchants DO
detect it: through chargeback reconciliation, months later, one lost dispute at a time.
Rewrite ¶4 to name that path and say precisely what fails about it — that it finds the
cost after it is paid, and only for the step-downs that attracted fraud. Naming the bad
alternative is what makes the switching argument; "no way" just makes the reader argue.
```

```
CRITIC · Stage 1 · 01-press-release.md (revised) · 2026-08-30
  3 Alternative named .......... PASS — ¶4 now names reconciliation and its failure mode
All other dimensions unchanged.
VERDICT: PASS
Note: "That is not monitoring; it is billing" is doing the work the draft's "no way"
claimed to do.
```

---

```
CRITIC · Stage 2 · 02-faq-{external,internal,regional}.md · 2026-08-30
Structural: 2 PASS · 5 PASS · 7 PASS · 8 PASS
Substantive: 6 → Q-04…Q-13 raised
VERDICT: PASS
Note: six blockers, all question-shaped, all with owners. IFAQ-09 is the honest one — it
names the initiative's internal tension (the silent fallback protects a metric we report).
An internal FAQ that skipped that question would have been written to be agreed with.
```

---

```
CRITIC · Stage 3 · 03-demo-spec.md · 2026-08-30
Structural: 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS
Note: F4 (policy service itself fails → recorded, never silent) is the spec refusing to
contain a copy of the defect it fixes. F5 promises detection flagging only — correctly
scoped to what BLK-03's unresolved state permits.
```

---

```
CRITIC · Stage 4 · 04-docs.md · 2026-08-30
Structural: 3 PASS · 5 PASS · 7 PASS · 8 PASS
VERDICT: PASS
Note: the require-exemption policy option is documented as not-writable, citing BLK-02.
A doc that cannot be written is a feature that cannot ship; the gap is the finding.
```

---

```
CRITIC · Stage 5 · 05-telemetry.md · 2026-08-30
Structural: 2 PASS · 5 PASS · 8 PASS
VERDICT: PASS
Note: contrast with ghost-seats — here the auth log already exists, so M1/M2 baselines are
[OBSERVED] and the artifact passes dimension 2 without an override. The chargeback-side
metrics are honestly [UNKNOWN] and gated on BLK-05 rather than estimated.
```

---

```
CRITIC · Stage 6 · 06-requirements.md · 2026-08-30
Structural: 1 PASS · 2 PASS · 5 PASS · 7 PASS · 8 PASS
Substantive: 6 → Q-04 carried onto REQ-D4
VERDICT: PASS
Note: the restitution mechanism was proposed as a requirement during drafting and does not
appear in the numbered set — it cannot cite a decision, only a wish. It sits in candidates
citing EFAQ-05/BLK-01, which is the correct disposition: visible, unscheduled, waiting on
its owner.
```

---

```
CRITIC · Stage 7 · 07-release-plan.md (first cut) · 2026-08-30
Structural
  5 Traceability ............... REVISE
  8 Template completeness ...... PASS
VERDICT: REVISE
Instruction: REQ-DP4 appears in both R2 and R3. A requirement in two slices means one of
them is not independently shippable — R2 was carrying the exemption flag so it could claim
"EEA-complete," which it cannot while BLK-02 is open. Move REQ-DP4 wholly into R3, let R2
ship visibility only, and let the reconciliation table say every requirement lands exactly
once.
Resolution: moved. Re-reviewed → PASS. Reconciliation: 9/9 requirements in exactly one
slice, no orphans, DAG acyclic.
```

---

```
CRITIC · Stage 8 · 08-readiness.md · 2026-08-30
Structural: 2 PASS · 5 PASS · 8 PASS
VERDICT: PASS
Note: GO WITH CONDITIONS on R1+R2 follows from the artifact — both are unblocked and
deliver ¶3's promise. A GO covering R3 would have failed: two open blockers shape what R3
even is.
```
