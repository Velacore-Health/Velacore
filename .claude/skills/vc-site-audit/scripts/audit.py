"""Velacore full site audit. Read-only toward the site; writes only to _audit/<date>/.

Run from the repo root:
    python -I .claude/skills/vc-site-audit/scripts/audit.py            full audit
    python -I .claude/skills/vc-site-audit/scripts/audit.py --no-live  local files only
    python -I .claude/skills/vc-site-audit/scripts/audit.py --no-render skip screenshots

Target model: velacorehealth.com serves the static site in public/, and each treatment's
Start visit button links to that treatment's OpenLoop hosted intake. The Shopify store is a
temporary stopgap, checked only while it is the live site.

Never prints a restricted product name: unapproved items are reported by position only.
"""
import argparse
import csv
import datetime as dt
import html
import importlib.util
import io
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
CFG = json.loads((HERE.parent / "audit-config.json").read_text(encoding="utf-8"))
PUBLIC = ROOT / "public"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) VelacoreSiteAudit/1.0"
STATES = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
          "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
          "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
          "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island",
          "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington",
          "West Virginia", "Wisconsin", "Wyoming"]

sections = {}  # title -> list of (level, msg)
cur = None


def section(title):
    global cur
    cur = title
    sections.setdefault(title, [])


def add(level, msg):
    sections[cur].append((level, msg))


def norm_product(name):
    n = name.lower()
    for p in CFG["approved_products"]:
        if p.rstrip("+") in n:
            return p
    return None


def load_check_module():
    path = ROOT / ".claude/skills/vc-compliance-check/scripts/check.py"
    spec = importlib.util.spec_from_file_location("vc_check", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.geturl(), r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, url, ""
    except Exception as e:  # network down, DNS, TLS
        return None, url, str(e)


def visible_text(page):
    chk = load_check_module()
    return chk.strip_markup(page)


# ---------------------------------------------------------------- compliance
def audit_compliance():
    section("1. Compliance scan of the repo")
    r = subprocess.run([sys.executable, "-I", str(ROOT / ".claude/skills/vc-compliance-check/scripts/check.py")],
                       capture_output=True, text=True, encoding="utf-8", cwd=ROOT)
    for line in r.stdout.splitlines():
        if line.startswith("FAIL:"):
            add("FAIL", line[5:].strip())
        elif line.startswith("Summary:"):
            add("PASS" if r.returncode == 0 else "FAIL", "vc-compliance-check " + line[8:].strip())


# ---------------------------------------------------------------- local site
def parse_cards(page):
    cards = []
    for m in re.finditer(r'<article class="tcard"[^>]*>(.*?)</article>', page, re.S):
        body = m.group(1)
        name = re.search(r"<h3>(.*?)</h3>", body, re.S)
        price = re.search(r'class="tcard-price">(.*?)</span>', body, re.S)
        link = re.search(r'<a href="([^"]*)"[^>]*>\s*(Start[^<]*)</a>', body)
        cards.append({
            "name": html.unescape(re.sub(r"<[^>]+>", "", name.group(1))).strip() if name else "",
            "price": re.sub(r"<[^>]+>", " ", price.group(1)).split() if price else [],
            "href": link.group(1) if link else "",
            "line": page.count("\n", 0, m.start()) + 1,
        })
    return cards


def audit_local():
    section("2. Local static site, public/")
    index = (PUBLIC / "index.html").read_text(encoding="utf-8")
    pages = {p.name: p.read_text(encoding="utf-8") for p in PUBLIC.glob("*.html")}

    # treatment cards: approved names, intake links, prices
    seen = set()
    for i, c in enumerate(parse_cards(index), 1):
        prod = norm_product(c["name"])
        if prod is None:
            if c["href"] and "start" in c["name"].lower() or "not sure" in c["name"].lower():
                continue  # the generic "Not sure where to start" card
            add("FAIL", f"treatment card #{i} at public/index.html:{c['line']} is not one of the five approved treatments")
            continue
        seen.add(prod)
        want = CFG["intake_links"].get(prod, "")
        if want:
            if c["href"] == want:
                add("PASS", f"{c['name']}: Start visit goes to its OpenLoop intake link")
            else:
                add("FAIL", f"{c['name']}: Start visit goes to '{c['href']}', expected its intake link {want}")
        else:
            add("REVIEW", f"{c['name']}: Start visit goes to '{c['href']}'. No OpenLoop intake link set yet in audit-config.json")
    for p in CFG["approved_products"]:
        if p not in seen:
            add("REVIEW", f"no treatment card found for {p}")

    # internal links and anchors
    ids = {n: set(re.findall(r'id="([^"]+)"', t)) for n, t in pages.items()}
    broken = []
    for n, t in pages.items():
        for href in re.findall(r'href="([^"]+)"', t):
            if href.startswith(("http", "mailto:", "tel:", "//")):
                continue
            path, _, frag = href.partition("#")
            target = n if not path else path
            if path and not (PUBLIC / path).exists():
                broken.append(f"{n} -> {href}")
            elif frag and target in ids and frag not in ids[target] and frag != "top":
                broken.append(f"{n} -> {href} (missing anchor)")
            elif href == "#":
                broken.append(f"{n} -> # (placeholder link)")
    add("FAIL" if broken else "PASS", "internal links: " + ("; ".join(sorted(set(broken))) if broken else "all resolve"))

    # sitemap
    sm = (PUBLIC / "sitemap.xml").read_text(encoding="utf-8") if (PUBLIC / "sitemap.xml").exists() else ""
    locs = re.findall(r"<loc>([^<]+)</loc>", sm)
    missing = [u for u in locs if not (PUBLIC / (urllib.parse.urlparse(u).path.strip("/") or "index.html")).exists()]
    add("FAIL" if missing else "PASS", f"sitemap lists {len(locs)} URLs" + (f"; no file for: {', '.join(missing)}" if missing else ", all map to files"))
    for legal in ("privacy.html", "terms.html", "refund-policy.html", "telehealth-consent.html"):
        if legal not in pages:
            add("FAIL", f"legal page missing: {legal}")
        elif f'href="{legal}"' not in index:
            add("FAIL", f"legal page not linked from index.html: {legal}")
    add("PASS", "all four legal pages exist and are linked from the home page") if all(
        l in pages and f'href="{l}"' in index for l in ("privacy.html", "terms.html", "refund-policy.html", "telehealth-consent.html")) else None

    # wording tied to the old platform
    level = "FAIL" if CFG["platform"] == "openloop" else "REVIEW"
    for term in CFG["legacy_model_terms"]:
        hits = {n: t.lower().count(term.lower()) for n, t in pages.items() if term.lower() in t.lower()}
        if hits:
            add(level, f"old-model wording '{term}': " + ", ".join(f"{n} x{c}" for n, c in sorted(hits.items()))
                + (" (rewrite for OpenLoop)" if level == "REVIEW" else ""))
    for term in CFG["placeholder_terms"]:
        hits = {n: t.count(term) for n, t in pages.items() if term in t}
        if hits:
            add("REVIEW", f"placeholder '{term}': " + ", ".join(f"{n} x{c}" for n, c in sorted(hits.items())))

    # states directory
    tc = visible_text(pages.get("telehealth-consent.html", ""))
    found = [s for s in STATES if re.search(r"\b" + re.escape(s) + r"\b", tc)]
    # "Virginia" also matches inside "West Virginia" via \b? no: "West Virginia" contains " Virginia" with a boundary
    add("PASS" if len(found) == 51 else "REVIEW",
        f"telehealth-consent.html names {len(found)} of 51 states plus DC" + ("" if len(found) == 51 else
        "; missing: " + ", ".join(s for s in STATES if s not in found)))


# ---------------------------------------------------------------- prices
def site_prices():
    out = {}
    for c in parse_cards((PUBLIC / "index.html").read_text(encoding="utf-8")):
        p = norm_product(c["name"])
        m = re.search(r"\$(\d+)", " ".join(c["price"]))
        if p and m:
            out[p] = int(m.group(1))
    return out


def csv_prices():
    out = {}
    path = ROOT / "shopify-products-import.csv"
    if path.exists():
        for r in csv.DictReader(io.StringIO(path.read_text(encoding="utf-8"))):
            p = norm_product(r.get("Title", ""))
            if p:
                out[p] = int(float(r["Variant Price"]))
    return out


def theme_prices():
    out = {}
    path = ROOT / "shopify-theme/sections/treatments.liquid"
    if path.exists():
        for m in re.finditer(r"<h3>([^<]+)</h3>.*?tcard-price\">[^$]*\$(\d+)", path.read_text(encoding="utf-8")):
            p = norm_product(m.group(1))
            if p:
                out[p] = int(m.group(2))
    return out


# ---------------------------------------------------------------- live
def audit_live(live):
    section("3. Live site, " + CFG["live_base"])
    status, final, page = fetch(CFG["live_base"] + "/")
    if status is None:
        add("REVIEW", f"could not reach the live site: {page[:120]}")
        return
    add("PASS" if status == 200 else "FAIL", f"home page answers {status} at {final}")
    title = re.search(r"<title>(.*?)</title>", page, re.S | re.I)
    title = html.unescape(title.group(1)).strip() if title else ""
    is_shopify = "Shopify.shop" in page or "cdn.shopify.com" in page
    theme = re.search(r'Shopify\.theme = \{"name":"([^"]+)"', page)
    live["platform"] = "Shopify" if is_shopify else "static or other"
    add("REVIEW" if is_shopify else "PASS",
        f"live platform: {live['platform']}" + (f", theme '{theme.group(1)}'" if theme else "")
        + (". Target is the static public/ site with OpenLoop intake links; this store is the stopgap" if is_shopify else ""))
    add("PASS" if CFG["expected_store_name"].lower() in title.lower() else "FAIL",
        f"page title is '{title}'" + ("" if CFG["expected_store_name"].lower() in title.lower() else
                                      f"; should include '{CFG['expected_store_name']}'"))
    if re.search(r'<form[^>]*action="[^"]*/password', page) or "/password" in final:
        add("FAIL", "storefront password page is up; LegitScript needs the site public")
    if re.search(r"LegitScript\s+Certified", page, re.I):
        add("FAIL", "'LegitScript Certified' text is live; only allowed after certification")

    # words on the live page
    chk = load_check_module()
    text = chk.strip_markup(page)
    for m in chk.DRUGLIKE.finditer(text):
        w = m.group(0).lower().split("-")[-1]
        if not (w in chk.APPROVED or w.rstrip("s") in chk.APPROVED or w in chk.GENERIC_OK):
            add("FAIL", "live home page shows a drug-like word that is not one of the five (name withheld)")
            break
    if chk.COACHING.search(text):
        add("FAIL", "live home page uses coaching language")
    claims = []
    for pat, label in chk.CLAIMS:
        for m in re.finditer(pat, text, re.I):
            ctx = chk.context(text, m)
            if not chk.SAFE_CONTEXT.search(ctx):
                claims.append(f"'{label}': ...{ctx}...")
    for c in sorted(set(claims))[:10]:
        add("REVIEW", "live claim word " + c)

    # same-site links from the home page
    host = urllib.parse.urlparse(final).netloc
    links = set()
    for href in re.findall(r'href="([^"#]+)', page):
        u = urllib.parse.urljoin(final, html.unescape(href))
        pu = urllib.parse.urlparse(u)
        if pu.netloc == host and not re.search(r"\.(css|js|png|jpe?g|webp|svg|ico|woff2?)(\?|$)", pu.path) \
                and not pu.path.startswith(("/cdn", "/cart")):
            links.add(u.split("?")[0])
    bad = []
    for u in sorted(links)[:40]:
        s, _, _ = fetch(u)
        if s != 200:
            bad.append(f"{urllib.parse.urlparse(u).path} ({s})")
    add("FAIL" if bad else "PASS", f"checked {min(len(links), 40)} same-site links" + (": broken " + ", ".join(bad) if bad else ", all answer 200"))

    # Shopify-only: products and product pages
    if is_shopify:
        s, _, body = fetch(CFG["live_base"] + "/products.json")
        if s == 200:
            prods = json.loads(body).get("products", [])
            live["prices"] = {}
            for i, p in enumerate(prods, 1):
                key = norm_product(p["title"])
                if key is None:
                    add("FAIL", f"live store product #{i} is not one of the five approved treatments (name withheld)")
                    continue
                live["prices"][key] = int(float(p["variants"][0]["price"]))
                ps, _, pp = fetch(f"{CFG['live_base']}/products/{p['handle']}")
                ok = ps == 200 and re.search(r"not\s+FDA[\s-]approved", pp, re.I)
                add("PASS" if ok else "FAIL", f"live product page {p['title']}: " + ("answers 200 with the FDA disclaimer" if ok else f"status {ps}, disclaimer {'found' if pp and 'FDA' in pp else 'missing'}"))
                live.setdefault("first_product", f"{CFG['live_base']}/products/{p['handle']}")

    # the Vercel foundation site, which public/ deploys to
    fu = CFG.get("foundation_url")
    if fu:
        s, f, body = fetch(fu + "/")
        t = re.search(r"<title>(.*?)</title>", body or "", re.S | re.I)
        t = html.unescape(t.group(1)).strip() if t else ""
        ok = s == 200 and CFG["expected_store_name"].lower() in t.lower()
        add("PASS" if ok else "FAIL", f"foundation site {fu} answers {s}, title '{t}'")
        local_h1 = re.search(r"<h1[^>]*>(.*?)</h1>", (PUBLIC / "index.html").read_text(encoding="utf-8"), re.S)
        if local_h1 and body and re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", local_h1.group(1))).strip() not in re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", body)):
            add("REVIEW", f"foundation site headline differs from public/index.html; Vercel may be behind the repo")

    # configured intake links answer
    for prod, url in CFG["intake_links"].items():
        if url:
            s, f, _ = fetch(url)
            add("PASS" if s == 200 else "FAIL", f"{prod} intake link answers {s}" + ("" if CFG["intake_host_hint"] in f.lower() else f", lands on {f}"))


def audit_prices(live):
    section("4. Prices across every surface")
    surfaces = {"public/ site": site_prices(), "theme fallback": theme_prices(), "product CSV": csv_prices()}
    if live.get("prices"):
        surfaces["live store"] = live["prices"]
    surfaces["planned"] = {k: v for k, v in CFG["planned_prices"].items() if v}
    rows = ["| Treatment | " + " | ".join(surfaces) + " |", "|---" * (len(surfaces) + 1) + "|"]
    for p in CFG["approved_products"]:
        vals = [surfaces[s].get(p) for s in surfaces]
        rows.append(f"| {p} | " + " | ".join(f"${v}" if v else "-" for v in vals) + " |")
        current = {v for s, d in surfaces.items() if s != "planned" for v in [d.get(p)] if v}
        if len(current) > 1:
            add("FAIL", f"{p}: surfaces disagree on price: " + ", ".join(f"{s} ${d.get(p)}" for s, d in surfaces.items() if s != "planned" and d.get(p)))
        plan = CFG["planned_prices"].get(p)
        if plan and current and current != {plan}:
            add("REVIEW", f"{p}: shows ${'/$'.join(map(str, sorted(current)))}, planned month-to-month is ${plan} once the platform is signed")
        if p == "glutathione" and current:
            add("REVIEW", "glutathione is still listed; OpenLoop's written proposal says it is not included")
    live["price_table"] = "\n".join(rows)


def audit_theme_zip():
    section("5. Shopify theme zip, stopgap only")
    zp = ROOT / "velacore-shopify-theme.zip"
    if not zp.exists():
        add("REVIEW", "velacore-shopify-theme.zip not found")
        return
    stale = []
    with zipfile.ZipFile(zp) as z:
        names = set(z.namelist())
        for f in (ROOT / "shopify-theme").rglob("*"):
            if f.is_file() and f.name != "SETUP.md":
                rel = f.relative_to(ROOT / "shopify-theme").as_posix()
                if rel not in names:
                    stale.append(f"{rel} missing from zip")
                elif z.read(rel).replace(b"\r\n", b"\n") != f.read_bytes().replace(b"\r\n", b"\n"):
                    stale.append(f"{rel} differs")
    add("REVIEW" if stale else "PASS", "theme zip " + ("is out of date: " + "; ".join(stale[:8]) if stale else "matches shopify-theme/"))


# ---------------------------------------------------------------- render
def audit_render(outdir, live, use_live):
    section("6. Rendered pages, desktop and phone")
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        add("REVIEW", "Playwright for Python is not installed; render checks skipped")
        return
    targets = [("local-home", (PUBLIC / "index.html").as_uri())]
    if use_live:
        targets.append(("live-home", CFG["live_base"] + "/"))
        if live.get("first_product"):
            targets.append(("live-product", live["first_product"]))
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for name, url in targets:
            for vp, (w, h) in CFG["viewports"].items():
                ctx = browser.new_context(viewport={"width": w, "height": h}, user_agent=UA,
                                          is_mobile=vp == "phone", has_touch=vp == "phone")
                page = ctx.new_page()
                errors = []
                page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                page.on("pageerror", lambda e: errors.append(str(e)))
                try:
                    page.goto(url, wait_until="networkidle", timeout=45000)
                except Exception as e:
                    add("REVIEW", f"{name} {vp}: page did not settle: {str(e)[:100]}")
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(800)
                info = page.evaluate("""() => ({
                    overflow: document.documentElement.scrollWidth - window.innerWidth,
                    broken: [...document.images].filter(i => i.complete && i.naturalWidth === 0 && i.src).map(i => i.src.split('/').pop().slice(0,60)),
                    h1: (document.querySelector('h1')||{}).innerText || ''
                })""")
                shot = outdir / f"{name}-{vp}.png"
                page.screenshot(path=str(shot), full_page=True)
                problems = []
                if info["overflow"] > 2:
                    problems.append(f"sideways scroll of {info['overflow']}px")
                if info["broken"]:
                    problems.append("broken images: " + ", ".join(info["broken"][:5]))
                errs = [e for e in errors if "favicon" not in e][:3]
                if errs:
                    problems.append("console errors: " + " | ".join(x[:90] for x in errs))
                add("REVIEW" if problems else "PASS", f"{name} {vp}: " + ("; ".join(problems) if problems else "renders clean") + f". Screenshot {shot.relative_to(ROOT).as_posix()}")
                ctx.close()
        browser.close()


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-live", action="store_true")
    ap.add_argument("--no-render", action="store_true")
    a = ap.parse_args()
    stamp = dt.datetime.now().strftime("%Y-%m-%d_%H%M")
    outdir = ROOT / "_audit" / stamp
    outdir.mkdir(parents=True, exist_ok=True)
    live = {}

    audit_compliance()
    audit_local()
    if not a.no_live:
        audit_live(live)
    audit_prices(live)
    audit_theme_zip()
    if not a.no_render:
        audit_render(outdir, live, not a.no_live)

    counts = {k: sum(1 for s in sections.values() for lv, _ in s if lv == k) for k in ("FAIL", "REVIEW", "PASS")}
    lines = [f"# Velacore site audit, {stamp.replace('_', ' ')}", "",
             f"**{counts['FAIL']} fail, {counts['REVIEW']} review, {counts['PASS']} pass.** "
             f"Live platform: {live.get('platform', 'not checked')}.", ""]
    for title, items in sections.items():
        lines += [f"## {title}", ""]
        for level in ("FAIL", "REVIEW", "PASS"):
            lines += [f"- **{level}** {msg}" for lv, msg in items if lv == level]
        if title.startswith("4.") and live.get("price_table"):
            lines += ["", live["price_table"]]
        lines.append("")
    report = "\n".join(lines)
    (outdir / "report.md").write_text(report, encoding="utf-8")
    print(report)
    print(f"Report saved to {(outdir / 'report.md').relative_to(ROOT).as_posix()}")
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
