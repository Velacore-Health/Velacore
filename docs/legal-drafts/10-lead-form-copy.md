# Start page email box, copy and privacy policy change

Status: Needs attorney. Needs the partner's written answer. Needs Dourado's go. Nothing here can go live before all three.

Draft by vc-copy, Nov 20 2026. Not served. Nothing here is live. Nothing was sent.

Attorney-review note, keep at the top of the working file: drafted by a copywriter, not reviewed by counsel, not legal advice.

Serves the plan in `docs/start-lead-form-plan.md` and stays inside its limits: first name, email and state only, no program, no phone, no health question, no free text, and the Continue button always works without the box.

Two things in this draft differ from the brief on purpose. Both are explained in section 5, notes 1 and 2.

- The heading and the email do not promise to save a place in the intake, because nothing in the repo says a place is saved.
- The email does not state flatly that the visit was not finished, because nothing in the repo gives us a way to know that.

## 1. The box on the Start page

Sits in the Start page card, above the Continue button. Class names are left to Vale. The same words go on all nine Start pages, with no program name anywhere in the box.

### Heading, element: h2

Want to come back later?

### Help text, element: p

Leave your email and we will send you one link back to this site. This step is optional.

### Field labels, element: label

- First name
- Email
- State

First line of the state picker, element: option

Choose your state

### Button labels

- Save button, element: button, type submit: Save and continue
- No-save route, element: a.btn: Continue without saving

### Consent line, element: p, directly above the Save button

By choosing Save and continue, you agree that Velacore Health may email you once about finishing your visit. See our Privacy Policy.

The words Privacy Policy link to `../privacy.html`.

### Two extra lines Vale will need

- Email field error, element: p with role alert: Enter an email address so we know where to send the link.
- Save failed, element: p with role alert: We could not save your details. You can still continue to the secure intake.

### Removed from the old copy

Nothing. The box is new and every existing line on the Start page stays, including the price line, the three steps, the hand-off line and the fine print with the compounded medication disclaimer.

One overlap to settle in the build: the page already has a button that reads Continue to secure intake. With the box in place that button is the no-save route. Either it takes the label Continue without saving, or it keeps its current label and the box carries only the Save button. Both are fine for copy. See note 7 on how the two buttons must look.

## 2. The message after saving

Shown in place of the box once the save succeeds. It names no program.

### Message, element: p with role status

Saved. We will send one email to the address you gave, with a link back to this site.

### Second line, element: p

Next is the secure intake on our telehealth services partner's site. You will see their name there instead of ours.

### Button, element: a.btn.btn-primary

Continue to secure intake

Left out on purpose: when the email arrives. The plan says about a day, but the timing is not decided, so the page does not promise one.

## 3. The follow-up email

One email, sent once. Nothing is sent by vc-copy. The tool and the first send each need Dourado's OK.

### Subject

The link you asked for

Two other options:

- Your link from Velacore
- Here is your link

### Preview line

You asked us to email this so you could come back later.

### Body, 73 words

Hi [first name],

You asked us to email you a link so you could finish your visit later.

If your visit is still unfinished, this link takes you back to our site:

Return to Velacore Health

The link opens our home page, so you will choose where to begin.

If you already finished, please ignore this email. It is the only one we will send about this.

Questions go to hello@velacorehealth.com.

Velacore Health

### The one link

Return to Velacore Health points to `https://www.velacorehealth.com/#goals`, the home page chooser. [VALE: confirm the live address on the day. The address here comes from the canonical tag in `public/privacy.html`.] The link carries no tags that identify the person and no program name.

If the first name is blank, the greeting is: Hello,

### Footer line, placeholders

You got this email once because you asked for it at velacorehealth.com.

[PLACEHOLDER: unsubscribe link]

[PLACEHOLDER: business mailing address for First Venture Group LLC, doing business as Velacore Health. Dourado supplies it. None is in the repo.]

## 4. The privacy policy change

Applies to `public/privacy.html`. Only the parts the box touches are rewritten. Everything not listed here stays as it is. This section changes nothing on the live page; it is the wording for the day the box ships.

### Clause 1. Date, element: p.updated

Current text:

> Last updated: November 19, 2026

New text:

Last updated: [DOURADO: the date the box goes live]

### Clause 2. Scope, element: div.legal-note p

Current sentence:

> This policy covers this website and emails you send us.

New sentence:

This policy covers this website, emails you send us and the one email we send if you ask for it on a Start page.

### Clause 3. h2: Information we collect, first list item

Current text, both sentences are replaced:

> Information you give us: if you email us, we receive your name, your email address and whatever you write. This website has no forms, no accounts and no checkout.

New text:

Information you give us: if you email us, we receive your name, your email address and whatever you write. Each Start page has one optional box where you can ask for a link by email. If you use it, we receive your first name, your email address, your state and the date and time you saved them. This website has no accounts and no checkout.

Removed: "This website has no forms". Reason: the box is a form, so the sentence would be false the day it ships.

### Clause 4. h2: Information we collect, closing paragraph

Current first sentence, kept as it is:

> We do not collect health information, intake answers, identity documents or card details on this website.

New sentence added straight after it:

The Start page box does not ask about your health and does not record which program you were looking at.

[VALE: the second half is true only if the form service does not store the page address the box was sent from. The plan lists this as a check before building. If the service stores it, this sentence cannot ship as written.]

[NEEDS ATTORNEY: whether the kept sentence can still stand once the box exists. See note 3.]

### Clause 5. h2: How we use information, one new list item

New item, added after "To answer your emails.":

To send you one email with a link back to this site, if you asked for it in the Start page box.

### Clause 6. h2: How we share information, service providers item

Current text:

> Service providers that support this website, such as our web host, analytics provider, font provider and email provider.

New text:

Service providers that support this website, such as our web host, analytics provider, font provider, email provider and the service that stores the Start page box entries and sends the one email.

[DOURADO and VALE: where the list lives is not chosen. Reword this item once it is, so it describes the real service.]

### Clause 7. New section, element: h2 and paragraphs, placed after "How we share information"

Heading:

The optional box on Start pages

Text:

Each Start page has a box you can use to ask for a link by email. It is optional. You can continue to the secure intake without it.

If you use it, we collect your first name, your email address, your state and the date and time you saved them. The box does not ask about your health. It does not record which program you were looking at.

We use these details for one thing: to send you one email with a link back to this site.

[DOURADO: what the state is used for. No use is written anywhere in the repo, so none is stated here. See note 4.]

We do not sell these details. We do not give them to advertising companies and we do not use them to build advertising audiences.

We keep these details for 90 days and then delete them.

[PROPOSED: 90 days is the plan's proposal, not a decision. NEEDS ATTORNEY and Dourado's decision before it is published.]

To have them deleted sooner, email hello@velacorehealth.com from the address you saved and ask us to delete them. The email we send you also carries an unsubscribe link.

[NEEDS ATTORNEY: whether we must keep the address of a person who unsubscribes on a do-not-email list past 90 days, and how to say so here. See note 6.]

### Clauses not changed

How we share information other than the service providers item, the no-sale sentence, Your health information and HIPAA, Data security, Your choices, Cookies, Children, Changes, Contact. The page's meta description is also unchanged; it says the site "does not collect health information", which ties to note 3.

## 5. Notes for Vale

### Legal judgments I made that the attorney must confirm

1. No promise that a place is saved. The brief calls this a link to finish later. Nothing in the repo says the partner's intake keeps a half-finished visit, and the plan says our email can only link to the home page chooser. So the heading says come back later, the help text says a link back to this site, and no line says pick up where you left off. The consent line still says "about finishing your visit", as the brief asked. If the attorney reads even that as implying a saved place, change it to "about coming back to our site".

2. The email does not say flatly that the visit was not finished. The brief asked for that. The plan itself says the partner passes nothing back to us about who started, so I cannot trace any way for us to know who finished. A flat statement would be false for everyone who did finish, and a false statement in a commercial email is a legal risk. The body says "If your visit is still unfinished" and tells finishers to ignore it. If a lawful way to know is found, the flat line is: You started a visit with us and did not finish it. This also means the email goes to every person who saves, finished or not. Dourado should know that before he approves a send.

3. Whether this list is health information. I wrote what is factually true: the box does not ask about health and does not record the program. I did not write that the list is not health information, because that is a legal conclusion. A first name and email on a list of people who started a visit at a telehealth company may itself be treated as health information by federal and state regulators, with no program attached. The state field also tells us which entries come from Washington and Nevada. This is the plan's attorney question 1 and it decides whether the box can exist at all, whether the sentence "We do not collect health information" in the policy and in the meta description can stay, and whether the hard rule that patient health data never touches our systems is at risk.

4. The state field has no stated purpose. The plan lists it as a field but does not say what it is for. I could not write a use for it without inventing one, so the policy carries a placeholder. Collecting a detail with no use is hard to defend. Either Dourado names the use or the field comes off. Related: `docs/funnel-plan.md` section 3 and the question sent to the partner both say name and email only. The state goes beyond what the partner was asked to approve.

5. No checkbox. My judgment is that one is not needed for this email: the person types their details and presses a button whose only purpose is to save them, with the consent line directly above it, and federal commercial email law works on opt-out, not opt-in. That judgment fails if the attorney answers note 3 the other way. State health data laws ask for separate, affirmative consent, and a line under a button may not meet that. This is the plan's attorney question 3. If a checkbox is added it must start unticked.

6. The email is treated as a commercial email. I assumed it needs an unsubscribe link, a physical mailing address, a truthful subject line and a clear sender, even though the person asked for it. Three things follow that the attorney should confirm. First, an unsubscribe request has to be honored going forward, which may mean keeping that address on a do-not-email list longer than 90 days, against the deletion promise. Second, the consent line promises one email, so a second email of any kind to this list breaks the promise and the list must never feed a newsletter. Third, replies will land in a mailbox and may contain health details, which the email cannot warn against without naming a health topic.

7. The no-save route must not be harder to find than the save route. If Continue without saving is small or grey while Save and continue is the bold button, the box reads as a gate, which the plan rules out and which regulators treat as a pressure design. This is a design call for Vale, but it carries a legal edge, so it is listed here.

8. The sender name. The email body names no program, medication or health topic. The brand name itself contains the word Health, and it appears in the sender name, the sign-off, the link text and the mailing address line. I cannot remove it without hiding who the email is from. The attorney and Dourado should decide whether that is acceptable for an inbox other people can see.

9. Not sold and not used for advertising audiences. I wrote this as a flat promise because the plan says so. It is only true if the form service and the email tool are set up that way. Many email tools switch on click and open tracking by default, and some offer to sync lists to ad platforms. Those settings have to be checked on the chosen tool before the sentence ships. It also depends on the Start pages staying free of analytics and ad tags, which is true today per the comment at the top of each Start page.

10. Retention. The policy says 90 days, marked proposed. I left out the plan's second half, deletion at once when the person becomes a patient, because nothing in the repo shows how we would know who became a patient. Checking the list against the partner's patient records would itself be handling patient data. Plan attorney question 4.

11. Deletion requests. The policy says to email hello@velacorehealth.com from the saved address. It states no deadline for acting on a request. The attorney sets that, as with question 10 in the README.

12. Age. The site is for adults 18 and older and the policy says we do not knowingly collect from children. The box has no age question, and adding one would go beyond the plan's three fields. The attorney should say whether that is acceptable.

13. The scope sentence. I widened it to cover the one email we send. Small, but it changes what the policy says it covers.

### Claims I could not trace to the repo

- That the partner has agreed to a page that collects contact details before its intake. The plan says the answer is still awaited.
- Which service stores the entries, what it records with each one such as the page address or the IP address, whether it sets cookies, and what it costs. The plan lists these as unconfirmed. Three sentences in section 4 depend on the answers.
- Whether the partner's intake saves a half-finished visit.
- Any way to know whether a person who saved their details finished the intake.
- The purpose of the state field.
- The business mailing address. None is in the repo.
- The live site address for the email link. I used the canonical address in `public/privacy.html`; `CLAUDE.md` names a different host address.
- When the email is sent. The plan says about a day; nothing fixes it.

### Things for Vale outside copy

- The Continue button on every Start page is switched off today while the intake links are awaited. The box should not ship before the links do. It must not be reused as a way to collect emails for the day visits open; that is a different purpose and needs its own consent wording.
- These files also say the site has no forms and will be wrong the day the box ships: `docs/legal-drafts/03-your-privacy-choices.md`, `docs/legal-drafts/04-privacy-policy-changes.md` clauses 3 and 11, `docs/legal-drafts/07-contact-page.md`, `docs/legal-drafts/README.md`, `docs/DEPLOY.md`. I touched none of them.
- If first name and state are not needed to send the link, the email field could be the only required one. That is a build choice with a privacy upside.

### Checks

- Not run: the compliance scan. I have no way to run scripts in this session, and its claim checks read `public/` only. vc-reviewer must clear the box, the policy change and the email before any of it moves.
- Checked by hand: no long dashes, no round brackets, no emojis, no all-caps labels, no trailing arrows, no dollar figures, no program or medication named, no outcome claims, no pressure wording, the partner named only as our telehealth services partner, and the email body counted at 73 words.

vc-copy

FOR DOURADO, Velacore Health
