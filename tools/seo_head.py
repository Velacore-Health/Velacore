"""SEO tags for the hand-written pages that no builder makes, Nov 19 2026.

Dourado: every page must be SEO'd, with title tags, meta information and the right indexing. The legal pages had no
description, canonical or share tags, so search engines saw two copies of each, with and without .html. The 404 page
is kept out of search. Descriptions were written by vc-copy from each page's own text.
Run from the repo root:  python -I tools/seo_head.py   It is safe to run again; it rewrites only its own block.
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.velacorehealth.com"
OG = f"{SITE}/images/og.jpg"
PAGES = {
    "privacy": "What the Velacore Health website collects, how it is used and who receives it. It does not collect health information or sell personal information.",
    "terms": "Terms for using Velacore Health, a telehealth coordination platform, not a medical practice. Covers eligibility, billing, renewals and governing law.",
    "refund-policy": "Your program payment is refunded in full if the clinician does not prescribe. You can cancel any time, and any billing period not yet ordered can be refunded.",
    "telehealth-consent": "What you agree to when you start an online visit. Covers how telehealth works, independent licensed clinicians, risks, and your right to withdraw.",
}
BLOCK = re.compile(r"\n  <!-- seo:start -->.*?<!-- seo:end -->", re.S)


def block(title, desc, url):
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    tags = [f'<meta name="description" content="{d}" />', f'<link rel="canonical" href="{url}" />',
            f'<meta property="og:title" content="{t}" />', f'<meta property="og:description" content="{d}" />',
            '<meta property="og:type" content="website" />', f'<meta property="og:url" content="{url}" />',
            '<meta property="og:site_name" content="Velacore Health" />', f'<meta property="og:image" content="{OG}" />',
            '<meta property="og:image:width" content="1200" />', '<meta property="og:image:height" content="630" />',
            '<meta name="twitter:card" content="summary_large_image" />', f'<meta name="twitter:title" content="{t}" />',
            f'<meta name="twitter:description" content="{d}" />', f'<meta name="twitter:image" content="{OG}" />']
    return "\n  <!-- seo:start -->\n  " + "\n  ".join(tags) + "\n  <!-- seo:end -->"


def main():
    for slug, desc in PAGES.items():
        assert 70 <= len(desc) <= 160, (slug, len(desc))
        f = ROOT / "public" / f"{slug}.html"
        s = BLOCK.sub("", f.read_text(encoding="utf-8"))
        title = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1)).strip()
        anchor = re.search(r"\n  <title>.*?</title>", s, re.S)
        s = s[:anchor.end()] + block(title, desc, f"{SITE}/{slug}") + s[anchor.end():]
        f.write_text(s, encoding="utf-8")
        print("seo tags on", f"public/{slug}.html")
    f = ROOT / "public" / "404.html"
    s = f.read_text(encoding="utf-8")
    if '<meta name="robots"' not in s:
        anchor = re.search(r"\n  <title>.*?</title>", s, re.S)
        s = s[:anchor.end()] + '\n  <meta name="robots" content="noindex" />' + s[anchor.end():]
        f.write_text(s, encoding="utf-8")
    print("404 page kept out of search")


if __name__ == "__main__":
    main()
