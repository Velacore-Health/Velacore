"""Builds one page per program into public/programs/<slug>.html from the data below.

Run from the repo root after any change to prices, wording or the template:
    python -I tools/build_programs.py

Prices come from docs/pricing-research.md section 5. Facts come from
docs/openloop-proposal-notes.md. Nothing here may make an outcome claim.
"""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "programs"


def img_size(rel):
    """Real width and height of a public image, read with ffprobe, so the page tags match the file."""
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0",
                              str(ROOT / "public" / "images" / rel)], capture_output=True, text=True, check=True)
        w, h = out.stdout.strip().split(",")[:2]
        return int(w), int(h)
    except Exception:
        return 760, 950

PROGRAMS = [
    {
        "slug": "tirzepatide", "name": "Tirzepatide", "cat": "Weight", "image": "products/tirzepatide.webp",
        "title": "Tirzepatide Program, Reviewed Online",
        "meta": "Compounded tirzepatide injection reviewed and prescribed by licensed clinicians in all 50 states. $199 first month, then $279 a month, shipping included. Prescription required.",
        "lede": "A dual GIP and GLP-1 receptor agonist, prepared as an injection by a licensed 503A compounding pharmacy and prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Injection, 5 dose levels", "Ships every 4 weeks"],
        "plans": [
            {"id": "monthly", "label": "Month to month", "price": "$279", "unit": "/mo", "note": "$199 your first month, then $279 a month. Cancel any time."},
            {"id": "12week", "label": "12-week plan", "price": "$249", "unit": "/mo", "note": "$747 charged up front, shipped every 4 weeks."},
        ],
        "what_h": "What tirzepatide is",
        "what": [
            "Tirzepatide is a peptide that acts on two receptors, GIP and GLP-1, both involved in blood sugar regulation and appetite signaling. It is given as a small injection under the skin.",
            "The compounded version is prepared by a licensed 503A compounding pharmacy to your clinician's prescription. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
        ],
        "facts": ["Dual GIP and GLP-1 receptor agonist", "Five dose levels, 8.5 mg to 44.5 mg per 4-week cycle", "Injection supplies and written instructions included", "Clinician review before every dose change", "Baseline labs at a national lab, included", "Optional nausea medication at a local pharmacy, if your clinician prescribes it"],
        "journey": [
            ("Online intake", "You answer questions about your health, history and goals. A licensed clinician in your state reviews it, usually without a live appointment. A video visit is available on request and required for the first prescription in a few states."),
            ("First prescription and labs", "If appropriate, the clinician prescribes the starting dose and orders baseline labs at a national laboratory at no cost to you. In most cases you can start before the results are back."),
            ("Monthly reviews", "Each month you update a short intake. The clinician reviews it with your labs and decides whether to hold or raise the dose. Nothing changes without that review."),
            ("Steady dose, quarterly reviews", "Once your dose is steady, reviews move to every three months. Refills, changes and cancellation run through your patient portal."),
        ],
        "eligibility": "Adults 18 to 74 with a body mass index of 27 or above, or 25 or above with a related health condition. The clinician makes the final decision on every intake.",
        "faq": [
            ("Is this the same as a brand-name medication?", "No. This is a compounded medication prepared by a licensed 503A pharmacy to your clinician's prescription. Compounded medications are not FDA approved. Your clinician will discuss what that means for you."),
            ("How is the dose decided?", "Your clinician starts at the lowest level and reviews a short update from you each month before any increase. There are five levels. You never move up without a review."),
            ("What does the price include?", "The medication, injection supplies, clinician reviews, baseline labs at a national laboratory, shipping, and patient support around the clock. There is no separate consultation or physician fee."),
            ("What if I am not prescribed?", "Nothing is ordered and your program payment is refunded in full."),
            ("Can I switch plans or cancel?", "Yes. Cancel any time for any reason from your patient portal. Any month whose medication has not been ordered is refunded."),
        ],
    },
    {
        "slug": "semaglutide", "name": "Semaglutide", "cat": "Weight", "image": "products/semaglutide.webp",
        "title": "Semaglutide Program, Reviewed Online",
        "meta": "Compounded semaglutide injection reviewed and prescribed by licensed clinicians in all 50 states. $149 first month, then $229 a month, shipping included. Prescription required.",
        "lede": "A GLP-1 receptor agonist, prepared as an injection by a licensed 503A compounding pharmacy and prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Injection, 5 dose levels", "Ships every 4 weeks"],
        "plans": [
            {"id": "monthly", "label": "Month to month", "price": "$229", "unit": "/mo", "note": "$149 your first month, then $229 a month. Cancel any time."},
            {"id": "12week", "label": "12-week plan", "price": "$199", "unit": "/mo", "note": "$597 charged up front, shipped every 4 weeks."},
        ],
        "what_h": "What semaglutide is",
        "what": [
            "Semaglutide is a peptide that acts on the GLP-1 receptor, a pathway involved in blood sugar regulation and appetite signaling. It is given as a small injection under the skin.",
            "The compounded version is prepared by a licensed 503A compounding pharmacy to your clinician's prescription. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
        ],
        "facts": ["GLP-1 receptor agonist", "Five dose levels, 0.8 mg to 8.96 mg per 4 weeks", "Injection supplies and written instructions included", "Clinician review before every dose change", "Baseline labs at a national lab, included", "Optional nausea medication at a local pharmacy, if your clinician prescribes it"],
        "journey": [
            ("Online intake", "You answer questions about your health, history and goals. A licensed clinician in your state reviews it, usually without a live appointment. A video visit is available on request and required for the first prescription in a few states."),
            ("First prescription and labs", "If appropriate, the clinician prescribes the starting dose and orders baseline labs at a national laboratory at no cost to you. In most cases you can start before the results are back."),
            ("Monthly reviews", "Each month you update a short intake. The clinician reviews it with your labs and decides whether to hold or raise the dose. Nothing changes without that review."),
            ("Steady dose, quarterly reviews", "Once your dose is steady, reviews move to every three months. Refills, changes and cancellation run through your patient portal."),
        ],
        "eligibility": "Adults 18 to 74 with a body mass index of 27 or above, or 25 or above with a related health condition. The clinician makes the final decision on every intake.",
        "faq": [
            ("Is this the same as a brand-name medication?", "No. This is a compounded medication prepared by a licensed 503A pharmacy to your clinician's prescription. Compounded medications are not FDA approved. Your clinician will discuss what that means for you."),
            ("How is the dose decided?", "Your clinician starts at the lowest level and reviews a short update from you each month before any increase. There are five levels. You never move up without a review."),
            ("What does the price include?", "The medication, injection supplies, clinician reviews, baseline labs at a national laboratory, shipping, and patient support around the clock. There is no separate consultation or physician fee."),
            ("What if I am not prescribed?", "Nothing is ordered and your program payment is refunded in full."),
            ("Can I switch plans or cancel?", "Yes. Cancel any time for any reason from your patient portal. Any month whose medication has not been ordered is refunded."),
        ],
    },
    {
        "slug": "microdosing", "name": "Microdosing GLP-1", "cat": "Weight, entry tier", "image": "products/microdosing.webp",
        "title": "Microdosing GLP-1 Program, Reviewed Online",
        "meta": "Low-dose GLP-1 combined with NAD+, B12 or amino acids, oral or injection, prescribed by licensed clinicians. $129 first month, then $179 a month, shipping included. Prescription required.",
        "lede": "A low dose of a GLP-1 medication combined with NAD+, B12 or amino acids, in an oral or injectable form, prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Oral or injection, 7 formulations", "Ships every 4 weeks"],
        "plans": [
            {"id": "monthly", "label": "Month to month", "price": "$179", "unit": "/mo", "note": "$129 your first month, then $179 a month. Cancel any time."},
            {"id": "12week", "label": "12-week plan", "price": "$159", "unit": "/mo", "note": "$477 charged up front, shipped every 4 weeks."},
        ],
        "what_h": "What the microdosing program is",
        "what": [
            "The program uses a GLP-1 medication at a lower dose than the standard weight programs, combined in one preparation with ingredients such as NAD+, B12, L-carnitine, inositol, methionine, choline, magnesium or L-theanine. There are seven formulations, in oral or injectable form, and your clinician picks the one that fits your intake.",
            "Each preparation is compounded by a licensed 503A pharmacy to your clinician's prescription. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. Ingredient availability can vary by state and pharmacy.",
        ],
        "facts": ["Low-dose GLP-1 plus vitamins or amino acids", "Seven formulations, oral or injection", "Clinician consults, unlimited, at no extra cost", "Async review on a 12-week cycle, video any time", "Supplies and written instructions included", "Patient support 24 hours a day"],
        "journey": [
            ("Online intake", "You answer questions about your health, history and goals. A licensed clinician in your state reviews it, usually without a live appointment. A video visit is available on request and required for the first prescription in a few states."),
            ("First prescription", "If appropriate, the clinician chooses the formulation and form and prescribes a 4-week supply."),
            ("12-week reviews", "Every 12 weeks you update a short intake and the clinician reviews it. You can request a video visit at any time at no extra cost."),
            ("Ongoing", "Refills ship every 4 weeks. Changes and cancellation run through your patient portal."),
        ],
        "eligibility": "Adults 18 to 74 with a body mass index over 20. The clinician makes the final decision on every intake.",
        "faq": [
            ("How is this different from the standard semaglutide or tirzepatide programs?", "The GLP-1 dose is lower, it is combined with other ingredients in one preparation, there are oral options, and the clinician reviews on a 12-week cycle rather than monthly. The clinician decides which program fits your intake."),
            ("Which formulation will I get?", "Your clinician chooses from seven, based on your intake. Options include oral and injectable forms with NAD+, B12, L-carnitine, inositol, magnesium, L-theanine, methionine or choline."),
            ("What does the price include?", "The medication, supplies, unlimited clinician consults, shipping, and patient support around the clock. There is no separate consultation or physician fee."),
            ("What if I am not prescribed?", "Nothing is ordered and your program payment is refunded in full."),
            ("Can I cancel?", "Yes. Cancel any time for any reason from your patient portal. Any month whose medication has not been ordered is refunded."),
        ],
    },
    {
        "slug": "nad", "name": "NAD+", "cat": "Vitality", "image": "products/nad.webp",
        "title": "NAD+ Program, Reviewed Online",
        "meta": "NAD+ as an injection, nasal spray or oral dropper, prescribed by licensed clinicians in all 50 states. $129 first month, then $199 a month, shipping included. Prescription required.",
        "lede": "Nicotinamide adenine dinucleotide, a coenzyme found in every cell, prepared as an injection, nasal spray or oral dropper by a licensed 503A compounding pharmacy and prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Injection, nasal or oral", "Ships every 4 weeks"],
        "plans": [
            {"id": "monthly", "label": "Month to month", "price": "$199", "unit": "/mo", "note": "$129 your first month, then $199 a month. Cancel any time."},
            {"id": "12week", "label": "12-week plan", "price": "$169", "unit": "/mo", "note": "$507 charged up front, shipped every 4 weeks."},
        ],
        "what_h": "What NAD+ is",
        "what": [
            "NAD+ is a coenzyme the body makes and uses in cellular energy metabolism. In this program it is prepared by a licensed 503A compounding pharmacy as an injection, a nasal spray or an oral dropper, at a dose your clinician sets.",
            "Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. Whether NAD+ is appropriate for you is the clinician's decision.",
        ],
        "facts": ["Injection, nasal spray or oral dropper", "50 mg to 200 mg per dose, set by your clinician", "Supplies and written instructions included", "Clinician review at each refill", "Video visit on request, at no extra cost", "Patient support 24 hours a day"],
        "journey": [
            ("Online intake", "You answer questions about your health, history and goals. A licensed clinician in your state reviews it, usually without a live appointment. A video visit is available on request and required for the first prescription in a few states."),
            ("First prescription", "If appropriate, the clinician prescribes a 4-week supply in the form that fits you."),
            ("Refill review at 3 to 4 weeks", "You update a short intake and the clinician reviews it before writing a 12-week refill."),
            ("12-week reviews", "Reviews continue every 12 weeks. Refills ship every 4 weeks. Changes and cancellation run through your patient portal."),
        ],
        "eligibility": "Adults 18 and over, per our Terms of Service. The clinician makes the final decision on every intake.",
        "faq": [
            ("Which form should I choose?", "Your clinician decides the form and dose from your intake. The injection, nasal spray and oral dropper deliver different amounts per dose."),
            ("Do I need labs?", "Not as a rule. Your clinician will tell you if labs are recommended for you."),
            ("What does the price include?", "The medication, supplies, clinician reviews, shipping, and patient support around the clock. There is no separate consultation or physician fee."),
            ("What if I am not prescribed?", "Nothing is ordered and your program payment is refunded in full."),
            ("Can I cancel?", "Yes. Cancel any time for any reason from your patient portal. Any month whose medication has not been ordered is refunded."),
        ],
    },
    {
        "slug": "sermorelin", "name": "Sermorelin", "cat": "Hormone support", "image": "products/sermorelin.webp",
        "title": "Sermorelin Program, Reviewed Online",
        "meta": "Compounded sermorelin injection prescribed by licensed clinicians in all 50 states. $129 first month, then $199 a month, shipping included. Prescription required.",
        "lede": "A growth hormone-releasing hormone analog, prepared as an injection by a licensed 503A compounding pharmacy and prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Injection", "Ships every 4 weeks"],
        "plans": [
            {"id": "monthly", "label": "Month to month", "price": "$199", "unit": "/mo", "note": "$129 your first month, then $199 a month. Cancel any time."},
            {"id": "12week", "label": "12-week plan", "price": "$169", "unit": "/mo", "note": "$507 charged up front, shipped every 4 weeks."},
        ],
        "what_h": "What sermorelin is",
        "what": [
            "Sermorelin is a peptide analog of growth hormone-releasing hormone, the signal the body uses to prompt its own growth hormone release. It is given as a small injection under the skin at a dose your clinician sets.",
            "The compounded version is prepared by a licensed 503A compounding pharmacy to your clinician's prescription. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
        ],
        "facts": ["Growth hormone-releasing hormone analog", "500 to 600 mcg per dose, set by your clinician", "Injection supplies and written instructions included", "Clinician review at each refill", "Video visit on request, at no extra cost", "Patient support 24 hours a day"],
        "journey": [
            ("Online intake", "You answer questions about your health, history and goals. A licensed clinician in your state reviews it, usually without a live appointment. A video visit is available on request and required for the first prescription in a few states."),
            ("First prescription", "If appropriate, the clinician prescribes a 4-week supply."),
            ("Refill review at 3 to 4 weeks", "You update a short intake and the clinician reviews it before writing a 12-week refill."),
            ("12-week reviews", "Reviews continue every 12 weeks. Refills ship every 4 weeks. Changes and cancellation run through your patient portal."),
        ],
        "eligibility": "Adults 18 and over, per our Terms of Service. The clinician makes the final decision on every intake.",
        "faq": [
            ("Is sermorelin the same as growth hormone?", "No. Sermorelin is an analog of the releasing hormone, not growth hormone itself. Whether it is appropriate for you is the clinician's decision."),
            ("Do I need labs?", "Not as a rule. Your clinician will tell you if labs are recommended for you."),
            ("What does the price include?", "The medication, injection supplies, clinician reviews, shipping, and patient support around the clock. There is no separate consultation or physician fee."),
            ("What if I am not prescribed?", "Nothing is ordered and your program payment is refunded in full."),
            ("Can I cancel?", "Yes. Cancel any time for any reason from your patient portal. Any month whose medication has not been ordered is refunded."),
        ],
    },
]

MENU = [
    ("Weight", [("tirzepatide", "Tirzepatide", "images/products/tirzepatide.webp", "Dual GIP / GLP-1 injection"),
                ("semaglutide", "Semaglutide", "images/products/semaglutide.webp", "GLP-1 injection"),
                ("microdosing", "Microdosing GLP\u20111", "images/products/microdosing.webp", "Low dose, oral or injection")]),
    ("Vitality", [("nad", "NAD+", "images/products/nad.webp", "Injection, nasal or oral")]),
    ("Hormone support", [("sermorelin", "Sermorelin", "images/products/sermorelin.webp", "GHRH analog injection")]),
]


def mega_menu(prefix):
    """The Treatments dropdown. prefix is '' on the home page and '../' on program pages."""
    cols = []
    for cat, items in MENU:
        rows = []
        for slug, name, img, sub in items:
            thumb = f'<img src="{prefix}{img}" alt="" width="54" height="54" loading="lazy" />' if img and (ROOT / "public" / img).exists() else f'<img class="mega-tile" src="{prefix}logo-mark.png" alt="" width="119" height="128" loading="lazy" />'
            rows.append(f'<a class="mega-item" href="{prefix}programs/{slug}.html">{thumb}<span><b>{name}</b><small>{sub}</small></span></a>')
        cols.append(f'<div class="mega-col"><h4>{cat}</h4>{"".join(rows)}</div>')
    return (f'<div class="nav-item has-mega"><a href="{prefix}index.html#treatments" aria-haspopup="true" aria-expanded="false">Treatments</a>'
            f'<div class="mega" role="menu">{"".join(cols)}'
            f'<div class="mega-col mega-cta"><h4>Not sure?</h4><p>Start the online visit and a licensed clinician will help determine what is appropriate.</p>'
            f'<a class="btn btn-primary btn-sm" href="{prefix}index.html#intake">Start online visit</a></div></div></div>')


GA = """  <script async src="https://www.googletagmanager.com/gtag/js?id=G-B2PQL4DLF8"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-B2PQL4DLF8');
  </script>"""

GLYPH = """<svg class="node-glyph" style="width:150px;height:150px" viewBox="0 0 80 80" fill="none" stroke="#0C8F72" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="40" cy="40" r="22"/><circle cx="40" cy="40" r="5" fill="#57D9B6" stroke="none"/><path d="M40 18v6M40 56v6M18 40h6M56 40h6"/><circle cx="24" cy="24" r="2.6" fill="#57D9B6" stroke="none"/><circle cx="56" cy="24" r="2.6" fill="#57D9B6" stroke="none"/><circle cx="24" cy="56" r="2.6" fill="#57D9B6" stroke="none"/><circle cx="56" cy="56" r="2.6" fill="#57D9B6" stroke="none"/></svg>"""

TRUST = """    <div class="trust-bar">
      <div class="container trust-items">
        <span>Licensed clinicians in all 50 states</span>
        <span>503A compounding pharmacies</span>
        <span>HIPAA-compliant intake on our partner's platform</span>
        <span>Shipping included, no hidden fees</span>
      </div>
    </div>"""

DISCLAIMER = "Prescription required. Starting a visit is not a guarantee of treatment. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. Individual results vary. Not appropriate for everyone. Your clinician decides whether this program is appropriate for you."


def start_button(p, cls="btn btn-primary"):
    return f'<a class="{cls}" href="#" data-intake="{"nad+" if p["slug"] == "nad" else p["slug"]}" aria-disabled="true">Start your visit</a>'


def page(p):
    media = f'<img class="tcard-photo" src="../images/{p["image"]}" width="{img_size(p["image"])[0]}" height="{img_size(p["image"])[1]}" alt="Velacore Health {p["name"]}" fetchpriority="high" />' if p["image"] and (ROOT / "public" / "images" / p["image"]).exists() else '<img class="brand-tile" src="../logo-mark.png" alt="" width="119" height="128" />'
    plans = "\n".join(
        f'''          <label class="plan-option">
            <input type="radio" name="plan" value="{pl["id"]}" data-price="{pl["price"]}" data-unit="{pl["unit"]}" data-note="{pl["note"]}"{" checked" if i == 0 else ""} />
            <span class="plan-name">{pl["label"]}</span><span class="plan-amt">{pl["price"]}{pl["unit"]}</span>
          </label>''' for i, pl in enumerate(p["plans"]))
    first = p["plans"][0]
    chips = "".join(f'<li class="chip"><span class="dot"></span> {c}</li>' for c in p["chips"])
    facts = "".join(f'<li><span class="check">✓</span> {f}</li>' for f in p["facts"])
    journey = "".join(
        f'''          <li class="step">
            <div class="step-num">{i}</div>
            <h3>{h}</h3>
            <p>{t}</p>
          </li>''' for i, (h, t) in enumerate(p["journey"], 1))
    faq = "".join(
        f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in p["faq"])
    what = "".join(f"<p>{x}</p>" for x in p["what"])
    faq_ld = ",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (q.replace('"', "'"), a.replace('"', "'")) for q, a in p["faq"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GA}
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p["title"]} | Velacore Health</title>
  <meta name="description" content="{p["meta"]}" />
  <meta name="theme-color" content="#15302A" />
  <meta property="og:title" content="{p["title"]} | Velacore Health" />
  <meta property="og:description" content="{p["meta"]}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.velacorehealth.com/programs/{p["slug"]}" />
  <meta property="og:image" content="https://www.velacorehealth.com/images/og.png" />
  <link rel="canonical" href="https://www.velacorehealth.com/programs/{p["slug"]}" />
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_ld}]}}
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400..700,0..100;1,9..144,400..700,0..100&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
  <link rel="icon" href="../logo-mark.png" />
</head>
<body class="prog-{p["slug"]}">
  <div class="topbar"><span>Clinician-reviewed telehealth, available in <b>all 50 states</b>. Prescription required.</span></div>
  <header class="site-header" id="top">
    <div class="container nav">
      <a href="../index.html" class="brand" aria-label="Velacore Health home">
        <img class="brand-mark" src="../logo-mark.png" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span>
      </a>
      <nav class="nav-links" id="navLinks" aria-label="Primary">
        {mega_menu("../")}
        <a href="../index.html#how">How it works</a>
        <a href="../learn.html">Learn</a>
        <a href="../index.html#provider">Clinicians</a>
        <a href="../faq.html">FAQ</a>
        <a href="#start" class="btn btn-primary btn-sm">Start online visit</a>
      </nav>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </header>

  <main>
    <section class="prog-hero">
      <div class="container">
        <p class="crumbs"><a href="../index.html">Home</a> / <a href="../index.html#treatments">Treatments</a> / {p["name"]}</p>
        <div class="prog-grid">
          <div class="prog-copy">
            <p class="eyebrow">{p["cat"]}</p>
            <h1>{p["name"]}</h1>
            <p class="hero-lede">{p["lede"]}</p>
            <ul class="hero-chips">{chips}</ul>
            <ul class="facts">{facts}</ul>
          </div>
          <div class="prog-side">
            <div class="tcard prog-media"><div class="tcard-media">{media}</div></div>
            <p class="img-note">Illustrative image. Your medication is prepared and labeled by a licensed 503A pharmacy and may look different.</p>
            <div class="price-box" id="priceBox">
              <div class="price-top">
                <span class="price-big" id="planPrice">{first["price"]}<small id="planUnit">{first["unit"]}</small></span>
                <span class="tcard-rx">Rx only</span>
              </div>
              <p class="price-note" id="planNote">{first["note"]}</p>
              <div class="plan-select" role="radiogroup" aria-label="Choose a plan">
{plans}
              </div>
              {start_button(p, "btn btn-primary btn-block")}
              <p class="price-fine">{DISCLAIMER}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

{TRUST}

    <section class="section on-cream">
      <div class="container prog-two">
        <div>
                    <h2>{p["what_h"]}</h2>
          <div class="prog-text">{what}</div>
        </div>
        <div class="prog-note">
          <h3>Who this program is for</h3>
          <p>{p["eligibility"]}</p>
          <p>Every program is prescription only. Velacore coordinates access and education; the licensed clinician decides; the 503A pharmacy fills.</p>
          {start_button(p, "btn btn-ghost")}
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <div class="section-head">
                    <h2>A review before every change, not just a refill</h2>
          <p class="section-sub">Velacore coordinates each step. A licensed clinician makes every prescribing decision.</p>
        </div>
        <ol class="steps steps-4">
{journey}
        </ol>
      </div>
    </section>

    <section class="section on-cream" id="faq">
      <div class="container faq-wrap">
        <div class="section-head center">
                    <h2>{p["name"]} questions, answered</h2>
        </div>
        <div class="faq" id="faqList">
{faq}
        </div>
        <p class="edu-note">More answers on the <a href="../faq.html">main FAQ</a>, the <a href="../refund-policy.html">refund policy</a> and the <a href="../telehealth-consent.html">telehealth consent</a>.</p>
      </div>
    </section>

    <section class="section" id="start">
      <div class="container cta-grid">
        <div class="cta-copy">
                    <h2>Start your {p["name"]} visit.</h2>
          <p>You complete a secure intake on our telehealth partner's pages, a licensed clinician reviews it, and if treatment is appropriate your medication ships to your door.</p>
          <ul class="cta-points">
            <li><span class="dot"></span> A licensed clinician makes the prescribing decision</li>
            <li><span class="dot"></span> Refunded in full if not prescribed</li>
            <li><span class="dot"></span> Filled by a licensed 503A pharmacy, shipping included</li>
            <li><span class="dot"></span> Cancel any time from your patient portal</li>
          </ul>
        </div>
        <div class="intake-card intake-list">
          {start_button(p, "btn btn-primary btn-block")}
          <a class="btn btn-ghost btn-block" href="../index.html#treatments">See all programs</a>
          <p class="intake-fine">{DISCLAIMER}</p>
        </div>
      </div>
    </section>

    <section class="please-note">
      <div class="container">
        <p><b>Please note:</b> Velacore Health is a telehealth platform. We do not provide, guarantee, or facilitate any medical services, prescriptions, or treatments. Our platform coordinates access to licensed clinicians and 503A compounding pharmacies. All medical decisions are made solely by the independent clinician. All medications are prescription only and require a valid prescription. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.</p>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="container footer-grid">
      <div class="footer-brand">
        <a href="../index.html" class="brand"><img class="brand-mark" src="../logo-mark.png" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span></a>
        <p>A telehealth platform coordinating access to licensed clinicians and 503A compounding pharmacies.</p>
      </div>
      <nav class="footer-col" aria-label="Programs"><h4>Programs</h4>
        <a href="tirzepatide.html">Tirzepatide</a><a href="semaglutide.html">Semaglutide</a><a href="microdosing.html">Microdosing GLP-1</a><a href="nad.html">NAD+</a><a href="sermorelin.html">Sermorelin</a></nav>
      <nav class="footer-col" aria-label="More"><h4>More</h4>
        <a href="../index.html#how">How it works</a><a href="../learn.html">Learn</a><a href="../faq.html">FAQ</a><a href="#" data-intake="portal" aria-disabled="true">Patient portal</a><a href="mailto:hello@velacorehealth.com">Contact</a></nav>
      <nav class="footer-col" aria-label="Legal"><h4>Legal</h4>
        <a href="../privacy.html">Privacy Policy</a><a href="../terms.html">Terms of Service</a><a href="../telehealth-consent.html">Telehealth Consent</a><a href="../refund-policy.html">Refund Policy</a></nav>
    </div>
    <div class="container footer-legal">
      <p class="states-served">Velacore Health telehealth services are available in all 50 US states and the District of Columbia. Every prescription requires review by a clinician licensed for your state. Prescription required.</p>
      <p class="disclaimer"><b>Important:</b> Velacore Health does not provide, guarantee, or facilitate any medical services, prescriptions, or treatments. The platform coordinates access to licensed clinicians and 503A compounding pharmacies; all medical decisions are made solely by the independent clinician. All medications are prescription only. Compounded medications are not FDA approved. Content on this site is for general informational purposes only and is not medical advice. Always consult a qualified healthcare provider.</p>
      <div class="footer-bottom"><p>© <span id="year"></span> Velacore Health · First Venture Group LLC. All rights reserved.</p>
      <nav aria-label="Legal"><a href="../privacy.html">Privacy</a><a href="../terms.html">Terms</a><a href="../telehealth-consent.html">Telehealth consent</a><a href="../refund-policy.html">Refund policy</a></nav></div>
    </div>
  </footer>

  <div class="mobile-cta" id="mobileCta" aria-hidden="false"><a href="#start" class="btn btn-primary btn-block">Start online visit</a></div>
  <script src="../script.js"></script>
</body>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in PROGRAMS:
        (OUT / f"{p['slug']}.html").write_text(page(p), encoding="utf-8")
        print("wrote", f"public/programs/{p['slug']}.html")


if __name__ == "__main__":
    main()
