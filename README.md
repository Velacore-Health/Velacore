# Velacore Health — Website

Marketing website for **Velacore Health**, a **telehealth platform** that coordinates access to
independent, licensed physicians and 503A compounding pharmacies. All prescribing decisions are made
solely by the independent physician; all treatments are prescription only.

Built as a fast, self-contained static site — no build step, no dependencies. Just open
`index.html` or deploy the folder anywhere. Intended to **replace** the current site.

> **Compliance — read first:** the public site names **only the five permitted treatments**
> (Tirzepatide, Semaglutide, NAD+, Glutathione, Sermorelin) and contains **no restricted product
> names, no coaching language, and no health claims.** Before changing any wording, read
> **[`COMPLIANCE.md`](./COMPLIANCE.md)** — including why restricted products must live behind a
> **server-side** member gate (a client-side password does not work) and what's still outstanding.

## Swapping in images

Every image is a dashed **placeholder** — search the HTML for `img-slot` and replace each block
with an `<img>`. Suggested dimensions are noted inside each placeholder and in nearby comments
(hero visual, provider headshot, five treatment photos).

## Structure

The deployable website lives in **`public/`** (that folder is what gets served — everything
outside it, like this README and `COMPLIANCE.md`, stays private and off the live site).

| Path | Purpose |
|------|---------|
| `public/index.html` | All page content and sections |
| `public/styles.css` | Full design system (colors, layout, responsive) |
| `public/script.js` | Mobile nav, FAQ accordion, scroll reveals |
| `vercel.json` | Vercel config (serves `public/`, security headers) |
| `.github/workflows/deploy-pages.yml` | Auto-deploys `public/` to GitHub Pages |
| `velacore-preview.html` | Self-contained design preview (for the Artifact link) — not deployed |

## Sections

1. **Hero** — telehealth positioning, "Start online visit" CTA, image slot
2. **How it works** — 5 steps (online visit → physician review → 503A fulfillment → coordination → refund)
3. **Why Velacore** — 4 pillars
4. **Treatments** — the 5 permitted products (Tirzepatide, Semaglutide, NAD+, Glutathione, Sermorelin) with prices + "refund if not prescribed" badges
5. **Providers** — "Meet a prescribing provider" (Dr. Broussard, independent)
6. **Guarantee** — prescribe-or-refund
7. **FAQ** — prescription-required, model, refund, states
8. **Get started** — embedded JotForm telehealth intake (form `261070496021449`)
9. **Please note** — critical compliance disclaimer
10. **Footer** — nav, states-served, medical/legal disclaimer

## Preview locally

```bash
# From the project folder:
python3 -m http.server 8000 --directory public
# then open http://localhost:8000
```

## Deploy

### Vercel (recommended)
1. Sign in at <https://vercel.com> with GitHub.
2. **Add New → Project → Import** `Velacore-Health/Velacore`.
3. Set **Production Branch** to `claude/velacore-health-website-qnjdnh` (Settings → Git), or make
   that branch the repo default first. `vercel.json` already serves `public/`.
4. **Deploy.** Add the `velacorehealth.com` domain under Settings → Domains and follow the DNS steps.

### GitHub Pages (backup)
1. Repo **Settings → Pages → Build and deployment → Source = "GitHub Actions".**
2. The `deploy-pages.yml` workflow publishes `public/` on every push to the site branch.

## Before going live — replace the placeholders

- [ ] **Intake form** — wire `#leadForm` to your JotForm telehealth intake (see `NOTE` in `index.html` / `TODO` in `script.js`).
- [ ] **Treatment prices** — confirm the five program prices are current.
- [ ] **Member gate** — build the **server-authenticated** member area for restricted products, then point "Member login" at it (see `COMPLIANCE.md`).
- [ ] **States served** — replace the placeholder line with the confirmed licensed-states list.
- [ ] **Legal pages** — Privacy, Terms, Telehealth consent (footer links are stubs).
- [ ] **Contact email** — update `hello@velacorehealth.com`.
- [ ] **Compliance review** — LegitScript pre-submission audit + healthcare attorney (see `COMPLIANCE.md`).

> ⚠️ **Regulatory note:** Telehealth and prescription marketing is heavily regulated. The public
> site names only the five permitted treatments and carries no health claims — keep it that way.
> Have all copy, disclaimers, and the intake flow reviewed by qualified legal/clinical advisors
> before launch.
