"""Point links at local copies and generate docs/hub-index.md (+ docs/manuals.md if build/vendor.json exists).

- hamradiosouthernrepeaters.co.uk links -> local note (by frontmatter source_url) or archived original
- anytonetechzone.byethost7.com mod links -> local mod notes (same anchors)
Idempotent; safe to rerun.   python3 -I scripts/finalise.py
"""
import json, os, re, urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = "https://hamradiosouthernrepeaters.co.uk"
PAGE_NOTES = {  # Norman's HTML pages -> our notes
    "/anytone-dmr.html": "hub-index.md",
    "/50-questions-answers.html": "getting-started/questions-answers.md",
    "/anytone-dmr/50-questions-answers.html": "getting-started/questions-answers.md",
    "/anytone-dmr/2-uncategorised/50-questions-answers.html": "getting-started/questions-answers.md",
    "/20-expanding-rx-frequencies.html": "mods/expanding-rx-frequencies.md",
    "/anytone-dmr/2-uncategorised/17-ste.html": "analogue/ste-squelch-tail-eliminate.md",
    "/64-anytone-igate.html": "aprs-gps/anytone-igate.md",
    "/anytone-dmr/anytone-168-mods.html": "mods/168/index.md",
    "/images/878Mods/878techmods.html": "mods/868-878/index.md",
    "/images/578Mods/578techmods.html": "mods/578/index.md",
    "/dmr-info.html": "dmr-nxdn/index.md",
    "/nxdn.html": "dmr-nxdn/nxdn.md",
}
TECHZONE = {"878techmods.htm": "/images/878Mods/878techmods.html", "578techmods.htm": "/images/578Mods/578techmods.html"}
LINK = re.compile(r"(\]\(|<)(https?://(?:www\.)?(?:hamradiosouthernrepeaters\.co\.uk|hamradio\.joomla\.com|anytonetechzone\.byethost7\.com)[^)\s>]*)([)>])")


def notes():
    for f in DOCS.rglob("*.md"):
        if "originals" not in f.parts:
            yield f


def build_map():
    by_url = {}
    for f in notes():
        m = re.search(r"^source_url:\s*(\S+)", f.read_text(), re.M)
        if m:
            by_url.setdefault(m.group(1).replace("http://", "https://"), f.relative_to(DOCS).as_posix())
    for path, note in PAGE_NOTES.items():
        by_url.setdefault(SITE + path, note)
    return by_url


def resolve(url, by_url):
    """Return a docs-relative target for an on-site/techzone URL, or None."""
    u = urllib.parse.urlparse(url)
    path = urllib.parse.unquote(u.path)
    if "byethost" in u.netloc:
        name = path.rsplit("/", 1)[-1]
        if (DOCS / "originals/anytonetechzone" / name).is_file():  # Jason's tools, recovered from DB1IG mirror
            return "originals/anytonetechzone/" + urllib.parse.quote(name)
        if name not in TECHZONE:
            return None
        path = TECHZONE[name]
    full = SITE + path  # hamradio.joomla.com is Norman's old domain for the same site
    if u.fragment and f"{full}#{u.fragment}" in by_url:
        return by_url[f"{full}#{u.fragment}"]
    if full in by_url:
        return by_url[full]
    local = DOCS / "originals" / path.lstrip("/")
    if local.is_file():
        return "originals/" + urllib.parse.quote(path.lstrip("/"))
    return None


def rewrite(by_url):
    changed, unresolved = 0, set()
    for f in notes():
        here = f.parent.relative_to(DOCS)
        text = f.read_text()

        def sub(m):
            # keep the note's own source_url / Source admonition links absolute (they are attribution)
            target = resolve(m.group(2), by_url)
            if not target:
                unresolved.add(m.group(2))
                return m.group(0)
            rel = os.path.relpath(DOCS / target.split("#")[0], DOCS / here) + ("#" + target.split("#")[1] if "#" in target else "")
            return f"]({rel})" if m.group(1) == "](" else f"[{m.group(2)}]({rel})"

        body_start = text.find("\n---", 4) + 4 if text.startswith("---") else 0
        head, body = text[:body_start], text[body_start:]
        # Source admonition lines stay as the canonical attribution link
        new = "\n".join(l if l.lstrip().startswith(("Originally published", "© Jason", "!!! ")) else LINK.sub(sub, l)
                        for l in body.split("\n"))
        if new != body:
            f.write_text(head + new)
            changed += 1
    return changed, unresolved


FOOTER = re.compile(r"^\s*<?\[?https?://tiny\.cc/Anytone-?DMR\]?(\(.*?\))?>?\s*$", re.M | re.I)


def restore_pdf_links(by_url):
    """Re-attach PDF link annotations (build/extract/<stem>/links.json) that the notes lost; drop tiny.cc footers."""
    fixed, listed = 0, 0
    for f in notes():
        text = f.read_text()
        m = re.search(r"^original:\s*\S*/([^/\s]+)\.pdf\s*$", text, re.M)
        new = FOOTER.sub("", text)
        lj = ROOT / "build/extract" / (m.group(1) if m else "-") / "links.json"
        if m and lj.exists():
            leftover = []
            for anchor, uri in json.loads(lj.read_text()):
                bare = uri.split("://", 1)[-1].rstrip("/")
                local = resolve(uri, by_url) if any(h in uri for h in ("hamradiosouthernrepeaters", "hamradio.joomla", "byethost")) else None
                if local and "(" + os.path.relpath(DOCS / local.split("#")[0], f.parent) in new:
                    continue
                if bare in new or f"[{anchor}](" in new or "tiny.cc/" in uri or urllib.parse.quote(uri.rsplit("/", 1)[-1]) in new or uri.rsplit("/", 1)[-1] in new:
                    continue
                # wrap first plain (unlinked) occurrence of the anchor text
                hit = re.search(r"(?<!\[)" + re.escape(anchor) + r"(?![^\[]*\]\()", new) if len(anchor) > 3 else None
                if hit and not new[hit.start():hit.end()].startswith("http"):
                    new = new[:hit.start()] + f"[{anchor}]({uri})" + new[hit.end():]
                    fixed += 1
                elif hit:
                    new = new[:hit.start()] + f"<{uri}>" + new[hit.end():]
                    fixed += 1
                else:
                    leftover.append((anchor, uri))
            if leftover and "## Links in the original PDF" not in new:
                new = new.rstrip() + "\n\n## Links in the original PDF\n\n" + "\n".join(
                    f"- [{a or u}]({u})" for a, u in dict.fromkeys(leftover)) + "\n"
                listed += len(leftover)
        if new != text:
            f.write_text(new)
    return fixed, listed


TOPICS = [  # folder, nav title, blurb (order = home page order)
    ("getting-started", "Getting started", "Before buying, first steps, Q&A"),
    ("cps-firmware", "CPS, firmware & codeplugs", "Programming software, updates, MCU reset, CSV"),
    ("contacts-talkgroups", "Contacts & talk groups", "Digital contacts, talk groups, talker alias"),
    ("networks-hotspots", "Networks & hotspots", "BrandMeister, FreeDMR, reflectors, Pi-Star, OpenSpot"),
    ("aprs-gps", "APRS & GPS", "Digital and analogue APRS, GPS, roaming, IGate"),
    ("bluetooth", "Bluetooth", "BT firmware, PTT, earpieces"),
    ("scanning-monitoring", "Scanning & monitoring", "Scan lists, CDT scan, Digi Moni"),
    ("operating", "Operating", "Private calls, roaming, simplex, satellites, messages"),
    ("encryption", "Encryption", "AES/ARC4, Motorola and Hytera interoperability"),
    ("analogue", "Analogue features", "Tones, 5-tone, STE, cross band, power"),
    ("hardware", "Hardware & antennas", "Antennas, connectors, timeout timer"),
    ("troubleshooting", "Troubleshooting", "Beeps, LEDs, error messages, odd behaviour"),
    ("models", "Model-specific", "AT-D578UV repeater mode, AT-D890UV NXDN"),
    ("mods", "Mods, hints & tips", "Jason VK7ZJA's 868/878 and 578 pages, 168 mods"),
    ("dmr-nxdn", "DMR & NXDN info", "Reflectors, talk groups, hotspot calibration"),
]
GEN = "<!-- generated by scripts/finalise.py -->"


def title(f):
    m = re.search(r"^title:\s*\"?(.*?)\"?\s*$", f.read_text(), re.M)
    return m.group(1) if m else f.stem


def topic_pages():
    """Write an index.md for topic folders (unless hand-written) and the topic grid on the home page."""
    cards = []
    for folder, name, blurb in TOPICS:
        d = DOCS / folder
        pages = sorted((f for f in d.rglob("*.md") if f.name != "index.md"), key=lambda f: title(f).lower())
        idx = d / "index.md"
        if not idx.exists() or GEN in idx.read_text():
            body = "\n".join(f"- [{title(f)}]({f.relative_to(d).as_posix()})" for f in pages)
            idx.write_text(f"---\ntitle: {name}\n---\n{GEN}\n\n# {name}\n\n{blurb}.\n\n{body}\n")
        cards.append(f"-   **[{name}]({folder}/index.md)** · {len(pages)} pages\n\n    {blurb}")
    home = DOCS / "index.md"
    text = home.read_text()
    grid = "<!-- topics:start -->\n<div class=\"grid cards\" markdown>\n\n" + "\n\n".join(cards) + "\n\n</div>\n<!-- topics:end -->"
    home.write_text(re.sub(r"<!-- topics:start -->.*?<!-- topics:end -->", lambda m: grid, text, flags=re.S))


def natural(item):
    m = re.match(r"(\d+)([a-z]?)", item)
    return (int(m.group(1)), m.group(2)) if m else (9999, item)


def hub_index(by_url):
    m = json.loads((ROOT / "build/manifest.json").read_text())
    items = sorted((i for i in m["hub_items"] if i["item"][0].isdigit()), key=lambda i: natural(i["item"]))
    out = ["---\ntitle: Original index (items 1–190)\n---\n", "# Original index",
           "Norman's numbered list from the original page, in his order. Each link goes to the copy on this site,"
           " or to the external site where the item points elsewhere. "
           "See also [Videos](videos.md) and [UK DMR networks](uk-networks.md).\n"]
    for it in items:
        text, extra = re.sub(r"\s*\|\s*", " ", it["text"]).strip(" |"), []
        for l in it["links"]:
            t = resolve(l["href"], by_url) if any(h in l["href"] for h in ("hamradiosouthernrepeaters", "hamradio.joomla", "byethost")) else None
            md = f"[{l['text'] or 'link'}]({t or l['href']})"
            if l["text"] and l["text"] in text and f"[{l['text']}]" not in text:
                text = text.replace(l["text"], md, 1)
            else:
                extra.append(md)
        out.append(f"- **{it['item']}.** " + " · ".join(filter(None, [text] + extra)))
    (DOCS / "hub-index.md").write_text("\n".join(out) + "\n")
    return len(items)


if __name__ == "__main__":
    by_url = build_map()
    print("pdf links re-attached inline %d, listed at end %d" % restore_pdf_links(by_url))
    n = hub_index(by_url)
    topic_pages()
    changed, unresolved = rewrite(by_url)
    print(f"hub-index: {n} items | notes rewritten: {changed} | unresolved on-site links: {len(unresolved)}")
    for u in sorted(unresolved):
        print("  ", u)
