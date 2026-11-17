"""Record one narration line with the lines around it as context, then warm the low end.

  python -I tools/video/peptides/vo_line.py N "text" [stability] [style]

Writes 03-edits/peptides-video/vo5/line-N.mp3. Voice is Bella, a stock ElevenLabs voice.
"""
import subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools" / "video"))
import eleven
W = ROOT / "03-edits" / "peptides-video" / "vo5"
VOICE = "hpp4J3VqNfWAUOO0d1Us"
n, text = int(sys.argv[1]), sys.argv[2]
st = float(sys.argv[3]) if len(sys.argv) > 3 else 0.5
sy = float(sys.argv[4]) if len(sys.argv) > 4 else 0.15
src = (ROOT / "tools" / "video" / "peptides" / "build_cut.py").read_text(encoding="utf-8").splitlines()
a = src.index("LINES = [")
L = [s.strip().rstrip(",").strip('"') for s in src[a + 1:a + 7]]
body = {"text": text, "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability": st, "similarity_boost": 0.75, "style": sy, "use_speaker_boost": True, "speed": 1.0}}
if n > 1: body["previous_text"] = L[n - 2]
if n < 6: body["next_text"] = L[n]
tag = sys.argv[5] if len(sys.argv) > 5 else ""
raw = W / f"_l{n}{tag}.mp3"
raw.write_bytes(eleven.call(f"/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128", body, accept="audio/mpeg"))
out = W / (f"line-{n}-take-{tag}.mp3" if tag else f"line-{n}.mp3")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(raw), "-af", "bass=g=4:f=160:w=0.7", "-b:a", "192k", str(out)], check=True)
print("wrote", out.name)
