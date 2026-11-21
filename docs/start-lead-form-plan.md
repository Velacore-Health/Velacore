# Lead form before the intake, plan

Draft by Vale, Nov 20 2026, on Dourado's "maybe draft it now". Nothing here is built or public. It waits on three things: OpenLoop's written answer, the attorney's read, and Dourado's go.

## Why

Dourado tested the other Agile partner site's Start page on Nov 20: it takes a name, email, phone, state and the program of interest, shows a short "next: your secure intake" screen, then opens the Agile intake. Agile passes nothing back to us about who started, so without a step like this we never learn who clicked Continue and left. Our own funnel plan, docs/funnel-plan.md section 3, already lists this as a later step: only name and email, only if OpenLoop agrees, no health questions.

## What we would build

On each Start page, above the Continue button, one optional box. The Continue button always works without it.

- Heading: a plain line offering to email a link to finish later.
- Fields: first name and email. Nothing else. A state field was in the first draft and came out the same day: nothing we would do needs it, it goes beyond the name and email OpenLoop was asked about, and it marks which entries fall under the strictest state privacy laws.
- One consent line under the fields, linking the privacy policy.
- Two ways forward: Save and continue, or Continue without saving.

Not at launch: a state, a phone number, text messages, last name, date of birth, any health question, any free text box.

The box ships only together with the real intake links. The Continue button is switched off today, and the box is never used to collect emails for the day visits open.

## What is stored, and what is not

- Stored: first name, email, the date and time.
- Not stored: the program. The form sends no program field, and every Start page posts to the same form name, so a saved lead does not say which program page it came from. Check before building: whether the form service also records the page address the form was sent from. If it does, the program is stored after all and the attorney's answer below decides it.
- Never sent to Meta, Google or any ad tool, as a list or as an event with the email attached. The Continue click can still be counted with no personal details.

Why the program is left out: an email address next to a program name is health information about a named person. Regulators treat it that way, and it would break the rule in CLAUDE.md that patient health data never touches our systems. The cost is that a follow-up email cannot name the program; it links to the site's chooser.

## Where it would live

Options, cheapest first. None chosen; each needs Dourado's OK and an entry in docs/installs.md or docs/DEPLOY.md.

1. The site host's own form feature. No new vendor and no server code. Unconfirmed: what the current host plan includes, what it costs past the included amount, and what extra details it records with each entry.
2. An email tool with its own hosted form. Adds a vendor and a monthly cost, and gives the follow-up email in the same place.

Either way the list is exported only to the business Drive or the email tool, never to this repo.

## The follow-up email

One email, sent once, about a day after someone saves. The partner passes nothing back about who finished, so we cannot tell who did: the email goes to everyone who saved, says so plainly, and tells finishers to ignore it. It names no program and no medication, in the subject or the body, because other people can see an inbox. It says the visit was not finished, links to the home page chooser, and carries the unsubscribe link and the business mailing address that commercial email law requires. Sending anything needs Dourado's OK for the tool and the first send.

## What must change before it goes live

- public/privacy.html says "This website has no forms, no accounts and no checkout." That sentence and the "Information you give us" paragraph change, and the policy's effective date moves.
- The Start pages gain the box, and the site audit gains a check that the form has no program field and no health field.
- docs/DEPLOY.md line "No forms, no server code" changes.
- COMPLIANCE.md gets the decision and its limits.
- vc-reviewer reviews the page, the policy and the email before anything ships.

## Questions for the attorney

1. With first name and email only, and no program, is this ordinary contact data under the state health privacy laws, including Washington's and Nevada's? A list of people who started a visit at a telehealth company may count as health information by itself.
2. If the form service records the page address, and the address names the program, does that change the answer? Should the Start pages then post from one shared address?
3. Is the consent line enough for one follow-up email, or does it need a checkbox?
4. What must the privacy policy say about who stores the list and how long it is kept? Proposed: deleted after 90 days. An unsubscribe must still be honored after that, which may mean keeping that one address on a do not email list; the policy has to say so.
5. Does our Business Associate Agreement with the partner bear on this list at all?

## Question already with OpenLoop

Asked in Dourado's Nov 20 reply: may we have a page before the intake that collects only a name and email. Waiting on the answer.

## Found while drafting the words

vc-copy's draft is docs/legal-drafts/10-lead-form-copy.md, with 13 points for the attorney. The ones that shape the build:

- The promise that the list is not used for advertising depends on the email tool's settings. Many switch on open and click tracking by default; those go off.
- Nothing shows the partner keeps a half finished intake, so no line promises a saved place. The email links to the home page chooser.
- The email needs a business mailing address, and none is in the repo.
- Five other files say the site has no forms and change the day the box ships: legal drafts 03, 04 and 07, the legal drafts README, and docs/DEPLOY.md.

## What we are not copying from the other site

The program question on the form, the state, the phone number, the text message opt-in, and making the form a gate that must be filled before the intake opens.

## Order of work once all three say yes

1. Dourado picks where the list lives.
2. vc-copy's wording, in docs/legal-drafts/10-lead-form-copy.md, goes to the attorney with the questions above.
3. Vale builds the box on one Start page for a local preview, then all nine.
4. vc-reviewer, then Dourado's push OK.
