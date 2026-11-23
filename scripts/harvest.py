"""Fetch Norman's AnyTone pages + every on-site file they link, archive originals, extract PDFs.

Re-runnable: reports NEW / CHANGED / GONE files against the previous build/manifest.json.
Never touches hand-written notes under docs/ other than docs/originals/.

    uv run --with pymupdf python -I scripts/harvest.py [--refresh]

Without --refresh, files already archived locally are reused (no re-download / re-extract).
"""
import hashlib, html, json, re, subprocess, sys, urllib.parse, urllib.request
from html.parser import HTMLParser
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://hamradiosouthernrepeaters.co.uk"
PAGES = [  # (slug, site path)
    ("hub", "/anytone-dmr.html"),
    ("dmr-info", "/dmr-info.html"),
    ("nxdn", "/nxdn.html"),
    ("questions-answers", "/50-questions-answers.html"),
    ("expanding-rx", "/20-expanding-rx-frequencies.html"),
    ("ste", "/anytone-dmr/2-uncategorised/17-ste.html"),
    ("igate", "/64-anytone-igate.html"),
    ("mods-168", "/anytone-dmr/anytone-168-mods.html"),
    ("mods-868-878", "/images/878Mods/878techmods.html"),
    ("mods-578", "/images/578Mods/578techmods.html"),
    ("dmr-access-reflectors", "/dmr-info/2-uncategorised/60-access-reflectors.html"),
    ("dmr-access-talk-groups", "/dmr-info/2-uncategorised/61-access-talk-groups.html"),
    ("dmr-hotspot-offset-calibration", "/dmr-info/2-uncategorised/63-hotspot-offset-calibration.html"),
    ("dmr-pistar-ssh-update", "/dmr-info/2-uncategorised/57-pistar-ssh-update.html"),
    ("dmr-no-ip-duc-raspberry-pi", "/dmr-info/2-uncategorised/30-no-ip-duc-on-raspberry-pi.html"),
    ("dmr-md380-90-password", "/dmr-info/2-uncategorised/59-md380-90-password.html"),
]
FILE_RE = re.compile(r"\.(pdf|zip|doc|docx|jpe?g|png|gif|csv|xlsx?|txt|rdt)$", re.I)
UA = {"User-Agent": "Mozilla/5.0 (archive of AnyTone DMR guide, with owner's permission)"}
BUILD, ORIG = ROOT / "build", ROOT / "docs" / "originals"


def get(url):
    req = urllib.request.Request(urllib.parse.quote(url, safe=":/?=&%#;~+"), headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


class Links(HTMLParser):
    """Collects (href/src, anchor text) pairs."""

    def __init__(self):
        super().__init__()
        self.links, self._a = [], None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self._a = [a["href"], ""]
        elif tag == "img" and a.get("src"):
            self.links.append((a["src"], a.get("alt") or ""))

    def handle_data(self, data):
        if self._a:
            self._a[1] += data

    def handle_endtag(self, tag):
        if tag == "a" and self._a:
            self.links.append((self._a[0], " ".join(self._a[1].split())))
            self._a = None


class HubCells(HTMLParser):
    """Hub item list: <td> cells of the two-column table, as (col, text, [(href, text)])."""

    def __init__(self):
        super().__init__()
        self.cells, self._cell, self._col, self._a = [], None, -1, None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "tr":
            self._col = -1
        elif tag == "td":
            self._col += 1
            self._cell = [self._col, "", []]
        elif tag == "a" and self._cell is not None and a.get("href"):
            self._a = [a["href"], ""]
        elif tag == "br" and self._cell is not None:
            self._cell[1] += " "

    def handle_data(self, data):
        if self._cell is not None:
            self._cell[1] += data
            if self._a:
                self._a[1] += data

    def handle_endtag(self, tag):
        if tag == "a" and self._a and self._cell is not None:
            self._cell[2].append((self._a[0], " ".join(self._a[1].split())))
            self._a = None
        elif tag == "td" and self._cell is not None:
            self._cell[1] = " ".join(self._cell[1].split())
            self.cells.append(tuple(self._cell))
            self._cell = None


def absolute(href, base):
    u = urllib.parse.urljoin(SITE + base, html.unescape(href.strip()))
    return u.replace("http://", "https://", 1).replace("://www.hamradio", "://hamradio")


def hub_items(src):
    """Numbered hub items, keyed '1', '1a', 'v12', 'A'... Unnumbered cells join the item above (same column)."""
    p = HubCells()
    p.feed(src)
    items, current = [], {}
    for col, text, links in p.cells:
        m = re.match(r"^(v?\d+[a-z]?|[A-O])[.)]\s+", text)
        if m:
            current[col] = {"item": m.group(1), "col": col, "text": text[m.end():], "links": []}
            items.append(current[col])
        elif col in current and (text or links):
            current[col]["text"] += " | " + text
        else:
            continue
        current[col]["links"] += [{"href": absolute(h, "/anytone-dmr.html"), "text": t} for h, t in links]
    return items


def pdf_links(pdf):
    """[(anchor text, uri)] from the PDF's link annotations; finalise.py re-attaches them to notes."""
    out = []
    for page in pymupdf.open(pdf):
        for l in page.get_links():
            if l.get("uri"):
                out.append((" ".join(page.get_textbox(l["from"]).split()), l["uri"]))
    return out


def extract_pdf(pdf, out):
    """text.md with ![](img) markers in reading order + page PNGs for reference; OCR full-page scans."""
    out.mkdir(parents=True, exist_ok=True)
    doc, md, n = pymupdf.open(pdf), [], 0
    for pno, page in enumerate(doc, 1):
        page.get_pixmap(dpi=80).save(out / f"page-{pno}.png")
        md.append(f"\n<!-- page {pno} -->\n")
        blocks = page.get_text("dict", sort=True)["blocks"]
        has_text = any(b["type"] == 0 and "".join(s["text"] for l in b["lines"] for s in l["spans"]).strip() for b in blocks)
        for b in blocks:
            if b["type"] == 0:
                md.append("\n".join("".join(s["text"] for s in l["spans"]) for l in b["lines"]))
            elif b["type"] == 1 and b["width"] * b["height"] > 400:  # skip bullets/specks
                n += 1
                name = f"img-{n:02d}.{b['ext']}"
                (out / name).write_bytes(b["image"])
                md.append(f"![]({name})")
        if not has_text:  # likely a scan: OCR it, agent cleans up
            try:
                ocr = page.get_textpage_ocr(language="eng", dpi=300, full=True)
                t = page.get_text(textpage=ocr).strip()
                if t:
                    md.append(f"<!-- OCR -->\n{t}\n<!-- /OCR -->")
            except Exception as e:
                md.append(f"<!-- OCR failed: {e} -->")
    (out / "text.md").write_text("\n\n".join(md))
    (out / "links.json").write_text(json.dumps(pdf_links(pdf), indent=1))
    return {"pages": len(doc), "images": n}


def main():
    old = {}
    if (BUILD / "manifest.json").exists():
        old = {f["url"]: f for f in json.loads((BUILD / "manifest.json").read_text())["files"]}
    (BUILD / "pages").mkdir(parents=True, exist_ok=True)

    files, other_html, pages = {}, set(), []
    for slug, path in PAGES:
        raw = get(SITE + path).decode("utf-8", "replace")
        (BUILD / "pages" / f"{slug}.html").write_text(raw)
        subprocess.run(["pandoc", "-f", "html", "-t", "gfm-raw_html", "--wrap=none",
                        "-o", str(BUILD / "pages" / f"{slug}.md"), str(BUILD / "pages" / f"{slug}.html")], check=True)
        pages.append({"slug": slug, "url": SITE + path})
        lp = Links()
        lp.feed(raw)
        for href, text in lp.links:
            u = absolute(href, path)
            if not u.startswith(SITE):
                continue
            p = urllib.parse.urlparse(u).path
            if FILE_RE.search(p):
                files.setdefault(u, {"url": u, "refs": []})["refs"].append({"page": slug, "text": text})
            elif p.endswith(".html") and urllib.parse.urlparse(u).path not in {q for _, q in PAGES}:
                other_html.add(u)

    report = {"NEW": [], "CHANGED": [], "GONE": [], "DEAD": []}
    for u, f in sorted(files.items()):
        local = ORIG / urllib.parse.unquote(urllib.parse.urlparse(u).path).lstrip("/")
        f["path"] = str(local.relative_to(ROOT / "docs"))
        if local.exists() and u in old and "--refresh" not in sys.argv:
            f.update({k: old[u][k] for k in ("status", "size", "sha256", "extract", "slug") if k in old[u]})
            continue
        try:
            data = get(u)
        except Exception as e:
            f.update(status=f"ERROR {e}")
            report["DEAD"].append(u)
            continue
        f.update(status="ok", size=len(data), sha256=hashlib.sha256(data).hexdigest())
        if u not in old:
            report["NEW"].append(u)
        elif old[u].get("sha256") != f["sha256"]:
            report["CHANGED"].append(u)
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(data)
        if local.suffix.lower() == ".pdf":
            try:
                f["extract"] = extract_pdf(local, BUILD / "extract" / local.stem)
                f["slug"] = local.stem
            except Exception as e:
                f["extract"] = f"FAILED {e}"
        elif local.suffix.lower() == ".doc":
            out = BUILD / "extract" / local.stem
            out.mkdir(parents=True, exist_ok=True)
            subprocess.run(["textutil", "-convert", "txt", "-output", str(out / "text.md"), str(local)], check=False)
            f["slug"] = local.stem
    report["GONE"] = [u for u in old if u not in files]

    hub = hub_items((BUILD / "pages" / "hub.html").read_text())
    manifest = {"pages": pages, "files": list(files.values()), "hub_items": hub,
                "unconverted_onsite_html": sorted(other_html)}
    (BUILD / "manifest.json").write_text(json.dumps(manifest, indent=1))

    ok = [f for f in files.values() if f.get("status") == "ok"]
    print(f"pages {len(pages)} | hub items {len(hub)} | files {len(files)} ok {len(ok)} "
          f"| pdfs extracted {sum(isinstance(f.get('extract'), dict) for f in ok)} "
          f"| {sum(f['size'] for f in ok) / 1e6:.1f} MB")
    for k, v in report.items():
        print(f"{k} {len(v)}" + "".join(f"\n  {x}" for x in v if k != "NEW" or old))
    print("unconverted on-site html:", *sorted(other_html), sep="\n  ")


if __name__ == "__main__":
    sys.exit(main())
