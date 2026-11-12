"""Renders the Velacore product label as flat artwork, one PNG per program.

Run from the repo root:  python -I brand/label/make_labels.py
Output: brand/label/label-<slug>.png, 1200 x 1600 px.
The label follows docs/BRAND.md section 6: the designer's logo, version 03, shown in pine,
then the program name, then the four required lines, with the program's cap color as a thin
stripe. Nothing else. These files are attached to the Gemini vial prompts so the label text
comes out exact.
"""
import base64
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "brand" / "label"
LOGO_FILE = ROOT / "brand" / "logo" / "VelaCore Health_03" / "VelaCore Health-01.png"
LOGO = "data:image/png;base64," + base64.b64encode(LOGO_FILE.read_bytes()).decode()

PINE = "#15302A"
PROGRAMS = [
    ("tirzepatide", "TIRZEPATIDE", "#3E5FC0"),
    ("semaglutide", "SEMAGLUTIDE", "#8A6BC9"),
    ("microdosing", "MICRODOSING GLP-1", "#0C8F72"),
    ("nad", "NAD+", "#8A6BC9"),
    ("sermorelin", "SERMORELIN", "#8A6BC9"),
]

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@600;800&display=swap" rel="stylesheet">
<style>
html,body{{margin:0;background:#fff}}
.label{{width:1200px;height:1600px;box-sizing:border-box;background:#FFFFFF;display:flex;flex-direction:column;
  align-items:center;justify-content:center;padding:0 110px 60px;font-family:'Hanken Grotesk',sans-serif;color:{pine};position:relative}}
canvas.logo{{width:620px;height:auto;display:block}}
.rule{{width:100%;height:4px;background:{color};margin:64px 0 60px}}
.name{{font-weight:800;font-size:150px;letter-spacing:6px;line-height:1;text-align:center;white-space:nowrap}}
.lines{{margin-top:72px;text-align:center;font-weight:600;font-size:44px;letter-spacing:4px;line-height:1.75}}
.rx{{margin-top:36px;font-weight:800;font-size:52px;letter-spacing:4px}}
.stripe{{position:absolute;left:0;right:0;bottom:0;height:60px;background:{color}}}
</style></head><body>
<div class="label">
  <canvas class="logo" width="1507" height="1135"></canvas>
  <div class="rule"></div>
  <div class="name">{name}</div>
  <div class="lines">FOR PRESCRIPTION USE ONLY<br>PRESCRIPTION COMPOUNDED<br>503A COMPOUNDING PHARMACY</div>
  <div class="rx">Rx ONLY</div>
  <div class="stripe"></div>
</div>
<script>
window.ready = new Promise(function (done) {{
  var img = new Image();
  img.onload = function () {{
    // Draw the black-on-white logo, then turn darkness into pine with matching opacity.
    var c = document.querySelector('canvas.logo'), x = c.getContext('2d');
    x.drawImage(img, 0, 0, c.width, c.height);
    var d = x.getImageData(0, 0, c.width, c.height), p = d.data;
    for (var i = 0; i < p.length; i += 4) {{
      // Ink = how dark the pixel is, times how opaque it is; works for white or clear backgrounds.
      var dark = (255 - (p[i] + p[i + 1] + p[i + 2]) / 3) * p[i + 3] / 255;
      p[i] = 0x15; p[i + 1] = 0x30; p[i + 2] = 0x2A; p[i + 3] = dark;
    }}
    x.putImageData(d, 0, 0);
    document.fonts.ready.then(function () {{
      // Shrink the program name until it fits inside the label margins.
      var n = document.querySelector('.name'), size = 150;
      while (n.scrollWidth > 980 && size > 60) {{ size -= 2; n.style.fontSize = size + 'px'; }}
      done(size);
    }});
  }};
  img.src = "{logo}";
}});
</script></body></html>"""


def main():
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 1600})
        for slug, name, color in PROGRAMS:
            pg.set_content(PAGE.format(color=color, pine=PINE, logo=LOGO, name=name), wait_until="networkidle")
            size = pg.evaluate("window.ready")
            out = OUT / f"label-{slug}.png"
            pg.locator(".label").screenshot(path=str(out))
            print("wrote", out.relative_to(ROOT).as_posix(), "name size", size)
        b.close()


if __name__ == "__main__":
    main()
