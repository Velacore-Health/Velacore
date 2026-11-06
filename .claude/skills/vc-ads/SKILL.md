---
name: vc-ads
description: Plan, draft and check Meta and Google ads for Velacore Health, a telehealth brand for physician-prescribed compounded GLP-1s and peptides on OpenLoop. Use for campaign plans, ad copy, creative briefs, landing page briefs, UTM and tracking setup, policy and LegitScript readiness, and reading ad results. Use when Dourado says ads, campaign, Meta, Facebook ads, Instagram ads, Google ads, pixel, UTM, landing page, or cost per patient.
---

# vc-ads

Paid media for a prescription telehealth brand is a gated category on both platforms. The order of operations is fixed: certification first, tracking second, creative third, spend last.

## Steps

1. Check the gate. Read the "Status as of" block in `docs/HANDOFF.md`. If LegitScript is not issued in Velacore's name, every output is a draft marked "ready to submit once certified" and no budget is spent. Say this in the first line.
2. Read `references/policy-checklist.md`. Run every ad, landing page and audience through it. A single fail blocks the item.
3. Read `references/campaign-blueprint.md` for the structure, naming, budgets and tracking plan. Adapt it to the task; do not restate it.
4. Build the deliverable in the shape the `vc-ads` agent file describes. Pull prices only from `docs/pricing-research.md` section 5 and `docs/openloop-proposal-notes.md`. Pull benchmarks only from the sources listed in the pricing memo, and label them.
5. Hand anything that will be published to `vc-reviewer` before it goes to Dourado.
6. Close with what changed, what was verified and how, what is untested, then the one next step.

## What the tracking can and cannot do

- On our site: GA4 is installed with tag G-B2PQL4DLF8. PostHog is connected to the account and can record Start visit clicks. Every Start visit link carries UTMs, so the click is attributable to the ad.
- On OpenLoop: Launchpad has funnel analytics and A/B funnel tests inside its dashboard. A Meta pixel or Google tag on OpenLoop's hosted pages, and a post-payment redirect, were "being built" as of Nov 2026 and are unconfirmed. Until confirmed, the paid conversion lives only in OpenLoop's weekly payout counts.
- So: optimize campaigns to the Start visit click, report cost per click-to-intake, and reconcile to paid patients weekly from the payout. Name this limit in every plan and every report.

## What this skill never does

Launch, edit, pause or fund a campaign. Create or change a Meta Business or Google Ads account. Submit a certification application. Write anything about a product that is not on the public site. All of those are Dourado's, one step at a time, after his OK.
