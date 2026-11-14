# Privacy policy, additions and rewrites only

Status: Needs attorney. Needs OpenLoop papers.

Draft by vc-copy, Nov 13 2026. Not served. Nothing here is live.

Applies to `public/privacy.html`. Only the clauses the platform change touches are rewritten. Everything not listed here stays as it is.

Attorney-review note, keep at the top of the working file: drafted by a copywriter, not reviewed by counsel, not legal advice.

## The live page is out of date, please read this first

The live policy is dated July 22 2026, before the platform change. Three statements in it no longer match how the site works:

1. "Information we collect" says we collect "the health and intake information you submit through our online questionnaire". We have no questionnaire. Intake runs on the partner's hosted pages.
2. "How we share information" names "our intake form provider". That was the retired form tool. There is none.
3. "Your health information and HIPAA" says "Where we handle protected health information on their behalf, we maintain Business Associate Agreements with vendors". The site handles none, and the repo holds no such agreement for the new partner.

These should be corrected even if nothing else in this folder ships.

## Section by section comparison

| Topic | Live page | Action |
|---|---|---|
| Effective date | Has "Last updated: July 22, 2026" | Rewrite, clause 1 |
| Scope | One sentence | Rewrite, clause 2 |
| Categories collected | Present, wrong | Rewrite, clause 3 |
| Uses | Present | Small rewrite, clause 4 |
| Sharing | Present, names intake form provider | Rewrite, clause 5 |
| Hand-off to the partner | Missing | New, clause 6 |
| HIPAA | Present, wrong | Rewrite, clause 7 |
| Cookies and analytics | Two vague sentences | Rewrite, clause 8 |
| Do Not Track | Missing | New, clause 9 |
| Text messages | Missing | New placeholder, clause 10 |
| Email | Missing | New, clause 11 |
| Retention | Missing | New, clause 12 |
| Security | Present | Keep |
| Choices | Present | Rewrite to link out, clause 13 |
| Children | Present | Keep |
| State privacy rights | Missing | New, by link, clause 13 |
| Third-party links | Missing | New, clause 14 |
| United States only | Missing | New, clause 15 |
| Changes | Present | Keep |
| Contact | Email only | Rewrite, clause 16 |

## Clauses changed

### Clause 1. Effective date, element: p.updated

Effective [DOURADO: date this version goes live]

Removed: "Last updated: July 22, 2026". Reason: the date predates the platform change.

### Clause 2. Scope, element: div.legal-note p

This Privacy Policy explains what the Velacore Health website collects, how it is used and who receives it. Velacore Health is operated by First Venture Group LLC. This policy covers this website and emails you send us. It does not cover the secure intake, patient portal, billing or medical records run by our telehealth services partner, the clinicians and the pharmacy. Those are covered by their own privacy notices, which you see when you start a visit.

### Clause 3. h2: Information we collect

- Information you give us. If you email us, we receive your name, your email address and whatever you write. This website has no forms, no accounts and no checkout.
- Information collected automatically. When you visit, your browser sends your IP address, device and browser type, the pages you view, the links you click and the site or ad that sent you here. Our analytics provider and our web host receive this.
- Ad tags in the page address. If you arrive from an ad, the address may carry tags that start with utm_. If you continue to the secure intake, those tags travel with the link so our partner can tell which ad you came from. We do not store them.

We do not collect health information, intake answers, identity documents or card details on this website.

Removed: "the health and intake information you submit through our online questionnaire" and the payment bullet. Reason: neither happens on our site any more.

### Clause 4. h2: How we use information

- To run, secure and improve this website.
- To understand which pages people use.
- To answer your emails.
- To meet legal requirements.

Removed: "To coordinate your access to licensed clinicians and 503A compounding pharmacies" as a use of data, and the line about orders and accounts. Reason: the coordination happens by linking you to the partner, not by handling your data.

### Clause 5. h2: Who receives information

- Our analytics provider, which receives website visit data.
- Our web host, which keeps standard server logs.
- Our font provider, which receives your IP address when your browser fetches the site's fonts.
- Our email provider, which stores the emails you send us.
- Authorities, when the law requires it or to protect rights and safety.

We do not sell your personal information for money and we do not run advertising pixels on this site.

[NEEDS ATTORNEY: confirm the no-sale sentence as worded. See the flags in `03-your-privacy-choices.md`.]

Removed: licensed clinicians, pharmacies and "our intake form provider" as recipients of data from us. Reason: we do not hold that data to share.

### Clause 6. h2: When you start a visit, new

When you press Continue on a Start page, you leave this website. The next page belongs to our telehealth services partner, and you will see their name there instead of ours. From that point on:

- your intake answers, identity check, payment and medical records are collected by the partner, the clinicians and the pharmacy
- their privacy notice and their Notice of Privacy Practices apply, not this policy
- Velacore does not receive your intake answers or your card details

[NEEDS OPENLOOP: link to the partner's privacy statement, promised on the Nov 12 call]

[NEEDS OPENLOOP and NEEDS ATTORNEY: what patient information Velacore can see in the partner's business dashboard and export, and how to describe it here. Same open point as in `02-health-information-and-hipaa.md`.]

### Clause 7. h2: Your health information and HIPAA

Your health information is held by our telehealth services partner, the independent clinicians and the pharmacy. They are responsible for it under federal and state health privacy law and they give you their own Notice of Privacy Practices. This website does not collect or store health information. Read more on the Health information and HIPAA page, draft `02-health-information-and-hipaa.md`.

Removed: the sentence about Business Associate Agreements. Reason: it describes an arrangement the repo cannot support for the new partner.

### Clause 8. h2: Cookies and analytics

We use Google Analytics to count visits and see which pages are used. It sets cookies in your browser and receives your IP address, device details and the pages you view. It runs on the home page, the FAQ, the Learn page, the program pages and the legal pages. It does not run on the Start pages or on the Learn articles.

Our own code sets no cookies. The site's typefaces load from Google Fonts, which means your browser contacts Google to fetch them.

You can block or delete cookies in your browser settings. The site works without them.

[Rewrite this clause after Dourado's tracking decision. The page list above is true as of Nov 13 2026 and must be rechecked on the day this goes live.]

Removed: "We use cookies and similar technologies for functionality and analytics". Reason: too vague, and we use none for functionality.

### Clause 9. h2: Do Not Track, new

This website does not currently change how it behaves when your browser sends a Do Not Track signal.

[NEEDS ATTORNEY: whether the Global Privacy Control signal must be honored]

### Clause 10. h2: Text messages, new, placeholder

Velacore does not send text messages today. If that changes, this section will explain what we send, how often, how to stop by replying STOP, how to get help by replying HELP, and that message and data rates may apply. We will ask for your consent first.

Texts about your care, your order or your account come from our telehealth services partner under their terms.

[NEEDS OPENLOOP: what texts the partner sends patients, from what name, and the partner's own text terms]

[NEEDS ATTORNEY: full text message terms before Velacore sends any text]

### Clause 11. h2: Email, new

If you email us, we use your address to reply. We do not add you to a marketing list unless you ask. Every marketing email will carry an unsubscribe link. Please do not send health details by email.

### Clause 12. h2: How long we keep information, new

- Emails you send us are kept as long as needed to answer you and keep a record of the exchange. [DOURADO and NEEDS ATTORNEY: the retention period for the hello@ mailbox]
- Analytics data is kept for the period set in our analytics account. [DOURADO: read the data retention setting off the Google Analytics admin screen. Not stated here until confirmed.]
- Server logs are kept by our web host under its own schedule.

Health records are kept by the partner, the clinicians and the pharmacy for as long as the law requires them to. We do not set that period.

### Clause 13. h2: Your choices

You can ask what we hold about you, ask us to correct or delete it, and opt out of marketing email, by writing to hello@velacorehealth.com. State-specific rights, including California, Washington and Nevada, are on the Your privacy choices page, draft `03-your-privacy-choices.md`. Rights over your health records are on the Health information and HIPAA page, draft `02-health-information-and-hipaa.md`.

### Clause 14. h2: Links to other sites, new

This site links to our telehealth services partner's pages and may link to other websites. We do not control them. Their own privacy notices apply once you leave this site.

### Clause 15. h2: United States only, new

This website and the programs on it are for people located in the United States. We do not offer the service elsewhere. If you visit from another country, your information is processed in the United States.

### Clause 16. h2: Contact

Questions about this policy go to hello@velacorehealth.com.

[DOURADO: mailing address for First Venture Group LLC, if you want one shown. None is written here.]

## Clauses not changed

Data security, Children, Changes.

## Design notes for Vale, outside copy

The four legal pages carry a small "Legal" label above the heading and a long dash in the browser title. Both go against the design checklist and the no long dash rule. Worth fixing when these pages are next built.
