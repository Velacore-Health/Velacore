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
   - The $250 friend pricing is OpenLoop's "Agile" affiliate model: cheap, but no pricing control, one
     set of intake forms, communications under Agile's brand, little analytics.
   - **Transcript caveat:** the transcript came from an AI note-taker (Pocket) and mis-hears names and
     numbers (it rendered "Velacore" as "Bellatore/Bellacore", "Meta" as "Medela", and garbled the
     medication price between $90 and $190). Treat every figure above as unconfirmed until it appears
     in OpenLoop's written proposal; the call audio is in Bryan's export if a number needs checking.
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

## Accounts and tools

- Business email: firstventuregroupllc@gmail.com. The Gmail connector in the old cloud session was tied
  to bryandourado@gmail.com (Salvage Health mail), so Velacore drafts went there for copy/paste.
- Bryan's other business (Salvage Health) is separate. Don't mix it in.
