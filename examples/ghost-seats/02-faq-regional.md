# Regional FAQ — Ghost Seats

Jurisdictional questions. Named regulations are public law and appear here as categories.
Every entry produces a question and an owner role. No entry produces a compliance
conclusion — "we are compliant" is not a sentence this file can contain, and neither is the
opposite.

Two of the six blockers in this session surfaced here.

## Data protection

```
RFAQ-01 · GDPR-style regimes · BLOCKER
Q: When a controller instructs us to remove a user and we do not propagate that removal to a
   sub-processor, does the retained read access constitute a failure of our obligations as
   processor — and is it reportable?
A: Not evaluable here, and it is the highest-consequence unknown in the session. What can be
   stated from the document: the instruction was received, the local action was taken, the
   downstream action was not confirmed, and the record we gave the controller says it was.
   Whether that is a personal data breach under Article 4(12), whether the 72-hour clock
   applies, and whether the controller or we are the notifying party are all determinations
   for privacy counsel.
   → BLK-02 · PRIVACY · severity high · Owner role: privacy counsel / DPO · Status: OPEN
```

```
RFAQ-02 · GDPR-style regimes · BLOCKER
Q: If a data subject exercised erasure during one of these windows and we told the
   controller it was done, what is the position?
A: Same mechanism, worse facts: an erasure instruction has no more reason to propagate than
   a removal does, and unlike a removal, an erasure comes with a statement to the data
   subject. Whether any erasure requests actually fell in an affected window is unknown and
   depends on BLK-06.
   → BLK-02 · PRIVACY · severity high · Owner role: privacy counsel / DPO · Status: OPEN
```

```
RFAQ-03 · CCPA/CPRA-style regimes · OPEN
Q: Does retained access by a former workspace member touch the "sale" or "share"
   definitions, or the deletion-request obligations?
A: Deletion obligations plausibly; sale/share plausibly not, since nothing new is disclosed
   to a third party — the third party already had it and did not relinquish it. "Plausibly"
   is not a legal position and this needs counsel.
   → Q-01 · Ask: privacy counsel
```

```
RFAQ-04 · DPDPA-style regimes · OPEN
Q: Do consent-notice or data-principal-rights obligations in these regimes create a separate
   duty here, and does any of it require local-language notification?
A: Not evaluable here. Raised because these regimes have different notification mechanics
   from the GDPR-style ones and a single global answer to BLK-02 may not be portable.
   → Q-01 · Ask: privacy counsel
```

```
RFAQ-05 · Residency · OPEN
Q: The confirmation records are new data. Where are they stored, and does any customer's
   residency commitment constrain that?
A: The records are metadata — event, integration, outcome, timestamp — with no document
   content. That is a reason to expect this is simple and not a reason to assume it.
   → Q-17 · Ask: privacy counsel and platform engineering lead
```

## Sector rules and certification

```
RFAQ-06 · SOC 2 · BLOCKER
Q: Our SOC 2 report attests to logical access controls including timely revocation. Does the
   current behaviour mean we have been attesting to a control that does not operate as
   described — and if so, what is owed to the auditor and to customers holding that report?
A: Not evaluable here. What is stateable: the control as described covers revocation, the
   observed behaviour is that revocation does not always complete, and the evidence we would
   have produced to an auditor is the audit log — which records the local removal. Whether
   that is a control deficiency, whether it is material, and whether it requires disclosure
   at the next examination are determinations for the compliance owner.
   → BLK-04 · REGULATORY · severity high · Owner role: compliance lead / SOC 2 control
     owner · Status: OPEN
```

```
RFAQ-07 · Sector rules · OPEN
Q: Do any customers in regulated sectors — financial services, health, public sector,
   education — carry access-control obligations stricter than the general case?
A: Not evaluable here; there is no customer segmentation by sector in this session. Raised
   because a stricter subset would change severity rather than scope, and severity is what
   the readiness recommendation turns on.
   → Q-13 · Ask: compliance lead
```

## Operational and localisation

```
RFAQ-08 · Notification clocks · OPEN
Q: If notification is required, which clocks apply, when do they start, and who starts them?
A: Downstream of BLK-02 and BLK-03. Noted separately because the clock question has a
   different owner from the liability question and gets forgotten between them.
   → Q-01 · Ask: privacy counsel
```

---

*Tag counts: 5 OPEN · 3 BLOCKER · 0 ANSWERED*

*Blockers raised here: BLK-02, BLK-04*

*What a context pack would have changed: with the standard DPA and the current SOC 2 control
narrative in `wb/context/`, RFAQ-01 and RFAQ-06 would still route to counsel — that does not
change — but they would cite the specific clause and control number instead of describing
the shape of the question. The owner would get a five-minute question rather than a research
task.*
