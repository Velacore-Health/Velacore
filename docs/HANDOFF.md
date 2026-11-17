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
