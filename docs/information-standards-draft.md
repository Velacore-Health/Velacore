# Information standards page, draft

Draft by vc-copy, Nov 20 2026. Not in tools/pages.py, not built, not published. It needs vc-reviewer and then Dourado's word before it goes anywhere. The labels below match the keys of a PAGES entry. Links are written as HTML, the same way the other entries carry them.

## slug

information-standards

## title

How We Check the Information on This Site

## meta

Where the facts and prices on this site come from, who writes them, and how to report an error. A licensed clinician decides care. Prescription required.

## h1

How we check our information

## lede

Here is where the facts on this site come from, who writes them and what we leave out on purpose. A licensed clinician decides your care, not this website.

## sections

### Where our information comes from

Program facts and prices come from the written program terms of our telehealth services partner.

Our education articles cite public pages from the FDA and the National Institute of Diabetes and Digestive and Kidney Diseases. Each article lists its sources.

### Who writes and reviews it

Velacore Health writes the pages and the education articles on this site.

The education articles have not been reviewed by a clinician. Each article says so beside its date. They are general education, not medical advice.

### Prices

Every price on this site is read from one list, so each page shows the same number.

Prices are set by our telehealth services partner, not by Velacore. You can see them on the <a href="pricing.html">pricing page</a>.

### A licensed clinician decides

Velacore Health is a telehealth coordination platform. We are not a provider or a prescriber, and this website does not give medical advice.

An independent licensed clinician reviews your intake and decides whether to prescribe. If the clinician prescribes, a licensed 503A compounding pharmacy fills the prescription. Prescription required.

Reading this site does not create a clinician and patient relationship.

### What compounded means

A compounded medication is prepared by a licensed pharmacy for one named patient, after a clinician writes a prescription for that patient.

Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy.

### What we leave out on purpose

- We make no promises about outcomes.
- We do not promise that you will be prescribed anything. The clinician decides.
- Product images are illustrations. Your medication is prepared and labeled by a licensed 503A pharmacy and may look different.

### Updates and corrections

We update a page when a price, a program detail or a fact changes, not on a calendar. Each education article shows the date it was last updated.

Found something wrong? Email <a href="mailto:hello@velacorehealth.com">hello@velacorehealth.com</a> and tell us which page. Please leave health details out of the email.

Do not email us for urgent help. If this is a medical emergency, call 911.

## faq

### Has a clinician reviewed the articles on this site?

No. Velacore Health writes them, and they have not been reviewed by a clinician. They are general education, not medical advice.

### Who sets the prices?

Our telehealth services partner sets them. Every price on this site is read from one list, so each page shows the same number.

### Is this site medical advice?

No. It is general information. A licensed clinician reviews your intake and makes every prescribing decision.

## Notes for Vale

Counts, done by hand: title 41 characters, meta 153 characters, seven sections, three FAQ pairs, about 440 words of copy with the FAQ included. The builder's own length checks will confirm the first two.

Claims I was not able to trace to a file in the repo, or traced only in part:

1. "We update a page when a price, a program detail or a fact changes, not on a calendar." This came from the brief. No file in the repo states it as a rule. It is also a promise about what we will keep doing, so Dourado should agree to it knowingly.
2. "Velacore Health writes the pages and the education articles on this site." The article half is the live byline in tools/build_articles.py line 130. The pages half is not stated in any public file; I carried the byline's wording over to the stand-alone pages.
3. "Every price on this site is read from one list." Traced for the pricing page in tools/build_pages.py, the program and Start pages in tools/build_programs.py, and the home cards and hero line in tools/inject_panel.py. Not traced for public/faq.html, the legal pages or the Learn articles. public/learn/what-is-microdosing-glp-1.html shows one more dollar figure than the other articles and I did not find where it comes from. If any price on those pages is typed by hand, this sentence is not true yet.
4. "Prices are set by our telehealth services partner, not by Velacore." Traced to the Nov 20 written answer in docs/openloop-proposal-notes.md. Two things sit beside it. The pricing page still carries the line that prices are illustrative until the partner's final price list is confirmed, and the notes say final terms come with the executed Order Form, which is not signed. Decide whether this page should carry the same pending line or whether that line is ready to retire.
5. "Reading this site does not create a clinician and patient relationship." The nearest source is section 2 of public/terms.html, which says using this site does not create a physician and patient relationship with Velacore. My wording differs, and the legal pages themselves are still waiting on attorney review per COMPLIANCE.md.
6. "Our education articles cite public pages from the FDA and the National Institute of Diabetes and Digestive and Kidney Diseases." True for the four articles in tools/articles.py today. It goes stale the day an article cites any other source.
7. "Each article lists its sources" and "Each article says so beside its date." Traced to the template in tools/build_articles.py lines 130 and 141. I did not open the four built pages to see them rendered.
8. "We make no promises about outcomes." This is the rule in COMPLIANCE.md. Whether every live page keeps it is what the compliance scan proves, and I could not run the scan.

Things I changed or left out against the brief, and why:

- The brief asked for "never a provider, prescriber or coach". I left the last word out. The compliance scan fails any public page that contains it, and the hard rule is no coaching language. The line now reads "not a provider or a prescriber".
- The copy says nothing about whether the program pages, the stand-alone pages or the legal pages have had clinician or attorney review. Only the articles are covered, because that is the only review statement the site already makes. A reader could assume the rest was reviewed. If Dourado wants a plain line on that, it needs his decision.
- No treatment is named. "Prescription required" is still in the meta and in the clinician section.
- No link to the 503A article from the compounded section. I was not sure of the link path from a root page to a Learn article. It would be a useful link if you add it.

Not done:

- The compliance scan was not run. This session had no way to run scripts, and the scanner reads public/, not docs/. I checked the copy by hand against the claim and coaching patterns in the scanner, lines 43 to 59, and found no match. vc-reviewer should clear it once it is in tools/pages.py and built.
- Dourado's Nov 20 approval to build this page is not recorded in docs/HANDOFF.md. Worth logging when you update the status block.
- The page is not in the footer, the sitemap or tools/seo_head.py. That is build work for Vale.

vc-copy

FOR DOURADO, Velacore Health
