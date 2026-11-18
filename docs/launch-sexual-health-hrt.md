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
7. Product images follow `docs/BRAND.md`: drop `sexual-health.png` and `womens-hrt.png` in `assets-in/products/`, run `python -I tools/prepare_images.py`, then make the small menu photos with `tools/make_thumbs.py`.
8. vc-reviewer passes both pages for launch.

## On launch day

1. Add the slugs to `LIVE` in `tools/draft_programs.py`.
2. Add both programs to `.claude/skills/vc-site-audit/audit-config.json`, under approved products, intake links and planned prices.
3. Add the approved drug names to the approved list in `.claude/skills/vc-compliance-check/scripts/check.py`.
4. Run the builders from the repo root: `build_programs.py`, `build_pages.py`, `build_articles.py`, then `inject_panel.py`.
5. Edit the hand-written parts the builders do not cover:
   - the two program URLs in `public/sitemap.xml`
   - the home page treatments grid and the program chooser in `public/index.html`
   - the words "six programs" on the home page and in the goal band, once the chooser covers the new programs
   - the pricing page wording that says one price covers shipping, if OpenLoop says shipping is extra for these programs
6. Run the compliance check and the site audit. Both must pass.
7. vc-reviewer ship review, then Dourado says push it.
