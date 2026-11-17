# Image and video queue, Nov 16 2026

The running list of what still has to be made or changed, in the order we will do it. Dourado runs Gemini; Vale picks up each download from the Downloads folder, checks it and files it. One item at a time. Tick an item off here when it passes.

Gemini video and image credits reset at 9:21 PM on Nov 16. Video gave two clips per window last time, so the two clips go first.

## Where it stands at the end of Nov 16

Every Gemini item below was made and passed Vale's check on Nov 16. The prompts stay here as the record of what worked.

- Item 1, opening clip: done, first run. In the video as `clips/clip1.mp4`.
- Item 2, clip 5: done, first run.
- Item 3, clinician photo: done. On the local site in step 2, mirrored at Dourado's request so she faces the patient photo. Two points for vc-reviewer: her face shows in profile, and blurred medicine bottles sit in the cabinet behind her.
- Item 4, clinician in motion: done, first run. In the video as `clips/clip6.mp4`.
- Item 4b, six-vial group shot: done on the third image. The edit prompt below failed, it kept five vials and misspelled the small print. What worked was a fresh image from six separate vial photos; that prompt is in the Nov 16 chat and should be copied into `docs/gemini-prompts.md`. Gemini then fixed one misspelled HEALTH and Vale patched the other by copying the word from the Tirzepatide vial. Tell vc-reviewer about the patch. On the local home page hero and in the video closing scene.
- Item 5, wide Sermorelin: done, cropped tighter by Vale so the vial matches the other tiles. On the local home page as the Hormone support tile.
- Item 6, NAD+ vial on marble: done. Filed as `assets-in/products/nad-marble.jpg`, not on the site yet.

Nothing from this session is live. Nothing is pushed. vc-reviewer has seen none of it.

## The Nov 17 push set, in this order

All four made, checked and vc-reviewer PASS on Nov 17: A, B, C and D. Step 4 needed a second try.

Dourado, Nov 17: get all the images done before the next push. Glutathione was redone and passed review the same morning. Four left. Save each download in Downloads as Gemini names it; Vale finds it, checks every label line enlarged, files it and places it. Each one goes through vc-reviewer before the push.

### A. Microdosing GLP-1 oral dropper, replaces the placeholder in the Tired of needles section

New chat, Images on, Aspect ratio 3:4. Attach, in this order: `nad-oral-marble.jpg`, then `microdosing-marble.jpg`, both from `assets-in\products`.

```
Edit the first attached photo. Keep the scene exactly the same: the same white marble riser, the same pale marble tabletop, the same soft mint wall fading to white, the same daylight from the upper left, the same soft shadow, the same camera height and the same vertical 3 by 4 framing. Keep the bottle the same shape and size, with the same ribbed deep pine green cap and the same white dropper bulb.

Change only three things. One: make the bottle glass clear warm amber brown pharmacy glass. Two: change the product name on the label from NAD+ to Microdosing GLP-1, set on two centered lines, Microdosing on the first line and GLP-1 on the second, in the same serif font, weight and color as NAD+, spelled exactly as on the label in the second attached photo. Three: change the violet line under the dark green band and the short violet dash under the name to jade green, color 0C8F72, exactly as on the label in the second attached photo.

Keep every other word on the label exactly as it is, word for word: the VELACORE HEALTH logo, FOR PRESCRIPTION USE ONLY, PRESCRIPTION COMPOUNDED, 503A COMPOUNDING PHARMACY, and Rx ONLY in its outlined pill. Add no other text anywhere. Exactly one bottle. No other objects, no hands, no pills, no syringe, no needle.
```

Reject if any label word is misspelled, if 503A has a malformed 5, or if the glass is not amber.

### B. NAD+ vial, redone to match the set

Why: the NAD+ vial on the site is the earlier marble photo, cropped; its riser and vial shape differ from Tirzepatide, Semaglutide, Microdosing and Glutathione.

New chat, Images on, Aspect ratio 3:4. Attach, in this order: `tirzepatide-marble.jpg`, then `semaglutide-marble.jpg`, both from `assets-in\products`.

```
Edit the first attached photo. Keep everything exactly the same: the same vial, the same deep pine green cap and silver crimp, the same marble riser, tabletop, mint wall, light, shadow, camera height and framing, and every word of the label in the same place and font.

Change only two things. One: change the product name on the label from Tirzepatide to NAD+, in the same serif font, size, weight and color, centered. Two: change the blue line under the dark green band and the short blue dash under the name to violet, exactly the violet used on the label in the second attached photo.

Keep every other word exactly as it is: the VELACORE HEALTH logo, FOR PRESCRIPTION USE ONLY, PRESCRIPTION COMPOUNDED, 503A COMPOUNDING PHARMACY, and Rx ONLY in its outlined pill. Add no other text anywhere. Exactly one vial, no other objects.
```

### C. Sermorelin vial, redone to match the set

Same as B, same two attachments, same prompt with Sermorelin in place of NAD+.

### D. Step 4 support photo for How it works

Try 1 rejected Nov 17: a third arm and hand, a cluttered room, pictures on the floor. Dourado wants a happy medium between the Hims framing and our brand, people in their late twenties to late thirties, somewhat attractive. Try 2, new chat, Images on, 4:3, nothing attached:

```
Photoreal candid photograph, horizontal 4 by 3, editorial lifestyle style, like a real quiet moment at home, not a stock photo. A naturally good-looking man about 32, well groomed, short dark hair, light stubble, an approachable everyday face, ordinary healthy build, not a model, wearing a plain deep pine green crewneck sweater. He sits on a light linen sofa in a calm, bright, minimal living room. He holds his phone in both hands in front of his chest, typing a short message with his thumbs, a small easy smile, looking down at the phone. Exactly two arms and two hands, both on the phone, natural fingers, nothing resting on the sofa back.

Frame him from the knees up, slightly off center to the right, filling about half the frame. Behind him a smooth plain white wall with soft pale mint daylight on it, one tall green plant softly out of focus on the left, and one pale mint cushion beside him. Lots of clean empty wall space. Nothing on the floor, no shelves, no clutter, no pictures or frames on the walls, no books, no papers, no table.

Soft cool morning daylight from a large window on the left, gentle shadows, true skin tones with natural texture, no retouched or glamour look, shallow depth of field, calm and uncluttered. The phone screen faces away from the camera and shows nothing readable. No logos, no text anywhere, no watch, no coffee mug, no medical items, no pills, no needles, no scale.
```

Reject if: any extra or missing arm, hand or finger, any readable text, clutter, a model or fitness look, or a face that reads as a known person.

### E. Semaglutide oral, asked by Dourado Nov 17

The written proposal prices Semaglutide oral and gives 5 or 10 mg a day, but not the form. Drawn as an amber dropper to match the Microdosing GLP-1 oral photo until OpenLoop names the form; the question is in `docs/openloop-email-draft.md`. If they say tablet, it is redone as a white bottle per BRAND.md section 6. Not placed on the site until Dourado adds Semaglutide oral as an offering.

New chat, Images on, Aspect ratio 3:4. Attach, in this order: `microdosing-oral.jpg`, then `semaglutide-marble.jpg`, both from `assets-in\products`.

```
Edit the first attached photo. Keep everything exactly the same: the same amber glass dropper bottle, the same ribbed deep pine green cap and white dropper bulb, the same marble riser, tabletop, mint wall, light, shadow, camera height and framing, and every word of the label in the same place and font.

Change only two things. One: change the product name on the label from Microdosing GLP-1 to Semaglutide, in the same serif font, weight and color, centered on one line. Two: change the jade green line under the dark green band and the short jade dash under the name to violet, exactly the violet used on the label in the second attached photo.

Keep every other word exactly as it is: the VELACORE HEALTH logo, FOR PRESCRIPTION USE ONLY, PRESCRIPTION COMPOUNDED, 503A COMPOUNDING PHARMACY, and Rx ONLY in its outlined pill. Add no other text anywhere. Exactly one bottle, no other objects.
```

Save the download; Vale files it as `semaglutide-oral.jpg`.

## Gemini, in this order

### 1. Opening clip, replaces clip 1

Why: the opening shows beads floating and does not match "if peptides sound complicated". The new clip goes from a tangle to four calm beads.

New chat, video.

```
One continuous shot, no cuts. At the start, a dense, tangled cluster of many long chains of small translucent glass spheres fills the center of the frame, knotted and overlapping like a loose ball of beaded string, turning very slowly. For the first three seconds it stays tangled and complex. Then, slowly and gracefully, the tangle loosens and the chains drift apart and fade softly out of focus toward the edges of the frame. By six seconds only four larger translucent glass spheres remain, floating calmly in one evenly spaced horizontal row across the center of the frame, each a slightly different soft color: mint, jade green, pale aqua, soft green. For the last three seconds the four spheres hold still in their row, glowing very gently, in sharp focus. All spheres stay soft mint, jade green or pale aqua, with no warm, orange, pink or yellow glow. Background: a clean bright pale mint and white room, softly out of focus, with faint diffused window light. Style: photoreal scientific 3D visualization, macro scale, soft diffused daylight, shallow depth of field, very slow gentle camera drift, calm, serene and reassuring, smooth and unhurried motion. No text, no letters, no labels, no numbers, no people, no hands, no syringes, no needles, no pills, no logos. 16 by 9 landscape, 8 seconds.
```

### 2. Clip 5, the Messenger clip

Why: the Messenger section of the video is still blank.

New chat, video.

```
One continuous shot, no cuts. Close macro view of the surface of a cell, shown as a smooth, softly glowing, frosted glass-like pale mint curved surface filling the lower third of the frame. One small smooth cup-shaped receptor made of the same frosted pale mint glass rises from the center of the surface, open at the top. A short chain of exactly four translucent glass spheres, joined end to end by short thin clear glass links like beads on a string, drifts slowly down from the top of the frame during the first four seconds. It settles gently and snugly into the cup of the receptor and stays there. Then one soft, slow ripple of cool pale aqua and white light spreads calmly outward across the cell surface from the receptor, and the scene holds still for the last two seconds. The chain stays one unbroken line of four spheres the whole time: no spheres detach, no spheres merge, no extra chains, no extra receptors. All spheres stay soft mint, jade green or pale aqua. All light stays cool white and aqua, with no warm, orange, pink, red or yellow glow, no sparks, no flashes, no bursts. Background: a clean bright pale mint and white space, softly out of focus. Style: photoreal scientific 3D visualization, macro scale, soft diffused daylight, shallow depth of field, very slow gentle camera drift, calm, serene and reassuring, smooth and unhurried motion. Nothing fleshy, veiny or organic looking. No text, no letters, no labels, no numbers, no people, no hands, no syringes, no needles, no pills, no logos. 16 by 9 landscape, 8 seconds.
```

### 3. Clinician photo, replaces `step-clinician`

Why: Dourado, Nov 16: the current photo reads as a man at home with a laptop and a coffee. It needs to read as a clinician's office, official but still warm. It is used on the site in the steps section and in the video under the closing line.

New chat, Images on, Aspect ratio 4:3, attach nothing.

```
Photoreal photograph, horizontal 4 by 3. A licensed clinician at work in a bright, modern medical office. The clinician is an adult in their forties wearing a clean white coat over deep pine green scrubs, with a stethoscope around the neck. They sit at a tidy white desk, seen from the side and slightly behind, looking down at a patient chart in a plain manila folder that lies open on the desk, one hand resting on the page and a pen in the other. The face is turned away from the camera and mostly out of frame, shown only from the jaw down. On the desk: a closed slim laptop, the folder, and nothing else. Behind the desk, softly out of focus, the room is clearly a clinic: a white wall with two framed certificates whose text is too blurred to read, a wall-mounted blood pressure cuff, a glass-front cabinet with neatly arranged plain medical supplies, and one small green plant. Large window with cool, soft morning daylight from the left. Colors: white and pale mint with one touch of pine green. Calm, professional, clean and welcoming. Natural skin with real texture, no glossy or airbrushed look, candid, nobody posing.

No coffee mug, no curtains, no sofa, no kitchen, no home furniture, no patient, no second person, no computer screen showing text, no readable text or logos anywhere, no name badge, no pills, no syringes, no needles, no scale, no tape measure.
```

Reject it if any hand has extra or missing fingers, if any readable text appears, or if the room still looks like a home.

### 4. Clinician in motion, for the closing line of the video

Why: Dourado, Nov 16: the closing line needs a moving picture that shows a clinician reviewing a health history, not a still photo. This animates the photo from item 3, so the site and the video show the same clinic. It uses a video credit; three clips came through in the last window, so it may have to wait for the next reset.

New chat, video. Attach the finished clinician photo from item 3.

```
Animate the attached photo into one continuous shot, no cuts. Keep everything exactly as it is in the photo: the same clinician in a white coat over pine green scrubs, the same desk, the same open patient chart, the same bright clinic room and the same soft morning daylight. The clinician calmly reads the chart, slowly turns one page, then writes a short note on the page with the pen. The movements are small, slow and natural. The camera pushes in very slowly toward the chart and the hands. The face stays turned away and out of frame the whole time. Both hands stay natural, with five fingers each, and never blur, melt or change shape. Nothing else in the room moves. Calm, professional and reassuring. No readable text anywhere, no letters appearing on the page, no patient, no second person, no pills, no syringes, no needles, no logos. 16 by 9 landscape, 8 seconds.
```

Save as `clip6.mp4`. Reject it if a hand distorts, if any readable text appears, or if the face turns to the camera.

### 4b. Six-vial group shot, replaces `hero-group`

Why: the group photo on the home page has five vials and is missing Glutathione. The new one is also the picture for the video's closing scene.

New chat, Images on, Aspect ratio 4:3. Attach, in this order: `hero-group.jpg` from `assets-in\lifestyle`, then `glutathione.jpg` from `assets-in\products`.

```
Edit the first attached photo. Keep the five vials exactly as they are: the same glass, the same deep matte pine green caps with silver crimps, and the same printed labels, word for word, with the same logo and the same colored lines. Do not change, add or remove any word on any label, and add no other text anywhere. Keep the same pale white marble tabletop with soft gray veining, the same white marble risers, the same soft pale mint wall fading to white, the same bright cool daylight from the upper left and the same horizontal 4 by 3 framing.

Add one more vial, so there are exactly six. The new vial is the Glutathione vial from the second attached photo: same glass, same pine green cap and silver crimp, and the same printed label, word for word, with the word Glutathione, the three small lines and Rx ONLY. Take only the vial from the second photo. Do not bring any water, splash or droplets into the scene.

Arrange the six vials in one row across the frame, side by side, evenly spaced, none in front of or behind another, none touching. From left to right: Microdosing GLP-1, Semaglutide, Tirzepatide, NAD+, Glutathione, Sermorelin. The two outer vials stand on the marble tabletop. The two vials next to them stand on low marble risers. The two center vials stand on taller marble risers of equal height. Make all six vials the same size, slightly smaller than in the first photo so the row fits with clean space on both sides. Every label faces the camera, fully visible, sharp, dry and readable.

No water, no plants, no other objects, no syringe, no needle.
```

### 5. Wide Sermorelin for the Hormone support tile

Why: the home page Hormone support tile still borrows the water photo.

Go back to the Sermorelin marble chat from Nov 16 and press retry under the last message. If that chat is gone: new chat, Aspect ratio 4:3, attach `sermorelin-marble.jpg` from `assets-in\products`, and paste:

```
Make a horizontal 4 by 3 version of this exact image. Keep the vial, the label, the marble riser, the light and the background exactly the same, word for word on the label. Only widen the frame, showing more of the marble tabletop and the mint wall on both sides, with the vial centered and generous empty space around it. Add nothing new to the scene.
```

### 6. NAD+ vial on marble

Why: the NAD+ nasal spray and dropper are on marble and the NAD+ vial is still in water, so the three do not match.

New chat, Images on, Aspect ratio 3:4, attach `nad.jpg` from `assets-in\products`.

```
Edit the attached photo. Keep the vial exactly the same: the same clear glass vial, the same deep matte pine green cap, the same silver crimp, and the same printed label, word for word, with the same logo, the same violet line and the same layout. Do not change, add or remove any word on the label, and add no other text anywhere. Keep the same camera height and the same vertical 3 by 4 framing, with the vial centered and slightly smaller in the frame so there is clear space above the cap.

Change only the setting. Remove all the water: no splash, no droplets, no wet surface, no reflection. Place the vial upright on one simple solid white marble riser with crisp edges, standing on a pale white marble tabletop with soft gray veining. Background a soft pale mint wall, color EEF5F1, fading to white at the top. Bright cool daylight from the upper left, a soft natural shadow to the lower right of the vial, crisp studio product photography. The vial and label stay dry, sharp and fully readable.

Show exactly one vial. No other objects, no plants, no second vial, no bottle, no box, no hands, no syringe, no needle.
```

## Vale's side, no Gemini needed

- When the opening clip arrives: cut it in, and add the four step names on screen as she says "four steps".
- When clip 5 arrives: it drops into the Messenger section on the next build.
- When the clinician photo arrives: convert it and use it on the site steps.
- When the clinician motion clip arrives: use it under the closing line in the video in place of the still photo.
- When the group shot arrives: convert it, use it on the home page hero and in the video's closing scene in place of the six tiles.
- Done Nov 17: the NAD+ nasal spray and dropper photos are on the NAD+ page as the Forms card.
- Dourado, Nov 17: a proper photo of the oral GLP-1 before that offering goes on the site. Two shots on the marble set, edited from the Tirzepatide photo so the label matches: Semaglutide oral, a white HDPE bottle with the pine cap per BRAND.md section 6 and the label reading Semaglutide, and the Microdosing GLP-1 oral form, an amber glass dropper. Save as `semaglutide-oral.jpg` and `microdosing-oral.jpg` in `assets-in/products/`, then `python -I tools/prepare_images.py`.
- Next photo for the needle-free section on the home page: the Microdosing GLP-1 oral form, amber glass dropper per BRAND.md section 6, same marble set, edited from the Tirzepatide photo method. Until it exists the home tile shows the microdosing vial.
- Add a Find your program button under the video player on the Learn page.
- Send the finished video and every new image through vc-reviewer. The reviewer has not yet seen the new closing line, "and it's made after a review of your health history", or the closing scene.
- Update `docs/gemini-prompts.md` with the prompts that passed.
- Logo, asked by Dourado Nov 16: he wants it crisp and in the site's colors, because the purple and violet gradient clashes with the pine, jade and mint. The designer's vector already exists at `brand/logo/VelaCore Health_01/VelaCore Health-01.svg`; the site is using a small PNG of it. Plan: keep the designer's shape, since it is printed on every vial label in every product photo, and prepare two or three color treatments in pine and jade as SVG for Dourado to choose from. Then update `docs/BRAND.md`, which today says the mark is never recolored, and swap the site files. A full redraw of the mark would mean remaking every product photo, so that is only on his explicit word.

## Waiting on a decision or on OpenLoop

- Whether the other four vial photos move from water to marble. Dourado to decide after seeing them side by side.
- Oral Semaglutide and oral Microdosing photos. The proposal gives a daily dose and not the form. Ask OpenLoop whether it is a tablet, drops or something else before making a picture.
- "Free evaluation" wording for a call to action. Not used until OpenLoop confirms in writing what the patient is charged.

## Asked by Dourado late on Nov 16, not started

- Product pictures and site sections by form. The injectable vials stay the lead for the site and for ads. He also wants the non-needle forms shown for people who are tired of injections: sprays, and oral forms. Within the six approved programs that means the NAD+ nasal spray and dropper, which are made, and the oral forms of Semaglutide and Microdosing GLP-1, which wait on OpenLoop naming the form. A form-based section on the site is a design and copy job for Vale, vc-copy and vc-reviewer.
- A men's sexual health category. He wants to add it and sees it as a strong seller. It is outside the six approved programs, so nothing is written or built for it. It needs, in order: Dourado's decision to change the approved list in CLAUDE.md and COMPLIANCE.md, a separate order form and fee from OpenLoop, a check of what LegitScript and the Meta and Google ad policies allow for that category, and then copy and images. Vale advised deciding it after the first six are certified.

## vc-reviewer, Nov 16

First pass blocked three things and all three were fixed the same night: the AI clinician's face on the step 2 photo and in the video's closing line clip, both now cropped to hands and chart, and a malformed 503A on the Microdosing vial in the hero, now patched. The second look passed all three for the site. Use of the video in any ad stays blocked. Two hand patches exist on `assets-in/lifestyle/hero-group.jpg`, both made with ffmpeg by copying a correct word from a neighboring vial in the same image, and both were compared pixel by pixel by the reviewer: HEALTH on the Semaglutide vial, copied from Tirzepatide, and 503A on the Microdosing GLP-1 vial, copied from Sermorelin. The version before the second patch is `_hero-group-six-before-503-patch.jpg`. The reviewer also set what the Learn page must carry beside the player; that list is in its Nov 16 report and must be built before the video goes on the page.

## Done on Nov 16

- Clip 3, redone once for a straight chain. Clip 4, first run.
- NAD+ nasal spray and NAD+ oral dropper, each in water and on marble.
- Sermorelin vial on marble, tall version.
- Narration re-recorded in Bella's voice and approved line by line. Details in `docs/video-peptides-script.md`.
- New mix: matched line levels, ambient bed, subtitles as words only, closing scene with the six programs and a button click with an ordinary mouse click sound. No lead-in sound effect; Dourado disliked both the chime and the swell.

## Clinician shot in the explainer, late Nov 16, waiting on Dourado

- The closing scene logo is now the site header lockup, jade mark with the pine and jade wordmark. vc-reviewer passed it.
- Dourado found the chin-down crop too tight: the eye goes to the chart, and the handwriting is scribble.
- Dourado's decision, Nov 16: the whole frame with her face, and no label over the shot. He tried the label and did not like how it looked.
- The disclosure moved to the closing scene small print: People and images are AI-generated illustrations, not real clinicians or patients. The same line must be visible text beside the player on the Learn page.
- The house rule in `docs/gemini-prompts.md` section 8 was rewritten to match. It is our own rule, not a quoted LegitScript rule. vc-reviewer has not seen this version yet; it goes back with the Learn page block.
- Fallback if LegitScript or the attorney objects: a new Veo clip, seen from behind her shoulder, reading a chart on a tablet, no writing and no face.
- Question for the attorney packet: is a labeled AI-generated clinician acceptable on a telehealth site under FTC rules and for LegitScript.

## Single vials on marble, Nov 16 late night

Dourado's decision: all six product photos on marble, no water.

- Made and checked line by line: `tirzepatide-marble.jpg`, `semaglutide-marble.jpg`, `microdosing-marble.jpg`, `glutathione-marble.jpg`, all in `assets-in/products`.
- The method that works: make one good photo, then attach it first and ask Gemini to change only the product name and the two colored lines. Same camera, riser and light every time, and the fine print stays as it was. Rebuilding the scene per vial gave a different camera and a broken 5 in 503A on the first Semaglutide try.
- Ask for the vial large in the frame, about three quarters of the height. Small vials are what made labels look blurry on the site.
- NAD+ and Sermorelin on the site are the earlier marble photos, cropped to match. Their riser and vial shape differ a little. Gemini hit its limit; redo both with the method above after the Nov 17 reset, attaching `tirzepatide-marble.jpg` first and `semaglutide-marble.jpg` second for the violet.
- The site copies in `public/images/products` were made directly with ffmpeg at 1200 by 1600, not with `tools/prepare_images.py`. The water versions are in git history.

## Step 4 photo for How it works, asked Nov 17 2026

Why: step 4 is ongoing reviews and support. The kitchen photo from the hero does not say that. Save the download as `step-support.jpg` in `assets-in/lifestyle`. Replaces `hero.webp` in the step 4 entry of the `flow` block in `tools/pages.py`.

New chat, Images on, Aspect ratio 4:3.

```
Photoreal candid photograph, horizontal 4 by 3, like a real moment someone caught on a phone, not a stock or studio image. A man about 45, ordinary build, short dark hair with a little gray, relaxed on a light linen sofa in a bright living room at home, morning daylight from a window on the left. He holds his phone in one hand and is typing a short message with his thumb, calm and unhurried, a small easy smile, looking at the phone. A mug of coffee on the side table, a plant in the corner, white walls, one pale mint cushion. The phone screen faces away from the camera and shows nothing readable. Cool natural daylight, soft shadows, true skin tones, shallow depth of field. No logos, no text anywhere, no watch, no medical items, no pills, no needles, no scale.
```

Reject if: any readable screen, any text, a logo, a medical item, a gym or workout look, a visibly thin or muscular build, or a face that reads as a known person.
