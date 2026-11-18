"""Makes the photos for the Learn page cards, Nov 18 2026.

Run from the repo root:  python -I tools/make_learn_cards.py

Dourado asked for the Learn page to lean into the Hims look: photos instead of line icons. Each card photo is cut to
3 by 2 from the full-size original in assets-in and saved at 480 and 960 wide, the sizes the cards show at, then
sharpened once. FOCUS moves the crop left or right, 0 is the left edge and 1 the right. Uses ffmpeg.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public" / "images" / "learn" / "cards"
# card name: (original, horizontal focus)
CARDS = {
    "safe": ("lifestyle/clinicians-review.jpg", 0.55),
    "stop": ("lifestyle/clinicians-video.jpg", 0.5),
    "right-for-me": ("lifestyle/step-visit.jpg", 0.5),
    "taken": ("lifestyle/step-delivery.jpg", 0.5),
    "made": ("lifestyle/pharmacy-lab.jpg", 0.5),
    "difference": ("lifestyle/about-hero.jpg", 0.5),
    "article-503a": ("lifestyle/goal-vitality.jpg", 0.35),
    "article-sema-tirz": ("products/learn-sema-tirz.jpg", 0.5),
    "article-microdosing": ("products/learn-microdosing.jpg", 0.5),
    "article-glp1-online": ("lifestyle/learn-glp1-online.jpg", 0.5),
}
WIDTHS = (480, 960)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (rel, focus) in CARDS.items():
        src = ROOT / "assets-in" / rel
        if not src.exists():
            print(f"MISSING {src.relative_to(ROOT).as_posix()}")
            continue
        # widest 3 by 2 window that fits, slid to the focus point
        crop = (f"crop='min(iw,ih*3/2)':'min(ih,iw*2/3)':"
                f"'(iw-min(iw,ih*3/2))*{focus}':'(ih-min(ih,iw*2/3))/2'")
        for w in WIDTHS:
            amount = 0.7 if w == 480 else 0.5
            dst = OUT / f"{name}-{w}.webp"
            r = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                                "-vf", f"{crop},scale={w}:{w * 2 // 3}:flags=lanczos,unsharp=3:3:{amount}:3:3:0",
                                "-c:v", "libwebp", "-quality", "90", str(dst)], capture_output=True, text=True)
            print(("FAILED " if r.returncode else "wrote ") + dst.relative_to(ROOT).as_posix())
    return 0


if __name__ == "__main__":
    sys.exit(main())
