# Learn page photo swaps, Nov 18 2026

Dourado asked to swap photos on the Learn page after it moved to photo cards. Three new Gemini images. Run them the same way as `docs/gemini-site-set-nov17.md`: a new chat for each, Images on, 3.1 Pro, the aspect ratio named in the heading, the largest size offered, no attachments unless the prompt names some, paste the block, check it against the reject list at the bottom, download, rename, and drop it in `assets-in/lifestyle`, or `assets-in/products` where the prompt says so. Then tell Vale "convert the images".

## What we need, at a glance

| # | File name | Aspect | Replaces | Where it goes |
|---|---|---|---|---|
| 1 | step-visit.png | 4:3 | The man in his late forties at a laptop | Learn card How do I know if they are right for me, and step 1 on How it works |
| 2 | learn-forms.png | 16:9 | The dog sniffing a parcel | Learn card How is it taken, the four forms side by side |
| 3 | learn-peptides.png | 3:2 |  The woman on the sofa, still used at the top of About | Learn card Peptides vs. GLP-1s |

The old step-visit original is kept as `assets-in/lifestyle/_prev-step-visit-older.jpg`. vc-reviewer PASS Nov 18 2026, prompt 2 rechecked the same day. When the new step-visit is placed, its alt text changes from a man to a person in tools/pages.py and public/learn.html.

## House rules these prompts follow

- Adults in their late twenties to late thirties, varied backgrounds, ordinary healthy builds, current casual clothes, looking at what they are doing, not at the camera.
- Cool daylight, white and pale mint rooms, one touch of green, the person close and off center with calm empty space.
- Never: pills, needles, syringes, injections, scales, tape measures, mirrors, waistlines, gym gear, readable text, logos.
- No person is ever named, captioned or presented as a Velacore patient.

---

## 1. step-visit.png, 4:3

```
A photoreal editorial photograph, horizontal 4 by 3, shot on a full-frame camera with a 35 mm lens at f/2.8, candid and calm, like a quiet weekday morning at home. Not an illustration, not a 3D render.

THE PERSON
One woman in her early thirties with shoulder-length dark brown hair tucked behind one ear, seated at a light oak kitchen table on the right third of the frame, seen from the side, her eyes on the laptop screen in front of her as she types. She wears a soft oatmeal knit sweater with the sleeves pushed up a little. Natural, approachable, well groomed, an ordinary healthy build.

ANATOMY, follow exactly
One body, exactly two arms and two hands, both resting on the laptop keyboard, five fingers on each hand, short clean natural nails, wrists bent naturally. No extra fingers, no fused fingers, no third hand.

THE TABLE AND ROOM
On the table only the slim silver laptop, its screen angled away so nothing on it can be read, a white ceramic mug of coffee and a small green plant in a plain white pot, softly blurred. The left half of the frame is calm empty space: a smooth white wall with a very soft pale mint tone where daylight falls from a large window out of frame on the left. Nothing hangs on the walls, nothing on the floor.

LIGHT AND COLOR
Cool soft morning daylight from the left, gentle shadows, no lamps, no glow. White, light oak, pale mint and soft oatmeal, the plant as the one touch of green. Natural skin texture, true-to-life colors, shallow depth of field.

DO NOT INCLUDE
No readable text, numbers or logos on the laptop or anywhere. No pills, syringes, needles, scales, tape measures, mirrors. No workout clothes or gym gear. No looking at the camera. No extra fingers.
```

## 2. learn-forms.png, 16:9, folder products

Changed Nov 18 2026 at Dourado's request: the Learn card How is it taken has to show what it describes, the forms a prescription can come in. This replaces the box and instruction card picture. It is a product photo, so the illustration note sits on the page with it.

Attach four files in this order, all from `assets-in` then `products`: `semaglutide.jpg`, `semaglutide-oral.jpg`, `nad-oral.jpg`, `nad-nasal.jpg`.

```
Combine the four attached product photos into one horizontal 16 by 9 product photograph. Take each container exactly as it is: the same glass, the same caps, dropper and spray pump, and the same printed labels, word for word, with the same logo and the same colored lines. Do not change, add or remove any word on any label, and add no other text anywhere.

Stand all four upright in one row, evenly spaced with a clear gap between each, from left to right: the injection vial, the oral bottle with its cap on and closed, the amber dropper bottle, and the nasal spray bottle. Each stands on its own simple solid white marble riser of equal height, on a pale white marble tabletop with soft gray veining. Background a soft pale mint wall fading to white at the top. Bright cool daylight from the upper left, a soft shadow to the lower right of each. Every label faces the camera, sharp and readable. The row is centered with calm empty space on both sides.

No loose tablets or capsules, no water, no plants, no other objects, no syringe, no needle, no hands.
```

## 3. learn-peptides.png, 3:2, no attachments

Changed Nov 18 2026 at Dourado's request: he wants the Peptides vs. GLP-1s diagram to look high tech, not a basic illustration. Gemini makes the picture with no words in it; Vale lays the words Peptides and GLP-1s over it in the page, so they stay sharp and spelled right. Dourado's decision overrides the BRAND.md line against 3D renders for this education visual.

```
A premium high-tech scientific visualization, horizontal 3 by 2, photoreal 3D render with the look of a modern biotech brand, clean and calm, not a cartoon, not flat clip art.

THE SUBJECT
One large translucent glass sphere, centered slightly left, filling about two thirds of the frame height. Inside it, a delicate chain of small glossy beads linked like a string of pearls, round beads, not capsule or tablet shaped, curves gracefully through the sphere, the beads alternating deep jade green and soft mint, representing a chain of amino acids. Nested inside the large sphere, in its lower right part, sits one smaller solid sphere in deep jade green with a soft inner glow, about one third the size of the large sphere, fully inside it and not touching its edge. The upper left part of the large sphere stays clear and empty so a word can be placed there later. The small jade sphere stays plain and smooth so words can be placed on it later.

BACKGROUND AND LIGHT
A soft gradient background from very pale mint to white, with a faint subtle glow behind the sphere. Cool soft studio light from the upper left, gentle reflections and refraction in the glass, a soft shadow beneath. Colors only deep pine green, jade green, mint and white, with a faint hint of soft blue in the glass reflections.

DO NOT INCLUDE
No text, no letters, no numbers, no labels, no logos anywhere. No pills, syringes, needles, vials, people or hands. No DNA double helix. No purple. No busy particles or sparkles.
```

---

## Reject the image if

- For learn-forms only: the four product labels are meant to be readable. Reject it if any label word changes, if loose tablets or a needle appear, or if any other text shows.
- For learn-peptides: reject it if any letter or number appears, if the small sphere is not fully inside the large one, if a DNA helix appears, or if any bead or sphere looks like a pill, capsule or tablet.

- Any hand has more or fewer than five fingers, or there is an extra hand or arm.
- Any readable word, number or logo appears.
- The person looks at the camera instead of the screen or the card.
- The person looks older than the late thirties, or model-thin.
- Anything in the never list shows: pills, needles, syringes, vials, scales, tape measures, mirrors, gym gear.
- The skin looks glossy or airbrushed.

When one fails, reply in the same chat with the one thing to fix, for example "same image, but the left hand must have exactly five fingers".
