---
name: Working Backwards
description: A judge-gated PR/FAQ pipeline presented as its own code review.
colors:
  merge-blue: "#4c8eff"
  merge-blue-hover: "#3a7bef"
  on-accent: "#ffffff"
  merge-blue-soft: "#16233d"
  merge-blue-ink: "#8ab4ff"
  terminal-black: "#0d1117"
  panel-charcoal: "#161b22"
  elevated-charcoal: "#1c2129"
  diff-white: "#e6edf3"
  comment-gray: "#9198a1"
  muted-label-gray: "#7d8590"
  hairline-border: "#313842"
  diff-add-green: "#3fb950"
  diff-add-green-soft: "#12261a"
  review-amber: "#d29922"
  review-amber-soft: "#2b2210"
  diff-remove-red: "#f85149"
  diff-remove-red-soft: "#2d1214"
typography:
  display:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(2.2rem, 5.6vw, 3.9rem)"
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: "-0.022em"
  base:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  headline-clamp:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.8rem, 4vw, 2.6rem)"
    fontWeight: 400
  emphasis:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.98rem"
    fontWeight: 400
  numeral:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "1.5rem"
    fontWeight: 400
  subpage-display:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(2rem, 5vw, 3.2rem)"
    fontWeight: 400
  subpage-headline:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.7rem"
    fontWeight: 400
  subpage-title:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 400
  doc-h1:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.28rem"
    fontWeight: 500
    letterSpacing: "-0.01em"
  headline:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.22rem"
    fontWeight: 400
  lede:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.1rem"
    fontWeight: 400
  lede-featured:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.02rem"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.6
  caption:
    fontFamily: "Hanken Grotesk, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.85rem"
    fontWeight: 400
  label-small:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.78rem"
    fontWeight: 500
  label:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.72rem"
    fontWeight: 500
    letterSpacing: "0.05em"
  label-micro:
    fontFamily: "JetBrains Mono, ui-monospace, SF Mono, Menlo, Consolas, monospace"
    fontSize: "0.65rem"
    fontWeight: 500
    letterSpacing: "0.06em"
rounded:
  panel: "6px"
  pill: "999px"
  sharp: "0px"
spacing:
  section: "4rem"
  panel: "1.2rem"
components:
  button-primary:
    backgroundColor: "{colors.merge-blue}"
    textColor: "#ffffff"
    rounded: "{rounded.panel}"
    padding: "0.6rem 1.1rem"
  button-primary-hover:
    backgroundColor: "#3a7bef"
  button-secondary:
    backgroundColor: "{colors.panel-charcoal}"
    textColor: "{colors.diff-white}"
    rounded: "{rounded.panel}"
    padding: "0.6rem 1.1rem"
  status-pill-pass:
    backgroundColor: "{colors.diff-add-green-soft}"
    textColor: "{colors.diff-add-green}"
    rounded: "{rounded.pill}"
  status-pill-revise:
    backgroundColor: "{colors.review-amber-soft}"
    textColor: "{colors.review-amber}"
    rounded: "{rounded.pill}"
  status-pill-block:
    backgroundColor: "{colors.diff-remove-red-soft}"
    textColor: "{colors.diff-remove-red}"
    rounded: "{rounded.pill}"
---

# Design System: Working Backwards

## Overview

**Creative North Star: "The Review Queue"**

The product's real mechanic — draft, judge, PASS / REVISE / BLOCK, merge — already is a pull request review, so the page borrows that grammar wholesale instead of describing it in prose. The press release renders as a diff against nothing (every line an addition), the judge's scoring sits in a docked review panel, and every verdict throughout the site is a status pill in exactly three colors, never more. This is a near-black editor world: flat, dense, unapologetically a tool rather than a brochure. It replaced two prior visual identities built earlier in the project's life — a warm cream-paper editorial page, and a cooler "case file with ink stamps" redesign — both rejected by the user as the wrong layout and color scheme.

**Key Characteristics:**
- Near-black editor ground with a single blue accent reserved for links, primary actions, and "you are here" state — never for semantic verdicts.
- Exactly three semantic colors (green/amber/red) carry every PASS/REVISE/BLOCK, ASSUMED/OBSERVED/UNKNOWN, and blocker-severity signal on the page. They are never reused decoratively.
- JetBrains Mono for anything that is data, a label, or a citation; Hanken Grotesk for anything meant to be read as prose.
- Flat elevation — no drop shadows. Depth is three steps of background lightness (ground → panel → elevated panel), matching how real dark code-editor UIs actually work.

## Colors

Three functional families plus one accent: nothing on this page is colored for decoration.

### Primary
- **Merge Blue** (#4c8eff): the one non-semantic accent. Used only for links, primary CTA fill, the "you are here" state on tabs/toggles, and citation highlights (`Source:` lines, requirement-to-paragraph tracing). Never used for a verdict.

### Neutral
- **Terminal Black** (#0d1117): page ground.
- **Panel Charcoal** (#161b22): first elevation step — side columns, table headers, code blocks, the repo-bar strip.
- **Elevated Charcoal** (#1c2129): second elevation step — the deepest recessed panel (skip-note, UI mockup chrome).
- **Diff White** (#e6edf3): primary text.
- **Comment Gray** (#9198a1): secondary/body prose inside cards and notes.
- **Muted Label Gray** (#7d8590): tertiary — mono captions, table headers, tab labels. Deliberately lightened once already this project after measuring below 4.5:1 contrast on the ground color; re-check before darkening it again.
- **Hairline Border** (#313842): every 1px rule and panel border.

### Named Rules
**The Three-Color Verdict Rule.** PASS/OK/added is always Diff Add Green. REVISE/ASSUMED is always Review Amber. BLOCK/UNKNOWN/blocker-severity is always Diff Remove Red. These three never decorate anything that isn't a verdict, a provenance tag, or a blocking state — reusing them elsewhere would make an actual verdict harder to spot at a glance.

**The One Accent Rule.** Merge Blue is the only non-semantic color on the page. If something needs "brand" treatment rather than a status treatment, it is blue or it is neutral — never a fourth hue.

## Typography

**Display Font:** Hanken Grotesk (with -apple-system, Segoe UI, sans-serif fallback)
**Body Font:** Hanken Grotesk (same family, lighter weight)
**Label/Mono Font:** JetBrains Mono (with ui-monospace, SF Mono, Menlo, Consolas fallback)

**Character:** A grotesque/monospace pairing borrowed directly from developer-tool typography — Hanken Grotesk carries every sentence a visitor actually reads; JetBrains Mono is reserved for anything that is literally data (stage IDs, provenance tags, verdict pills, code, commands, file paths). The split is functional, not decorative: if you're reading it, it's Hanken; if you're citing or copying it, it's JetBrains Mono.

### Hierarchy
- **Display** (500 weight, `clamp(2.2rem, 5.6vw, 3.9rem)`, 1.08 line-height): the H1 only.
- **Headline** (400 weight, `clamp(1.8rem, 4vw, 2.6rem)`): section H2s. `h3` uses a fixed 1.22rem step below the H2 clamp.
- **Lede** (400 weight, 1.1rem): the one-line section intro directly under an H2, and the hero's `.diffline` prose at 1.02rem.
- **Body** (400 weight, 0.9rem, 1.6 line-height): running prose inside components — `.para`, `.src-para`, table cells, blockquotes, slot text.
- **Caption** (400 weight, 0.85rem): compact secondary text inside cards and panels — `.note`, `.gatenote`, `.step p`, `.card .ask`, `.req .rst`, the footer.
- **Label — small** (500 weight, 0.72rem, mono, 0.05–.1em tracking): UI chrome text that reads as a short phrase rather than a single tag — buttons, nav tabs, the prompt box, verdict lines, code blocks.
- **Label — micro** (500 weight, 0.65rem, mono, 0.04–.1em tracking, uppercase where used): the smallest tier — provenance tags, table headers, blocker categories, chips, pills.

### Sub-page Hierarchy
`mechanics.html` (a Read-mode reference page, not the Persuade-mode landing page) runs its own smaller heading scale — Display `clamp(2rem, 5vw, 3.2rem)`, Headline `1.7rem`, Title `1.15rem` — appropriately quieter than the hero-scale landing page since a reference page's job is comprehension, not conversion. Everything below Display (body, caption, label tiers, and the full color system) is shared identically across both pages.

### Type Scale
The full scale, smallest to largest, consolidated from a fragmented 24-value set during a 2026-08-30 audit: **0.65rem → 0.72rem → 0.78rem → 0.85rem → 0.9rem → 1.02rem → 1.1rem → 1.22rem**, plus the responsive `clamp()` display step and two decorative numerals (`.step .num` 1.5rem, `.stage .n` 1.05rem) that sit outside the reading hierarchy on purpose.

### Named Rules
**The Legibility-Over-Decoration Rule.** Monospace is used because content is genuinely data (diffs, IDs, code, citations) — never as a "technical-looking" costume on ordinary prose.

**The One-Step Rule.** No two components within 0.03rem of each other on the type scale — if a new size is needed, round to the nearest existing step rather than adding a new one. This scale was consolidated from 24 near-duplicate values down to 8 real steps; don't let it drift back.

## Layout

Single reading column at `max-width: 76rem`, `1.5rem` side padding. Sections stack with `4rem` vertical padding and a hairline top border between them (`3.2rem` on mobile, `≤960px` breakpoint). The stage carousel is the one dense grid moment: a 3-column `prompt / artifact / judge` layout at desktop, collapsing to a single stacked column on mobile. Card-grid components (blockers, install methods) use a collapsed-border grid (shared 1px borders between cells, no gap) rather than gapped cards with individual shadows.

## Elevation & Depth

Flat by design — no drop shadows anywhere except the diff-gutter markers' bordered left edge. Depth reads through three background-lightness steps (Terminal Black → Panel Charcoal → Elevated Charcoal), matching real dark-mode editor UIs, which don't shadow panels either. The one shadow this system used to have (a hard `4px 4px 0` offset on UI-mockup cards, inherited from an earlier visual identity) was removed during this build — it read as a physical-paper costume this world doesn't wear.

### Named Rules
**The No-Shadow Rule.** Elevation is a background-lightness step, never a box-shadow. If something needs to look "lifted," it gets a lighter background, not a shadow.

## Shapes

Two radius values, used by role, never mixed within one component family:
- **6px** on every standalone panel: buttons, requirement cards, the docpage mock, callouts, verdict lines, the carousel container, mode/draft toggles, code blocks, the repo-bar.
- **999px (full pill)** on every status badge: PASS/REVISE/BLOCK stampwords, provenance pills, the repo-bar's merge-status pill.
- **0px (sharp)** on collapsed-border grid components — blocker cards, the 9-stage tab grid, the 4-step "how it runs" grid, the install-methods grid — where cells share hairline borders; rounding individual cells in a collapsed-border grid would show gaps of the page background at shared corners, so these stay sharp on purpose.

### Named Rules
**The Grid-Stays-Sharp Rule.** A component whose cells share a border with their neighbors (collapsed-border grid) never gets individual corner radius. Radius is reserved for genuinely standalone boxes.

## Components

### Buttons
- **Shape:** 6px radius.
- **Primary (`.btn.solid`):** Merge Blue fill, white text, Merge Blue border. Hover darkens slightly (#3a7bef).
- **Secondary (`.btn`):** Panel Charcoal fill, Diff White text, Hairline Border. Hover brightens the border to Muted Label Gray.

### Status Pills
- **Style:** full-pill radius, 1px border in the semantic color, background tinted to the same color's `-soft` variant, text in the semantic color. Used for verdict stampwords (`PASS`/`REVISE`/`BLOCK`), the repo-bar's merge status, and the `.pill.ok`/`.pill.bad` component.
- **Motion:** a one-shot scale-in (`.7 → 1.06 → 1`, ~0.4s) plays once when a verdict pill enters the viewport or a stage is switched; never loops.

### Cards / Containers
- **Corner Style:** 6px for standalone cards (requirement cards, docpage); sharp (0px) for collapsed-border grid cells (blocker cards, stage tabs).
- **Background:** Panel Charcoal for recessed/code content; Terminal Black for the base page; Elevated Charcoal for UI-mockup chrome.
- **Shadow Strategy:** none — see Elevation & Depth.
- **Border:** 1px Hairline Border throughout.

### Diff Blocks (signature component)
The hero's press-release paragraphs render as diff lines: Diff Add Green-tinted background, a 3px Diff Add Green left border (the diff tool's literal added-line marker), a mono `+` gutter, prose in Comment Gray.

### Navigation (stage tabs)
9-tab sharp-cornered grid, Panel Charcoal at rest, Merge Blue fill + white text when selected, a Merge Blue underline rail (`transform: scaleX()`-driven, never `width`) that glides between the selected tab and the previous one.

### Rendered Document (`.mddoc`)
"The complete artifact, as written to disk" no longer dumps raw markdown into a `<pre>` — a small dependency-free renderer (`mdToHtml()`) converts headings, bold/italic/inline-code, blockquotes, lists, tables, and fenced blocks into real typography, reusing the page's existing type scale and token system rather than inventing document-specific styles. Two deliberate exceptions to the "no colored side-borders" default now exist on this page — the hero's `.diffline` marker and `.mddoc blockquote`'s left border — both earned by the same reasoning: they're the literal, universal convention for their respective content (a diff addition; a quoted block), not a decorative card accent, and neither is used anywhere else. Fenced code blocks (`.mddoc pre`) reuse the Elevated Charcoal background already established for `.mock`/`.logbox`, so a Q&A block embedded in a rendered document reads as the same "console output" material as everywhere else on the page. `.csv` files bypass the renderer entirely and stay in a plain `.raw` monospace block — CSV isn't markdown, and parsing it as prose would corrupt quoted fields.

## Do's and Don'ts

### Do:
- **Do** keep PASS/REVISE/BLOCK exactly three colors (green/amber/red), everywhere they appear on the site.
- **Do** use JetBrains Mono only for genuine data — IDs, tags, code, commands — never as generic "technical" decoration.
- **Do** use the 3px colored left-border only on diff lines; it is earned by the diff-tool world, not a general card-accent device.
- **Do** keep elevation as background-lightness steps; never add a box-shadow to a panel.

### Don't:
- **Don't** reuse Merge Blue for a verdict — it is the one non-semantic color and must stay recognizably different from PASS/REVISE/BLOCK.
- **Don't** round the corners of collapsed-border grid cells (blocker cards, stage tabs, the 4-step grid) — it breaks the shared-edge illusion.
- **Don't** reintroduce a kicker/eyebrow label above a heading — removed deliberately in an earlier pass and re-confirmed absent in this rebuild.
- **Don't** add a second accent hue. If something needs emphasis and isn't a verdict, it's blue or it's neutral.
