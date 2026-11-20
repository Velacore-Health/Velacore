# Legal drafts, index

Written by vc-copy, Nov 13 2026. Everything in this folder is a draft. Nothing is served, nothing is live, nothing was sent. None of it is legal advice.

## What this is

Dourado asked for a check of Velacore's policy pages against the ground a reference site covers. The reference site was reduced to structure only before any writing began. No wording, name, address, phone number or partner from it appears in this folder. Every sentence here is written fresh, and every fact about the service comes from `docs/openloop-proposal-notes.md` or from our own live pages.

## The drafts

| Draft | File | Status | What is blocking it |
|---|---|---|---|
| Telehealth consent, public summary | `01-telehealth-consent.md` | Needs attorney. Needs OpenLoop papers. | The partner's signed consent document. State notices. Florida and New York weight-loss disclosures. Controlled substances confirmation. Recording answer. |
| Health information and HIPAA | `02-health-information-and-hipaa.md` | Needs attorney. Needs OpenLoop papers. | Link to the partner's Notice of Privacy Practices. Decision on Velacore's access to the partner dashboard and export. |
| Your privacy choices | `03-your-privacy-choices.md` | Needs attorney. | Dourado's open tracking decision. Whether state privacy laws apply. Deadlines. The no-sale wording. |
| Privacy policy, changes | `04-privacy-policy-changes.md` | Needs attorney. Needs OpenLoop papers. | Same tracking decision. Partner's privacy statement. Retention periods. |
| Terms, additions | `05-terms-additions.md` | Needs attorney. | Arbitration, class waiver, governing law, copyright agent, state notices. |
| Refund policy, additions | `06-refund-policy-additions.md` | Needs OpenLoop papers. | The partner's written refund policy. |
| Contact page | `07-contact-page.md` | Can go live after vc-reviewer. | Nothing, if the phone, address and portal lines are left out. Dourado supplies phone and address. |
| FAQ additions | `08-faq-additions.md` | Part A can go live after vc-reviewer. Part B needs OpenLoop papers. One answer needs attorney. | Nine questions for OpenLoop. |
| About page, outline | `09-about-page.md` | Can go live after vc-reviewer. | Dourado's people details, or his word to leave them out. |

## Fix first: things on the live site that are wrong today

Found while reading the live pages. These matter more than any new page.

1. `public/privacy.html` says we collect "the health and intake information you submit through our online questionnaire" and share with "our intake form provider". Neither is true since the platform change. It also says we maintain Business Associate Agreements where we handle health information. The page is dated July 22 2026. Corrected text is in `04-privacy-policy-changes.md`, clauses 3, 5 and 7.
2. `public/telehealth-consent.html` opens by saying that starting a visit means agreeing to that page. The binding consent is the one on the partner's intake. Corrected in `01-telehealth-consent.md`.
3. `public/script.js` sends Google an event with the program name when a live intake link is clicked on a page that carries the Google tag. It does not fire today because the links are placeholders. It should be settled before the intake links go live. Build change for Vale, tied to the tracking decision.
4. Nov 19 2026: "HIPAA-compliant" was removed from the FAQ, program pages and Learn article; do not add it back without OpenLoop's written confirmation. The refund policy and Terms say "Shipping is included". Both are vendor claims with no written source in the repo yet.
5. The live FAQ asks "Can I cancel or pause any time?" and answers only about cancelling.

## What the site collects, checked Nov 13 2026

Full table in `03-your-privacy-choices.md`. Short version:

- Google Analytics tag on the home page, FAQ, the Learn hub page, the six program pages, the four legal pages and the 404 page.
- No analytics on the six Start pages or the four Learn articles.
- Google Fonts on every page, Start pages included.
- UTM tags are copied onto the intake link and not stored.
- No forms, no accounts, no ad pixels, no cookies set by our own code.

## Decisions for Dourado

1. The tracking call: keep Google Analytics on program pages or take it off, and what, if anything, runs on Start pages. Three drafts wait on it.
2. Whether Velacore will use the partner's dashboard and export of patient details. If yes, the HIPAA page and privacy policy must say so, and counsel should say what agreement is needed first.
3. Phone number and mailing address for the Contact page, the privacy pages and the Terms.
4. People details for the About page, or leave them out.
5. Effective dates for each page on the day it goes live.
6. Whether to send Velacore marketing email or texts at all. Today we send neither, and the drafts say so.
7. Whether Velacore wants an arbitration clause. Counsel drafts it, but the choice is his.

## Questions for OpenLoop

Documents promised on the Nov 12 call and still needed:

1. The telehealth consent patients sign at intake.
2. The partner's privacy statement and its Notice of Privacy Practices, with a link we may publish.
3. The written refund policy.
4. The updated Agile proposal with every program and price, Glutathione included.

Questions, grouped by draft:

Consent
5. Do any of our six programs involve a controlled substance? Please confirm in writing that none does.
6. Are video visits, phone calls or support chats recorded? Who keeps the recordings and for how long?
7. Where does the patient see the clinician's name, license type and license number, and when?
8. Does the signed consent carry the state-specific telehealth notices?
9. Does the intake show the Florida and New York weight-loss program disclosures to patients in those states?
10. How does a patient get a copy of the consent they signed?
11. How are lab results delivered, and what happens when one needs urgent follow-up?
12. Which states require a live video visit for the first prescription? The proposal lists eight. The call said about seven.

Health information
13. What are the legal names of the medical group and the pharmacies, and may we name them?
14. Who is the contact for records requests and privacy complaints?
15. What exactly does the business dashboard and export show Velacore, and under what agreement? Is a Business Associate Agreement part of the service agreement?
16. Can you put "HIPAA-compliant platform" in writing, with whatever attestation backs it?

Billing and refunds
17. At what moment is the card first charged: at intake or after the clinician approves? Charge or authorization hold?
18. How many days does a refund take once approved?
19. How does a patient dispute a charge, and how long do they have?
20. What exact name appears on the card statement?
21. What happens with a lost, damaged or warm package? Replacement or refund, and how soon must it be reported?
22. What is the process for a wrong item or wrong dose?
23. Are cancellation and refund two separate requests? What is the cutoff before a billing date?
24. On a prepaid plan, how is the refund for unshipped months worked out?
25. Is shipping included in every program price? Please confirm in writing.

Support and portal
26. What is the patient portal address, and may we link to it?
27. What is the patient support phone number, and may we publish it? Is there a mailing address for disputes?
28. What texts and emails does the partner send patients, under what name, and what are its message terms?

FAQ
29. Does the intake ask for a photo ID, a selfie or both? What for, who sees them, how long are they kept?
30. Which carriers are used? Is a signature needed on delivery? Is cold packaging used?
31. Where in the portal does a patient change the card or shipping address, and what is the cutoff?
32. Can a program prescription be sent to a local pharmacy?
33. What are the typical times from intake to decision and from prescription to delivery, and may we publish them?
34. Can a patient pause without cancelling?
35. What are the eligibility rules for NAD+, Glutathione and Sermorelin?

## Questions for the attorney

1. Is First Venture Group LLC a business associate of the medical group, the pharmacy or the partner? Does that change if Velacore uses the patient dashboard and export?
2. Does our public consent page work as a summary that defers to the partner's signed consent, and is the deferral wording right?
3. State-specific telehealth notices: which are required on our site, as opposed to on the partner's intake?
4. Florida and New York weight-loss program disclosures: do they apply to a coordination platform, and if so what text and where?
5. Recording: may we ask patients not to record visits, given that state rules differ?
6. Confidentiality exceptions: is the plain-language summary accurate?
7. Do California and the other state privacy laws apply to us at our size? If not, should we offer the rights anyway?
8. Can we say "we do not sell or share personal information" with Google Analytics on the site? Is an opt-out link or a response to the Global Privacy Control signal required?
9. Does analytics data from a page named for one program count as consumer health data under the Washington and Nevada style laws? Is consent needed first? Is a separate consumer health data policy with its own home page link required?
10. Response deadlines, acknowledgment periods, request limits, appeal process and authorized agent rules for privacy requests.
11. Retention periods we should state.
12. Arbitration and class action waiver: whether to have them, and the drafting.
13. Governing law and venue: is Tennessee enforceable against consumers in other states?
14. Copyright complaints: register an agent and add the formal steps?
15. Text message terms, before Velacore sends any text.
16. Disclaimer, limitation of liability and indemnity in the Terms: each is one sentence today.
17. The sentence "A prescription written after a telehealth visit is a real prescription" in the FAQ draft.
18. Auto-renewal disclosures: the programs renew each period. Which state renewal rules apply, and do they bind us or the merchant of record?

## Categories outside our approved list

The reference site carries treatment categories that are not among Velacore's six approved programs. None of them is named or described anywhere in this folder, and no policy text was drafted for them. Adding any category is Dourado's decision, plus OpenLoop's confirmation in writing, plus vc-reviewer clearing it, as `COMPLIANCE.md` sets out.

## Checks

- Not run: the compliance scan. It reads `public/` only, and these drafts are in `docs/`. I also have no way to run scripts in this session. Each draft needs vc-reviewer before any of it moves into `public/`.
- Checked by hand: no long dashes, no round brackets, no emojis, no treatment outside the six, no named clinician, no outcome or weight claims, no brand-name comparisons, no retired fee or vendor names, "Prescription required" on every draft page that names a treatment, the compounded disclaimer on the two that list the programs.
- Order of next steps: fix the five live issues above, send the OpenLoop questions, book the attorney.

vc-copy

FOR DOURADO, Velacore Health
