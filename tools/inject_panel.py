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
            # Nov 20 2026: the 12-week line under the price comes from the same data; any words after it stay as written.
            new, n = re.subn(r"12-week plan \$\d+(?:/mo| per 4 weeks), \$\d+ up front\.(?: Save \$\d+ over 12 weeks\.)?(?: Oral form \$\d+(?:/mo| every 4 weeks)\.)?", lambda _: bp.week12_line(slugs[st.group(1)]), new, count=1)
            assert n == 1, (st.group(1), "12-week line")
            return new
        s, cards = re.subn(r'<article class="tcard".*?</article>', card, s, flags=re.S)
        print("home cards checked:", cards)
        # The Tired of needles tiles carry a short monthly price line too, from the same source.
        def tile(m):
            li = m.group(0)
            h = re.search(r'href="programs/([a-z-]+)\.html', li)
            if not h or h.group(1) not in slugs:
                return li
            # An oral tile is priced by its form, not by the program it links to: its whole line is the program's Oral form line.
            if "data-oral" in li[:40]:
                line = next(f[2] for f in slugs[h.group(1)]["forms"] if f[0] == "Oral")
                new, n = re.subn(r"(<b>[^<]+</b><p>)[^<]*(</p>)", lambda m: m.group(1) + line + m.group(2), li, count=1)
                assert n == 1, "oral tile line"
                return new
            then = bp.monthly_price(slugs[h.group(1)])
            return re.sub(r'(?:<s class="was">.*?</s> )?\$\d+ (?:first month(?:, then \$\d+/mo)?|a month|every 4 weeks)\.',
                          lambda _: f"{then} {bp.PERIOD}.", li, count=1)
        s, tiles = re.subn(r'<li[^>]*><a href="programs/[^"]+"><img [^>]*>.*?</li>', tile, s, flags=re.S)
        print("needle-free tiles checked:", tiles)
        # The hero price line, Nov 20 2026: it sits in the weight band, so it is the lowest month to month price among the
        # weight programs only, per vc-reviewer, from the same source.
        low = min(int(bp.monthly_price(q).lstrip("$")) for q in slugs.values() if q["cat"].startswith("Weight"))
        s, n = re.subn(r'<p class="hero-price">.*?</p>', f'<p class="hero-price">From ${low} {bp.PERIOD}. Shipping included.</p>', s, count=1, flags=re.S)
        assert n == 1, "hero price line"
    if name in ("learn.html", "faq.html"):
        band = bp.goal_band("")
        if "<!-- goalband:start -->" in s:
            s = re.sub(r"<!-- goalband:start -->.*?<!-- goalband:end -->", lambda m: band, s, count=1, flags=re.S)
        else:
            j = s.index("    <!-- Please note -->")
            s = s[:j] + band + "\n\n" + s[j:]
    f.write_text(s, encoding="utf-8")
    print("panel on", name)
