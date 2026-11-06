# Velacore Health brand bible

Started Nov 6 2026. This is the one place for approved logos, colors, type, voice and image rules. Anything made for Velacore, on the site, in an ad, in a Gemini prompt, on a label or in a deck, follows this file. When something here changes, change it here first.

## 1. The mark

A double helix with two leaves, set inside a thin ring. It says biology plus growth. Two versions exist:

- Full logo: the helix in a violet-to-blue gradient, the ring in the same gradient, VELACORE below in a heavy geometric sans, HEALTH under that in wide-spaced capitals between two short rules. File: `public/logo-full.png`, 317 by 231 pixels.
- Mark only: the helix and ring in jade on a transparent background. File: `public/logo-mark.png`, 119 by 128 pixels. This is the header and favicon mark on the site.

Rules:
- Never redraw, recolor or stretch the mark. Never add a drop shadow or an outline.
- On white or mint, use either version. On pine or any dark ground, use the jade mark with white wordmark text, never the gradient logo.
- Clear space around the logo is at least the height of the letter V in VELACORE.
- Minimum size on screen: 28 pixels tall for the mark, 110 pixels wide for the full logo.
- The label on product vials uses the mark above the wordmark, both in pine, no gradient. See section 6.

Missing: the original logo source. We have no vector file and no version larger than 317 pixels. Dourado to find the designer's file, SVG, AI, EPS or a PNG at 2000 pixels or more, and put it in `brand/logo/`. Until then, print and large-format uses are on hold.

## 2. Colors

Site palette, the approved values:

| Name | Hex | Use |
|---|---|---|
| Paper | #FFFFFF | Page background |
| Mint | #EEF5F1 | Alternating sections, image backdrops |
| Mint deep | #DDF0E7 | Soft tint blocks |
| Pine | #15302A | All text, the one dark band, the footer |
| Pine soft | #4C625B | Secondary text |
| Jade | #0C8F72 | Buttons, links, the mark on light grounds |
| Jade tint | #C9EEDF | Highlights, icon backgrounds |
| Line | #D5E0DB | Borders and rules |

Program colors, taken from the vial caps and the logo gradient. Each program owns one, used as its card stripe, its page stripe and its cap in product images:

| Program | Color | Hex |
|---|---|---|
| Tirzepatide | Helix blue | #3E5FC0 |
| Semaglutide | Helix violet | #8A6BC9 |
| Microdosing GLP-1 | Jade | #0C8F72 |
| NAD+ | Helix violet | #8A6BC9 |
| Sermorelin | Helix violet | #8A6BC9 |

Logo gradient: helix violet #8A6BC9 at the lower left to helix blue #3E5FC0 at the upper right. These are the site's values; the exact gradient stops will be read from the source file when it arrives.

Rules: pine is the only text color on light grounds. Jade is for things you can click or the mark. The program colors are stripes and caps, never text and never backgrounds. No gradients anywhere except inside the logo itself. No black, no pure grey.

## 3. Type

- Headlines: Fraunces, weight 500, optical size high, the SOFT axis around 30 to 50. Sentence case. No single word colored or italic inside a headline.
- Body, buttons, labels, navigation: Hanken Grotesk, 400 to 600.
- Logo wordmark: the logo's own lettering. It is not a web font we have. Do not try to set VELACORE in Fraunces or Hanken; use the logo file.
- Sizes on the site: body 17 px, line length under 80 characters, headlines from 2.6 rem to 4.4 rem.
- Nothing in all caps except the logo wordmark and the product label. No tracked-out small-caps labels.

Both web fonts load from Google Fonts. Desktop files for Canva or print: download Fraunces and Hanken Grotesk from Google Fonts, both are free under the Open Font License.

## 4. Voice

Plain, calm, specific. Velacore coordinates; the licensed clinician decides; the 503A pharmacy fills, always in that order. No outcome promises, no weight numbers, no brand-name drug comparisons, no coaching language, no "FDA approved" near a compounded medication. Sentence case. No em dashes, no parentheses, no emojis, no exclamation marks. Full rules live in `COMPLIANCE.md` and in the `vc-copy` agent.

## 5. Images

The motif: the product itself, on mint, in soft studio light, nothing else. White label, one colored cap per program, clear glass. No people in product shots, no props, no marble, no plants, no sparkles, no glow.

Lifestyle photos, when used: natural light, real rooms, people in their forties and fifties, nobody posed at a gym, no before and after, no scales, no tape measures, faces soft or turned. One such photo per page at most.

Illustrations: thin pine or jade line icons on mint, as on the education cards. No 3D renders, no clip art, no stock-looking isometric scenes.

Files: product images are `public/images/products/<program>.webp`, one fixed name each. Drop Gemini output in `assets-in/products/` and run `tools/prepare_images.py`. Prompts are in `docs/image-brief.md`.

## 6. The product label

Every vial, bottle and spray carries the same label, so the shelf reads as one brand:

Line 1: the jade helix mark, small, centered
Line 2: VELACORE HEALTH, pine, wide spaced capitals
Line 3: the program name, pine, bold capitals
Line 4 to 7, small: FOR PRESCRIPTION USE ONLY / PRESCRIPTION COMPOUNDED / 503A COMPOUNDING PHARMACY / Rx ONLY

Nothing else. No seals, no stars, no "FDA", no benefit words, no dosage claims on the mock label.

Cap color by program per section 2. Silver crimp on vials. Amber glass for the microdosing dropper, white HDPE for any pill bottle, white for nasal sprays.

## 7. Files and where they live

- `public/logo-full.png`, `public/logo-mark.png`: the only approved logo files today.
- `brand/velacore-brand-card.html` and `brand/velacore-brand-card.png`: a one-page card with the logo, the palette and the type, to upload alongside any Gemini or Canva prompt so the tool sees the brand.
- `docs/image-brief.md`: product image prompts.
- `docs/BRAND.md`: this file.

## 8. Open items

1. Find the original logo source file and save it in `brand/logo/`. Dourado.
2. Confirm the gradient stops and the wordmark typeface from that file, then update section 2 and 3. Vale.
3. Decide whether the vial label keeps the helix mark or the mark goes only on the cap seal. Dourado, once the first Gemini labels come back.
