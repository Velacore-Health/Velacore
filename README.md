# Velacore Health — Website

Marketing website for **Velacore Health**, a telehealth practice offering clinician-guided,
pharmacy-compounded peptide therapy delivered to patients at home.

Built as a fast, self-contained static site — no build step, no dependencies. Just open
`index.html` or deploy the folder anywhere.

## Structure

| File | Purpose |
|------|---------|
| `index.html` | All page content and sections |
| `styles.css` | Full design system (colors, layout, responsive) |
| `script.js` | Mobile nav, FAQ accordion, lead form, scroll reveals |

## Sections

1. **Hero** — headline, value prop, eligibility CTA, protocol preview card
2. **How it works** — 4-step process
3. **Programs** — Metabolic & Weight, Recovery, Longevity, Hormone, Sleep
4. **Why Velacore** — differentiators + stats
5. **Pricing** — placeholder membership tiers
6. **Safety & compliance** — trust cards
7. **FAQ** — common questions
8. **Get started** — lead-capture form (demo)
9. **Footer** — nav, contact, medical/legal disclaimer

## Preview locally

```bash
# From the project folder:
python3 -m http.server 8000
# then open http://localhost:8000
```

## Deploy

Drop the folder on any static host:

- **Netlify / Vercel:** drag-and-drop the folder, or connect the repo.
- **GitHub Pages:** enable Pages on this branch, root folder.
- **Cloudflare Pages / S3:** upload as static assets.

## Before going live — replace the placeholders

- [ ] **Pricing** — real membership/medication pricing (`#pricing` section).
- [ ] **Lead form** — wire `#leadForm` to your intake/CRM provider (see `TODO` in `script.js`).
- [ ] **Programs** — confirm the exact therapies and language your clinicians offer.
- [ ] **States served** — list the states where you're licensed.
- [ ] **Legal pages** — Privacy, Terms, Telehealth consent (footer links are stubs).
- [ ] **Contact email** — update `hello@velacorehealth.com`.
- [ ] **Compliance review** — have counsel/clinical review all medical claims and the disclaimer.

> ⚠️ **Regulatory note:** Peptide and telehealth marketing is heavily regulated. Have all
> medical claims, disclaimers, and the intake flow reviewed by qualified legal/clinical
> advisors before launch.
