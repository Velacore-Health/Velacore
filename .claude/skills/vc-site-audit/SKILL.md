---
name: vc-site-audit
description: Full audit of velacorehealth.com and the public/ site. Runs the compliance scan, checks treatment cards and their OpenLoop intake links, legal pages, links, sitemap, the states directory, old Asher and JotForm wording, prices on every surface against the plan, the live site's title and links and product pages, the theme zip, and desktop plus phone screenshots. Use when Dourado says "audit the site", "is the site up to date", "check everything", before any deploy, and after a batch of site edits.
---

# vc-site-audit

Read-only toward the site. Writes only a report and screenshots to `_audit/<date>/`, which is gitignored.

## Steps

1. Read `audit-config.json` in this folder. It holds the decisions the audit checks against: platform, planned prices, the OpenLoop intake link per treatment, wording that belongs to the old model. If a decision changed since the last run, update the config first, with Dourado's OK.
2. From the repo root run:
   `python -I .claude/skills/vc-site-audit/scripts/audit.py`
   Add `--no-live` when offline or when only local files changed. Add `--no-render` to skip screenshots and save about a minute.
3. Open the screenshots named in section 6 and look at them. The script catches sideways scroll, broken images and console errors; it cannot judge whether a page looks right.
4. Report to Dourado in plain words, grouped as: must fix before launch, worth a look, all good. Give file and line or the URL for each. Never write a restricted product's name; the script withholds them and so do you. End with the standard report format from CLAUDE.md.

## What it checks

1. The `vc-compliance-check` scan, folded in.
2. `public/`: each treatment card is one of the five, its Start visit link matches the OpenLoop intake link in the config, internal links and anchors resolve, the sitemap maps to real files, the four legal pages exist and are linked, old-model wording such as physician fee, Asher and JotForm, placeholder text, and how many states the consent page's complaint directory names.
3. Live `velacorehealth.com` and the Vercel foundation site: each answers 200, what platform serves it, page title, no password page, no LegitScript badge, no unapproved drug names or coaching or claim words on the home page, same-site links from the home page answer 200, and on Shopify only, each live product page carries the FDA disclaimer. Any intake links set in the config must answer 200.
4. Prices on every surface side by side: `public/`, the theme fallback, the product CSV, the live store, and the planned month-to-month price. Disagreement between live surfaces is a FAIL.
5. The theme zip matches `shopify-theme/`. Stopgap only.
6. Screenshots of the local home page, the live home page and one live product page at desktop and phone widths.

## Target model, decided Nov 6 2026

- Asher is canceled. OpenLoop is the platform. JotForm is retired.
- `public/` is the site and the foundation to build on. Vercel already serves it at https://velacore.vercel.app. The velacorehealth.com domain moves from the Shopify store to Vercel.
- Each treatment's Start visit button links out to that treatment's OpenLoop hosted intake page. Patient data never touches our site.
- The live Shopify store is a stopgap and goes away once Vercel serves the domain.

## What it doesn't check

Legal page wording against the OpenLoop refund model, the states list against official sources, Vercel or DNS settings, ad pixels, and anything behind a login.
