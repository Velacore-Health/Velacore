# Velacore Health — Website Compliance Notes

This records the compliance decisions baked into the site so they aren't accidentally undone.
It is **not legal advice.** Your own guide recommends a LegitScript pre-submission audit
(White Label MD / Bloom Consulting) and a healthcare attorney — do that before submitting.

## Positioning model (the core rule)

Velacore is presented **only** as a **telehealth coordination platform** — never as a provider,
prescriber, medical practice, or "wellness/health coaching" company. It **coordinates access** to
**independent licensed physicians** and **503A compounding pharmacies**. **All medical decisions
are made solely by the independent provider.**

## Approved copy embedded verbatim (from the launch brief)

| Location | Copy |
|----------|------|
| "Please note" disclaimer (`.please-note`) | Full approved paragraph — coordination platform, no medical services/prescriptions/treatments, decisions solely by the independent provider. |
| Footer first sentence | "…telehealth coordination platform that provides structured wellness resources and coordinates access to independent physician-directed programs." |
| States served (footer + topbar) | "…available to residents of select US states. Contact our care team to confirm availability in your state." |
| Refund / guarantee (`#guarantee`, Step 05, FAQ) | Full refund incl. physician review fee within 15 days if not approved; medications non-returnable once dispensed. |
| How it works — Step 00 | "Start with a free Velacore wellness evaluation…determines the right program path before any medical review." |
| Independent Physician Access (`#access`) | "…may be eligible for a courtesy referral to an independent, licensed healthcare provider…" |

## Deliberately NOT on the public site

- **No DEA numbers / confidential underwriting data.** The Payment Processing Guide is marked
  "Confidential · Not for redistribution," and DEA registrations are not public. That packet is for
  payment-processor underwriting only — never publish it.
- **No health / efficacy / outcome claims** anywhere (programs use neutral, descriptive language).
- **No "wellness coaching" / "health coaching"** in copy, meta description, or meta keywords.
- **No medical-director claim.** Dr. Broussard is shown as an *independent* prescribing provider.
  The medical-director relationship still needs a signed agreement + attorney review (per the
  brief), so the site neither asserts nor denies that role.

## Still required before LegitScript submission (from your brief — not code)

- [ ] Site fully public (remove password) before the LegitScript scan.
- [ ] Confirm the real **states-served list** from Asher Med and replace the placeholder line.
- [ ] Confirm **pharmacy routing** (Kaduceus vs. Greenville — Greenville is TX-only).
- [ ] Signed **Medical Director Agreement** (Dr. Broussard) + attorney review of provider language.
- [ ] 5 written SOPs, BAAs (JotForm, Tidio, email, Airtable), pharmacy license + fulfillment agreement.
- [ ] Legal pages: Privacy, Terms, Telehealth consent (footer links are stubs).
- [ ] Replace placeholder programs/pricing with your real lineup — keep language claim-free.
- [ ] Wire the CTA/form to your JotForm "Find Your Protocol" evaluation.

## Image slots to fill (search the HTML for `img-slot`)

Hero visual · provider headshot · program photos · founder photo. Each is a dashed placeholder
you can replace with an `<img>`; suggested dimensions are noted in the placeholder and in comments.
