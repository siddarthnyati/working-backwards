# Regional FAQ — Silent Step-Down

Jurisdictional questions. Regulations appear as public categories; every entry produces a
question and an owner, never a compliance conclusion.

```
RFAQ-01 · EEA / PSD2 SCA · BLOCKER
Q: Under PSD2 strong customer authentication, an EEA transaction processed without
   authentication generally requires an exemption to be claimed. When we stepped down
   silently, no exemption was claimed. Whose compliance failure is that — ours, the
   acquirer's, the merchant's — and is it reportable to anyone?
A: Not evaluable here, and it is the highest-consequence question in the session. What is
   stateable: the transactions exist [OBSERVED], no exemption flag was applied [OBSERVED:
   the code path sends none], and SCA obligations sit somewhere in the chain.
   → BLK-02 · REGULATORY · severity high · Owner role: compliance lead · Status: OPEN
```

```
RFAQ-02 · EEA · OPEN
Q: If step-down continues as a merchant-chosen policy, must the exemption flag be applied
   going forward — and which exemption?
A: Downstream of BLK-02; shapes REQ-DP4 directly. → Q-11 · Ask: compliance lead
```

```
RFAQ-03 · Other markets · OPEN
Q: Markets with their own authentication mandates — do any prohibit processing on timeout
   outright, making "allow step-down" not offerable there?
A: Not evaluable without the market list. Policy availability may be jurisdictional, which
   changes the settings design from a toggle to a matrix.
   → Q-12 · Ask: compliance lead
```

```
RFAQ-04 · Data residency · OPEN
Q: The new authentication-outcome records are metadata. Does any residency commitment
   constrain where they are stored?
A: Expected simple; not assumed simple. → Q-13 · Ask: privacy counsel
```

---

*Tag counts: 3 OPEN · 1 BLOCKER · 0 ANSWERED*
*Blocker raised here: BLK-02*
