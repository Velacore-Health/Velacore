# Launch steps: Sexual Health and Women's HRT

Written Nov 18 2026. Dourado approved both categories that day, limited to the items OpenLoop names in writing.

## How the switch works

The two programs are built into the site but switched off. Their data lives in `tools/draft_programs.py`. A program goes live only when its slug is added to the `LIVE` list at the top of that file. While `LIVE` is empty, the builders write the live site exactly as before; this was checked on Nov 18 by rebuilding and confirming no file in `public/` changed.

When a slug is in `LIVE`, the builders add that program to:

- its own program page and Start page
- the Treatments dropdown, under Sexual and women's health
- the slide-in menu, with its price line
- the pricing page, as its own card
- the footer program list on every generated page
- the phone price bar on its page

Price lines are read from the program data, never typed twice. Sexual health shows From $96 a pack. Women's HRT shows $79 a month, billed $237 every 12 weeks.

Until then, `python -I tools/build_drafts.py` writes the draft pages to `drafts/programs/`, which is never published.

## Before the switch goes on

Every item here must be done first. The open items for each page are also listed in `tools/draft_programs.py`.

1. OpenLoop answers in writing every open item, mainly which items are compounded, which pharmacy fills them, the refund and cancel terms, shipping, the HRT age limit, and whether the vials are taken by mouth or injected.
2. OpenLoop's clinical team supplies the important safety information for each medication. It replaces the placeholder in the `safety` field.
3. The compounded disclaimer is set per item to match OpenLoop's answer.
4. If any item is filled outside a 503A pharmacy, the site-wide 503A wording in the footer, the please-note block and the trust strip is broadened.
5. The attorney decides whether any analytics may run on these pages.
6. Each line swap in `SWAPS` that OpenLoop confirms is removed, and the "Draft placeholder" words come out of the FAQ answers.
7. Product images: done Nov 18 2026 and checked against the label artwork, then remade in the studio look Nov 20 2026. The studio versions wait in `assets-in/products/studio/` as `_hold-sexual-health.jpg`, a vial, and `_hold-womens-hrt.jpg`, a bottle, so the converter skips them; the marble versions are in `assets-in/products/`. Their labels carry only FOR PRESCRIPTION USE ONLY; if OpenLoop confirms the items are compounded, or names a different form, the labels and photos are remade in Gemini first.
8. vc-reviewer passes both pages for launch.

## On launch day

Dourado, Nov 20 2026: when a hidden program launches, every section of the site that lists programs must carry it. Nothing is pushed until the list below is done and the site audit's section "2b. Every live program on every surface" passes. That check reads the live list in `tools/draft_programs.py` and fails if a live program is missing from its program page, Start page, pricing card, the home program row, the program chooser, the Treatments menu, the sitemap, the footer, its product photo, its menu thumbnail or its square home-row photo. The parts a script cannot judge are marked by hand below.

1. Add the slugs to `LIVE` in `tools/draft_programs.py`.
2. Add both programs to `.claude/skills/vc-site-audit/audit-config.json`, under approved products, intake links and planned prices, and add each slug to `BASE_SLUGS` in `.claude/skills/vc-site-audit/scripts/audit.py` once it is permanent.
3. Add the approved drug names to the approved list in `.claude/skills/vc-compliance-check/scripts/check.py`, and update the approved list in `COMPLIANCE.md` and the hard rules in `CLAUDE.md`.
4. Photos, all from the studio shots so the look matches:
   - drop the `_hold-` from each studio file name in `assets-in/products/studio/`
   - add both names to `STUDIO_PRODUCTS` in `tools/prepare_images.py`, run `python tools/prepare_images.py sexual-health womens-hrt`
   - add both to the square home-row list in `home_weight_card` in `tools/prepare_images.py` and run `python -I tools/prepare_images.py --home`
   - add a box for each to `STUDIO_BOXES` in `tools/make_thumbs.py` and run it
   - if either has a needle-free form, add it to `FORM_TILES` and run `--tiles`
   - back up any new picture to the Drive folder, standing OK
5. Run the builders from the repo root: `build_programs.py`, `build_pages.py`, `build_articles.py`, `inject_panel.py`, then `seo_head.py`. These cover the program pages, Start pages, Treatments menu, slide-in menu, pricing card, footer and phone price bar.
6. Edit the hand-written parts the builders do not cover:
   - `public/sitemap.xml`: the two program URLs and the two Start URLs if Start pages are listed
   - `public/index.html` home program row: one card each, in the same style, with its square photo, category label, price from the data and Start button
   - the program chooser in `public/index.html` and `public/script.js`: a goal tile with its photo for the new category, and the new slugs in `MAP`, `NOTE` and `TITLE`, including the needle-free answer if a form is taken by mouth
   - the slide-in menu goals list, `GOALS` in `tools/build_programs.py`, and the small home tiles under the two big home cards if a new goal is added
   - the pricing page needle-free cards, `form_cards` in `tools/build_pages.py`, and the home needle-free tiles, if either program has a form without a needle
   - every program count in the copy, such as "six programs" on the home page, the goal band, the chooser and How it works
   - the home page title, meta description, keywords and share text in the head of `public/index.html`, which name the programs
   - the Learn page and FAQ, where a program list or a form list appears
   - the pricing page wording that says one price covers shipping, if OpenLoop says shipping is extra for these programs
   - `docs/BRAND.md`, the program colors for the label lines
7. Run the compliance check and the site audit. Both must pass, including section 2b. Check every new card at phone and desktop sizes for cut photos and labels that overlap a product.
8. vc-reviewer ship review, then Dourado says push it.

Added Nov 20 2026, from vc-reviewer. Before a Start page is ever built for these two programs, change `start_plans` in `tools/build_programs.py`. As written it would open the Sexual Health Start page with a Choose your plan picker that lists the medication formats, which reads as the patient choosing the medication. On these programs the clinician chooses; the Start page must show the price line only, or a picker of true billing plans if OpenLoop gives any.
