"""Renders the Velacore product label as flat artwork, one PNG per program.

Run from the repo root:  python -I brand/label/make_labels.py
Output: brand/label/label-<slug>.png, 1200 x 1600 px.
Style A, pine band, chosen by Dourado Nov 11 2026: the designer's logo reversed out in white on a
pine panel, a fine line in the program color, the program name in Fraunces, the three
prescription lines and Rx ONLY in an outlined pill. Follows docs/BRAND.md section 6.
These files are attached to the Gemini vial prompts so the label comes out exact.
"""
import base64
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "brand" / "label"
LOGO_FILE = ROOT / "brand" / "logo" / "VelaCore Health_03" / "VelaCore Health-01.png"
LOGO = "data:image/png;base64," + base64.b64encode(LOGO_FILE.read_bytes()).decode()

PROGRAMS = [
    ("tirzepatide", "Tirzepatide", "#3E5FC0"),
    ("semaglutide", "Semaglutide", "#8A6BC9"),
    ("microdosing", "Microdosing GLP-1", "#0C8F72"),
    ("nad", "NAD+", "#8A6BC9"),
    ("glutathione", "Glutathione", "#8A6BC9"),
    ("sermorelin", "Sermorelin", "#8A6BC9"),
]

PAGE = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,500..600,0..100&family=Hanken+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<style>
html,body{margin:0;background:#fff}
.label{width:1200px;height:1600px;box-sizing:border-box;position:relative;overflow:hidden;background:#fff;
  font-family:'Hanken Grotesk',sans-serif;color:#15302A}
.top{height:700px;background:#15302A;display:flex;align-items:center;justify-content:center}
canvas.logo{display:block;width:560px;height:auto}
.band{height:14px;background:var(--c)}
.body{padding:110px 120px 0;text-align:center;display:flex;flex-direction:column;align-items:center}
.name{font-family:'Fraunces',serif;font-weight:560;font-variation-settings:'opsz' 144,'SOFT' 50;font-size:170px;
  line-height:1;white-space:nowrap;letter-spacing:-1px}
.dash{width:120px;height:6px;background:var(--c);margin:70px 0 64px;border-radius:3px}
.lines{font-weight:600;font-size:34px;letter-spacing:7px;line-height:1.9;text-transform:uppercase}
.rx{margin-top:56px;font-weight:700;font-size:40px;letter-spacing:6px;border:3px solid #15302A;border-radius:60px;padding:16px 46px}
</style></head><body>
<div class="label" style="--c:{c}">
  <div class="top"><canvas class="logo" width="1507" height="1135"></canvas></div>
  <div class="band"></div>
  <div class="body">
    <div class="name">{name}</div>
    <div class="dash"></div>
    <div class="lines">For prescription use only<br>Prescription compounded<br>503A compounding pharmacy</div>
    <div class="rx">Rx ONLY</div>
  </div>
</div>
<script>
window.ready = new Promise(function (done) {
  var img = new Image();
  img.onload = function () {
    // Reverse the black logo out in white; ink = darkness times opacity, so clear or white grounds both work.
    var c = document.querySelector('canvas.logo'), x = c.getContext('2d');
    x.drawImage(img, 0, 0, c.width, c.height);
    var d = x.getImageData(0, 0, c.width, c.height), p = d.data;
    for (var i = 0; i < p.length; i += 4) {
      var dark = (255 - (p[i] + p[i + 1] + p[i + 2]) / 3) * p[i + 3] / 255;
      p[i] = 255; p[i + 1] = 255; p[i + 2] = 255; p[i + 3] = dark;
    }
    x.putImageData(d, 0, 0);
    document.fonts.ready.then(function () {
      // Shrink the program name until it fits inside the side margins.
      var n = document.querySelector('.name'), par = n.parentElement, cs = getComputedStyle(par);
      var max = par.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight) - 20, size = 170;
      while (n.scrollWidth > max && size > 60) { size -= 2; n.style.fontSize = size + 'px'; }
      done(size);
    });
  };
  img.src = "LOGO";
});
</script></body></html>"""


def main():
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 1600})
        for slug, name, color in PROGRAMS:
            pg.set_content(PAGE.replace("{c}", color).replace("{name}", name).replace("LOGO", LOGO),
                           wait_until="networkidle")
            size = pg.evaluate("window.ready")
            out = OUT / f"label-{slug}.png"
            pg.locator(".label").screenshot(path=str(out))
            print("wrote", out.relative_to(ROOT).as_posix(), "name size", size)
        b.close()


if __name__ == "__main__":
    main()
