# Visual direction, Nov 17 2026

Written for Dourado after the Hims study, while he slept. This is the list he asked for: the colors and backgrounds we would use for edgier imagery, how every image should be oriented, and what moves on the site. Nothing here is built unless it says so. The brand bible in `docs/BRAND.md` stays the rule book; this file says how to push it.

What Hims does that we are copying: one idea per screen, a photo or a product doing the talking, a button after every section, cards in a color that tells you the category before you read a word. What we never copy: their outcome claims, their badges, their products, their copy, their look.

## 1. Colors

Already on the site, from BRAND.md:

| Name | Hex | Where it lives |
|---|---|---|
| Paper | #FFFFFF | Page background |
| Mint | #EEF5F1 | Every other section, image backdrops |
| Mint deep | #DDF0E7 | Soft blocks, the Not sure card fade |
| Pine | #15302A | All text, the dark band, the footer, every vial cap |
| Pine soft | #4C625B | Second line text |
| Jade ink | #0A7A61 | Every button and link |
| Jade tint | #C9EEDF | Icon backgrounds, highlights |

New on Nov 17, the goal tints. Built into the home program cards tonight. Each goal owns one, so a visitor learns the color before the name:

| Goal | Hex | Comes from |
|---|---|---|
| Weight | #E4EBF9 | Pale helix blue |
| Vitality | #ECE6F8 | Pale helix violet |
| Hormone support | #D9F0E6 | Pale jade |

Where the goal tints can go next, in order: the chooser goal tiles, the program page hero band, the panel goal rows, the pricing cards. One tint per surface, never two side by side on one card.

The gradient rule, changed tonight: a fade is allowed when it runs between two close tones over a short distance. White to a goal tint on a card body is the model. That is what keeps it from banding; banding shows up when a gradient crosses a long distance or two strong colors. Never a fade under text that needs the color to be readable. Never a glow, never a spotlight, never a dark fade.

For edgier imagery, the darker end of the palette we would use, none of it on the site yet:

| Name | Hex | Use |
|---|---|---|
| Pine | #15302A | A full dark background behind one vial, the cap and label still readable |
| Pine 2 | #1F3F37 | The lighter dark surface, for a card on pine |
| Deep marble | a white marble slab lit low, the gray veins strong | Product on stone with mood |
| Helix blue | #3E5FC0 | One colored rim light on glass, never a wash |
| Helix violet | #8A6BC9 | Same, for the vitality vials |

## 2. Backgrounds

Product shots, the set we have: vial on a white marble riser, white marble table, pale mint wall fading to white, daylight from the upper left. This stays the catalog look on every card and program page.

Three edgier sets we could add, each a Gemini edit of the approved vial photo so the label never changes. Pick one and the prompts go into `docs/gemini-queue.md`:

1. Marble, low light. Same vial, same marble, but the wall goes to deep mint shadow and the light comes from one side so the glass catches a hard highlight. Use: the home hero, one big photo per goal.
2. Pine studio. The vial on a pine ground, matte, with a soft pool of light under it and one thin rim of the program color along the glass edge. Use: the dark band on the home page, the pricing page header, social.
3. Frosted glass. The vial behind a sheet of frosted glass with the mint wall behind, only the label sharp. Use: section dividers, the Learn page, the video poster.

Lifestyle photos stay as BRAND.md says: real homes, cool daylight, adults 35 to 60, no gym, no scale, no needle. The edgier move there is tighter crops and more shadow, not different people.

Section backgrounds on the site, in order of weight: paper, mint, a goal tint, pine. One pine band per page at most.

## 3. How images are oriented

| Image | Shape | Rule |
|---|---|---|
| Vial on a card | Square, 1 by 1 | Vial fills three quarters of the height, cap at the top fourth, label dead center. Built tonight. |
| Vial on a program page | Portrait, 3 by 4 | Same vial, more table below it, room for the stripe. |
| Vial on the hero | Wide, 4 by 3 or wider | Two or three vials in a row on one slab, the lead program nearest the camera. |
| Menu thumbnail | Square, 216 px | A close crop on the label, nothing else. Done. |
| Goal tile | 4 by 3 | The vials for that goal, grouped, shot a little from above. Done. |
| Lifestyle, a step | 4 by 3 | The person off center, the action readable at phone size, nothing important in the outer fifth on each side because phones crop it. |
| Lifestyle, a band | 21 by 9 | Faces in the middle third. Only where the band is the one picture on that screen. |
| Video poster | 16 by 9 | The first frame of the film, no text. |

Phone first on every one: the subject must read at 375 wide. Every image carries width and height so the page never jumps. The first image on a page loads at once, the rest lazy.

## 4. What moves

On the site now:

- The slide-in menu. The panel slides from the right, the page behind dims. Built Nov 17.
- The program row. Drag, swipe, or the two arrows; it snaps to each card. Built Nov 17.
- The chooser. Each step fades up when it opens. Built Nov 17.
- The hero menu rows nudge right by 2 px on hover.
- Everything above stops for a visitor who has asked their phone for less motion.

Left over and switched off: a scrolling text marquee and a floating molecule drawing from the first build. Neither is on any page. A scroll reveal script from the first build added a class that no style ever used, so it never moved anything; removed Nov 17.

What Hims moves, and what we take:

| On Hims | Take it | How, on Velacore |
|---|---|---|
| Product cards slide sideways | Yes, done | The program row |
| Product photo swaps as you hover a plan | Yes | On a program page, hovering a plan option swaps the photo to that form, vial or spray or dropper. Needs the per-form photos first. |
| Menu slides in from the side | Yes, done | The panel |
| Looping video in the hero | Maybe | One short silent clip, the vial turning on marble, 6 seconds, only on the home hero, only if it is under 1 MB. Not before the marble set is finished. |
| Numbers that count up | No | We have no numbers we are allowed to show. |
| Floating badges and labels drifting in | No | Decoration without a job. |
| Hover lift and shadow on every card | No | Rule 6 in the design checklist: one moment per page. |
| A sticky button that follows you | Yes, have it | The phone bar shows after the hero scrolls away. |

The rule for anything new that moves: it answers something the visitor did, it shows what changed, and it is gone in under half a second. One page, one moment.

## 5. The phone recording, Nov 17 2026

Dourado recorded hims.com on his Samsung S26 Ultra, 88 seconds, top to bottom. Read from 44 stills and two slow-motion strips. The recording stayed outside the repo and was deleted after this read.

What the phone view does:

- Every screen is one color block. The page is a stack of full-width blocks, each its own tone: deep brown, tan, blue, teal, navy, peach, cream, black. Inside most blocks sits one rounded card a shade lighter or darker than the block. The eye reads one card per thumb-length.
- Every block has one headline, one or two lines, and one or two pill buttons. Nothing else. Fine print sits under the block in a smaller tone with a Read more fold.
- The hero is a slow drift. The product scene on the dark gradient turns and drifts about a degree over several seconds, a loop, no cuts. The headline and button sit still on top of it. That is the only ambient motion on the page.
- The program row slides sideways, cards with a photo, a name, a from price and a small label. We have this.
- A question block with pill answers: a headline that asks, four pills under it, each a route. Our chooser does this with tiles; theirs is lighter.
- A number that counts. A weight figure ticks down on a tan block beside a scale photo. We have no number we are allowed to show, so no.
- A three-word stepper, Measure, Treat, Optimize, that highlights one word at a time as you scroll past. Cheap and clear. Ours would be Intake, Review, Delivery.
- A testimonial carousel with stars. Never, by COMPLIANCE.md.
- A doctor row with names, titles and credentials. Not ours; our clinicians are independent and unnamed on the site.
- An email capture block and an app download block. Not before the Agile decision on pre-intake email.
- Footer: an accordion of link groups, the LegitScript badge, a giant watermark wordmark. The accordion is worth taking for the phone footer; the badge waits for certification.

What to take, in order, each a piece Dourado sees before it goes live:

1. Color blocks on the phone. Turn the home page into a stack of full-width blocks, each on paper, mint, a goal tint or pine, with one rounded card inside. One headline, one line, one button per block. The sections already exist; this is spacing, color and cutting words.
2. The hero drift. One 6 to 8 second silent loop of the marble vial scene turning about a degree, under 1 MB, the headline and the goal rows still on top. Needs the marble hero shot first, then a Gemini or ffmpeg move on it. Still image for reduced motion.
3. The question block. "What are you here for?" with three pills instead of three tiles, on a goal-tint block, at the top and the foot of the page. The tiles stay inside the chooser.
4. The Intake, Review, Delivery stepper on How it works, one word lit as it passes the middle of the screen.
5. The phone footer as an accordion.

Not taken: the counting number, the testimonial carousel, the named doctors, the email capture, the FDA badges, the drug brand names, the coming soon banner.

## 6. Next steps, in order

1. Dourado picks one of the three edgier product sets, or none.
2. The prompts go into `docs/gemini-queue.md` as edits of the approved Tirzepatide photo, one vial at a time.
3. The first set goes on the home hero only. Everything else keeps the catalog look until he has seen it live.
