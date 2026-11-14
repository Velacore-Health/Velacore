"""Collect Google autocomplete suggestions for seed phrases. Run: python -I tools/keyword_suggest.py "seed one" "seed two". Generic queries only; never put a person or patient detail in a seed."""
import json, sys, time, urllib.parse, urllib.request
seeds = sys.argv[1:]
out = {}
for s in seeds:
    for suffix in ["", " a", " c", " h", " w", " v", " for", " vs", " cost", " online"]:
        q = (s + suffix).strip()
        url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=" + urllib.parse.quote(q)
        try:
            data = json.loads(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=10).read().decode("utf-8", "replace"))
            for x in data[1]:
                out.setdefault(s, set()).add(x)
        except Exception as e:
            print("err", q, e, file=sys.stderr)
        time.sleep(0.3)
for s, v in out.items():
    print(f"## {s} ({len(v)})")
    for x in sorted(v): print("  ", x)
