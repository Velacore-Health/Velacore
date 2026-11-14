# Velacore funnel plan

Written Nov 13 2026 at Dourado's direction. The site has to sell without looking spammy. Every page has one job, every button has one purpose, and we decide what the visitor sees next. Nothing here changes a compliance rule: no outcome claims, no testimonials until real consented ones exist, no LegitScript badge until it is issued, and patient health answers never touch our pages.

## What the site does today, and where people leak

1. Every Start visit button on the home page jumps to the bottom of the page, where the visitor has to pick the program a second time. That is an extra click for someone who already chose.
2. The home page has 23 buttons and links of nearly equal weight. Learn more, Start visit, Meet the clinicians, How it is made, Support and FAQ, Refund policy. The visitor has to decide what matters.
3. The Start visit links go nowhere yet. They wait on the Agile intake links from OpenLoop.
4. When the links do arrive, the visitor jumps from a branded Velacore page straight into a generic Agile form. On the Nov 12 call OpenLoop agreed that a short primer page in between would ease that jump.
5. Nothing measures where people drop. Google Analytics is on the pages, but no button click is tracked.

## The funnel we want

```
Ad or search  ->  Program page  ->  Start page  ->  Agile intake  ->  Clinician  ->  Pharmacy
                  one program,     what happens     OpenLoop's
                  one button       next, one        secure form
                                   button
Home page     ->  pick a goal  ->  Program page  ->  same path
```

### 1. Program pages are the landing pages

Ads point at a program page, never the home page. Each program page does one thing: get the visitor to start that program's visit.

- One primary button, Start your visit, at the top, after the facts, and at the bottom. On a phone a slim bar with the price and the button stays at the bottom of the screen.
- Order of the page, built to answer the questions people have before they click: what it is and what it costs, how it works in four steps, what is included, who reviews it, the refund promise, questions, then the button again.
- Secondary links fade back: See all programs stays, everything else moves to the footer.

### 2. The home page routes, it does not sell everything at once

- Hero: the vial group shot, one line, the starting price, and one button: Find your program.
- Right under it, three goal tiles: Weight, Vitality, Hormone support. Each opens a short row of that goal's programs. Each program card has one button that goes to its program page.
- Then trust, in this order: how it works, who the clinicians are, the refund promise, questions.
- The bottom section stops asking the visitor to pick again. It becomes a short close: one line and Find your program.

### 3. A Start page between us and the intake

One page per program, for example `start/tirzepatide.html`. It is the only place a Start visit button leads.

- Shows: the program and its price, what happens next in three short lines, about 5 to 10 minutes for the intake, a licensed clinician reviews it, refunded in full if not prescribed.
- Says plainly that the visitor continues on our telehealth partner's secure site, which shows the partner's name.
- One button: Continue to secure intake. It carries the ad's tracking tags into the Agile link.
- Later, only if OpenLoop's IT says yes and only name and email: an optional "send me a link to finish later" box, so a visitor who leaves can be reached again. No health questions, ever.
- This page is where we measure. Every visit to a Start page and every Continue click is counted, so we know how many ad clicks became intake starts.

### 4. Every other page ends in the funnel

Learn, FAQ, the clinicians section and the legal pages each end with one line and Find your program. No dead ends.

### 5. Measurement

- Google Analytics events on: Find your program, each goal tile, each program card, Start your visit, Continue to secure intake.
- UTM tags from the ad carried through to the Agile link, per OpenLoop's note that Agile tracks UTM only.
- Any tracking on our pages goes through a health-privacy check first; Start pages name a program, which can be sensitive.

## Images this plan needs

1. Three goal tiles, from Gemini, using the vial photos as references so labels stay right:
   - Weight: Microdosing GLP-1, Semaglutide and Tirzepatide on the marble risers.
   - Vitality: NAD+ and Glutathione on the marble risers.
   - Hormone support: Sermorelin alone on one marble riser.
2. A Start page image: calm and quiet, no text on screen. Candidate: the existing step-visit photo, cropped.
3. A share image for links and ads, 1200 by 630, from the hero group shot plus the wordmark. Made here, no Gemini needed.

## Order of work

1. Goal tile images, now, in Gemini.
2. Home page routing and the Start pages, built with placeholders until the Agile links arrive.
3. Program page layout and the phone price bar.
4. Click tracking, after the privacy check.
5. Copy for every new line through vc-copy; everything through vc-reviewer before a push.

FOR DOURADO, Velacore Health
