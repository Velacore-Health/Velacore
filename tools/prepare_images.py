"""Converts images dropped in assets-in/ into the site's format.

Run from the repo root:  python -I tools/prepare_images.py

assets-in/products/  -> public/images/products/<name>.webp   the five program vials
assets-in/lifestyle/ -> public/images/lifestyle/<name>.webp  people and scenes
Each PNG or JPG is resized to 1600 px on the long side and saved as WebP at quality 88.
Prompts and file names are in docs/gemini-prompts.md. Uses ffmpeg. Nothing else is touched.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = {
    "products": {"tirzepatide", "semaglutide", "microdosing", "nad", "glutathione", "sermorelin"},
    "lifestyle": {"hero", "hero-group", "goal-weight", "goal-vitality", "goal-hormone", "step-visit", "step-clinician", "step-delivery", "wellness"},
}


def main():
    total = 0
    for folder, expected in FOLDERS.items():
        total += convert(ROOT / "assets-in" / folder, ROOT / "public" / "images" / folder, expected)
    if not total:
        print("No images in assets-in/products or assets-in/lifestyle. Names are in docs/gemini-prompts.md.")
    else:
        print("Now run: python -I tools/build_programs.py")
    return 0


def convert(IN, OUT, EXPECTED):
    IN.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in IN.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"})
    for src in files:
        name = src.stem.lower().replace(" ", "-")
        dst = OUT / f"{name}.webp"
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
               "-vf", "scale='if(gt(iw,ih),1600,-2)':'if(gt(iw,ih),-2,1600)'",
               "-c:v", "libwebp", "-quality", "88", str(dst)]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode:
            print(f"FAILED {src.name}: {r.stderr.strip()[:200]}")
            continue
        note = "" if name in EXPECTED else "  NOTE: not one of the expected names, so no page uses it yet"
        print(f"wrote {dst.relative_to(ROOT).as_posix()} from {src.name}{note}")
    return len(files)


if __name__ == "__main__":
    sys.exit(main())
