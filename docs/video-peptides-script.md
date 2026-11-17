# Learn page explainer video: narration script

Draft by vc-copy, Nov 13 2026. Not approved. Nothing is recorded, published or posted without Dourado's word, and the script goes through vc-reviewer first.

The video animates the four-step drawing on `public/learn.html`, the pep-walk block: amino acid, peptide, protein, messenger. One narrator, an ElevenLabs AI voice.

Target: 40 to 50 seconds at a calm, natural pace. Narration total: 110 words.

Numbers are written as words in the narration so the AI voice reads them cleanly. The captions use numerals so they match the page.

## Beats

### 1. Opener

Narration:
Peptides can sound complicated. Here is the simple version, in four steps.

Caption: Peptides, in four steps

Words: 12

### 2. Amino acid

Narration:
It starts with amino acids, the small building blocks. Your body uses twenty kinds.

Caption: Amino acids are the building blocks. 20 kinds.

Words: 14

### 3. Peptide

Narration:
Link a few together and you have a peptide. It is a short chain, usually two to fifty amino acids long.

Caption: A peptide is a short chain, usually 2 to 50

Words: 21

### 4. Protein

Narration:
Link many more and fold the chain, and you have a protein. Same building blocks, just a much longer chain.

Caption: A protein is a much longer chain, folded

Words: 20

### 5. Messenger

Narration:
Many peptides work as messengers. A peptide fits a receptor on a cell, like a key in a lock, and the cell responds.

Caption: A peptide fits a receptor, and the cell responds

Words: 23

### 6. Closing

Narration:
Whether a peptide is right for you is a licensed clinician's decision, made after a review of your health history.

Caption: A licensed clinician decides if a peptide is right for you

Words: 20

## Title card

Peptides, explained simply.

## Closing card, small type, per vc-reviewer Nov 13

Education only, not medical advice. Prescription required.

If the video is ever used outside the Learn page, on social, ads, email or YouTube, the closing card must also carry the compounded-medication line, and the AI-voice note goes in the caption or description.

## Page notes, per vc-reviewer Nov 13

- Under the player: "Narration uses an AI-generated voice." Advisable, not required.
- A caption track that matches the narration word for word.
- No autoplay with sound. The video sits behind a play button, so it does not add a second motion moment to the page.
- Use a stock or designed ElevenLabs voice, never a clone of a real person.

## Word count

| Beat | Words |
|------|-------|
| 1. Opener | 12 |
| 2. Amino acid | 14 |
| 3. Peptide | 21 |
| 4. Protein | 20 |
| 5. Messenger | 23 |
| 6. Closing | 20 |
| Total | 110 |

## Notes for the voice and the edit

- Leave about half a second of silence between beats so each drawing step can land. In ElevenLabs this can be a line break or a break tag of 0.5 seconds.
- Pronunciation to check on the first take: peptide as PEP-tide, receptor as ree-SEP-ter.
- No product names, no prices and no brand-name drugs appear, so the video names no treatment. "Prescription required" is not strictly needed on the card, but it can sit in small type under the title card if Dourado wants it.
- The key and lock line is an analogy for fit only. It makes no claim about what the response does.

## Edit decisions, Nov 13 2026, approved by Dourado

- Look: AI video clips from Veo in Gemini, prompts in `docs/gemini-prompts.md` block 13, replacing the flat code animation, which Dourado found not cutting edge enough.
- Voice: Eric, ElevenLabs voice id cjVigY5qzO86Huf0OWal, settings stability 0.8, style 0, speed 0.84, for a calm, educational, empathetic read. Opening line softened to "If peptides sound complicated, you are not alone."
- Pacing: about 0.6 seconds between the end of one line and the start of the next, trailing silence trimmed. Dourado approved this pace on the clips 1 and 2 preview.
- Music: a quiet ambient bed from ElevenLabs music, ducked under the voice, faded out before its closing swell.
- Step tags: a small pill in the lower left names each step: Amino acids, Peptide, Protein, Messenger.

## Final narration, Nov 16 2026, approved line by line by Dourado

Voice changed from Eric to Bella, a stock ElevenLabs voice, with a little warmth added in the low end. Dourado wanted a female voice that is calm and informative with some lift. Each line was recorded and approved on its own. The takes are in `03-edits/peptides-video/vo5/` as `beat1.mp3` to `beat6.mp3`. Build with `python -I tools/video/peptides/build_cut.py vo5`.

Captions, word for word:

1. If peptides sound complicated, you're not alone. Here's the simple version in four steps.
2. It starts with amino acids, the small building blocks. Your body uses twenty kinds.
3. Link a few together and you have a peptide. It's a short chain, usually two to fifty amino acids long.
4. Link many more and fold the chain, and you have a protein. Same building blocks, just a much longer chain.
5. Many peptides work as messengers. A peptide fits a receptor on a cell, like a key in a lock, and the cell responds.
6. Whether a peptide is right for you is a licensed clinician's decision, and it's made after a review of your health history.

Line 6 wording changed from the version vc-reviewer cleared on Nov 13, which read "decision, made after a review". The meaning is the same. vc-reviewer has not yet seen the new line; it must confirm it when the finished video is reviewed.

How the takes were shaped, for anyone redoing a line:

- Line 1 is two recordings joined, so "alone" settles before the second sentence.
- Line 3 has its comma pause after "short chain" trimmed to about a tenth of a second.
- Lines 2, 4 and 5 were read with an upbeat mark in the reading script so the sentence endings do not drop. The marks are not in the captions.
- Line 6 is on the newer ElevenLabs engine, eleven_v3, directed as calm, soothing and informative with a gentle smile. Lines 1 to 5 are on eleven_multilingual_v2.
- Every line gets a short fade in and out in the build, which removed pops at the joins.

Picture notes from the same session: clips 3 and 4 were made Nov 16; clip 5 is still to come. The amino acid clip starts 5.5 seconds in and is slowed about a third so the bead lights up early and holds to the cut.
