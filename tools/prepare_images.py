"""Converts product images dropped in assets-in/products/ into the site's format.

Run from the repo root:  python -I tools/prepare_images.py

For each PNG or JPG in assets-in/products/: resize to 1600 px on the long side,
convert to WebP at quality 88, save as public/images/products/<name>.webp.
Uses ffmpeg, which is installed on this machine. Nothing else is touched.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IN = ROOT / "assets-in" / "products"
OUT = ROOT / "public" / "images" / "products"
EXPECTED = {"tirzepatide", "semaglutide", "microdosing", "nad", "sermorelin"}


def main():
    IN.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(p for p in IN.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"})
    if not files:
        print(f"No images in {IN}. Drop PNGs there, named per docs/image-brief.md.")
        return 0
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
        note = "" if name in EXPECTED else "  (name is not one of the five programs; the site will not use it unless a page references it)"
        print(f"wrote {dst.relative_to(ROOT).as_posix()} from {src.name}{note}")
    print("Now run: python -I tools/build_programs.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
