# Velacore Health website

The marketing website for Velacore Health, a telehealth coordination platform that connects patients
to independent licensed physicians and 503A compounding pharmacies. Velacore is never the provider or
the prescriber. Every prescribing decision is made by the independent clinician, and every treatment
is prescription only.

Rewritten Nov 20 2026. The earlier version of this file described the first one-page draft and is in
git history.

## Read these first

- `CLAUDE.md` the working rules, the repo map, the build order and the two checks.
- `docs/HANDOFF.md` the state file: what exists, what was decided, what is open.
- `COMPLIANCE.md` the rules the public site must follow, including which treatments may be named.
- `docs/DEPLOY.md` where the site lives and how a change goes live.
- `docs/BRAND.md` logos, colors, type, voice and the image rules.

## Where the site lives

The live site is https://www.velacorehealth.com, published by Netlify from the `public/` folder on
every push to the branch `claude/velacore-health-website-qnjdnh`, using `netlify.toml`. Nothing
outside `public/` is served.

## What is in the repo

| Path | What it is |
|------|------------|
| `public/` | The site. Most pages are generated; see the Build section of `CLAUDE.md`. |
| `tools/` | The builders and their data: programs, stand-alone pages, articles, menu and prices, share picture. |
| `drafts/` | Hidden pages that are built but never served. |
| `docs/` | Handoff, deploy notes, brand guide, research and plans. Never served. |
| `brand/` | The brand card used with image prompts. |
| `netlify.toml` | Netlify settings: publish folder, clean addresses, security headers. |
| `velacore-preview.html` | A one-file design preview from the first draft. Not served and not kept current. |

## Build and preview

Pages are built with Python from the repo root. The builders and their order are listed in the Build
section of `CLAUDE.md`. On this Windows machine Python is `python` or `py`.

To preview, serve `public/` at http://localhost:8000:

```
python -m http.server 8000 --directory public
```

## Before anything goes live

Both checks must pass, the compliance reviewer must return PASS, and Bryan Dourado must approve that
exact batch. The steps are in `docs/DEPLOY.md`.

- `python -I .claude/skills/vc-compliance-check/scripts/check.py`
- `python -I .claude/skills/vc-site-audit/scripts/audit.py --no-live`

## Rules that never bend

- The public site names only the treatments approved in `COMPLIANCE.md`.
- No efficacy or outcome claims and no coaching language.
- The FDA compounded-medication disclaimer stays on product pages.
- The LegitScript badge stays off until certification is issued in Velacore's name.
- No secrets, cost sheets, license documents or patient data in the repo.
- Patient health data never touches our servers. Intake runs on the partner's hosted forms.
