# Campaign blueprint for the Velacore launch

A starting structure, not a plan. Adapt it to the task and the budget Dourado gives. Every number marked benchmark comes from `docs/pricing-research.md` section 3 and its sources; never present one as our result.

## Goal

The first 10 paying patients fast, because the $3,000 monthly OpenLoop fee stops at 10. Then a cost per paying patient at or under the benchmark range of $150 to $250, benchmark, sources in the pricing memo, with the 12-week plan as the default offer to protect retention.

## Offer

- Lead offer: $149 first month of semaglutide, then $229 a month, cancel any time. Tirzepatide $199 first month, then $279.
- Entry tier: microdosing GLP-1 at $179 a month for price-sensitive buyers.
- Default plan on the landing page: the 12-week plan, $199 or $249 a month, charged up front.
- Confirm all prices against the signed agreement before any ad runs.

## Structure

Meta, one ad account, one pixel on velacorehealth.com only.

- Campaign 1, Prospecting, broad US 18 to 74, objective traffic optimized to the Start visit click until a real conversion event exists. Three ad sets by creative angle, not by audience: how it works, price and plan, the physician review.
- Campaign 2, Microdosing entry tier, same shape, its own landing page.
- No retargeting campaign until the policy page is rechecked for the category.

Google, one account.

- Campaign 1, Search, exact and phrase match on service terms: compounded semaglutide online, tirzepatide telehealth, semaglutide prescription online, NAD+ injection prescription. Negative keywords: every brand name, "free", "without prescription", "buy" without "prescription".
- Campaign 2, Search, brand: velacore health.
- No Performance Max and no Display until there is a conversion event the platform can learn from.

## Naming

`VC_{platform}_{campaign}_{adset}_{creative}_{date}`. Example: `VC_META_PROSPECT_HOWITWORKS_V1_2026-12-01`.

## Tracking plan

- Every Start visit link: `?utm_source={meta|google}&utm_medium=paid&utm_campaign={campaign}&utm_content={creative}`.
- GA4 event `start_visit_click` with the product and the UTMs as parameters. PostHog event of the same name as the second record.
- Weekly reconciliation sheet: spend, clicks, Start visit clicks, cost per Start visit click, paying patients from OpenLoop's Wednesday payout, cost per paying patient. One row per campaign per week.
- When OpenLoop confirms a pixel or post-payment redirect on its hosted pages, move the optimization event to the purchase and retire the click proxy.

## Creative briefs, first round

1. How it works. Four plain steps, screen text only, voice optional. No body footage.
2. Price and plan. The real price with the real conditions on screen for the full length.
3. The physician review. What "an independent licensed clinician decides" means, said plainly. No white coat stock footage that implies our own doctor until OpenLoop provides a named prescriber.
4. The honest FAQ. One question per ad: Do I need a prescription. What if I am not approved. Is this FDA approved.

Every brief gets its hooks and copy from the vc-copy agent and its policy pass from this skill's checklist before it goes to Dourado.

## Budget shape

Start small and even: a daily budget Dourado sets, split 70 percent Meta prospecting, 30 percent Google search, for 14 days, then move money toward whichever has the lower cost per Start visit click. Raise budget only after the first paying patients reconcile.
