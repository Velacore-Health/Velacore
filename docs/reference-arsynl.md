# Reference site: arsynl.com

Reviewed Nov 6 2026 at Dourado's request as the model for how the Velacore site should be set up. ARSYNL Rx is the operator who confirmed the original product list. They are LegitScript certified and run the same shape we are moving to: a marketing site that links out to a hosted intake.

## How their site is built

Home page, top to bottom:
1. Hero: headline, one paragraph, one button "Shop Therapies", three goal chips. Photo collage on the right.
2. Trust bar: LegitScript Certified, HIPAA Compliant, US-Licensed Providers, Veteran-Founded. Repeated on every product page.
3. Why ARSYNL: four tiles. Secure, free shipping, 100 percent online, mission.
4. Founder story with a one-minute video.
5. Symptom section: "Feeling off isn't just getting older", a list of signs, a stat, a "See treatment options" button.
6. Outcomes section. This is where they make claims we will not make.
7. Category grid: six categories, each with a "View products" link.
8. Delivery format comparison table.
9. "Get started in 3 simple steps": intake, provider review, ship with check-ins.
10. Best sellers: three product cards with price range, "Learn More" and "See if I qualify".
11. Comparison table, ARSYNL vs others.
12. Mission and nonprofit block with three stats: veteran-founded, 50 states, 24/7 provider messaging.
13. FAQ accordion with a "Get started today" button.
14. Program strip: "$199.99 a month, starting price, billed monthly, cancel anytime" with four bullets.
15. Blog teasers, four posts dated within the last two weeks.
16. Footer: Privacy Policy, Terms of Use, Returns and Refund, Informed Consent for Telehealth, LegitScript seal, disclaimer, email, phone, Dover DE address.

Product page, `/products/<slug>/`:
1. Breadcrumb, category label, product name as the H1, one paragraph.
2. Hero image with three seals on it. Six benefit bullets in two columns.
3. Price box: "$269 a month", plan selector "1-Month Plan", "Flexible, billed monthly".
4. The compounded-medication disclaimer directly under the price box, in full.
5. Trust bar again.
6. "Sound familiar?" dark panel with eight symptom bullets and a qualify button.
7. "What is tirzepatide + B6", mechanistic paragraph, six fact bullets, two buttons.
8. "A titration plan, not a refill": provider reviews before every dose increase, flat pricing, supplies and nausea support included.
9. Testimonials carousel, named, aged, "verified customer".
10. How to use it. More FAQ. Qualify buttons repeated about five times down the page.

Intake: "See if I qualify" leaves arsynl.com and lands on `carerx.arsynl.com`, their vendor's hosted intake on an ARSYNL subdomain, with an "intake first" checkout flow. Our Launchpad plan is the same shape. Ask OpenLoop to mask Launchpad on a Velacore subdomain, for example `intake.velacorehealth.com`.

Refunds: all sales final once the pharmacy dispenses and the carrier has the package; cancel in the account before it ships. Ours is more generous under OpenLoop: refund any month not yet ordered.

## Their prices against ours, read Nov 6 2026

ARSYNL shows a price range per product; the low end is one month, the high end is a multi-month pack. Their home page headline is "$199.99 a month, starting price, billed monthly".

| Product | ARSYNL, monthly | Velacore planned, month to month | Velacore first month | Velacore 12-week plan |
|---|---|---|---|---|
| Semaglutide injection | $219 | $229 | $149 | $199/mo |
| Tirzepatide injection | $269 | $279 | $199 | $249/mo |
| Microdosing GLP-1 | not offered | $179 | $129 | $159/mo |
| NAD+ | not shown on the home page | $199 | $129 | $169/mo |
| Sermorelin | not shown on the home page | $199 | $129 | $169/mo |
| Glutathione | $139 | off our site | | |

They also sell sildenafil and tadalafil from $64, low dose naltrexone from $79, testosterone from $239, and hair loss. None of those are on our list.

Reading: on the plain monthly price we sit $10 above them on both GLP-1s. On everything a shopper actually compares we are under: the first month is $70 cheaper, the 12-week plan is $20 a month cheaper, and our headline can honestly say "from $199 a month" on the 12-week plan, the same number as theirs. Microdosing at $179 is a tier they do not have.

Three ways to go, for Dourado to pick:
1. Keep $229 and $279, lead with "from $199 a month" and the first-month offer. Margin stays where the pricing memo wants it. Recommended.
2. Go to $209 and $259 month to month, $10 under them. At $209 semaglutide leaves about $114 a month after OpenLoop's example cost, which is right at the memo's floor for paying back a $200 acquisition cost. Only worth it if the lower price clearly lifts conversion; test it in Launchpad's A/B tool first.
3. Match at $219 and $269. Splits the difference, loses the "cheaper than" story on monthly, keeps a little margin.

## What to adopt for Velacore

1. A dedicated page per program at `/programs/<slug>/`: tirzepatide, semaglutide, microdosing, NAD+, sermorelin. Each with the hero, bullets, price box with a plan selector for month to month and the 12 and 24 week plans, the disclaimer under the price, a mechanistic "what it is", "a titration plan, not a refill" written to OpenLoop's monthly then quarterly reviews, how to use it, FAQ, and the Start visit button repeated. These pages are what Google ranks and what ads land on.
2. A trust bar under the hero and on every program page: HIPAA-compliant intake, licensed clinicians in all 50 states, 503A pharmacies, shipping included. The LegitScript seal goes in the same bar only once the certificate exists.
3. A patient portal icon in the header, next to the Start visit button.
4. A symptom-style section, written as questions people bring to a clinician, with no outcome promises. ARSYNL's "sound familiar" list is a good shape; the copy has to stay factual.
5. FAQ and Contact as their own pages, with the 24/7 support line once OpenLoop gives us the number.
6. A short founder note from Dourado on the home page and an About page. ARSYNL leans hard on the founder story; ours can be plainer. Dourado's call on how personal.
7. A blog with education posts, two a month to start, written by vc-copy and reviewed by vc-reviewer. Theirs is dated within days and feeds search.
8. A program strip near the bottom: "$149 first month, then $229 a month, cancel any time" with four bullets, as a second conversion point.
9. The qualify button repeated down every page, at least four times.

## What not to copy

- Efficacy and outcome claims: "47 percent more weight loss", "20.2 percent of body weight", "most effective weight loss medication ever studied", "less fat, more lean mass", "feel like yourself again". These break COMPLIANCE.md and Meta's health advertising rules.
- Brand-name comparisons: "the active molecule in Mounjaro and Zepbound". Never on our site.
- "Proven therapies", "money-back guarantee", invented statistics like "50 percent of adults show low hormone markers".
- Testimonials until we have real, consented, unpaid ones with the typical-results line.
- The ARSYNL vs others comparison table. It makes claims about competitors.
- Products outside our list. Their catalog includes items that are off our site by decision.

## Build order proposed

1. Program pages, five of them, from one template.
2. Trust bar and portal icon on the home page.
3. FAQ and Contact pages.
4. Symptom section and program strip on the home page.
5. About page and founder note, once Dourado writes or dictates the story.
6. Blog scaffold and the first two posts.
