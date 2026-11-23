"""Split the mod pages into one note per section (at each unique <a id=...> anchor).

Writes docs/mods/<model>/<nn>-<anchor>.md + index.md. Existing files are left alone unless --force.
    python3 -I scripts/split_mods.py [--force]
"""
import re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = {  # page slug -> (out folder, site dir of the page, source url, models)
    "mods-868-878": ("868-878", "images/878Mods", "https://hamradiosouthernrepeaters.co.uk/images/878Mods/878techmods.html", ["AT-D868UV", "AT-D878UV"]),
    "mods-578": ("578", "images/578Mods", "https://hamradiosouthernrepeaters.co.uk/images/578Mods/578techmods.html", ["AT-D578UV"]),
    "mods-168": ("168", "anytone-dmr", "https://hamradiosouthernrepeaters.co.uk/anytone-dmr/anytone-168-mods.html", ["AT-D168UV"]),
}
SKIP_IDS = {"back-top", "top"}
JASON = ('!!! note "Author: Jason Reilly VK7ZJA (silent key, January 2023)"\n'
         '    © Jason Reilly 2018–2022. Jason\'s pages were preserved by Norman Williams on '
         'hamradiosouthernrepeaters.co.uk and are reproduced here, with light formatting and spelling edits for readability, so that his work stays available. '
         'They will be removed on request from his family. [Original page]({url})\n\n')
NORMAN = '!!! info "Source"\n    Originally published by Norman Williams on hamradiosouthernrepeaters.co.uk. [Original page]({url})\n\n'



def kebab(s):
    return re.sub(r"[^a-z0-9]+", "-", re.sub(r"([a-z])([A-Z])", r"\1-\2", s).lower()).strip("-")


def title_of(md, anchor):
    for line in md.splitlines():
        t = re.sub(r"[*_\\#>`\[\]]|\(#[^)]*\)|!\(.*?\)", "", line).strip(" :-")
        if len(t) > 3:
            return t[:90]
    return anchor


def split(slug, out, sitedir, url, models, force):
    html = (ROOT / "build/pages" / f"{slug}.html").read_text()
    seen = []
    def mark(m):
        a = m.group(1)
        if a in seen or a in SKIP_IDS:
            return m.group(0)
        seen.append(a)
        return f"XSPLITX{a}XSPLITX" + m.group(0)
    html = re.sub(r'<a [^>]*?id="([^"]+)"', mark, html)
    md = subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none"],
                        input=html, capture_output=True, text=True, check=True).stdout
    parts = re.split(r"XSPLITX(.+?)XSPLITX", md)
    head, rest = parts[0], list(zip(parts[1::2], parts[2::2]))
    files = {a: f"{i:02d}-{kebab(a)}.md" for i, (a, _) in enumerate(rest, 1)}
    d = ROOT / "docs/mods" / out
    d.mkdir(parents=True, exist_ok=True)
    depth = "../../originals/" + sitedir + "/"
    credit = (NORMAN if out == "168" else JASON)

    def fix(body):
        body = re.sub(r"\]\(#([^)\s]+)\)", lambda m: f"]({files[m.group(1)]})" if m.group(1) in files else f"](index.md)", body)
        # relative images/links to on-site files -> archived originals
        body = re.sub(r"(\]\()(?!https?:|mailto:|#|\.\./|[0-9]{2}-[a-z0-9-]+\.md|index\.md)([^)\s]+)", lambda m: m.group(1) + ("../../originals" + m.group(2) if m.group(2).startswith("/") else depth + m.group(2)), body)
        body = re.sub(r"\]\(https?://(?:www\.)?hamradiosouthernrepeaters\.co\.uk/([^)\s]+\.(?:jpe?g|png|gif|pdf|zip))", r"](../../originals/\1", body)
        # pandoc hard breaks ("\\" at line end) -> plain newline (nl2br renders it); drop "\\"-only lines
        body = re.sub(r"(?m)^\\\s*$", "", body)
        body = re.sub(r"(?m)(?<!\\)\\$", "", body)
        return body.strip() + "\n"

    index = [f"---\ntitle: AnyTone {out} mods, hints & tips\nsource_url: {url}\ntags: [{", ".join(models)}]\n---\n",
             f"# AnyTone {out} mods, hints & tips\n", credit.format(url=url), fix(head), "\n## Sections\n"]
    written = 0
    for a, body in rest:
        t = title_of(body, a)
        index.append(f"- [{t}]({files[a]})")
        f = d / files[a]
        if f.exists() and not force:
            continue
        fm = f"---\ntitle: \"{t.replace(chr(34), '')}\"\nsource_url: {url}#{a}\ntags: [{", ".join(models)}]\n---\n\n"
        f.write_text(fm + f"[← All {out} mods](index.md)\n\n" + credit.format(url=f"{url}#{a}") + fix(body))
        written += 1
    if force or not (d / "index.md").exists():
        (d / "index.md").write_text("\n".join(index) + "\n")
    print(f"{slug}: {len(rest)} sections, {written} written")


if __name__ == "__main__":
    for slug, args in PAGES.items():
        split(slug, *args, force="--force" in sys.argv)
