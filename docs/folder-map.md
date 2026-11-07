# Velacore folder map

Draft v1, Nov 6 2026. One numbered system, the same on this PC and in the Velacore business Drive, so anything can be found by number. Same method as Salvage Health, shorter list. Nothing has been moved yet; Dourado approves the map first, then the Drive is read and tidied through the business account route, moves only, never deletes.

## The rule for every file

- Name: `YYYY-MM-DD_topic_v1`, lowercase, dashes inside the topic, version at the end. Example: `2026-11-06_label-spec_v1.pdf`.
- New files land in `00-inbox` first and are sorted within the week.
- Nothing loose in a Drive root or a folder root. Screenshots and screen recordings go to `07-references`.
- Compliance and vendor documents live in `02-compliance` and `06-vendors`, never beside marketing media.
- Secrets, keys and passwords never go in any Drive folder or any project folder. Cost sheets, DEA and NPI documents and anything with patient data stay in `02-compliance` or `06-vendors` in Drive only, never in the repo.

## The folders

| Number | Name | What goes in it | On the PC | In Drive |
|---|---|---|---|---|
| 00 | inbox | Anything new before it is sorted | `assets-in/` | `00-inbox` |
| 01 | brand | Logo source files, brand card, fonts, label artwork, approved product images | `brand/` and `public/images/products/` | `01-brand` |
| 02 | compliance | LegitScript application and letters, state rules, consent and policy drafts, counsel notes | `COMPLIANCE.md` and `docs/` for the public rules only | `02-compliance` |
| 03 | site | Page copy drafts, screenshots of approved pages, audit reports worth keeping | `public/`, `docs/`, `_audit/` | `03-site` |
| 04 | ads | Campaign plans, ad copy, creative, landing page briefs, reports, once LegitScript clears | `docs/` plans only | `04-ads` |
| 05 | media | Video and photo workflow: raw clips, selects, edits, scheduled, posted | `01-raw-clips/` to `04-scheduled/`, gitignored | `05-media` with the same five subfolders |
| 06 | vendors | OpenLoop proposal, agreement, call notes, pharmacy and lab documents, Asher closeout, Shopify stopgap | `docs/openloop-proposal-notes.md` for the public terms only | `06-vendors` with one subfolder per vendor |
| 07 | references | Competitor screenshots, reference sites, research reports such as the Gemini Deep Research output, Kevin's review notes | `docs/reference-*.md` | `07-references` |

Inside `05-media`, the five subfolders keep the names the PC already uses: `01-raw-clips`, `02-selects`, `03-edits`, `04-scheduled`, `05-posted`.

## The map file

A copy of this file sits in the root of the Drive as `00_FOLDER-MAP.md` and here as `docs/folder-map.md`. When a folder is added, both copies change the same day.

## Weekly housekeeping, proposed

Monday about 8:50 AM, after the site audit: read the Drive and the PC inbox, move files that have an obvious home, rename to the date pattern where the date is known, never delete, write one dated line to `docs/housekeeping-log.md` saying what moved and what was left alone and why. Scheduled only on Dourado's yes.

## Not done yet

1. Read what is in the Velacore Drive today, read-only, through the business account. Needs Dourado's yes.
2. Send the list and this map to Kevin, then move files only after Dourado approves the map.
3. Rename the PC media folders to sit under one `05-media` folder, or leave them as they are. Dourado's call; the repo map in CLAUDE.md changes with it.
