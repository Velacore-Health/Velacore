# Funnel copy, home goal chooser and Start pages

Written Nov 13 2026 by vc-copy for the plan in `docs/funnel-plan.md`. Not yet cleared by vc-reviewer. Nothing here is live until Dourado says so.

Prices are tokens. On OpenLoop Agile, OpenLoop sets the retail price, so every price stays a placeholder until the Agile proposal is in writing. Pull prices from the program data in `tools/build_programs.py`, never type them by hand.

## 1. Home page

### Hero button

- a.btn.btn-primary: Find your program
- Links to the goal chooser right under the hero.
- Removed: the second hero button, See programs and prices. The plan asks for one button in the hero, and the chooser right below does the same job.

### Goal chooser, right under the hero

- h2: Choose where to start
- p.section-sub: Every program is prescription only. A licensed clinician reviews your intake and decides what is appropriate.

Tile 1

- h3: Weight
- p: Three GLP-1 programs: Tirzepatide, Semaglutide and Microdosing GLP-1.
- button: See weight programs

Tile 2

- h3: Vitality
- p: Two programs: NAD+ and Glutathione, in the form your clinician prescribes.
- button: See vitality programs

Tile 3

- h3: Hormone support
- p: One program: Sermorelin, a growth hormone-releasing hormone analog.
- button: See the Sermorelin program

Note: tile lines name what is inside and nothing more. No benefit words, so the tile titles carry the category and the lines stay mechanistic.

### Closing section, replaces "Your visit starts here" and its program list

- h2: Ready when you are
- p: Choose a program to see its price and what happens next. A licensed clinician makes every prescribing decision, and you are refunded in full if you are not prescribed.
- a.btn.btn-primary: Find your program
- p.intake-fine: Prescription required. Starting a visit is not a guarantee of treatment. Compounded medications are not FDA approved.
- Removed: the six program buttons. They made a visitor choose a program a second time. The fine print stays because the home page names treatments.

## 2. Start page template, one per program

File pattern: `public/start/<slug>.html`. Tokens: {Program}, {first_month_price}, {monthly_price}.

### Head

- title: Start your {Program} visit | Velacore Health
- meta description: Before your {Program} visit: a short online intake on our telehealth partner's secure site, review by a licensed clinician, and a full refund if you are not prescribed. Prescription required.

### Body

- h1: Before you start your {Program} visit
- p.price-note: {first_month_price} your first month, then {monthly_price} a month. Shipping included. Cancel any time.

What happens next, ol.steps, three items

1. You fill in a secure online intake. It takes about 5 to 10 minutes.
2. A licensed clinician in your state reviews it and decides whether {Program} is appropriate for you.
3. If you are prescribed, a licensed 503A pharmacy fills your order and ships it to you. If not, your payment is refunded in full.

Hand-off sentence, p

- The next page is our telehealth partner's secure site, so you will see their name there instead of ours.

Optional second sentence, only if vc-reviewer agrees it is accurate for Agile:

- Your health answers go to them, not to us.

Buttons

- a.btn.btn-primary: Continue to secure intake
- a.back-link: Back to {Program}

Placeholder while the intake link is not live, replaces the primary button

- p: The online visit for {Program} opens soon. In the meantime, email hello@velacorehealth.com with any questions.
- The email address is a mailto link.

Fine print, p.intake-fine, same wording as the program pages

- Prescription required. Starting a visit is not a guarantee of treatment. Compounded medications are not FDA approved and are not reviewed by the FDA for safety or efficacy. Individual results vary. Not appropriate for everyone. Your clinician decides whether this program is appropriate for you.

## Open points for Vale and vc-reviewer

1. The 5 to 10 minute intake time comes from the funnel plan, not from OpenLoop in writing. Confirm it with OpenLoop or change the line to: It takes a few minutes.
2. CLAUDE.md still says Glutathione is off the site since Nov 6. COMPLIANCE.md says Dourado put it back on Nov 13 on the strength of the Nov 12 call, verbal only. This copy follows COMPLIANCE.md. If the written Agile proposal leaves Glutathione out, Tile 2 becomes: One program: NAD+, as an injection, nasal spray or oral dropper. Button: See the NAD+ program.
3. The tile titles Weight, Vitality and Hormone support come from the plan. vc-reviewer should confirm they read as categories, not as claims.
4. Start pages name a program, which can be sensitive. Suggest noindex on them and the health-privacy check from the plan before any tracking runs there.

vc-copy

FOR DOURADO, Velacore Health
