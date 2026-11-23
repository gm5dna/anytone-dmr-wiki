"""Make sure every URL we link has an Internet Archive snapshot (Save Page Now if none in the last year).

Resumable: state in build/wayback.json. Norman's own pages/files first (site closes June 2027).
    python3 -I scripts/wayback.py
The site links https://web.archive.org/web/2/<url> (latest snapshot), so no per-link rewrite is needed.
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "build/wayback.json"
SKIP = re.compile(r"facebook\.com|paypal|google\.com/search|web\.archive\.org|tinyurl|tiny\.cc|localhost|^https?://[^/]*\.local", re.I)
UA = {"User-Agent": "anytone-dmr-wiki archiver (python urllib)"}


def urls():
    m = json.loads((ROOT / "build/manifest.json").read_text())
    own = [p["url"] for p in m["pages"]] + [f["url"] for f in m["files"]]
    ext = set()
    for it in m["hub_items"]:
        ext |= {l["href"] for l in it["links"]}
    for f in (ROOT / "docs").rglob("*.md"):
        ext |= {a or b for a, b in re.findall(r"\]\((https?://[^)\s]+)\)|<(https?://[^>\s]+)>", f.read_text())}
    ext = {u.split("#")[0] for u in ext if not SKIP.search(u)}
    return own + sorted(ext - set(own))


def call(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return r.status, r.read()


def main():
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    todo = [u for u in urls() if state.get(u) not in ("saved", "recent")]
    print(f"{len(todo)} to check ({len(state)} already done)", flush=True)
    for i, u in enumerate(todo, 1):
        try:
            _, body = call("https://archive.org/wayback/available?url=" + urllib.parse.quote(u, safe=""))
            snap = json.loads(body).get("archived_snapshots", {}).get("closest", {})
            if snap.get("timestamp", "") >= time.strftime("%Y%m%d", time.gmtime(time.time() - 365 * 86400)):
                state[u] = "recent"
            else:
                for attempt in range(3):
                    try:
                        call("https://web.archive.org/save/" + u)
                        state[u] = "saved"
                        break
                    except urllib.error.HTTPError as e:
                        state[u] = f"HTTP {e.code}"
                        if e.code != 429:
                            break
                        time.sleep(120)
                time.sleep(15)  # ponytail: anonymous SPN pacing (8s triggered a temporary block); use S3 keys if too slow
        except Exception as e:
            state[u] = f"error {e}"
        STATE.write_text(json.dumps(state, indent=1))
        if i % 25 == 0:
            print(i, u, state[u], flush=True)
    bad = {u: s for u, s in state.items() if s not in ("saved", "recent")}
    print(f"done: {len(state)} urls, {len(bad)} not archived")
    for u, s in bad.items():
        print(" ", s, u)


if __name__ == "__main__":
    sys.exit(main())
