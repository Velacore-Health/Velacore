# Title tags, meta descriptions and the home page top, drafts, Nov 18 2026

Drafts only. No site file has been edited. Nothing here goes live until vc-reviewer clears it and Dourado says yes.

How to read the counts:

- Every count includes spaces and punctuation.
- Title counts include the " | Velacore Health" ending, which is 18 characters. The build adds that ending, so the value to paste into the data file is the title without it.
- Counts were made by hand. Vale should confirm them with a quick length check before the build.
- Limits used: titles 60 or fewer, meta descriptions 155 or fewer.

The model followed, not copied: on the home page the brand comes first, then the categories plus "Telehealth". On program pages the search term comes first, for example "Compounded Semaglutide, Online Visit". Prices go in the meta description, never in the title, because prices are still placeholders until the OpenLoop Agile proposal is signed, and a title is harder to keep in step than a description.

Every price below was read from the plan notes in `tools/build_programs.py` on Nov 18 2026.

## Home, public/index.html, hand-written

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Velacore Health \| Clinician-Reviewed Peptide Telehealth | Velacore Health \| GLP-1 and Peptide Telehealth | Velacore Health is a telehealth platform that coordinates access to licensed clinicians and 503A compounding pharmacies. Prescription GLP-1 and peptide programs, reviewed by a clinician, shipped to your door. Prescription required. | Online visits for Tirzepatide, Semaglutide, Microdosing GLP-1, NAD+, Glutathione and Sermorelin. A licensed clinician decides. Prescription required. |
| 55 | 46 | 231 | 149 |

Note: the old meta was cut off in search at about 155. The new one names all six programs and keeps the clinician and prescription facts. The og and twitter title and description tags in the same file should get the same new text.

## Tirzepatide, programs/tirzepatide

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Tirzepatide Program, Reviewed Online \| Velacore Health | Compounded Tirzepatide, Online Visit \| Velacore Health | Compounded tirzepatide injection reviewed and prescribed by licensed clinicians in all 50 states. $199 first month, then $279 a month, shipping included. Prescription required. | Compounded tirzepatide injection. A licensed clinician decides. $199 first month, then $279 a month. Shipping included. Prescription required. |
| 54 | 58 | 176 | 142 |

Paste into the program data: title "Compounded Tirzepatide, Online Visit".

## Semaglutide, programs/semaglutide

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Semaglutide Program, Reviewed Online \| Velacore Health | Compounded Semaglutide, Online Visit \| Velacore Health | Compounded semaglutide, as an injection or an oral form, reviewed and prescribed by licensed clinicians in all 50 states. Injection $149 first month, then $229 a month; oral $259 a month; shipping included. Prescription required. | Compounded semaglutide. A licensed clinician decides. Injection $149 first month, then $229 a month; oral $259 a month. Prescription required. |
| 54 | 47 | 230 | 142 |

Paste into the program data: title "Compounded Semaglutide, Online Visit".

Note: "Shipping included" does not fit next to both prices. If Dourado wants the oral form in the title instead of the word Compounded, the alternative is "Semaglutide Online, Injection or Oral | Velacore Health", 55 characters.

## Microdosing GLP-1, programs/microdosing

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Microdosing GLP-1 Program, Reviewed Online \| Velacore Health | Microdosing GLP-1 Program Online \| Velacore Health | Low-dose GLP-1 combined with NAD+, B12 or amino acids, oral or injection, prescribed by licensed clinicians. $129 first month, then $179 a month, shipping included. Prescription required. | Low-dose GLP-1 with vitamins or amino acids, oral or injection. A licensed clinician decides. $129 first month, then $179 a month. Prescription required. |
| 60 | 50 | 187 | 153 |

Paste into the program data: title "Microdosing GLP-1 Program Online".

## NAD+, programs/nad

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| NAD+ Program, Reviewed Online \| Velacore Health | NAD+ Online Visit: Injection, Nasal, Oral \| Velacore Health | NAD+ as an injection, nasal spray or oral dropper, prescribed by licensed clinicians in all 50 states. $129 first month, then $199 a month, shipping included. Prescription required. | NAD+ injection, nasal spray or oral dropper. A licensed clinician decides. $129 first month, then $199 a month. Shipping included. Prescription required. |
| 47 | 55 | 181 | 153 |

Paste into the program data: title "NAD+ Online Visit: Injection, Nasal, Oral".

## Glutathione, programs/glutathione

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Glutathione Program, Reviewed Online \| Velacore Health | Compounded Glutathione, Online Visit \| Velacore Health | Glutathione in the form your clinician prescribes, prepared by a licensed 503A pharmacy, in all 50 states. $129 first month, then $199 a month, shipping included. Prescription required. | Glutathione, a peptide of three amino acids. A licensed clinician decides. $129 first month, then $199 a month. Shipping included. Prescription required. |
| 54 | 47 | 185 | 153 |

Paste into the program data: title "Compounded Glutathione, Online Visit".

Note: the Glutathione form and price are still placeholders until the written Agile proposal. The title names no form on purpose. If the proposal changes the price, the meta changes with it.

## Sermorelin, programs/sermorelin

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Sermorelin Program, Reviewed Online \| Velacore Health | Compounded Sermorelin, Online Visit \| Velacore Health | Compounded sermorelin injection prescribed by licensed clinicians in all 50 states. $129 first month, then $199 a month, shipping included. Prescription required. | Compounded sermorelin injection. A licensed clinician decides. $129 first month, then $199 a month. Shipping included. Prescription required. |
| 53 | 57 | 162 | 141 |

Paste into the program data: title "Compounded Sermorelin, Online Visit".

Build note for all six program pages: the price sentence in each meta should be built from the plan data, the same way the menu reads the first month price, so no number is typed twice.

## Start pages, start/each program, one shared template

These pages carry a noindex tag, so search engines leave them out. The title only shows in the browser tab and in shared links, so it stays as is. The meta is shortened because it ran past 155 on every page.

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Start your Tirzepatide visit \| Velacore Health | No change | Before your Tirzepatide visit: a short online intake on our telehealth partner's secure site, review by a licensed clinician, and a full refund if you are not prescribed. Prescription required. | A short online intake on our partner's secure site, then a licensed clinician decides. Full refund if not prescribed. Prescription required. |
| 46 | 46 | 193 | 140 |

Current title lengths for the other five: Semaglutide 46, Microdosing GLP-1 52, NAD+ 39, Glutathione 46, Sermorelin 45. The new meta has no program name in it, so it is 140 on every Start page.

## How it works, how-it-works, tools/pages.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| How Velacore works: intake, clinician review, pharmacy \| Velacore Health | How It Works: Intake, Review, Pharmacy \| Velacore Health | Online intake, a licensed clinician reviews it, then a 503A pharmacy fills. What happens at each step. Prescription required. | You answer questions online, a licensed clinician decides whether to prescribe, and a 503A pharmacy fills and ships the order. Prescription required. |
| 72 | 56 | 125 | 149 |

## Clinicians, clinicians, tools/pages.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| The clinicians who review your intake \| Velacore Health | Independent Licensed Clinicians \| Velacore Health | Physicians and nurse practitioners licensed in your state review every intake. They are independent of Velacore. Prescription required. | Physicians and nurse practitioners licensed in your state review each intake. Independent of Velacore, credentialed before care. Prescription required. |
| 55 | 49 | 135 | 151 |

Removed nothing factual. Added "credentialed before care", which rests on Schedule B of the OpenLoop proposal and is already on the page.

## Pricing, pricing, tools/pages.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Pricing: what one program price includes \| Velacore Health | GLP-1 and Peptide Program Prices \| Velacore Health | One price per program with no separate consultation or physician fee. Plans, payment methods, refunds and cancellation. Prescription required. | First month from $129, then from $179 a month. One price covers medication, clinician reviews and shipping. No consultation fee. Prescription required. |
| 58 | 50 | 142 | 151 |

Note: $129 is the lowest first month and $179 the lowest month to month price in the plan data. Both are month to month, so neither needs a prepaid plan to be true, which keeps to guardrail 6 in the pricing research.

## About, about, tools/pages.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| About us: a telehealth coordination platform \| Velacore Health | About Our Telehealth Platform \| Velacore Health | Velacore Health is a telehealth coordination platform operated by First Venture Group LLC. What we do and what we do not do. Prescription required. | Velacore Health is a telehealth platform operated by First Venture Group LLC. Independent clinicians decide. 503A pharmacies fill. Prescription required. |
| 62 | 47 | 147 | 153 |

## Contact, contact, tools/pages.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Contact us \| Velacore Health | Contact Us \| Velacore Health | Email Velacore Health about programs, pricing and policies. Medical questions go to your clinician. In an emergency call 911. Prescription required. | No change |
| 28 | 28 | 148 | 148 |

Only the capital U changes, to match the other titles.

## FAQ, public/faq.html, hand-written

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Questions, answered \| Velacore Health | FAQ: Prescriptions, Refunds, Eligibility \| Velacore Health | Answers about prescriptions, clinicians, refunds, fees, eligibility, labs, shipping, privacy and the states Velacore Health serves. | Answers on prescriptions, refunds, fees, eligibility, labs and shipping. Not prescribed? Your program payment is refunded in full. Prescription required. |
| 37 | 58 | 131 | 153 |

The og title and description tags in the same file should match.

## Learn, public/learn.html, hand-written

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Peptides, explained simply \| Velacore Health | What Are Peptides and GLP-1s? \| Velacore Health | What peptides are, how they are made and taken, and how they differ from GLP-1s. Plain-language education from Velacore Health. Not medical advice. | What peptides are, how they are made and taken, and how they differ from GLP-1s. Plain-language education, not medical advice. Prescription required. |
| 44 | 47 | 147 | 149 |

The og title and description tags in the same file should match.

## Article, learn/how-to-get-a-glp-1-prescription-online, tools/articles.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| How to get a GLP-1 prescription online: the steps \| Velacore Health | How to Get a GLP-1 Prescription Online \| Velacore Health | Online intake, review by a licensed clinician, a video visit in some states, then a pharmacy fills. A prescription is not guaranteed. | The steps: an online intake, review by a licensed clinician, a video visit in some states, then a 503A pharmacy fills. A prescription is not guaranteed. |
| 67 | 56 | 133 | 152 |

## Article, learn/semaglutide-vs-tirzepatide, tools/articles.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| Semaglutide vs tirzepatide: how the two differ \| Velacore Health | Semaglutide vs Tirzepatide Explained \| Velacore Health | Semaglutide acts on the GLP-1 receptor. Tirzepatide acts on the GIP and GLP-1 receptors. A plain look at the mechanisms. Prescription required. | No change |
| 64 | 54 | 143 | 143 |

The meta already says what the article is, mechanism only, with no ranking of the two.

## Article, learn/what-is-a-503a-compounding-pharmacy, tools/articles.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| What is a 503A compounding pharmacy? 503A vs 503B \| Velacore Health | What Is a 503A Pharmacy? 503A vs 503B \| Velacore Health | A 503A pharmacy compounds medication for one patient from a prescription. How it differs from a 503B outsourcing facility, and who regulates each. | No change |
| 67 | 55 | 146 | 146 |

## Article, learn/what-is-microdosing-glp-1, tools/articles.py

| Current title | New title | Current meta | New meta |
|---|---|---|---|
| What is microdosing GLP-1? Low dose vs standard dose \| Velacore Health | What Is Microdosing GLP-1? \| Velacore Health | Microdosing GLP-1 means a lower dose than standard programs. It is not an FDA-defined term. What it means and how our program describes it. | No change |
| 70 | 44 | 139 | 139 |

## Legal pages

Privacy Policy, Terms of Service, Telehealth Consent and Refund Policy keep their plain names and their current tags. Not touched.

## The word "weight loss": my call

It does not appear in any title or meta description, not even as a category label.

Why:

1. A title is about 50 characters with no room for a qualifier. Next to a drug name, a reader cannot tell a category label from a promise. "Semaglutide for Weight Loss" reads as what the medication will do for you. That is an outcome claim, and it is attached to a compounded medication that the FDA has not approved.
2. COMPLIANCE.md asks for factual, mechanistic copy. The site's cleared words for this category are "Weight" and "GLP-1 weight programs". "Weight loss" would be a new term nobody has cleared.
3. The title and meta are the most-read words Velacore publishes. They show up in search results and in shared links on their own, with no top bar and no disclaimer beside them.
4. The search cost is small. People with high intent search for the drug names and "GLP-1", and those words lead every new title. I have no search volume data, so this is a judgment, not a measurement.

If Dourado wants a category word in a title later, "GLP-1 weight program" is already cleared on the page. "Weight management" would be the next thing to try, and it needs vc-reviewer's call first.

Flag for vc-reviewer: please confirm the no-"weight loss" call. Please also clear the "Compounded [name] Online" title pattern, which puts the honest word "compounded" first but sits closer to online-sale wording than the old "Reviewed Online" titles did.

## The home page top

### New H1, options

1. GLP-1 and peptide programs, online
2. Prescription programs, started online
3. Telehealth for GLP-1s and peptides
4. Pick a program to start
5. Choose where to start

I recommend option 1, "GLP-1 and peptide programs, online". It is five words and says what the service is. It matches the words in the new home title, makes no claim, and leaves the big image cards to do the selling, which is the Hims model. Option 3 is a close second if Dourado wants the word telehealth up top. I left out "Find your program" and "What are you here for?" because they are already the nav button and the goal band heading, and a repeated H1 reads like an echo.

### The sub line

Cut it to one short line rather than removing it:

Prescription only. No consultation fee. Shipping included.

Removed from the old line: the explanation that "an independent licensed clinician decides whether to prescribe, and a 503A compounding pharmacy fills the order." That now lives on How it works and Clinicians, as Dourado asked.

Why keep one line instead of none: once the clinician sentence goes, nothing beside the H1 says these are prescription programs. "Prescription only" puts that fact next to the product names at first glance. The other two facts help a buyer and are already on the pricing page. The business model is still disclosed in the first screen and a half: the top bar says "Clinician-reviewed telehealth" and "Prescription required", and the weight band right under the cards says "A licensed clinician in your state reviews your intake and decides what is appropriate for you." The footer disclaimer is unchanged.

Flag for vc-reviewer: please confirm that the top bar, the weight band line and the footer are enough business-model disclosure once the hub sub line is gone.

## Two small things I noticed, not changed

- The facts given for this task say all 50 states plus DC. The top bar on every page says "all 50 states". If DC is confirmed in writing, the top bar can say "all 50 states and DC".
- The home page og and twitter tags carry their own description text. They should be updated with the new home meta so shared links match search.

vc-copy

FOR DOURADO, Velacore Health

---

## vc-reviewer rulings, Nov 18 2026, applied by Vale

- Program titles changed to the "Online Visit" form so a title never reads as Velacore selling the drug. Microdosing GLP-1 Program Online stays as written.
- "Weight loss" and "Weight management" are both out of titles and metas. The cleared category words stay "Weight" and "GLP-1 weight program".
- The home top must still say on the first screen that Velacore is a platform and that independent clinicians decide. Vale's recommendation, to keep the hub as lean as Dourado wants: change the top bar on every page to "A telehealth platform. Independent licensed clinicians decide. Prescription required." and keep the hub sub line as "Prescription only. No consultation fee. Shipping included." Check the top bar at 375 before shipping. Awaiting Dourado's choice.
