# Proposed additions to CLAUDE.md

Draft Nov 6 2026. Four sections Kevin's site CLAUDE.md has and ours lacks, so both files read the same way. Vale does not change CLAUDE.md on another agent's say-so; these go in when Dourado says yes. Nothing here changes the hard rules, the isolation rules or the compliance rules.

## Deploys cost money

Every push to the branch publishes `public/`. Nothing is pushed until Dourado says push it for that exact batch, the checks in `docs/DEPLOY.md` have passed, and only one publisher is live. Batch small changes; never push after a single tweak. The host plan and its cost are recorded in `docs/DEPLOY.md`; a free plan is not allowed for Velacore.

## Design checklist

Check every new page, section or effect against this before showing Dourado. Full rules in `docs/how-dourado-judges-design.md` and `docs/BRAND.md`.

1. Phone first: design at 375, then widen. Nothing overflows or sits past the edge at 375 or 1280.
2. Every label fits its longest real text. No clipped words, no three-line pills.
3. Facts match the source. Prices, plans and options come from the program data or the live system, never typed twice.
4. One accent color, pine text, fewer words, more white space. No small labels above headings, no all-caps labels, no trailing arrows, no middle-dot strings, no decorative numbering unless the content is a sequence.
5. Contrast 4.5 to 1 on all text, every tap target 44 px, visible focus, reduced motion respected.
6. Motion is rare and deliberate. One moment per page at most.
7. The logo is never redrawn. The brand guide wins; if it is wrong, say so and edit the guide.
8. Images carry width and height; above-the-fold images load eagerly.
9. Health claims are decided by `COMPLIANCE.md` and `vc-reviewer`, never by a design pass.

## Build

Program pages are generated. Edit `tools/build_programs.py`, then from the repo root run `python -I tools/build_programs.py`. Product images: drop PNGs in `assets-in/products/`, run `python -I tools/prepare_images.py`, then the build. Preview with the `velacore-site` entry in `.claude/launch.json`, which serves `public/` at http://localhost:8000. Windows note: Python is `python` or `py`, never `python3`.

## Audit

Two scripts, both read-only:

- `python -I .claude/skills/vc-compliance-check/scripts/check.py` scans every public file for drug names outside the approved five, claim and coaching words, the LegitScript badge, the FDA disclaimer and secrets. Must show 0 fail.
- `python -I .claude/skills/vc-site-audit/scripts/audit.py --no-live` checks links, files, sitemap, legal pages, prices across every surface, and renders the home and one program page at 375 and 1280 for overflow, broken images, text contrast and 44 px tap targets. Drop `--no-live` to include the live site. Must show no FAIL except the Start visit placeholders until OpenLoop sends the intake URLs.

Both run before anything is shown to Dourado and before every deploy. A weekly read-only run is proposed in `docs/DEPLOY.md`; it is scheduled only on Dourado's yes.
