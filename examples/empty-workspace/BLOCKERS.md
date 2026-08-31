# Blockers — Empty Workspace

Questions with owners, never findings. All six OPEN; only the user changes Status.

| ID | Category | Sev | Ask (short) | Owner role | Blocks | Status |
|---|---|---|---|---|---|---|
| BLK-01 | PRIVACY | high | Lawful basis + retention for imported non-user contacts | privacy counsel | REQ-DP3, R4 | OPEN |
| BLK-02 | REGULATORY | high | Invite email: transactional or marketing, per market | compliance lead | REQ-DP3, R4 | OPEN |
| BLK-03 | DEPENDENCY | high | Who owns the onboarding surface — growth or product | VP Product | R2, R3 | OPEN |
| BLK-04 | DATA | high | Can current volume power the holdback experiment | data & analytics lead | REQ-D3, R4 | OPEN |
| BLK-05 | COMMERCIAL | medium | Invite incentives: value vs gaming vs margin giveaway | commercial lead | candidates only | OPEN |
| BLK-06 | SECURITY | medium | Address-book OAuth scope + token storage exposure | security lead | REQ-DP3, R4 | OPEN |

---

```
BLK-01 · PRIVACY · severity: high
Surfaced by: IFAQ-03, RFAQ-02
Ask: Importing an address book means holding personal data of people who never signed up.
     What is the lawful basis, how long may non-user contacts be retained, and can we
     honour a deletion request from someone who was never our user?
Owner role: privacy counsel
Blocks: REQ-DP3, R4
Status: OPEN
```

```
BLK-02 · REGULATORY · severity: high
Surfaced by: RFAQ-01
Ask: Is an invite email to a non-user a transactional message from the inviting user or
     marketing from us — under CAN-SPAM, CASL, and ePrivacy-style regimes — and what does
     each answer require of sender identity and footers, per market?
Owner role: compliance lead
Blocks: REQ-DP3, R4
Status: OPEN
```

```
BLK-03 · DEPENDENCY · severity: high
Surfaced by: IFAQ-01
Ask: Growth and product both claim the first-run surface, and the last collision shipped
     conflicting experiments. Who is the single owner of the onboarding surface and the
     activation number?
Owner role: VP Product
Blocks: R2, R3
Status: OPEN
```

```
BLK-04 · DATA · severity: high
Surfaced by: IFAQ-02
Ask: Does current signup volume give a day-30 holdback experiment acceptable power inside
     one quarter — and if not, what is the honest alternative design?
Owner role: data & analytics lead
Blocks: REQ-D3, R4
Status: OPEN
```

```
BLK-05 · COMMERCIAL · severity: medium
Surfaced by: IFAQ-05, EFAQ-05
Ask: Do invite incentives create teams or farm seats — and is discounting a behaviour that
     already correlates with retention just margin given away?
Owner role: commercial lead
Blocks: nothing shipping — candidates only
Status: OPEN
```

```
BLK-06 · SECURITY · severity: medium
Surfaced by: IFAQ-04
Ask: What does an attacker get from the address-book token store, and are we widening
     OAuth scope for a feature whose value rests on an [ASSUMED] claim?
Owner role: security lead
Blocks: REQ-DP3, R4
Status: OPEN
```

*Four high, two medium. BLK-03 is the quiet one that decides the schedule: it blocks the
two slices that need no lawyer — an ownership dispute, not a hard problem.*
