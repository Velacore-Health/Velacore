"""Velacore compliance scan. Read-only. Prints FAIL / REVIEW / PASS lines.

Run from the repo root:  python -I .claude/skills/vc-compliance-check/scripts/check.py
Exit code 1 if any FAIL, else 0.

Restricted catalog names are never written in this repo, so this script does not
list them. It flags any drug-like word that is not one of the five approved
treatments, and a human or the agent judges each hit.
"""
import csv
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path.cwd()
TEXT_EXT = {".html", ".liquid", ".json", ".js", ".css", ".md", ".csv", ".txt", ".xml", ".yml", ".yaml"}
SKIP_DIRS = {".git", "01-raw-clips", "02-selects", "03-edits", "04-scheduled", "node_modules"}
# Scanned for public-surface rules: claims, coaching, badge text.
PUBLIC = ("public/", "shopify-theme/", "shopify-products-import.csv", "velacore-preview.html", "velacore-shopify-theme.zip:")

APPROVED = {"tirzepatide", "semaglutide", "sermorelin", "glutathione"}
# Generic words that end like drug names but are not product names.
GENERIC_OK = {"peptide", "peptides", "polypeptide", "polypeptides", "nucleotide", "nucleotides",
              "dinucleotide", "glucagon"}
DRUGLIKE = re.compile(r"\b[a-z0-9-]*(?:tide|relin|orelin|tropin|peptin|tidine|morelin)s?\b", re.I)

CLAIMS = [
    (r"\blose\s+(?:up\s+to\s+)?\d+", "weight-loss amount"),
    (r"\b\d+\s*(?:lbs?|pounds)\b", "pounds figure"),
    (r"\bclinically[\s-]proven\b", "proven claim"),
    (r"\bproven\b", "proven"),
    (r"\bguarantee[ds]?\b", "guarantee"),
    (r"\bcures?\b", "cure"),
    (r"\bmelts?\b", "melt"),
    (r"\bburns?\s+fat\b|\bfat[\s-]burn", "fat burning"),
    (r"\bmiracle\b", "miracle"),
    (r"\banti[\s-]?aging\b|\breverses?\s+aging\b", "anti-aging"),
    (r"\bboosts?\b", "boost"),
    (r"\bsafe\s+and\s+effective\b", "safe and effective"),
    (r"\b100\s*%", "100 percent"),
    (r"\bresults\b", "results"),
]
COACHING = re.compile(r"\bcoach(?:es|ing)?\b", re.I)
SECRETS = [
    (r"\bsk_(?:live|test)_[A-Za-z0-9]{8,}", "Stripe-style key"),
    (r"\b(?:api[_-]?key|secret|token)\s*[:=]\s*['\"][^'\"]{12,}", "inline key"),
    (r"\bDEA\s*(?:#|no\.?|number)?\s*[:#]?\s*[A-Z]{2}\d{7}\b", "DEA number"),
]

results = {"FAIL": [], "REVIEW": [], "PASS": []}


def add(level, msg):
    results[level].append(msg)


def iter_texts():
    for p in sorted(ROOT.rglob("*")):
        rel = p.relative_to(ROOT).as_posix()
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts) or not p.is_file():
            continue
        if rel.startswith(".claude/skills/vc-compliance-check/"):
            continue  # this skill's own pattern lists
        if p.suffix.lower() in TEXT_EXT:
            yield rel, p.read_text(encoding="utf-8", errors="replace")
        elif p.suffix.lower() == ".zip":
            with zipfile.ZipFile(p) as z:
                for n in z.namelist():
                    if Path(n).suffix.lower() in TEXT_EXT:
                        yield f"{rel}:{n}", z.read(n).decode("utf-8", errors="replace")


def _blank(m):
    # keep newlines so line numbers stay right
    return re.sub(r"[^\n]", " ", m.group(0))


def strip_markup(text):
    """Visible text only: drop scripts, styles, comments, tags and Liquid code."""
    text = re.sub(r"<script\b.*?</script>|<style\b.*?</style>|<!--.*?-->", _blank, text, flags=re.S | re.I)
    text = re.sub(r"\{%-?\s*schema\s*-?%\}.*?\{%-?\s*endschema\s*-?%\}", _blank, text, flags=re.S)
    text = re.sub(r"\{%.*?%\}|\{\{.*?\}\}", _blank, text, flags=re.S)
    text = re.sub(r"<[^>]*>", _blank, text, flags=re.S)
    return text


# Standard disclaimer phrasings that contain claim words but are required or harmless.
SAFE_CONTEXT = re.compile(r"not\s+a\s+guarantee|do(?:es)?\s+not\s+provide,\s+guarantee|results\s+vary|"
                          r"no\s+guarantee|does\s+not\s+guarantee|cannot\s+guarantee|not\s+guaranteed|"
                          r"search\s+results|no\s+results\s+for", re.I)


def context(text, m, width=60):
    s = text[max(0, m.start() - width): m.end() + width]
    return " ".join(s.split())


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def main():
    unknown = {}
    for rel, text in iter_texts():
        is_public = rel.startswith(PUBLIC)
        # 1. drug-like names anywhere in the repo
        for m in DRUGLIKE.finditer(text):
            w = m.group(0).lower().split("-")[-1]
            if w in APPROVED or w.rstrip("s") in APPROVED or w in GENERIC_OK or w in {"tide", "tides"}:
                continue
            unknown.setdefault(w, []).append(f"{rel}:{line_of(text, m.start())}")
        # 2. public-surface rules
        if is_public and Path(rel.split(":")[-1]).suffix.lower() not in {".css", ".js", ".json"}:
            body = strip_markup(text)
            seen = set()
            for pat, label in CLAIMS:
                for m in re.finditer(pat, body, re.I):
                    ctx = context(body, m)
                    key = (label, line_of(body, m.start()))
                    if SAFE_CONTEXT.search(ctx) or key in seen:
                        continue
                    seen.add(key)
                    add("REVIEW", f"claim word '{label}' at {rel}:{key[1]}: ...{ctx}...")
            for m in COACHING.finditer(body):
                add("FAIL", f"coaching language at {rel}:{line_of(body, m.start())}: ...{context(body, m)}...")
            if re.search(r"LegitScript\s+Certified", text, re.I) and not rel.startswith(("shopify-theme/", "velacore-shopify-theme.zip:")):
                for m in re.finditer(r"LegitScript\s+Certified", text, re.I):
                    add("FAIL", f"LegitScript badge text outside the theme toggle at {rel}:{line_of(text, m.start())}")
        # 3. secrets anywhere
        for pat, label in SECRETS:
            for m in re.finditer(pat, text):
                add("FAIL", f"possible {label} at {rel}:{line_of(text, m.start())}")

    for word, where in sorted(unknown.items()):
        add("FAIL", f"drug-like word not on the approved list: '{word}' in {len(where)} place(s): {', '.join(where[:5])}")
    if not unknown:
        add("PASS", "no drug-like words outside the five approved treatments")

    # 4. file names
    for p in ROOT.rglob("*"):
        parts = p.relative_to(ROOT).parts
        if any(x in SKIP_DIRS for x in parts):
            continue
        m = DRUGLIKE.search(p.name)
        if m and m.group(0).lower() not in APPROVED:
            add("FAIL", f"file name has a drug-like word: {p.relative_to(ROOT).as_posix()}")
    add("REVIEW", "file names that don't match a public product: "
        + ", ".join(sorted({p.relative_to(ROOT).as_posix() for p in ROOT.glob("public/images/*")
                            if p.stem not in {"tirzepatide", "semaglutide", "sermorelin", "glutathione", "nad",
                                              "og", "start", "dr-broussard",
                                              "amino"}}) or ["none"]))  # amino = education-section chain illustration

    # 5. badge toggle default
    sd = ROOT / "shopify-theme/config/settings_data.json"
    try:
        raw = sd.read_text(encoding="utf-8")
        flag = re.search(r'"legitscript_certified"\s*:\s*(true|false)', raw)
        if flag and flag.group(1) == "false":
            add("PASS", "LegitScript badge toggle is OFF in settings_data.json")
        elif flag:
            add("FAIL", "LegitScript badge toggle is ON in settings_data.json; allowed only after certification is issued")
        else:
            add("REVIEW", "legitscript_certified setting not found in settings_data.json")
    except OSError:
        add("REVIEW", "settings_data.json not found")

    # 6. disclaimer on product surfaces
    disc = re.compile(r"not\s+FDA[\s-]approved", re.I)
    mp = ROOT / "shopify-theme/sections/main-product.liquid"
    if mp.exists() and disc.search(mp.read_text(encoding="utf-8")):
        add("PASS", "FDA compounded-medication disclaimer present in main-product.liquid")
    else:
        add("FAIL", "FDA compounded-medication disclaimer missing from main-product.liquid")
    csvp = ROOT / "shopify-products-import.csv"
    if csvp.exists():
        rows = list(csv.DictReader(io.StringIO(csvp.read_text(encoding="utf-8"))))
        titles = [r.get("Title", "") for r in rows]
        for r in rows:
            name = r.get("Title", "").lower()
            if not any(a in name for a in APPROVED | {"nad"}):
                add("FAIL", f"CSV product not on the approved list: {r.get('Title')}")
            if not disc.search(r.get("Body (HTML)", "")):
                add("FAIL", f"CSV product missing FDA disclaimer: {r.get('Title')}")
        add("PASS" if len(rows) == 5 else "REVIEW", f"CSV has {len(rows)} products: {', '.join(titles)}")

    for level in ("FAIL", "REVIEW", "PASS"):
        for msg in results[level]:
            print(f"{level}: {msg}")
    print(f"\nSummary: {len(results['FAIL'])} fail, {len(results['REVIEW'])} review, {len(results['PASS'])} pass")
    return 1 if results["FAIL"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
