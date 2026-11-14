"""Builds the stand-alone site pages: How it works, Clinicians, Pricing, About, Contact.

Run from the repo root:  python -I tools/build_pages.py
Copy lives in tools/pages.py. Prices on the Pricing page are read from the program data in
tools/build_programs.py, never typed here. Writes public/<slug>.html and refreshes the page
lines in public/sitemap.xml between its markers.
No analytics tag on these pages until Dourado makes the health-privacy call.
"""
import html
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
SITE = "https://www.velacorehealth.com"
SCHEMA_TYPE = {"about": "AboutPage", "contact": "ContactPage"}


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bp = load("build_programs")
PAGES = load("pages").PAGES


def price_table():
    """One card per program, every figure read from the program data."""
    cards = []
    for p in bp.PROGRAMS:
        plans = "".join(
            f'<div class="pt-plan"><span class="pt-label">{pl["label"]}</span>'
            f'<span class="pt-price">{pl["price"]}<small>{pl["unit"]}</small></span>'
            f'<span class="pt-note">{pl["note"]}</span></div>' for pl in p["plans"])
        cards.append(f'<div class="pt-card"><h3><a href="programs/{p["slug"]}.html">{p["name"]}</a></h3>{plans}</div>')
    return '<div class="pt-grid">' + "".join(cards) + "</div>"


def block(text):
    if text.strip() == "{{price_table}}":
        return price_table()
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if lines and all(l.startswith("- ") for l in lines):
        return "<ul>" + "".join(f"<li>{l[2:]}</li>" for l in lines) + "</ul>"
    if lines and all(re.match(r"\d+\. ", l) for l in lines):
        return "<ol>" + "".join("<li>" + re.sub(r"^\d+\. ", "", l) + "</li>" for l in lines) + "</ol>"
    return f"<p>{text.strip()}</p>"


def plain(text):
    return html.unescape(re.sub(r"<[^>]+>", "", text))


def page(a):
    url = f"{SITE}/{a['slug']}"
    sections = "".join(f"<h2>{h}</h2>" + "".join(block(b) for b in bs) for h, bs in a["sections"])
    faq = "".join(f'<details class="faq-item"><summary>{q}</summary><div class="faq-body"><p>{ans}</p></div></details>' for q, ans in a.get("faq", []))
    ld = [
        {"@context": "https://schema.org", "@type": SCHEMA_TYPE.get(a["slug"], "WebPage"), "name": a["h1"], "description": a["meta"], "url": url,
         "publisher": {"@type": "Organization", "name": "Velacore Health", "logo": {"@type": "ImageObject", "url": f"{SITE}/logo-full.png"}}},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": a["h1"], "item": url}]},
    ]
    if a.get("faq"):
        ld.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": plain(q), "acceptedAnswer": {"@type": "Answer", "text": plain(ans)}} for q, ans in a["faq"]]})
    ld_html = "\n".join(f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    faq_html = f'<section class="art-faq" aria-label="Common questions"><h2>Common questions</h2><div class="faq">{faq}</div></section>' if faq else ""
    programs = "".join(f'<a href="programs/{p["slug"]}.html">{p["name"]}</a>' for p in bp.PROGRAMS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- No analytics on this page until Dourado makes the health-privacy call. -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(a["title"])} | Velacore Health</title>
  <meta name="description" content="{html.escape(a["meta"])}" />
  <meta name="theme-color" content="#15302A" />
  <meta property="og:title" content="{html.escape(a["title"])}" />
  <meta property="og:description" content="{html.escape(a["meta"])}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/images/og.png" />
  <link rel="canonical" href="{url}" />
{ld_html}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400..700,0..100;1,9..144,400..700,0..100&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="icon" href="logo-mark.png" />
</head>
<body class="article-page">
  <div class="topbar"><span>Clinician-reviewed telehealth, available in <b>all 50 states</b>. Prescription required.</span></div>
  <header class="site-header" id="top">
    <div class="container nav">
      <a href="index.html" class="brand" aria-label="Velacore Health home">
        <img class="brand-mark" src="logo-mark.png" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span>
      </a>
      <nav class="nav-links" id="navLinks" aria-label="Primary">
        {bp.mega_menu("")}
        <a href="how-it-works.html">How it works</a>
        <a href="learn.html">Learn</a>
        <a href="clinicians.html">Clinicians</a>
        <a href="faq.html">FAQ</a>
        <a href="index.html#goals" class="btn btn-primary btn-sm" data-find>Find your program</a>
      </nav>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </header>

  <main>
    <article class="section art">
      <div class="container art-wrap">
        <p class="crumbs"><a href="index.html">Home</a> / {a["h1"]}</p>
        <h1>{a["h1"]}</h1>
        <p class="art-answer">{a["lede"]}</p>
        <div class="art-body">
{sections}
        </div>
        {faq_html}
        <p class="edu-note">Prescription required. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. Whether any treatment is appropriate for you is decided solely by a licensed clinician.</p>
        <div class="art-next">
          <a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a>
        </div>
      </div>
    </article>
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="brand"><img class="brand-mark" src="logo-mark.png" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span></a>
        <p>A telehealth platform coordinating access to licensed clinicians and 503A compounding pharmacies.</p>
      </div>
      <nav class="footer-col" aria-label="Programs"><h4>Programs</h4>
        {programs}</nav>
      <nav class="footer-col" aria-label="More"><h4>More</h4>
        <a href="how-it-works.html">How it works</a><a href="clinicians.html">Clinicians</a><a href="pricing.html">Pricing</a><a href="learn.html">Learn</a><a href="faq.html">FAQ</a><a href="about.html">About</a><a href="contact.html">Contact</a></nav>
      <nav class="footer-col" aria-label="Legal"><h4>Legal</h4>
        <a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Service</a><a href="telehealth-consent.html">Telehealth Consent</a><a href="refund-policy.html">Refund Policy</a></nav>
    </div>
    <div class="container footer-legal">
      <p class="states-served">Velacore Health telehealth services are available in all 50 US states and the District of Columbia. Every prescription requires review by a clinician licensed for your state. Prescription required.</p>
      <p class="disclaimer"><b>Important:</b> Velacore Health does not provide, guarantee, or facilitate any medical services, prescriptions, or treatments. The platform coordinates access to licensed clinicians and 503A compounding pharmacies; all medical decisions are made solely by the independent clinician. All medications are prescription only. Compounded medications are not FDA approved. Content on this site is for general informational purposes only and is not medical advice. Always consult a qualified healthcare provider.</p>
      <div class="footer-bottom"><p>© <span id="year"></span> Velacore Health, First Venture Group LLC. All rights reserved.</p>
      <nav aria-label="Legal"><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="telehealth-consent.html">Telehealth consent</a><a href="refund-policy.html">Refund policy</a></nav></div>
    </div>
  </footer>
  <script src="script.js"></script>
</body>
</html>
"""


def between(text, start, end, new):
    i, j = text.index(start) + len(start), text.index(end)
    return text[:i] + "\n" + new + "\n" + text[j:]


def main():
    for a in PAGES:
        assert len(a["title"]) <= 60, (a["slug"], "title over 60", len(a["title"]))
        assert len(a["meta"]) <= 155, (a["slug"], "meta over 155", len(a["meta"]))
        assert "$" not in json.dumps(a), (a["slug"], "a price is typed in the copy")
        (PUB / f"{a['slug']}.html").write_text(page(a), encoding="utf-8")
        print("wrote", f"public/{a['slug']}.html")
    sm = PUB / "sitemap.xml"
    lines = "\n".join(f'  <url><loc>{SITE}/{a["slug"]}</loc><priority>0.7</priority></url>' for a in PAGES)
    sm.write_text(between(sm.read_text(encoding="utf-8"), "<!-- pages:start -->", "<!-- pages:end -->", lines), encoding="utf-8")
    print("updated sitemap.xml with", len(PAGES), "pages")


if __name__ == "__main__":
    main()
