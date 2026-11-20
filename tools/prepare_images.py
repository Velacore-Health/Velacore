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
# Nov 20 2026: two studio shots sit differently in their frames. The Microdosing dropper stands lower, so its cut moves
# down to line its base up with the others; the nasal spray is taller, so its cut is looser and higher to keep the tip;
# the NAD+ dropper gets the same looser cut so its bulb has room above it.
TILE_CROP_FOR = {
    "microdosing-oral": "crop=trunc(iw*0.85/2)*2:trunc(ih*0.85/2)*2:trunc(iw*0.075):trunc(ih*0.15)",
    "nad-nasal": "crop=trunc(iw*0.90/2)*2:trunc(ih*0.90/2)*2:trunc(iw*0.05):trunc(ih*0.04)",
    "nad-oral": "crop=trunc(iw*0.90/2)*2:trunc(ih*0.90/2)*2:trunc(iw*0.05):trunc(ih*0.05)",
}


def make_tiles(src, out, name):
    out.mkdir(parents=True, exist_ok=True)
    for w in TILE_WIDTHS:
        amount = 0.8 if w <= 450 else 0.6
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                        "-vf", f"{TILE_CROP_FOR.get(name, TILE_CROP)},scale={w}:{w * 4 // 3}:flags=lanczos,unsharp=3:3:{amount}:3:3:0",
                        "-c:v", "libwebp", "-quality", "92", str(out / f"{name}-{w}.webp")], capture_output=True, text=True)


# Nov 20 2026, Dourado: the whole site uses the studio look. These product photos come from the studio shots.
STUDIO_PRODUCTS = {"tirzepatide", "semaglutide", "microdosing", "nad", "glutathione", "sermorelin",
                   "nad-nasal", "nad-oral", "microdosing-oral", "semaglutide-oral"}


def studio_or(src, name):
    """Nov 20 2026, Dourado: the needle-free and form tiles use the studio shots, no marble, when one exists in
    assets-in/products/studio/<name>.jpg; otherwise the photo dropped in assets-in/products."""
    studio = ROOT / "assets-in" / "products" / "studio" / f"{name}.jpg"
    if studio.exists():
        return studio
    print(f"WARNING no studio shot for {name}: using {src.name}, the marble photo. Restore assets-in/products/studio from the backup.")
    return src


def tiles_only():
    """python -I tools/prepare_images.py --tiles  remakes only the form tiles, leaving the main product photos alone."""
    for name in sorted(FORM_TILES):
        src = studio_or(ROOT / "assets-in" / "products" / f"{name}.jpg", name)
        if not src.exists():
            print(f"MISSING {name}")
            continue
        make_tiles(src, ROOT / "public" / "images" / "products" / "tiles", name)
        print(f"wrote tiles/{name}-*.webp from {src.relative_to(ROOT).as_posix()}")
    return 0


def home_weight_card():
    """python -I tools/prepare_images.py --home  remakes the Tirzepatide and Sermorelin cuts on the two big home cards from the studio
    shot. tirzepatide-480 is the whole photo for phones. tirzepatide-wide is a 4 by 3 cut for 701 to 1299 px with the vial
    a little right of center, since the card text sits on the left: the plain left margin of the photo is mirrored to
    widen it, so no vial is ever cut or faded."""
    src = studio_or(ROOT / "assets-in" / "products" / "tirzepatide.jpg", "tirzepatide")
    out = ROOT / "public" / "images" / "products"
    run = lambda vf, dst: subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf", vf, "-c:v", "libwebp",
                                          "-quality", "92", str(out / dst)], capture_output=True, text=True)
    run("scale=480:642:flags=lanczos,unsharp=5:5:0.6:5:5:0", "tirzepatide-480.webp")
    # In the 1792 by 2400 studio shot the vial is centered; cut the full width from y 250 to 2050, then mirror 544 px of
    # plain margin on the left and 64 on the right, so the frame is 2400 by 1800 with the vial at 60 percent across.
    wide = ("crop=1792:1800:0:250,split=3[a][b][c];[b]crop=544:1800:0:0,hflip[l];[c]crop=64:1800:1728:0,hflip[r];"
            "[l][a][r]hstack=inputs=3,scale={w}:{h}:flags=lanczos,unsharp=5:5:0.5:5:5:0")
    run(wide.format(w=1200, h=900), "tirzepatide-wide.webp")
    run(wide.format(w=800, h=600), "tirzepatide-wide-800.webp")
    print("wrote tirzepatide-480, tirzepatide-wide and tirzepatide-wide-800 from " + src.relative_to(ROOT).as_posix())
    # Nov 20 2026, Dourado: on phones and tablets the Sermorelin vial on the home Hormone card read smaller than the
    # Tirzepatide vial beside it. The same two cuts from the Sermorelin studio shot make both vials the same size.
    ssrc = studio_or(ROOT / "assets-in" / "products" / "sermorelin.jpg", "sermorelin")
    srun = lambda vf, dst: subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(ssrc), "-vf", vf, "-c:v", "libwebp",
                                           "-quality", "92", str(out / dst)], capture_output=True, text=True)
    srun("scale=480:642:flags=lanczos,unsharp=5:5:0.6:5:5:0", "sermorelin-480.webp")
    srun(wide.format(w=1200, h=900), "sermorelin-wide.webp")
    srun(wide.format(w=800, h=600), "sermorelin-wide-800.webp")
    print("wrote sermorelin-480, sermorelin-wide and sermorelin-wide-800 from " + ssrc.relative_to(ROOT).as_posix())
    return 0


GOAL_SIZES = ((480, 360), (800, 600), (1200, 900))
# Nov 20 2026, Dourado: between 421 and 580 px the goal tiles are two columns about as tall as wide, and the 4 by 3 photo
# floated small in them. These square cuts, x, y and side in the 2400 by 1792 source, center the products so they fill the column.
GOAL_SQUARE = {"goal-weight": (412, 158, 1600), "goal-vitality": (304, 0, 1792), "goal-hormone": (304, 0, 1792)}


def goal_sizes(names):
    """python -I tools/prepare_images.py --goals goal-hormone  makes the 480, 800 and 1200 px copies of a home goal photo
    from assets-in/lifestyle/<name>.jpg, plus the 1600 px master. Nov 20 2026, studio look."""
    out = ROOT / "public" / "images" / "lifestyle"
    for name in names:
        src = ROOT / "assets-in" / "lifestyle" / f"{name}.jpg"
        if not src.exists():
            print(f"MISSING {src.relative_to(ROOT).as_posix()}")
            continue
        for w, h in GOAL_SIZES:
            amount = 0.7 if w <= 480 else 0.5
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf",
                            f"scale={w}:{h}:flags=lanczos,unsharp=5:5:{amount}:5:5:0", "-c:v", "libwebp", "-quality", "90",
                            str(out / f"{name}-{w}.webp")], capture_output=True, text=True)
        if name in GOAL_SQUARE:
            x, y, side = GOAL_SQUARE[name]
            for w in (480, 800):
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf",
                                f"crop={side}:{side}:{x}:{y},scale={w}:{w}:flags=lanczos,unsharp=5:5:0.6:5:5:0", "-c:v", "libwebp",
                                "-quality", "90", str(out / f"{name}-sq-{w}.webp")], capture_output=True, text=True)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src), "-vf", "scale=1600:-2", "-c:v", "libwebp",
                        "-quality", "88", str(out / f"{name}.webp")], capture_output=True, text=True)
        print(f"wrote {name}-480, -800, -1200 and the 1600 master")
    return 0


def main():
    if "--goals" in sys.argv[1:]:
        return goal_sizes(sorted(ONLY))
    if "--tiles" in sys.argv[1:]:
        return tiles_only()
    if "--home" in sys.argv[1:]:
        return home_weight_card()
    total = 0
    for folder, expected in FOLDERS.items():
        total += convert(ROOT / "assets-in" / folder, ROOT / "public" / "images" / folder, expected)
    if not total:
        print("No images in assets-in/products or assets-in/lifestyle. Names are in docs/gemini-prompts.md.")
    else:
        print("Now run: python -I tools/build_programs.py")
    return 0


ONLY = {a.lower() for a in sys.argv[1:] if not a.startswith("--")}


def convert(IN, OUT, EXPECTED):
    IN.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    # Nov 18 2026: files starting with an underscore are kept versions, never converted.
    files = sorted(p for p in IN.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"} and not p.name.startswith("_")
                   and (not ONLY or p.stem.lower() in ONLY))
    for src in files:
        name = src.stem.lower().replace(" ", "-")
        dst = OUT / f"{name}.webp"
        if OUT.name == "products" and name in STUDIO_PRODUCTS:
            src = studio_or(src, name)
        if OUT.name == "products" and name in FORM_TILES:
            make_tiles(src if name in STUDIO_PRODUCTS else studio_or(src, name), OUT / "tiles", name)
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
