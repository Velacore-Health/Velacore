"""Draws the explainer's text overlays in the brand fonts: one clear PNG per subtitle, and the closing scene.

Run from the repo root:  python -I tools/video/peptides/render_overlays.py [end]
Reads 03-edits/peptides-video/subs/list.json, written by build_cut.py. Writes subs/sNN.png there.
With the word "end" it also writes end-scene.mp4, the closing scene with the six programs and the button.
The fonts load from Google Fonts, the same ones the site uses, so nothing is installed on this machine.
"""
import json, subprocess, sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).parent
WORK = ROOT / "03-edits" / "peptides-video"
FPS, END_LEN = 30, 7.0

subs = json.loads((WORK / "subs" / "list.json").read_text(encoding="utf-8"))
with sync_playwright() as p:
    br = p.chromium.launch()
    pg = br.new_page(viewport={"width": 1280, "height": 720})
    pg.goto((HERE / "overlay.html").as_uri(), wait_until="networkidle")
    pg.evaluate("window.ready")
    for i, s in enumerate(subs):
        pg.evaluate("s => setSub(s)", s["text"])
        pg.screenshot(path=str(WORK / "subs" / f"s{i:02d}.png"), omit_background=True)
    print("subtitles drawn:", len(subs))
    if "end" in sys.argv[1:]:
        enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-i", "-",
                                "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", str(WORK / "end-scene.mp4")],
                               stdin=subprocess.PIPE)
        for f in range(int(END_LEN * FPS)):
            pg.evaluate(f"renderEnd({f / FPS})")
            enc.stdin.write(pg.screenshot(type="png"))
        enc.stdin.close(); enc.wait()
        print("closing scene drawn:", END_LEN, "s")
    br.close()
