# Velacore Health — Website Compliance Notes

Record of the compliance decisions baked into the public site so they aren't accidentally undone.
**This is not legal advice.** Run a LegitScript pre-submission audit (e.g. White Label MD / Bloom
Consulting) and have a healthcare attorney review before submitting. Reference:
<https://www.legitscript.com/resources/>.

## Positioning model (the core rule)

Velacore is presented **only** as a **telehealth platform** that **coordinates access** to
**independent, licensed physicians** and **503A compounding pharmacies**. It is **not** a provider,
prescriber, medical practice, or "wellness/health coaching" company. **All prescribing decisions are
made solely by the independent physician.** All treatments are **prescription only** and this is
stated throughout ("Prescription required").

Coaching / "wellness coaching" language has been removed entirely and the site leans fully into
telehealth (online visit → independent physician review → 503A pharmacy fulfillment → refund if not
prescribed).

## Public treatments — the ONLY products named on the scannable site

Per the owner's guidance (confirmed with the arsynl.com operator), the public, LegitScript-scannable
site names **only these five**:

| Treatment | Public descriptor (factual, no efficacy claims) | Program cost |
|-----------|--------------------------------------------------|--------------|
| Tirzepatide | Dual GIP / GLP-1 receptor agonist | $75–$115/mo |
| Semaglutide | GLP-1 receptor agonist | $40–$55/mo |
| NAD+ | NAD+ injectable | $80/mo |
| Glutathione | Glutathione injectable | $80/mo |
| Sermorelin | Growth hormone–releasing hormone analog | $130/mo |

Descriptors are deliberately **mechanistic/factual**, not benefit claims (e.g. "GLP-1 receptor
agonist," not "melts fat"). Keep it that way.

## Restricted products — NOT on any public / committed file

The remaining catalog items are **restricted** and must **not** appear on the public site, in meta,
in this repo, or in any file served without authentication. They are intentionally **not listed by
name anywhere in this repository.** They belong only in a gated member area (see below).

## How the member gate MUST work (important)

- **Server-side authentication only.** The restricted catalog must never be sent to an
  unauthenticated request. A client-side JavaScript "password" that hides a `<div>` does **not**
  work — the names sit in the page source and are fully scannable. Do not use that approach.
- **Gating is risk-reduction, not an exemption.** Per LegitScript, an applicant must disclose
  **every URL/domain it owns or controls, and all of them must meet the certification standards.**
  A login-gated area you own is still subject to review. Gating keeps restricted products off the
  public marketing surface; it does not make gated content rule-free.
- Recommended implementations: a real members platform with accounts (e.g. your white-label app),
  a host with authenticated routes, or a members area on your commerce/CMS platform — **not** a
  static page with a shared password.
- The public site currently links "Member login" to a placeholder (`#`). Point it at the
  authenticated portal when it exists.

## Deliberately NOT on the public site

- **No DEA numbers / confidential underwriting data.** The Payment Processing Guide is marked
  "Confidential · Not for redistribution"; DEA registrations are not public. Underwriting only.
- **No health / efficacy / outcome claims.** Treatment copy is factual and mechanistic.
- **No "wellness/health coaching"** anywhere (copy, meta description, meta keywords).
- **No medical-director claim.** Dr. Broussard is shown as an *independent* prescribing physician.
  The medical-director relationship still needs a signed agreement + attorney review.

## LegitScript website essentials reflected in the build

- "Prescription required" stated in the top bar, treatments, FAQ, form, disclaimer, and footer.
- Prescriber identity/credentials **disclosed before care** (provider section + pillar copy).
- Business model clearly disclosed (coordination platform; physician decides).
- Transparent pricing and a clear refund policy.
- States-served disclosure (placeholder line — replace with the confirmed list).

## Still required before submission (from your brief — not code)

- [ ] Confirm the real **states-served list**; replace the placeholder line.
- [ ] Confirm **pharmacy routing** (out-of-state fulfillment constraints).
- [ ] Signed **Medical Director Agreement** + attorney review of provider language.
- [ ] 5 written SOPs; BAAs with every vendor touching patient data.
- [ ] Legal pages: Privacy, Terms, Telehealth consent (footer links are stubs).
- [ ] Build the **server-authenticated** member area for restricted products.
- [ ] Wire the intake form/CTA to your JotForm telehealth intake.
- [ ] Site fully public (no password) before the LegitScript scan of the public surface.

## Image slots to fill (search the HTML for `img-slot`)

Hero visual · provider headshot · five treatment photos. Each is a dashed placeholder you replace
with an `<img>`; suggested dimensions are noted in the placeholder and in nearby comments.
