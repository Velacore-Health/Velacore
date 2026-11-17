"""Builds the peptides explainer cut from the Veo clips, Eric's narration, the music bed and the step pills.

Run from the repo root:  python -I tools/video/peptides/build_cut.py
Reads 03-edits/peptides-video/: clips/clip1.mp4 to clip5.mp4, vo3/beat1.mp3 to beat6.mp3 by default, music-bed.mp3,
label-amino.png, label-peptide.png, label-protein.png, label-messenger.png.
Writes rough-cut.mp4, rough-cut.vtt, rough-cut-sheet.png and rough-cut-beats.json in the same folder.
If clips/clip5.mp4 is missing, beat 5 plays over a plain mint holding frame.
Needs ffmpeg and ffprobe on PATH. Standard library only.
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
WORK = ROOT / "03-edits" / "peptides-video"
OUT = "rough-cut"
VO = sys.argv[1] if len(sys.argv) > 1 else "vo3"   # narration folder: vo3 is Bella, lowered; vo2 is Eric
FPS, W, H = 30, 1280, 720
LEAD, GAP, XF = 0.9, 0.6, 0.4          # first word, pause between lines, cross dissolve
CARD_HOLD, CARD_LAG = 7.0, 0.7           # closing card length, pause after the last word
MUSIC_GAIN, VOICE_LUFS = 0.45, -16       # bed sits about 8 dB under the voice in the gaps, lower while she speaks
MUSIC_SKIP = 6.0
MUSIC = "music-bed-aura.mp3"             # soothing ambient pad, ElevenLabs music, Nov 16
LEAD_IN, LEAD_IN_GAIN = "lead-in-swell.wav", 0.0   # lead-in sound switched off Nov 16: Dourado disliked the chime and the swell; the bed fading up is the lead-in
LINE_LUFS = -19                          # every narration line is brought to the same loudness before the mix
STEPS_IN = 5.0                            # the four step names come in once the four beads have settled
GAP_AFTER_OPEN = 1.9                      # longer pause after line 1 so all four step names can be read
SUBS = True                              # subtitles on the picture, words only, drawn by render_overlays.py
# hand-set subtitle breaks where the automatic ones split a phrase badly; the words must match the line exactly
SUB_OVERRIDE = {6: ["Whether a peptide is right for you", "is a licensed clinician's decision,", "and it's made after a review", "of your health history."]}
SUB_MAX = 44                             # longest subtitle line, in characters
MINT, PINE = "EEF5F1", "15302A"
FONT = "C\\:/Windows/Fonts/segoeuisl.ttf"  # stand-in; the brand face Hanken Grotesk is not installed here
CARD_TEXT = "Education only, not medical advice. Prescription required."
LINES = [
    "If peptides sound complicated, you're not alone. Here's the simple version in four steps.",
    "It starts with amino acids, the small building blocks. Your body uses twenty kinds.",
    "Link a few together and you have a peptide. It's a short chain, usually two to fifty amino acids long.",
    "Link many more and fold the chain, and you have a protein. Same building blocks, just a much longer chain.",
    "Many peptides work as messengers. A peptide fits a receptor on a cell, like a key in a lock, and the cell responds.",
    "Whether a peptide is right for you is a licensed clinician's decision, and it's made after a review of your health history.",
]
PILLS = {1: "label-amino.png", 2: "label-peptide.png", 3: "label-protein.png", 4: "label-messenger.png"}
# where each clip starts in its source, in seconds
CLIP_IN = {0: 0.0, 1: 5.5, 2: 1.4, 3: 0.0, 4: 0.0}
CLICK_AT, CLICK_GAIN = 4.82, 0.4          # seconds into the closing scene when the button is pressed; click level


def run(args, **kw):
    return subprocess.run(args, cwd=WORK, capture_output=True, text=True, **kw)


def speech_end(path):
    """End of the last spoken sound, so trailing silence is dropped."""
    total = float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).stdout)
    err = run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "silencedetect=n=-40dB:d=0.25", "-f", "null", "-"]).stderr
    starts = [float(x) for x in re.findall(r"silence_start: ([0-9.]+)", err)]
    ends = [float(x) for x in re.findall(r"silence_end: ([0-9.]+)", err)]
    if starts and (len(ends) < len(starts) or ends[-1] >= total - 0.05):
        return starts[-1]
    return total


def ts(x):
    return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{x % 60:06.3f}"


# ---- timeline from the real narration
beats, t = [], LEAD
for i in range(6):
    d = speech_end(f"{VO}/beat{i + 1}.mp3")
    beats.append({"beat": i + 1, "start": round(t, 3), "end": round(t + d, 3), "speech": round(d, 3)})
    t += d + (GAP_AFTER_OPEN if i == 0 else GAP)
cuts = [0.0] + [round((beats[i]["end"] + beats[i + 1]["start"]) / 2, 3) for i in range(5)]
cuts[1] = round(beats[1]["start"] - 0.25, 3)   # hold the opening picture until just before line 2, so the step names can be read
card_at = round(beats[5]["end"] + CARD_LAG, 3)
end = round(card_at + CARD_HOLD, 3)
cuts += [card_at, end]                    # 8 marks, 7 picture segments
nseg = len(cuts) - 1
seg_len = []
for k in range(nseg):
    span = cuts[k + 1] - cuts[k]
    seg_len.append(round(span + (XF / 2 if k in (0, nseg - 1) else XF), 3))

has5 = (WORK / "clips" / "clip5.mp4").exists()

# ---- picture
inputs, filt = [], []
def add(*a):
    inputs.extend(a)
    return (len([x for x in inputs if x == "-i"]) - 1)

norm = f"fps={FPS},scale={W}:{H},setsar=1,format=yuv420p"
labels = []
for k in range(5):
    if k == 4 and not has5:
        n = add("-f", "lavfi", "-i", f"color=c=0x{MINT}:s={W}x{H}:r={FPS}:d={seg_len[k]}")
        filt.append(f"[{n}:v]{norm}[s{k}]")
    else:
        n = add("-i", f"clips/clip{k + 1}.mp4")
        left = 10.0 - CLIP_IN[k] - 0.05
        if left < seg_len[k]:  # not enough clip after the in point: slow it gently to fill the beat
            filt.append(f"[{n}:v]trim=start={CLIP_IN[k]}:duration={left},setpts={seg_len[k] / left:.4f}*(PTS-STARTPTS),"
                        f"minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:vsbmc=1,trim=duration={seg_len[k]},setpts=PTS-STARTPTS,"
                        f"scale={W}:{H},setsar=1,format=yuv420p[s{k}]")
        else:
            filt.append(f"[{n}:v]trim=start={CLIP_IN[k]}:duration={seg_len[k]},setpts=PTS-STARTPTS,{norm}[s{k}]")
    labels.append(f"s{k}")
# beat 6: the clinician at her desk reviewing a chart, clips/clip6.mp4, animated in Veo from the step-clinician office photo
n = add("-i", "clips/clip6.mp4")
filt.append(f"[{n}:v]trim=start=0.3:duration={seg_len[5]},setpts=PTS-STARTPTS,{norm}[s5]")
labels.append("s5")
# closing scene: the six programs, the button and a click, drawn by render_overlays.py
n = add("-i", "end-scene.mp4")
filt.append(f"[{n}:v]trim=duration={seg_len[6]},setpts=PTS-STARTPTS,{norm}[s6]")
labels.append("s6")
# cross dissolves
prev = labels[0]
for k in range(1, nseg):
    off = round(cuts[k] - XF / 2, 3)
    filt.append(f"[{prev}][{labels[k]}]xfade=transition=fade:duration={XF}:offset={off}[x{k}]")
    prev = f"x{k}"
# step pills, moved to the upper left so they clear the subtitles, beats 2 to 5
for b, png in PILLS.items():
    n = add("-loop", "1", "-framerate", str(FPS), "-t", str(end), "-i", png)
    a, z = beats[b]["start"] - 0.2, beats[b]["end"] + 0.1
    filt.append(f"[{n}:v]format=rgba,fade=t=in:st={a:.3f}:d=0.4:alpha=1,fade=t=out:st={z:.3f}:d=0.4:alpha=1[p{b}]")
    filt.append(f"[{prev}][p{b}]overlay=0:-565:enable='between(t,{a:.3f},{z + 0.4:.3f})'[o{b}]")
    prev = f"o{b}"
# subtitles: each line split into short phrases, timed by their share of the line
def phrases(line):
    out = []
    for sent in re.split(r"(?<=[.!?]) ", line):
        cur = ""
        for part in re.split(r"(?<=,) ", sent):
            for word_run in ([part] if len(part) <= SUB_MAX else part.split(" ")):
                cand = (cur + " " + word_run).strip()
                if len(cand) <= SUB_MAX:
                    cur = cand
                else:
                    if cur:
                        out.append(cur)
                    cur = word_run
        if cur:
            out.append(cur)
    return out

subs = []
for b, line in zip(beats, LINES):
    ph = SUB_OVERRIDE.get(b["beat"]) or phrases(line)
    total = sum(len(x) for x in ph)
    t0 = b["start"]
    for x in ph:
        t1 = t0 + b["speech"] * len(x) / total
        subs.append((round(t0, 3), round(t1, 3), x))
        t0 = t1
(WORK / "subs").mkdir(exist_ok=True)
(WORK / "subs" / "list.json").write_text(json.dumps([{"start": a, "end": z, "text": x} for a, z, x in subs], indent=1), encoding="utf-8")
# draw the subtitle PNGs, and the closing scene if it is not there yet
draw = [sys.executable, "-I", str(ROOT / "tools" / "video" / "peptides" / "render_overlays.py")]
if "end" in sys.argv[2:] or not (WORK / "end-scene.mp4").exists():
    draw.append("end")
subprocess.run(draw, check=True, cwd=ROOT)
# the four step names appear under the four beads as she says "four steps"
n = add("-loop", "1", "-framerate", str(FPS), "-t", str(end), "-i", "subs/steps.png")
sa, sz = STEPS_IN, cuts[1] - XF / 2 - 0.3
filt.append(f"[{n}:v]format=rgba,fade=t=in:st={sa:.3f}:d=0.4:alpha=1,fade=t=out:st={sz:.3f}:d=0.3:alpha=1[stp]")
filt.append(f"[{prev}][stp]overlay=0:0:enable='between(t,{sa:.3f},{sz + 0.3:.3f})'[stepped]")
prev = "stepped"
if SUBS:
    for i, (a, z, x) in enumerate(subs):
        last = i == len(subs) - 1 or subs[i + 1][0] - z > 0.3
        n = add("-loop", "1", "-framerate", str(FPS), "-t", str(end), "-i", f"subs/s{i:02d}.png")
        filt.append(f"[{prev}][{n}:v]overlay=0:0:enable='between(t,{a:.3f},{z + (0.25 if last else 0):.3f})'[sb{i}]")
        prev = f"sb{i}"
filt.append(f"[{prev}]trim=duration={end},format=yuv420p[vout]")

# ---- sound: clip audio is never mapped, so the Veo sound is muted
voices, line_gain = [], []
for i, b in enumerate(beats):
    n = add("-i", f"{VO}/beat{i + 1}.mp3")
    ms = int(b["start"] * 1000)
    cut = b["speech"] + 0.15
    lj = run(["ffmpeg", "-hide_banner", "-nostats", "-i", f"{VO}/beat{i + 1}.mp3", "-af", "loudnorm=print_format=json", "-f", "null", "-"]).stderr
    gain = LINE_LUFS - float(re.search(r'"input_i"\s*:\s*"(-?[0-9.]+)"', lj).group(1))
    line_gain.append(round(gain, 1))
    filt.append(f"[{n}:a]atrim=0:{cut:.3f},afade=t=in:st=0:d=0.02,afade=t=out:st={cut - 0.1:.3f}:d=0.1,volume={gain:.2f}dB,adelay={ms}|{ms}[v{i}]")
    voices.append(f"[v{i}]")
filt.append("".join(voices) + f"amix=inputs=6:normalize=0,apad,atrim=0:{end},loudnorm=I={VOICE_LUFS}:TP=-1.5:LRA=11,aresample=48000,asplit[voice][key]")
n = add("-i", MUSIC)
# a little air added so the bed carries on small speakers, then ducked under the voice so it lifts in the gaps
# the track itself takes six seconds to fade in, so start six seconds into it: the bed is there from the first frame
filt.append(f"[{n}:a]atrim={MUSIC_SKIP}:{end + MUSIC_SKIP},asetpts=PTS-STARTPTS,highshelf=f=1800:g=7,volume={MUSIC_GAIN},afade=t=in:st=0:d=0.5,"
            f"afade=t=out:st={end - 4:.3f}:d=4,aresample=48000[bed]")
filt.append("[bed][key]sidechaincompress=threshold=0.03:ratio=4:attack=80:release=220[music]")
n = add("-i", LEAD_IN)
filt.append(f"[{n}:a]volume={LEAD_IN_GAIN},afade=t=in:st=0:d=0.5,aresample=48000[lead]")
# a soft mouse click as the pointer presses the button in the closing scene
click_ms = int((card_at - XF / 2 + CLICK_AT) * 1000)
n = add("-i", "click.wav")
filt.append(f"[{n}:a]volume={CLICK_GAIN},adelay={click_ms}|{click_ms},aresample=48000[click]")
filt.append(f"[voice][music][lead][click]amix=inputs=4:normalize=0,alimiter=limit=0.84:level=false,atrim=0:{end}[aout]")

cmd = ["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[vout]", "-map", "[aout]",
       "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19", "-preset", "slow", "-r", str(FPS),
       "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-movflags", "+faststart", "-t", str(end), f"{OUT}.mp4"]
r = run(cmd)
if r.returncode:
    sys.exit("ffmpeg failed:\n" + r.stderr[-3000:])

# ---- captions, word for word with the narration
vtt = ["WEBVTT", ""]
for b, line in zip(beats, LINES):
    vtt += [f"{ts(b['start'])} --> {ts(b['end'] + 0.3)}", line, ""]
(WORK / f"{OUT}.vtt").write_text("\n".join(vtt), encoding="utf-8")
(WORK / f"{OUT}-beats.json").write_text(json.dumps({"beats": beats, "cuts": cuts, "clip5": has5}, indent=1))

# ---- checks
cols = 6
rows = -(-int(end // 2 + 1) // cols)
run(["ffmpeg", "-v", "error", "-y", "-i", f"{OUT}.mp4", "-vf", f"fps=1/2,scale=480:-1,tile={cols}x{rows}", "-frames:v", "1", f"{OUT}-sheet.png"])
dur = run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f"{OUT}.mp4"]).stdout.strip()
loud = run(["ffmpeg", "-hide_banner", "-nostats", "-i", f"{OUT}.mp4", "-af", "ebur128=peak=true", "-f", "null", "-"]).stderr
print("wrote", f"03-edits/peptides-video/{OUT}.mp4", dur, "s", "clip5" if has5 else "clip5 placeholder")
for b in beats:
    print(f"beat {b['beat']}: voice {b['start']:.2f} to {b['end']:.2f}")
print("picture cuts:", cuts)
print("line gains dB:", line_gain)
print("subtitles:", len(subs))
for key in ("I:", "LRA:", "Peak:"):
    m = re.findall(rf"{key}\s+(-?[0-9.]+ \w+)", loud)
    if m:
        print(key, m[-1])
