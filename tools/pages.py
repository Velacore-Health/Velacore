# Velacore stand-alone pages: how it works, clinicians, pricing, about, contact.
# Written by vc-copy on 2026-11-13. Same shape as ARTICLES in tools/articles.py.
# Edit the text here, never in the built pages.
# Every service fact traces to docs/openloop-proposal-notes.md or a page already live.
# No price is typed in this file. The pricing page carries the token {{price_table}}
# and the builder fills it from the program data in tools/build_programs.py.
# Nothing here is published until vc-reviewer clears it and Dourado says so.

PAGES = [
    {
        "slug": "how-it-works",
        "title": "How Velacore works: intake, clinician review, pharmacy",
        "meta": "Online intake, a licensed clinician reviews it, then a 503A pharmacy fills. What happens at each step. Prescription required.",
        "h1": "How Velacore works",
        "lede": "Velacore coordinates. An independent licensed clinician decides. A licensed 503A compounding pharmacy fills. This page sets out each step in order. Prescription required.",
        # The visual layout, added Nov 16 2026 on Dourado's note that the page read like a worksheet.
        # Short lines only. Every fact here is already in the sections below, which fold under each step by heading.
        "flow": {
            "sub": "Four steps, started online. A licensed clinician makes every prescribing decision. Prescription required.",
            "steps": [
                {"short": "Answer questions online", "title": "Answer a few questions online",
                 "img": "step-visit", "w": 1600, "h": 1194, "alt": "A man typing on his laptop at his kitchen table",
                 "line": "Pick a program and complete a secure intake about your goals, health history and medications.",
                 "facts": ['Not sure which program? <a href="index.html#goals" data-find>Find your program</a> walks you through it', "The intake runs on our telehealth partner's secure pages"],
                 "more": "Online intake"},
                {"short": "A clinician reviews it", "title": "A licensed clinician reviews it",
                 "img": "step-clinician", "w": 1600, "h": 1194, "alt": "Hands of a clinician in a white coat writing notes on a patient chart at a clinic desk",
                 "line": "A physician or nurse practitioner licensed in your state reviews your intake and decides whether to prescribe.",
                 "facts": ["Most reviews happen without a live appointment", "A video visit is yours on request, at no extra cost", "Velacore has no say in the decision"],
                 "more": "Clinician review"},
                {"short": "A pharmacy ships it", "title": "A pharmacy prepares and ships it",
                 "img": "step-delivery", "w": 1600, "h": 1194, "alt": "A dog sniffing a plain shipping box on the front step",
                 "line": "If you are prescribed, a licensed 503A compounding pharmacy prepares your medication and ships it to you.",
                 "facts": ["Ongoing plans ship every four weeks", "Baseline labs at a national laboratory, at no cost to you, on the Semaglutide and Tirzepatide programs"],
                 "note": "Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
                 "more": "Pharmacy fulfillment"},
                {"short": "Reviews and support continue", "title": "Reviews and support continue",
                 "img": "hero", "w": 1194, "h": 1600, "pos": "50% 30%", "alt": "A woman pouring a glass of water in her kitchen",
                 "line": "The clinician reviews your intake updates on a set schedule, and patient support is available 24 hours a day, every day.",
                 "facts": ["Nothing about your prescription changes without a clinician's review", "Message your clinician through your patient portal"],
                 "more": "Ongoing reviews and support"},
            ],
            "promise": {"title": "Not prescribed? Your program payment is refunded in full.",
                        "line": "A prescription is not guaranteed. After you start, you can cancel at any time, and you can request a refund for any month whose medication has not yet been ordered. Medications are non-returnable once dispensed."},
            "scope": "What Velacore does and does not do",
        },
        "sections": [
            ("The steps at a glance", [
                "1. <strong>Online intake.</strong> You pick a program and answer questions about your health, history and medications.\n"
                "2. <strong>Clinician review.</strong> A physician or nurse practitioner licensed in your state reviews your intake and decides whether to prescribe.\n"
                "3. <strong>Pharmacy fulfillment.</strong> If you are prescribed, a licensed 503A compounding pharmacy prepares your medication and ships it to you.\n"
                "4. <strong>Ongoing reviews and support.</strong> The clinician reviews your intake updates on a set schedule, and patient support is available 24 hours a day, every day.",
                "Every program is prescription only. Starting a visit is not a guarantee of treatment.",
            ]),
            ("Online intake", [
                'You start by choosing a program. If you are not sure which one, <a href="index.html#goals">Find your program</a> walks you through the options. The clinician still makes the final decision on which program, if any, is appropriate.',
                "The intake is a set of questions about your goals, your health history and the medications you take. It runs on our telehealth services partner's secure pages, not on this website, so you will see their name there instead of ours.",
                "The Semaglutide and Tirzepatide programs are for adults 18 to 74 with a body mass index of 27 or above, or 25 or above with a related health condition. The Microdosing GLP-1 program is for adults 18 to 74 with a body mass index over 20. Each program page states who the program is for.",
            ]),
            ("Clinician review", [
                "A physician or nurse practitioner licensed in your state reviews your intake. The clinician decides whether to prescribe, based solely on clinical judgment. Velacore has no say in that decision.",
                "Most reviews happen without a live appointment. A video visit is required for the first prescription in Arkansas, the District of Columbia, Delaware, Kansas, Mississippi, New Mexico, Rhode Island and West Virginia. Everywhere else a video visit is optional, and you can request one at any time at no extra cost.",
                'Clinician hours are 7am to 7pm Central Time. More about who the clinicians are and how they are credentialed is on the <a href="clinicians.html">clinicians page</a>.',
            ]),
            ("Pharmacy fulfillment", [
                "If the clinician prescribes, a licensed 503A compounding pharmacy prepares your medication to that prescription and ships it to you. Ongoing plans ship every four weeks.",
                "Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
                "For the Semaglutide and Tirzepatide programs, the clinician also orders baseline labs at a national laboratory at no cost to you. In most cases you can start medication before the results are back. For other programs the clinician will tell you if labs are recommended.",
                'A 503A pharmacy prepares medication for one named patient from a valid prescription. Our article on <a href="learn/what-is-a-503a-compounding-pharmacy.html">what a 503A compounding pharmacy is</a> explains the term.',
            ]),
            ("Ongoing reviews and support", [
                "A prescription is not a one-time event. The clinician reviews your intake updates on a schedule that depends on the program.",
                '- <strong><a href="programs/semaglutide.html">Semaglutide</a> and <a href="programs/tirzepatide.html">Tirzepatide</a>.</strong> Each month you update a short intake. The clinician reviews it with your labs and decides whether to hold or change the dose. Once your dose is steady, reviews move to every three months.\n'
                '- <strong><a href="programs/microdosing.html">Microdosing GLP-1</a>.</strong> The first prescription is a 4-week supply. After that you update a short intake every 12 weeks and the clinician reviews it.\n'
                '- <strong><a href="programs/nad.html">NAD+</a>, <a href="programs/glutathione.html">Glutathione</a> and <a href="programs/sermorelin.html">Sermorelin</a>.</strong> The first prescription is a 4-week supply. The clinician reviews an intake update at 3 to 4 weeks before writing a 12-week refill, and reviews continue every 12 weeks.',
                "Nothing about your prescription changes without a clinician's review.",
                "Patient support is available 24 hours a day, every day. You can message your clinician or request a video visit through your patient portal. If you are experiencing a medical emergency, call 911 or go to the nearest emergency room.",
            ]),
            ("If the clinician does not prescribe", [
                "A prescription is not guaranteed. Prescriptions are issued only when the clinician decides one is clinically appropriate.",
                "If the clinician does not prescribe, nothing is ordered and your program payment is refunded in full to your original payment method.",
                'After you start, you can cancel at any time for any reason. You can request a refund for any month whose medication has not yet been ordered. Medications are non-returnable once dispensed, as required by federal and state pharmacy law. The full terms are in the <a href="refund-policy.html">refund policy</a>.',
            ]),
            ("What Velacore does and does not do", [
                "Velacore Health is a telehealth coordination platform. Here is what that covers.",
                "- We run this website.\n"
                "- We explain the programs and show their prices.\n"
                "- We point you to the secure intake.\n"
                "- We answer questions about how the service works.",
                "Here is what it does not cover.",
                "- We do not practice medicine or give medical advice.\n"
                "- We do not prescribe, and we have no say in whether a clinician prescribes.\n"
                "- We do not make, compound or ship medication.\n"
                "- We do not hold your card details. Our telehealth services partner bills you.\n"
                "- We do not promise that you will be prescribed anything.",
                "The intake, the clinician review, billing and patient support are run by our telehealth services partner on its own secure pages.",
            ]),
        ],
        "faq": [
            ("Do I have to speak with a clinician live?", "In most states, no. Most reviews happen without a live appointment. A video visit is required for the first prescription in Arkansas, the District of Columbia, Delaware, Kansas, Mississippi, New Mexico, Rhode Island and West Virginia."),
            ("Can I start medication before my lab results are back?", "For the Semaglutide and Tirzepatide programs, in most cases yes. The clinician reviews the results at your first monthly review. That decision belongs to the clinician."),
            ("How often does medication ship?", "Ongoing plans ship every four weeks."),
            ("Does Velacore decide whether I am prescribed?", "No. The independent licensed clinician decides, based solely on clinical judgment. Velacore coordinates access and education."),
        ],
    },
    {
        "slug": "clinicians",
        "title": "The clinicians who review your intake",
        "meta": "Physicians and nurse practitioners licensed in your state review every intake. They are independent of Velacore. Prescription required.",
        "h1": "The clinicians who review your intake",
        "lede": "Every intake is reviewed by a physician or nurse practitioner who holds an active license in your state. The clinician is independent of Velacore, and the prescribing decision is theirs alone.",
        "sections": [
            ("Who reviews your intake", [
                "Your intake is reviewed by a licensed physician or nurse practitioner. The clinicians are medical doctors, doctors of osteopathic medicine and nurse practitioners.",
                "They are engaged through our telehealth services partner, not by Velacore. Your clinician may vary based on your state and availability.",
                "Every program on this site is prescription only. Prescription required.",
            ]),
            ("Licensed in your state", [
                "The clinicians are licensed across all 50 states. Your intake goes to a clinician who holds an active license in the state where you live.",
                "Velacore telehealth services are available in all 50 US states and the District of Columbia. Every prescription requires review by a clinician licensed for your state.",
            ]),
            ("Credentialed before they review an intake", [
                "Our telehealth services partner credentials each clinician before that clinician reviews a single intake. The process covers these checks.",
                "- A primary source background check.\n"
                "- A review of education and training.\n"
                "- A review of work history.\n"
                "- A review of board certification.\n"
                "- A review of state board standing and state licenses.\n"
                "- Verification of the National Provider Identifier.\n"
                "- A review of liability coverage and malpractice history.\n"
                "- A review of federal and state sanction and exclusion lists.\n"
                "- A review of the National Practitioner Data Bank.\n"
                "- Signed attestations from the clinician.",
                "Malpractice coverage is in place for the clinicians.",
            ]),
            ("Independent of Velacore", [
                "Clinicians are independent providers. They are <strong>not employed by Velacore Health</strong>, and Velacore does not direct their decisions.",
                "Every prescribing decision is made at the clinician's own clinical discretion. Velacore coordinates access and education. It does not prescribe, and it has no say in whether a clinician prescribes.",
            ]),
            ("Hours", [
                "Clinician hours are 7am to 7pm Central Time and do not include holidays.",
                "Patient support is separate from clinician hours. It is available 24 hours a day, every day.",
                "Telehealth is not for emergencies. If you are experiencing a medical emergency, call 911 or go to the nearest emergency room.",
            ]),
            ("Video visits", [
                "Most reviews happen without a live appointment. The clinician reads your intake and decides.",
                "A live video visit is required for the first prescription in these states.",
                "- Arkansas\n"
                "- District of Columbia\n"
                "- Delaware\n"
                "- Kansas\n"
                "- Mississippi\n"
                "- New Mexico\n"
                "- Rhode Island\n"
                "- West Virginia",
                "Everywhere else a video visit is optional. You can request one at any time at no extra cost.",
            ]),
            ("What a clinician can decide", [
                "- Whether to prescribe at all. A prescription is not guaranteed.\n"
                "- Which program, if any, is appropriate for you.\n"
                "- The form and the dose, within the options of the program.\n"
                "- Whether to hold or change a dose at each review.\n"
                "- Whether labs are recommended. For the Semaglutide and Tirzepatide programs, baseline labs are ordered at a national laboratory at no cost to you.\n"
                "- For the Semaglutide and Tirzepatide programs, whether to prescribe an optional nausea medication that you pick up at a local pharmacy.",
                'If the clinician does not prescribe, nothing is ordered and your program payment is refunded in full. The order of events is set out on the <a href="how-it-works.html">how it works page</a>.',
            ]),
        ],
        "faq": [
            ("Are the clinicians employed by Velacore?", "No. They are independent providers engaged through our telehealth services partner. Velacore does not direct their decisions."),
            ("Can I ask for a video visit even if my state does not require one?", "Yes. You can request a video visit at any time at no extra cost."),
            ("Can the clinician decide on a different program from the one I picked?", "Yes. You choose the program you want to start with, and the clinician decides which program, if any, is appropriate. If the clinician does not prescribe, your program payment is refunded in full."),
            ("When are clinicians available?", "Clinician hours are 7am to 7pm Central Time and do not include holidays. Patient support is available 24 hours a day, every day."),
        ],
    },
    {
        "slug": "pricing",
        "pricing": True,   # visual layout, Nov 17 2026: cards first, short bands, the paragraphs below fold under them
        "title": "Pricing: what one program price includes",
        "meta": "One price per program with no separate consultation or physician fee. Plans, payment methods, refunds and cancellation. Prescription required.",
        "h1": "Pricing",
        "lede": "Each program has one price, shown before you start. There is no separate consultation or physician fee. Prescription required.",
        "sections": [
            ("What one price includes", [
                "The program price covers the parts of the service that would otherwise be billed one by one.",
                "- The medication, if the clinician prescribes it.\n"
                "- The clinician's review of your intake and of each intake update after that.\n"
                "- A video visit on request, at no extra cost.\n"
                "- Patient support 24 hours a day, every day.\n"
                "- For the Semaglutide and Tirzepatide programs, baseline labs at a national laboratory.",
                "There is no separate consultation fee and no separate physician fee. Each program page lists exactly what its price includes.",
            ]),
            ("Two ways to pay", [
                "Each program offers two plan types.",
                "- <strong>Month to month.</strong> You are charged each month. You can cancel at any time.\n"
                "- <strong>Prepaid plan.</strong> You are charged once, up front. Medication still ships every four weeks. The 12-week plan is priced below, and 24 and 52 week plans are also offered.",
                "You choose the plan when you start. The clinician's review is the same on both.",
            ]),
            ("Programs and prices", [
                "{{price_table}}",
                "The prices shown are illustrative until our telehealth services partner's final price list is confirmed.",
                "Every program is prescription only, and the clinician decides whether a program is appropriate for you. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
            ]),
            ("What is not included or not accepted", [
                "- <strong>Insurance.</strong> Programs are paid out of pocket and are not billed to insurance.\n"
                "- <strong>American Express.</strong> It is not accepted at this time.\n"
                "- <strong>Returns.</strong> Medications are non-returnable once dispensed, as required by federal and state pharmacy law.",
            ]),
            ("Payment methods", [
                "Accepted payment methods are Visa, Mastercard, FSA and HSA cards, Apple Pay and Google Pay.",
                "Billing is handled by our telehealth services partner. Its name is the one you will see on your card statement. Velacore does not hold your card details.",
            ]),
            ("Refunds and cancellation", [
                "If the clinician does not prescribe, nothing is ordered and your program payment is refunded in full.",
                "You can cancel at any time, for any reason, from your patient portal or by contacting support. Cancellation stops future charges. A month whose medication has already been ordered will still ship and is not refunded.",
                "You can request a refund at any time for any reason. The refund covers every billing period for which medication has not yet been ordered. On a 12-week plan, the shipments not yet ordered are refunded on the same basis.",
                'Refunds go back to the original payment method. The full terms are in the <a href="refund-policy.html">refund policy</a>.',
            ]),
        ],
        "faq": [
            ("Is there a consultation fee?", "No. There is no separate consultation fee and no separate physician fee. The clinician's review is part of the program price."),
            ("Can I pay with an FSA or HSA card?", "Yes. FSA and HSA cards are accepted, along with Visa, Mastercard, Apple Pay and Google Pay."),
            ("Can I bill a program to my insurance?", "No. Programs are paid out of pocket and are not billed to insurance."),
            ("What happens to a 12-week plan if I cancel?", 'Cancellation stops future charges, and the shipments not yet ordered are refunded. A month whose medication has already been ordered will still ship and is not refunded. The full terms are in the <a href="refund-policy.html">refund policy</a>.'),
            ("Whose name will be on my card statement?", "Our telehealth services partner's. It handles billing and issues refunds."),
        ],
    },
    {
        "slug": "about",
        "title": "About us: a telehealth coordination platform",
        "meta": "Velacore Health is a telehealth coordination platform operated by First Venture Group LLC. What we do and what we do not do. Prescription required.",
        "h1": "About Velacore Health",
        "lede": "Velacore Health is a telehealth coordination platform. We connect adults in the United States with independent licensed clinicians and licensed 503A compounding pharmacies.",
        "sections": [
            ("Who operates Velacore", [
                "Velacore Health is operated by First Venture Group LLC.",
            ]),
            ("How it works", [
                "Three parties, three jobs.",
                "1. <strong>Velacore coordinates.</strong> We run this website, explain the programs and their prices, and point you to the secure intake.\n"
                "2. <strong>An independent clinician decides.</strong> A physician or nurse practitioner licensed in your state reviews your intake and decides whether a prescription is appropriate. That decision is theirs alone.\n"
                "3. <strong>A 503A pharmacy fills.</strong> If you are prescribed, a licensed 503A compounding pharmacy prepares your medication and ships it to you.",
                'The intake, the clinician review, billing and patient support are run by our telehealth services partner on its own secure pages. Each step is set out on the <a href="how-it-works.html">how it works page</a>.',
            ]),
            ("What we offer access to", [
                'Six programs: <a href="programs/tirzepatide.html">Tirzepatide</a>, <a href="programs/semaglutide.html">Semaglutide</a>, <a href="programs/microdosing.html">Microdosing GLP-1</a>, <a href="programs/nad.html">NAD+</a>, <a href="programs/glutathione.html">Glutathione</a> and <a href="programs/sermorelin.html">Sermorelin</a>. Every one is prescription only. Prescription required.',
                "Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.",
                '<a href="pricing.html">See programs and prices</a>.',
            ]),
            ("What we do not do", [
                "- We do not practice medicine or give medical advice.\n"
                "- We do not prescribe, and we have no say in whether a clinician prescribes.\n"
                "- We do not make, compound or ship medication.\n"
                "- We do not collect your health information on this website.\n"
                "- We do not hold your card details. Our telehealth services partner bills you.\n"
                "- We do not bill insurance.\n"
                "- We do not promise that you will be prescribed anything.",
            ]),
            ("What you can expect from us", [
                "- Prices shown before you start.\n"
                "- A plain explanation of each step.\n"
                "- Cancel any time, for any reason.\n"
                "- A full refund of your program payment if the clinician does not prescribe.\n"
                '- Straight answers by email at <a href="mailto:hello@velacorehealth.com">hello@velacorehealth.com</a>.',
            ]),
            ("Where we serve", [
                "All 50 US states and the District of Columbia. Every prescription requires review by a clinician licensed for your state.",
            ]),
            ("Please note", [
                "Velacore Health does not provide, guarantee or facilitate any medical services, prescriptions or treatments. All medical decisions are made solely by the independent clinician. Content on this site is general information and is not medical advice.",
            ]),
        ],
        "faq": [
            ("Is Velacore Health a pharmacy?", "No. Velacore does not make, compound or ship medication. Prescriptions written by the independent clinicians are filled by licensed 503A compounding pharmacies."),
            ("Is Velacore Health a medical practice?", "No. Velacore is a telehealth coordination platform. It does not practice medicine, and every medical decision is made solely by the independent clinician."),
            ("Who owns Velacore Health?", "Velacore Health is operated by First Venture Group LLC."),
        ],
    },
    {
        "slug": "contact",
        "title": "Contact us",
        "meta": "Email Velacore Health about programs, pricing and policies. Medical questions go to your clinician. In an emergency call 911. Prescription required.",
        "h1": "Contact us",
        "lede": "Velacore Health coordinates access to licensed clinicians and 503A pharmacies. Here is who to reach for what.",
        "sections": [
            ("In an emergency", [
                "If this is a medical emergency, call 911 or go to the nearest emergency room. If you are thinking about harming yourself, call or text 988 to reach the Suicide and Crisis Lifeline. Do not email us for urgent help.",
            ]),
            ("Questions about how Velacore works", [
                'Email <a href="mailto:hello@velacorehealth.com">hello@velacorehealth.com</a>. Use this for questions about the programs, pricing, how a visit works, this website, or our policies.',
                "Please do not put health details in an email to us. That means no symptoms, no medications, no medical history, no photos of ID. We are not your clinician and regular email is not the right place for that information.",
            ]),
            ("Medical questions", [
                "Medical questions go to your clinician, not to Velacore. We cannot give medical advice.",
                "If you are already a patient, message your clinician or ask for a video visit through your patient portal. Patient support is available 24 hours a day, every day.",
                "If you are not yet a patient, the place to ask is your intake. A licensed clinician reviews it and decides whether a program is appropriate for you. Prescription required.",
            ]),
            ("Billing, refunds, shipping and changes to your order", [
                'These are handled by our telehealth services partner, whose name appears on your card statement. Use the support link in your patient portal. You can also email us at <a href="mailto:hello@velacorehealth.com">hello@velacorehealth.com</a> with your name and the email on your account, and we will pass your request along. See the <a href="refund-policy.html">refund policy</a>.',
            ]),
            ("Privacy requests", [
                'Email <a href="mailto:hello@velacorehealth.com">hello@velacorehealth.com</a> with the subject line Privacy request. Read our <a href="privacy.html">privacy policy</a>.',
            ]),
            ("Please note", [
                "Velacore Health does not provide medical services or prescriptions. All medical decisions are made solely by the independent clinician. All medications are prescription only.",
            ]),
        ],
        "faq": [],
    },
]
