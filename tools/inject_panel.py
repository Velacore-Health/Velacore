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
    if name in ("learn.html", "faq.html"):
        band = bp.goal_band("")
        if "<!-- goalband:start -->" in s:
            s = re.sub(r"<!-- goalband:start -->.*?<!-- goalband:end -->", lambda m: band, s, count=1, flags=re.S)
        else:
            j = s.index("    <!-- Please note -->")
            s = s[:j] + band + "\n\n" + s[j:]
    f.write_text(s, encoding="utf-8")
    print("panel on", name)
