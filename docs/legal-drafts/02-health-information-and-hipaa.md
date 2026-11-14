# Health information and HIPAA

Status: Needs attorney. Needs OpenLoop papers.

Draft by vc-copy, Nov 13 2026. Not served. Nothing here is live.

New page. Suggested file `public/health-information.html`. Suggested h1: Health information and HIPAA.

Attorney-review note, keep at the top of the working file: this page is a plain-language explanation, not a Notice of Privacy Practices. Velacore does not claim to be a HIPAA covered entity anywhere on it. Whether Velacore is a business associate of anyone, and whether any agreement is needed for the patient export the partner's dashboard offers, is a question for counsel. Not legal advice.

## Why this page exists

The reference site publishes a pharmacy-style privacy notice in which the site operator names itself as the covered entity, with no effective date. We do not copy that. Velacore's site receives no health data, so the honest page is a short one that says who holds the records and where the real notice comes from.

## Page copy

### Effective date, element: p.updated

Effective [DOURADO: date this page goes live]

### Lede, element: div.legal-note p

Velacore Health is a coordination platform. We are not your doctor or your pharmacy, and this website does not collect or store your health information. This page explains who does hold it and what rights you have.

### h2: Who holds your health records

When you start a visit, you leave this website and continue on our telehealth services partner's secure pages. Your intake answers, your identity documents, your clinician's notes, your prescriptions and your lab results are collected and kept there.

Three parties handle that information so your care can be delivered:

- our telehealth services partner, which runs the intake, billing, support and the patient portal
- the independent medical group whose licensed clinicians review your intake
- the licensed 503A pharmacy that fills a prescription if one is written

[NEEDS OPENLOOP: the legal names of the medical group and the pharmacy or pharmacies, and whether they may be named on this page]

### h2: Where the Notice of Privacy Practices comes from

Health care providers must give you a Notice of Privacy Practices. It explains how they may use and share your health information and what your rights are. Yours comes from the medical group and the pharmacy, through our telehealth services partner. It does not come from Velacore.

You will see it [NEEDS OPENLOOP: where and when the patient is shown the Notice of Privacy Practices, at intake, in the portal, or both].

You can read it here: [NEEDS OPENLOOP: link to the partner's Notice of Privacy Practices]

### h2: Your rights over your health information

These are the usual rights patients have with their health care providers. The Notice of Privacy Practices you receive sets out the exact terms, and it is the one that applies.

- Access. You can ask to see your health records or get a copy.
- Amendment. You can ask for a correction if you believe something in your record is wrong or incomplete.
- Accounting. You can ask for a list of certain times your information was shared.
- Restrictions. You can ask for limits on how your information is used or shared. The provider does not have to agree to every request.
- Confidential communications. You can ask to be contacted in a certain way or at a certain address.
- A copy of the notice. You can ask for a paper copy at any time.
- Complaints. You can complain if you believe your privacy rights were not respected. You will not be penalized for doing so.

### h2: How to use these rights

Send requests about your health records to the party that holds them, not to Velacore.

[NEEDS OPENLOOP: the contact route for records requests and privacy complaints, and the name or title of the privacy officer if one is published]

You may also file a complaint with the Office for Civil Rights at the US Department of Health and Human Services.

[NEEDS ATTORNEY: confirm how the federal complaint route should be described and whether to link to it]

If you email us a request about your health records by mistake, we will point you to the right contact. We will not be able to look up or change your records ourselves.

### h2: What Velacore does and does not see

What this website does not do:

- It has no intake form, no login and no place to type health details.
- It does not receive your intake answers, your diagnosis, your prescription or your lab results.
- It does not hold your card details.

What Velacore may see:

- Ordinary website visit data, as described in our Privacy Policy, draft `04-privacy-policy-changes.md`.
- Anything you choose to send us by email. Please do not email health details.
- [NEEDS OPENLOOP and NEEDS ATTORNEY: our partner offers Velacore a business dashboard and export that may show a patient's name, email, phone, program, last medication, subscription status and billing dates. Decide before launch whether Velacore will access it, under what written agreement, and how this paragraph should describe it. Until that is decided, this page cannot honestly say Velacore never sees patient information.]

### h2: Questions

For questions about this page, email hello@velacorehealth.com. For questions about your care or your records, use the patient portal or contact patient support.

## Open items on this draft

1. Link to the partner's Notice of Privacy Practices.
2. The dashboard and export question above. This is the most important open point on the page. The dashboard fields come from the Nov 12 call notes in `docs/HANDOFF.md`.
3. Whether a Business Associate Agreement exists or is needed between First Venture Group LLC and the partner. The proposal notes say BAA, indemnity and breach terms have not been seen.
4. The live FAQ says the partner's platform is "HIPAA-compliant". That is a vendor claim with no written source in the repo yet. Ask OpenLoop for it in writing or soften the FAQ line.
