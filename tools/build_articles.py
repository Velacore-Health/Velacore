"""Builds the Learn articles: one page per entry in tools/articles.py.

Run from the repo root:  python -I tools/build_articles.py
Writes public/learn/<slug>.html, refreshes the article list on public/learn.html between its
markers, and refreshes the article lines in public/sitemap.xml between its markers.
The plan and the rules for what gets written are in docs/seo/content-plan.md.
No analytics tag on these pages until Dourado makes the health-privacy call.
"""
import datetime as dt
import html
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
OUT = PUB / "learn"
SITE = "https://www.velacorehealth.com"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bp = load("build_programs")
ARTICLES = load("articles").ARTICLES
PROGRAMS = {p["slug"]: p for p in bp.PROGRAMS}


def para(text):
    """A paragraph, or a bulleted list when every line starts with '- '."""
    lines = [l for l in text.strip().split("\n") if l.strip()]
    if lines and all(l.lstrip().startswith("- ") for l in lines):
        return "<ul>" + "".join(f"<li>{l.lstrip()[2:]}</li>" for l in lines) + "</ul>"
    return f"<p>{text.strip()}</p>"


def plain(text):
    return html.unescape(re.sub(r"<[^>]+>", "", text))


def nice_date(iso):
    d = dt.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def page(a):
    url = f"{SITE}/learn/{a['slug']}"
    sections = "".join(f"<h2>{h}</h2>" + "".join(para(p) for p in ps) for h, ps in a["sections"])
    faq = "".join(f'<details class="faq-item"><summary>{q}</summary><div class="faq-body"><p>{ans}</p></div></details>' for q, ans in a["faq"])
    sources = "".join(f'<li><a href="{u}" rel="noopener nofollow">{html.escape(label)}</a></li>' for label, u in a.get("sources", []))
    prog = PROGRAMS.get(a.get("program") or "")
    prog_box = (f'<aside class="art-program"><h2>The {prog["name"]} program</h2><p>{prog["plans"][0]["note"]} Prescription required. '
                f'A licensed clinician decides whether it is appropriate for you.</p>'
                f'<a class="btn btn-primary" href="../programs/{prog["slug"]}.html">See the {prog["name"]} program</a></aside>') if prog else ""
    others = [o for o in ARTICLES if o["slug"] != a["slug"]][:3]
    more = "".join(f'<li><a href="{o["slug"]}.html">{o["h1"]}</a></li>' for o in others)
    ld = [
        {"@context": "https://schema.org", "@type": "Article", "headline": a["h1"], "description": a["meta"],
         "dateModified": a["reviewed"], "datePublished": a.get("published", a["reviewed"]), "mainEntityOfPage": url,
         "author": {"@type": "Organization", "name": "Velacore Health"},
         "publisher": {"@type": "Organization", "name": "Velacore Health", "logo": {"@type": "ImageObject", "url": f"{SITE}/logo-full.png"}}},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(ans)}} for q, ans in a["faq"]]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Learn", "item": SITE + "/learn"},
            {"@type": "ListItem", "position": 3, "name": a["h1"], "item": url}]},
    ]
    ld_html = "\n".join(f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- No analytics on Learn articles until Dourado makes the health-privacy call. -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(a["title"])} | Velacore Health</title>
  <meta name="description" content="{html.escape(a["meta"])}" />
  <meta name="theme-color" content="#15302A" />
  <meta property="og:title" content="{html.escape(a["title"])}" />
  <meta property="og:description" content="{html.escape(a["meta"])}" />
  <meta property="og:type" content="article" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/images/og.png" />
  <link rel="canonical" href="{url}" />
{ld_html}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
  <link rel="icon" href="../logo-mark.png" />
</head>
<body class="article-page">
  <div class="topbar"><span>Clinician-reviewed telehealth, available in <b>all 50 states</b>. Prescription required.</span></div>
  <header class="site-header" id="top">
    <div class="container nav">
      <a href="../index.html" class="brand" aria-label="Velacore Health home">
        <img class="brand-mark" src="../logo-mark.png" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span>
      </a>
      <nav class="nav-links" id="navLinks" aria-label="Primary">
        {bp.mega_menu("../")}
        <a href="../how-it-works.html">How it works</a>
        <a href="../learn.html">Learn</a>
        <a href="../clinicians.html">Clinicians</a>
        <a href="../faq.html">FAQ</a>
        <a href="../index.html#goals" class="btn btn-primary btn-sm" data-find>Find your program</a>
      </nav>
      {bp.MENU_BUTTON}
    </div>
  </header>
  {bp.side_panel("../")}

  <main>
    <article class="section art">
      <div class="container art-wrap">
        <p class="crumbs"><a href="../index.html">Home</a> / <a href="../learn.html">Learn</a> / {a["topic"]}</p>
        <h1>{a["h1"]}</h1>
        <p class="art-meta">Last updated {nice_date(a["reviewed"])}. Written by Velacore Health and not reviewed by a clinician. General education, not medical advice.</p>
        <p class="art-answer">{a["answer"]}</p>
        <div class="art-body">
{sections}
        </div>
        {prog_box}
        <section class="art-faq" aria-label="Common questions">
          <h2>Common questions</h2>
          <div class="faq">{faq}</div>
        </section>
        {f'<section class="art-sources"><h2>Sources</h2><ul>{sources}</ul></section>' if sources else ''}
        <p class="edu-note">This article is general education, not medical advice. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. Whether any treatment is appropriate for you is decided solely by a licensed clinician.</p>
        <div class="art-next">
          <a href="../index.html#goals" class="btn btn-primary" data-find>Find your program</a>
          <div class="art-more"><h2>Keep reading</h2><ul>{more}</ul></div>
        </div>
      </div>
    </article>
    {bp.goal_band('../')}
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="../index.html" class="brand"><img class="brand-mark" src="../logo-mark.png" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span></a>
        <p>A telehealth platform coordinating access to licensed clinicians and 503A compounding pharmacies.</p>
      </div>
      <nav class="footer-col" aria-label="Programs"><h4>Programs</h4>
        {"".join(f'<a href="../programs/{p["slug"]}.html">{p["name"]}</a>' for p in bp.PROGRAMS)}</nav>
      <nav class="footer-col" aria-label="More"><h4>More</h4>
        <a href="../how-it-works.html">How it works</a><a href="../learn.html">Learn</a><a href="../faq.html">FAQ</a><a href="../pricing.html">Pricing</a><a href="../about.html">About</a><a href="../contact.html">Contact</a></nav>
      <nav class="footer-col" aria-label="Legal"><h4>Legal</h4>
        <a href="../privacy.html">Privacy Policy</a><a href="../terms.html">Terms of Service</a><a href="../telehealth-consent.html">Telehealth Consent</a><a href="../refund-policy.html">Refund Policy</a></nav>
    </div>
    <div class="container footer-legal">
      <p class="states-served">Velacore Health telehealth services are available in all 50 US states and the District of Columbia. Every prescription requires review by a clinician licensed for your state. Prescription required.</p>
      <p class="disclaimer"><b>Important:</b> Velacore Health does not provide, guarantee, or facilitate any medical services, prescriptions, or treatments. The platform coordinates access to licensed clinicians and 503A compounding pharmacies; all medical decisions are made solely by the independent clinician. All medications are prescription only. Compounded medications are not FDA approved. Content on this site is for general informational purposes only and is not medical advice. Always consult a qualified healthcare provider.</p>
      <div class="footer-bottom"><p>© <span id="year"></span> Velacore Health, First Venture Group LLC. All rights reserved.</p>
      <nav aria-label="Legal"><a href="../privacy.html">Privacy</a><a href="../terms.html">Terms</a><a href="../telehealth-consent.html">Telehealth consent</a><a href="../refund-policy.html">Refund policy</a></nav></div>
    </div>
  </footer>
  <script src="../script.js"></script>
</body>
</html>
"""


def between(text, start, end, new):
    i, j = text.index(start) + len(start), text.index(end)
    return text[:i] + "\n" + new + "\n" + text[j:]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    keep = set()
    for a in ARTICLES:
        assert len(a["title"]) <= 60, (a["slug"], "title over 60", len(a["title"]))
        assert len(a["meta"]) <= 155, (a["slug"], "meta over 155", len(a["meta"]))
        (OUT / f"{a['slug']}.html").write_text(page(a), encoding="utf-8")
        keep.add(f"{a['slug']}.html")
        print("wrote", f"public/learn/{a['slug']}.html")
    for old in OUT.glob("*.html"):
        if old.name not in keep:
            old.unlink(); print("removed", old.name)
    # Learn hub list, grouped by topic
    topics = {}
    for a in ARTICLES:
        topics.setdefault(a["topic"], []).append(a)
    cards = "".join(
        f'<div class="art-topic"><h3>{t}</h3><ul>' + "".join(f'<li><a href="learn/{a["slug"]}.html">{a["h1"]}</a></li>' for a in items) + "</ul></div>"
        for t, items in topics.items())
    hub = PUB / "learn.html"
    hub.write_text(between(hub.read_text(encoding="utf-8"), "<!-- articles:start -->", "<!-- articles:end -->",
                           f'        <div class="art-list">{cards}</div>'), encoding="utf-8")
    sm = PUB / "sitemap.xml"
    lines = "\n".join(f'  <url><loc>{SITE}/learn/{a["slug"]}</loc><lastmod>{a["reviewed"]}</lastmod><priority>0.6</priority></url>' for a in ARTICLES)
    sm.write_text(between(sm.read_text(encoding="utf-8"), "<!-- articles:start -->", "<!-- articles:end -->", lines), encoding="utf-8")
    print("updated learn.html and sitemap.xml with", len(ARTICLES), "articles")


if __name__ == "__main__":
    main()
