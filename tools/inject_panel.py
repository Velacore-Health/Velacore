"""Puts the slide-in menu on the hand-written pages. Generated pages get it from their builders.
Run from the repo root after any change to side_panel in build_programs.py:  python -I tools/inject_panel.py
"""
import importlib.util, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("bp", ROOT / "tools" / "build_programs.py")
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)
PAGES = ["index.html", "learn.html", "faq.html", "terms.html", "privacy.html", "telehealth-consent.html", "refund-policy.html"]
TOGGLE = re.compile(r'<button class="nav-toggle" id="navToggle"[^>]*>\s*(?:<span></span>\s*)+</button>')
for name in PAGES:
    f = ROOT / "public" / name; s = f.read_text(encoding="utf-8")
    s = TOGGLE.sub(bp.MENU_BUTTON, s, count=1)
    panel = bp.side_panel("")
    if "<!-- panel:start -->" in s:
        s = re.sub(r"<!-- panel:start -->.*?<!-- panel:end -->", lambda m: panel, s, count=1, flags=re.S)
    else:
        j = s.index("  </header>") + len("  </header>")
        s = s[:j] + "\n  " + panel + s[j:]
    if name == "index.html":
        # The home program cards are hand-written, but their prices come from the program data, Nov 19 2026.
        slugs = {p["slug"]: p for p in bp.PROGRAMS if any(x["id"] == "monthly" for x in p["plans"])}
        def card(m):
            block = m.group(0)
            st = re.search(r'data-start="([a-z-]+)"', block)
            if not st or st.group(1) not in slugs:
                return block
            new, n = re.subn(r'<span class="tcard-price">.*?</small></span>', lambda _: bp.tcard_price(slugs[st.group(1)]), block, count=1, flags=re.S)
            assert n == 1, st.group(1)
            return new
        s, cards = re.subn(r'<article class="tcard".*?</article>', card, s, flags=re.S)
        print("home cards checked:", cards)
        # The Tired of needles tiles carry a short first month price line too; same slash, same source.
        def tile(m):
            li = m.group(0)
            h = re.search(r'href="programs/([a-z-]+)\.html', li)
            # An oral tile is priced by its form, not by the program it links to, so it is never rewritten here.
            if not h or h.group(1) not in slugs or "data-oral" in li[:40]:
                return li
            first, then = bp.first_and_then(slugs[h.group(1)])
            return re.sub(r'(?:<s class="was">.*?</s> )?\$\d+ first month(?:, then \$\d+/mo)?\.',
                          lambda _: f"{bp.was(then)}{first} first month, then {then}/mo.", li, count=1)
        s, tiles = re.subn(r'<li[^>]*><a href="programs/[^"]+"><img [^>]*>.*?</li>', tile, s, flags=re.S)
        print("needle-free tiles checked:", tiles)
    if name in ("learn.html", "faq.html"):
        band = bp.goal_band("")
        if "<!-- goalband:start -->" in s:
            s = re.sub(r"<!-- goalband:start -->.*?<!-- goalband:end -->", lambda m: band, s, count=1, flags=re.S)
        else:
            j = s.index("    <!-- Please note -->")
            s = s[:j] + band + "\n\n" + s[j:]
    f.write_text(s, encoding="utf-8")
    print("panel on", name)
