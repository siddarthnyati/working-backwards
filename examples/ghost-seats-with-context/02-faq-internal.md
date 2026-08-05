# Internal FAQ — Ghost Seats (with context)

Only the entries that changed are reproduced. Everything else is identical to
`examples/ghost-seats/02-faq-internal.md`.

Three answers moved from `OPEN` to `ANSWERED`. One moved in the other direction: it got
worse, and that is the more interesting result.

---

## Changed: now ANSWERED

```
IFAQ-03 · Finance · ANSWERED
Q: What are we not doing instead?
A: `wb/context/2026-platform-strategy.md` states the ratio directly: roughly two-thirds of
   engineering investment is weighted to self-serve automation and cost, with the remaining
   third across pillars 1 and 2. Ghost Seats competes inside the third. The document also
   says work needing changes to the integration agreement "does not fit this year as
   written," which is exactly what R3 needs.
   So: this displaces other pillar-2 work, and the full-coverage half of it displaces a 2027
   commitment. The proposal has to say what it displaces — the strategy document says so
   explicitly under "how to argue with this document."
```

*Tier-0 version: `OPEN` → Q-08 · Ask: your VP. The question was right and it took a meeting.*

```
IFAQ-02 · Finance · ANSWERED (partially)
Q: What revenue does this protect, and how would we know?
A: The document names the mechanism without quantifying it: deals above 500 seats stall in
   security review, on "a request for evidence we can produce but cannot produce quickly."
   Ghost Seats produces exactly that evidence for one common question. It does not say how
   many deals or how much revenue, so the size is still unknown.
   The `[ASSUMED]` claim C7 — that most affected customers have never discovered this — is
   untouched by this document and still propagates into REQ-DP5.
   → Q-08 remains, narrowed: not "what revenue," but "how many stalled deals cited access
     evidence." · Ask: enterprise renewals lead
```

```
IFAQ-16 · GTM · ANSWERED
Q: Does the launch communication say this was broken?
A: The strategy document's pillar 2 includes "honest limits stated up front rather than
   discovered in a questionnaire." That is a stated principle and it applies to us as
   directly as to a customer's auditor. It does not answer the legal question in IFAQ-05 —
   whether saying so constitutes an admission — but it settles the default posture and puts
   the burden on legal to argue against disclosure rather than on product to argue for it.
   → Q-11 remains for the legal determination · Ask: legal counsel
```

## Changed: got worse

```
IFAQ-10 · Engineering · BLOCKER (unchanged status, stronger evidence)
Q: Who owns the integration contract — platform or partnerships?
A: The FAQ surfaced no clear answer in the tier-0 run and the strategy document confirms
   there isn't one. Under "known gaps in this document": *no ownership map for the
   integration layer. Platform and partnerships have overlapping claims and this has cost us
   twice.*
   The gap is now cited rather than inferred, and the document says it has already caused
   damage twice. BLK-05 does not close — a document naming a gap is not an owner — but it is
   considerably harder to wave away in a review.
   → BLK-05 · DEPENDENCY · severity high · Owner role: still unassigned. The strategy
     document escalates this rather than resolving it. · Status: OPEN
```

```
IFAQ-17 · Engineering · BLOCKER (new — surfaced only because the document exists)
Q: R3 requires per-integration membership reads, which means changing what the integration
   agreement requires of a partner. The strategy document says that is a 2027 conversation
   and needs partnerships to have an owner first. Are we proposing to break the plan?
A: Not evaluable here. What is stateable: the full-coverage half of this initiative requires
   the thing the strategy document defers, and the document tells you what to do about it —
   acknowledge the constraint and ask for an exception, rather than discovering it in review.
   This question does not exist in the tier-0 run. Nothing in the problem, the press release
   or the FAQ bank would have produced it. It came entirely from the document.
   → BLK-05 · DEPENDENCY · severity high · Status: OPEN
   → Q-21 · Is an exception available this year, and what does it displace? · Ask: VP Platform
```

---

*The point of IFAQ-17: context does not only close questions. It opens the ones that were
always there and invisible. A conflict you can name in a proposal is a conversation; the same
conflict discovered in a review is a rewrite.*

*Tag counts, this run: 3 ANSWERED · 7 OPEN · 7 BLOCKER*
*Blockers: same six. BLK-05 now cited to a document rather than inferred from silence.*
