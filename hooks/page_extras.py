"""MkDocs hook: lazy-load images and add a 'Report a problem' link to every page."""
import re
from urllib.parse import quote

REPO = "https://github.com/gm5dna/anytone-dmr-wiki/issues/new"


def on_page_content(html, page, config, files):
    html = re.sub(r"<img(?![^>]*\bloading=)", '<img loading="lazy"', html)
    url = config["site_url"].rstrip("/") + "/" + page.url
    link = f"{REPO}?title={quote('Problem on: ' + page.title)}&body={quote('Page: ' + url + chr(10) + chr(10) + 'What is wrong:' + chr(10))}"
    return html + f'\n<p class="report-problem"><a href="{link}">Report a problem with this page</a></p>\n'
