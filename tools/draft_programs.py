"""Sexual health and women's HRT, approved by Dourado on Nov 18 2026, limited to the items OpenLoop names in writing.

The switch: a program joins the live site only when its slug is listed in LIVE. While LIVE is empty the build output
of the live site is unchanged and the pages exist only as drafts in drafts/programs, made by tools/build_drafts.py.
Before a slug goes in LIVE, every open item below must be closed in writing and vc-reviewer must pass the page.
The launch steps are in docs/launch-sexual-health-hrt.md.
"""

LIVE = []

# Template lines that state facts not yet confirmed for these categories, swapped on the program page and the Start page.
# vc-reviewer Nov 18 2026: the 503A fill, shipping and the refund if not prescribed are unconfirmed for these categories.
# Remove a swap once OpenLoop confirms the template's own line in writing.
SWAPS = [
    ("Filled by a licensed 503A pharmacy, shipping included", "Filled by a licensed pharmacy"),
    ("prepared and labeled by a licensed 503A pharmacy", "prepared and labeled by a licensed pharmacy"),
    ("the licensed clinician decides; the 503A pharmacy fills.", "the licensed clinician decides; a licensed pharmacy fills."),
    ("<span>503A compounding pharmacies</span>", "<span>Licensed pharmacies</span>"),
    ("<span>Shipping included, no hidden fees</span>", "<span>Prescription only</span>"),
    ("<li><span class=\"dot\"></span> Refunded in full if not prescribed</li>", "<li><span class=\"dot\"></span> Refund terms to be confirmed by OpenLoop</li>"),
    # Start page
    ("Full refund if not prescribed. ", ""),
    (" Shipping included.</p>", "</p>"),
    ("a licensed 503A pharmacy fills your order and ships it to you. If not, your payment is refunded in full.", "a licensed pharmacy fills your order and ships it to you."),
]

DRAFTS = [
    {
        "slug": "sexual-health", "name": "Sexual Health", "cat": "Sexual health", "image": "products/sexual-health.webp",
        "title": "Sexual Health Online Visit",
        "meta": "An online visit for sexual health: vials, dissolving tablets or daily tadalafil. A licensed clinician decides. 21 and over. Prescription required.",
        "lede": "Prescription sexual health medications, as single-dose vials, dissolving tablets or a daily tadalafil pack, prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Vials, dissolving tablets or daily pack", "21 and over"],
        "plans": [
            {"id": "vials", "label": "Single-dose vials, 10 pack", "price": "$99", "unit": "/pack", "note": "From $99. A 10 pack is $99, $109 or $119, depending on the formulation your clinician prescribes."},
            {"id": "tablets", "label": "Dissolving tablets, pouch of 6 or 12", "price": "$96", "unit": "/pack", "note": "From $96. A pouch of 6 is $96 or $102. A pouch of 12 is $144 or $156. The price depends on the formulation your clinician prescribes."},
            {"id": "daily", "label": "Tadalafil daily, 28 pack", "price": "$112", "unit": "/pack", "note": "$112 for a 28 pack, 2.5 mg or 5 mg, set by your clinician."},
        ],
        "what_h": "What the sexual health program is",
        "what": [
            "The program covers prescription medications made from sildenafil, tadalafil, apomorphine, silodosin and L-citrulline, alone or combined, in three forms: single-dose vials, dissolving tablets, and a daily tadalafil pack. Your clinician chooses the medication, the form and the dose from your intake.",
            "Velacore coordinates the visit, an independent licensed clinician decides whether to prescribe, and a licensed pharmacy fills the prescription. Whether any of these medications is appropriate for you is the clinician's decision.",
        ],
        "facts": ["Single-dose vials, 10 pack", "Dissolving tablets, pouch of 6 or 12", "Tadalafil daily, 2.5 mg or 5 mg, 28 pack", "Medication, form and dose set by your clinician", "Clinician review every 12 weeks at refill", "Video visit on request"],
        "journey": [
            ("Online intake", "You answer questions about your health and history. A licensed clinician reviews it, usually without a live appointment. A video visit is required in some states and available on request."),
            ("Prescription", "If appropriate, the clinician chooses the medication, form and dose and sends the prescription to a licensed pharmacy."),
            ("12-week refill reviews", "Every 12 weeks you update a short refill intake and the clinician reviews it before the next refill. A video visit is available on request."),
        ],
        "eligibility": "Adults 21 and over. Patients 75 and over are eligible only for single-ingredient medications. The clinician makes the final decision on every intake.",
        "faq": [
            ("Which medications are offered?", "Single-dose vials, 10 pack: sildenafil and tadalafil, $99; silodosin and tadalafil, $99; sildenafil, tadalafil and apomorphine, $109; sildenafil, tadalafil, apomorphine and L-citrulline, $119. Dissolving tablets: sildenafil and tadalafil, $96 for 6 or $144 for 12; silodosin and tadalafil, $96 for 6 or $144 for 12; sildenafil, tadalafil and apomorphine, $102 for 6 or $156 for 12. Tadalafil daily, 2.5 mg or 5 mg, 28 pack, $112."),
            ("Who is eligible?", "Adults 21 and over. Patients 75 and over are eligible only for single-ingredient medications, which on this page means tadalafil daily. The clinician makes the final decision on every intake."),
            ("Who chooses the medication and dose?", "Your clinician decides the medication, the form and the dose from your intake."),
            ("Do I need labs?", "Your clinician will tell you if labs are recommended for you."),
            ("What if I am not prescribed?", "Draft placeholder, to be confirmed in writing by OpenLoop: nothing is ordered and the payment is refunded in full."),
            ("Can I cancel?", "Draft placeholder, to be confirmed in writing by OpenLoop: cancel any time for any reason from your patient portal, and anything whose medication has not been ordered is refunded."),
        ],
        "safety": "Important safety information for every medication on this page will come from OpenLoop's clinical team, approved in writing, before the page goes live.",
        "open_items": [
            "Which items are compounded and which are FDA-approved products, including tadalafil daily. The template prints the compounded disclaimer on every program page, so each item must be labeled correctly before launch.",
            "The pharmacy that fills each item, its state licenses, and its LegitScript or NABP status.",
            "Important safety information for each medication, written or approved in writing by OpenLoop's clinical team.",
            "When the patient is charged, before or after clinician review.",
            "Whether the cancel any time and refund if not prescribed terms apply to this category; the FAQ uses them.",
            "How often each pack refills and ships.",
            "Whether a video visit on request costs anything.",
            "Whether to show the strength of each formulation; the notes file has them, the page leaves them off.",
            "Price range: the Nov 2 summary says $99 to $156 per pack, the Nov 12 pages list dissolving tablets from $96.",
            "Whether the category is in the signed Agile order.",
            "What the single-dose vials are, taken by mouth or by injection. The page must state the form before launch.",
            "Product image products/sexual-health.webp is not made yet.",
        ],
    },
    {
        "slug": "womens-hrt", "name": "Women's HRT", "cat": "Women's health", "image": "products/womens-hrt.webp",
        "title": "Menopause and Women's HRT Online Visit",
        "meta": "Women's HRT by online visit, estradiol or non-hormonal. A licensed clinician decides. $79 a month, billed $237 every 12 weeks. Prescription required.",
        "lede": "Estradiol in several forms, or a non-hormonal option, prescribed only when a licensed clinician decides it is appropriate for you.",
        "chips": ["Prescription only", "Hormonal or non-hormonal", "Billed every 12 weeks"],
        "plans": [
            {"id": "12week", "label": "Billed every 12 weeks", "price": "$79", "unit": "/mo", "note": "$237 charged every 12 weeks."},
        ],
        "what_h": "What the women's HRT program is",
        "what": [
            "A program for menopause and perimenopause. The options are an estradiol pill, patch or gel; estradiol vaginal cream, plus progesterone if needed; or a non-hormonal option, a paroxetine pill or a desvenlafaxine pill. Your clinician chooses the medication and the dose from your intake.",
            "Velacore coordinates the visit, an independent licensed clinician decides whether to prescribe, and a licensed pharmacy fills the prescription. Whether any of these medications is appropriate for you is the clinician's decision.",
        ],
        "facts": ["Estradiol pill, patch or gel", "Estradiol vaginal cream, plus progesterone if needed", "Non-hormonal: paroxetine pill or desvenlafaxine pill", "Medication and dose set by your clinician", "Clinician review every quarter at refill", "Labs ordered when merited, paid by the patient"],
        "journey": [
            ("Online intake", "You complete a full health intake. A licensed clinician engaged through our telehealth services partner reviews it, usually without a live appointment. A video visit is required in some states."),
            ("Prescription and labs", "If appropriate, the clinician prescribes and orders labs when they are merited. Labs are not in the program price and are paid by the patient."),
            ("Quarterly refill reviews", "Every quarter you update a short refill intake and the clinician reviews it before the next refill. A video visit is available on request."),
        ],
        "eligibility": "The clinician decides who is eligible from your intake and makes the final decision on every intake.",
        "faq": [
            ("Which medications are offered?", "Estradiol as a pill, patch or gel; estradiol vaginal cream, plus progesterone if needed; or a non-hormonal paroxetine pill or desvenlafaxine pill. Your clinician decides which, if any, is appropriate."),
            ("How am I billed?", "$79 a month, charged as $237 every 12 weeks. Labs are not included."),
            ("Do I need labs?", "Your clinician orders labs when they are merited. Labs are not in the program price and are paid by the patient."),
            ("What if I am not prescribed?", "Draft placeholder, to be confirmed in writing by OpenLoop: nothing is ordered and the payment is refunded in full."),
            ("Can I cancel?", "Draft placeholder, to be confirmed in writing by OpenLoop: cancel any time for any reason from your patient portal, and anything whose medication has not been ordered is refunded."),
        ],
        "safety": "Important safety information for every medication on this page will come from OpenLoop's clinical team, approved in writing, before the page goes live.",
        "open_items": [
            "The eligibility age. The page says only that the clinician decides.",
            "Which items are compounded and which are FDA-approved products, including each estradiol form. The template prints the compounded disclaimer on every program page, so each item must be labeled correctly before launch.",
            "The pharmacy that fills each item, its state licenses, and its LegitScript or NABP status.",
            "Important safety information for estradiol, progesterone and each non-hormonal pill, written or approved in writing by OpenLoop's clinical team.",
            "What labs cost the patient, and whether labs are needed before the first prescription.",
            "Whether progesterone if needed applies to every estradiol form or only the vaginal cream; the page follows the notes wording.",
            "What the $79 covers besides the medication, such as clinician reviews and shipping.",
            "When the patient is charged, and whether the cancel and refund terms apply, including part of a 12-week period; the FAQ uses them.",
            "Whether the category is in the signed Agile order.",
            "How the two non-hormonal pills, paroxetine and desvenlafaxine, may be named in a menopause program. The attorney and OpenLoop's clinical team must clear the wording, and the safety block must cover both.",
            "Menopause in the page title was cleared by vc-reviewer on Nov 18 2026, on condition the page never names a symptom or a result.",
            "Product image products/womens-hrt.webp is not made yet.",
        ],
    },
]

for _d in DRAFTS:
    _d["swaps"] = SWAPS
