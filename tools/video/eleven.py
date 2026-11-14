"""Small ElevenLabs helper for Velacore. Reads ELEVENLABS_API_KEY from .env and never prints it.

  python -I tools/video/eleven.py voices
  python -I tools/video/eleven.py tts VOICE_ID "text" out.mp3
  python -I tools/video/eleven.py credits
  python -I tools/video/eleven.py music "prompt" SECONDS out.mp3
"""
import json, sys, urllib.request
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
API = "https://api.elevenlabs.io"

def key():
    for line in (ROOT / ".env").read_text(encoding="utf-8-sig").splitlines():
        if line.strip().startswith("ELEVENLABS_API_KEY="):
            return line.split("=", 1)[1].strip()
    sys.exit("ELEVENLABS_API_KEY missing from .env")

def call(path, body=None, accept="application/json"):
    req = urllib.request.Request(API + path, headers={"xi-api-key": key(), "Accept": accept, "Content-Type": "application/json"},
                                 data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()

def main():
    cmd = sys.argv[1]
    if cmd == "credits":
        d = json.loads(call("/v1/user/subscription")); print(d["character_count"], "of", d["character_limit"], "used")
    elif cmd == "voices":
        for v in json.loads(call("/v1/voices"))["voices"]:
            l = v.get("labels", {})
            print(v["voice_id"], "|", v["name"], "|", v.get("category"), "|", l.get("gender"), l.get("age"), l.get("accent"), l.get("descriptive") or l.get("description"), l.get("use_case"))
    elif cmd == "tts":
        vid, text, out = sys.argv[2], sys.argv[3], sys.argv[4]
        # optional 5th argument: JSON voice settings, e.g. '{"stability":0.75,"style":0,"speed":0.85}'
        vs = {"stability": 0.55, "similarity_boost": 0.75, "style": 0.1, "use_speaker_boost": True}
        if len(sys.argv) > 5:
            vs.update(json.loads(sys.argv[5]))
        audio = call(f"/v1/text-to-speech/{vid}?output_format=mp3_44100_128",
                     {"text": text, "model_id": "eleven_multilingual_v2", "voice_settings": vs},
                     accept="audio/mpeg")
        Path(out).write_bytes(audio); print("wrote", out, len(audio), "bytes")
    elif cmd == "music":
        music(sys.argv[2], sys.argv[3], sys.argv[4])

def music(prompt, seconds, out):
    audio = call("/v1/music?output_format=mp3_44100_128", {"prompt": prompt, "music_length_ms": int(float(seconds) * 1000)}, accept="audio/mpeg")
    Path(out).write_bytes(audio); print("wrote", out, len(audio), "bytes")

if __name__ == "__main__":
    main()
