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


NOTE = ("Prescription required. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. "
        "Whether any treatment is appropriate for you is decided solely by a licensed clinician.")


def flow_main(a, faq_html):
    """The visual layout: a short opening, the steps as photo rows, a refund band and two short lists.
    The long paragraphs are not typed again. Each step and band names a heading in a["sections"] and
    that section's text is folded under it."""
    f = a["flow"]
    sec = dict(a["sections"])

    def more(label, heading):
        return f'<details class="hw-more"><summary>{label}</summary><div class="hw-more-body">{"".join(block(b) for b in sec[heading])}</div></details>'

    glance = "".join(f'<li><a href="#step-{i}"><span class="hw-n">{i}</span>{s["short"]}</a></li>' for i, s in enumerate(f["steps"], 1))
    stepper = "".join(f'<li><a href="#step-{i}">{s["word"]}</a></li>' for i, s in enumerate(f["steps"], 1))
    steps = ""
    for i, s in enumerate(f["steps"], 1):
        facts = "".join(f"<li>{x}</li>" for x in s["facts"])
        note = f'<p class="hw-note">{s["note"]}</p>' if s.get("note") else ""
        steps += f"""
          <li class="hw-step" id="step-{i}">
            <figure class="hw-photo"><img src="images/lifestyle/{s["img"]}.webp" width="{s["w"]}" height="{s["h"]}" alt="{html.escape(s["alt"])}" loading="lazy"{' style="object-position:' + s["pos"] + '"' if s.get("pos") else ""} /></figure>
            <div class="hw-copy">
              <div class="hw-n">{i}</div>
              <h2>{s["title"]}</h2>
              <p class="hw-line">{s["line"]}</p>
              <ul class="hw-facts">{facts}</ul>{note}
              {more("More about this step", s["more"])}
            </div>
          </li>"""
    pr = f["promise"]
    does = "".join(f"<li>{x[2:]}</li>" for x in sec[f["scope"]][1].split("\n"))
    doesnt = "".join(f"<li>{x[2:]}</li>" for x in sec[f["scope"]][3].split("\n"))
    return f"""  <main>
    <section class="section on-cream page-top hw-top">
      <div class="container">
        <h1>{a["h1"]}</h1>
        <p class="hw-sub">{f["sub"]}</p>
        <div class="hw-cta"><a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a> <a href="pricing.html" class="btn btn-ghost">See prices</a></div>
        <ol class="hw-glance" aria-label="The four steps">{glance}</ol>
      </div>
    </section>
    <section class="section hw-body">
      <!-- Stepper, Nov 17 2026: one word per step, the current one lit as its step passes the middle of the screen -->
      <ol class="hw-stepper" data-stepper aria-label="Where you are in the four steps">{stepper}</ol>
      <div class="container">
        <ol class="hw-steps">{steps}
        </ol>
        <div class="hw-promise">
          <h2>{pr["title"]}</h2>
          <p>{pr["line"]}</p>
          <a href="refund-policy.html">Refund policy</a>
        </div>
        <div class="hw-scope">
          <h2>{f["scope"]}</h2>
          <div class="hw-split">
            <div class="hw-card"><h3>Velacore does</h3><ul class="hw-facts">{does}</ul></div>
            <div class="hw-card"><h3>Velacore does not</h3><ul class="hw-nots">{doesnt}</ul></div>
          </div>
          <p class="hw-partner">{sec[f["scope"]][4]}</p>
        </div>
        <div class="hw-faq">{faq_html}</div>
        <p class="edu-note">{NOTE}</p>
        <div class="art-next">
          <a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a>
        </div>
      </div>
    </section>
  </main>"""


def clinicians_main(a, faq_html):
    """Clinicians page, Nov 18 2026 at Dourado's request for a layout that is not one long column. The same parts as
    How it works: a split opening with the photo, four quick facts, two cards, photo rows that alternate sides, a
    glowing panel and the questions. Every sentence is read from a["sections"]; nothing is typed twice."""
    sec = dict(a["sections"])
    photos = a.get("photos", {})

    def pic(rel, alt, eager=False):
        stem = rel.split("/")[-1]
        small = ROOT / "public" / "images" / "lifestyle" / f"{stem}-800.webp"
        srcset = f' srcset="images/{rel}-800.webp 800w, images/{rel}.webp 1600w" sizes="(max-width:900px) 100vw, 560px"' if small.exists() else ""
        w, h = img_size(f"{rel}.webp")
        return (f'<figure class="hw-photo"><img src="images/{rel}.webp"{srcset} width="{w}" height="{h}" alt="{html.escape(alt)}"'
                f' loading="{"eager" if eager else "lazy"}" /></figure>')

    def body(heading, skip=()):
        return "".join(block(b) for i, b in enumerate(sec[heading]) if i not in skip)

    def checks(text, cls="hw-facts"):
        return f'<ul class="{cls}">' + "".join(f"<li>{l.strip()[2:]}</li>" for l in text.split("\n") if l.strip()) + "</ul>"

    facts = "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in CLIN_FACTS)
    cred = sec["Credentialed before they review an intake"]
    video = sec["Video visits"]
    decide = sec["What a clinician can decide"]
    states = "".join(f"<li>{l.strip()[2:]}</li>" for l in video[2].split("\n") if l.strip())
    rows = [
        ("Credentialed before they review an intake", f'<p>{cred[0]}</p>{checks(cred[1], "hw-facts cl-checks")}<p class="hw-note">{cred[2]}</p>'),
        ("Video visits", f'<p>{video[0]}</p><p>{video[1]}</p><ul class="cl-chips">{states}</ul><p>{video[3]}</p>'),
        ("What a clinician can decide", f'{checks(decide[0])}<p class="hw-note">{decide[1]}</p>'),
    ]
    row_html = "".join(f"""
          <li class="hw-step cl-row">
            {pic(*photos[h])}
            <div class="hw-copy">
              <h2>{h}</h2>
              {copy}
            </div>
          </li>""" for h, copy in rows)
    hero = pic(*a["hero"], eager=True) if a.get("hero") else ""
    return f"""  <main>
    <section class="section on-cream page-top hw-top cl-top">
      <div class="container">
        <div class="cl-hero">
          <div>
            <p class="crumbs"><a href="index.html">Home</a> / Clinicians</p>
            <h1>{a["h1"]}</h1>
            <p class="hw-sub">{a["lede"]}</p>
            <div class="hw-cta"><a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a> <a href="how-it-works.html" class="btn btn-ghost">How it works</a></div>
          </div>
          {hero}
        </div>
        <ul class="cl-facts">{facts}</ul>
      </div>
    </section>
    <section class="section hw-body cl-body">
      <div class="container">
        <div class="hw-split cl-split">
          <div class="hw-card"><h2>Who reviews your intake</h2>{body("Who reviews your intake")}</div>
          <div class="hw-card"><h2>Licensed in your state</h2>{body("Licensed in your state")}</div>
        </div>
        <ol class="hw-steps cl-rows">{row_html}
        </ol>
        <div class="hw-promise cl-promise">
          <h2>Independent of Velacore</h2>
          {body("Independent of Velacore")}
        </div>
        <div class="hw-card cl-hours"><h2>Hours</h2>{body("Hours")}</div>
        <div class="hw-faq">{faq_html}</div>
        <p class="edu-note">{NOTE}</p>
        <div class="art-next">
          <a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a>
        </div>
      </div>
    </section>
  </main>"""


# The four quick facts at the top of the Clinicians page. Each one restates a line already on the page.
CLIN_FACTS = [
    ("MD, DO and NP", "Physicians and nurse practitioners"),
    ("All 50 states and DC", "Licensed where you live"),
    ("7am to 7pm Central", "Clinician hours, not on holidays. Support runs 24 hours a day"),
    ("Video on request", "At no extra cost"),
]


def year_table():
    """Nov 20 2026, from the Bold You study: month to month plans are charged every 4 weeks, so a full year is 13 charges.
    One row per month to month price, each figure read from the program data and multiplied here, never typed."""
    def money(n):
        return f"${n:,}"
    rows = []
    for p in bp.PROGRAMS:
        for pl in p["plans"]:
            if pl["id"] not in ("monthly", "oral"):
                continue
            name = p["name"] + (", oral" if pl["id"] == "oral" else bp.injection(p))
            price = int(pl["price"].lstrip("$"))
            rows.append(f'<tr><th scope="row">{name}</th><td>{money(price)}</td><td>{money(price * bp.CHARGES_PER_YEAR)}</td></tr>')
    return ('<div class="yr"><h2>What a full year costs</h2>'
            f'<p class="hw-line">Month to month plans are charged {bp.PERIOD}, so a full year is {bp.CHARGES_PER_YEAR} charges, not 12.</p>'
            '<div class="yr-wrap"><table class="yr-table"><thead><tr><th scope="col">Program</th>'
            f'<th scope="col">Charged {bp.PERIOD}</th><th scope="col">{bp.CHARGES_PER_YEAR} charges, one year</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table></div>'
            '<p class="hw-note">The one year figure is the month to month price for a full year with no change in price. '
            'A prepaid plan is charged once, up front, at the price in its card.</p></div>')


# Nov 20 2026, Dourado: a card that lists two plans names the next step on its button, the plan picker that opens
# its Start page. Only the Semaglutide oral card keeps Start visit, since that form has one plan and no picker.
CARD_BUTTON = "Choose your plan"


def price_cards():
    """One card per program in the home page card style: vial photo, form line, monthly price, the
    12-week plan, Learn more and Start visit. Every figure is read from the program data in build_programs.py."""
    cards = []
    for p in bp.PROGRAMS:
        if not any(x["id"] == "monthly" for x in p["plans"]):
            cards.append(pack_card(p))
            continue
        monthly = next(x for x in p["plans"] if x["id"] == "monthly")
        week12 = next(x for x in p["plans"] if x["id"] == "12week")
        w = re.match(r"^(\$\d+) charged up front", week12["note"]); assert w, p["slug"]
        wi, he = img_size(p["image"])
        cards.append(
            f'<article class="tcard" data-cat="{ {"Vitality": "vitality", "Hormone support": "hormone"}.get(p["cat"], "weight") }" id="price-{p["slug"]}"><div class="tcard-media"><span class="tcard-cat">{p["cat"]}</span>'
            f'<img class="tcard-photo" src="images/{p["image"]}"{bp.prod_srcset(p["image"], "", "(max-width:700px) 92vw, 380px")} width="{wi}" height="{he}" alt="Illustration: {p["name"]} vial" loading="lazy" /></div>'
            f'<div class="tcard-body"><h3>{p["name"]}</h3><p class="tcard-mech">{p["chips"][1]}. {p["chips"][2]}.</p>'
            f'<div class="tcard-meta">{bp.tcard_price(p)}<span class="tcard-rx">Rx only</span></div>'
            f'<p class="tcard-plan">{bp.week12_line(p)}</p>'
            f'<a class="tcard-link" href="programs/{p["slug"]}.html">What the price includes</a>'
            f'<a href="start/{p["slug"]}.html" class="btn btn-primary btn-block btn-sm" data-start="{p["slug"]}">{CARD_BUTTON}</a></div></article>')
    return ('<div class="tgrid pr-grid">' + "".join(cards) + "</div>"
            + '<div class="section-head center pr-forms-head"><h2>Needle-free forms</h2><p class="section-sub">Each of these forms is taken '
              'without a needle. A licensed clinician decides which form is appropriate for you.</p></div>'
            + '<div class="tgrid pr-grid pr-forms-grid">' + "".join(form_cards()) + "</div>")


def form_cards():
    """Nov 20 2026, Dourado: the pricing page carries a card for each needle-free form the site lists, Semaglutide oral,
    NAD+ nasal spray, NAD+ oral dropper and the Microdosing GLP-1 oral options. Each form line and price is read from the
    program data in build_programs.py: the Semaglutide oral price from its oral plan, the NAD+ and Microdosing forms at
    their program's own price."""
    progs = {p["slug"]: p for p in bp.PROGRAMS}
    out = []

    def card(p, title, img, alt, mech, price, plan, link, start, button="Start visit"):
        wi, he = img_size(img)
        return (f'<article class="tcard" data-cat="{CAT_KEY.get(p["cat"], "weight")}" id="price-form-{start}"><div class="tcard-media"><span class="tcard-cat">{p["cat"]}</span>'
                f'<img class="tcard-photo" src="images/{img}"{bp.prod_srcset(img, "", "(max-width:700px) 92vw, 380px")} width="{wi}" height="{he}" alt="Illustration: {alt}" loading="lazy" /></div>'
                f'<div class="tcard-body"><h3>{title}</h3><p class="tcard-mech">{mech}</p>'
                f'<div class="tcard-meta">{price}<span class="tcard-rx">Rx only</span></div>'
                f'<p class="tcard-plan">{plan}</p>'
                f'<a class="tcard-link" href="{link}">What the price includes</a>'
                f'<a href="start/{start}.html" class="btn btn-primary btn-block btn-sm" data-start="{start}">{button}</a></div></article>')

    def week12(p):
        return bp.week12_line(p, oral=False)

    sema = progs["semaglutide"]
    oral = next(x for x in sema["plans"] if x["id"] == "oral")
    line = next(f for f in sema["forms"] if f[0] == "Oral")[2]
    out.append(card(sema, "Semaglutide oral", "products/semaglutide-oral.webp", "Semaglutide oral bottle",
                    re.sub(r"\s*\$\d+ every 4 weeks\.?$", "", line),
                    f'<span class="tcard-price">{oral["price"]} <small>{bp.PERIOD}, oral form</small></span>',
                    "Month to month. " + oral["note"].split(". ")[-1], "programs/semaglutide.html#forms", "semaglutide-oral"))
    nad = progs["nad"]
    for name, img, line in nad["forms"]:
        if name == "Injection":
            continue
        slug = "nad-" + {"Nasal spray": "nasal", "Oral dropper": "oral"}[name]
        out.append(card(nad, f"NAD+ {name.lower()}", img, f"NAD+ {name.lower()}", line, bp.tcard_price(nad), week12(nad),
                        "programs/nad.html#forms", slug, CARD_BUTTON))
    micro = progs["microdosing"]
    out.append(card(micro, "Microdosing GLP-1 oral", "products/microdosing-oral.webp", "Microdosing GLP-1 oral dropper bottle",
                    f'Oral options among the {re.search(r"(\d+) formulations", micro["chips"][1]).group(1)} formulations. The clinician picks the form.', bp.tcard_price(micro), week12(micro),
                    "programs/microdosing.html", "microdosing", CARD_BUTTON))
    return out


CAT_KEY = {"Vitality": "vitality", "Hormone support": "hormone", "Sexual health": "sexual", "Women's health": "women"}


def pack_card(p):
    """Nov 18 2026: the card for a program with no monthly plan, sexual health and women's HRT. Same look as the others;
    the price line comes from bp.price_line and each plan's own price, so nothing is typed twice."""
    if (PUB / "images" / p["image"]).exists():
        wi, he = img_size(p["image"])
        media = (f'<img class="tcard-photo" src="images/{p["image"]}"{bp.prod_srcset(p["image"], "", "(max-width:700px) 92vw, 380px")} '
                 f'width="{wi}" height="{he}" alt="Illustration: {p["name"]}" loading="lazy" />')
    else:
        media = '<img class="brand-tile" src="logo-mark.svg" alt="" width="119" height="128" loading="lazy" />'
    line = bp.price_line(p)
    big, small = (line.split(", ", 1) if ", billed " in line else (line, ""))
    plans = " ".join(f'{pl["label"]}: {"from " if pl["note"].startswith("From") else ""}{pl["price"]}{pl["unit"]}.' for pl in p["plans"]) if len(p["plans"]) > 1 else ""
    return (f'<article class="tcard" data-cat="{CAT_KEY.get(p["cat"], "weight")}" id="price-{p["slug"]}"><div class="tcard-media"><span class="tcard-cat">{p["cat"]}</span>{media}</div>'
            f'<div class="tcard-body"><h3>{p["name"]}</h3><p class="tcard-mech">{p["chips"][1]}. {p["chips"][2]}.</p>'
            f'<div class="tcard-meta"><span class="tcard-price">{big} <small>{small}</small></span><span class="tcard-rx">Rx only</span></div>'
            + (f'<p class="tcard-plan">{plans}</p>' if plans else "") +
            f'<a class="tcard-link" href="programs/{p["slug"]}.html">What the price includes</a>'
            f'<a href="start/{p["slug"]}.html" class="btn btn-primary btn-block btn-sm" data-start="{p["slug"]}">Start visit</a></div></article>')


def img_size(rel):
    return bp.img_size(rel)


def pricing_main(a, faq_html):
    """The pricing page as a visual page: cards first, then short bands. The long paragraphs in a["sections"]
    fold under the bands by heading, so nothing is typed twice."""
    sec = dict(a["sections"])
    def fold(label, heading):
        return f'<details class="hw-more"><summary>{label}</summary><div class="hw-more-body">{"".join(block(b) for b in sec[heading])}</div></details>'
    includes = "".join(f"<li>{x[2:]}</li>" for x in sec["What one price includes"][1].split("\n"))
    pay = sec["Two ways to pay"][1].split("\n")
    pay_cards = "".join(f'<div class="hw-card"><p>{x[2:]}</p></div>' for x in pay)
    nots = "".join(f"<li>{x[2:]}</li>" for x in sec["What is not included or not accepted"][0].split("\n"))
    return f"""  <main>
    <section class="section on-cream page-top hw-top">
      <div class="container">
        <h1>{a["h1"]}</h1>
        <p class="hw-sub">One price per program, shown before you start. No consultation fee, no physician fee, shipping included. Prescription required.</p>
        <div class="hw-cta"><a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a> <a href="how-it-works.html" class="btn btn-ghost">How it works</a></div>
      </div>
    </section>
    <section class="section pr-cards">
      <div class="container">
        <div class="section-head center"><h2>Programs and prices</h2><p class="section-sub">Pay month to month or choose a 12-week plan. A licensed clinician decides whether a program is appropriate for you.</p></div>
        {price_cards()}
        <p class="treat-note">{sec["Programs and prices"][1]} Product images are illustrations. Your medication is prepared and labeled by a licensed 503A pharmacy and may look different.</p>
      </div>
    </section>
    <section class="section on-cream">
      <div class="container">
        <div class="hw-split pr-split">
          <div>
            <h2>What one price includes</h2>
            <p class="hw-line">{sec["What one price includes"][0]}</p>
            <ul class="hw-facts">{includes}</ul>
            <p class="hw-note">{sec["What one price includes"][2]}</p>
          </div>
          <div>
            <h2>Two ways to pay</h2>
            <p class="hw-line">{sec["Two ways to pay"][0]}</p>
            <div class="pr-pay">{pay_cards}</div>
            <p class="hw-note">{sec["Two ways to pay"][2]}</p>
          </div>
        </div>
        {year_table()}
      </div>
    </section>
    <section class="section hw-body pr-body">
      <div class="container">
        <div class="hw-promise">
          <h2>Not prescribed? Your program payment is refunded in full.</h2>
          <p>You can cancel at any time, for any reason. Every billing period whose medication has not yet been ordered is refunded. Medications are non-returnable once dispensed.</p>
          {fold("More about refunds and cancellation", "Refunds and cancellation")}
          <a href="refund-policy.html">Refund policy</a>
        </div>
        <div class="hw-split pr-split2">
          <div class="hw-card"><h3>Not included or not accepted</h3><ul class="hw-nots">{nots}</ul></div>
          <div class="hw-card"><h3>Payment methods</h3><p>{sec["Payment methods"][0]}</p><p class="hw-note">{sec["Payment methods"][1]}</p></div>
        </div>
        <div class="hw-faq">{faq_html}</div>
        <p class="edu-note">{NOTE}</p>
        <div class="art-next">
          <a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a>
        </div>
      </div>
    </section>
  </main>"""


def page(a):
    url = f"{SITE}/{a['slug']}"
    photos = a.get("photos", {})
    sections = "".join(f"<h2>{h}</h2>" + (bp.art_photo(*photos[h]) if h in photos else "") + "".join(block(b) for b in bs) for h, bs in a["sections"])
    hero = bp.art_photo(*a["hero"], eager=True) if a.get("hero") else ""
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
    main_html = flow_main(a, faq_html) if a.get("flow") else pricing_main(a, faq_html) if a.get("pricing") else clinicians_main(a, faq_html) if a["slug"] == "clinicians" else f"""  <main>
    <article class="section art">
      <div class="container art-wrap">
        <p class="crumbs"><a href="index.html">Home</a> / {a["h1"]}</p>
        <h1>{a["h1"]}</h1>
        <p class="art-answer">{a["lede"]}</p>
        {hero}
        <div class="art-body">
{sections}
        </div>
        {faq_html}
        <p class="edu-note">{NOTE}</p>
        <div class="art-next">
          <a href="index.html#goals" class="btn btn-primary" data-find>Find your program</a>
        </div>
      </div>
    </article>
  </main>"""
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
  <meta property="og:image" content="{SITE}/images/og.jpg" />
  <meta property="og:image:width" content="1200" />
  <meta property="og:image:height" content="630" />
  <meta property="og:site_name" content="Velacore Health" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{html.escape(a["title"])}" />
  <meta name="twitter:description" content="{html.escape(a["meta"])}" />
  <meta name="twitter:image" content="{SITE}/images/og.jpg" />
  <link rel="canonical" href="{url}" />
{ld_html}
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="icon" href="logo-mark.png" />
</head>
<body class="article-page">
  <div class="topbar"><span>A telehealth platform. Independent licensed clinicians decide. Prescription required.</span></div>
  <header class="site-header" id="top">
    <div class="container nav">
      <a href="index.html" class="brand" aria-label="Velacore Health home">
        <img class="brand-mark" src="logo-mark.svg" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span>
      </a>
      <nav class="nav-links" id="navLinks" aria-label="Primary">
        {bp.mega_menu("")}
        <a href="how-it-works.html">How it works</a>
        <a href="learn.html">Learn</a>
        <a href="clinicians.html">Clinicians</a>
        <a href="faq.html">FAQ</a>
        <a href="index.html#goals" class="btn btn-primary btn-sm" data-find>Find your program</a>
      </nav>
      {bp.MENU_BUTTON}
    </div>
  </header>
  {bp.side_panel("")}

{main_html.rsplit('</main>', 1)[0]}
    {bp.goal_band('')}
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="brand" aria-label="Velacore Health home"><img class="brand-mark" src="logo-mark.svg" width="119" height="128" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span></a>
        <p>A telehealth platform coordinating access to licensed clinicians and 503A compounding pharmacies.</p>
      </div>
      <nav class="footer-col" aria-label="Programs"><h4>Programs</h4>
        {programs}</nav>
      <nav class="footer-col" aria-label="More"><h4>More</h4>
        <a href="how-it-works.html">How it works</a><a href="clinicians.html">Clinicians</a><a href="pricing.html">Pricing</a><a href="learn.html">Learn</a><a href="faq.html">FAQ</a><a href="about.html">About</a><a href="information-standards.html">Information standards</a><a href="contact.html">Contact</a></nav>
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
        assert "{{" in a["meta"] or len(a["meta"]) <= 155, (a["slug"], "meta over 155", len(a["meta"]))
        assert "$" not in json.dumps(a), (a["slug"], "a price is typed in the copy")
        if "{{low_then}}" in a["meta"]:
            # The lowest month to month price across programs, read from the program data.
            lows = [int(bp.monthly_price(q).lstrip("$")) for q in bp.PROGRAMS if any(x["id"] == "monthly" for x in q["plans"])]
            a = {**a, "meta": a["meta"].replace("{{low_then}}", "$" + str(min(lows)))}
            assert len(a["meta"]) <= 155, (a["slug"], "meta over 155", len(a["meta"]))
        (PUB / f"{a['slug']}.html").write_text(page(a), encoding="utf-8")
        print("wrote", f"public/{a['slug']}.html")
    sm = PUB / "sitemap.xml"
    lines = "\n".join(f'  <url><loc>{SITE}/{a["slug"]}</loc><priority>0.7</priority></url>' for a in PAGES)
    sm.write_text(between(sm.read_text(encoding="utf-8"), "<!-- pages:start -->", "<!-- pages:end -->", lines), encoding="utf-8")
    print("updated sitemap.xml with", len(PAGES), "pages")


if __name__ == "__main__":
    main()
