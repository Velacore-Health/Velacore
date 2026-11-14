"""Draws the peptide walk-through on the Learn page. Run: python -I tools/make_peptide_walk.py, then paste the output over the pep-walk block in public/learn.html."""
import math
T = ["#C9EEDF", "#8FDDC3", "#57C9A6", "#0C8F72"]
ST = "#0A7A61"
def lab(x, y, s, a="middle"):
    return f'<text class="pw-lab" x="{x}" y="{y}" text-anchor="{a}">{s}</text>'
def bead(x, y, r, i):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{T[i % 4]}" stroke="{ST}" stroke-width="2"/>'
def chain(pts, r, w=3):
    d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
    return f'<path d="{d}" fill="none" stroke="{ST}" stroke-width="{w}" stroke-linejoin="round"/>' + "".join(bead(x, y, r, i * 3 + 1) for i, (x, y) in enumerate(pts))
# 0 amino acid: one bead and a ring of 20 kinds
s0 = "".join(bead(240 + 108 * math.cos(2 * math.pi * k / 20 - math.pi / 2), 150 + 108 * math.sin(2 * math.pi * k / 20 - math.pi / 2), 8, k) for k in range(20))
s0 += f'<circle cx="240" cy="150" r="42" fill="{T[1]}" stroke="{ST}" stroke-width="2.5"/>' + lab(240, 292, "20 kinds of amino acid")
# 1 peptide: a short chain of 6
s1 = chain([(110 + 52 * i, 140 + 26 * math.sin(i * 1.1)) for i in range(6)], 20)
s1 += f'<path d="M96 214 v10 H384 v-10" fill="none" stroke="{ST}" stroke-width="2"/>' + lab(240, 252, "Peptide: 2 to 50 amino acids")
# 2 protein: a long chain folded back and forth
pts = [(240 + 125 * math.sin(3 * u + 0.6) * (0.75 + 0.25 * math.cos(5 * u)), 132 + 92 * math.sin(2 * u) * (0.8 + 0.2 * math.sin(7 * u))) for u in (2 * math.pi * k / 72 for k in range(72))]
s2 = chain(pts, 8, 2.5) + lab(240, 290, "Protein: a long chain, folded")
# 3 messenger: a peptide meets a receptor on a cell surface
s3 = f'<path d="M0 238 Q240 206 480 238 V300 H0 Z" fill="#DDF0E7" stroke="{ST}" stroke-width="2.5"/>'
s3 += f'<path d="M290 226 V184 a20 20 0 0 0 40 0 V226" fill="none" stroke="{ST}" stroke-width="5" stroke-linecap="round"/>'
s3 += chain([(96 + 40 * i, 70 + 28 * i) for i in range(4)], 14)
s3 += f'<path d="M232 158 Q270 166 296 176" fill="none" stroke="{ST}" stroke-width="2.5" stroke-dasharray="5 6" stroke-linecap="round"/>'
s3 += lab(70, 42, "Peptide", "start") + lab(372, 196, "Receptor", "start") + lab(60, 282, "Cell", "start")
s3 += "".join(f'<path d="M{310 - w} {256 + 10 * k} q{w} 8 {2 * w} 0" fill="none" stroke="{ST}" stroke-width="2" stroke-linecap="round" opacity="{1 - .25 * k}"/>' for k, w in enumerate((14, 20, 26)))
steps = [
    ("Amino acid", "Amino acids are the building blocks. The body uses 20 kinds.", s0),
    ("Peptide", "Link a few together and you have a peptide: a short chain, usually 2 to 50 amino acids.", s1),
    ("Protein", "Link many more and fold the chain, and you have a protein.", s2),
    ("Messenger", "Many peptides work as messengers. A peptide fits a receptor on a cell, and the cell responds.", s3),
]
g = "".join(f'<g class="pw-step{" is-on" if i == 0 else ""}" data-step="{i}">{svg}</g>' for i, (_, _, svg) in enumerate(steps))
btns = "".join(f'<button type="button" data-go="{i}" data-cap="{cap}" aria-pressed="{"true" if i == 0 else "false"}">{name}</button>' for i, (name, cap, _) in enumerate(steps))
print(f'''          <div class="edu-viz pep-walk" data-pepwalk>
            <svg viewBox="0 0 480 300" role="img" aria-labelledby="pwCap">{g}</svg>
            <p class="pw-cap" id="pwCap" aria-live="polite">{steps[0][1]}</p>
            <div class="pw-tabs" role="group" aria-label="Walk through how peptides are built">{btns}</div>
          </div>''')
