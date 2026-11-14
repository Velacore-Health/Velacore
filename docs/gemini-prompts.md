# Gemini prompts for Velacore images, set 2

Written Nov 11 2026 at Dourado's direction: more people, everyday healthy routines, and vials in clean splashing water, so the site reads as health and wellness. Set 1 from Nov 6 is retired; it produced plain vials on mint.

Paste one block per generation into Gemini. Do not paste this whole file.

## How to run each one

1. Open gemini.google.com, switch on Images under the box, keep 3.1 Pro, and set Aspect ratio to the one the block names: 3:4 for tall, 4:3 or 16:9 for wide. Gemini offers 1:1, 9:16, 3:4, 4:3 and 16:9.
2. For the vial blocks, start a new chat for each vial and attach the label file named in the block first. The five labels are on the Desktop in `velacore-vials\labels` and in the repo under `brand/label/`. For the people blocks, attach nothing.
3. Paste the block. Ask for the largest size offered.
4. Check the result against the reject list at the bottom. If it fails, reply in the same chat with what to fix, for example "same image, but the label must match the attached artwork word for word".
5. Download the PNG, name it exactly as the block says, and drop it in the Velacore Health folder under `assets-in`, in `products` for vials and `lifestyle` for people.
6. Tell Vale "convert the images". The site picks them up from there.

## The look, the same in every image

Bright, clean, cool daylight. White and pale mint, with one touch of green. Real places, not studios, for people. Candid moments, nobody posing for the camera. Natural skin with texture, no glossy or airbrushed look. Colors true to life, slightly soft, like a good phone photo on an overcast morning. No text anywhere unless the block asks for it.

## Rules for people, never break these

- Adults about 35 to 60, varied backgrounds, ordinary everyday builds. Nobody model-thin, nobody with a fitness-model body.
- Everyday activity only: cooking, walking, coffee, reading, a laptop at a kitchen table. No gym, no workout gear, no sweat.
- Never show: scales, tape measures, mirrors, waistlines, bellies, loose clothing being held out, before and after, pills, needles, syringes, injections, medical gowns.
- Never a caption, name or quote that makes the person look like a Velacore patient. They are scenes, not testimonials.
- Faces are fine, but most looking away from the camera.

---

## 1. Hero, save as `hero.png`, folder `lifestyle`

Photoreal candid photograph, vertical 3 by 4. A woman in her late forties in a bright, real home kitchen on a weekday morning, standing at the counter pouring water from a glass carafe into a glass, a bowl of fresh green apples and a cutting board with sliced cucumber beside her. She wears a soft oatmeal knit sweater, hair loosely tied back, small relaxed smile, looking down at what she is doing, not at the camera. Cool natural daylight from a large window on the left, white cabinets, pale mint tile, a small green plant on the windowsill. Shallow depth of field, 50 mm lens look, natural skin texture, true-to-life colors. No text, no logos, no scale, no measuring tape, no pills, no needles.

The vial blocks were rewritten Nov 11 2026. Gemini now builds each vial from scratch and wears the exact label artwork in `brand/label/`, made by `brand/label/make_labels.py` from the designer's logo. Do not attach the old site vial images: their labels carry an off-spec line, and Gemini rewrote one label as research-use wording.

## 2. Tirzepatide vial in water, save as `tirzepatide.png`, folder `products`

Start a new Gemini chat. Attach `label-tirzepatide.png` from the Desktop folder `velacore-vials\labels`.

```
Photoreal product photograph, vertical 3 by 4. One clear glass 10 ml pharmaceutical vial with a deep matte pine green flip-off cap, color 15302A, and a silver aluminum crimp. Wrap the attached label artwork around the vial body as a printed white paper label, exactly as designed: the same dark green top panel with the white logo, the same thin colored line in the program color, the same words, fonts and spacing. Do not add, remove, translate or change any word on the label, and add no other text anywhere. The vial stands upright in the center, in a shallow layer of perfectly clear water on a white surface, with a crisp crown-shaped splash of clear water rising around its base and a few clean droplets frozen in the air beside it. The label faces the camera and stays dry, sharp and fully readable. It is physically wrapped on the curved glass: it spans the full width of the vial body edge to edge and continues around the back, the text and logo bend gently with the curve, the shading darkens softly toward both side edges, and a thin vertical highlight from the window light runs down the glass over the label. The camera sits slightly above the vial, looking down about 10 degrees, so the top and bottom edges of the label curve downward like a gentle smile, every line of text follows that same curve, and the letters near both side edges narrow as they turn away around the glass. Background a soft pale mint, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, high-speed photography, crystal clear water, a gentle reflection on the wet surface. No other objects, no syringe, no needle, no bubbles inside the vial, no color in the water.
```

## 3. Semaglutide vial in water, save as `semaglutide.png`, folder `products`

Start a new Gemini chat. Attach `label-semaglutide.png` from the Desktop folder `velacore-vials\labels`.

```
Photoreal product photograph, vertical 3 by 4. One clear glass 10 ml pharmaceutical vial with a deep matte pine green flip-off cap, color 15302A, and a silver aluminum crimp. Wrap the attached label artwork around the vial body as a printed white paper label, exactly as designed: the same dark green top panel with the white logo, the same thin colored line in the program color, the same words, fonts and spacing. Do not add, remove, translate or change any word on the label, and add no other text anywhere. The vial stands upright in the center, in a shallow layer of perfectly clear water on a white surface, with a crisp crown-shaped splash of clear water rising around its base and a few clean droplets frozen in the air beside it. The label faces the camera and stays dry, sharp and fully readable. It is physically wrapped on the curved glass: it spans the full width of the vial body edge to edge and continues around the back, the text and logo bend gently with the curve, the shading darkens softly toward both side edges, and a thin vertical highlight from the window light runs down the glass over the label. The camera sits slightly above the vial, looking down about 10 degrees, so the top and bottom edges of the label curve downward like a gentle smile, every line of text follows that same curve, and the letters near both side edges narrow as they turn away around the glass. Background a soft pale mint, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, high-speed photography, crystal clear water, a gentle reflection on the wet surface. No other objects, no syringe, no needle, no bubbles inside the vial, no color in the water.
```

## 4. NAD+ vial in water, save as `nad.png`, folder `products`

Start a new Gemini chat. Attach `label-nad.png` from the Desktop folder `velacore-vials\labels`.

```
Photoreal product photograph, vertical 3 by 4. One clear glass 10 ml pharmaceutical vial with a deep matte pine green flip-off cap, color 15302A, and a silver aluminum crimp. Wrap the attached label artwork around the vial body as a printed white paper label, exactly as designed: the same dark green top panel with the white logo, the same thin colored line in the program color, the same words, fonts and spacing. Do not add, remove, translate or change any word on the label, and add no other text anywhere. The vial stands upright in the center, in a shallow layer of perfectly clear water on a white surface, with a crisp crown-shaped splash of clear water rising around its base and a few clean droplets frozen in the air beside it. The label faces the camera and stays dry, sharp and fully readable. It is physically wrapped on the curved glass: it spans the full width of the vial body edge to edge and continues around the back, the text and logo bend gently with the curve, the shading darkens softly toward both side edges, and a thin vertical highlight from the window light runs down the glass over the label. The camera sits slightly above the vial, looking down about 10 degrees, so the top and bottom edges of the label curve downward like a gentle smile, every line of text follows that same curve, and the letters near both side edges narrow as they turn away around the glass. Background a soft pale mint, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, high-speed photography, crystal clear water, a gentle reflection on the wet surface. No other objects, no syringe, no needle, no bubbles inside the vial, no color in the water.
```

## 5. Sermorelin vial in water, save as `sermorelin.png`, folder `products`

Start a new Gemini chat. Attach `label-sermorelin.png` from the Desktop folder `velacore-vials\labels`.

```
Photoreal product photograph, vertical 3 by 4. One clear glass 10 ml pharmaceutical vial with a deep matte pine green flip-off cap, color 15302A, and a silver aluminum crimp. Wrap the attached label artwork around the vial body as a printed white paper label, exactly as designed: the same dark green top panel with the white logo, the same thin colored line in the program color, the same words, fonts and spacing. Do not add, remove, translate or change any word on the label, and add no other text anywhere. The vial stands upright in the center, in a shallow layer of perfectly clear water on a white surface, with a crisp crown-shaped splash of clear water rising around its base and a few clean droplets frozen in the air beside it. The label faces the camera and stays dry, sharp and fully readable. It is physically wrapped on the curved glass: it spans the full width of the vial body edge to edge and continues around the back, the text and logo bend gently with the curve, the shading darkens softly toward both side edges, and a thin vertical highlight from the window light runs down the glass over the label. The camera sits slightly above the vial, looking down about 10 degrees, so the top and bottom edges of the label curve downward like a gentle smile, every line of text follows that same curve, and the letters near both side edges narrow as they turn away around the glass. Background a soft pale mint, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, high-speed photography, crystal clear water, a gentle reflection on the wet surface. No other objects, no syringe, no needle, no bubbles inside the vial, no color in the water.
```

## 6. Microdosing GLP-1 vial in water, save as `microdosing.png`, folder `products`

Start a new Gemini chat. Attach `label-microdosing.png` from the Desktop folder `velacore-vials\labels`.

```
Photoreal product photograph, vertical 3 by 4. One clear glass 10 ml pharmaceutical vial with a deep matte pine green flip-off cap, color 15302A, and a silver aluminum crimp. Wrap the attached label artwork around the vial body as a printed white paper label, exactly as designed: the same dark green top panel with the white logo, the same thin colored line in the program color, the same words, fonts and spacing. Do not add, remove, translate or change any word on the label, and add no other text anywhere. The vial stands upright in the center, in a shallow layer of perfectly clear water on a white surface, with a crisp crown-shaped splash of clear water rising around its base and a few clean droplets frozen in the air beside it. The label faces the camera and stays dry, sharp and fully readable. It is physically wrapped on the curved glass: it spans the full width of the vial body edge to edge and continues around the back, the text and logo bend gently with the curve, the shading darkens softly toward both side edges, and a thin vertical highlight from the window light runs down the glass over the label. The camera sits slightly above the vial, looking down about 10 degrees, so the top and bottom edges of the label curve downward like a gentle smile, every line of text follows that same curve, and the letters near both side edges narrow as they turn away around the glass. Background a soft pale mint, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, high-speed photography, crystal clear water, a gentle reflection on the wet surface. No other objects, no syringe, no needle, no bubbles inside the vial, no color in the water.
```

## 7. Online visit, save as `step-visit.png`, folder `lifestyle`

Photoreal candid photograph, horizontal 4 by 3. A man in his early fifties at a wooden kitchen table in the morning, typing on a laptop, a mug of coffee and a phone beside it, reading glasses on, calm and focused. Seen from a three-quarter angle behind his shoulder so the laptop screen is turned away and unreadable. Cool window light, white walls, a pale mint dish towel on a chair, a green plant. Natural skin texture, true-to-life colors, 35 mm lens look. No text, no logos, no pills, no medical items.

## 8. Clinician review, save as `step-clinician.png`, folder `lifestyle`

Replaced Nov 11 2026: the first version, a woman on a sofa on a call, did not read as a clinician. The face stays out of frame on purpose: an AI face shown as one of "your clinicians" would be a fake doctor.

```
Photoreal candid photograph, horizontal 4 by 3. A licensed clinician reviewing a patient intake at a clean, bright home-office desk. Framed from the shoulders down so the face is out of frame: deep pine green medical scrubs, a stethoscope around the neck, one hand on a laptop trackpad and the other holding a pen over a notepad, as if carefully reading. The laptop is angled away so its screen cannot be read. On the desk: a mug of tea, a small green plant, a closed folder. Cool natural window light, white walls and soft mint tones, shallow depth of field, true-to-life colors, natural skin texture on the hands, 35 mm lens look. No face, no name badge, no ID card, no logos, no words, letters or numbers anywhere, no pills, no needles, no syringes.
```

## 9. Delivery, save as `step-delivery.png`, folder `lifestyle`

Final version Nov 11 2026. Earlier tries read as a stock photo, then a gift, then carried an AI-drawn Velacore mark that vc-reviewer blocked: the real shipment comes from the pharmacy, so the box stays plain. The dog ties this step to the walk photo.

```
Photoreal candid photograph, horizontal 4 by 3, like a real moment someone snapped on their phone, not a stock or studio image. A plain white corrugated mailer box, about 12 by 9 by 4 inches, sealed with one strip of ordinary brown kraft packing tape, sits on a light gray stone front step just outside an open front door painted soft sage green. A blue merle Australian shepherd, gray, black and white speckled coat with copper markings on the face, has just stepped out of the doorway and is curiously sniffing the corner of the box, ears up, tail a blur. Seen from slightly above and to the side, natural and a little off-center, with part of the doorframe and a small white planter with green leaves at the edge of the frame. Bright cool morning daylight, soft shadows, true-to-life colors, white, light gray and soft mint tones. No shipping label visible, no words, letters, numbers, logos or brand marks anywhere, no people, no hands.
```

## 10. Walk outdoors, save as `wellness.png`, folder `lifestyle`

Photoreal candid photograph, horizontal 16 by 9. Two friends in their late thirties to early forties, a man and a woman, no gray hair, natural ordinary builds, walking side by side on a tree-lined park path in soft early morning light, mid-conversation and laughing, in current casual everyday wear: she in straight-leg jeans, white sneakers and a light oversized knit sweater, he in dark chinos, clean white sneakers and an unbuttoned light overshirt over a plain tee. One blue merle Australian shepherd, gray, black and white speckled coat with copper markings, trots beside them on a loose plain leash held by the woman. Seen from a little distance, slightly from the side, green trees and a hint of mist behind them. Natural skin texture, true-to-life colors, 85 mm lens look, gentle background blur. Bright, airy, clean wellness brand look: cool natural daylight, fresh greens, pale and soft tones, no warm golden-hour or orange light. Not a workout, no athletic wear, no fitness trackers in focus, no text, no logos, no signs.

## 11. Hero group shot, save as `hero-group.png`, folder `lifestyle`

Written Nov 13 2026. The first try put one vial behind the others and left the splash with no vial in it. This version uses the five finished vial photos as references, so the labels are already right, and asks for one straight row.

Start a new Gemini chat. Set Aspect ratio to 4:3. Attach all five photos from the Desktop folder `velacore-vials\group-refs`.

```
Photoreal product photograph, horizontal 4 by 3. Use the five attached photos as exact references for the five vials: same glass, same deep matte pine green caps with silver crimps, and the same printed labels, word for word, with the same colors. Do not change, add or remove any word on any label, and add no other text anywhere. Stand all five vials upright in one straight row across the middle of the frame, side by side, evenly spaced with a small gap between each, all on the same line, all the same size, none in front of or behind another, none touching. From left to right: Microdosing GLP-1, Semaglutide, Tirzepatide in the center, NAD+, Sermorelin. Every label faces the camera, fully visible, sharp, dry and readable, physically wrapped on the curved glass. All five vials stand in one shallow layer of perfectly clear water on a white surface, and each vial has its own small crown-shaped splash of clear water rising around its base, with a few clean droplets in the air. The splashes stay low, below the labels, and never cover them. Camera straight on at label height, looking down about 10 degrees. Background a soft pale mint, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, high-speed photography, crystal clear water, gentle reflections on the wet surface. Leave clean space above and to both sides of the row. No other objects, no syringe, no needle, no color in the water.
```

If one vial drifts behind the others, reply in the same chat: "same image, but all five vials in one straight row, none behind another, every label fully visible."

Floating version, Dourado's idea Nov 13 2026, because a splash under five vials read oddly. Use it in the same chat as the five photos:

```
New version, same five vials from the attached photos, same labels word for word, same pine green caps. Horizontal 4 by 3. No water on the ground and no splash. The five vials float in the air in front of a soft pale mint background, color EEF5F1, fading to white at the top, as if gently suspended mid-fall. They form one loose row across the frame from left to right: Microdosing GLP-1, Semaglutide, Tirzepatide in the center, NAD+, Sermorelin. Each vial sits at a slightly different height, a gentle wave, and each is tilted a little, no more than 10 degrees, every one at a different small angle. All five are the same size, none in front of or behind another, none overlapping or touching, with clear space between them. Every label faces the camera, fully visible, sharp and readable. A few small clear water droplets float near the vials, never on the labels. A soft, faint shadow on a white surface below them. Bright cool daylight from the upper left, crisp studio product photography, high detail on the glass. No other objects, no text other than the labels, no syringe, no needle.
```

The floating try, Nov 13, was rejected: Dourado found it flat, and the fifth label read a misspelled word instead of Sermorelin. Next, his marble idea:

```
New version, same five vials from the attached photos, same labels word for word, same pine green caps. Check every label against the attached photos, especially the right-hand vial, which must read Sermorelin. Horizontal 4 by 3. The vials stand upright, never tilted, on a pale white marble tabletop with soft gray veining. On the marble sit simple solid risers of the same white marble, plain rectangular blocks with crisp edges, at three heights, so the vials are staggered: the center vial on the tallest riser, the two vials beside it on medium risers, the two outer vials on the marble tabletop itself. From left to right: Microdosing GLP-1, Semaglutide, Tirzepatide in the center, NAD+, Sermorelin. All five in one row across the frame, side by side, evenly spaced, none in front of or behind another, none touching. Every label faces the camera, fully visible, sharp and readable. Background a soft pale mint wall, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, soft natural shadows on the marble, crisp studio product photography, high detail on the glass. No water, no plants, no other objects, no text other than the labels, no syringe, no needle.
```

---

## 12. Glutathione vial in water, save as `glutathione.png`, folder `products`

Added Nov 13 2026 when Dourado put glutathione back. To match the five other splash vials, this edits the finished NAD+ photo and swaps only the label. The form is not confirmed: the vial is a placeholder look, like the others, and the illustrative-image line covers it. Redo it if the Agile proposal names a tablet.

Start a new Gemini chat, Aspect ratio 3:4. Attach two files, in this order: `nad.jpg` from the Desktop folder `velacore-vials\group-refs`, then `label-glutathione.png` from `velacore-vials\labels`.

```
Edit the first attached photo. Keep everything exactly the same: the vial, the pine green cap, the water splash, the droplets, the light, the background and the framing. Change only the printed label on the vial: replace it with the second attached label artwork, exactly as designed, the same dark green top panel with the white logo, the same thin violet line, and the word Glutathione with the three small lines and Rx ONLY. Do not add, remove or change any word on the label, and add no other text anywhere. The label stays wrapped on the curved glass, dry, sharp and fully readable.
```

---

## Reject the image if any of these show

- Any word on a vial label misspelled, warped, doubled or changed from the attached label artwork.
- Any label wording about research, serum, topical use, or not for human use. Velacore vials are prescription medicine for patients; research-use wording is the gray-market signal LegitScript and the ad platforms reject.
- A cap that is not deep pine green, or a syringe or needle anywhere in the frame.
- Extra or missing fingers, melted hands, faces that look plastic or airbrushed, teeth that blur together.
- Water that is colored, foamy, or covering the label.
- Anything on the people rules list above.
- Any text, watermark of another brand, or logo that was not asked for.
- The image looks like a stock ad: everyone grinning at the camera, perfect symmetry, glossy skin.

## Notes

- Gemini adds an invisible SynthID watermark to every image. Never try to strip it. On the site the images are scenes, not patient photos, so no label is needed; any Meta ad that uses them must carry Meta's AI label.
- Keep each finished PNG in the business Drive under 01-brand as well, so the originals are safe.
