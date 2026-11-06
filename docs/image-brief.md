# Product image brief for Gemini

Written Nov 6 2026. One prompt per program, all in the same motif as the site so they sit together on the page. Dourado runs these in Gemini, saves the results, and the converter in `tools/prepare_images.py` does the rest.

## The motif, in one paragraph

White pharmacy label on clear glass, one colored cap per program, soft studio light, a pale mint backdrop. No people, no hands, no marble, no plants, no text other than the label. The label carries the jade helix mark small at the top, then reads exactly: VELACORE HEALTH on the first line, the program name on the second, and under it in small type: FOR PRESCRIPTION USE ONLY, PRESCRIPTION COMPOUNDED, 503A COMPOUNDING PHARMACY, Rx ONLY. Nothing else on the label. No "FDA approved", no benefit words, no stars, no badges.

Cap colors, the same ones the site uses for each program's stripe:
- Tirzepatide: royal blue, hex 3E5FC0
- Semaglutide: violet, hex 8A6BC9
- Microdosing GLP-1: jade green, hex 0C8F72
- NAD+: violet, hex 8A6BC9
- Sermorelin: violet, hex 8A6BC9

## How to run it

1. Open Gemini, choose image generation, square format, highest quality.
2. Upload two files with the prompt so Gemini sees the real brand: `brand\velacore-brand-card.png` and `public\logo-mark.png`. Add the line: "Use the uploaded logo mark on the label above the brand name. Match the colors on the uploaded brand card."
3. Paste the shared style block first, then the product line for the image you want.
3. Generate 3 or 4 variations. Pick the one where the label text is correct and readable. Gemini often misspells label text; if every variation is wrong, add "label text must read exactly:" and repeat the lines.
4. Save as PNG, as large as it offers, 2000 by 2000 or bigger.
5. Name the file exactly as listed and drop it in `assets-in\products\`. Then tell Vale "convert the product images". The converter resizes, trims, saves to `public\images\products\` and the site picks them up with no other change.

## Shared style block, paste first every time

Product photograph for a telehealth pharmacy brand. A single clear glass medical vial or bottle centered on a seamless pale mint background, hex EEF5F1, soft diffused studio light from the upper left, gentle shadow under the product, shallow depth of field, photoreal, 85mm lens look. Clean white paper label wrapped around the product. Square image, product fills about 70 percent of the height with even margin around it. No people, no hands, no props, no background objects, no extra text anywhere outside the label.

## Product lines, paste one after the style block

Tirzepatide, file `tirzepatide.png`
A 10 ml multi-dose injection vial with a royal blue flip-off cap, hex 3E5FC0, and silver crimp. Label text must read exactly: VELACORE HEALTH / TIRZEPATIDE / FOR PRESCRIPTION USE ONLY / PRESCRIPTION COMPOUNDED / 503A COMPOUNDING PHARMACY / Rx ONLY.

Semaglutide, file `semaglutide.png`
A 10 ml multi-dose injection vial with a violet flip-off cap, hex 8A6BC9, and silver crimp. Label text must read exactly: VELACORE HEALTH / SEMAGLUTIDE / FOR PRESCRIPTION USE ONLY / PRESCRIPTION COMPOUNDED / 503A COMPOUNDING PHARMACY / Rx ONLY.

Microdosing GLP-1, file `microdosing.png`
A small amber-tinted glass dropper bottle with a jade green cap, hex 0C8F72, standing beside a small 5 ml injection vial with the same jade cap, the two touching, bottle slightly in front. Label text on both must read exactly: VELACORE HEALTH / MICRODOSING GLP-1 / FOR PRESCRIPTION USE ONLY / PRESCRIPTION COMPOUNDED / 503A COMPOUNDING PHARMACY / Rx ONLY.

NAD+, file `nad.png`
A 5 ml injection vial with a violet flip-off cap, hex 8A6BC9, centered, with a slim white nasal spray bottle with a violet cap standing just behind it to the right, slightly out of focus. Label text on the vial must read exactly: VELACORE HEALTH / NAD+ / FOR PRESCRIPTION USE ONLY / PRESCRIPTION COMPOUNDED / 503A COMPOUNDING PHARMACY / Rx ONLY.

Sermorelin, file `sermorelin.png`
A 5 ml injection vial with a violet flip-off cap, hex 8A6BC9, and silver crimp. Label text must read exactly: VELACORE HEALTH / SERMORELIN / FOR PRESCRIPTION USE ONLY / PRESCRIPTION COMPOUNDED / 503A COMPOUNDING PHARMACY / Rx ONLY.

## Optional, for later

Oral semaglutide, file `semaglutide-oral.png`, only if that program is added to the site: a white HDPE pill bottle with a violet cap, same label lines with ORAL SEMAGLUTIDE on line two.

Hero lifestyle photo, file `hero.png`, 3 by 2 landscape, when Dourado wants one: a real-looking morning kitchen scene, a person in their forties opening a small white shipping box on a counter, the vial visible inside, natural window light, no faces in sharp focus, no before and after, no scale, no measuring tape, no gym. The site's hero frame takes it as is.

## What the converter does

`python -I tools/prepare_images.py` reads every PNG or JPG in `assets-in\products\`, trims transparent or flat borders, resizes to 1600 pixels on the long side, saves `public\images\products\<name>.webp`, and prints what changed. The old photos stay in `public\images\` untouched so nothing breaks if a new one is missing. Rerun the site build after: `python -I tools\build_programs.py`.
