---
name: vc-compliance-check
description: Read-only LegitScript compliance scan of the Velacore repo. Flags drug-like words outside the five approved treatments, efficacy and coaching language, the LegitScript badge state, missing FDA disclaimers and stray secrets. Use when Dourado says "compliance check", before any deploy or theme zip rebuild, and after editing public/ or shopify-theme/.
---

# vc-compliance-check

Read-only. This skill reports problems and never fixes them. Fixes need Dourado's OK.

## Steps

1. From the repo root, run:
   `python -I .claude/skills/vc-compliance-check/scripts/check.py`
2. Read every FAIL and REVIEW line. The script only matches patterns, so judge each hit:
   - A drug-like word that isn't one of the five approved treatments is a FAIL unless it's plainly generic. Never write a restricted product's name into a report, a commit message or any file. Refer to it by file and line only, as "a restricted name".
   - Claim words often show up in allowed disclaimers, for example "not a guarantee of treatment" or "Individual results vary". Call those fine. A benefit or outcome promise is a real problem.
   - Image file names that aren't one of the five products: check whether the picture or its alt text points at a restricted item.
3. Report to Dourado in plain words, grouped as: must fix before LegitScript, worth a look, all good. Give file and line for each. End with the standard report format from CLAUDE.md.

## What it checks

- Drug-like words, meaning names ending in -tide, -relin, -tropin and similar, that aren't Tirzepatide, Semaglutide, Sermorelin or Glutathione. NAD+ is checked through the CSV. Covers every text file in the repo and the text files inside the theme zip.
- On public surfaces only, meaning `public/`, `shopify-theme/`, the product CSV, the preview HTML and the theme zip: efficacy or claim words, coaching language, and "LegitScript Certified" text outside the theme's toggle.
- The `legitscript_certified` toggle in `shopify-theme/config/settings_data.json` is off.
- The FDA compounded-medication disclaimer is in `main-product.liquid` and in every CSV product body.
- Possible secrets: live keys, inline API keys, DEA numbers.

## What it doesn't check

Live sites, rendered pages, images' visual content, prices against `docs/pricing-research.md`, the states list, and legal page wording. Those belong to `vc-site-audit`, which hasn't been built yet.
