# Velacore Health — Handoff (as of Oct 29, 2026)

Read this first in a new session, then `COMPLIANCE.md`, `shopify-theme/SETUP.md` and
`docs/openloop-call-guide.md`. Work on branch `claude/velacore-health-website-qnjdnh`.

## Who and what

Bryan Dourado, founder/CEO of **Velacore Health** (First Venture Group LLC). Direct-to-consumer
telehealth for peptides. Positioned ONLY as a **telehealth coordination platform** connecting patients
to independent licensed physicians and 503A compounding pharmacies. Not a provider, prescriber, or
wellness/health coach. Goal: LegitScript certification, then Meta/Google ads and real cash flow.
Bryan is non-technical: explain steps plainly and don't assume knowledge.

## What exists in the repo

- `public/` — static marketing site (Vercel, GA4 G-B2PQL4DLF8): home, legal pages, 404, SEO files.
  Still live while the Shopify move is decided. Old JotForm: https://form.jotform.com/261070496021449
- `shopify-theme/` — full Shopify theme (Liquid), same design. Rich per-product pages for the five
  treatments, intake-URL setting, LegitScript badge toggle (OFF until certified). `SETUP.md` is the
  admin setup guide. Zip at repo root: `velacore-shopify-theme.zip` (rebuild after theme edits).
- `shopify-products-import.csv` — imports the 5 products into Shopify.
- `docs/sops/` — 5 SOP docx files + REVIEW-NOTES.md (served nowhere).
- `docs/openloop-call-guide.md` (+ .docx) — questions for the OpenLoop call.
- `COMPLIANCE.md` — compliance decisions and the status of each LegitScript requirement.

## Hard rules (do not break)

- **Only five treatments are named publicly:** Tirzepatide, Semaglutide, NAD+, Glutathione,
  Sermorelin. Restricted catalog items must NOT appear anywhere in the repo or any public file.
- **Confidential material stays out of the repo:** the Asher Payment Processing Guide (DEA numbers,
  underwriting data), API keys, anything marked confidential.
- No efficacy/health claims; factual, mechanistic copy only. No coaching language.
- Don't show a "LegitScript Certified" badge until certification is actually issued.
- The $20 physician fee is paid by the patient inside Asher's intake (CPOM is ON). It is
  non-refundable. **Do NOT charge it in Shopify.** The program price is refunded within 15 days if the
  physician declines.

## Current decisions

- **Stay with Asher for now**; compare OpenLoop first. Asher confirmed in writing (Oct 2026): all 50
  states, CPOM on, API V1 (no webhooks, no checkout, no link-generation API), hosted intake links are
  reusable and not prefillable. Plan: Shopify checkout → thank-you page sends the patient to the
  matching Asher hosted link. Keep patient health data off our servers (no direct-API intake).
- **Payments:** EasyPay Direct planned (needs LegitScript first). Shopify Payments won't take Rx.
- **LegitScript:** "scrappy" route. Asher recommends Bloom Consulting Agency. Ask Asher for a partnership
  confirmation letter.

## Status as of Nov 13, 2026 (newest; read first)

Nov 24 2026, OpenLoop's written answers arrived as a PDF from Jordan Narlock, summarized in docs/openloop-proposal-notes.md, last section. The site was corrected to match, not pushed yet: refunds stop at shipping, not ordering; prepaid plans renew unless changed before the renewal date; video visits, changes and cancelling go through patient support; no extra cost for video stays only on Microdosing, NAD+ and Sermorelin; labs are not required before the first prescription; the patient pays for nausea medication; clinician hours are Monday to Friday; plans are chosen at the end of the partner's intake. Both checks at baseline. COMPLIANCE.md refund line updated. Answer 6 on 503A pharmacies contradicts itself; Dourado then said it is going to be 503A, so the site keeps 503A, and the reply asks OpenLoop to confirm it in writing for all six programs. Jordan wants to send the contract before the holiday break. Vale drafted a reply asking for the MSA, Order Form and BAA plus three follow-ups, in the private email draft file; Dourado sends it himself. Vale's advice: read the contract against the proposal before signing.

Nov 23 2026, Jordan Narlock at OpenLoop replied to the Nov 20 email: answering will take him a while, and since they want us up and running after the holiday he asked whether we have more questions, to answer them all in one document. Vale drafted the reply, not sent, Dourado sends it himself as Reply all: yes, this is everything, the Nov 20 list stands as it is, and 17 final questions are added, numbered, in four groups: billing and plans, programs and care, patient experience, LegitScript and the catalog. Taken from the private question bank, minus anything the Nov 20 email already asks or Johnny already answered. The banked programs are asked about only as a general request for the full Agile catalog, with no program named, so nothing unapproved is written down. Text in the private untracked docs/openloop-email-draft.md, section Reply to Jordan, Nov 23 2026. When answers arrive, cross off the bank and update the site where an answer changes something; the Start pages get rechecked against the real intake before the Continue buttons are switched on.

Weekly audit, Nov 23 2026

- Compliance check 0 fail, 7 review, 3 pass. Site audit with the live site 1 fail, 7 review, 19 pass; report in _audit/2026-11-23_0806/report.md. The one fail is the 9 Start page placeholder links, waiting on OpenLoop's intake URLs. Reviews are the six program intake placeholders and the consent page naming 9 of 51 states, both known. New since last week: nothing; this is the first weekly bullet, and the counts match the last ones recorded in this file. Live site, the Netlify forward, all 23 sitemap URLs, SEO tags and prices all pass.

Nov 21 2026, leading with the 12-week price: advised, built, blocked, withdrawn. Nothing on the site changed. Dourado asked whether the cards should show only the 12-week price so it looks lower, and whether that is bait and switch. Vale advised against showing it alone and for a version that leads with From and the 12-week price with the plan and the up-front charge directly under it, then built that on the home and pricing cards with an audit safeguard. vc-reviewer BLOCKED it on three grounds. One: the repo's own rule, .claude/skills/vc-ads/references/policy-checklist.md, Claims and copy: no from price that needs a prepay to be true; one fail blocks the item, and the home and pricing pages are the landing pages. Vale had not read that checklist before advising, which was the mistake. Two: nothing in writing says which plan lengths the Agile intake sells, so a 12-week headline price may not be buyable, and From is only accurate if no cheaper plan is sold; the proposal lists 24 and 52 week plans at lower prices per 4 weeks. Three: From would mean two things on one page, the hero's month to month floor and the card's prepaid price. Decision, Vale: the rule stands and the advice is withdrawn. The headline price stays the month to month price; the 12-week plan stays the second option with its up-front charge and saving, as pushed in 326f02f, which the reviewer passed. The uncommitted build was discarded; public/ and tools/ match the pushed commit, a full rebuild reproduces it, and both checks are unchanged at 0 fail and 1 fail for the 9 Start placeholders. The reviewer confirmed every figure in the discarded build was correct, so the numbers are not in question. Only Dourado can change the checklist rule, in his own words. If he ever does, the lead price must also wait for OpenLoop to confirm in writing what the intake sells. Saved in Vale's memory as lead-price-no-prepay: read the policy checklist before any advice on how a price is shown.

Nov 20 2026, twenty-second push, on Dourado's "Push": the plan step and the 12-week saving, 326f02f, with the handoff note 96df3e3. Live within seconds. Checked live: the eight Start pages with a picker each carry two plan rows, the right saving with compared with month to month, the reviewer's handoff wording, none of the blocked sentence, and the FDA disclaimer; Semaglutide oral has no picker. Home shows Choose your plan on all six program cards and six saving lines; pricing shows it on nine cards, with Start visit left only on Semaglutide oral. At 320, 375 and 1280 px, home, pricing, all nine Start pages and the six program pages have no sideways scroll, no script errors, and every plan row is at least 44 px. On each of the six program pages, picking the 12-week plan put the saving in the price note and plan=12week on the Start link, and clicking through landed on the Start page with the 12-week row selected. From the home Tirzepatide card the button opens the Start page on Choose your plan with month to month selected. Full live audit: 1 fail, the 9 Start placeholders, 19 pass. Worth knowing for the next live check: Netlify rewrites the served page with single quotes and clean links, so a pattern written for the files in public/ can miss on live source; count the words or use the rendered page. Not checked: a real phone, Safari, and anything about the partner's intake, which is still to come.

Nov 20 2026, the plan step and the 12-week saving, vc-reviewer PASS after one block, not pushed yet. Dourado saw on the home Tirzepatide card that a patient had nowhere to pick month to month or the 12-week plan; Start visit led to a page showing only the month to month price. Vale's decision under decide-and-advise: the choice gets its own step, not a selector on every card. One: the Start page opens with Choose your plan, two rows read from the plan data, on eight Start pages, the six programs plus NAD+ nasal and NAD+ oral dropper; Semaglutide oral has one plan and no picker. Two: the program cards on the home and pricing pages say Choose your plan on the button; only the Semaglutide oral card and the needle-free chooser card for it keep Start visit. Three: a plan picked on the program page rides to the Start page as ?plan=12week and arrives selected; it is never passed to the intake link. Four, Dourado: show what the 12-week plan saves. Dollars, not a percentage, because the dollar figure is the larger number on every program and is exact: $30 on Tirzepatide, Semaglutide injection and Microdosing GLP-1, $48 on Glutathione, $150 on NAD+ and Sermorelin, worked out by saving() in tools/build_programs.py as three month to month charges less the up-front charge. Cards say Save $30 over 12 weeks; the Start row and the program page note add compared with month to month. The reviewer blocked the first handoff line, Your plan is set on that page, because it can read as already set. Now, its accepted wording: Your choice on this page is not sent to them. You choose your plan again on their page, and the plan you choose there is the one you are charged for. The 12-week row also carries the refund policy's term, If you cancel, shipments not yet ordered are refunded. Checked: all nine Start pages at 320, 375 and 1280 px for overflow, 44 px rows, spilled text and script errors; the carry from each program page, with UTM tags kept; all 33 pages fit; compliance 0 fail; site audit 1 fail for the 9 Start placeholders, whose card parser now accepts the new button text. Open, in the private question bank as 27 and 28: which plans the partner's intake shows, under what names and with what default, and how a prepaid refund is worked out. Recheck every Start page against the real intake the day the links arrive, before the Continue buttons are switched on. Also open: a 12-week pick on the NAD+ page is not carried into a form tile, cosmetic; and start_plans must change before a Start page is built for the hidden programs, noted in docs/launch-sexual-health-hrt.md. Dourado's Caroline line in the same message was a television show overheard by voice typing; disregarded on his word.

Nov 20 2026, twenty-first push, on Dourado's "Push": the one site, one address batch, f560e1b to aadeda5, five commits: corrected notes, vercel.json removed, the netlify.app forward. First push with Netlify as the only publisher; it built and went live in under a minute. Checked live with no redirect following: velacore-health.netlify.app answers 301 to the same path on www.velacorehealth.com for home, pricing, a program page, a Start page, an article, the FAQ, the share picture and a page that does not exist; the http form goes to https first, then to www. On www, twelve addresses answer 200 from Netlify with no forward, among them home, pricing, two program pages, a Start page, the sitemap and robots.txt, and an unknown page answers 404. velacorehealth.com and velacore.health still forward to www. velacore.vercel.app answers 404. The security headers are unchanged. Full live audit: 1 fail, the 9 Start placeholders, 19 pass. The audit's foundation line still passes because it follows the forward to www; it now proves the forward lands on the site and nothing more. Not checked: a real phone, and how long search engines take to drop the old netlify.app copies, which is theirs to decide. Left open, Dourado's call, no rush: the empty Vercel account and the Vercel app on the GitHub side if still installed.

Nov 20 2026, how Vale works from here, Dourado: "I need you to suggest the best decision and advise me rather than ask me what to do. I'm relying on you to execute at a high level that is far superior to my current experience of SEO and marketing and how the search engines optimize as well as content and structures." So on search, marketing, content and structure Vale decides, builds and explains, and stops for his word only at the gates in CLAUDE.md: a push, spending, sending, signing, his own accounts, new treatments or claims, anything that cannot be undone. Saved in Vale's memory as decide-and-advise. First decision under it, not pushed: velacore-health.netlify.app now forwards to www.velacorehealth.com page for page, two rules in netlify.toml, https and http, placed with the velacore.health forwards. Reason: one site at one address, so links, shares and search credit never split across two copies; the canonical tags were already a hint, a permanent forward is the firm version. The rule matches only visits that ask for the netlify.app name, so the real domain, which points at that name in DNS, is not caught and cannot loop. Deploy previews use other names and are untouched. netlify.toml parses, ten forwards, one header block. Both checks unchanged. Untested until pushed: that the netlify.app address really forwards, page for page, and that www still answers 200. Check both right after the next push.

Nov 20 2026, the old Vercel project is deleted, by Dourado on his own screen, walked through one step at a time. Netlify is now the only publisher. Order: he opened the Vercel dashboard, team Velacore Health Site, one project named velacore; its Domains screen listed only velacore.vercel.app, so our domain was never attached; he asked whether the copy was the real site, so he paused it first; with it paused Vale read seven real addresses, all 200 from Netlify with prices showing, and velacore.vercel.app answered 503; then he deleted the project. Checked after the delete: www.velacorehealth.com home, pricing, a program page and the FAQ, plus velacorehealth.com and velacore.health, all answer 200 from Netlify; velacore.vercel.app answers 404, deployment not found; the live security headers are the same five as before. In the repo, not pushed: vercel.json removed, the netlify.toml opening comment reworded, CLAUDE.md, README.md, docs/DEPLOY.md and the site audit's notes updated. netlify.toml parses and only its comment changed. Both checks unchanged: compliance 0 fail, site audit 1 fail for the 9 Start placeholders. Not checked: the site from Dourado's phone on the real address, and whether Netlify rebuilds cleanly from this commit, which shows on the next push. Left open, his call: the empty Vercel account and the Vercel app on the GitHub side if still installed; and velacore-health.netlify.app, which still shows the site with no forward to www.

Nov 20 2026, stale project notes corrected, on Dourado's "Yeah correct whatever you need to correct without breaking anything". Docs only, nothing in public/ or tools/ changed, both checks unchanged at 0 fail and 1 fail for the 9 Start placeholders. CLAUDE.md: the repo map says Netlify at www.velacorehealth.com, nine Start pages, the drafts folder, the share picture builder, and to always name the image when running prepare_images; the peptide walk-through sentence is gone because public/learn.html has no such block; the Build section lists the five builders in order and the settled price rule; the Audit line mentions the fixed prices and that every live program must be on every surface. docs/DEPLOY.md: Where it lives, What it costs, How to verify, How to undo and Open decisions now describe Netlify as the live host; the older plan sections are kept and marked as the record. README.md: rewritten short, pointing at CLAUDE.md, HANDOFF, COMPLIANCE, DEPLOY and BRAND; the old one-page draft description is in git history. Found while checking and not acted on, both Dourado's call: one, the old Vercel project still publishes a second copy at velacore.vercel.app on every push, which breaks the one publisher rule in CLAUDE.md; closing it is his click in the Vercel dashboard, then vercel.json can come out. Two, velacore-health.netlify.app serves a third copy with no forward to www; the 23 search pages carry a www canonical tag, and a forward is one rule in netlify.toml on his word. Not corrected: the plan sections lower in DEPLOY.md and the older status blocks in this file still read as written at the time.

Nov 20 2026, CLAUDE.md, on Dourado's "Yes update it": the hard rule line no longer calls Glutathione's form and price placeholders; it records the Nov 12 proposal price and OpenLoop's Nov 20 written confirmation of injection in all 50 states. Not changed and still stale in CLAUDE.md, for Dourado's word: the repo map says public/ is served by Vercel at velacore.vercel.app, while the live site is Netlify at www.velacorehealth.com.

Nov 20 2026, twentieth push, on Dourado's "Yes push": the full fact audit fixes, f560e1b, vc-reviewer PASS. After the PASS Vale took three of its notes: the form Start pages say "You may be asked for that choice again inside the secure intake", the handoff line says "You choose your plan there, and you may be asked again for other choices you made here", and the clinicians tile says hours are not on holidays. Checked live: 27 pages and script.js read from source with none of the 14 old phrases left; no sideways scroll or script errors on those pages at 320, 375 and 1280 px; the phone bar follows every plan on NAD+, Semaglutide and Glutathione; Glutathione's page says Injection; the refund policy is dated Nov 20 and says billing period. Full live audit: 1 fail, the 9 Start placeholders, 19 pass. Still open: questions 12 to 26 in the bank for OpenLoop, Dourado's decisions listed in the entry below, the attorney's read of the legal pages, and the hidden sexual health draft, whose phone bar shows the same text for all three plans and must be fixed before it launches.

Nov 20 2026, full fact audit and fixes, on Dourado's "Yes do a full thorough audit and update everything on the site", not pushed yet, final vc-reviewer pass pending when this was written. vc-reviewer audited all 33 pages, the captions and script.js against docs/openloop-proposal-notes.md and returned 29 findings. Fixed now, each backed by the notes or by removing an unsourced line: the illustrative-prices sentence is gone everywhere, PRICE_PENDING removed; Glutathione is an injection on its page, menus, home card, chooser notes and COMPLIANCE.md; the phone price bar follows the selected plan through data-bar on every plan, plan_bar in tools/build_programs.py; Start pages say the program, form and plan are chosen again inside the partner's intake, since the link cannot carry a choice; refund wording says billing period, not month, on every page; plan lengths read prepaid plans of 12 weeks or longer; questions that promised pausing or switching plans now ask about cancelling only; the clinician sets the starting level, not always the lowest; clinician hours add no holidays; Tirzepatide is listed here as an injection; home step 4 says check-ins on your program's schedule; two unsourced Learn lines removed, support walking you through a first dose and strict quality standards; telehealth services partner is the one name used; the four legal page footers carry the compounded line; refund policy, terms and consent dated Nov 20; Glutathione added to keywords; the 503A article links to How it works; a button that ran past the edge at 320 px on the Microdosing article now wraps. Waiting on OpenLoop, banked as questions 12 to 25 in the private email draft: 503A for our pharmacies, shipping included, the refund cut-off, video visit cost on three programs, Glutathione's journey, eligibility ages, the nausea medication, clinician days, what the portal does, supplies, intake length, payment and insurance lines, plus the oral Microdosing and oral Semaglutide questions already banked. Dourado decides: the CLAUDE.md line that still calls Glutathione's form and price placeholders; analytics on the pages where it is switched off, now that OpenLoop OK'd tags on public pages; whether the privacy policy should mention the partner dashboard; the Weight, entry tier label on Microdosing; that only the Start pages say visits open soon. Legal pages still need the attorney: consent and terms assume what the partner's intake shows.

Nov 20 2026, nineteenth push, on Dourado's "Push": the labs wording, f03ed9a. Checked live at 375 and 1280 px on ten pages, home, FAQ, pricing, how it works, clinicians, three program pages and two articles: no sideways scroll, no script errors, none of the old always-ordered wording, and every no-cost or included labs line says baseline. The new first-prescription line is on the Semaglutide and Tirzepatide pages, the GLP-1 article, and in the page source of the FAQ and How it works answers. Full live audit: 1 fail, the 9 Start placeholders, 19 pass. Still open with OpenLoop: question 11 in the bank, whether baseline labs are a standard order and whether they are paid on Agile.

Nov 20 2026, labs wording, vc-reviewer PASS after one block, not pushed yet. Dourado: the site made people assume labs are a step everyone must do; in practice labs are needed only when the clinician asks based on the intake. Every labs line now says two things. One: in most cases you do not need labs before your first prescription, and the clinician asks for them first only if your intake calls for it. Two, Semaglutide and Tirzepatide only: when the clinician orders baseline labs, they are done at a national laboratory at no cost to you. The reviewer blocked a first version that dropped the word baseline, which widened the no-cost promise past the proposal's base weight-loss labs; baseline is back on every cost line. Sources changed: tools/build_programs.py, tools/pages.py, tools/articles.py, and by hand public/index.html and public/faq.html with its structured data. Two articles carry today's date with their Nov 13 published date kept. Open, and Dourado has been told: the proposal's written patient journey orders labs with the first prescription and reads them at day 30, so on paper labs are a normal step. The new wording is true under either reading. Question 11 in the bank asks OpenLoop; if baseline labs are a standard order, one sentence saying so goes back on the two program pages, and if they are not included on Agile, every no-cost line and the consent page line come down.

Nov 20 2026, eighteenth push, on Dourado's "Looks fine push it": the education video with the studio end card, 42d460f. Checked live: the file on www.velacorehealth.com is byte for byte the one vc-reviewer passed, 4,014,024 bytes; on the Learn page at phone width it plays from the start, 50.1 seconds, with its captions track and poster, no errors and no sideways scroll. Full live audit: 1 fail, the 9 Start placeholders, 19 pass. Not checked: a real phone, Safari, and the sound by ear.

Nov 20 2026, seventeenth push, on Dourado's "Yes push it": the new share picture, ded563c. Checked live: www.velacorehealth.com/images/og.jpg returns 200 as a JPEG, the old og.png returns 404, and home, pricing, a program page, an article and the information standards page carry the new tag and no old one. How each app crops and caches it is not checked. Same message, Dourado asked for the education video's end card to use the new pictures. Done, vc-reviewer PASS, not pushed yet: one CSS rule in tools/video/peptides/overlay.html recrops the box for the studio six-vial photo, the cut was rebuilt with python -I tools/video/peptides/build_cut.py vo5 end, and the web copy made with ffmpeg -i rough-cut.mp4 -c:v libx264 -pix_fmt yuv420p -crf 26 -preset slow -profile:v high -r 30 -c:a aac -b:a 112k -ar 48000 -movflags +faststart, then copied to public/media/peptides-explained.mp4, 4.0 MB, 50.1 seconds. Nothing else in the video changed: the captions file is identical, the reviewer found the audio stream byte identical, and the first 41 seconds match the old file. The marble versions are kept in 03-edits/peptides-video as rough-cut-marble-end-backup.mp4 and end-scene-marble-backup.mp4. Reviewer notes, not blocking: the Microdosing GLP-1 name is the hardest to read at that size; the end card small print is now the only place the AI illustration line appears for the video, so keep it in every rebuild; the comment in build_cut.py lines 116 to 118 about a line beside the player is out of date.

Nov 20 2026, new share picture, on Dourado's "Yes", vc-reviewer PASS after one block, not pushed yet. public/images/og.jpg replaces the dark Nov 6 og.png, which is deleted; this closes item nine of Things to add. Built by python -I tools/make_og.py: the six-vial studio group photo, the header lockup, the home headline and the top bar line read from public/index.html, the web address, and the illustration note along the bottom, read from PRODUCT_NOTE. The reviewer blocked plain jade on the word Health, now jade ink, and the missing illustration note, now on the frame; BRAND.md section 6 says share pictures carry it. Every share tag points to og.jpg, and the two hidden draft pages were rebuilt, which also brought them up to the current template and prices. Not checked: how each app crops and caches the picture; that needs a look after the push. Dourado asked on Nov 20 which pictures he must make: none today; later ones wait on OpenLoop's answers about the oral forms and the sexual health products.

Nov 20 2026, Things to add, kept so none is forgotten. Dourado: "Bank all of them and don't forget about these things we need to add." One: Sexual health and women's HRT, approved Nov 18, built and hidden, waiting on OpenLoop's written product list; launch by docs/launch-sexual-health-hrt.md. Two: the banked programs, the ones the other Agile site sells and we do not. All banked, none approved. Their names stay out of this repo per CLAUDE.md; they are in Vale's project memory, product-bank-not-approved, with a recommendation for each, and question 10 of the bank in the private email draft covers asking OpenLoop. Three: oral tirzepatide, offered per OpenLoop, no price yet. Four: the optional name and email box before the intake, docs/start-lead-form-plan.md. Five: the real intake links, ideally one per program. Six: a patient support phone number and the partner's support contacts on the Contact page. Seven: Glutathione's form line, injection is confirmed in writing; and CLAUDE.md still calls its form and price placeholders. Eight: small fixes found by the reviewer: refund wording says a month where billing period is exact, the refund policy names 52 week plans for every program, the phone bar shows the month to month price while the 12-week plan is selected. Nine: og.png is still in the old picture style. Each of one to three needs OpenLoop in writing; two also needs Dourado's yes per program.

Nov 20 2026, sixteenth push, on Dourado's "Push": batch 1 from the Bold You study, 91bd424, plus the docs commits up to fb89b95. Checked live at 375 and 1280 px on home, pricing, two program pages, a Start page, the new information standards page, the microdosing article and the FAQ: no sideways scroll, no script errors, no a month or /mo price label left, the footer link present wherever there is a footer link column. The pricing year table shows all seven rows with the right totals, the home weight band reads From $179 every 4 weeks, and the chooser's oral card reads $259 every 4 weeks, oral form. Full live audit: 1 fail, the 9 Start placeholders, 19 pass.

Nov 20 2026, question bank. Dourado could not find boldyouwellness.com in LegitScript's public lookup and hit the daily limit, so its certification is unconfirmed. His call: wait for OpenLoop's reply, and keep the open questions banked to possibly ask. The bank is the last section of the private untracked docs/openloop-email-draft.md, nine questions from the Bold You study: the LegitScript name, billing every 4 weeks, one intake link per program, plan lengths, microdosing forms, pausing, timing, the lead form, cold shipping. When OpenLoop answers the Nov 20 reply, cross off what they covered before sending anything. Batch 1, commit 91bd424, is still not pushed; Dourado has not answered the push question.

Nov 20 2026, lead form before the intake, drafts only, nothing built or public. Dourado tested the other Agile partner site's Start form and asked whether we should do the same; on his "maybe draft it now" Vale wrote docs/start-lead-form-plan.md and vc-copy wrote docs/legal-drafts/10-lead-form-copy.md. The plan: an optional box on the Start pages, first name and email only, no program stored, no state, no phone, never a gate, never fed to ad tools, one follow-up email that names no program. It waits on OpenLoop's written answer to the name and email question in the Nov 20 reply, the attorney's read of the questions in the plan, Dourado's choice of where the list lives, and the real intake links. vc-reviewer has not seen it; it goes to review when it is built.

Nov 20 2026, batch 1 from the Bold You study, docs/boldyou-study-nov20.md, on Dourado's "Yes build batch", vc-reviewer PASS after one block, not pushed yet. One: billing period. The partner's prices are per 4 weeks, so a month to month plan is charged 13 times a year. Every price label now says every 4 weeks, /4 wks or per 4 weeks, from PERIOD, PERIOD_NB and CHARGES_PER_YEAR in tools/build_programs.py, and the pricing page has a table, What a full year costs, built by year_table in tools/build_pages.py. The sitewide label change was Vale's call to keep the site consistent with the table Dourado approved; the reviewer agreed. Basis is the proposal notes; OpenLoop has not answered the billing question directly. Two: plan lengths. The pricing page says a 24-week plan is also offered and a 52-week plan on some programs, since the Nov 12 proposal gives Glutathione no 52-week plan. Three: a new page, public/information-standards.html, How we check our information, copy by vc-copy in docs/information-standards-draft.md, entered in tools/pages.py, linked as Information standards in every footer link column and in the sitemap. The reviewer blocked two sentences that were not true, the sourcing line and the article date line; both were reworded, and the microdosing article's date is now Nov 20 with its published date kept at Nov 13. Also: the home Semaglutide oral tile line now comes from the program data, and under 360 px the plan picker puts the price under the plan name. Open for Dourado: the page's promise to update when a fact changes; whether to say plainly that program and legal pages have had no clinician or attorney review; whether Glutathione's form line changes to injection; the refund wording still says a month where billing period would be exact, for vc-copy and the attorney; the phone bar shows the month to month price while the 12-week plan is selected. Bold You's LegitScript status could not be checked, the lookup needs a human check.

Nov 20 2026, Dourado sent the reply to Johnny Nguyen, Reply all with Jordan Narlock and Jonathan copied. Text in the private untracked docs/openloop-email-draft.md. It asks for the Order Form and BAA with the MSA, OpenLoop's patient documents, how a patient picks a program inside the one intake link, multiple programs in one intake, billing, shipping, oral tirzepatide's price, whether oral semaglutide is $259, photos of the oral forms, eligibility, the video-visit states, whether baseline labs are still included as the Nov 2 proposal says, privacy and support contacts, a clinician reviewer for articles, and the sexual health and HRT product list. Left out on purpose, as Johnny had answered or was still looking into them: coaching wording, the approval process, the dashboard and BAA coverage, promo pricing and prepaid refunds. Waiting on: Jordan's MSA and Johnny's answers.

Nov 20 2026, fifteenth push, on Dourado's "Yes push it": OpenLoop's fixed prices, cc299ee, plus the docs commits ac84df7 and f7f24e3. Checked live after the push: home, pricing, all six program pages, a Start page and the FAQ show only the new prices, with no first month price or price slash; the home weight band reads From $179 a month. Full live audit: 1 fail, the 9 Start placeholders, 19 pass, and the price table matches OpenLoop's prices for all six programs.

Nov 20 2026, prices now match OpenLoop, vc-reviewer PASS after one block, not pushed yet. On Dourado's "Yes change prices", after OpenLoop wrote that Agile prices are fixed: Tirzepatide $249, 12-week $239/mo $717; Semaglutide injection $209, 12-week $199/mo $597, oral $259; Microdosing GLP-1 $179, 12-week $169/mo $507; NAD+ $229, 12-week $179/mo $537; Glutathione $145, 12-week $129/mo $387; Sermorelin $229, 12-week $179/mo $537. No first month price and no price slash anywhere. Every surface reads from the program data, now including the home card 12-week lines and the home weight band line, From $179 a month, the lowest weight program price; the reviewer blocked a first version that showed $145, the Glutathione price, in the weight band. The site audit now FAILs any price that differs from planned_prices in audit-config.json, which hold OpenLoop's prices. COMPLIANCE.md and docs/pricing-research.md updated. Open, asked in the reply to OpenLoop: Shipping included has no written source; Semaglutide oral $259 is from the Nov 2 proposal; Glutathione plans and the site's 24 and 52 week line; the site still says Glutathione's form is set by the clinician although OpenLoop confirmed injection. CLAUDE.md still calls Glutathione's form and price placeholders; Dourado to decide whether to update that line. The reply to Johnny is drafted in the private untracked docs/openloop-email-draft.md, not sent.

Nov 20 2026, OpenLoop answered our first question email in writing, Johnny Nguyen 4:18 PM. Summary in docs/openloop-proposal-notes.md, Written answers. Biggest change: Agile prices are fixed and partners cannot change them, so the site's own prices and first month prices must give way to OpenLoop's. Not changed on the site yet; waiting on Dourado. Site prices that differ from the Nov 12 proposal: Tirzepatide, Semaglutide injection month to month, Microdosing 12 week, NAD+, Glutathione and Sermorelin, plus every first month price. Semaglutide oral at $259 already matches. Also settled: Glutathione is an injection in all 50 states; Meta and Google tags are allowed on our public pages but never on the intake or portal; one intake link for everything, on Agile's own address, about 3 days after signing; billing and patient support are OpenLoop's. Example LegitScript site to study: boldyouwellness.com. The follow-up email draft, private and untracked, now opens with what the reply left open.

Nov 20 2026, eleventh push, chooser fix, vc-reviewer PASS, pushed on Dourado's "Yes push": he picked Vitality then no needles and got the NAD+ injection vial and Glutathione with a Start button. Now the needle-free Vitality answer shows only NAD+, with the nasal spray photo and the line "NAD+ as a nasal spray or an oral dropper", and the note says Glutathione is not listed because a form without a needle is not confirmed yet. Update that note when OpenLoop confirms Glutathione's forms. Reviewer notes: the card line swap in public/script.js matches the exact NAD+ wording and the tiles/ image path, so re-test the chooser if either changes; on the injections path Glutathione still shows Start visit with the form set by the clinician, as decided Nov 13.

Nov 20 2026, twelfth push, chooser photo fix, vc-reviewer PASS, pushed on Dourado's "Push": Weight then no needles showed Microdosing GLP-1 as an injection vial. Now every needle-free answer shows each program's needle-free photo, taken from its Tired of needles tile, so Microdosing shows its dropper and NAD+ its nasal spray. Live check: all six chooser paths show the right photo with no page errors, and the live audit is 1 fail, the 9 Start placeholders, 8 review, 18 pass. Re-test the chooser if the Tired of needles tiles or their image names change.

Nov 20 2026, last marble picture replaced, vc-reviewer PASS, not pushed yet: the Learn card How is it taken now shows the four forms, Semaglutide vial and tablet bottle, NAD+ dropper and nasal spray, in the studio look. Made in Gemini from the four approved studio shots; the first try had 505A on two labels and a broken HEALTH on two, rejected; the second try, with HEALTH spelled out and the 3 named as never a 5, passed every label. Files: assets-in/products/learn-forms.jpg, the Gemini original assets-in/products/studio/_learn-forms-gemini.jpg, the rejected try _learn-forms-try1-rejected.jpg, the marble version _marble-learn-forms.jpg. tools/make_learn_cards.py focus for taken is now 0.48. docs/BRAND.md section 5 now describes the studio look instead of marble, on the reviewer's note. learn-forms.jpg and _learn-forms-gemini.jpg were uploaded to the Drive backup folder products studio the same day. Dourado, Nov 20: always add new pictures to the Drive backup, no need to ask each time.

Nov 20 2026, home cards, no cut vials, vc-reviewer PASS, not pushed yet: Dourado: no cut images, get close without hurting the design, and the trio a little bigger, on phones and desktop. Up to 1299 px both big home cards now show the 4 by 3 wide studio cuts at every width, with the photo box never wider than 4 by 3, so only plain side margin is trimmed; the phone fade on the photo's left edge is 30 percent so it no longer dims the label. sermorelin-480 was dropped before any push, and tirzepatide-480 is kept but unused. The trio has a closer cut, images/products/goal-weight-hub-800 and -1200, made by prepare_images.py --home; it shows on the weight card from 1300 px, in the weight section photo up to 700 px and on the Weight goal card up to 420 px. On phones up to 420 px every goal card photo fills its 16 by 10 box and is placed so each vial shows whole, so those tiles are about 33 px shorter than before. Reviewer checked 34 widths from 320 to 1920 with every vial whole. Notes, not blocking: at 320 px the weight card is tight; at 860 px the Hormone goal card vial base sits 2 px from the bottom, unchanged.

Nov 20 2026, thirteenth push, on Dourado's "Go ahead and push if you don't see any problems" after vc-reviewer PASS: program card labels no longer sit on the vial. The home program row uses square cuts, images/products/sq/<program>-800 and -1200, made by prepare_images.py --home: the studio shot gets plain margin by repeating its edge pixels, 204 px each side and 95 px above, then is cut 2200 square so the cap sits at 21 percent, below the label. The chooser swaps cloned cards back to the full portrait photo, since its boxes are 4 by 5. All other 4 by 5 program card photos, on pricing, the chooser and program pages, show the photo's top with no zoom, so the cap clears the label. Checked: zero label overlaps and zero cut vials at 360 to 1440 px, by Vale's pixel check and the reviewer's own geometry check. The reviewer's mirror fold note was fixed by switching from mirrored margins to repeated edge pixels, and the step now runs on ffmpeg so python -I works.

Nov 20 2026, Dourado: when the hidden programs launch, every section that lists programs must carry them. docs/launch-sexual-health-hrt.md now lists every surface, with the photo steps for the studio shots. The site audit has a new section, 2b, that fails if any live program, the six plus any slug in LIVE, is missing from its program page, Start page, pricing card, home program row, chooser, Treatments menu, sitemap, footer, product photo, menu thumbnail or square home-row photo; tested by pretending Women's HRT was live, which listed all eleven gaps.

Nov 20 2026, vc-reviewer PASS, not pushed yet: the pricing page carries a Needle-free forms section, four cards built by form_cards in tools/build_pages.py, Semaglutide oral, NAD+ nasal spray, NAD+ oral dropper and Microdosing GLP-1 oral, every price from the program data. The Weight goal card uses the closer trio cut, goal-weight-hub, at every width except 421 to 580 px, where a tighter square, GOAL_SQUARE goal-weight 472, 185, 1480, is served; a first try at 587, 300, 1250 clipped the Microdosing vial from 421 to 428 px and was blocked by the reviewer. Reviewer notes, not blocking: on the pricing NAD+ cards the nozzle and dropper bulb sit beside the category label, not under it, nothing overlaps.

Nov 20 2026, fourteenth push, on Dourado's "Push": the pricing Needle-free forms cards, the closer trio on the Weight goal card, the launch steps for every surface and audit section 2b. Checked live after the push: the pricing page shows all four form cards at 800 and 1280 px, the Weight goal card fills its tile like Vitality and Hormone, both big home cards show the whole vial from 600 to 1440 px, and all six chooser paths show the right photos and Start links. The label overlap check flagged only the NAD+ oral dropper card at 1280 and 1440, the known false alarm from the bulb's faint shadow; a close-up shows about 27 px of clear space. Full live audit: 1 fail, the 9 Start placeholders waiting on OpenLoop's intake links, and section 2b passes with 6 programs on 11 surfaces.

Nov 20 2026, tenth push, goal cards on phones, vc-reviewer PASS after one block, pushed on Dourado's "Yes push": between 421 and 860 px the home goal tiles are two columns and the photo used to float small in its column. Now it fills the column: square cuts centered on the products from 421 to 580, made by prepare_images.py --goals GOAL_SQUARE, and the 4 by 3 photo covering the column from 581 to 860; the Sermorelin tile sits at 35 percent so its cap clears the top. The block was the picture tag set to display contents, which pushed the photo off-center from 581 to 605; fixed. Tightest margins, at 860 px: Vitality caps about 9 px, Sermorelin base about 5 px; re-check 860 if a crop moves.

Nov 20 2026, decision: no agreement checkbox on the Start pages. Dourado compared a competitor on Agile that gates its Continue button behind an I agree checkbox, and decided against it because the site keeps no record of who ticked it. The consent record belongs in the partner's intake; two questions were added to the private OpenLoop follow-up draft: whether their intake shows and records Velacore's terms, refund and privacy policies, and how they want Agile and OpenLoop named before the intake.

Nov 20 2026, image backup: on Dourado's "Send everything to the Google drive", all 82 source pictures in assets-in were uploaded to the Velacore business Drive, firstventuregroupllc@gmail.com, My Drive, folder "Website image sources Nov 20 2026": the 66 product and lifestyle originals, marble versions and rejected tries at the top level, and the 16 studio shots, group shots and hidden Sexual Health and Women's HRT shots in the subfolder "products studio". Verified by name list and file sizes. Re-upload new studio shots there after each Gemini session. assets-in stays gitignored.

Nov 20 2026, ninth push, the whole site on the studio look, vc-reviewer PASS, pushed on Dourado's "Just push everything else we have after vc approvals": main product photos, menu label close-ups, form tiles, the home Tirzepatide card cuts, the six-vial square with a one-letter hand patch on the Sermorelin HEALTH, new Gemini goal-weight and goal-vitality, goal-hormone widened from the Sermorelin shot, and the Learn pictures learn-sema-tirz and learn-microdosing with their cards. tools/prepare_images.py gained STUDIO_PRODUCTS and the --tiles, --home and --goals modes; tools/make_thumbs.py gained STUDIO_BOXES; both warn when a studio shot is missing. Marble originals kept as _marble- files in assets-in. Still on marble: the Learn card taken, waiting for Gemini's daily limit to reset. Reviewer notes for Dourado, not blocking: the home weight goal card's three vials read small at card size; public/images/og.png, the share picture, is the old dark design with middle dots in its tagline. assets-in/products/studio needs a backup outside the repo.

Nov 20 2026, form tiles on studio shots, local, vc-reviewer PASS: Dourado caught that the Tired of needles tiles still showed marble after the eighth push; Vale had wired the studio shots into the price box only and missed the tiles. New studio shots, label-checked: nad-nasal, nad-oral, microdosing-oral. tools/prepare_images.py --tiles remakes only the six form tiles, preferring assets-in/products/studio/<name>.jpg and warning when it falls back to marble; TILE_CROP_FOR gives three shots their own cut. Still on marble, waiting for Dourado's call on the whole site: the main product photo on each program page and home, and the menu label close-ups from tools/make_thumbs.py. Not pushed.

Nov 20 2026, eighth push: on Dourado's "Push", 408ada7 to b86aa38 went live: the logo fix, one image note per page, tablet layout fixes, illustration alts, the menu image note and all seven studio price box photos. Verified live: the tirzepatide, nad and semaglutide-oral price box files match the local files byte for byte; the home page carries the menu note; the NAD+ page alts start Illustration; the full audit shows 1 fail, the 9 Start placeholders, and 18 pass; a live phone render of Sermorelin shows the studio photo in the price box with no script errors. The hidden Sexual Health and Women's HRT shots are not in public and were not pushed. This note itself is local, not pushed.

Nov 20 2026, all seven studio price box photos done, local, vc-reviewer PASS: Microdosing GLP-1, NAD+, Glutathione, Sermorelin and Semaglutide oral join Tirzepatide and Semaglutide, every label checked enlarged with a flat-topped 5 in 503A. Sources live only in assets-in/products/studio/, gitignored; if that folder is lost, make_thumbs.py falls back to the marble photos, so it needs a backup outside the repo. NAD+ is now serif in the price box only; the menu thumbs and main NAD+ image still use the older plain-font label, Dourado's call. Hidden studio shots done the same day, label-checked, off the site: assets-in/products/studio/_hold-sexual-health.jpg, a vial in helix blue, and _hold-womens-hrt.jpg, a bottle in plum, both with only FOR PRESCRIPTION USE ONLY since OpenLoop has not said whether those items are compounded; the pages stay unbuilt until OpenLoop's written product list. Not pushed: 40ad240, bf58edb, 1aa00bd and this commit wait for Dourado's push OK.

Nov 19 2026, menu note and studio shots batch, local, vc-reviewer PASS: product image alts start "Illustration:"; the illustration note also sits in the side panel foot and the desktop mega menu; tools/make_thumbs.py builds the price box picture from assets-in/products/studio/<name>.jpg when it exists, a 90 percent cut that keeps the shadow, else from the marble photo. Studio shots done and label-checked: Tirzepatide, Semaglutide. Next: Microdosing, sent to Dourado with its photo; then NAD+, Glutathione, Sermorelin, Semaglutide oral. Until all seven are in, five price boxes still show the marble riser. Reviewer notes, Dourado's call, not blocking: the note says the medication "may look different", while dispensed vials never carry Velacore branding, so a firmer line such as one saying it comes with the pharmacy's own label would serve LegitScript better; that goes through vc-copy. Not pushed: 40ad240, bf58edb and this commit wait for Dourado's push OK.

Nov 19 2026, layout batch ready, local, vc-reviewer PASS after one block: the logo links home everywhere and on the home page glides to the top with no #top, since #top pointed at the sticky header; one image note per page, worded "on this page", on the first phone screen above the first pictures; the program hero photo, collapsed to a 2 px dot on phones since 7210e0b, is restored; tablets 701 to 1000 px stack the hero cards; the weight band price line is centered; headings use text-wrap balance; the price box shows a full-product portrait, thumbs/<slug>-full.webp from tools/make_thumbs.py. Next batch: the illustration note in the shared menu panel and mega menu, alt text starting "Illustration of". In progress with Dourado: seven Gemini studio shots with no marble and a soft shadow for the price box, prompt in docs/gemini-queue.md, one at a time; each comes back through vc-reviewer. Dourado's tablet screenshot of the misalignment never arrived; asked him to resend.

Nov 19 2026, seventh push: on Dourado's "Push it", bff8173 to 408ada7 went live, the privacy batch and the BAA removal. Verified live: privacy, faq, refund-policy, programs/nad and the GLP-1 Learn article carry no "HIPAA-compliant", no Business Associate wording and no online questionnaire; the full audit shows 1 fail, the 9 Start placeholders, and 18 pass, with SEO complete on 32 pages and all 22 sitemap URLs answering 200 directly; pages load with no script errors under the security headers. Recommended next, in order, given to Dourado: send the first OpenLoop email; ask OpenLoop for a billing-only Agile dashboard without patient program or medication, so the no-patient-data statement stays true; send docs/legal-drafts to the attorney. This note itself is local, not pushed.

Nov 19 2026, privacy batch ready, local, vc-reviewer PASS after two blocks: Dourado confirmed Velacore collects and stores no patient or health information; once a visitor goes to Agile, Velacore has nothing to do with it. privacy.html now says so: the website has no forms, accounts or checkout, collects only visit data and emails, passes a request to the partner only when asked, discloses the utm tags that travel to the intake and that Google Analytics records them, and explains GA cookies and Google Fonts. The unsourced "HIPAA-compliant" is now "secure" on the FAQ, program trust bar and GLP-1 Learn article. The refund page no longer promises to confirm when a refund is processed. Drafts in docs/legal-drafts updated to match. Launch gates, before the first patient: the Agile dashboard shows Velacore patient names with program and last medication, so either decline that access in writing or disclose it after counsel decides; "which you see when you start a visit" needs the real intake; the safeguards wording and the whole page still need the attorney. Waiting for Dourado's push OK with bff8173 and 399c265.

Nov 19 2026, sixth push done and one change waiting: on Dourado's "Push and take out", 43aaa76 to c3caf03 went live, the SEO and security batch and the chooser fix. Verified live: the new CSP and Permissions-Policy headers are served; nine pages load with fonts, no policy messages and no script errors, and analytics still fires on the pages that carry it; the chooser no-needles NAD+ card says Choose your form; the audit's SEO section passes with all 22 sitemap URLs answering 200 directly. Then, on his OK, the sentence claiming Business Associate Agreements was removed from privacy.html and Last updated set to November 19 2026; vc-reviewer PASS; local, waiting for his push OK. Still open on privacy.html, older, for the attorney's rewrite in docs/legal-drafts/04-privacy-policy-changes.md: line 76 says Velacore collects health information through an online questionnaire, which contradicts the no-PHI rule and faq.html; line 94 an intake form provider; line 77 our payment processor; line 103 HIPAA-style safeguards wording. Also unsourced: "HIPAA-compliant" on faq.html and the six program pages.

Nov 19 2026, SEO and security batch, local, vc-reviewer PASS, waiting for Dourado's push OK with 5e6fe25 and 43aaa76: Dourado's standing rule, now in memory: every build is checked for SEO tags and indexing, safety, and that nothing breaks. tools/seo_head.py gives the four legal pages vc-copy's descriptions, canonicals on the clean URL and share tags, and makes the 404 noindex; run it after editing a legal page. The builders add Twitter and og:image size tags. netlify.toml and vercel.json: Permissions-Policy turns off geolocation, camera, microphone, payment and usb, and a narrow CSP blocks plugins, foreign base tags, foreign framing and off-site form posts without touching scripts, styles or fonts; tested in a browser with the headers injected. If OpenLoop ever offers an embedded intake, frame-ancestors, form-action and payment must change first. The site audit has a new section 5, SEO tags and indexing: 32 pages complete, all 22 sitemap URLs answer 200 live with no redirect, no duplicate titles or descriptions. Start pages stay noindex on purpose. Found, older, not changed, needs Dourado and the attorney before LegitScript: privacy.html still names a payment processor and an intake form provider and an online questionnaire, and states "we maintain Business Associate Agreements with vendors", which COMPLIANCE.md marks unresolved; docs/legal-drafts/04-privacy-policy-changes.md has the rewrite waiting on counsel.

Nov 19 2026, fifth push: on Dourado's "Push it", 6c23a52 and b2240bc went live after vc-reviewer PASS on its second look; the first look BLOCKED a "You chose the injection" line on Start pages reached without a choice, and "Your clinician confirms the form". Now: form cards on the Semaglutide and NAD+ pages link to their own Start pages, start/semaglutide-oral.html, start/nad-nasal.html and start/nad-oral.html, built from FORM_CHOICES in tools/build_programs.py; only those three say "You told us you prefer ...", in vc-copy's wording, with the clinician deciding whether to prescribe and the form and the dose. Each has its own intake key in audit-config.json and falls back to the program's link, since Dourado expects one link per program; if so, the form preference reaches the clinician only if the Agile intake asks for it, which the OpenLoop email asks. The Semaglutide oral plan re-points the page's Start buttons and phone bar. Verified live: full audit 1 fail, now 9 Start placeholders, 16 pass; every form card and the oral plan switch work; no sideways scroll. Found live: Netlify strips .html from hrefs, so the chooser's vitality no-needles NAD+ card fell back to /start/nad; a fix matching with or without .html is local, awaiting vc-reviewer and Dourado's push OK. Lesson: any script that matches an href must tolerate the stripped form. This note itself is local, not pushed.

Nov 19 2026, fourth push: on Dourado's "Yes push", c5e31bd and the handoff note b641ce2 went live after vc-reviewer PASS. Dourado spotted the home Tired of needles tiles had no slash; tools/inject_panel.py now writes their price line from the program data, skipping any data-oral tile, which is priced by form. Slash rule, per vc-reviewer, recorded in the was() docstring: only on a short price line whose headline is the first month price with "then $X/mo" beside it; never inside a sentence, on a "from" price, or where the regular price is already the big figure. So the program price box note, Start page sentence, home goal line, Semaglutide forms line and Learn article stay as words. Verified live: full audit 1 fail, the Start placeholders, 16 pass; home page no sideways scroll at 320, 375 and 1280; the chooser no-needles path shows $259 oral Semaglutide and the slashed Microdosing card. Open copy point for vc-copy: the Microdosing tile under Tired of needles says "Oral or injection"; consider saying an oral form is one of the options. This note itself is local, not pushed.

Nov 19 2026, third push: on Dourado's "Push", 2834bec and the handoff note df882e0 went live after vc-reviewer PASS. Program pages no longer scroll sideways at 320 px: up to 380 px the price box thumb is 72 px and Rx only may wrap under the price. PRICE_PENDING in tools/build_programs.py puts "The prices shown are illustrative until our telehealth services partner's final price list is confirmed." at the start of the fine print on all six program and six Start pages. Verified live: full audit 1 fail, the Start placeholders, 16 pass; all 12 program and Start pages show no sideways scroll at 320, 375 and 1280. Not checked: Safari, Firefox, real phones. This note itself is local, not pushed.

Nov 19 2026, second push: on Dourado's "Push if everything passes", three commits, 773d854 to 07df212, went live after vc-reviewer PASS on each. Thumbnails are saved at 432 px by tools/make_thumbs.py, since phones show them up to 106 CSS px. The price slash: wherever a first month price shows, the monthly price after month one sits in front of it struck through, read from the program data by first_and_then, was, price_html and tcard_price in tools/build_programs.py; inject_panel.py now also writes the six home card prices. Menu cards and the phone bar keep "then $X/mo" beside it, Semaglutide says injection, screen readers hear "Monthly price after the first month", and the bar hides the struck figure below 360 px. The home price note now says prices are illustrative until the partner's list is confirmed. The site audit's price reader was fixed for the nested spans. Verified live: full audit 1 fail, the Start placeholders, 16 pass; the slash shows on home, pricing, menu and bar at 320, 375 and 1280 with no sideways scroll; the live thumbnail is the new 23 KB file. The slash is honest only while OpenLoop really has a first month price and charges the struck figure from month two; if not, every slash comes off. Open, flagged by vc-reviewer, not caused by this batch: program pages scroll sideways at 320 px because the price box is about 350 px wide; the illustrative-price sentence is not on program pages yet. Not checked: Safari, Firefox, real phones, an attorney's read of the slash under FTC and state auto-renewal rules.

Nov 19 2026, pushed: on Dourado's "Push it", nine commits, 55ba448 to 6e81d97, went live: the dropdown fix, the program page first phone screen, the centered home program row and button fixes, the chooser fade removal, and five note commits. Checks before push: compliance 0 fail, audit only the Start placeholders. Live within 10 seconds of the push. Verified live: the full audit with the live site shows 1 fail, the known Start placeholders, 16 pass; home, Tirzepatide, faq, learn and pricing return 200 at 375 and 1280 with no sideways scroll and no script errors; on the live home page at 375 the chooser fade is gone, the filters sit on one line with on and off states, the cards snap to center, and Watch the explainer is the outlined button. Not checked: Safari, Firefox, real phones. This note itself is local, not pushed.

Nov 19 2026, last: Dourado chose to drop the fade-up on the program chooser steps, so the phone card row is the home page's one motion moment. The chooser still walks step 1 to results, tested headless at 375. vc-reviewer PASS. Compliance 0 fail, audit only the Start placeholders. Not pushed: six commits now wait for his push OK. Open for Dourado: the phone bottom bar slides in and out on its own as he scrolls, which vc-reviewer flagged as a possible second motion; it could show and hide instantly instead. Reel verdict: the slide-in cart reel from levilayernn was first skipped because the site has no cart today.

Nov 19 2026, cart decision: Dourado decided patients must be able to choose more than one program and check out once, then go to intake. Velacore will have a cart. Not built yet. OpenLoop is the merchant of record and Agile includes a Velacore-branded cart per the Nov 12 call, unconfirmed in writing, so the likely shape is: our site lets people pick programs, then hands them to the Agile cart and intake; card details never touch our site. Questions for OpenLoop are section 2 of the follow-up email in docs/openloop-email-draft.md, still unsent. That follow-up was rewritten Nov 19 to hold all open OpenLoop questions the first email does not ask, to send after OpenLoop replies to the first. 54 questions after the vial one was answered.

Nov 19 2026, vial branding settled: Dourado says the vials patients receive will not carry Velacore branding. The Velacore label exists only in our pictures. BRAND.md section 6 now says so. The site's illustration note, "may look different", is still true but soft; a plainer line was offered to Dourado, not changed. Ads and video that show labeled vials must carry the illustration note; vc-ads to apply. When it is built, the levilayernn reel applies: a cart panel that slides in and stays, with keep browsing and check out, so people are never pulled away mid-choice. Copy must say a clinician reviews each program; no bundle reads as a regimen.

Nov 19 2026, later: committed 7210e0b, program pages show photo, price, plan choice, Start and the FDA notice on the first phone screen, vc-reviewer PASS. Then, from three more reels Dourado liked, one more commit. The home program row now centers each card on phones at 480 px and below, with the side cards slightly smaller as you swipe. Tabbing into a card brings it fully on screen. The home filter row stays on one line and scrolls sideways; its buttons are plain on and off buttons, not tabs. Button rules: the phone bottom bar hides whenever another green button or the chooser's results are on screen, "Watch the explainer" is now an outlined button, the duplicate Find your program button above the guarantee band is gone, and card Start buttons are 48 px tall. vc-reviewer PASS after three rounds. Not pushed; five commits wait for Dourado's push OK. Open decision for Dourado: the home page now has two moments of motion, the chooser fade-up and the card row. Either the fade-up goes or both stay and docs/visual-direction.md section 4 records it. Not checked: Safari, Firefox, real phones with a screen reader. The tabs reel was judged: tabs only fit the home filters; program pages keep safety information in plain view, never behind tabs.

Nov 19 2026: Dourado sent design and ad reels to judge. Decisions given: a crossed-out price only if it is the real monthly price, a savings line only with honest math, since a new patient's first 12 weeks month to month cost only $10 more than the 12-week plan on Tirzepatide; no "Most popular" badge until there is real data, and never on a drug; the five stages of awareness are a plan for vc-ads, nothing runs before LegitScript. Committed 16acde9, the Treatments dropdown fix: no menu role, aria-expanded matches the screen, Escape closes it. vc-reviewer PASS. Not pushed. Open finding, not built: on a phone the first screen of every program page shows no photo, price or Start button; the first Start button is about two screens down. Proposed to Dourado as a preview first.

Nov 18 2026, night: pushed 55ba448 on Dourado's "push", after he was told the ten notes and hidden-program commits ride along. vc-reviewer PASS on the Semaglutide oral photo. Verified live: the new photo served on the second check, home, Semaglutide and Pricing return 200, /nope-404 returns 404, and the hidden sexual health and HRT pages and photo return 404. Live audit 16 pass, only the Start placeholder fail. A live phone screenshot shows the one-bottle oral tile next to the injection tile.

Nov 18 2026, night, local only: three Gemini images made by Dourado from his tablet, each checked letter by letter. Sexual Health and Women's HRT bottles pass and wait as `_hold-` files in assets-in/products until launch. Semaglutide oral is now one standing bottle; the two-bottle photo was cut off at the right edge and two edits failed to fix it. The old one is kept as `_prev-semaglutide-oral-two-bottles.jpg`. The new photo, its tiles and its thumbnail are in public/ and change the Semaglutide Forms card, the Needle-free menu and the side panel. Caution: `tools/prepare_images.py` run with no names re-made every photo at a different size from the live files; it now takes file names and makes product photos 1200 wide like the live ones. Compliance 0 fail, site audit only the Start placeholder fail. Not pushed.

Nov 18 2026, late evening: Dourado asked to push the sexual health and HRT products with placeholders. Vale built the structure and kept it switched off, since naming these medications live without OpenLoop's safety text and pharmacy answers would fail the vc-reviewer launch blockers. The two programs are wired into every builder: program and Start pages, Treatments dropdown, slide-in menu, pricing cards, generated footers and the phone price bar. A program goes live only when its slug is added to LIVE in tools/draft_programs.py; with LIVE empty the rebuild changed no file in public/. A switched-on copy rendered clean at 375 and 1280. Launch steps, including the hand edits to index.html and sitemap.xml, are in docs/launch-sexual-health-hrt.md. Commit e91afbc, not pushed. Dourado decided the same night: keep both programs hidden until OpenLoop answers in writing.

Nov 18 2026, evening: sexual health and women's HRT drafted on Dourado's "Yes, draft them". Not live and not publishable: copy by vc-copy in tools/draft_programs.py, built by python -I tools/build_drafts.py into drafts/programs, outside public/, with a draft banner, noindex, no analytics, a safety placeholder and an Open before launch list. Facts come from the Nov 12 proposal pages 15, 16, 24 and 25, read in the Drive viewer and recorded in docs/openloop-proposal-notes.md. vc-reviewer PASS for the draft copy, fixes applied. Launch blockers: every open item answered by OpenLoop in writing, the compounded disclaimer placed per item, the site-wide 503A wording broadened if any item is filled elsewhere, full prices in menus and the phone bar, the attorney's tracking decision, the approved-name list in vc-compliance-check, real product images, then a vc-reviewer ship review. Two new questions are in the held follow-up of docs/openloop-email-draft.md.

Nov 18 2026, afternoon: pushed 5e3357b with four docs-only commits, on Dourado's "push it" and a second yes for the extra commits. vc-reviewer PASS, verified live; the live audit shows 16 pass and only the Start placeholder fail. Titles and metas on every page follow docs/seo-titles-nov18.md. The top bar on all pages now reads "A telehealth platform. Independent licensed clinicians decide. Prescription required." and carries the home page business-model disclosure. The home hub H1 is "GLP-1 and peptide programs, online", with the sub line "Prescription only. No consultation fee. Shipping included." The pricing meta fills its from prices from the program data in build_pages.py. Still waiting: Dourado's screenshots of the sexual health and HRT pages from the Nov 12 Agile proposal, Velacore payout column cropped out, before those pages are built.

Nov 18 2026, early afternoon: pushed 3daa4d7 on Dourado's "push it", vc-reviewer PASS, verified live. Every small product picture is now a square cut around the label by tools/make_thumbs.py, so each name reads at 54 px. The home Not sure tile shows the clipboard render. Phone Learn article cards show a label close-up, except the comparison card, which keeps both vials so neither drug is singled out.

Nov 18 2026, about noon: pushed 9a14f3d on Dourado's "push it", verified live. The new styles and card images were served about 20 seconds after the push. The live audit shows 16 pass and only the Start placeholder fail. Learn, Clinicians and How it works have no overflow and no broken images at 375 and 1280.

Nov 18 2026, late morning, local only, vc-reviewer PASS on every piece. Changes in this batch:
- Side menu: mouse drag on the card rows and the panel.
- Email links also copy the address with a short note.
- Clinicians page rebuilt as a visual layout by clinicians_main in build_pages.py.
- New step-visit photo, a woman at a laptop, on How it works step 1.
- Learn cards: right for me is a glass clipboard render, How is it taken shows the four forms side by side, and Peptides vs. GLP-1s is a glass sphere render with a page-text key.
- BRAND.md section 5 records the 3D exception for education visuals. Originals are in assets-in, and the crops come from tools/make_learn_cards.py.
Waits for Dourado's push.
Still open from the design pass: the program hero's empty space on desktop, the two Semaglutide form tiles, the Semaglutide oral tile photo cut at the right edge, the goal card thumbnails cropping caps, uneven phone card margins, three footer column sets and the shorter legal nav.

Nov 18 2026, about 3:20 AM: pushed 0d5ea6c on Dourado's "push what we can now", verified live. The live audit shows 16 pass and only the Start placeholder fail, with no overflow on home, Pricing or Learn at 375 and 1280.

Next session, Dourado's plan: update images where needed. The list:
1. The three Learn photos, prompts reviewed in docs/gemini-learn-set-nov18.md: step-visit.png, learn-taken.png and learn-difference.png. The old step-visit original is set aside, so do not run prepare_images for lifestyle until the new one is in. On placing step-visit, change its alt text from a man to a person in tools/pages.py and public/learn.html.
2. Semaglutide oral photo: the tipped-over bottle is cut at the right edge on the tiles and the Forms card. It needs a Gemini redo with the bottle fully in frame. Write and review the prompt first.
3. Goal card thumbnails on "What are you here for?": the small vial pictures crop off the caps. Check whether a looser crop of the existing photos fixes it before asking for new images.
Then the design calls still open: the program hero's empty space on desktop, the two Semaglutide form tiles filling two thirds of the panel, uneven phone card margins, three different footer column sets, and the shorter nav on the legal pages.

Nov 18 2026, about 3 AM, local only, vc-reviewer PASS twice: a site-wide design pass at Dourado's request, phone and desktop. A scan of all 29 pages found the touching Learn buttons, one-word last lines, fine print too small and too wide, and em dashes in titles; all fixed in styles.css with balanced headings and pretty wrapping. A visual review of 30 screenshots found more: the 404 page broke into two columns, now one centered column; program closing buttons centered; bullets on the first line; the trust strip a list on phone; the pricing refund panel no longer touching the section above; the stepper on one row; the Legal labels removed. Then, at Dourado's direction, no hard flat blocks: the dark pine panels carry jade and helix blue glows with grain, BRAND.md section 2 fifth exception. Open design calls for Dourado: program hero empty space under the left column on desktop, the two Semaglutide form tiles filling two thirds of the panel, the oral Semaglutide photo cut at the right edge, the goal card thumbnails cropping caps, uneven phone side margins between cards, three different footer column sets and a shorter nav on the legal pages. Not pushed.

Nov 18 2026, about 1:40 AM: pushed 9241cf4 on Dourado's "push now", verified live. It carries the Learn page photo cards, the program card crop eased to 1.06, and the reviewed prompts in docs/gemini-learn-set-nov18.md. The live audit shows 16 pass and only the Start placeholder fail, and all 10 Learn photos load at 375 with no overflow. Open: Dourado makes the three Learn photos from that file when he is at his computer; the old step-visit original is set aside, so do not run prepare_images for lifestyle until the new step-visit.png is in. On placing it, change the step-visit alt text from a man to a person in tools/pages.py and public/learn.html, and send the images through vc-reviewer.

Nov 18 2026, about 1:10 AM, local only, vc-reviewer PASS after one block: the Learn page leans into the Hims look at Dourado's request. The six question cards lead with photos instead of line icons, and Go deeper is four photo cards with the product illustration note under them. Photos are 3 by 2 crops of approved originals, made by tools/make_learn_cards.py; the article cards come from build_articles.py. The reviewer blocked the walking couple on the What if I stop card as an implied outcome; it now shows the clinician video visit. Open, not blocking: the right for me card photo shows a man older than the BRAND.md section 5 age range. Not pushed; waits for Dourado's push it.

Nov 18 2026, about 12:30 AM, vc-reviewer PASS, pushed on Dourado's "push it when you're done": four changes. One, the needle-free and Forms tiles were soft because the browser zoomed the photo 1.16 and then shrank it hard; the zoom is now cut into tile photos at 300, 450, 600 and 900 wide in public/images/products/tiles, made by make_tiles in tools/prepare_images.py. The assets-in originals were renamed so the plain names hold the live marble photos; the older ones are kept with an underscore and the script skips them. Two, the header mark is now public/logo-mark.svg, the designer's own paths. Three, primary buttons are lit from above, the fourth gradient exception in BRAND.md. Four, the hub hover tiles: violet became plum and ocean blue became pine, and hover runs on mouse devices only. Kevin's list in docs/design-references-kevin.md is updated. Reviewer note: any future button wording names the step, never a health result.

Nov 18 2026, about 12:35 AM: push 689a044 verified live. styles.css, logo-mark.svg and the tile photos served about 20 seconds after the push, the live audit shows 16 pass and only the Start placeholder fail, and a live screenshot shows the sharp tiles, the vector mark and the lit button.

Nov 17 2026, about 5:50 PM, local only, vc-reviewer PASS: hover fills on the home hub from Dourado's Hims reference. Each small tile fills with its own gradient and white text, and the two big cards deepen their tint and ease the photo to 1.03. Colors are in the BRAND.md section 2 hover table, the third gradient exception. Mouse devices only, same state on keyboard focus, off under reduced motion. Kevin, the Salvage session, answered Dourado's question about buttons, tiles and gradients from the uploaded videos, general knowledge only. Saved with where Velacore stands on each point in docs/design-references-kevin.md. Open proposals from it: lit-from-above primary buttons, an SVG logo, and the fine pointer check on hover.

Nov 17 2026, 5:40 PM: pushed on Dourado's "Push it", commits 85242af, 431d3f7 and a2679fc. The home weight card fade no longer touches a vial, and its blue eases into the photo's colors, live on www.velacorehealth.com. Checked before: compliance 0 fail, site audit only the Start placeholders. Checked after: new stylesheet and tirzepatide-wide files serve, live audit 16 pass with the same placeholder fail, the card serves tirzepatide-480 at 375, tirzepatide-wide-800 at 1000 and the trio at 1360, no overflow. Not checked: iOS Safari and Dourado's own phone. Still open: the OpenLoop consent question, waiting on Dourado's choice.

Nov 17 2026, about 5:45 PM, local only, vc-reviewer PASS: Dourado found the color edge where the weight card photo starts too hard. The .hub-weight background now eases from #E4EBF9 into the photo's own sampled left-edge colors, mint wall to marble, across the text side; text contrast 5.48 to 1 at worst. BRAND.md section 2 records it as the second gradient exception. The Hormone support card still uses its flat tint.

Nov 17 2026, about 5:40 PM, local only, vc-reviewer PASS: the home weight card fade no longer touches a vial. Below 1300 px the photo box is narrower than the three-vial group, so from 701 to 1299 px the card shows one Tirzepatide vial, `public/images/products/tirzepatide-wide.webp` plus -800, made by hand from tirzepatide-marble.jpg: a square crop around the vial with 200 px mirrored strips each side. Like tirzepatide-480, remake it whenever the Tirzepatide photo changes. At 1300 px and up the trio stays, with a 16 px fade. The sub line uses a non-breaking hyphen in GLP-1. Dourado asked to host OpenLoop's telehealth consent on our site, not as a redirect. Told him we have our own consent page already, that copying theirs word for word needs OpenLoop's written OK, and offered to add that request to the OpenLoop email draft and have vc-copy align our page meanwhile; waiting on his answer.

Nov 17 2026, 5:30 PM: pushed on Dourado's "Push it", commits 5c42b3c and 0e088fc. The Pricing page cards line up and carry their category colors on www.velacorehealth.com. Checked before: compliance 0 fail, site audit only the Start placeholders. Checked after: the live stylesheet and the six data-cat cards serve, live audit 16 pass with the same placeholder fail, every card in the first row has its price row at the same offset at 1440, no overflow at 1440 or 375. Not checked: iOS Safari and Dourado's own phone.

Nov 17 2026, about 5:30 PM, local only, vc-reviewer PASS: the Pricing page cards line up row by row with the same subgrid method as the home row, and each pricing card now carries data-cat so its top stripe and dot match the home card colors; before, every pricing card showed violet. Not pushed.

Nov 17 2026, 5:07 PM: pushed on Dourado's "Push it", commits 54b3070 through 3fdce85. Live at www.velacorehealth.com: aligned program row, Needle-free menu group, sharp goal thumbs, all ten new photos, and the sharper product photos. Checked before: compliance 0 fail, site audit only the Start placeholders. Checked after: new stylesheet, images and pages serve 200, live audit 16 pass with the same placeholder fail, live screenshots of pricing at 1440, clinicians and home at 375 with no overflow and no broken images. Not checked: iOS Safari and Dourado's own phone. Seen on the live pricing page: the price rows there do not line up across cards the way the home row now does.

Nov 17 2026, about 4:50 PM, local only, vc-reviewer PASS: Dourado said the product photos were not sharp enough. No new images were made. The ten product photos were rebuilt from their full-size originals in assets-in/products with a Lanczos resize and light sharpening at quality 92, each with an 800 wide copy that cards and tiles serve through srcset; the helper is `prod_srcset` in tools/build_programs.py, and the index cards carry it by hand. Program cards zoom 1.28 on the vial, and form tiles zoom 1.16 with a clip, so labels read larger. tools/prepare_images.py now sharpens product photos and writes the 800 copy itself. Originals: tirzepatide, semaglutide, microdosing, nad, glutathione and sermorelin come from the -marble jpgs; the forms come from nad-nasal-marble, nad-oral-marble, microdosing-oral and semaglutide-oral. Untested: iOS Safari with the clip.

Nov 17 2026, about 4:45 PM, local only, vc-reviewer PASS: the last three photos are in. clinicians-hero, the woman now looking at her laptop, is the Clinicians page top photo. clinicians-review, the man now reading his tablet, sits under What a clinician can decide. pharmacy-lab is at the top of the 503A article and in the About page How it works section, moved there from What we do not do on the reviewer's note so it never reads as Velacore's own lab. All ten images from docs/gemini-site-set-nov17.md are now placed. Still not drawn: the US map for Licensed in your state.

Nov 17 2026, about 4:30 PM, local only, vc-reviewer PASS: seven of the new Gemini photos are on the site. Clinicians page: credential still life and video visit. About: woman on sofa. Contact, and FAQ by hand in public/faq.html: man with phone. Learn articles: the GLP-1 hands photo, the Semaglutide and Tirzepatide pair, and the Microdosing pair, the last two with the product illustration note. Photo slots come from `art_photo` in tools/build_programs.py, fed by the hero and photos keys in tools/pages.py and tools/articles.py; a slot stays empty until its file exists. Waiting on Dourado: clinicians-hero and clinicians-review, redone because the clinicians looked away from their devices, and pharmacy-lab, not yet made. Each goes back through vc-reviewer when it lands. Originals in assets-in under the same names; web copies made by hand with ffmpeg at 1600 and 800 wide. The US map for Licensed in your state is not drawn yet.

Nov 17 2026, after 4 PM, local only, vc-reviewer PASS: the home program row lines up on every card through CSS subgrid, with older browsers keeping the flex row. The arrow buttons measure the first visible card. The Treatments dropdown and the side panel gain a Needle-free group from `NEEDLE_FREE` in `tools/build_programs.py`: Semaglutide oral, NAD+ nasal spray, NAD+ oral dropper and Microdosing GLP-1 oral. The dropdown columns are now Weight, Vitality with Hormone support under it, Needle-free, and Not sure. The goal rows use single-vial thumbs, because the squeezed group photos looked low resolution to Dourado. Three new thumbs, nad-nasal, nad-oral and microdosing-oral, were cropped by hand from the product photos and are not made by prepare_images.py, so remake them if those photos change. "A metered spray" became "A nasal spray", per the reviewer, until OpenLoop confirms the device. Dourado asked to add HRT, TRT and ED; declined under the hard rule, nothing written. Ten new Gemini prompts for Clinicians, About, FAQ, Contact and Learn are in `docs/gemini-site-set-nov17.md`, waiting on Dourado. The reviewer warned that photoreal AI clinicians as the Clinicians page hero will read as Velacore's clinicians now that the AI notes are gone. Dourado decided Nov 17 2026: no note and no wait, the clinician photos go on the page as they are. The other house rules still hold: no name, badge, credential or quote on any pictured clinician. The reviewer also found items outside the six approved treatments named in committed docs, openloop-proposal-notes, reference-arsynl, gemini-queue and HANDOFF; Dourado to decide whether to scrub them.

Nov 17 2026, 4:05 PM: pushed on Dourado's "Push it", commits 2d2c741, 8849d72 and aea9ccc, so the AI notes removal, the home gradient and the single-vial phone weight card are live at www.velacorehealth.com. Checked before the push: compliance 0 fail, site audit only the six Start placeholders. Checked after: the live stylesheet and the 480 Tirzepatide file serve, no AI illustration line on home, live audit 16 pass with the same placeholder fail, screenshots at 375, 1040 and 1280 with no overflow and no tap target under 44 px. Not checked: iOS Safari rendering of the fade and grain, and Dourado's own phone.

Nov 17 2026, later afternoon, local only: Dourado asked for a gradient behind the home top for contrast and kept it, much better in his words. Three pale washes, mint, blue and violet, fade to white, with a faint grain against banding; the four small cards are white with a soft shadow, both big cards get the same shadow, and the illustration note under them is pine soft. Lowest measured text contrast on it 5.2 to 1. On phones the weight card shows the single Tirzepatide vial, `public/images/products/tirzepatide-480.webp`, instead of the cut-off three-vial photo, made by hand with ffmpeg from tirzepatide.webp at 480 wide, not by tools/prepare_images.py, so remake it whenever the Tirzepatide photo changes, and both big cards fade the photo in over a longer stretch; desktop keeps the trio. BRAND.md section 2 records the gradient exception.

Nov 17 2026, after the 1:25 PM push, local only: Dourado asked to take the AI notes off the website. Removed the line under the home clinician photo and the line under the Learn page video. The video's own closing small print still says people and images are AI-generated; changing it means a video rebuild. Vale flagged that vc-reviewer had recommended the home line because that block discloses prescriber identity, and that the AI-people question is on the attorney list; Dourado's call. Not pushed.

Pushed Nov 17 2026 at about 1:25 PM on Dourado's push it, 6 commits to 23c6d47: Semaglutide oral, the amber NAD+ spray and dropper, the home clinician photo, the Hims-style home hub and edge-to-edge header. Verified live: www.velacorehealth.com rebuilt within about 20 seconds; home, the six program pages, privacy, terms, pricing and the new image files return 200, the 404 page returns 404; the hub, the platform line, the illustration notes and See Sermorelin are in the live markup; the live audit shows 1 fail for the six Start placeholders, 8 review, 16 pass; the live home page renders at 375, 1040 and 1280 with no sideways scroll and no tap under 44 px. This note is committed locally and rides with the next push.

Nov 17 2026, about 1:30 PM, local only, not pushed. The home hero is rebuilt from Dourado's marked-up Hims screenshot: the header row runs edge to edge on every page, the Treatments dropdown is centered on the header above 980 px, then a hub with a short h1, the telehealth-platform sentence under it, two big goal cards, Weight and Hormone support, four small cards, NAD+ and Glutathione, Needle-free options, Compare prices, Not sure, and the illustration note; under it a weight band with the three weight vials, the price line and the trust list. Dourado asked for TRT as the second big card; it is Hormone support until TRT is in OpenLoop's written terms and cleared by the attorney, and its name stays out of the files. vc-reviewer BLOCKED twice-fixable, then PASS: the platform sentence and the illustration note had to be on the first screen. Open from that review: at 375 the weight card photo crops two vials, and the three-vial photo shows three times on the home page; a wide weight photo from Gemini would fix both. BRAND.md section 2 now allows the flat goal tint on the two big home cards.

Nov 17 2026, about 1:15 PM, local only, not pushed. Every liquid bottle is now amber glass by Dourado's choice: the NAD+ nasal spray and the NAD+ oral dropper were remade in amber to match the Microdosing dropper, so the four needle-free tiles match. BRAND.md section 6 now says amber for every liquid bottle. The home clinician block, Licensed clinicians in every state, now shows an AI-generated over-the-shoulder clinician on a video visit in place of the logo mark, `public/images/lifestyle/clinician-call.webp`, prompt H in `docs/gemini-queue.md`, with the line under it: Picture is an AI-generated illustration and does not show a Velacore clinician. vc-reviewer PASS on the batch, the line added on its note. Open from that review: if the clinician photo is ever redone, neutral scrubs instead of pine and a patient in casual clothes on the screen; COMPLIANCE.md line 77 still names an Asher-era physician and lines 174 to 177 still list a provider headshot slot, tidy when convenient. Audits: 0 fail, 7 review, 3 pass; 1 fail for the six Start placeholders, 8 review, 7 pass. Unpushed: the Semaglutide oral commit, the amber spray, the amber dropper and this batch; waiting on Dourado's push it.

Nov 17 2026, morning, second overnight run, Dourado asleep, local only after the morning push. He recorded hims.com on his phone and asked for whatever should come first; the read of that recording and the take list are `docs/visual-direction.md` section 5. Built from it, each vc-reviewer PASS before commit: the home page as one rounded card per block with one headline, one line and one button, How it works on the home page cut to four short rows; a sticky four-word stepper on How it works, Intake, Review, Delivery, Support, the current step lit; the phone footer as an accordion on every page, script-added so links stay visible without it. Also the six program pages in the card pattern: the category as a pill under the h1, what and who as two cards, the journey as numbered rows in one card with two buttons; copy unchanged, vc-reviewer PASS. Skipped on purpose: the pill version of the goal question, because Dourado accepted the photo rows and has not seen pills; the hero drift loop, which waits on the marble hero shot. The unused marquee and molecule code from the first build is removed. Pushed Nov 17 2026 on Dourado's push, 6 commits to 9671ec3. Verified live: the changed pages return 200, the home cards, the stepper, the program rows and the phone footer accordion all run on the live site at 375 and 1280 with no script errors; the live audit shows only the six Start placeholders failing. Later that morning Dourado found two photo crops wrong on his Samsung at about 480 px: the Not sure card now uses a square six-vial image, hero-group-square-1200.webp and -600.webp, made from the group photo on a blurred backdrop, and the chooser goal tiles keep their 4 by 3 photo between 421 and 860 px; the stale desktop wide-card rules are gone. vc-reviewer PASS, pushed as ef1a7e2 on his push, verified live at 480 and 1280. His Learn page showing the bead drawing was a stale browser copy; a refresh fixed it. Dourado asked why the nasal sprays were not on the site: no reason beyond the queue, the NAD+ spray and dropper photos from Nov 16 were never placed. Now the Forms card on the NAD+ page, `forms` on the NAD+ entry in `tools/build_programs.py`, files `products/nad-nasal.webp` and `nad-oral.webp`, vc-reviewer PASS, commit e696855, waiting for push. NAD+ is the only approved program with a spray; the oral forms of Semaglutide and Microdosing wait on OpenLoop naming them in writing. Reviewer note to carry: some header and footer links measure under 44 px on program pages, pre-existing, separate fix. Then at his direction a Tired of needles section on the home page, `#noneedle`, three tiles linking to the NAD+ forms and the Microdosing page, vc-reviewer PASS. Open for the written proposal check: if Glutathione gets a non-injection form, the Two programs line in that section goes stale. Dourado wants a proper oral GLP-1 photo before that offering goes on, queued in gemini-queue. He also wants the wider catalog on the site: the proposal items not yet on the site were laid out for him with what each needs; he has not yet named which ones in writing. He raised a hormone program that is not in the written proposal on file and is a controlled substance; it waits on OpenLoop in writing and the attorney, and its name stays out of the files until then. Pushed Nov 17 2026 on Dourado's push, 3 commits to 8c90494: the NAD+ Forms card and the Tired of needles section, with the microdosing vial standing in as the placeholder photo until the oral GLP-1 shot is made. Verified live, the live audit shows only the six Start placeholders failing. Then the image batch for the next push, every piece vc-reviewer PASS: Glutathione redone by Dourado; NAD+ and Sermorelin redone from the Tirzepatide photo so all six vials match, old sources kept as `_prev-*-nov16.jpg`; the Microdosing GLP-1 amber dropper replaces the placeholder in Tired of needles, its form still to confirm with OpenLoop, question added to the email draft; the step 4 photo on How it works, a man about 32 on a plain sofa, after try 1 had a third arm. Dourado's direction: people in photos are late twenties to late thirties, naturally good-looking, ordinary builds, framed the Hims way; BRAND.md section 5 updated, and those photos stay out of Weight sections and weight ads. Pushed Nov 17 2026 on Dourado's push it, to fff62f7; verified live, every changed page and new image returns 200 and the served vial files match local byte for byte. Next asked by Dourado: the oral GLP-1 images. Semaglutide oral is drawn as an amber dropper to match the Microdosing one until OpenLoop names the form; the question is in the email draft.

Night of Nov 16 2026, after the first push. Pushed Nov 17 2026 at about 12:15 AM on Dourado's push it, 10 commits to 2fbe37d, every piece vc-reviewer PASS. Verified live: changed pages and new files return 200, the chooser runs on the live home page at 375, the live audit shows only the six Start placeholders failing.
- How it works is rebuilt as a visual page: four photo steps with short lines, the long copy folded under each step, a refund band, two does and does not cards. Data is the `flow` block in `tools/pages.py`, layout is `flow_main` in `tools/build_pages.py`. Dourado's brief for the whole site: sell and teach at a glance, for people with a short attention span, not a worksheet.
- Learn page: the bead walk-through is gone; the video sits beside the intro text. Dourado found the flat drawing clashed with the video.
- Image sharpness: the files were sharp, the vials were small in frame. Goal tiles are cropped tighter and the hero and tiles now use srcset with sharpened sizes. Glutathione on water is only 896 px wide at the source and Tirzepatide is heavily compressed.
- Dourado's decision: all six single vial photos go on marble, no water. NAD+ and Sermorelin are made. Tirzepatide, Semaglutide, Microdosing GLP-1 and Glutathione still need a Gemini edit each, one step at a time, vial large in the frame. Swap all six on the site together.
- Also in this batch, each vc-reviewer PASS: the Not sure where to start card now shows the six-vial photo as a wide band on desktop; the Treatments menu thumbnails are sharp 216 px close-ups of the marble vials in `public/images/products/thumbs/`; the brand guide section 5 now says marble.
- Dourado's questions answered Nov 16: an AI clinician face is a house rule, not a LegitScript one; he chose the full shot with no label. He said yes to a Find your program chooser. Built Nov 17 at `#goals`: goal, then injection or needle-free, then the matching program cards cloned from the list. Two questions, not three; the third screen is the result. Open facts for the written Agile proposal: weekly dosing wording, Glutathione's form, the word tablet.
- Pushed Nov 17 2026 at about 12:45 AM on Dourado's push it, 9 commits to f5deb4d: the pricing page, the hero menu, Plus Jakarta Sans headlines, the header gap fix. Verified live, see below. The video end card still shows the old font until the video is rebuilt and re-reviewed.
- Nov 17 2026, after midnight: the pricing page rebuilt as program cards first with short bands and folded copy, vc-reviewer PASS with three notes applied; the home hero rebuilt as a menu, three goal rows that open step 2 of the chooser, with the lede moved below. Dourado named hims.com and hims.com/peptides-plus as the layout model: image-driven, button-led, one question per screen. Memory file site-direction-sell-at-a-glance holds the rule. Take their layout patterns only, never their outcome claims, brand products, copy or look.
- Nov 17 2026, about 2 AM, local only, Dourado asleep: the slide-in menu passed vc-reviewer on its recheck. The home program row is rebuilt as one row of square cards that slides on every screen, drag, swipe, arrows or arrow keys; the phone 3D carousel and desktop grid are gone. Each card body fades white to a goal tint, weight blue, vitality violet, hormone jade, the first gradients on the site; BRAND.md section 2 now allows a short two-tone fade and bans long or strong ones so nothing bands. Dourado's words: emulate the Hims site to fit our brand, the colors in the cards and the gradients without banding, tasteful, everything with a purpose. He also asked for a list of colors, backgrounds, image orientation and motion for edgier imagery: `docs/visual-direction.md`, three product set options for him to pick from. Nothing pushed; he said continue while he sleeps, so the next pieces are built and reviewed locally and wait for his push it. Also built that night: the chooser's first question as a band at the foot of 11 pages, `goal_band` in `tools/build_programs.py`, on How it works, Pricing, Clinicians, About, Contact, Learn, FAQ and the four articles; not on the home page, program pages or legal pages. A dead scroll reveal script from the first build was removed. The explainer video was rebuilt so the end card uses Plus Jakarta Sans, and the cursor now enters at button height instead of crossing the FDA small print, a reviewer catch from Nov 16; same length, same size, captions unchanged. Every piece vc-reviewer PASS: the panel recheck, the program row with four fixes applied, the goal band, the video. Pushed Nov 17 2026 in the morning on Dourado's push, 8 commits to d82e819. Verified live: the changed pages and the new video return 200, the row slides and the goal band opens the chooser on the live home page at 375 and 1280, the panel opens, no script errors, the live audit shows only the six Start placeholders failing.
- Nov 17 2026 after 12:45 AM, local only: the slide-in menu on 22 pages, `side_panel` in `tools/build_programs.py`, hand-written pages get it from `python -I tools/inject_panel.py` after any change to it. Dourado asked for a Hims-style side panel; built with the goal rows, the six programs with first month prices, the site links and one button.
- Dourado also pointed at the Hims Tools links, BMI calculator and the like. They are free calculators that end in a Get started button, with a line that the result does not decide eligibility. A BMI calculator fits Velacore because the GLP-1 programs state BMI ranges; proposed, not built.
- Hims-style plan, in order, each piece reviewed and shown before it goes live: home hero as a menu, done; program pages in the card pattern with sections folded; a button after every section and the chooser's first question at the bottom of every page; Learn and Clinicians the same way; six big product sections on the home page on marble and mint.
- Waiting on Gemini credits, reset about 2:30 AM Nov 17: the step 4 support photo for How it works, prompt in gemini-queue; NAD+ and Sermorelin marble redo.
- Open: a vector vial sample was offered and not yet answered. The no extra cost video visit wording needs written confirmation for Semaglutide and Tirzepatide. Four Start visit buttons in the home carousel are 41 px tall at 375.


Late Nov 16 2026, the explainer is on the Learn page in the local copy, not pushed.
- `public/learn.html` has a video block: player with poster, captions attached and off by default, prescription and FDA small print, an AI voice and AI pictures line, a transcript and a Find your program button. Files are `public/media/peptides-explained.mp4` at 3.6 MB, its `.vtt`, and `public/images/learn/peptides-explained-poster.webp`. vc-reviewer PASS.
- Dourado's decisions that night: the closing scene uses the site header lockup, no purple. The AI clinician is shown at full frame with her face and no label over the shot. The house rule in `docs/gemini-prompts.md` section 8 was rewritten to match; it is our own rule, not a quoted LegitScript rule.
- Open on that shot: the reviewer's advisory is that the white coat, stethoscope and two blurred wall certificates imply credentials. Cheapest fix is a clip without the wall frames. The question of an AI clinician goes to the attorney before the LegitScript submission. Ad use of the video stays blocked.
- Small leftovers: the Messenger pill overlaps her for under half a second at 34 s; `docs/gemini-prompts.md` section 13 still says no people and names the old narrator; nobody but Dourado can confirm the audio.
- Pushed Nov 16 2026 at about 11 PM on Dourado's push it, one push of 14 commits to fe03d46: the five pages plus four Learn articles, the three home page images, and the Learn video block. Verified live at www.velacorehealth.com: 21 pages and 6 new files return 200, the 404 page returns 404, the video plays on the live Learn page at 375, the live audit shows only the six Start placeholders failing. This note itself is committed locally and rides along with the next push.


- **Nov 16 evening: explainer video and image session. Nothing pushed, the site is unchanged.**
  The running list of what is left, in order, with every Gemini prompt, is `docs/gemini-queue.md`.
  Read that first when picking this up.
  - Explainer rough cut is `03-edits/peptides-video/rough-cut.mp4`, 47 seconds, built by
    `python -I tools/video/peptides/build_cut.py vo5`. Voice is now Bella, approved line by line;
    final script and how each take was shaped are in `docs/video-peptides-script.md`. The closing
    line changed to "a licensed clinician's decision, and it's made after a review of your health
    history". vc-reviewer has not seen that line or the new closing scene.
  - The mix: every line matched to the same loudness, an ambient bed that ducks under the voice,
    subtitles as words only in Hanken Grotesk, no lead-in sound effect, voice in at 0.9 seconds.
    The closing scene is drawn in code by `tools/video/peptides/render_overlays.py` and
    `overlay.html`: logo, "See which program may fit you", the six programs, a Find your program
    button, a pointer click with a click sound, and the small print with the FDA line.
  - Dourado asked about a "free evaluation" call to action. Vale advised against the word free
    until OpenLoop confirms in writing what the patient is charged. He did not object and liked the
    Find your program closing scene; treat the free wording as open, not decided.
  - Clips 3 and 4 made today. Still to make: a new opening clip, clip 5, a clinician clip in motion.
  - New product photos filed in `assets-in/products/`, none on the site yet: NAD+ nasal spray and
    NAD+ oral dropper, each in water and on marble, and the Sermorelin vial on marble.
  - Dourado's calls today: the two new NAD+ forms go on marble, not water. The clinician step photo
    looks like a home and must be remade as a clinic office. The home page group shot is missing
    Glutathione and must be remade with six vials; the same shot will replace the six tiles in the
    video's closing scene. Whether the other four vials move to marble is undecided.
  - Oral Semaglutide and oral Microdosing photos wait on OpenLoop naming the form.
  - The OpenLoop question email is drafted in `docs/openloop-email-draft.md`. Dourado has not said
    it was sent.
  - Later the same night, after Gemini reset: the whole queue was made. The video now has a new
    opening clip with the four step names, clip 5, and a clinician clip under the closing line, and
    its closing scene shows the six-vial group shot. On the local site only, three home page images
    changed: the hero is the new six-vial group shot, step 2 is the new clinic photo mirrored to face
    step 1, and the Hormone support tile has its own Sermorelin marble photo. Compliance check 0 fail,
    site audit only the six Start placeholders. None of it is pushed and vc-reviewer has not seen it;
    that review is the next gate. Details and the two flags on the clinician photo are at the top of
    `docs/gemini-queue.md`.
  - Dourado asked for the logo to be crisp and in the site colors, no purple. The site header already
    uses the jade mark; the purple gradient file `public/logo-full.png` is what the video closing scene
    uses. Plan is in `docs/gemini-queue.md`: recolor the designer's vector, do not redraw the mark.
- **Nov 16: second OpenLoop proposal read, nothing on the site changed yet.** File is
  "Velacore Health - OpenLoop - Proposal - 11_12_26 (1).pdf", 30 pages, in the Velacore Workspace
  Drive, dated Nov 12 with a 30 day expiration. It stays out of the repo, and so does the column
  showing what Velacore receives. Read page by page in the Drive viewer, not downloaded.
  What it changes for the site, all still marked illustrative until the Order Form is signed:
  - Patient prices are listed as fixed amounts and differ from the site on five of six programs.
    Month to month: Semaglutide $209, Tirzepatide $249, Microdosing $179, NAD+ $229,
    Sermorelin $229, Glutathione $145. 12 weeks up front: $597, $717, $507, $537, $537, $387.
    The site's lower first month price is not in the proposal at all.
  - Glutathione is now in writing as an injection, with 4, 12 and 24 week plans.
  - New disclosure lines: all patient-facing materials must be approved by OpenLoop before use;
    Velacore receives PHI only under the BAA; no tracking pixels and no PHI-based advertising.
    This bears on the open analytics decision and on the rule that patient data never touches
    our servers.
  - The GLP-1 pages are titled as including care coaching. The site keeps no coaching language.
  - LegitScript is not mentioned anywhere in the document.
  - Open questions for OpenLoop and the attorney were given to Dourado in chat on Nov 16.
- **Five stand-alone pages built Nov 13, committed, not pushed.** How it works, Clinicians,
  Pricing, About and Contact, at `public/<slug>.html`. Copy is in `tools/pages.py`, builder is
  `python -I tools/build_pages.py`. The Pricing cards read from the program data, nothing typed
  twice. Menus and footers on every page point to them; the home page sections remain. No
  analytics on the five pages. vc-reviewer PASS. Dourado asked for these and for the Learn
  articles to go out in the same push; the push still needs his "push it" for the batch.
- **Open on those pages.** The Pricing page says prices are illustrative until the partner's
  final list is confirmed; no other page says so. Dourado decides whether to add the same line
  wherever a price shows. The reviewer will block that sentence and real intake links being live
  together. Contact has no phone or mailing address yet. The credentialing list on Clinicians
  comes from the Nov 2 proposal and needs a recheck against the signed Agile agreement.
- **Learn articles, batch 1, committed 310ec22, not pushed.** Four pages in `public/learn/`, built
  by `python -I tools/build_articles.py` from `tools/articles.py`. vc-reviewer PASS after three
  fixes. Byline says written by Velacore Health and not reviewed by a clinician. No analytics on
  them. Before pushing on a later day, set the dates to the real day. After the push, check that
  /learn still serves the hub, since a `learn` folder now sits beside `learn.html`.
- **Policy page drafts, Nov 13, in `docs/legal-drafts/`, nothing public.** Dourado asked for the
  reference site's policy pages to be studied and matched in our own words. Ten files by vc-copy:
  telehealth consent, health information and HIPAA, privacy choices, privacy policy changes, terms
  additions, refund additions, contact page, FAQ additions, About page, and a README with the
  questions for OpenLoop, the attorney and Dourado. Most wait on the attorney or OpenLoop papers.
  Contact, About and five FAQ answers are the nearest to ready. Categories on the reference site
  outside our six programs were not drafted; adding any is Dourado's decision plus written
  OpenLoop confirmation.
- **Live site problems found while drafting, not fixed yet.** `public/privacy.html` still
  describes our own intake questionnaire and Business Associate Agreements, which no longer match.
  `public/telehealth-consent.html` says starting a visit is consent to that page, but the binding
  consent is on the partner's intake. `public/script.js` would send the program name to Google on
  an intake click once real links go in; settle before the intake URLs arrive. "HIPAA-compliant
  platform" and "Shipping is included" have no written source.
- **Glutathione is back on the site, Dourado's decision in chat, Nov 13.** His words: "I would
  put glutathione back on the list. I'm pretty sure it's going to be on there." Basis: the OpenLoop
  rep named it as an Agile program on the Nov 12 call. Not in writing yet. It is the sixth program:
  its own page, home card, menu entry, intake button, sitemap entry, and a Style A label in
  `brand/label/`. CLAUDE.md and COMPLIANCE.md are updated. The older lines below that say five
  treatments, or glutathione off until written confirmation, are history.
- **What is placeholder on the glutathione page:** the form, which the copy leaves to the
  clinician on purpose because the demo showed a tablet and the old site said injection; the
  prices, $129 first month, $199 a month, 12-week $169 a month and $507 up front, copied from the
  NAD+ placeholder pattern, with $199 from `docs/pricing-research.md`; and the refill rhythm and
  video and support lines carried over from NAD+. Check all of it against the written Agile
  proposal, and take glutathione down if the proposal leaves it out.
- **Glutathione vial photo added Nov 13,** a Gemini edit of the NAD+ splash photo, vc-reviewer PASS.
- **Hero:** the five-vial marble group shot is the home hero, with one wrong digit on each label
  corrected by hand to 503A. vc-reviewer PASS.
- **Stopgap Shopify store and CSV:** the glutathione form wording there was made neutral, but the
  rest is still the old Asher-era store, old prices and the $20 fee. Never import the CSV or upload
  the theme as is.
- **Pushed Nov 13 on Dourado's "push it":** d5586e8 to b3098ae, ten commits, live on
  https://velacore-health.netlify.app. Verified: home, all six program pages, the four legal pages,
  FAQ and Learn return 200, the 404 page returns 404, the new hero and glutathione images load, and
  the live audit renders the Netlify home clean at 375 and 1280. velacorehealth.com is still the old
  Shopify store and still fails the audit: title My Store, broken policy links, missing disclaimers,
  old prices. That waits on the domain cutover or a Shopify fix.
- **Funnel rebuild, Nov 13, pushed on Dourado's "push it", b3098ae to 58f98d0, live on Netlify.** Verified live: home, Learn, FAQ, program pages, all six Start pages and the legal pages return 200, 404 returns 404, goal tile images load, Start pages carry no Google tag, and a phone visit from a program page with a utm tag lands on its Start page with the tag kept. Plan in `docs/funnel-plan.md`, copy in
  `docs/funnel-copy.md`. Home hero has one button, Find your program, to three goal tiles. Every
  Start visit goes to a per-program Start page, `public/start/<slug>.html`, generated by the build,
  noindex, no analytics, whose Continue button takes the Agile link from `audit-config.json`
  intake_links. UTM tags carry through. vc-reviewer PASS after two rounds.
- **Open decisions for Dourado:** Google Analytics on program pages and any tracking on Start
  pages, a health-privacy call; and a written source from OpenLoop for "Shipping included" before
  LegitScript. The Hormone support tile uses the sermorelin vial until its Gemini tile is made.
- **Explainer video:** Eric's calmer narration, music bed and Veo clips 1 and 2 are in
  `03-edits/peptides-video/`; clips 3 to 5 wait on the Gemini video limit. Decisions are in
  `docs/video-peptides-script.md`. ElevenLabs video needs their Pro plan; Dourado chose Gemini.

- **Domain moved Nov 13, on Dourado's word "move everything over", before the OpenLoop signing.**
  In Squarespace DNS for velacorehealth.com: the A record for @ changed from 23.227.38.65 to
  75.2.60.5 and the www CNAME from shops.myshopify.com to velacore-health.netlify.app. The five
  Google Workspace MX records and the verification TXT were not touched and were checked after.
  velacore.health: the Squarespace Defaults preset was deleted, A @ 75.2.60.5 and CNAME www to
  velacore-health.netlify.app added; Domain Connect and Email Security presets kept. In Netlify:
  www.velacorehealth.com is the primary domain, velacorehealth.com redirects to it, velacore.health
  and www.velacore.health are aliases. Let's Encrypt certificate issued, expires Feb 11 2027,
  renews itself. A redirect in netlify.toml sends velacore.health to www.velacorehealth.com, live
  after the next push. The Shopify stopgap no longer serves the domain; whether to close the store
  is Dourado's call. Decided Nov 13: Jonathan is closing the Shopify account. After it closes,
  `shopify-theme/`, `velacore-shopify-theme.zip` and `shopify-products-import.csv` are history; the
  site audit's stopgap store checks can be retired.
- **Google Search Console set up Nov 13** under firstventuregroupllc@gmail.com: Domain property
  velacorehealth.com, verified by a TXT record in Squarespace DNS, a second google-site-verification
  line next to the Workspace one. Never delete either. Sitemap https://www.velacorehealth.com/sitemap.xml
  submitted and accepted.

## Status as of Nov 12, 2026

Source: the Nov 12 OpenLoop call, Pocket recording in Dourado's personal Drive. Summary and
transcript were read in a scratch folder only; nothing from them is stored in this repo.

- **Platform decision changed: Agile, not Launchpad.** Bryan and Jonathan chose OpenLoop Agile at
  $1,000 total, paid as $250 a month, on the same 12-month term. Go-live can happen before it is
  paid off. This reverses the Nov 6 note below that Agile is rejected. Launchpad was offered with a
  lower integration fee, but the monthly fee would not move.
- **Go-live target:** the Monday or Tuesday after signing, built with JD at OpenLoop.
- **What Agile means for the site:** intake, cart, portal and card statement carry Agile branding.
  Ad tracking is basic UTM only, same as Launchpad. Agile gives an export and dashboards with name,
  email, phone, program, last medication, subscription status and billing dates, plus signup
  alerts. That export is patient data: it stays in OpenLoop's system and never comes into this repo.
- **OpenLoop promised to send, Nov 12:** the service agreement with the proposal as schedules, a
  refund policy, a telehealth consent and a privacy statement, dashboard screenshots, and an
  updated Agile proposal with every program and price. Nothing is confirmed until those arrive.
- **LegitScript:** OpenLoop gives a $3,000 coupon against the $5,625 LegitScript fee, invoiced
  within 15 days of asking. OpenLoop supplies its NPI and backend details plus a Q and A sheet and
  Slack help; Velacore files the application itself. Not needed to go live, needed before any ads.
  A website pre-check by OpenLoop was mentioned, unconfirmed.
- **Pre-intake email page:** Jonathan asked for a Velacore page that captures email before the
  Agile intake. OpenLoop's IT will say whether it works. Open question: it must collect contact
  details only, never health answers, or it breaks the no-PHI rule.
- **More programs:** OpenLoop says its whole Agile catalog is LegitScript compliant. That is a
  vendor claim, unconfirmed. On the call the partners leaned toward offering everything. The
  five-treatment rule in CLAUDE.md and COMPLIANCE.md still stands until Dourado decides in writing,
  OpenLoop confirms in writing, and vc-reviewer clears each new program. Two items are on hold, one
  by Jonathan and one by OpenLoop. Names stay out of this repo.
- **Site plan switched to Agile, Nov 12, on Dourado's word.** What that means, in order:
  1. Prices: on Agile OpenLoop sets the retail price. Every price on the site today, the $129 first
     month and the monthly prices, is our own Launchpad-era plan and stays a plan until the updated
     Agile proposal arrives. Then the program data in `tools/build_programs.py` changes once and
     the build carries it everywhere. Do not guess Agile prices.
  2. Start visit buttons: each one links to that program's Agile intake URL, which JD supplies.
     The buttons are already wired by program through `data-intake`; the URLs go into
     `.claude/skills/vc-site-audit/audit-config.json` and the build.
  3. Hand-off message: because the Agile intake shows Agile's name at the top, the intake section
     should tell patients they finish on the partner's secure pages and that the partner's name
     appears there and on the card statement. The site already says partner and card statement in
     general terms. Whether to name Agile publicly waits for the signed agreement, then vc-copy
     writes it and vc-reviewer checks it.
  4. Pre-intake page: only if OpenLoop's IT says yes, and only name and email, no health
     questions. Until then, no form on our site.
  5. Legal pages: refund, terms, privacy and consent get rewritten against the documents OpenLoop
     is sending, then vc-reviewer.
  6. Ads: Agile gives UTM tracking only, no pixel on the intake. vc-ads plans measurement around
     clicks on our own pages; any tracking on our pages goes through a health-privacy check first.
  7. Domain cutover and the Shopify stopgap still wait for the signed agreement.
- **Glutathione:** on the Nov 12 call the OpenLoop rep named glutathione as one of Agile's
  longevity programs, alongside NAD+ and sermorelin. Verbal only. Superseded Nov 13: Dourado put it
  back on the site without waiting; see the Nov 13 block.
- **Other facts from the call:** sync video is required in about 7 states and the intake handles
  it. Some customer service is offshore. OpenLoop does no marketing. Asher notice is given and ends
  after the first of the month. The OpenLoop rep liked the splash vial photos.

## Status as of Nov 6, 2026 (read this before the older sections)

- **Decision direction: move to OpenLoop Launchpad**, conditional on written answers from OpenLoop
  (ad pixel / post-payment redirect, the 10-patient fee rule, shipping included, glutathione, the
  MSA + BAA + SOC 2 with liability and LegitScript ownership written in). A confirmation email is
  drafted (see the conversation summary in `docs/openloop-call-guide.md` and the comparison doc);
  Bryan is sending it from firstventuregroupllc@gmail.com. Fee negotiation (start the 10-patient
  clock at LegitScript approval, or cap at two months) is deliberately held until the agreement
  arrives.
- **Shareable comparison for partner Jonathan Moss:** Claude Docs page "Asher vs OpenLoop
  Comparison" at https://claude.ai/artifact/SUTyr2Rwr6srVEEa6jUsVX (two tabs: Comparison, Asher
  support exchange). Private until Bryan shares it.
- **Pricing strategy: volume over price.** Launch prices in `docs/pricing-research.md`: first month
  $149 (sema) / $199 (tirz); month-to-month $229 / $279; 12-week plan $199 / $249 per month as the
  default; microdosing GLP-1 $179 as the cheap tier; NAD+/sermorelin $199. A/B test $199 vs $229
  for 60 days in Launchpad before moving lower. The Shopify theme and product CSV still show the
  OLD prices ($299/$349 etc.) and need updating once the platform is chosen.
- **Asher cancellation submitted Nov 6, 2026** through Asher's Subscription Center. The billing
  cycle runs through December 1, 2026, no balance is owed, and full portal access continues until
  then. Current patients can continue GLP-1 care directly under Asher through Asher's text line.
  Asher does no bulk export of patient records; non-PHI admin records must be saved by hand from
  the portal before Dec 1. See open items 11 and 12.
- **Ads are the only pipeline.** LegitScript is required before any Meta/Google ads; on OpenLoop it
  is $3,000 flat, 2–4 weeks, in Velacore's name, portable. Agile (the $1,000 tier) is rejected: no
  pixel, fixed price, Agile branding on card statements, no migration to Launchpad.
- **Build mode next:** once the platform is signed, the site needs: new prices, product-page
  "Start visit" links pointed at OpenLoop's hosted intake (per product), a patient-portal link,
  refund/terms/provider pages rewritten for OpenLoop's model (no $20 fee; OpenLoop providers),
  the FDA/compounded disclaimer kept, then ad creative and landing pages for the $149 first-month
  offer.
- **Local agent set up, Nov 6.** The repo now lives directly in `C:\Users\Dourado\Documents\Velacore Health`,
  no Velacore subfolder. The four video folders 01-raw-clips to 04-scheduled sit in the root and are
  gitignored. Repo git identity is set. `.env` exists and is gitignored. `.claude/settings.json` deny
  rules carry both the `C:/` and the `//c/` path forms; verified Nov 6 that they block, by reading
  a made-up filename under Salvage Health and getting a permission refusal. First
  project skill `vc-compliance-check` is built. First run: 0 fail, badge off, disclaimer present, the
  CSV has only the five products. Memory is seeded: agent name, report format, one step at a time,
  install rule. Not done yet: `vc-site-audit`, the optional `vale.md` agent file, and the GitHub CLI,
  pandoc and Shopify CLI installs. Local commits aren't pushed; a push to this branch deploys
  `public/` to GitHub Pages.
- **Platform decided, Nov 6 (Dourado, in session).** Asher is canceled and the partnership is over.
  OpenLoop is the platform. JotForm is retired. The plan is the same shape as salvagehealth.com:
  the static site in `public/`, which Vercel already serves at https://velacore.vercel.app, is
  the foundation to build on; the velacorehealth.com domain moves to Vercel; and every treatment's
  Start visit button links out to that treatment's OpenLoop hosted intake page. Dourado also has
  a Netlify account from Salvage Health, but Vercel is already set up, so it stays. The current
  live site is a copy-and-paste Shopify store running the Velacore theme; it is a stopgap until
  Vercel serves the domain. Open items 1 to 4 and 7 above are now moot or rewritten by this.
- **`vc-site-audit` built, Nov 6.** First run against the live store found: page title "My
  Store"; the footer links to telehealth consent, refund policy and terms all 404; none of the
  five live product pages carries the FDA compounded-medication disclaimer, so the live product
  bodies are not the CSV bodies; all surfaces show the old prices ($349/$299/$279/$199/$329)
  against the planned $279/$229/$199/-/$199; `public/telehealth-consent.html` has no state
  complaint directory at all, so the "about 25 states verified" note in open item 6 is stale;
  `public/index.html` still has the JotForm embed, the $20 physician fee wording and the
  hello@ placeholder email. Reports and screenshots land in `_audit/`, gitignored.
- **Setup facts from Kevin, Nov 6.** GitHub is plain git over HTTPS with the Windows credential
  manager; no GitHub CLI. The Velacore-Health GitHub org has a 2FA deadline of Nov 24, 2026;
  Dourado does that himself. Google connectors take one account at a time and it is
  bryandourado@gmail.com, so the Velacore inbox firstventuregroupllc@gmail.com is not readable by
  the agent; Dourado can forward it into the main Gmail or reconnect the connector to the Velacore
  account. Vercel is not connected yet; the official Vercel connector is the way in. Deploy
  practice to copy from salvagehealth.com once Vercel deploys from git: working checkout's push
  URL disabled, deploy from a clean worktree, one push only after Dourado says "push it".
  The OpenLoop proposal PDF is in Dourado's Downloads; pypdf 7.0.0 is installed and it has been
  read. Patient-facing terms and prices are in `docs/openloop-proposal-notes.md`; the column of
  what Velacore receives stays out of the repo. Three facts from it change the site: no separate
  physician fee and refund for any reason except a month already ordered; providers are OpenLoop's
  MD, DO and NP network, 7am to 7pm CST, with live video required for the first prescription in
  AR, DC, DE, KS, MS, NM, RI, WV; payment is Visa, Mastercard, FSA/HSA, Apple Pay, Google Pay, no
  Amex. Unresolved in writing: the proposal says intake and card entry happen on Velacore's
  interface, while the demo said Launchpad hosts them; the site plan assumes the hosted version.
- **Team built, Nov 6.** Project agents in `.claude/agents/`: `vc-ads` with its `vc-ads` skill
  for Meta and Google, `vc-copy`, `vc-reviewer`. See the Team section in CLAUDE.md.
- **Decided Nov 6 by Dourado:** the site sells four plus microdosing: tirzepatide, semaglutide,
  microdosing GLP-1, NAD+, sermorelin. Glutathione is off until OpenLoop confirms it in writing.
  Dr. Broussard's section is replaced by OpenLoop network copy with no named clinician. Still
  open: the Velacore inbox connection and the Vercel connector.
- **Brand bible started, Nov 6:** `docs/BRAND.md` and `brand/velacore-brand-card.png`. The logo
  is a helix-and-leaves mark in a ring, violet to blue on the full logo, jade on the mark; the
  program cap colors come from it. Only two small PNG logo files exist, 317 and 119 pixels;
  Dourado to find the designer's source file for `brand/logo/`. Gemini's first two vials from
  the brief came out on-brand. Dourado also asked for agent access to the
  firstventuregroupllc@gmail.com Drive, Photos and Gmail plus a local synced drive; the
  connectors hold one Google login, so the route is sharing the Velacore Drive folder to the
  connected account, Gmail delegation or forwarding, and Google Drive for desktop syncing a
  Velacore folder into this project. Steps given to Dourado; none done yet.
- **Kevin's home page review applied, Nov 6.** Kevin, the Salvage Health agent, reviewed the
  home page against `docs/how-dourado-judges-design.md` and scored it 7 of 10 with 14 items.
  Applied: sticky phone CTA only after the hero scrolls off and never over the start section;
  hero frame sized at phone width so the trust strip clears it; contrast fixed with jade ink
  #0A7A61 for buttons and links and #5F716A fine print, now in BRAND.md and on the brand card;
  steps one column under 600px; non-breaking hyphens in Microdosing GLP-1 and nowrap on the
  coming-soon suffix and footer links; every eyebrow label removed from the home page and the
  decorative ones from program pages; hero chips removed; the crumpled-paper tile and the shield
  replaced by the logo mark; width and height on every image; 44px tap targets. The audit now
  measures text contrast and tap targets on the home and one program page at 375 and 1280; both
  pass. Not done: generating the home cards from the program data so prices cannot drift. Kevin
  rechecked and scored 8.5 of 10 with five misses, all fixed the same hour: coming-soon label on
  its own line in the visit panel, logo tile on the microdosing card, sizes on all 12 home images,
  44px tap targets everywhere with the audit threshold raised to match, and a stray copy of the
  Treatments dropdown removed from the footer. Kevin also brought deploy questions from Dourado;
  answered from the repo only. Unconfirmed, for Dourado to read off the Vercel dashboard: whether
  the Vercel project auto-deploys from GitHub, which plan it is on (Pro is needed for a commercial
  site), and that only velacore.vercel.app is attached. `docs/DEPLOY.md` is to be written once
  those three are confirmed. Kevin also delivered a phone-only card carousel component, saved on
  the Desktop as `velacore-carousel-component.html`; not added, waiting for Dourado to confirm he
  wants it and whether flat or 3D. Separately,
  Dourado judged Gemini's first vial "pretty basic"; next is a real label artwork file the
  prompt can carry, plus his Gemini Deep Research findings when he pastes them.
- **Carousel and workflow, Nov 6, evening.** Dourado chose Kevin's 3D card carousel for the
  home page; it is in, phones only under 760px, follows the category filter, desktop keeps the
  grid. Kevin sent the full Salvage Health deploy loop; `docs/DEPLOY.md` draft v1 mirrors its
  headings with three UNCONFIRMED lines for the Vercel dashboard. Dourado's new rules: Velacore
  works exactly like Salvage Health with Kevin as the reviewer, same three words show me, push it,
  undo; nothing on a free plan; connectors and skills for Google Ads and Meta ads to be planned
  before LegitScript clears. Kevin recommends Netlify over Vercel for one dashboard; decision is
  Dourado's. `docs/gemini-deep-research-prompt.md` holds the Deep Research prompt for the vial
  label and photography research; Dourado is being walked through Gemini one step at a time.
  Kevin's parity checklist, `C:\Users\Dourado\Desktop\vicky-parity-checklist.md`, was read and
  answered: Velacore already has CLAUDE.md, DEPLOY.md, the audit, the compliance check, the brand
  guide, memory and deny rules; missing are the business Google account on the connectors and a
  host decision. Host terms were read and recorded in `docs/DEPLOY.md`: Vercel Hobby forbids
  commercial use, Netlify's policy has no pharmaceutical clause and only bars stored PHI without
  a BAA, which this site never holds. Kevin now stays on Salvage Health; anything from his side
  goes through Dourado.
- **Vial labels and caps, Nov 11, Dourado's choices.** Gemini's first splash edit rewrote the
  label as research-use wording, rejected. Velacore now owns exact label artwork:
  `brand/label/label-<program>.png`, made by `brand/label/make_labels.py`, Style A pine band
  picked by Dourado. Every vial cap is deep matte pine; the program color is only the label's
  thin line and dash. Vial prompts in `docs/gemini-prompts.md` start a fresh chat, attach the
  label, and ask for a camera slightly above so the label curves with the glass. All five
  splash vials are on the site, local only: product cards and program photos are 4 by 5,
  full-bleed, and the microdosing card and menu item now use its photo. vc-reviewer blocked the
  first pass because a branded vial can read as Velacore making the medicine; fixed with a
  visible line, "Illustrative image. Your medication is prepared and labeled by a licensed 503A
  pharmacy and may look different", under each program photo and in the home treatments note.
  Open question for OpenLoop: do dispensed vials carry Velacore branding. Ads that use these
  images need vc-ads to check Meta and Google AI-image rules first.
- **Lifestyle photos done, Nov 11.** How it works steps 1 to 3 carry the online visit, the
  clinician call and the delivery photos; a full-width walk band with the couple and their
  Australian shepherd sits after the Learn teaser. The delivery box is plain: an AI-drawn
  Velacore mark was blocked by vc-reviewer because shipments come from the pharmacy. People
  photos now lean to the late thirties and forties, per Dourado. Also fixed: the tablet nav
  switches to the menu button below 781 px, and the phone Treatments list no longer shifts off
  the left edge, a bug that was live on phones. vc-reviewer PASS on both batches, vials and
  lifestyle. Patient portal links removed everywhere until a member login exists, per Dourado.
  Pushed Nov 11 on Dourado's "push it", 22 commits, 9cfe230 to d5586e8; Netlify live within a
  minute; key pages 200, 404 page 404, live audit renders Netlify clean at 375 and 1280.
  Originals still to copy to the business Drive under 01-brand.
- **Live Shopify store, still on velacorehealth.com, fails the live audit, Nov 11.** Title is
  "My Store", three policy links 404, the FDA disclaimer is missing on four product pages,
  prices are the old ones, and one live product is outside the approved five. Fixing it needs
  Dourado in the Shopify admin, or the domain cutover to Netlify, which retires the store.
- **Other OpenLoop products, Nov 11.** Dourado reports OpenLoop said everything they offer is
  fine. Not in writing yet, so unconfirmed. He asked about three more categories: an oral form
  of an approved program, a men's health category, and a controlled-substance hormone therapy.
  Advice given: written list from OpenLoop first, then a sourced check of each against
  LegitScript, Google and Meta rules before any goes public; the controlled-substance category
  stays off the public site until counsel or OpenLoop compliance confirms in writing. Nothing
  added, and no product outside the approved five is named in this repo.
- **Image direction changed, Nov 11, at Dourado's direction.** More people and healthy everyday
  routines, vials in clear splashing water, so the site reads as health and wellness. BRAND.md
  section 5 rewritten with the guardrails: adults 35 to 60, ordinary builds, everyday activity,
  never scales, tape, mirrors, gyms, needles, pills or anything presenting a person as a patient.
  `docs/gemini-prompts.md` is set 2: one hero, five splash vials made by editing the existing
  vial photos so the labels stay exact, three how-it-works scenes and one outdoor walk, with a
  reject list. `tools/prepare_images.py` now also converts `assets-in/lifestyle/`. Seven unused
  public images were removed, among them glutathione.webp and dr-broussard.webp, which named an
  off-site treatment and the former physician in a served folder. Slots get wired as each image
  arrives: hero frame, product cards and program pages, a picture on how-it-works steps 1 to 3,
  and a full-width walk band.
- **Home page cut down for ad traffic, Nov 8, at Dourado's direction.** The home page was one
  continuous scroll, about 16,000 px on a phone. Now about 11,800: the peptide explainer moved
  to `public/learn.html`, the full 15-question FAQ and its FAQPage schema moved to
  `public/faq.html`, the home FAQ keeps six answers plus a link to the rest, the Why Velacore
  pillars and the clinicians block are one section ending in a Start your visit button, a short
  "New to peptides?" band links to the explainer, and the hero buttons are Start your visit and
  See programs and prices. Every section now ends in a next step. Nav, footer, legal pages, the
  program page generator and the sitemap point at the new pages; the sticky phone button shows
  on pages without a hero. No copy rewritten beyond button labels. Compliance 0 fail, audit
  clean at 375 and 1280, no broken anchors. vc-reviewer run before showing Dourado. Not pushed.
  Follow-ups for vc-copy: a shorter hero lede, and a price line under the hero buttons drawn
  from the program data rather than typed.
- **First Netlify deploy, Nov 8.** Dourado granted the Netlify GitHub app access to the Velacore
  repository, created project velacore-health in his team from branch
  claude/velacore-health-website-qnjdnh with publish directory public and no build command, and
  said push it. Vale pushed 17 commits, 71e89db to 2d13286, the GitHub Pages workflow was removed
  in that batch, and Netlify rebuilt to ready. Test address velacore-health.netlify.app; the
  project is Private on Netlify, so it asks for a Netlify login until Dourado clicks Make public.
  Noted on the way: the Velacore GitHub repository is public, so docs/ is readable by anyone;
  recommend making it private, Netlify works with private repositories. GitHub two-factor
  deadline reads Nov 23 on GitHub's own banner. Next: Dourado checks the test address on his
  phone, Make public when ready, audit against the live address, then the domain only after
  OpenLoop and his word.
- **Host and domain, Nov 6, night.** Dourado chose Netlify. velacorehealth.com is registered at
  Squarespace with DNS on Google Cloud DNS, web records on the Shopify stopgap, MX on Google
  Workspace with three live mailboxes, jonathan@, bryan@ and hello@. Domain plan and Dourado's
  clicks are in `docs/DEPLOY.md`. Kevin has stepped back to Salvage Health; Vale now guides
  Dourado directly, one step per message. Dourado is asking Jonathan for contributor access to
  the Squarespace domain. Netlify project creation is in progress with Dourado at the screen.
- **Four approvals done, Nov 6, night, on Dourado's "Yes to all four" in chat.** Connectors
  off for this project: Gmail, Drive, Calendar, PostHog, Kit, Metricool; on: Canva, Claude Docs,
  Netlify. CLAUDE.md gained Deploys cost money, Design checklist, Build and Audit. Weekly
  read-only audit scheduled as app task `vc-weekly-audit`, Monday 8 AM, next run Nov 9. Commits
  d32b650 and d35191e made locally; branch is 12 ahead of origin, nothing pushed. The connector
  switch proved account-wide and broke Kevin's session, so the six Salvage Health connectors are
  instead denied by tool name in `.claude/settings.json`, commit 257bb2a, tested with a refused
  Drive read; Dourado restored the shared switch himself, item closed. Kevin now
  coordinates and reports to Dourado; Vale reports to Kevin. Open for Dourado: the host choice,
  then the first push through one publisher.
- **FVG Drive cleanup, pass one, Nov 6, evening.** Dourado said yes in chat to reading and
  cleaning the business Drive. Inventory taken read-only: 9 folders and 8 loose Asher-era files in
  the root, and the designer's logo package with .ai, .eps and .svg found at Logo / VelaCore
  Health_FF / Logo. Pass one applied through the Drive web interface: eight numbered folders
  created per `docs/folder-map.md`, the 7 Asher files moved to 06-vendors/asher, the shared
  Social Media Profiles doc moved to 04-marketing and still shared, nothing deleted, renamed or
  opened. The inventory and the move manifest with the undo table live in `_private/`, which is
  gitignored because vendor file names stay out of the public repo. Not done: the root map file
  inside the Drive, moving the nine old folders under their numbers, renames.
- **Logo source downloaded, Nov 6, on Dourado's OK.** 13 files, 2.4 MB, into `brand/logo/`,
  .DS_Store left out, zip stays in Downloads. Three versions: 01 gradient mark with white
  wordmark, 02 all white, 03 all black, rasters 1507 by 1135, vectors .svg .ai .eps in 01. Real
  gradient stops are mint #78CBA9, blue #3A8EC6, magenta #DD25DA, not the violet-to-blue the
  bible guessed; BRAND.md sections 1, 2, 7 and 8 updated. The site's logo-full.png and jade
  logo-mark.png are derived files, now labeled as such. Open: whether the light-ground
  gradient-plus-black version the site uses is approved, Dourado's call. Not committed.
- **Business inbox route and Kevin's six fixes, Nov 6, late.** Dourado OK'd reaching
  firstventuregroupllc@gmail.com through Claude in Chrome. Checked read-only: both connected
  Chrome browsers show bryandourado@gmail.com as the first account; the business account is the
  second account in the same Chrome, index 1. Verified read-only: Gmail, Drive and Calendar at
  /u/1/ all open as firstventuregroupllc@gmail.com. The route works; no mail content read yet. Netlify has one team, Personal, owner
  bryandourado; Velacore would share its credits with Salvage unless it gets its own team.
  Kevin's optimization list: do not push until the host is chosen and the second publisher is off
  (10 local commits are unpushed); trim connectors to what Velacore uses; Bash deny rules already
  block the other business folders, verified by a denied cat of a made-up file; add Deploys cost,
  Design checklist, Build and Audit sections to CLAUDE.md; propose a weekly read-only audit; vet
  method for installs now in `docs/installs.md`. The CLAUDE.md change, the connector trim and the
  weekly audit wait for Dourado's word.
- **Restyle, Nov 6, at Dourado's direction: light, not AI-looking.** `styles.css` rewritten:
  white and mint-white sections, pine ink, jade for actions, Fraunces for headlines, the real
  vial as the hero, each program's vial-cap color as its stripe, one dark band for the promise.
  Removed: the floating-dot canvas, glow gradients, glass chips, button arrows, all-caps labels,
  numbered-step chrome, fade-ins and hover lifts. Product images now read from
  `public/images/products/<slug>.webp`; Dourado will generate branded vial and bottle images in
  Gemini from `docs/image-brief.md`, drop them in `assets-in/products/`, and
  `tools/prepare_images.py` converts them. The hero frame is the image slot for a lifestyle
  photo later. Dourado also asked what design skills the agent lacks; the Anthropic Design plugin
  and the design-skills plugin were suggested for critique and visual elevation.
- **Program pages built, Nov 6.** `public/programs/` has one page per program, generated from
  `tools/build_programs.py`: hero with price box and plan selector for month to month and the
  12-week plan, disclaimer under the price, trust bar, what the medication is, eligibility, the
  four-step journey per OpenLoop's notes, FAQ, start section. Home page cards now link to them and
  show the first-month price on every program; the header has a Treatments dropdown with
  thumbnails grouped Weight, Vitality, Hormone support, on every page. Sitemap lists the five
  clean URLs. Start buttons are still placeholders. Dourado's read of arsynl.com: he likes the
  dropdown, the rolling strip, the category grid, the form comparison table and the lifestyle
  imagery, which he will make with an image tool; and he wants our prices studied against theirs,
  see the price table in `docs/reference-arsynl.md`. Not built yet from that list: category grid,
  form comparison table, hero image slots, FAQ and Contact pages, About, blog.
- **Reference site reviewed, Nov 6:** arsynl.com, see `docs/reference-arsynl.md`. Same shape as
  our plan: marketing site, hosted intake on a branded subdomain. Proposed next build: one page
  per program, trust bar, portal icon, FAQ and Contact pages, symptom section, About, blog.
- **Site overhaul for OpenLoop, Nov 6, in `public/` only.** `index.html`: five program cards
  with the planned launch prices ($199 then $279 tirzepatide, $149 then $229 semaglutide, $179
  microdosing, $199 NAD+ and sermorelin, 12-week plan line on each), OpenLoop's four-step journey,
  clinician network block, cancel-any-time promise, FAQ rewritten for the OpenLoop terms (fees,
  payment methods, eligibility, labs, 24/7 support, video-visit states), JotForm removed, intake
  section is now one button per program plus a patient portal link, all `href="#"` with
  `data-intake` and `aria-disabled` until OpenLoop sends the hosted URLs; `script.js` blocks the
  placeholders and fires a GA4 `start_visit_click` event on real links; `styles.css` has the new
  plan line, button stack and placeholder styles. `refund-policy.html` rewritten in full.
  `terms.html` sections 3, 4, 7 and 10 and `telehealth-consent.html` updated. "Physician" became
  "clinician" where OpenLoop's NPs apply. Wording avoids naming OpenLoop on the site: it is "our
  telehealth services partner" until Dourado decides whether to name them. Audit after: 0 fails
  except the placeholder links, which are meant to fail until the URLs exist. Shopify theme and
  CSV untouched; they are the stopgap and still show the old prices. Nothing deployed.

## Open items

1. **OpenLoop call held Nov 2; follow-up demo Wed Nov 4, 12:30 PM CST** (partner Jonathan Moss joins;
   OpenLoop to send a proposal + full medication menu first). Findings from the transcript:
   - Two paths. **Launchpad:** 2–4 week launch, white-label branded intake, 3–4 programs, limited API,
     no Meta/Google pixel yet (basic UTM only), limited data export. **Traditional:** 4–8 weeks, only
     1–2 programs, heavy dev lift, needed for real analytics/TRT.
   - **OpenLoop is merchant of record (Stripe)** and says compliance/breach risk is theirs (verbal only).
     They say LegitScript is needed only to advertise, not to take payments.
   - Fees quoted: **$6,000 integration** ($3k at signing, $3k at first patient OR 90 days, whichever
     first, so owed regardless of volume), **$3,000/mo subscription waived once 10 active patients**,
     fixed all-in medication cost per product (the rep's "$90 for GLP-1s" was only an EXAMPLE, not a quoted
     price; Bryan hasn't seen the real price sheet yet, so per-patient cost vs Asher is unknown). LegitScript package **$3,000 flat**, "2–4 weeks", self-serve.
   - Contract: standard 1 year, "non-binding" with 60-day notice (confirm in the agreement).
   - Products: tirzepatide, semaglutide (+ microdosing), NAD+, sermorelin, B12 mix. **Glutathione NOT
     available yet** ("coming"). Labs not available yet. The restricted peptide catalog is NOT offered
     (they advise waiting on an FDA decision and not selling them anywhere tied to the brand).
   - The friend's deal (about $250 start, no monthly fee, $2,500 LegitScript) is OpenLoop's "Agile"
     affiliate model: no pricing control, one set of intake forms, communications likely under Agile's
     brand, little analytics. OpenLoop reps said they'd look at replicating what the friend got for
     Bryan. **Leverage point:** ask for branded comms + pricing control on Agile terms, the $2,500
     LegitScript price, the monthly cost, per-patient commission, and the upgrade path. Also ask the
     friend what he actually gets.
   - **Transcript caveat:** the transcript came from an AI note-taker (Pocket) and mis-hears names and
     numbers (it rendered "Velacore" as "Bellatore/Bellacore", "Meta" as "Medela", and garbled the
     medication price between $90 and $190). Treat every figure above as unconfirmed until it appears
     in OpenLoop's written proposal; the call audio is in Bryan's export if a number needs checking.
   - **Written proposal received (dated 11/02/26, expires in 30 days; PDF kept out of the repo).**
     $6,000 implementation ($3k at signing, $3k at first patient live or day 90, whichever is
     sooner); $3,000/mo until 10 patients (clock starts at go-live); 12-month term, 60-day notice
     for any reason. OpenLoop is merchant of record and pays meds, labs, pharmacy, 24/7 support;
     it remits Velacore's "membership services fee" weekly (Wednesdays). Example prices
     (patient pays → Velacore receives, per 4 weeks): semaglutide injection $209 → $114–119;
     tirzepatide $249 → $107–129; NAD+ and sermorelin $229 → $130; microdosing GLP-1 $179 → $90;
     B12 MIC $145 → $70. OpenLoop keeps about $90–95 (semaglutide), $120–142 (tirzepatide), $99
     (NAD+/sermorelin). Proposal marks all prices "an example, subject to change"; availability
     can change "at any time, with no notice."
   - Other terms: LegitScript via OpenLoop $3,000 flat, expedited (alone: $975 + $2,150, or $5,625
     with expediting; renewal via OpenLoop $2,000). **Glutathione is NOT included.** Patient
     refund policy is more generous than ours (any reason, except a month already ordered) and
     there is no separate $20 physician fee, so our legal pages and provider section would need
     rewriting. Optional +$10/patient/mo "care coaching" (keep off; we removed coaching language).
     Sync-video states for first prescription: AR, DC, DE, KS, MS, NM, RI, WV. Providers 7am–7pm CST.
   - **Unresolved in the proposal:** it says Velacore provides the patient interface, credit-card
     entry and API connection (a Traditional-style build, with PHI/PCI burden on us), while the
     call described white-label hosted forms (Launchpad); BAA, indemnity and breach liability are
     not in it (MSA unseen); whether Velacore can set its own retail price above the example and
     whether OpenLoop's cut stays fixed; what counts toward the "10 patients."
   - **Nov 4 demo (Launchpad vs Agile) findings** (from the call transcript):
     - **Launchpad** = hosted, Velacore-branded intake/refill forms and patient portal on masked
       Velacore URLs. Velacore only places per-product "Start Visit" links and a portal link on
       its own site (our Shopify theme already supports a per-product intake URL); it does NOT
       build the card interface. OpenLoop runs 24/7 customer service. Retail price is Velacore's
       to set within min/max guardrails, with live coupons, price history and A/B funnel tests.
       No per-program profit view. OpenLoop's prices are all-inclusive (no separate $20 fee).
     - OpenLoop is merchant of record on Stripe, paying out net-7 weekly. Disputes/chargebacks are
       theirs (verbal only; not yet in writing).
     - **Agile** = $1,000 TOTAL (or 4 x $250), no monthly fee. Co-branded: intake, cart, portal
       and card statement all say Agile. Retail price fixed, no UTM/Google/Meta pixels, redirect
       only. **No migration from Agile to Launchpad** (separate EHR; patients must re-sign up).
       The friend's "$250" is the first of four payments. OpenLoop offered Agile, not a hybrid.
     - Monthly-fee deferral refused. The $3,000/mo starts at the first patient and drops to zero
       at 10 (threshold was recently lowered 30 -> 20 -> 10). "10 patients" is still undefined.
     - LegitScript via OpenLoop: $3,000 flat incl. expedite, 2-4 weeks. Not needed to go live,
       needed to advertise. Certification stays with Velacore if it leaves (update profile with
       new NPI/backend); $2,000/yr renewal. They give feedback but won't rewrite the site;
       Launchpad includes pre-vetted product descriptions and FAQs.
     - Glutathione showed up in the demo instance (a dissolvable tablet), contradicting both the
       earlier call and the proposal. Confirm availability and form.
     - Bryan screen-shared Asher's partner pricing/markup tool with OpenLoop. Check the Asher
       agreement's confidentiality terms and don't share more.
     - Contract 12 months; notice is 60 days per the proposal (transcript says "sixteen-day",
       likely a mis-hearing). OpenLoop will email to reconnect end of week or early next Monday.
   - Bryan screen-shared Asher's dashboard (including his cost prices) on the call. Check the Asher
     agreement for confidentiality terms and don't repeat it on Nov 4.
2. **BAA with Asher is UNRESOLVED.** Asher softened from "embedded in the agreement" to "documentation
   doesn't confirm." Get section numbers or a standalone BAA in writing; have it reviewed.
3. Read the Asher Sign-Up Agreement (signed 03-02-2026) for termination, exclusivity and non-compete
   terms before any switch.
4. Ask Asher whether the "final approval" step applies to hosted-link orders (so payment can be
   confirmed before approving).
5. Domain flip: velacorehealth.com from Squarespace → Vercel or Shopify (not done).
6. Finish the 50-state provider-complaint directory on `telehealth-consent.html` (about 25 states
   verified from official sources so far: AL, AK, AZ, AR, CA, CO, CT, DE, DC, FL, GA, HI, ID, IL, IN,
   IA, KS, KY, LA, ME, MD, MA, MI, MN, MS). Verify each from an official source; don't type from memory.
7. Rebuild the JotForm shorter (3 pages, ~9 fields, hidden `product` field).
8. Jonno's fixes to SOP-01/02 (see `docs/sops/REVIEW-NOTES.md`); attorney or consultant review.
9. Gated member area for restricted products needs real server-side auth (not built).
10. Confirm the Shopify theme uploads and renders; products imported; Treatments collection set.
11. **Before Dec 1, 2026:** save the Asher order history and the patient contact list by hand from
    the Asher portal. Asher offers no bulk export and access ends with the billing cycle. Keep
    non-PHI admin records only, outside the repo.
12. **Before Dec 1, 2026:** get the OpenLoop agreement signed early enough for Launchpad to be live
    before Asher access ends, so current patients have somewhere to go. OpenLoop quoted 2 to 4
    weeks to launch; the proposal expires about Dec 2.

## Accounts and tools

- Business email: firstventuregroupllc@gmail.com. The Gmail connector in the old cloud session was tied
  to bryandourado@gmail.com (Salvage Health mail), so Velacore drafts went there for copy/paste.
- Bryan's other business (Salvage Health) is separate. Don't mix it in.
