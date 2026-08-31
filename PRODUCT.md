# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Existing codebase: static HTML/CSS/vanilla JS, single file (`docs/index.html`), no build step, no framework. Served as-is via GitHub Pages from the `docs/` folder on `main`.

## Users

Primary: product managers and product leads evaluating whether to bring a structured, judge-gated Working Backwards process into their team's workflow. They are skeptical by default — the page has to earn trust in the rigor of the method before they will try it, not just explain what it does.

Secondary: individual builders using Claude Code who want a repeatable discovery workflow for their own projects; a broader AI-tooling audience discovering the skill on GitHub.

## Product Purpose

An open Claude Skill that runs Amazon's Working Backwards PR/FAQ method end to end — not just the press release, but all nine stages (press release, FAQs, demo spec, docs, telemetry, requirements, release plan, readiness) — with an LLM acting as judge to gate each stage before the next unlocks. Success is a PM or builder trusting the output enough to run it on a real initiative.

## Positioning

Amazon's public PR/FAQ method stops at the press release: it decides whether to build, then hands off to a blank ticket. This skill is an independent, open implementation of the public method that continues past that handoff — adding a judge gate (PASS/REVISE/BLOCK across 8 fixed dimensions, with 2 dimensions barred from ruling and routed to a named human instead), inline provenance tagging on every claim (`[OBSERVED]`/`[REPORTED]`/`[ASSUMED]`/`[NEEDS EVIDENCE]`), and the requirements/release-plan stages that turn narrative into engineer-ready, source-cited work. Not affiliated with or endorsed by Amazon.

## Operating Context

The site's central artifact is a real, worked example ("Empty Workspace" — a fictional team-collaboration SaaS) run through all nine stages, with the skill's actual output embedded: real prompts, real judge verdicts, real blockers, real confidence stats. A companion "with context" run demonstrates what supplying strategy/ownership/legal docs changes (and, pointedly, does not change — blockers stay open regardless). The skill itself lives in `plugins/working-backwards/skills/working-backwards/`; the site is documentation/demonstration, not the product surface itself.

## Capabilities and Constraints

- Nine-stage pipeline: Intake, Press release, FAQs, Demo spec, Docs, Telemetry, Requirements, Release plan, Readiness.
- Three run modes: Full (4–8 hrs, all 9 stages), Targeted (2–3 hrs, skips 3/4/8), Lightweight (<1 hr, skips 3/4/5/7/8).
- LLM-as-judge scores 8 fixed dimensions; 6 produce real verdicts, 2 (strategic fit, feasibility) only ever produce questions routed to a named human.
- Every requirement carries a `Source:` line citing the paragraph it came from.
- Install paths: Claude Code plugin marketplace, manual skill copy, or `.skill` upload to Claude.ai.
- No backend, no analytics, no network calls from the page itself (the context-builder widget explicitly reads only file *names*, nothing is uploaded).

## Brand Commitments

- Name: "Working Backwards" (the skill/repo name — this is the product's actual identity, not a generic label).
- Legal: must retain the "not affiliated with or endorsed by Amazon" disclaimer and MIT license mention.
- Voice, already established in the copy and not up for reinterpretation in this pass: terse, declarative, anti-hype — the page argues *against* narrative admiration and for citation/evidence, so its own claims stay plainly stated and precisely hedged (no marketing superlatives).
- GitHub repo: `github.com/siddarthnyati/working-backwards` (public, real).

## Evidence on Hand

Real, not to be treated as placeholder: the Empty Workspace example (`examples/empty-workspace/`), all nine stage prompts (`stage-prompts.md`), the six real blockers (BLK-01–06) with owners and severities, the real CONFIDENCE.md output, the ghost-seats-with-context before/after study. No testimonials, pricing, or usage metrics exist and none should be implied.

## Product Principles

1. Every claim on the page traces to something real in the repo — no invented stats, testimonials, or logos.
2. The design should demonstrate the method's own values (evidence, honesty about gaps, no overclaiming) rather than just describe them — form should not contradict content.
3. A skeptical PM's trust is earned through legibility of the real artifacts (prompts, verdicts, blockers), not through polish alone.
4. Install and "walk a real run" must stay effortless to find — this is a page whose job is to get someone to actually try the skill, not just admire it.

## Accessibility & Inclusion

No product-specific requirement established beyond standard web accessibility (keyboard operability, contrast, reduced-motion support) — already a live constraint on this page given its interactive carousel and judge-verdict UI.
