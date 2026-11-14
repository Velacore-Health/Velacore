"""Renders the peptides explainer: times the animation to the narration, draws every frame, mixes the voice.

Run from the repo root:  python -I tools/video/peptides/render.py
Needs 03-edits/peptides-video/vo/beat1.mp3 to beat6.mp3 (ElevenLabs, voice Eric). Writes
03-edits/peptides-video/peptides.mp4 and peptides.vtt, plus beats.json with the timing.
"""
import json, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).parent
WORK = ROOT / "03-edits" / "peptides-video"
VO = WORK / "vo"
IDS = ["open", "amino", "pep", "prot", "msg", "close"]
LINES = [
    "Peptides can sound complicated. Here is the simple version, in four steps.",
    "It starts with amino acids, the small building blocks. Your body uses twenty kinds.",
    "Link a few together and you have a peptide. It is a short chain, usually two to fifty amino acids long.",
    "Link many more and fold the chain, and you have a protein. Same building blocks, just a much longer chain.",
    "Many peptides work as messengers. A peptide fits a receptor on a cell, like a key in a lock, and the cell responds.",
    "Whether a peptide is right for you is a licensed clinician's decision, made after a review of your health history.",
]
LEAD, GAP, TAIL, FPS = 0.6, 0.8, 3.2, 30

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout)

beats, t = [], LEAD
for i, bid in enumerate(IDS, 1):
    d = dur(VO / f"beat{i}.mp3")
    beats.append({"id": bid, "start": round(t, 3), "dur": round(d, 3)})
    t += d + GAP
end = beats[-1]["start"] + beats[-1]["dur"] + TAIL
(WORK / "beats.json").write_text(json.dumps(beats, indent=1))

def ts(x):
    return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{x % 60:06.3f}"
vtt = ["WEBVTT", ""]
for b, line in zip(beats, LINES):
    vtt += [f"{ts(b['start'])} --> {ts(b['start'] + b['dur'] + 0.3)}", line, ""]
(WORK / "peptides.vtt").write_text("\n".join(vtt), encoding="utf-8")

# voice track: each beat at its start, loudness to -16 LUFS
inputs, filt = [], []
for i, b in enumerate(beats):
    inputs += ["-i", str(VO / f"beat{i + 1}.mp3")]
    ms = int(b["start"] * 1000)
    filt.append(f"[{i}]adelay={ms}|{ms}[a{i}]")
filt.append("".join(f"[a{i}]" for i in range(len(beats))) + f"amix=inputs={len(beats)}:normalize=0,apad,atrim=0:{end:.3f},loudnorm=I=-16:TP=-1.5:LRA=11[out]")
voice = WORK / "voice.wav"
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt), "-map", "[out]", "-ar", "48000", str(voice)], check=True)

frames = int(end * FPS)
silent = WORK / "picture.mp4"
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-preset", "slow", str(silent)], stdin=subprocess.PIPE)
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": 1280, "height": 720})
    pg.add_init_script(f"window.BEATS = {json.dumps(beats)};")
    pg.goto((HERE / "film.html").as_uri(), wait_until="networkidle")
    pg.evaluate("window.ready")
    for f in range(frames):
        pg.evaluate(f"render({f / FPS})")
        enc.stdin.write(pg.screenshot(type="png"))
        if f % 300 == 0:
            print("frame", f, "of", frames, flush=True)
    br.close()
enc.stdin.close(); enc.wait()
out = WORK / "peptides.mp4"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(silent), "-i", str(voice), "-c:v", "copy", "-c:a", "aac", "-b:a", "128k",
                "-movflags", "+faststart", "-shortest", str(out)], check=True)
print("wrote", out.relative_to(ROOT), f"{end:.1f} s,", frames, "frames")
