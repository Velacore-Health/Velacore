# Learn page photo swaps, Nov 18 2026

Dourado asked to swap photos on the Learn page after it moved to photo cards. Three new Gemini images. Run them the same way as `docs/gemini-site-set-nov17.md`: a new chat for each, Images on, 3.1 Pro, the aspect ratio named in the heading, the largest size offered, no attachments, paste the block, check it against the reject list at the bottom, download, rename, and drop it in `assets-in/lifestyle`. Then tell Vale "convert the images".

## What we need, at a glance

| # | File name | Aspect | Replaces | Where it goes |
|---|---|---|---|---|
| 1 | step-visit.png | 4:3 | The man in his late forties at a laptop | Learn card How do I know if they are right for me, and step 1 on How it works |
| 2 | learn-taken.png | 4:3 | The dog sniffing a parcel | Learn card How is it taken |
| 3 | learn-difference.png | 4:3 | The woman on the sofa, still used at the top of About | Learn card Peptides vs. GLP-1s |

The old step-visit original is kept as `assets-in/lifestyle/_prev-step-visit-older.jpg`. vc-reviewer PASS on these prompts Nov 18 2026. When the new step-visit is placed, its alt text changes from a man to a person in tools/pages.py and public/learn.html.

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

## 2. learn-taken.png, 4:3

Hands and objects only, no face or body.

```
A photoreal close photograph, horizontal 4 by 3, seen from slightly above, 50 mm lens look at f/2.8. Two hands lift a folded plain white instruction card out of an open plain white shipping box on a light oak kitchen counter. Inside the box, folded pale mint tissue paper. The card shows only soft gray blocks and lines, too blurred to read. Beside the box on the counter: a small green plant in a white pot, softly blurred. Only the hands and forearms are in frame, with the cuffs of a soft gray sweater.

ANATOMY, follow exactly
Exactly two hands, a left and a right, belonging to one person standing at the counter. Five fingers on each hand, the thumbs on top of the card and the fingers beneath it, natural knuckles, short clean natural nails, realistic skin texture.

LIGHT AND COLOR
Cool soft daylight from a window on the left, white, light oak, pale mint and soft gray, one touch of green.

DO NOT INCLUDE
No face, no body beyond the forearms. Nothing else in the box. No readable text, numbers or logos on the card, the box or anywhere. No vials, bottles, pills, syringes, needles, scales, tape measures. No extra fingers.
```

## 3. learn-difference.png, 4:3

```
A photoreal editorial photograph, horizontal 4 by 3, shot on a full-frame camera with a 35 mm lens at f/2.8, candid and calm. Not an illustration, not a 3D render.

THE PERSON
One man in his early thirties with short dark hair and a neatly trimmed short beard, seated in a pale wooden chair at a small round white table by a window on the right third of the frame, seen three quarters from the side. He reads a tablet he holds in both hands, his eyes on the screen, relaxed and focused. He wears a light blue button-down shirt with the sleeves rolled once. An ordinary healthy build, approachable, well groomed.

ANATOMY, follow exactly
One body, exactly two arms and two hands, holding the tablet by its sides, the thumbs on the front edge and four fingers behind it on each hand, short clean natural nails. No extra fingers, no fused fingers, no third hand.

THE ROOM
On the table only a white ceramic cup of tea on a saucer. The left half of the frame is calm empty space: a smooth white wall with a very soft pale mint tone, daylight from a tall window on the right. One tall green plant in a plain white pot in the far corner, softly blurred. Nothing hangs on the walls, nothing on the floor.

LIGHT AND COLOR
Cool soft daylight, gentle shadows, no lamps, no glow. White, pale mint, light wood and soft blue, the plant as the one touch of green. Natural skin texture, true-to-life colors, shallow depth of field.

DO NOT INCLUDE
The tablet screen faces away from the camera so nothing on it can be seen. No readable text, numbers or logos anywhere. No pills, syringes, needles, scales, tape measures, mirrors. No workout clothes or gym gear. No looking at the camera. No extra fingers.
```

---

## Reject the image if

- Any hand has more or fewer than five fingers, or there is an extra hand or arm.
- Any readable word, number or logo appears.
- The person looks at the camera instead of the screen or the card.
- The person looks older than the late thirties, or model-thin.
- Anything in the never list shows: pills, needles, syringes, vials, scales, tape measures, mirrors, gym gear.
- The skin looks glossy or airbrushed.

When one fails, reply in the same chat with the one thing to fix, for example "same image, but the left hand must have exactly five fingers".
