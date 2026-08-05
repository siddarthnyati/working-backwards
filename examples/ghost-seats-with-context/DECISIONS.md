# Decisions — Ghost Seats (with context)

Stages 1 and 2 only. The dimension-4 review is reproduced beside the tier-0 version, because
that side-by-side is the entire argument for the context pack.

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
Substantive
  4 Strategic fit .............. Q-04 raised
  6 Falsifiability ............. Q-18, Q-19, Q-20 raised

VERDICT: PASS
```

**The draft-1 finding is identical to the tier-0 run.** A strategy document does not stop you
writing a press release with no rationale in it — it only lets the critic check the rationale
once you have written one. Absence is a presence check either way.

---

## Dimension 4, side by side

**Tier 0 — no context pack** *(from `examples/ghost-seats/DECISIONS.md`)*

```
Q-04 · The document describes the defect accurately and never says why the company should
       spend a quarter fixing it now rather than next year.
       I can see the rationale is absent. I cannot tell you what the right one is, and I have
       no strategy document to check a candidate against.
       Ask: your VP or strategy lead.
       Not evaluable from the document alone.
```

**Tier 1 — one strategy document**

```
CRITIC · Stage 1 · 01-press-release.md (revised) · 2026-08-05
  4 Strategic fit .............. cited, not adjudicated

`wb/context/2026-platform-strategy.md` names "trust and auditability" as the second of three
pillars for 2026, and states the commitment: "by the end of 2026, a customer should be able to
answer any question their auditor asks about our platform using artifacts they can generate
themselves." The rationale in ¶1 and ¶6 aligns with that line directly — the audit log is the
artifact, and it records an intention rather than an outcome.

The same document conflicts with the full scope. It states that roughly two-thirds of
engineering investment is weighted to self-serve automation and cost, and lists under "what we
are explicitly not doing in 2026": "anything that requires renegotiating the standard
integration agreement at scale, which is a 2027 conversation and needs partnerships to have an
owner first."

R3 requires per-integration membership reads. That is a change to what the integration
agreement requires of a partner.

So: aligned with the pillar, in conflict with the plan for delivering it. The document tells
you what to do with that — "a proposal that acknowledges the constraint and asks for an
exception is a conversation; one that ignores it is a rewrite."

I am citing and contrasting. I am not ruling. Whether the exception is available, and what it
displaces, is a decision for the document's owner.

→ Q-04 CLOSED — replaced by Q-04b
→ Q-04b · Is an exception to the 2027 integration-agreement constraint available this year,
  and what does it displace? · Ask: VP Platform · Cited, not adjudicated.
```

> **What actually improved.** Dimension 4 did not turn green — there is no green on a
> substantive dimension, and there never will be. What changed is the quality of the question:
> "does this match strategy?" became "the pillar says yes and the budget line says no, here
> are both sentences, which wins?"
>
> The first question needs a meeting to make progress. The second one *is* the meeting agenda.
>
> That conflict was invisible in the tier-0 run. Nothing in the problem, the press release, or
> the standard FAQ bank would have surfaced it. It came entirely from the document, and it
> would otherwise have surfaced in a review — which is the specific afternoon this method
> exists to prevent.

---

```
CRITIC · Stage 2 · 02-faq-{internal,regional}.md · 2026-08-05
Structural
  2 Evidence presence .......... PASS
  5 Traceability ............... PASS
  7 Clarity .................... PASS
  8 Template completeness ...... PASS
Substantive
  6 Falsifiability ............. Q-18, Q-19, Q-20 unchanged; Q-21 added

VERDICT: PASS

Note: three internal-FAQ answers moved to ANSWERED, citing the strategy document. One new
BLOCKER-tagged question (IFAQ-17) appeared that does not exist in the tier-0 run — the
integration-agreement conflict. The regional bank is byte-for-byte unchanged, because a
strategy document reaches none of it.

Blocker count: 6, both runs. Nothing a strategy document can do closes a legal, privacy,
regulatory, security or data question.
```

---

## The exchange rate, stated plainly

One two-page document, at Stages 1 and 2:

- Questions: 17 → 13 open. Four closed (Q-04, and three internal-FAQ answers), one added
  (Q-21), one sharpened (Q-04b replacing Q-04).
- Blockers: 6 → 6. None closed. One (BLK-05) now cited to a document that says the gap has
  already cost the company twice.
- One conflict found that the tier-0 run could not see.

Context does not reduce risk. It makes the risk specific, and it converts questions you would
have taken to a VP into questions you can answer yourself — which leaves the VP meeting for
the one question that actually needs them.
