# Your privacy choices

Status: Needs attorney.

Draft by vc-copy, Nov 13 2026. Not served. Nothing here is live.

New page. Suggested file `public/privacy-choices.html`. Suggested h1: Your privacy choices.

Attorney-review note, keep at the top of the working file: a copywriter wrote this from the structure of a typical state privacy notice. Whether any state privacy law applies to First Venture Group LLC at its current size, which rights must be offered, the response deadlines, and the legal label for our use of Google Analytics are all questions for counsel. No statute is cited and no deadline is stated. Not legal advice.

## What the site really collects, checked Nov 13 2026

Checked by reading the files in `public/`. This is the factual base for the page copy below.

| Where | What happens | Source |
|---|---|---|
| Home, FAQ, the Learn hub page, the six program pages, the four legal pages, the 404 page | A Google Analytics tag loads, ID ending DLF8. It sets cookies and sends Google the page address, device and browser details and an IP address. | The tag in each page head |
| The six Start pages | No analytics tag. A comment in the page says it stays off until Dourado makes the health-privacy call. | `public/start/*.html` |
| The four Learn articles | No analytics tag. | `public/learn/*.html` |
| Every page, Start pages included | Fonts load from Google Fonts. The browser contacts Google to fetch them, which shares an IP address. No cookie is set by this. | The font link in each page head |
| Every page | If the address carries ad tags that start with utm_, our script copies them onto the Continue link to the partner's intake. Google Analytics records them on the pages where it runs. No cookie and no browser storage is written by our own script. | `public/script.js`, the Start pages block |
| Pages with the Google tag | When someone clicks a live intake link, the script sends Google an event named start_visit_click with the program name and the link address. Today the intake links are placeholders, and Start pages carry no tag, so in practice the event does not fire. It would fire if a live intake link sat on a page that has the tag. | `public/script.js`, the intake links block |
| Whole site | No form, no login, no account, no checkout, no chat, no ad pixel from Meta or any other ad network. | Search of `public/` |
| Web host | The host keeps standard server logs. | Host is recorded in `docs/DEPLOY.md` |
| Email | Whatever a person writes to hello@velacorehealth.com. | Mailbox on Google Workspace |

## Flags before any of this goes live

1. The open tracking decision. `docs/HANDOFF.md` lists Google Analytics on program pages, and any tracking on Start pages, as an open health-privacy call for Dourado. A visit to a page named for one program can itself be health-related information under Washington and Nevada style laws. The copy below cannot be finished until that call is made.
2. The start_visit_click event sends a program name to Google. Recommend removing the program name from the event, or removing the event, before intake links go live. That is a build change for Vale, not a copy change.
3. "We do not sell personal information." Nothing in the site contradicts the plain meaning: no data is exchanged for money and there is no ad pixel. But some state laws define sale and sharing more widely, and whether Google Analytics falls inside those definitions depends on how the Google property is configured, which I cannot see from the repo. The sentence is written below with an attorney placeholder beside it.
4. Our site does not respond to browser opt-out signals today. Counsel should say whether it must.

## Page copy

### Effective date, element: p.updated

Effective [DOURADO: date this page goes live]

### Lede, element: div.legal-note p

This page explains the choices you have about personal information collected by the Velacore Health website. It covers this website only. Your health records are held by our telehealth services partner, the clinicians and the pharmacy, and your rights over those are explained on the Health information and HIPAA page, draft `02-health-information-and-hipaa.md`.

### h2: What this website collects

In the last 12 months this website has collected the following kinds of information.

| Kind of information | Examples | Where it comes from | Why |
|---|---|---|---|
| Online identifiers | IP address, cookie identifiers | Your browser | To deliver pages and count visits |
| Device and browser details | Browser type, screen size, operating system | Your browser | To make the site work on your device |
| Website activity | Pages viewed, links clicked, the site or ad that sent you here | Your browser and our analytics provider | To understand which pages are used |
| Contact details | Your name and email address | You, if you email us | To answer you |

This website does not collect health information, payment details, government ID numbers, precise location or account logins. It has no forms.

[Adjust this table after the tracking decision. If analytics comes off program pages, say so here.]

### h2: Who receives it

| Recipient | What they receive | Why |
|---|---|---|
| Our analytics provider | Online identifiers, device details, website activity | Visit measurement |
| Our web host | Online identifiers and device details in server logs | Serving the site and keeping it secure |
| Our font provider | Your IP address when your browser fetches fonts | Displaying the site's typefaces |
| Our email provider | The emails you send us | Running our mailbox |

We do not sell your personal information for money. We do not run advertising pixels on this site.

[NEEDS ATTORNEY: confirm whether "we do not sell or share personal information" can be stated without qualification given the Google Analytics tag, and whether an opt-out link or a response to browser opt-out signals is required]

### h2: Your choices right now

- You can block or delete cookies in your browser settings. The site works without them.
- You can browse the Start pages and Learn articles knowing they carry no analytics.
- You can ask us what we hold about you, or ask us to delete it, by email.

### h2: California

[NEEDS ATTORNEY: whether the California privacy law applies to First Venture Group LLC. If it does not, counsel should say whether to offer these rights anyway.]

If you live in California, you may have the right to:

- know what personal information we have collected about you, where it came from, why, and who received it
- ask for a copy
- ask us to correct it
- ask us to delete it
- opt out of any sale or sharing of your personal information
- limit the use of sensitive personal information, where that applies
- be treated the same whether or not you use these rights

We will not deny you service, charge you a different price or give you a different level of service because you made a request.

### h2: How to make a request

Email hello@velacorehealth.com with the subject line Privacy request. Tell us which right you want to use and which state you live in. Please do not include health details.

We will confirm we received it and reply within the time the law allows.

[NEEDS ATTORNEY: the acknowledgment and response deadlines to state here, and any limit on how often a person may ask in a 12 month period]

### h2: How we confirm it is you

Before we act on a request we need to be reasonably sure it comes from you. Because this site has no accounts, we will usually confirm by replying to the email address the request came from, and we may ask a question or two about your contact with us. We will not ask for a government ID or for health information.

[NEEDS ATTORNEY: confirm the verification method is sufficient]

### h2: Asking through someone else

You can have another person make a request for you. We will ask for your signed permission and may confirm directly with you before acting.

[NEEDS ATTORNEY: authorized agent requirements]

### h2: Other states

Several other states give their residents similar rights, such as the right to access, correct or delete personal information, to opt out of targeted advertising, and to appeal a decision we make on a request. If you live in one of those states, use the same email address and tell us where you live.

To appeal a decision, reply to our response and say you are appealing. [NEEDS ATTORNEY: the appeal process and deadline, and the list of states to name, if any]

### h2: Consumer health data, Washington, Nevada and similar laws

Some states have separate laws about consumer health data, meaning information that can link a person to a health condition, a treatment or an interest in one.

Here is how that applies to this website:

- We do not ask you for health information on this site.
- Your intake answers and health records are collected by our telehealth services partner, not by us.
- Visiting a page about a specific program could be treated as health-related information under these laws. [NEEDS ATTORNEY: whether analytics data from program pages counts as consumer health data, whether consent is required before it is collected, and whether a separate consumer health data privacy policy with its own link on the home page is required. This ties to Dourado's open tracking decision.]
- We do not sell consumer health data.

If you live in one of these states you may have the right to confirm whether we hold consumer health data about you, to access it, to withdraw consent and to have it deleted. Use the same email address.

### h2: Do Not Track and browser opt-out signals

This website does not currently change how it behaves when your browser sends a Do Not Track signal.

[NEEDS ATTORNEY: whether the site must honor the Global Privacy Control signal. If yes, Vale builds it before this page goes live and this paragraph is rewritten.]

### h2: Children

This website is for adults 18 and older. We do not knowingly collect personal information from anyone under 18, and we do not sell it.

### h2: Changes and contact

We will post any change to this page with a new effective date. Questions go to hello@velacorehealth.com.

[DOURADO: mailing address for privacy requests, if counsel says one is required]
