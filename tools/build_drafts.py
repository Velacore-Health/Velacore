"""Builds draft program pages that are not live, Nov 18 2026.

Run from the repo root:  python -I tools/build_drafts.py

Sexual health and women's HRT were approved by Dourado on Nov 18 2026, limited to the items OpenLoop names in writing.
Their copy is in tools/draft_programs.py. The pages use the same template as the live program pages, but they are
written to drafts/programs, outside public/, so no push can publish them. Each one carries a draft banner, a noindex
tag, the safety information placeholder and the open items that must be answered before launch.

To preview: python -I tools/build_drafts.py --preview DIR copies public/ into DIR and adds the drafts to DIR/programs.
"""
import html
import importlib.util
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "drafts" / "programs"


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


bp = load("build_programs")
DRAFTS = load("draft_programs").DRAFTS

# The line swaps that keep unconfirmed facts off these pages live in tools/draft_programs.py, applied by bp.render.

STYLE = """  <style>
    .draft-bar{background:#FFF4D6;color:#5A4300;text-align:center;font-weight:600;padding:10px 16px;font-size:.95rem}
    .draft-open ul{margin:12px 0 0;padding-left:20px}
    .draft-open li{margin:6px 0}
  </style>
"""


def draft_page(p):
    s = bp.render(p)
    # vc-reviewer Nov 18 2026: no analytics on these drafts; whether any tag may fire at launch is the attorney's call.
    assert s.count(bp.GA) == 1
    s = s.replace(bp.GA + "\n", "", 1)
    s = s.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0" />',
                  '<meta name="viewport" content="width=device-width, initial-scale=1.0" />\n  <meta name="robots" content="noindex, nofollow" />', 1)
    s = s.replace("</head>", STYLE + "</head>", 1)
    s = s.replace(f'<body class="prog-{p["slug"]}">',
                  f'<body class="prog-{p["slug"]}">\n  <div class="draft-bar" role="note">Draft, not live. Waiting on OpenLoop for the open items below.</div>', 1)
    items = "".join(f"<li>{html.escape(x)}</li>" for x in p["open_items"])
    extra = f'''    <section class="section blk draft-open">
      <div class="container">
        <div class="blk-card blk-card-mint">
          <h2>Open before launch</h2>
          <p>This block is for the draft only and is removed before the page goes live.</p>
          <ul>{items}</ul>
        </div>
      </div>
    </section>

    <section class="please-note">'''
    assert s.count('    <section class="please-note">') == 1
    s = s.replace('    <section class="please-note">', extra, 1)
    return s


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for p in DRAFTS:
        assert len(p["title"]) + len(" | Velacore Health") <= 60, (p["slug"], "title over 60")
        assert len(p["meta"]) <= 155, (p["slug"], "meta over 155")
        (OUT / f"{p['slug']}.html").write_text(draft_page(p), encoding="utf-8")
        print("wrote", f"drafts/programs/{p['slug']}.html")
    if "--preview" in sys.argv:
        dst = Path(sys.argv[sys.argv.index("--preview") + 1])
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(ROOT / "public", dst)
        for p in DRAFTS:
            shutil.copy(OUT / f"{p['slug']}.html", dst / "programs" / f"{p['slug']}.html")
        print("preview in", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
