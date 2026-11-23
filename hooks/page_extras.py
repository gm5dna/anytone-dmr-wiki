"""MkDocs hook: lazy-load images and add a 'Report a problem' link to every page."""
import re
from urllib.parse import quote

REPO = "https://github.com/gm5dna/anytone-dmr-wiki/issues/new"


MODS = {"mods/578/": "AT-D578UV mods", "mods/868-878/": "AT-D868UV/878UV mods", "mods/168/": "AT-D168UV mods"}


def on_post_page(output, page, config):
    """Jason's 578 and 868/878 pages share many titles: say which radio in the tab and share cards."""
    label = next((v for k, v in MODS.items() if page.file.src_uri.startswith(k)), None)
    if not label or page.file.src_uri.endswith("index.md"):
        return output
    output = re.sub(r"<title>(.*?) - ", lambda m: f"<title>{m.group(1)} · {label} - ", output, count=1)
    for prop in ('og:title', 'twitter:title'):
        output = re.sub(rf'(<meta (?:property|name)="{prop}" content=")([^"]*)"', lambda m: f'{m.group(1)}{m.group(2)} · {label}"', output, count=1)
    return output


def on_page_content(html, page, config, files):
    html = re.sub(r"<img(?![^>]*\bloading=)", '<img loading="lazy"', html)
    url = config["site_url"].rstrip("/") + "/" + page.url
    link = f"{REPO}?title={quote('Problem on: ' + page.title)}&body={quote('Page: ' + url + chr(10) + chr(10) + 'What is wrong:' + chr(10))}"
    return html + f'\n<p class="report-problem"><a href="{link}">Report a problem with this page</a></p>\n'
