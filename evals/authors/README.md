# Author-prompt evals — where's the golden set?

There isn't a `golden.json` here, **by design** — and the reason is the
difference between testing a checker and testing a writer.

The judge evals (`evals/judge/`) need labelled answers because the judge's
output is a *verdict*, and a verdict is right or wrong only relative to a
human's call on the same snippet. So a human wrote 14 snippets and labelled
the correct verdict in advance: that's a golden set.

The authors' output is a *document* — different words every run, and that's
fine. A golden full-text answer would false-fail every valid rewrite. So the
answer key here is not a labelled output; it is the **stage's output
contract**, expressed as machine-checkable properties that must hold for
*any* valid output:

| The eval runs on | Where it lives |
|---|---|
| The **verbatim author prompts** — parsed out of `references/stage-prompts.md` at run time, never copied | the skill itself |
| **Frozen inputs** — the committed artifacts of `examples/surprise-charge/` (stage 1 gets the real intake, stage 7 gets the real requirements) | `examples/surprise-charge/` |
| **26 properties across 8 stages** — the contracts (¶-numbered paragraphs, every %-figure tagged, ≥1 blocker with an owner and none self-closed, the "does not show" boundary, `Source:` on every requirement, `RESTS ON ASSUMPTION` on the [ASSUMED] chain, full requirement coverage in the plan, sanctioned verdict vocabulary, no blocker closed by the model) | `run_author_evals.py` |

So the "golden set" equivalent is **inputs + contract**: frozen upstream
artifacts in, properties out. A property regression means the prompt stopped
producing its contract — exactly what a golden label catches for the judge.

Two modes:

```
python evals/authors/run_author_evals.py --check-committed
    # scores the committed example artifacts (no model calls).
    # This validates the PROPERTIES before trusting them: if the known-good
    # run fails a property, the property is wrong, not the run.
    # Baseline: 26/26.

python evals/authors/run_author_evals.py
    # generates a fresh artifact per stage via `claude -p` using the real
    # author prompt + frozen inputs, then scores the properties.
    # This is the regression gate for author-prompt edits.
```

What this layer does **not** catch, said plainly: quality regressions that
still tick the boxes — writing that got worse while keeping its tags and
sections. That is what the judge guards at runtime and what Layer 3
(outcome evals against human-approved full outputs) would measure offline.

Stage 0 (intake) is interactive — it needs a scripted human — and is out of
scope here; its behavior is exercised by the judge evals and the challenge
budget rules in `SKILL.md`.
