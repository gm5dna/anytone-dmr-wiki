# Note-writing rules (AnyTone DMR wiki, MkDocs Material)

Project root: /Users/stuart/coding/personal/anytone-dmr. Docs live in `docs/`. Original author: Norman Williams
(content reproduced with his permission). The goal is a faithful, readable Markdown copy of each source document.

## Topic folders (pick exactly one per note)
| folder | covers |
|---|---|
| getting-started | before buying, first steps, why Windows PC, general "how to use radio", DMR basics for beginners |
| cps-firmware | CPS, firmware, MCU reset, codeplug import/upgrade/version, CSV export/import, Wine/Linux, passwords, languages, opening screen |
| contacts-talkgroups | digital contacts, talk groups, access TGs, RX group lists, remove spaces |
| networks-hotspots | BrandMeister, FreeDMR, reflectors, dynamic/static TGs, Pi-Star, OpenSpot, BlueDV, hotspot offsets/BER |
| aprs-gps | digital/analogue APRS, GPS lock/test, GPS roaming, SMS via APRS, IGate, KISS TNC |
| bluetooth | BT firmware, BT PTT, earpieces, BT module issues |
| scanning-monitoring | scanning, CDT scan, scan lists, Digi Moni, Remote Moni |
| operating | private call, last call reply, text messages, roaming, simplex, PMR446, manual dial, ranging, missed calls, satellite |
| encryption | AES/ARC4, Motorola/Hytera interop, RAS/CAP |
| analogue | tone decoding, 5-tone, STE, cross band, analogue power levels |
| hardware | antennas, SMA, KlickFast, screen icons, SignaLink, accessories, timeout timer |
| troubleshooting | beeps, LEDs, error messages, keys not working, odd behaviour, volume |
| models | docs specific to one model (168, 578, 890 incl. NXDN on 890) that do not fit a feature topic better |

If nothing fits well, choose the closest and report it as a misfit.

## File
`docs/<folder>/<slug>.md` (slug given in your batch). Never overwrite an existing file you did not write in this run.

## Frontmatter (exact keys)
```yaml
---
title: <clean human title, fix obvious typos in the TITLE only>
item: "57"                 # hub item number(s) as string; list if several: ["25", "26"]; omit if none
source_url: <source_url from batch>
original: ../originals/<...>  # = "../" + original from batch
tags: [AT-D878UV, AT-D578UV]   # radio models the doc applies to. Use only: AT-D168UV, AT-D868UV, AT-D878UV, AT-D578UV, AT-D890UV. [] if generic.
---
```
Infer models only from what the doc says/shows (title, text, screenshots). "878" alone → AT-D878UV. If the doc
says 868/878/578 generally, tag all three. Do not guess beyond the evidence.

## Body
1. `# <title>`
2. `!!! info "Source"` admonition, indented 4 spaces: `Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original PDF](<original>) · [Source](<source_url>)` (add `Hub item <n>.` if there is one).
3. The document content, **verbatim wording** (keep the author's spelling, capitals and phrasing; only fix
   PDF line-wrapping, hyphenation breaks and obvious OCR garbage). Turn layout into proper Markdown:
   headings, numbered steps, bullet lists, tables. Menu paths like `CPS – Optional Settings – Volume/Audio`
   → `**CPS → Optional Settings → Volume/Audio**`.
4. Images: the extracted images are in `docs/assets/img/<slug>/img-NN.<ext>` (same names as the `![](img-NN.ext)`
   markers in text.md, which mark their position). Embed as `![<alt text>](../assets/img/<slug>/img-NN.ext)`.
   **Look at every image** (Read the file). Alt text says what it shows. When a screenshot shows settings, add an
   italic caption line directly below listing the key settings visible, e.g.
   `*Optional Setting → Volume/Audio: Volume = Indoors.*` Describe only what is visible; never invent values.
   Skip images that are pure decoration (logos, PayPal/donate buttons, blank boxes) and duplicate images.
5. Check the page renders `build/extract/<dir>/page-N.png` against text.md. If a page has content that
   text.md missed (vector diagrams, tables drawn as graphics, text baked into images), transcribe it; if it is a
   diagram that cannot be transcribed, copy the page PNG to the assets folder as `page-N.png` and embed it.
6. `<!-- OCR -->` blocks are machine OCR of scanned pages: rewrite them as clean text, verified against the render.
7. Drop: repeated footers (`http://tiny.cc/Anytone-DMR`, page numbers), "click here" chrome.
8. Leave URLs as they are (including hamradiosouthernrepeaters.co.uk ones; they get rewritten later). Make bare URLs
   into `<https://...>` autolinks.
9. Do not add advice, commentary or information that is not in the source. Our own words appear only in alt text/captions.
10. Valid Markdown for Python-Markdown: blank line before lists and tables; tables need a header row.

## Readability pass (applies to all pages; supersedes "verbatim" in rule 3 and the QA line-per-line rule)

The aim is pages that are easy to follow on a phone. Keep every fact, setting, value, step and credit.

**Wording: light copy-edit only.** Fix obvious spelling mistakes and typos ("meathead" → "method", "to loud" → "too loud"),
broken punctuation, random capitals and SHOUTING (keep acronyms like CPS, APRS, TG, BT, MCU). Don't paraphrase,
summarise, re-order the argument or add advice. Keep the author's voice and their spelling choices (analog/analogue, etc.).
Never change: numbers, frequencies, IDs, talk group numbers, menu/field names as shown in the CPS or radio, callsigns,
URLs, file names, code/commands. Non-English pages (e.g. Italian): formatting only.

**Patterns to apply where they fit:**
1. **Paragraphs and headings.** Join PDF line fragments into proper sentences and paragraphs (nl2br is on, so one line equals one rendered line;
   a paragraph must be ONE line). Use `##`/`###` headings where the source has implied sections. There is exactly one `# H1`, and it matches the frontmatter title.
2. **Numbered steps.** Turn instructions into `1.` lists. Indent a step's screenshot, caption or sub-points by 4 spaces under it so
   the numbering continues. If the author numbered steps, keep their numbers (sane_lists is on).
3. **Settings tables.** Show runs of `Setting = value` / `Setting – value` as a `| Setting | Value |` table, with a blank line before it.
4. **Call-out boxes.** Use Material admonitions with the body indented 4 spaces: `!!! note`, `!!! warning` (risk to the radio or codeplug,
   "never do X"), `!!! tip`. Use them sparingly, for the author's own NOTE, IMPORTANT, WARNING and TIP lines.
5. **Menu paths** are written as `**CPS → Optional Setting → Volume/Audio**`. **Keys and buttons** are bold (**PTT**, **P1**).
6. **Emphasis:** at most a few bold phrases per page. Remove bold that only came from PDF styling.
7. Remove empty lines of punctuation, stray `\`, decorative dividers and duplicated headings.

**Must preserve exactly:** frontmatter (apart from fixing a typo in `title`, which must then match the H1), every link target and image path (you
may move them, but each one must still be there), the `!!! info "Source"` / `!!! note "Author…"` box and the `[← All … mods]` line at the top, and
the `## Links in the original PDF` section at the end. Image alt text and captions may be improved.
