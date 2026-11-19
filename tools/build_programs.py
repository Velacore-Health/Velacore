"""Builds one page per program into public/programs/<slug>.html from the data below.

Run from the repo root after any change to prices, wording or the template:
    python -I tools/build_programs.py

Prices come from docs/pricing-research.md section 5. Facts come from
docs/openloop-proposal-notes.md. Nothing here may make an outcome claim.
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "programs"
START_OUT = ROOT / "public" / "start"
# Agile intake links, one per program, kept in one place: the site audit config. Empty until OpenLoop sends them.
INTAKE = json.loads((ROOT / ".claude/skills/vc-site-audit/audit-config.json").read_text(encoding="utf-8"))["intake_links"]


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
        "title": "Compounded Tirzepatide, Online Visit",
        "meta": "Compounded tirzepatide injection. A licensed clinician decides. $199 first month, then $279 a month. Shipping included. Prescription required.",
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
        "title": "Compounded Semaglutide, Online Visit",
        "meta": "Compounded semaglutide. A licensed clinician decides. Injection $149 first month, then $229 a month; oral $259 a month. Prescription required.",
        "lede": "A GLP-1 receptor agonist, prepared as an injection or an oral form by a licensed 503A compounding pharmacy and prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Injection or oral", "Ships every 4 weeks"],
        "plans": [
            {"id": "monthly", "label": "Injection, month to month", "price": "$229", "unit": "/mo", "note": "$149 your first month, then $229 a month. Cancel any time."},
            {"id": "12week", "label": "Injection, 12-week plan", "price": "$199", "unit": "/mo", "note": "$597 charged up front, shipped every 4 weeks."},
            {"id": "oral", "label": "Oral, month to month", "price": "$259", "unit": "/mo", "note": "$259 a month for the oral form, taken by mouth daily. Cancel any time."},
        ],
        "what_h": "What semaglutide is",
        "what": [
            "Semaglutide is a peptide that acts on the GLP-1 receptor, a pathway involved in blood sugar regulation and appetite signaling. It is given as a small injection under the skin, or taken by mouth daily in the oral form.",
            "The compounded version is prepared by a licensed 503A compounding pharmacy to your clinician's prescription. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
        ],
        "facts": ["GLP-1 receptor agonist", "Injection: five dose levels, 0.8 mg to 8.96 mg per 4 weeks", "Oral: 5 mg or 10 mg a day", "Clinician review before every dose change", "Baseline labs at a national lab, included", "Optional nausea medication at a local pharmacy, if your clinician prescribes it"],
        "forms": [("Injection", "products/semaglutide.webp", "A small self-injection under the skin. Supplies included. $149 first month, then $229 a month."),
                  ("Oral", "products/semaglutide-oral.webp", "Taken by mouth daily. No needle. $259 a month.")],
        "journey": [
            ("Online intake", "You answer questions about your health, history and goals. A licensed clinician in your state reviews it, usually without a live appointment. A video visit is available on request and required for the first prescription in a few states."),
            ("First prescription and labs", "If appropriate, the clinician prescribes the starting dose and orders baseline labs at a national laboratory at no cost to you. In most cases you can start before the results are back."),
            ("Monthly reviews", "Each month you update a short intake. The clinician reviews it with your labs and decides whether to hold or raise the dose. Nothing changes without that review."),
            ("Steady dose, quarterly reviews", "Once your dose is steady, reviews move to every three months. Refills, changes and cancellation run through your patient portal."),
        ],
        "eligibility": "Adults 18 to 74 with a body mass index of 27 or above, or 25 or above with a related health condition. The clinician makes the final decision on every intake.",
        "faq": [
            ("Is this the same as a brand-name medication?", "No. This is a compounded medication prepared by a licensed 503A pharmacy to your clinician's prescription. Compounded medications are not FDA approved. Your clinician will discuss what that means for you."),
            ("How is the dose decided?", "Your clinician starts at the lowest level and reviews a short update from you each month before any increase. The injection has five levels and the oral form two daily doses. You never move up without a review."),
            ("What does the price include?", "The medication, any supplies your form needs, clinician reviews, baseline labs at a national laboratory, shipping, and patient support around the clock. There is no separate consultation or physician fee."),
            ("What if I am not prescribed?", "Nothing is ordered and your program payment is refunded in full."),
            ("Can I switch plans or cancel?", "Yes. Cancel any time for any reason from your patient portal. Any month whose medication has not been ordered is refunded."),
        ],
    },
    {
        "slug": "microdosing", "name": "Microdosing GLP-1", "cat": "Weight, entry tier", "image": "products/microdosing.webp",
        "title": "Microdosing GLP-1 Program Online",
        "meta": "Low-dose GLP-1 with vitamins or amino acids, oral or injection. A licensed clinician decides. $129 first month, then $179 a month. Prescription required.",
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
        "title": "NAD+ Online Visit: Injection, Nasal, Oral",
        "meta": "NAD+ injection, nasal spray or oral dropper. A licensed clinician decides. $129 first month, then $199 a month. Shipping included. Prescription required.",
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
        "forms": [("Injection", "products/nad.webp", "A small self-injection under the skin. Supplies included."),
                  ("Nasal spray", "products/nad-nasal.webp", "A nasal spray. No needle."),
                  ("Oral dropper", "products/nad-oral.webp", "Drops taken by mouth. No needle.")],
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
        "slug": "glutathione", "name": "Glutathione", "cat": "Vitality", "image": "products/glutathione.webp",
        "title": "Compounded Glutathione, Online Visit",
        "meta": "Glutathione, a peptide of three amino acids. A licensed clinician decides. $129 first month, then $199 a month. Shipping included. Prescription required.",
        "lede": "Glutathione, a peptide made of three amino acids, prescribed only when a licensed clinician decides it is appropriate for you and prepared by a licensed 503A compounding pharmacy in the form the clinician chooses.",
        "chips": ["Prescription only", "Form set by your clinician", "Ships every 4 weeks"],
        "plans": [
            {"id": "monthly", "label": "Month to month", "price": "$199", "unit": "/mo", "note": "$129 your first month, then $199 a month. Cancel any time."},
            {"id": "12week", "label": "12-week plan", "price": "$169", "unit": "/mo", "note": "$507 charged up front, shipped every 4 weeks."},
        ],
        "what_h": "What glutathione is",
        "what": [
            "Glutathione is a peptide made of three amino acids: glutamate, cysteine and glycine. The body makes it and uses it as an antioxidant inside cells. In this program your clinician chooses the form and sets the dose, and a licensed 503A compounding pharmacy prepares it to that prescription.",
            "Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. Whether glutathione is appropriate for you is the clinician's decision.",
        ],
        "facts": ["A peptide of three amino acids", "Form and dose set by your clinician", "Written instructions included", "Clinician review at each refill", "Video visit on request, at no extra cost", "Patient support 24 hours a day"],
        "journey": [
            ("Online intake", "You answer questions about your health, history and goals. A licensed clinician in your state reviews it, usually without a live appointment. A video visit is available on request and required for the first prescription in a few states."),
            ("First prescription", "If appropriate, the clinician prescribes a 4-week supply in the form that fits you."),
            ("Refill review at 3 to 4 weeks", "You update a short intake and the clinician reviews it before writing a 12-week refill."),
            ("12-week reviews", "Reviews continue every 12 weeks. Refills ship every 4 weeks. Changes and cancellation run through your patient portal."),
        ],
        "eligibility": "Adults 18 and over, per our Terms of Service. The clinician makes the final decision on every intake.",
        "faq": [
            ("Which form should I choose?", "You do not need to choose. Your clinician decides the form and dose from your intake, and the licensed 503A pharmacy prepares it to that prescription. Your written instructions cover how to use it."),
            ("Do I need labs?", "Your clinician will tell you if labs are recommended for you."),
            ("What does the price include?", "The medication, clinician reviews, shipping, and patient support around the clock. There is no separate consultation or physician fee."),
            ("What if I am not prescribed?", "Nothing is ordered and your program payment is refunded in full."),
            ("Can I cancel?", "Yes. Cancel any time for any reason from your patient portal. Any month whose medication has not been ordered is refunded."),
        ],
    },
    {
        "slug": "sermorelin", "name": "Sermorelin", "cat": "Hormone support", "image": "products/sermorelin.webp",
        "title": "Compounded Sermorelin, Online Visit",
        "meta": "Compounded sermorelin injection. A licensed clinician decides. $129 first month, then $199 a month. Shipping included. Prescription required.",
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

# Nov 18 2026: sexual health and women's HRT. Their data lives in tools/draft_programs.py and joins the live site only
# when the slug is listed in draft_programs.LIVE. While LIVE is empty this build writes exactly what it did before.
def _load_drafts():
    import importlib.util
    spec = importlib.util.spec_from_file_location("draft_programs", ROOT / "tools" / "draft_programs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_dp = _load_drafts()
LIVE_DRAFTS = [d for d in _dp.DRAFTS if d["slug"] in _dp.LIVE]
PROGRAMS += LIVE_DRAFTS

# The forms that need no injection, Nov 17 2026: (link, name, thumb, line). Used by the Treatments dropdown and the side panel.
NEEDLE_FREE = [("semaglutide.html#forms", "Semaglutide oral", "images/products/thumbs/semaglutide-oral.webp", "Taken by mouth daily"),
               ("nad.html#forms", "NAD+ nasal spray", "images/products/thumbs/nad-nasal.webp", "A nasal spray"),
               ("nad.html#forms", "NAD+ oral dropper", "images/products/thumbs/nad-oral.webp", "Drops taken by mouth"),
               ("microdosing.html", "Microdosing GLP‑1", "images/products/thumbs/microdosing-oral.webp", "Oral options, clinician picks")]

# The Treatments dropdown, one list per column; a column can hold more than one group.
# Needle-free added Nov 17 2026 at Dourado's request: the oral and nasal forms, each linking to its program.
MENU = [
    [("Weight", [("tirzepatide", "Tirzepatide", "images/products/thumbs/tirzepatide.webp", "Dual GIP / GLP-1 injection"),
                 ("semaglutide", "Semaglutide", "images/products/thumbs/semaglutide.webp", "GLP-1, injection or oral"),
                 ("microdosing", "Microdosing GLP‑1", "images/products/thumbs/microdosing.webp", "Low dose, oral or injection")])],
    [("Vitality", [("nad", "NAD+", "images/products/thumbs/nad.webp", "Injection, nasal or oral"),
                   ("glutathione", "Glutathione", "images/products/thumbs/glutathione.webp", "Form set by clinician")]),
     ("Hormone support", [("sermorelin", "Sermorelin", "images/products/thumbs/sermorelin.webp", "GHRH analog injection")])],
    [("Needle-free", NEEDLE_FREE)],
]
if LIVE_DRAFTS:
    MENU[2].append(("Sexual and women's health", [(d["slug"], d["name"], f"images/products/thumbs/{d['slug']}.webp", d["chips"][1]) for d in LIVE_DRAFTS]))


def first_month(p):
    """The first month price, read from the monthly plan note so it is never typed twice."""
    note = next(x for x in p["plans"] if x["id"] == "monthly")["note"]
    m = re.match(r"^(\$\d+) your first month", note)
    assert m, (p["slug"], note)
    return m.group(1)


def price_line(p):
    """One short price line for menus and cards, read from the plan notes so no price is typed twice. Monthly programs
    show the first month. A single plan billed every few weeks shows the month and the charge, per vc-reviewer Nov 18 2026.
    Programs sold by the pack show the lowest pack price."""
    if any(x["id"] == "monthly" for x in p["plans"]):
        return f"{first_month(p)} first month"
    first = p["plans"][0]
    m = re.match(r"^(\$\d+) charged every (\d+ weeks)", first["note"])
    if len(p["plans"]) == 1 and m:
        return f'{first["price"]} a month, billed {m.group(1)} every {m.group(2)}'
    assert all(x["unit"] == "/pack" for x in p["plans"]), p["slug"]
    return f'From ${min(int(x["price"].lstrip("$")) for x in p["plans"])} a pack'


def prod_srcset(rel, prefix, sizes):
    """Nov 17 2026: product photos come in a sharpened 1200 master and an 800 copy, both made from the full-size
    original in assets-in. The browser picks the smaller one on small screens so no card is soft from heavy scaling."""
    stem = rel[:-5] if rel.endswith(".webp") else rel
    if not (ROOT / "public" / "images" / f"{stem}-800.webp").exists():
        return ""
    w = img_size(f"{stem}.webp")[0]
    return f' srcset="{prefix}images/{stem}-800.webp 800w, {prefix}images/{stem}.webp {w}w" sizes="{sizes}"'


# Home tiles show at about 250 px wide; program page tiles at up to 370 px.
TILE_SIZES = "(max-width:700px) 40vw, 260px"
TILE_SIZES_WIDE = "(max-width:700px) 40vw, 380px"


def tile_img(rel, prefix, sizes=TILE_SIZES):
    """Nov 18 2026: form tiles use photos already cropped and sized for the tile, made by tools/prepare_images.py, so the
    browser never zooms or shrinks them hard. Returns the src, srcset, sizes, width and height attributes."""
    stem = rel[:-5].split("/")[-1]
    base = f"{prefix}images/products/tiles/{stem}"
    if not (ROOT / "public" / "images" / "products" / "tiles" / f"{stem}-600.webp").exists():
        w, h = img_size(rel)
        return f'src="{prefix}images/{rel}"{prod_srcset(rel, prefix, sizes)} width="{w}" height="{h}"'
    return (f'src="{base}-600.webp" srcset="{base}-300.webp 300w, {base}-450.webp 450w, {base}-600.webp 600w, {base}-900.webp 900w" '
            f'sizes="{sizes}" width="600" height="800"')


PRODUCT_NOTE = "Product images are illustrations. Your medication is prepared and labeled by a licensed 503A pharmacy and may look different."


def art_photo(rel, alt, prefix="", eager=False, note=""):
    """A wide photo for an article or page, Nov 17 2026. rel is the image path under public/images without .webp.
    Returns nothing until the file exists, so a slot can wait for its Gemini image. A -800 copy, when present, serves phones."""
    if not (ROOT / "public" / "images" / f"{rel}.webp").exists():
        return ""
    w, h = img_size(f"{rel}.webp")
    small = (ROOT / "public" / "images" / f"{rel}-800.webp").exists()
    srcset = f' srcset="{prefix}images/{rel}-800.webp 800w, {prefix}images/{rel}.webp {w}w" sizes="(max-width:800px) 92vw, 760px"' if small else ""
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    cap = f'<figcaption class="img-note">{note}</figcaption>' if note else ""
    return f'<figure class="art-photo"><img src="{prefix}images/{rel}.webp"{srcset} width="{w}" height="{h}" alt="{alt}" {load} decoding="async" />{cap}</figure>'


MENU_BUTTON = '<button class="menu-btn" id="menuBtn" aria-controls="sidePanel" aria-expanded="false"><span class="menu-btn-bars" aria-hidden="true"><span></span><span></span></span>Menu</button>'

GOALS = [("weight", "Weight", "Tirzepatide, Semaglutide, Microdosing GLP-1"),
         ("vitality", "Vitality", "NAD+, Glutathione"),
         ("hormone", "Hormone support", "Sermorelin")]


GOAL_THUMB = {"weight": "tirzepatide", "vitality": "nad", "hormone": "sermorelin"}  # Nov 17 2026: one vial fills the small tile


def panel_thumb(p, prefix):
    """The program's small photo, or the logo mark until that photo exists."""
    if (ROOT / "public" / "images" / "products" / "thumbs" / f"{p['slug']}.webp").exists():
        return f'<img src="{prefix}images/products/thumbs/{p["slug"]}.webp" width="216" height="216" alt="" loading="lazy" />'
    return f'<img class="panel-logo" src="{prefix}logo-mark.svg" width="119" height="128" alt="" loading="lazy" />'


def side_panel(prefix):
    """The slide-in menu, Nov 17 2026: the goal question, the six programs with their first month price,
    the site links, one button. The same on every page; prefix is '' at the root and '../' one level down."""
    goals = "".join(
        f'<li><a href="{prefix}index.html#goals-{g}" data-pick-goal="{g}"><img src="{prefix}images/products/thumbs/{GOAL_THUMB[g]}.webp" width="216" height="216" alt="" loading="lazy" />'
        f'<span><b>{name}</b><small>{sub}</small></span><i aria-hidden="true"></i></a></li>' for g, name, sub in GOALS)
    progs = "".join(
        f'<a class="panel-prog" href="{prefix}programs/{p["slug"]}.html">{panel_thumb(p, prefix)}'
        f'<b>{p["name"]}</b><small>{price_line(p)}</small></a>' for p in PROGRAMS)
    links = [("how-it-works.html", "How it works"), ("pricing.html", "Pricing"), ("learn.html", "Learn"), ("clinicians.html", "Clinicians"),
             ("faq.html", "FAQ"), ("about.html", "About"), ("contact.html", "Contact")]
    more = "".join(f'<a href="{prefix}{h}">{t}</a>' for h, t in links)
    nofree = "".join(
        f'<a class="panel-prog" href="{prefix}programs/{href}"><img src="{prefix}{img}" width="216" height="216" alt="" loading="lazy" />'
        f'<b>{name}</b><small>{line}</small></a>' for href, name, img, line in NEEDLE_FREE)
    return (f'<!-- panel:start -->\n  <div class="panel-overlay" id="panelOverlay" hidden></div>\n'
            f'  <aside class="panel" id="sidePanel" role="dialog" aria-modal="true" aria-label="Menu" aria-hidden="true" hidden>\n'
            f'    <div class="panel-head"><span class="panel-title">Menu</span><button type="button" class="panel-close" id="panelClose" aria-label="Close menu">&#215;</button></div>\n'
            f'    <p class="panel-kicker">What are you here for?</p><ol class="hero-menu panel-goals" aria-label="Choose a goal">{goals}</ol>\n'
            f'    <p class="panel-kicker">Programs</p><div class="panel-progs">{progs}</div>\n'
            f'    <p class="panel-kicker">Needle-free</p><div class="panel-progs">{nofree}</div>\n'
            f'    <p class="panel-kicker">More</p><nav class="panel-links" aria-label="Pages">{more}</nav>\n'
            f'    <div class="panel-foot"><a href="{prefix}index.html#goals" class="btn btn-primary btn-block" data-find>Find your program</a>'
            f'<p>Prescription required. A licensed clinician reviews your intake and decides what is appropriate for you.</p></div>\n'
            f'  </aside>\n  <!-- panel:end -->')


def goal_band(prefix):
    """The chooser's first question at the foot of a page, Nov 17 2026: three goal rows that open step 2 of the home
    chooser, and one button for the rest. Not on the home page, which has the chooser itself, and not on legal pages."""
    goals = "".join(
        f'<li><a href="{prefix}index.html#goals-{g}" data-pick-goal="{g}"><img src="{prefix}images/products/thumbs/{GOAL_THUMB[g]}.webp" width="216" height="216" alt="" loading="lazy" />'
        f'<span><b>{name}</b><small>{sub}</small></span><i aria-hidden="true"></i></a></li>' for g, name, sub in GOALS)
    return (f'<!-- goalband:start -->\n    <section class="section goal-band on-cream" aria-labelledby="goalBandTitle">\n      <div class="container">\n'
            f'        <h2 id="goalBandTitle">What are you here for?</h2>\n'
            f'        <p class="goal-band-sub">Pick a goal and two quick questions narrow six programs down to the ones that may fit. A licensed clinician decides what is appropriate.</p>\n'
            f'        <ol class="hero-menu goal-band-menu" aria-label="Choose a goal">{goals}</ol>\n'
            f'        <a href="{prefix}index.html#goals" class="btn btn-ghost" data-find>Not sure? Find your program</a>\n'
            f'      </div>\n    </section>\n    <!-- goalband:end -->')


def mega_menu(prefix):
    """The Treatments dropdown. prefix is '' on the home page and '../' on program pages."""
    cols = []
    for column in MENU:
        groups = []
        for cat, items in column:
            rows = []
            for slug, name, img, sub in items:
                href = slug if slug.endswith(".html") or ".html#" in slug else f"{slug}.html"
                thumb = f'<img src="{prefix}{img}" alt="" width="54" height="54" loading="lazy" />' if img and (ROOT / "public" / img).exists() else f'<img class="mega-tile" src="{prefix}logo-mark.svg" alt="" width="119" height="128" loading="lazy" />'
                rows.append(f'<a class="mega-item" href="{prefix}programs/{href}">{thumb}<span><b>{name}</b><small>{sub}</small></span></a>')
            groups.append(f'<h4>{cat}</h4>{"".join(rows)}')
        cols.append(f'<div class="mega-col">{"".join(groups)}</div>')
    # Nov 19 2026: a plain disclosure, not role="menu"; script.js keeps aria-expanded true to what is shown and closes it on Escape.
    return (f'<div class="nav-item has-mega"><a href="{prefix}index.html#treatments" aria-expanded="false">Treatments</a>'
            f'<div class="mega">{"".join(cols)}'
            f'<div class="mega-col mega-cta"><h4>Not sure?</h4><p>Two quick questions narrow it down. A licensed clinician reviews your intake and decides what is appropriate.</p>'
            f'<a class="btn btn-primary btn-sm" href="{prefix}index.html#goals">Find your program</a></div></div></div>')


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


def intake_key(p):
    return "nad+" if p["slug"] == "nad" else p["slug"]


def pb_thumb(p):
    """Nov 19 2026: the small product photo beside the price, shown on phones only so the first screen carries
    the product, the price and the Start button. The large photo further down keeps the alt text and the image note."""
    if (ROOT / "public" / "images" / "products" / "thumbs" / f"{p['slug']}.webp").exists():
        return f'<img class="pb-thumb" src="../images/products/thumbs/{p["slug"]}.webp" width="216" height="216" alt="" />'
    return ""


def plan_thumb(p, pl):
    """A plan with its own form photo, such as Semaglutide oral, swaps the phone thumbnail when it is chosen."""
    thumbs = ROOT / "public" / "images" / "products" / "thumbs"
    if not (thumbs / f"{p['slug']}.webp").exists():
        return ""
    own = f"{p['slug']}-{pl['id']}.webp"
    return f' data-thumb="../images/products/thumbs/{own if (thumbs / own).exists() else p["slug"] + ".webp"}"'


def pb_points(p):
    """Nov 19 2026: three short answers under the Start button, the most common worry first, each line taken from
    copy already on the site. Draft programs keep only the clinician line until OpenLoop confirms refund and shipping."""
    pts = ["One price with shipping. No consultation fee.",
           "A licensed clinician decides what is appropriate.",
           "Full refund if not prescribed."]
    if p.get("swaps"):
        pts = pts[1:2]
    return '<ul class="pb-points">' + "".join(f'<li><span class="check" aria-hidden="true">✓</span> {x}</li>' for x in pts) + "</ul>"


def start_button(p, cls="btn btn-primary", prefix="../"):
    """Every Start your visit button leads to the program's Start page, never straight to the intake."""
    return f'<a class="{cls}" href="{prefix}start/{p["slug"]}.html" data-start="{p["slug"]}">Start your visit</a>'


def mcta_price(p):
    """Phone bar price: two short lines so the full price always shows."""
    first = p["plans"][0]
    m = re.match(r"(\$\d+) your first month, then (\$\d+) a month", first["note"])
    if m:
        return f'<span class="mcta-price"><b>{m.group(1)} first month</b><small>then {m.group(2)}/mo</small></span>'
    line = price_line(p)
    if ", billed " in line:
        a, b = line.split(", ", 1)
        return f'<span class="mcta-price"><b>{a}</b><small>{b}</small></span>'
    if line.startswith("From "):
        return f'<span class="mcta-price"><b>{line}</b><small>{p["name"]}</small></span>'
    return f'<span class="mcta-price"><b>{first["price"]}{first["unit"]}</b><small>{p["name"]}</small></span>'


def render(p):
    """The finished program page: the template, then the program's line swaps, then its safety block when it has one."""
    s = page(p)
    for a, b in p.get("swaps", []):
        s = s.replace(a, b)
    if p.get("safety"):
        block = f'''    <section class="section blk" id="safety">
      <div class="container">
        <div class="blk-card blk-card-mint">
          <h2>Important safety information</h2>
          <p>{p["safety"]}</p>
        </div>
      </div>
    </section>

'''
        assert s.count('    <section class="please-note">') == 1
        s = s.replace('    <section class="please-note">', block + '    <section class="please-note">', 1)
    return s


def render_start(p):
    """The finished Start page, with the program's line swaps."""
    s = start_page(p)
    for a, b in p.get("swaps", []):
        s = s.replace(a, b)
    return s


def page(p):
    media = f'<img class="tcard-photo" src="../images/{p["image"]}"{prod_srcset(p["image"], "../", "(max-width:900px) 92vw, 560px")} width="{img_size(p["image"])[0]}" height="{img_size(p["image"])[1]}" alt="Velacore Health {p["name"]}" fetchpriority="high" />' if p["image"] and (ROOT / "public" / "images" / p["image"]).exists() else '<img class="brand-tile" src="../logo-mark.svg" alt="" width="119" height="128" />'
    plans = "\n".join(
        f'''          <label class="plan-option">
            <input type="radio" name="plan" value="{pl["id"]}" data-price="{pl["price"]}" data-unit="{pl["unit"]}" data-note="{pl["note"]}"{plan_thumb(p, pl)}{" checked" if i == 0 else ""} />
            <span class="plan-name">{pl["label"]}</span><span class="plan-amt">{pl["price"]}{pl["unit"]}</span>
          </label>''' for i, pl in enumerate(p["plans"]))
    first = p["plans"][0]
    chips = "".join(f'<li class="chip"><span class="dot"></span> {c}</li>' for c in p["chips"])
    facts = "".join(f'<li><span class="check">✓</span> {f}</li>' for f in p["facts"])
    journey = "".join(
        f'''            <li><span class="hiw-num">{i}</span><div><b>{h}</b><p>{t}</p></div></li>''' for i, (h, t) in enumerate(p["journey"], 1))
    faq = "".join(
        f'''          <details class="faq-item">
            <summary>{q}</summary>
            <div class="faq-body"><p>{a}</p></div>
          </details>''' for q, a in p["faq"])
    what = "".join(f"<p>{x}</p>" for x in p["what"])
    forms = ""
    if p.get("forms"):
        tiles = "".join(
            f'<li><img {tile_img(img, "../", TILE_SIZES_WIDE)} alt="Velacore Health {p["name"]} {name.lower()}" loading="lazy" /><div><b>{name}</b><p>{line}</p></div></li>'
            for name, img, line in p["forms"] if (ROOT / "public" / "images" / img).exists())
        forms = f'''
    <!-- Forms, Nov 17 2026: one card, one photo per form. Shown only where the program data lists forms. -->
    <section class="section blk prog-forms" id="forms">
      <div class="container">
        <div class="blk-card blk-card-mint">
          <div class="section-head">
            <h2>{ {2: "Two", 3: "Three", 4: "Four"}.get(len(p["forms"]), str(len(p["forms"]))) } forms, one program</h2>
            <p class="section-sub">Your clinician decides the form and the dose from your intake. Product images are illustrations; your medication is prepared and labeled by a licensed 503A pharmacy and may look different.</p>
          </div>
          <ul class="form-tiles form-tiles-{len(p["forms"])}">{tiles}</ul>
        </div>
      </div>
    </section>
'''
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
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
  <link rel="icon" href="../logo-mark.png" />
</head>
<body class="prog-{p["slug"]}">
  <div class="topbar"><span>A telehealth platform. Independent licensed clinicians decide. Prescription required.</span></div>
  <header class="site-header" id="top">
    <div class="container nav">
      <a href="../index.html" class="brand" aria-label="Velacore Health home">
        <img class="brand-mark" src="../logo-mark.svg" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span>
      </a>
      <nav class="nav-links" id="navLinks" aria-label="Primary">
        {mega_menu("../")}
        <a href="../how-it-works.html">How it works</a>
        <a href="../learn.html">Learn</a>
        <a href="../clinicians.html">Clinicians</a>
        <a href="../faq.html">FAQ</a>
        <a href="../start/{p["slug"]}.html" class="btn btn-primary btn-sm" data-start="{p["slug"]}">Start your visit</a>
      </nav>
      {MENU_BUTTON}
    </div>
  </header>
  {side_panel("../")}

  <main>
    <section class="prog-hero">
      <div class="container">
        <p class="crumbs"><a href="../index.html">Home</a> / <a href="../index.html#treatments">Treatments</a> / {p["name"]}</p>
        <div class="prog-grid">
          <div class="prog-copy">
            <h1>{p["name"]}</h1>
            <p class="prog-cat"><span class="tcard-cat">{p["cat"]}</span></p>
            <p class="hero-lede">{p["lede"]}</p>
            <ul class="hero-chips">{chips}</ul>
            <ul class="facts">{facts}</ul>
          </div>
          <div class="prog-side">
            <div class="tcard prog-media"><div class="tcard-media">{media}</div></div>
            <p class="img-note">Illustrative image. Your medication is prepared and labeled by a licensed 503A pharmacy and may look different.</p>
            <div class="price-box" id="priceBox">
              <div class="pb-head">{pb_thumb(p)}<div class="pb-price">
              <div class="price-top">
                <span class="price-big" id="planPrice">{first["price"]}<small id="planUnit">{first["unit"]}</small></span>
                <span class="tcard-rx">Rx only</span>
              </div>
              <p class="price-note" id="planNote">{first["note"]}</p>
              </div></div>
              <div class="plan-select" role="radiogroup" aria-label="Choose a plan">
{plans}
              </div>
              {start_button(p, "btn btn-primary btn-block")}
              <p class="price-fine">{DISCLAIMER}</p>
              {pb_points(p)}
            </div>
          </div>
        </div>
      </div>
    </section>

{TRUST}
{forms}
    <!-- Program cards, Nov 17 2026: what it is, who it is for, the four steps, each one card -->
    <section class="section blk prog-blocks">
      <div class="container prog-two">
        <div class="blk-card blk-card-mint">
          <h2>{p["what_h"]}</h2>
          <div class="prog-text">{what}</div>
        </div>
        <div class="blk-card blk-card-jade prog-who">
          <h2>Who this program is for</h2>
          <p>{p["eligibility"]}</p>
          <p>Every program is prescription only. Velacore coordinates access and education; the licensed clinician decides; the 503A pharmacy fills.</p>
          {start_button(p, "btn btn-primary")}
        </div>
      </div>
    </section>

    <section class="section blk">
      <div class="container">
        <div class="blk-card blk-card-mint">
          <div class="section-head">
            <h2>A review before every change, not just a refill</h2>
            <p class="section-sub">Velacore coordinates each step. A licensed clinician makes every prescribing decision.</p>
          </div>
          <ol class="hiw-rows">
{journey}
          </ol>
          <div class="blk-actions">{start_button(p, "btn btn-primary")}<a href="../how-it-works.html" class="btn btn-ghost">See every step</a></div>
        </div>
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
        <a href="../index.html" class="brand"><img class="brand-mark" src="../logo-mark.svg" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span></a>
        <p>A telehealth platform coordinating access to licensed clinicians and 503A compounding pharmacies.</p>
      </div>
      <nav class="footer-col" aria-label="Programs"><h4>Programs</h4>
        {"".join(f'<a href="{q["slug"]}.html">{q["name"]}</a>' for q in PROGRAMS)}</nav>
      <nav class="footer-col" aria-label="More"><h4>More</h4>
        <a href="../how-it-works.html">How it works</a><a href="../learn.html">Learn</a><a href="../faq.html">FAQ</a><a href="../pricing.html">Pricing</a><a href="../about.html">About</a><a href="../contact.html">Contact</a></nav>
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

  <div class="mobile-cta mobile-cta--price" id="mobileCta" aria-hidden="false">{mcta_price(p)}<a href="../start/{p["slug"]}.html" class="btn btn-primary" data-start="{p["slug"]}">Start your visit</a></div>
  <script src="../script.js"></script>
</body>
</html>
"""


# Start page copy. Drafted by vc-copy in docs/funnel-copy.md; tokens are filled per program.
START = {
    "title": "Start your {Program} visit",
    "meta": "A short online intake on our partner's secure site, then a licensed clinician decides. Full refund if not prescribed. Prescription required.",
    "h1": "Before you start your {Program} visit",
    "price": "{note} Shipping included.",
    # The intake length is not confirmed by OpenLoop in writing, so this says "a few minutes".
    "steps": [
        "You fill in a secure online intake. It takes a few minutes.",
        "A licensed clinician in your state reviews it and decides whether {Program} is appropriate for you. In a few states the first review is a live video visit.",
        "If you are prescribed, a licensed 503A pharmacy fills your order and ships it to you. If not, your payment is refunded in full.",
    ],
    "handoff": "The next page is our telehealth partner's secure site, so you will see their name there instead of ours.",
    "button": "Continue to secure intake",
    "back": "Back to {Program}",
    "pending": "The online visit for {Program} opens soon. In the meantime, email hello@velacorehealth.com with any questions.",
}


def start_page(p):
    fill = lambda s: s.replace("{Program}", p["name"]).replace("{note}", p["plans"][0]["note"])
    link = INTAKE.get(intake_key(p), "")
    steps = "".join(f'<li><span class="sp-num" aria-hidden="true">{i}</span><p>{fill(s)}</p></li>' for i, s in enumerate(START["steps"], 1))
    if link:
        button = f'<a class="btn btn-primary btn-block" href="{link}" data-intake="{intake_key(p)}" rel="noopener">{fill(START["button"])}</a>'
        pending = ""
    else:
        button = f'<a class="btn btn-primary btn-block" href="#" data-intake="{intake_key(p)}" aria-disabled="true">{fill(START["button"])}</a>'
        pending = f'<p class="sp-pending">{fill(START["pending"]).replace("hello@velacorehealth.com", "<a href=\"mailto:hello@velacorehealth.com\">hello@velacorehealth.com</a>")}</p>'
    media = f'<img src="../images/{p["image"]}"{prod_srcset(p["image"], "../", "(max-width:700px) 80vw, 400px")} width="{img_size(p["image"])[0]}" height="{img_size(p["image"])[1]}" alt="" />' if p["image"] and (ROOT / "public" / "images" / p["image"]).exists() else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <!-- No analytics on Start pages until Dourado makes the health-privacy call, per vc-reviewer Nov 13 2026. -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{fill(START["title"])} | Velacore Health</title>
  <meta name="description" content="{fill(START["meta"])}" />
  <meta name="robots" content="noindex" />
  <meta name="theme-color" content="#15302A" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Hanken+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../styles.css" />
  <link rel="icon" href="../logo-mark.png" />
</head>
<body class="start-page prog-{p["slug"]}">
  <header class="site-header sp-header">
    <div class="container nav">
      <a href="../index.html" class="brand" aria-label="Velacore Health home">
        <img class="brand-mark" src="../logo-mark.svg" alt="Velacore Health" /><span class="brand-name">Velacore <span class="brand-accent">Health</span></span>
      </a>
      <a class="sp-back" href="../programs/{p["slug"]}.html">Back<span class="sp-back-name"> to {p["name"]}</span></a>
    </div>
  </header>
  <main class="section sp-main">
    <div class="container sp-grid">
      <div class="sp-card">
        <h1>{fill(START["h1"])}</h1>
        <p class="sp-price">{fill(START["price"])}</p>
        <ol class="sp-steps">{steps}</ol>
        <p class="sp-handoff">{fill(START["handoff"])}</p>
        {button}
        {pending}
        <p class="price-fine">{DISCLAIMER}</p>
      </div>
      <div class="sp-side"><div class="sp-media" aria-hidden="true">{media}</div><p class="img-note">Illustrative image. Your medication is prepared and labeled by a licensed 503A pharmacy and may look different.</p></div>
    </div>
  </main>
  <footer class="site-footer sp-footer">
    <div class="container footer-legal">
      <p class="disclaimer"><b>Important:</b> Velacore Health does not provide, guarantee, or facilitate any medical services, prescriptions, or treatments. The platform coordinates access to licensed clinicians and 503A compounding pharmacies; all medical decisions are made solely by the independent clinician. All medications are prescription only. Compounded medications are not FDA approved.</p>
      <div class="footer-bottom"><p>© <span id="year"></span> Velacore Health, First Venture Group LLC.</p>
      <nav aria-label="Legal"><a href="../privacy.html">Privacy</a><a href="../terms.html">Terms</a><a href="../telehealth-consent.html">Telehealth consent</a><a href="../refund-policy.html">Refund policy</a></nav></div>
    </div>
  </footer>
  <script src="../script.js"></script>
</body>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in PROGRAMS:
        (OUT / f"{p['slug']}.html").write_text(render(p), encoding="utf-8")
        print("wrote", f"public/programs/{p['slug']}.html")
    START_OUT.mkdir(parents=True, exist_ok=True)
    for p in PROGRAMS:
        (START_OUT / f"{p['slug']}.html").write_text(render_start(p), encoding="utf-8")
        print("wrote", f"public/start/{p['slug']}.html")


if __name__ == "__main__":
    main()
