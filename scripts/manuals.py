"""Archive third-party manuals listed in build/vendor.json and write docs/manuals.md.

Manual PDFs -> docs/archive/third-party/<vendor>/ (skipped if already present). CPS/firmware are listed as links only.
    python3 -I scripts/manuals.py
"""
import hashlib, json, re, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"}
NORMAN_MANUALS = ["D890UV_user_manual", "AT_D890UV_Programming_Guide_251206", "AT-D168UV_manual_240827",
                  "AT-D168UV_brochure_240827", "Catalog_Anytone_2023_ENG"]


def kebab(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def main():
    v = json.loads((ROOT / "build/vendor.json").read_text())
    state_f = ROOT / "build/manuals-state.json"
    state = json.loads(state_f.read_text()) if state_f.exists() else {}
    today = time.strftime("%d/%m/%Y")
    rows = []
    for m in v["manuals"]:
        name = urllib.parse.unquote(m["url"].split("?")[0].rsplit("/", 1)[-1]).replace(" ", "_")
        local = DOCS / "archive/third-party" / kebab(m["vendor"].split("(")[0]) / name
        if not local.exists():
            try:
                with urllib.request.urlopen(urllib.request.Request(m["url"], headers=UA), timeout=120) as r:
                    data = r.read()
                if not data.startswith(b"%PDF"):
                    raise ValueError("not a PDF")
                local.parent.mkdir(parents=True, exist_ok=True)
                local.write_bytes(data)
                state[m["url"]] = {"retrieved": today, "sha256": hashlib.sha256(data).hexdigest(), "size": len(data)}
            except Exception as e:
                print("FAILED", m["url"], e)
                state[m["url"]] = {"error": str(e)}
                continue
        s = state[m["url"]]
        rows.append((", ".join(m["models"]), m["title"], m.get("version") or "", m["vendor"],
                     local.relative_to(DOCS).as_posix(), m["url"], s["retrieved"], s["size"], s["sha256"][:12]))
    state_f.write_text(json.dumps(state, indent=1))

    out = ["---\ntitle: Manuals & downloads\n---\n", "# Manuals & downloads\n",
           "## Manuals hosted on Norman's site\n",
           "| Document | Size |", "|---|---|"]
    m = json.loads((ROOT / "build/manifest.json").read_text())
    for f in m["files"]:
        stem = Path(f["path"]).stem
        if f.get("status") == "ok" and (stem in NORMAN_MANUALS or f["path"].endswith((".zip",))):
            out.append(f"| [{stem.replace('_', ' ')}]({urllib.parse.quote(f['path'])}) | {f['size'] / 1e6:.1f} MB |")
    out += ["\n## Manufacturer and distributor manuals\n",
            "These are archived copies, so that they stay available if the publisher's link changes. They remain the property "
            "of their publishers and will be removed on request. The source link goes to the publisher's current copy.\n",
            "| Radio | Document | Version | Publisher | Archived copy | Retrieved | SHA-256 (first 12) |", "|---|---|---|---|---|---|---|"]
    for r in sorted(rows):
        out.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | [PDF]({urllib.parse.quote(r[4])}) ({r[7] / 1e6:.1f} MB) · [source]({r[5]}) | {r[6]} | `{r[8]}` |")
    out += ["\n## CPS, firmware and drivers\n",
            "Programming software and firmware are **not** copied here. Download them from the manufacturer or an "
            "authorised distributor, and make sure the CPS, firmware and codeplug versions all match. "
            "Versions below were current when this list was checked.\n",
            "| Radio | Type | Version | Publisher | Download |", "|---|---|---|---|---|"]
    for s in sorted(v["software"], key=lambda s: (s["models"], s["vendor"])):
        link = s.get("file_url") or s["page_url"]
        out.append(f"| {', '.join(s['models'])} | {s['kind']} | {s.get('version', '')} | {s['vendor']} | [{'file' if s.get('file_url') else 'page'}]({link}) |")
    (DOCS / "manuals.md").write_text("\n".join(out) + "\n")
    print(f"manuals archived: {len(rows)}/{len(v['manuals'])}; software listed: {len(v['software'])}")


if __name__ == "__main__":
    main()
