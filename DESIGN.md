---
name: Working Backwards
description: A judge-gated PR/FAQ pipeline, set as a manuscript under editorial review.
colors:
  proof-stock: "#ECEEEA"
  proof-stock-recessed: "#E2E5E0"
  proof-stock-deep: "#D8DCD7"
  ink: "#1B1D1C"
  ink-secondary: "#484D4A"
  ink-muted: "#676D69"
  hairline: "#C4C9C4"
  correction-red: "#A5271B"
  correction-red-wash: "#EFDCD9"
  editors-blue: "#2C5AA0"
  editors-blue-wash: "#DCE3EF"
  stet-green: "#3F5F44"
typography:
  display:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "clamp(3.6rem, 11vw, 8.5rem)"
    fontWeight: 500
    lineHeight: 0.87
    letterSpacing: "-0.028em"
  deck:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "clamp(1.4rem, 2.6vw, 2.05rem)"
    fontWeight: 400
    lineHeight: 1.24
  headline:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "clamp(1.9rem, 3.4vw, 2.65rem)"
    fontWeight: 400
    lineHeight: 1.1
  subpage-display:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "clamp(3rem, 8vw, 5.5rem)"
    fontWeight: 400
    lineHeight: 0.95
  subpage-headline:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "clamp(1.8rem, 3.2vw, 2.4rem)"
    fontWeight: 400
    lineHeight: 1.12
  numeral:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "2.4rem"
    fontWeight: 400
  title:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "2rem"
    fontWeight: 400
  doc-title:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "1.75rem"
    fontWeight: 400
  stage-numeral:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "1.5rem"
    fontWeight: 400
  sigla-numeral:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "1.4rem"
    fontWeight: 400
  subhead:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "1.3rem"
    fontWeight: 400
  subtitle:
    fontFamily: "Bodoni Moda, Didot, Times New Roman, serif"
    fontSize: "1.25rem"
    fontWeight: 400
  lede:
    fontFamily: "Libre Caslon Text, Georgia, serif"
    fontSize: "1.16rem"
    fontWeight: 400
    lineHeight: 1.6
  standfirst:
    fontFamily: "Libre Caslon Text, Georgia, serif"
    fontSize: "1.06rem"
    fontWeight: 400
  body:
    fontFamily: "Libre Caslon Text, Georgia, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.62
  body-document:
    fontFamily: "Libre Caslon Text, Georgia, serif"
    fontSize: "0.98rem"
    fontWeight: 400
    lineHeight: 1.68
  body-compact:
    fontFamily: "Libre Caslon Text, Georgia, serif"
    fontSize: "0.94rem"
    fontWeight: 400
  caption:
    fontFamily: "Libre Caslon Text, Georgia, serif"
    fontSize: "0.86rem"
    fontWeight: 400
  mark:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "0.78rem"
    fontWeight: 400
  mark-small:
    fontFamily: "Courier Prime, Courier New, monospace"
    fontSize: "0.73rem"
    fontWeight: 400
    letterSpacing: "0.05em"
rounded:
  none: "0px"
spacing:
  section: "5.5rem"
  entry: "1.5rem"
components:
  action-primary:
    textColor: "{colors.editors-blue}"
    backgroundColor: "transparent"
    rounded: "{rounded.none}"
    padding: "0.95rem 1.35rem 0.9rem 0"
  action-secondary:
    textColor: "{colors.ink}"
    backgroundColor: "transparent"
    rounded: "{rounded.none}"
  verdict-ruled:
    textColor: "{colors.correction-red}"
    backgroundColor: "transparent"
  query-slip:
    textColor: "{colors.editors-blue}"
    backgroundColor: "transparent"
---

# Design System: Working Backwards

## Overview

**Creative North Star: "The Manuscript Under Editorial Review"**

The product is a document-production and review discipline, so the site is set
as a document under review — not as a piece of software tooling. Its materials
come from the world the subject actually lives in: proof stock, galleys, the
margin as an architectural zone, the editorial query slip, correction ink.

This replaced a "Review Queue" build that rendered the same idea as GitHub's
dark UI. That build was clean and it was wrong: `#0d1117` is literally GitHub's
background and `#4c8eff` its blue, so the page was a competent copy of the
most-copied developer UI in existence rather than an identity. The reasoning,
the tell-catalogue that diagnosed it, and the sources are in
[DESIGN-RESEARCH.md](DESIGN-RESEARCH.md); read that before changing this world.

**Key Characteristics:**
- Cool proof stock, deliberately not cream and not white. Light chosen from the
  physical scene (a PM reading a lot of text in daylight), never from category.
- **No cards, anywhere.** Sequences are ruled lists; queries are slips; sections
  are separated by rules and space. Boxes are the thing this design refuses.
- **Radius 0.** This is print.
- Three faces with three jobs: a didone for display, a Caslon for reading, a
  typewriter for marks and data.
- Extreme scale contrast — 8.5rem display against 0.73rem marginal marks.
- A wide left margin column (the *apparatus*) carries section identity, so the
  reading column stays a reading column.

## Colors

A proof sheet: paper, ink, and exactly two marking colours that mean something.

### Primary
- **Editor's Blue** (#2C5AA0): the query. Used *only* where the judge could not
  rule and routed a question to a named human — open blockers, open questions,
  the two barred rubric dimensions, and citation links back to sources.

### Secondary
- **Correction Red** (#A5271B): the ruling. Used *only* where the judge ruled
  against something — REVISE, BLOCK, `[ASSUMED]`, `[NEEDS EVIDENCE]`, blocked
  release slices.

### Tertiary
- **Stet Green** (#3F5F44): reserved, used almost nowhere. Available for an
  affirmative state that must be visible; a passing artifact normally carries
  no colour at all.

### Neutral
- **Proof Stock** (#ECEEEA): page ground. Cool, faintly green-grey.
- **Proof Stock Recessed** (#E2E5E0): quoted matter, typed blocks, alternating
  section bands.
- **Proof Stock Deep** (#D8DCD7): the deepest recess.
- **Ink** (#1B1D1C): primary text; a warm-neutral black, never #000.
- **Ink Secondary** (#484D4A) / **Ink Muted** (#676D69): running text inside
  components, and marginal marks.
- **Hairline** (#C4C9C4): every rule on the page.

### Named Rules

**The Colour Law.** No mark means it passed. Silence is approval, exactly as on
a real proof. Red means the judge ruled against it. Blue means the judge could
not rule and queried a human. Nothing on this site is coloured for decoration,
so a mark always means attention — and the palette teaches the product's central
claim before a word is read.

**The Two-Ink Rule.** There are two marking colours. A third would make the
first two ambiguous. If something needs emphasis and is neither a ruling nor a
query, it gets weight, size, or space — not hue.

## Typography

**Display:** Bodoni Moda (with Didot, Times New Roman fallback)
**Reading text:** Libre Caslon Text (with Georgia fallback)
**Marks, prompts, data:** Courier Prime (with Courier New fallback)

**Character:** A didone, a Caslon, and a typewriter — the three type technologies
of the printed document, each doing the job it actually did. Bodoni's extreme
thick/thin contrast carries the title page. Caslon is the historical face of the
printed memo and book, and does all the reading. Courier Prime sets everything
that was *typed* rather than *composed*: stage prompts, query slips, provenance
sigla, citations, code, CSV.

### Hierarchy
- **Display** (500, `clamp(3.6rem, 11vw, 8.5rem)`, 0.87 line-height): the h1 only.
- **Deck** (400 italic, `clamp(1.4rem, 2.6vw, 2.05rem)`): the line under the title.
- **Headline** (400, `clamp(1.9rem, 3.4vw, 2.65rem)`): section h2.
- **Numerals** (2.4rem step sequence / 1.5rem stage rail / 1.4rem sigla): Bodoni
  figures used structurally, not decoratively.
- **Lede** (1.16rem) → **Standfirst** (1.06rem) → **Body** (1rem) → **Caption**
  (0.86rem): the reading ramp.
- **Mark** (0.78rem) / **Mark small** (0.73rem, 0.05em tracking): Courier.

### Named Rules

**The Contrast Rule.** Adjacent steps in the reading ramp may sit close, but the
*display* step must stand far above everything else — the ratio from display to
body is roughly 8:1. A flat ramp was the single biggest craft failure of the
previous build; do not re-flatten it in the name of tidiness.

**The Typed/Composed Rule.** Courier is for what was typed (prompts, queries,
IDs, data). Caslon is for what was written to be read. Never use the typewriter
as a costume for "technical."

## Layout

A single reading measure, offset by an apparatus. `.wrap` caps at 74rem;
`.app` splits it into a **9.5rem margin column** and the main column, with a
2.75rem gutter. The margin holds the section sigla (`§1`, and its label) on a
2px rule, sticky while its section is in view. Below 1000px the apparatus
collapses to a horizontal label above the content.

Sections run 5.5rem vertical padding and alternate ground tone (`stock` /
`stock-recessed`) to give the long page rhythm. Reading text is capped at
38–46rem depending on role. The hero is deliberately the loosest composition on
the page; §2 (the stage walkthrough) is deliberately the densest.

### Named Rules

**The No-Card Rule.** Nothing on this site is a card. Parallel content becomes a
ruled list with hanging marginalia; the blocker set is a query sheet, the install
methods are a definition list, the pipeline steps are a numbered sequence. If a
new component wants a box, it is wrong — give it a rule and space instead.

## Elevation & Depth

There is no elevation. No shadows exist anywhere in this system. Depth is
expressed as ink density and ground tone, the way it is on paper. A recessed
block (typed matter, quoted matter) sits on `proof-stock-recessed` with a 2px
neutral rule down its left edge — the compositor's convention for set-off
matter, not a decorative accent bar.

### Named Rules

**The Flat-Paper Rule.** No `box-shadow`, ever. A surface that needs to recede
changes tone; a surface that needs emphasis gets a rule.

## Shapes

**Radius 0 everywhere.** There is not a single rounded corner in the system, and
this is the single highest-leverage decision in the whole design. Separation is
carried by 1px hairlines, 2px section rules, and space. The only "container"
edges are the demo-screen mocks (§ Demo spec), which are 1px boxed because they
depict actual product UI and are meant to read as screens.

## Components

### Actions
Not buttons. A rule above and below a row of typographic links; the primary
action is Editor's Blue with a `▸` prefix, the rest are ink. No fills, no
borders, no radius.

### Section sigla (signature component)
The margin column's `§n` in Bodoni over a Courier label, hung on a 2px ink rule
and sticky through the section. This is the page's wayfinding and its most
recognizable device.

### Query slip
A blocker or open question: the slip ID and category in blue Courier hanging
left, the question set as running Caslon in the centre column, owner and blocked
items in Courier at right, separated by a hairline. The judge's own query boxes
(`.qbox`) use a 2px blue left rule.

### Ruled sequence
The pipeline's four beats and the install methods: hanging Bodoni numeral or
Courier label, hairline between entries, no boxes, no equal heights.

### Rendered document (`.mddoc`)
"The complete artifact, as written to disk" renders markdown as real typography
through a small dependency-free renderer, set as a document: Bodoni headings,
Caslon body, Courier fenced blocks on recessed stock. `.csv` bypasses the
renderer and stays raw — CSV is not markdown, and parsing it as prose would
corrupt quoted fields.

## Do's and Don'ts

### Do:
- **Do** keep blue for queries and red for rulings, and let a passing thing
  carry no colour at all.
- **Do** reach for a rule and space before reaching for a container.
- **Do** keep the display step dramatically above the rest of the ramp.
- **Do** set typed artifacts in Courier and written prose in Caslon.

### Don't:
- **Don't** add a border-radius. Anywhere.
- **Don't** add a box-shadow. Anywhere.
- **Don't** build a card grid, even for content that is genuinely parallel.
- **Don't** introduce a third marking colour, or spend blue or red on decoration.
- **Don't** revert to a category-default world (dark IDE chrome, cream editorial)
  — see [DESIGN-RESEARCH.md](DESIGN-RESEARCH.md) for why the last one failed.
