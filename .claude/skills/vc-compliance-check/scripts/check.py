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
PUBLIC = ("public/", "velacore-preview.html")  # the Shopify theme and CSV were removed Nov 13 2026 when the store closed

APPROVED = {"tirzepatide", "semaglutide", "sermorelin", "glutathione"}
# Generic words that end like drug names but are not product names.
GENERIC_OK = {"peptide", "peptides", "polypeptide", "polypeptides", "nucleotide", "nucleotides",
              "dinucleotide", "glucagon"}
DRUGLIKE = re.compile(r"\b[a-z0-9-]*(?:tide|relin|orelin|tropin|peptin|tidine|morelin)s?\b", re.I)
PART = re.compile(r"[a-z0-9]*(?:tide|relin|orelin|tropin|peptin|tidine|morelin)s?", re.I)


def bad_parts(word):
    """Every hyphen-separated part that looks like a drug name and is not approved or generic."""
    out = []
    for w in word.lower().split("-"):
        if not PART.fullmatch(w) or w in {"tide", "tides"} or w in GENERIC_OK:
            continue
        if w in APPROVED or w.rstrip("s") in APPROVED:
            continue
        out.append(w)
    return out

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
            for w in bad_parts(m.group(0)):
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
            for m in re.finditer(r"LegitScript\s+Certified", text, re.I):
                add("FAIL", f"LegitScript badge text at {rel}:{line_of(text, m.start())}; allowed only after certification is issued")
        # 3. secrets anywhere
        for pat, label in SECRETS:
            for m in re.finditer(pat, text):
                add("FAIL", f"possible {label} at {rel}:{line_of(text, m.start())}")

    for word, where in sorted(unknown.items()):
        add("FAIL", f"drug-like word not on the approved list: '{word}' in {len(where)} place(s): {', '.join(where[:5])}")
    if not unknown:
        add("PASS", "no drug-like words outside the approved treatments")

    # 4. file names
    for p in ROOT.rglob("*"):
        parts = p.relative_to(ROOT).parts
        if any(x in SKIP_DIRS for x in parts):
            continue
        # Same rule as the text scan: every part of a hyphenated name is judged, so label-tirzepatide
        # passes and a name that pairs an unapproved word with an approved one still fails.
        if any(bad_parts(m.group(0)) for m in DRUGLIKE.finditer(p.name)):
            add("FAIL", f"file name has a drug-like word: {p.relative_to(ROOT).as_posix()}")
    add("REVIEW", "file names that don't match a public product: "
        + ", ".join(sorted({p.relative_to(ROOT).as_posix() for p in ROOT.glob("public/images/*")
                            if p.stem not in {"tirzepatide", "semaglutide", "sermorelin", "glutathione", "nad",
                                              "og", "start", "dr-broussard",
                                              "amino"}}) or ["none"]))  # amino = education-section chain illustration

    if not any("LegitScript badge" in m for m in results["FAIL"]):
        add("PASS", "no LegitScript badge text on public pages")

    # 5. FDA compounded-medication disclaimer on every program page and Start page
    disc = re.compile(r"not\s+FDA[\s-]approved", re.I)
    pages = sorted((ROOT / "public/programs").glob("*.html")) + sorted((ROOT / "public/start").glob("*.html"))
    missing = [p.relative_to(ROOT).as_posix() for p in pages if not disc.search(p.read_text(encoding="utf-8"))]
    if not pages:
        add("FAIL", "no program pages found in public/programs")
    elif missing:
        for m in missing:
            add("FAIL", f"FDA compounded-medication disclaimer missing from {m}")
    else:
        add("PASS", f"FDA compounded-medication disclaimer present on all {len(pages)} program and Start pages")

    for level in ("FAIL", "REVIEW", "PASS"):
        for msg in results[level]:
            print(f"{level}: {msg}")
    print(f"\nSummary: {len(results['FAIL'])} fail, {len(results['REVIEW'])} review, {len(results['PASS'])} pass")
    return 1 if results["FAIL"] else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
