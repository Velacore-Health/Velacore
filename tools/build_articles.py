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
    hero = bp.art_photo(a["hero"][0], a["hero"][1], "../", True, bp.PRODUCT_NOTE if a["hero"][0].startswith("products/") else "") if a.get("hero") else ""
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
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:site_name" content="Velacore Health" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{html.escape(a["title"])}" />
  <meta name="twitter:description" content="{html.escape(a["meta"])}" />
  <meta name="twitter:image" content="{SITE}/images/og.png" />
  <link rel="canonical" href="{url}" />
{ld_html}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
  <link rel="icon" href="../logo-mark.png" />
</head>
<body class="article-page">
  <div class="topbar"><span>A telehealth platform. Independent licensed clinicians decide. Prescription required.</span></div>
  <header class="site-header" id="top">
    <div class="container nav">
      <a href="../index.html" class="brand" aria-label="Velacore Health home">
        <img class="brand-mark" src="../logo-mark.svg" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span>
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
        {hero}
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
        <a href="../index.html" class="brand"><img class="brand-mark" src="../logo-mark.svg" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span></a>
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


# Learn hub card photo per article, files in public/images/learn/cards/<name>-480 and -960.
CARD_PHOTO = {
    "what-is-a-503a-compounding-pharmacy": "article-503a",
    "semaglutide-vs-tirzepatide": "article-sema-tirz",
    "what-is-microdosing-glp-1": "article-microdosing",
    "how-to-get-a-glp-1-prescription-online": "article-glp1-online",
}
PRODUCT_CARDS = {"article-503a", "article-sema-tirz", "article-microdosing"}
# Phone close-ups of one label, from tools/make_thumbs.py. The phone picture of the GLP-1 online card has no label.
PHONE_THUMB = {"what-is-a-503a-compounding-pharmacy": "nad", "what-is-microdosing-glp-1": "microdosing"}  # the comparison card keeps both vials so neither drug is singled out


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
    # Learn hub, Nov 18 2026 at Dourado's request for the Hims look: one photo card per article. Card photos are made
    # by tools/make_learn_cards.py; a card without one falls back to text only.
    def card(a):
        stem = f'images/learn/cards/{CARD_PHOTO.get(a["slug"], "")}'
        img = ""
        if a["slug"] in CARD_PHOTO and (PUB / f"{stem}-480.webp").exists():
            img = (f'<img src="{stem}-960.webp" srcset="{stem}-480.webp 480w, {stem}-960.webp 960w" '
                   f'sizes="(max-width:700px) 120px, (max-width:1000px) 45vw, 280px" width="960" height="640" alt="" loading="lazy" />')
            # On phones the card picture is about 120 px, too small to read a vial label, so it shows the label close-up.
            thumb = PHONE_THUMB.get(a["slug"])
            if thumb and (PUB / "images" / "products" / "thumbs" / f"{thumb}.webp").exists():
                img = f'<picture><source media="(max-width:700px)" srcset="images/products/thumbs/{thumb}.webp" />{img}</picture>'
        return f'<li><a class="art-card" href="learn/{a["slug"]}.html">{img}<span>{a["h1"]}</span></a></li>'
    cards = "".join(card(a) for a in ARTICLES)
    # three of the card photos show product vials, so the illustration note sits under the cards
    note = f'<p class="img-note art-note">{bp.PRODUCT_NOTE}</p>' if any(CARD_PHOTO.get(a["slug"]) in PRODUCT_CARDS for a in ARTICLES) else ""
    hub = PUB / "learn.html"
    hub.write_text(between(hub.read_text(encoding="utf-8"), "<!-- articles:start -->", "<!-- articles:end -->",
                           f'        <ul class="art-cards">{cards}</ul>{note}'), encoding="utf-8")
    sm = PUB / "sitemap.xml"
    lines = "\n".join(f'  <url><loc>{SITE}/learn/{a["slug"]}</loc><lastmod>{a["reviewed"]}</lastmod><priority>0.6</priority></url>' for a in ARTICLES)
    sm.write_text(between(sm.read_text(encoding="utf-8"), "<!-- articles:start -->", "<!-- articles:end -->", lines), encoding="utf-8")
    print("updated learn.html and sitemap.xml with", len(ARTICLES), "articles")


if __name__ == "__main__":
    main()
