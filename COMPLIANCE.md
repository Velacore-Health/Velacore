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

### Fees & refund policy (authoritative — owner-confirmed)

**What the customer pays:** the medication/program price **+ a one-time $20 physician fee** at
intake (collected on behalf of the independent medical group). **Shipping is included** — the
customer pays no separate shipping fee. (Velacore absorbs the remaining provider cost — $10 single /
$30 multi of the $30/$50 doctor cost — plus the flat $35 shipping.)

**Refunds:** if the independent physician does not approve the program (in full or in part), the
**program payment is refunded in full within 15 days**. The **$20 physician fee is non-refundable**.
**Medications are non-returnable and non-refundable once dispensed** (federal/state pharmacy law).

> ⚠️ Two things to reconcile so every surface matches: (1) the original launch brief said the
> physician fee *was* refunded — it is **not**; (2) the old live-site FAQ listed a $35/$50 review
> fee + separate $35 shipping — that's superseded by the **$20 fee + included shipping** model above.
> Make sure the **JotForm intake terms and the payment processor** state this same policy.

## Still required before submission (from your brief — not code)

- [x] States served: **all 50 US states** — ✅ written AsherMed confirmation received (Paulina,
  Asher Health Partner Support email: "affiliated physicians are licensed to prescribe in all 50
  states… you can confidently disclose"). Save that email to the compliance file.
- [x] Pharmacy license copy — received from AsherMed (attached to same email).
- [x] Partnership agreement — template received from AsherMed; ⚠️ execute (sign + return) so both
  parties hold a fully executed copy.
- [~] **AsherMed BAA:** AsherMed states BAA provisions are **embedded in the main agreement**
  (support email). Legitimate under HIPAA IF the required 45 CFR 164.504(e) provisions are present.
  ⚠️ Verify: get section numbers in writing + read the agreement for permitted uses, safeguards,
  breach notification, and return/destruction terms. Update SOP-01 §7/§8 wording once confirmed
  (reference the agreement sections instead of a standalone BAA).
- [x] Pharmacy routing — ✅ written confirmation received: **White Label Pharmacy and PerfectRx are
  licensed to dispense and ship to all 50 states** (AsherMed support email). Save email to the
  compliance file. Follow-up asked to confirm Velacore orders route exclusively through these two.
- [ ] Signed **Medical Director Agreement** + attorney review of provider language.
- [ ] 5 written SOPs; BAAs with every vendor touching patient data.
- [x] Legal pages drafted: `privacy.html`, `terms.html`, `telehealth-consent.html`, `refund-policy.html`, linked in the footer. **⚠️ Attorney review required before launch** — especially governing-law/venue/arbitration (currently Texas placeholder), HIPAA specifics, and auto-renewal terms. Confirm the JotForm terms and payment processor match these pages.
- [x] Intake wired to JotForm (form 261070496021449).
- [ ] Build the **server-authenticated** member area for restricted products.
- [ ] Confirm the JotForm intake terms + payment processor mirror the Refund Policy (fee non-refundable).
- [ ] Site fully public (no password) before the LegitScript scan of the public surface.

## Image slots to fill (search the HTML for `img-slot`)

Hero visual · provider headshot · five treatment photos. Each is a dashed placeholder you replace
with an `<img>`; suggested dimensions are noted in the placeholder and in nearby comments.
