"""Converts images dropped in assets-in/ into the site's format.

Run from the repo root:  python -I tools/prepare_images.py semaglutide-oral
Name the files to convert, without the extension. Nov 18 2026: run with no names it reconverts every image, and the
results differ from the files that are live, so always name the ones that changed.

assets-in/products/  -> public/images/products/<name>.webp   the five program vials
assets-in/lifestyle/ -> public/images/lifestyle/<name>.webp  people and scenes
Each PNG or JPG is resized to 1600 px on the long side and saved as WebP at quality 88. Product photos are
1200 wide, sharpened, saved at quality 92, and get an 800 wide copy for cards on phones.
Prompts and file names are in docs/gemini-prompts.md. Uses ffmpeg. Nothing else is touched.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = {
    "products": {"tirzepatide", "semaglutide", "microdosing", "nad", "glutathione", "sermorelin", "nad-nasal", "nad-oral", "microdosing-oral", "semaglutide-oral", "learn-sema-tirz", "learn-microdosing"},  # form variants: <program>-<form>
    "lifestyle": {"hero", "hero-group", "goal-weight", "goal-vitality", "goal-hormone", "step-visit", "step-clinician", "step-delivery", "step-support", "clinician-call", "wellness", "clinicians-hero", "clinicians-video", "clinicians-credential", "clinicians-review", "pharmacy-lab", "about-hero", "support-phone", "learn-glp1-online"},
}

# Nov 18 2026, Dourado found the needle-free tiles soft. The tiles used to zoom the full photo in the browser and then
# shrink it to about 250 px, and that double resize blurred them. Now the zoom is cut into the file here: the same
# frame the browser showed, 86.2 percent of the photo, made at the sizes the tile shows at, then sharpened once.
FORM_TILES = {"semaglutide", "semaglutide-oral", "nad", "nad-nasal", "nad-oral", "microdosing-oral"}
TILE_WIDTHS = (300, 450, 600, 900)
TILE_CROP = "crop=trunc(iw*0.862/2)*2:trunc(ih*0.862/2)*2:trunc(iw*0.069):trunc(ih*0.099)"


def make_tiles(src, out, name):
    out.mkdir(parents=True, exist_ok=True)
    for w in TILE_WIDTHS:
        amount = 0.8 if w <= 450 else 0.6
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                        "-vf", f"{TILE_CROP},scale={w}:{w * 4 // 3}:flags=lanczos,unsharp=3:3:{amount}:3:3:0",
                        "-c:v", "libwebp", "-quality", "92", str(out / f"{name}-{w}.webp")], capture_output=True, text=True)


def main():
    total = 0
    for folder, expected in FOLDERS.items():
        total += convert(ROOT / "assets-in" / folder, ROOT / "public" / "images" / folder, expected)
    if not total:
        print("No images in assets-in/products or assets-in/lifestyle. Names are in docs/gemini-prompts.md.")
    else:
        print("Now run: python -I tools/build_programs.py")
    return 0


ONLY = {a.lower() for a in sys.argv[1:]}


def convert(IN, OUT, EXPECTED):
    IN.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    # Nov 18 2026: files starting with an underscore are kept versions, never converted.
    files = sorted(p for p in IN.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"} and not p.name.startswith("_")
                   and (not ONLY or p.stem.lower() in ONLY))
    for src in files:
        name = src.stem.lower().replace(" ", "-")
        dst = OUT / f"{name}.webp"
        if OUT.name == "products" and name in FORM_TILES:
            make_tiles(src, OUT / "tiles", name)
        if OUT.name == "products":
            # Nov 17 2026: product photos are sharpened after a Lanczos resize, and get an 800 copy for cards on phones.
            cmd = ["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                   "-vf", "scale=1200:-2:flags=lanczos,unsharp=5:5:0.5:5:5:0",  # 1200 wide, the size of the live product photos
                   "-c:v", "libwebp", "-quality", "92", str(dst)]
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf", "scale=800:-2:flags=lanczos,unsharp=5:5:0.6:5:5:0",
                            "-c:v", "libwebp", "-quality", "92", str(OUT / f"{name}-800.webp")], capture_output=True, text=True)
        else:
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
