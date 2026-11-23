# AnyTone DMR UK Wiki

A preserved, searchable copy of Norman Williams' AnyTone DMR guide
(hamradiosouthernrepeaters.co.uk/anytone-dmr.html), built with MkDocs Material and published at
<https://gm5dna.github.io/anytone-dmr-wiki/>. See [LICENCE](LICENCE) for rights and credits.

## Layout

- `docs/` holds the site. There is one note per source document, in topic folders.
- `docs/originals/` holds Norman's files exactly as downloaded (PDFs, images, zips), with paths mirroring his site.
- `docs/archive/third-party/` holds the manufacturer manuals, which are listed on `docs/manuals.md`.
- `docs/mods/` holds the mods pages, split one section per note by `scripts/split_mods.py`.
- `build/` is git-ignored and holds working files: the manifest, PDF extractions, Wayback state and agent batches.

## Rebuilding / refreshing

Run the steps in order (`uv` provides the dependencies):

```sh
uv run --with pymupdf python -I scripts/harvest.py --refresh   # re-download; reports NEW / CHANGED / GONE
python3 -I scripts/split_mods.py          # new sections only. NEVER --force: it would wipe the edited mods notes
python3 -I scripts/finalise.py            # restores PDF links, points on-site links at local copies, writes hub-index.md
python3 -I scripts/manuals.py             # archives manuals listed in build/vendor.json, writes manuals.md
python3 -I scripts/wayback.py             # makes sure linked URLs have Internet Archive snapshots (slow, resumable)
uv run --with-requirements requirements.txt mkdocs serve
```

Notes for new PDFs are written by hand (or by an agent) following `STYLE.md`. The extraction for each one is
in `build/extract/<name>/`. The scripts never overwrite hand-edited notes, except `split_mods.py --force`.

Pushing to `main` deploys the site through GitHub Actions (`mkdocs build --strict`).
