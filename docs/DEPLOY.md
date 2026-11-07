# Velacore Health, how the site goes live

Draft v1, Nov 6 2026. Same headings and the same three words as Salvage Health's note, so Dourado talks to both agents the same way. Lines marked UNCONFIRMED are facts only Dourado can read off a dashboard; they get filled in when he does.

The three words:
- Show me: a local preview at http://localhost:8000 plus screenshots at 375 and 1280 wide and the audit result. Nothing changes anywhere real.
- Push it: the change goes live on the website. Only after Dourado says this, never before.
- Undo: the site goes back to the last good version.

## Where it lives

- Files: GitHub, repository Velacore under the Velacore-Health account, branch claude/velacore-health-website-qnjdnh. The site is the `public/` folder only. Nothing in `docs/`, `tools/`, `brand/` or `shopify-theme/` is served.
- Live address today: https://velacore.vercel.app, served by Vercel from `public/` using `vercel.json` in the repo.
- Real address: velacorehealth.com. It still points at the stopgap Shopify store. It moves to the static site once the OpenLoop agreement is signed and Dourado says so.
- Second publisher: a GitHub Actions workflow in `.github/workflows/deploy-pages.yml` publishes `public/` to GitHub Pages on every push to the branch above. Two publishers for one folder is one too many. Decision pending, see Open decisions.
- What the site connects to: Google Fonts, Google Analytics 4 tag G-B2PQL4DLF8, schema.org markup. No forms, no server code, no keys, no patient health information. Intake, card entry and the patient portal live on the telehealth partner's hosted pages.

## How a change goes live

1. Vale edits the source. Program pages are never edited by hand; `tools/build_programs.py` is edited and run.
2. Vale runs the compliance check and the site audit, looks at the key pages at 375 and 1280, and shows Dourado.
3. Dourado says push it.
4. Vale commits and pushes the branch in one deliberate command, after a second confirmation if anything else is in the same push.
5. The host rebuilds. Vale verifies the live page and reports.

## What it costs

- Vercel plan: UNCONFIRMED. Dourado reads it under the Vercel project, Settings, Billing. Vercel's own terms say the free Hobby plan is for non-commercial use, so a business site needs Pro. Dourado's rule for Velacore: nothing on a free plan.
- Whether Vercel is linked to the GitHub repository for automatic deploys: UNCONFIRMED. Visible under the project's Settings, Git.
- Domain: UNCONFIRMED whether anything other than velacore.vercel.app is attached. Visible under Settings, Domains.
- GitHub Pages: free, but it is a second live copy and it has no commercial-use question because it is not the public address. It should be switched off once Vercel is confirmed, or become the only path. Dourado decides.
- Deploy count does not cost credits on Vercel the way Netlify charges Salvage Health, as far as the repo records. UNCONFIRMED against the plan Dourado is on.
- Host terms, read Nov 6 2026 from the published pages, not legal advice:
  - Vercel's fair use guidelines say Hobby teams are restricted to non-commercial personal use and that "advertising the sale of a product or service" counts as commercial. A site that sells programs needs Pro. Vercel's Hobby page lists Pro developer seats at $20 per user per month. Source: vercel.com/docs/limits/fair-use-guidelines and vercel.com/docs/plans/hobby.
  - Netlify's acceptable use policy has no clause about medical, pharmaceutical or prescription content. Its one health clause says protected health information may not be stored on Netlify services except under a signed Business Associate Agreement. The Velacore site stores none; intake lives on the partner's pages. Netlify's pricing page lists Free at $0 with a 300 credit limit, Personal at $9 a month with 1,000 credits, Pro at $20 a month with 3,000 credits, and says nothing about commercial use on any plan. Source: netlify.com/legal/acceptable-use-policy and netlify.com/pricing.
  - Either host works for this site on a paid plan. The deciding factors are one dashboard for both businesses, which favors Netlify, and the credit-per-deploy rule, which Vercel does not have.

## Before every deploy

All of these must be true, in this order:
1. `python -I .claude/skills/vc-compliance-check/scripts/check.py` shows 0 fail. Review lines are read and either fixed or explained in the report.
2. `python -I .claude/skills/vc-site-audit/scripts/audit.py --no-live` shows no FAIL except the Start visit placeholder links, which fail on purpose until OpenLoop sends the hosted URLs. Section 6 must be PASS on every page and width: no sideways scroll, no broken image, no low-contrast text, no tap target under 44 px.
3. The key pages have been looked at by eye at 375 and 1280, in the Browser pane or from the screenshots in `_audit/`.
4. The change has been checked against `docs/how-dourado-judges-design.md` and `docs/BRAND.md`.
5. For anything public that touches a claim, a price or a legal page: `vc-reviewer` has returned PASS.
6. Dourado has said push it for this exact batch.

Until LegitScript certification is issued in Velacore's name the badge stays off and no ads run. That is a compliance gate, not a deploy step, but a deploy never turns it on.

## How to deploy

Not yet exercised. Nothing has been pushed from this machine. The intended sequence, to be confirmed on the first real push with Dourado watching:

1. `git status` clean except the batch being shipped; `git log --oneline -3` shows the expected commits.
2. Run the two checks above once more on the committed tree.
3. `git push origin claude/velacore-health-website-qnjdnh` as its own command, nothing chained before or after it.
4. If GitHub answers with a server error, run `git ls-remote origin` to see whether the push landed before trying once more.

Salvage Health keeps its push address disabled between deploys and works from a clean worktree so unfinished pages never reach main. Velacore has one branch and no build step that could leak a draft page, so the simpler sequence above is enough for now. If the site gains draft pages or a second branch, copy Kevin's worktree-and-disabled-remote method.

## How to verify

1. Wait about a minute, then fetch https://velacore.vercel.app and the changed pages and confirm the new markup is there, for example a changed heading or the stylesheet version.
2. Key pages return 200: home, the five program pages, privacy, terms, telehealth consent, refund policy. 404 page still returns 404.
3. Run the audit without `--no-live` so section 3 reads the live site.
4. Look at the live home page at phone width once.
5. Report to Dourado: what went live, what was verified and how, what is untested.

## How to undo

- Vercel: open the project's Deployments list, pick the last good deployment, choose Promote to Production. Takes under a minute. UNCONFIRMED whether this costs anything on the plan Dourado is on.
- Or in git: `git revert <commit>` on the branch, run the checks, push again. Slower, but it leaves a record in the repo.
- GitHub Pages, while it still publishes: a revert and push is the only undo.

## Cutover to Netlify, the plan

Drafted Nov 6 2026 after Kevin read the Netlify account: one team on the Personal plan at $9 a month, about 4,700 credits available, auto recharge off, only the Salvage Health project in it, builds one at a time. A second project in that team is fine on credits. Nothing below has been started.

1. `netlify.toml` sits at the repo root, uncommitted until the move is approved. It publishes `public/`, keeps the four security headers from `vercel.json`, and rewrites clean URLs so `/terms` and `/programs/tirzepatide` work without `.html`.
2. Dourado connects the Velacore repository to a new Netlify project in his team. That is his click, see the list below. Production branch: `claude/velacore-health-website-qnjdnh`. Build command empty, publish directory `public`.
3. First push batch, one commit, one push on his words push it: remove `.github/workflows/deploy-pages.yml` so GitHub Pages stops publishing; keep `vercel.json` in the repo but leave the Vercel project unlinked, or delete the Vercel project once the Netlify copy is checked. Add `netlify.toml`. Run both checks before the commit.
4. After the push, Netlify builds. Verify the Netlify address at phone width: home, the five program pages, the four legal pages, clean URLs, 404 page, the security headers in the response. Run the audit against the Netlify address.
5. Keep velacore.vercel.app up until the Netlify copy passes. Then Dourado decides whether to delete the Vercel project.
6. velacorehealth.com moves only after the OpenLoop agreement is signed and Dourado says so. That is a DNS change at the registrar, his hands, one step at a time.
7. Credit rule, same as Salvage Health: a production deploy costs 15 credits, so changes are batched. Running out pauses every site in the team. If Velacore needs its own pool, a second Netlify team is the fix; decided by Dourado.

Clicks only Dourado can do for the move:
- In Netlify, Add new project, Import an existing project, choose GitHub, and grant Netlify access to the Velacore-Health organization or the Velacore repository when GitHub asks. Then pick the repository and the branch above, leave the build command empty, set the publish directory to public, and create the project.
- Say push it for the first batch.
- Later: the DNS change for velacorehealth.com at the registrar, and whether to delete the Vercel project and the Shopify stopgap.

## Known glitches

- Playwright screenshots from the audit land in `_audit/`, which is gitignored; review copies for Kevin go to `C:\Users\Dourado\Desktop\velacore-review\` because his rules block the Velacore folder.
- Kevin's browser pane can hold an old stylesheet. A hard reload fixes a wrong measurement.
- The program-page generator writes CRLF on Windows; git warns about LF to CRLF on commit. Harmless.
- No GitHub CLI, no Vercel CLI, no Shopify CLI on this machine. Install only with Dourado's OK and log it in `docs/installs.md`.

## Open decisions, Dourado's

1. One live path: Vercel or GitHub Pages. Vale's recommendation: keep Vercel as the only publisher and delete the Pages workflow, or move to Netlify to match Salvage Health, which is already connected here and uses one dashboard. Either way, one.
2. The Vercel plan, link and domain, the three UNCONFIRMED lines above.
3. Whether the Google Analytics tag may stay on pages that name prescription programs. A question for compliance counsel, not an agent.
