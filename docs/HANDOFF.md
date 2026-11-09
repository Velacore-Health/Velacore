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
