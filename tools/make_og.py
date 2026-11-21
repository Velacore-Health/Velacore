"""The share picture, public/images/og.jpg, 1200 by 630. Run from the repo root: python -I tools/make_og.py

Nov 20 2026, Dourado's OK: the old one was the dark Nov 6 design. This one is the studio look: the six-vial group
photo, whole and uncropped at the sides, under the header lockup, the home page headline and the site's top bar line,
with the illustration note along the bottom.
The headline and the line are read from public/index.html so no words are typed twice. Needs Playwright with Chromium.
"""
import base64, html, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
PHOTO = ROOT / "assets-in" / "lifestyle" / "hero-group.jpg"   # 2400 by 1792, the six vials in the studio look
OUT = PUB / "images" / "og.jpg"


def page_words():
    s = (PUB / "index.html").read_text(encoding="utf-8")
    h1 = re.search(r"<h1[^>]*>([^<]+)</h1>", s).group(1).strip()
    bar = re.search(r"<span>(A telehealth platform\.[^<]+)</span>", s)   # the pine bar at the top of every page
    assert bar, "top bar line not found"
    return html.unescape(h1), html.unescape(bar.group(1).strip())


def illustration_note():
    """docs/BRAND.md section 6: a picture of labeled vials seen away from the page carries the illustration note on the
    frame. The words are the first sentence of PRODUCT_NOTE in tools/build_programs.py, read from the source."""
    src = (ROOT / "tools" / "build_programs.py").read_text(encoding="utf-8")
    full = re.search(r'^PRODUCT_NOTE = "([^"]+)"', src, re.M).group(1)
    return full.split(". ")[0] + "."


def data_uri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode()


def main():
    from playwright.sync_api import sync_playwright
    h1, bar = page_words()
    note = illustration_note()
    mark = data_uri(PUB / "logo-mark.svg", "image/svg+xml")
    photo = data_uri(PHOTO, "image/jpeg")
    doc = f"""<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600&family=Plus+Jakarta+Sans:wght@600;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;overflow:hidden;position:relative;background:#EEF5F1;color:#15302A;font-family:'Hanken Grotesk',sans-serif}}
.photo{{position:absolute;left:0;top:-64px;width:1200px;height:896px}}
.top{{position:absolute;left:64px;right:64px;top:26px;display:flex;align-items:center;justify-content:space-between}}
.brand{{display:flex;align-items:center;gap:13px;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:30px;letter-spacing:-.02em}}
.brand img{{height:46px;width:auto;display:block}}
.brand b{{font-weight:700;white-space:nowrap}}
.brand span{{color:#0A7A61}}
.url{{font-weight:600;font-size:23px;color:#0A7A61}}
h1{{position:absolute;left:64px;right:64px;top:86px;font-family:'Plus Jakarta Sans',sans-serif;font-weight:600;font-size:54px;line-height:1.1;letter-spacing:-.025em}}
p{{position:absolute;left:64px;right:64px;top:152px;font-size:23px;line-height:1.3;color:#4C625B}}
.note{{position:absolute;left:0;right:0;bottom:11px;text-align:center;font-size:16px;line-height:1.2;color:#4C625B}}
</style></head><body>
<img class="photo" src="{photo}" alt="">
<div class="top"><div class="brand"><img src="{mark}" alt=""><b>Velacore <span>Health</span></b></div><div class="url">velacorehealth.com</div></div>
<h1>{html.escape(h1)}</h1>
<p>{html.escape(bar)}</p>
<div class="note">{html.escape(note)}</div>
</body></html>"""
    tmp = OUT.with_suffix(".tmp.png")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        pg.set_content(doc, wait_until="networkidle")
        pg.evaluate("document.fonts.ready")
        fits = pg.evaluate("""() => { const h=document.querySelector('h1'), p=document.querySelector('p');
            return {h1Lines: Math.round(h.getBoundingClientRect().height / (54*1.1)), pLines: Math.round(p.getBoundingClientRect().height / (23*1.3)),
                    fonts: [...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family).filter((v,i,a)=>a.indexOf(v)===i)} }""")
        assert fits["h1Lines"] == 1 and fits["pLines"] == 1, fits
        assert any("Jakarta" in f for f in fits["fonts"]) and any("Hanken" in f for f in fits["fonts"]), fits
        pg.screenshot(path=str(tmp))
        b.close()
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(tmp), "-q:v", "3", "-pix_fmt", "yuvj444p", str(OUT)], check=True)
    tmp.unlink()
    print("wrote", OUT.relative_to(ROOT), OUT.stat().st_size // 1024, "KB;", h1, "|", bar, "|", note)


if __name__ == "__main__":
    sys.exit(main())
