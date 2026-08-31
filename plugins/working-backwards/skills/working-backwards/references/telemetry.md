# Telemetry

Read this before Stage 5. Output: `05-telemetry.md`.

## The governing rule

**If the press release claims it, telemetry must be able to measure it — or the claim comes
out of the press release.** This stage runs *before* requirements precisely so that an
unmeasurable claim is caught while changing it is cheap.

## Required structure

1. **North star** — one metric. Precise, computable definition — one two people would
   implement identically. State which PR claim it measures, by paragraph number.
   - Guard the denominator: include the cases the system cannot see. A metric that excludes
     what it can't observe repeats the failure most of these initiatives exist to fix.
   - Guard against gaming: ask "what is the cheapest way to move this number without
     creating the value?" and put the defence in the definition (e.g. count members *who
     acted*, not members).
2. **Input metrics** — each tied to a specific PR claim, each with: definition, baseline,
   target, instrumentation point, and whether that point exists today.
3. **Instrumentation table** — the events, their fields, owner role, exists-today status.
   Four of five points not existing is a finding about the discovery work, not a formatting
   problem; say it plainly.
4. **Claims we cannot currently measure** — one row per claim, and each row is a decision
   forced on the user: *instrument it, or cut the claim*. Deciding neither is deciding to
   ship an unverifiable promise.
5. **Questions raised** — targets and thresholds route to owners.

## Baselines and targets

- A baseline you do not have is `[UNKNOWN]`, never an estimate. If the baseline is not
  merely missing but *unobtainable before instrumentation exists*, say that explicitly —
  the distinction is what separates an honest gap from a lazy one, and it is what the
  critic will probe.
- A target set before its baseline exists is an invented figure with a deadline attached.
  Route it to an owner as a question instead.
- Watch for metrics whose success direction is counter-intuitive (an error-visibility rate
  whose baseline is zero *for the wrong reason* should go up). Label these, or the first
  dashboard reader will page someone about an improvement.

## What the critic checks here

Dimensions 2, 5, 8. Dimension 2 is the sharp one: an artifact full of `[UNKNOWN]`s passes
only when each one carries the reason it is unknown and the question that resolves it — and
fails when an unknown was papered over with a plausible number. Expect REVISE when baselines
are empty and unexplained; expect the user to override when they are empty *because the
world has never measured them* — both outcomes are the mechanism working.
