# Why AI-designed sites look AI-designed — and what to do instead

Research notes, 2026-08-31. Written after the user looked at a freshly rebuilt
site and said: *"clean but still looks AI designed."* They were right. This
documents why, so the mistake is not repeated.

---

## 1. The root cause

A language model generating a design returns **the statistical median of its
training data**. It is not choosing; it is averaging. The web contains far more
generic SaaS pages than art-directed ones, so the median is a generic SaaS page.

Two consequences that matter:

1. **Adjectives don't fix it.** Asking for "premium," "unique," "beautiful,"
   or "not generic" resolves to the model's own centroid for those words —
   which is the same centroid everyone else's prompt lands on. Only *concrete
   constraints* (named hex values, a specific typeface, a density target, a
   radius, a committed layout structure) move the output.
2. **Avoidance is also a default.** If a category's cliché is "purple gradient
   SaaS," then "dark mode with a blue accent" is simply the second-most-likely
   answer. Both are reflexes. The test is not *did I avoid the obvious one* but
   *could someone guess my aesthetic from the category alone?*

---

## 2. The catalogue of tells

Consolidated from the sources below. Grouped by where they show up.

### Color
- Purple/violet→blue gradients on anything.
- **Warm cream/beige (#F4F1EA-ish) grounds** — the "tasteful" reflex, now its own cliché.
- **Dark mode with a glowing accent** — the "technical product" reflex.
- Gradient text on headings or metrics.
- Radial "spotlight" haze behind a section.
- Gray text on colored ground (always looks washed out).

### Typography
- Inter, Geist, Space Grotesk, Instrument Serif, Poppins as the display face.
- One typeface for the whole page (flattens hierarchy).
- **Flat type scale** — sizes too close together. Aim for ≥1.25 ratio between steps.
- Oversized *full-sentence* headline filling the viewport.
- Oversized italic serif hero headline (the AI-startup default).
- Tracked uppercase kicker/eyebrow above a heading.
- Crushed letter-spacing on display type.

### Layout
- **Identical card grids** — same-size cards of icon + heading + text, repeated.
  This is the single most common structural tell, and it is usually used three
  or four times on one page.
- Nested cards (cards inside cards).
- Uniform border-radius on everything; extreme radius (24px+) on small cards.
- **Thick colored border on one side of a card** — named by multiple sources as
  the most recognizable single tell.
- Hairline border *plus* wide diffuse shadow (pick one: defined edge, or elevation).
- Monotonous spacing — the same value everywhere, every section the same height.
- Tiny numbered section labels (01 / 02 / 03) used decoratively.
- Hero metric row: big number, small label, three supporting stats.
- Everything centered; nothing overlaps; nothing breaks the grid.

### Motion
- Uniform fade-up-on-scroll applied to every section.
- Pulsing status dots on static status.
- Decorative blinking cursor in hero copy.
- Bounce/elastic easing (reads dated).
- Image scale/rotate on hover.

### Copy
- Em-dash saturation.
- "streamline / empower / supercharge / world-class / enterprise-grade."
- Aphoristic cadence: every section landing on a short manufactured-contrast line.

---

## 3. What genuinely good work does instead

From editorial and award-winning design practice:

- **Extreme scale contrast.** A 7rem display against 0.75rem marginal notes.
  Hierarchy carried by size ratio, not by boxes.
- **Asymmetric grids.** Varying column widths. A narrow outer column becomes a
  *margin-note zone* — a real editorial device, and the classic solution for
  dense text.
- **Deliberate grid-breaking**: pull quotes, full-bleed, inset elements that
  violate the column on purpose, for controlled tension.
- **Whitespace as pacing.** A dense passage earns a quiet one. Space is a
  compositional choice, not leftover.
- **Space and rules instead of boxes.** Borders are the last resort for
  separation, not the first.
- **A palette nobody else owns**, derived from the subject's real materials.
- **A type program with a job per face** — not a display face chosen for vibes.

---

## 4. Diagnosis of the previous working-backwards build

Being specific, because this is the part that generalizes. The "Review Queue"
build hit **at least eight** named tells:

| Tell | Where |
|---|---|
| Dark mode + accent as category reflex | Whole page. `#0d1117` is *literally* GitHub's background; `#4c8eff` its blue. It was a reskin of the most-copied dev UI in existence. |
| Identical card grids | Used **three** times: the 4-step "how it runs," the 6 blocker cards, the 3 install methods. |
| Uniform border-radius | A single rule applied `border-radius:6px` to a comma-list of every panel on the page. |
| Colored side-border on cards | Two instances. |
| Hairline border + panel fills | Every component wrapped in a 1px box. |
| Flat type scale | "Consolidating" the ramp produced 0.65 / 0.72 / 0.78 / 0.85 / 0.9rem — steps of ~1.08, far below the 1.25 guidance. Tidier, but flatter. |
| Monotonous spacing | Every section `padding: 4rem 0`. |
| Full-sentence oversized headline | The h1 was one long sentence at display size. |
| Em-dash saturation | 30 in body copy. |

The lesson: passing a mechanical linter is not the same as having a point of
view. Most of those tells were *individually defensible* and collectively fatal.

---

## 5. The rules adopted for the rebuild

1. **Derive the world from the subject's real materials**, not from its product
   category. This is a document-production and review discipline. Its materials
   are proofs, galleys, margins, editorial query slips, proof-correction marks,
   and citation apparatus — not IDE chrome.
2. **Pick light/dark from the physical scene**, never the category. Scene here:
   a PM at a laptop, in daylight, reading a lot of text to judge whether a
   process is rigorous. That is a reading scene → light ground. But *not cream* —
   a cool proof stock instead.
3. **Color carries meaning or it doesn't appear.** See §6.
4. **No card grids.** Sequences become ruled lists with hanging marginalia.
5. **Radius 0.** This is print. Sharp corners remove an enormous amount of the
   generated-UI signature in one move.
6. **Scale contrast ≥ 1.25 between steps**, and a display step far above the rest.
7. **Vary section density deliberately.**

---

## 6. The color law (the idea worth keeping)

The product's central claim is that its judge is *authoritative on six
dimensions and barred from two* — on the barred ones it does not rule, it
**routes a question to a named human.** The old build buried that distinction.
The rebuild encodes it in color, borrowed from real editorial practice:

- **No mark = it passed.** Silence is approval, exactly as on a real proof.
  Nothing is colored for decoration, so a mark always means attention.
- **Red = the judge ruled against it.** REVISE / BLOCK. Correction ink.
- **Blue = the judge could not rule and queried a human.** The editor's blue
  pencil — the colour that historically marks a query, not a correction. Open
  blockers, open questions, and the two barred dimensions.

This is information design, not decoration: the palette teaches the product's
most important idea before a word is read.

---

## 7. The type program

| Face | Job | Why |
|---|---|---|
| **Bodoni Moda** | Display | Real didone with optical sizing; extreme thick/thin contrast is dramatic at title-page scale. Not on any overused list (AI reaches for Playfair, a weaker Bodoni-ish). |
| **Libre Caslon Text** | Reading text | Caslon is the historical face of the printed memo, book, and document. Readable at length; carries the subject's own heritage. |
| **Courier Prime** | Marks, prompts, data, citations | Typewriter. The stage prompts *are* typed instructions and the queries *are* typed slips — more truthful than a code font, and avoids the JetBrains/IBM Plex/Space Mono default. |

Three faces, three jobs, none on the overused list.

---

## Sources

- [Impeccable — Slop antipattern catalogue](https://impeccable.style/slop/)
- [925 Studios — AI Slop Web Design: spotting and fixing generic websites](https://www.925studios.co/blog/ai-slop-web-design-guide)
- [925 Studios — AI slop fonts and gradients: the tells](https://www.925studios.co/blog/ai-slop-design-tells)
- [Shuffle — Why do most AI-generated websites look the same?](https://shuffle.dev/blog/2026/01/why-do-most-ai-generated-websites-look-the-same/)
- [Managed Code — Why AI-generated websites all look the same](https://www.managed-code.com/blog-post/why-ai-websites-look-the-same)
- [Affinity — Grid design for editorial and web layouts](https://www.affinity.studio/blog/grid-design-for-editorial-and-web-layouts)
- [Design Shack — Grids and typography](https://designshack.net/articles/layouts/grids-and-typography/)
- [Social Animal — Brutalist & editorial web design](https://socialanimal.dev/solutions/brutalist-editorial-web-design/)
