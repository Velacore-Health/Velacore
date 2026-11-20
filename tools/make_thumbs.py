"""Makes the small square product pictures used in the menus, the side panel, the home tiles and the goal rows.

Run from the repo root:  python -I tools/make_thumbs.py

Nov 18 2026, Dourado: every label in the small pictures must be legible and visible. A whole bottle shrunk to about
56 px leaves the product name unreadable and often cut off, so each thumbnail is now a square cut around the label,
from the logo band down to the line under the product name, ending above the fine print so no half-cut text shows, taken from the full-size original in assets-in/products, saved at 432 px
and sharpened once. Nov 19 2026: raised from 216 px, because the phone menu shows them up to 106 CSS px, about 318 device px. The boxes below are measured on each original, in its own pixels: left, top, side.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "images" / "products" / "thumbs"
# Vials share one layout; the bottles each have their own.
VIAL = (580, 905, 640)
BOXES = {
    "tirzepatide": VIAL, "semaglutide": VIAL, "microdosing": VIAL,
    "nad": VIAL, "glutathione": VIAL, "sermorelin": VIAL,
    "nad-nasal": (668, 1255, 480),
    "nad-oral": (648, 1165, 520),
    "microdosing-oral": (648, 1165, 520),
    "semaglutide-oral": (637, 846, 528),  # Nov 18 2026: one standing bottle, the two-bottle photo retired
}
# Not a product: the Not sure tile on the home page shows the glass clipboard, which has no label to read.
OTHER = {"not-sure": ("lifestyle/learn-evaluation.jpg", (330, 150, 1300))}
SIZE = 432


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [(n, ROOT / "assets-in" / "products" / f"{n}.jpg", box) for n, box in BOXES.items()]
    jobs += [(n, ROOT / "assets-in" / rel, box) for n, (rel, box) in OTHER.items()]
    for name, src, (x, y, side) in jobs:
        if not src.exists():
            print(f"MISSING {src.relative_to(ROOT).as_posix()}")
            continue
        dst = OUT / f"{name}.webp"
        r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                            "-vf", f"crop={side}:{side}:{x}:{y},scale={SIZE}:{SIZE}:flags=lanczos,unsharp=3:3:0.7:3:3:0",
                            "-c:v", "libwebp", "-quality", "92", str(dst)], capture_output=True, text=True)
        print(("FAILED " if r.returncode else "wrote ") + dst.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
