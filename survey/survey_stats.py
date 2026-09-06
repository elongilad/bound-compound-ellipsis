#!/usr/bin/env python3
"""Wilson CIs and population projections for the Even-Shoshan random survey.
Reproduces the figures in ch. 3 of the thesis from classification_1007.tsv.

source_period codes: B = biblical, C = classical/rabbinic-medieval, M = medieval/early-modern, N = Modern Hebrew coinage.
coinage_cats holds a JSON array of category codes 0-24 (see the thesis codebook, appendix C.1)."""
import csv, math, json, collections
def wilson(x, n, z=1.959964):
    p = x/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c-h, c+h
rows = list(csv.DictReader(open('classification_1007.tsv', encoding='utf-8'), delimiter='\t'))
assert len(rows) == 1007, len(rows)
modern = [r for r in rows if r['source_period'].strip() == 'N']
n = len(modern); assert n == 568, n
cats = {r['headword']: json.loads(r['coinage_cats'] or '[]') for r in modern}
assert all(all(isinstance(c, int) and 0 <= c <= 24 for c in v) for v in cats.values())
empty = [h for h, v in cats.items() if not v]
counts = collections.Counter(c for v in cats.values() for c in set(v))
POP = 27330                      # noun headwords in Even-Shoshan (2003)
MODERN_POP = POP * n / len(rows)  # 27,330 x 568/1,007 = 15,415.5; round only when printing
print(f"rows={len(rows)} modern-stratum n={n} assignments={sum(counts.values())} multi-coded={sum(1 for v in cats.values() if len(set(v))>1)} uncoded={empty}")
print(f"projected modern lexicon = {MODERN_POP:,.0f}")
for cat, x in counts.most_common():
    lo, hi = wilson(x, n)
    print(f"cat {cat:>2}: {x:3} / {n} = {100*x/n:5.2f}%   CI95 {100*lo:.2f}%-{100*hi:.2f}%   projected {MODERN_POP*x/n:.0f} ({MODERN_POP*lo:.0f}-{MODERN_POP*hi:.0f})")
# ellipsis (code 21): conservative (3 certain cases) and expanded (4, incl. the borderline noset) counts
x4 = counts[21]; x3 = x4 - 1
for label, x in (("ellipsis, conservative", x3), ("ellipsis, expanded", x4)):
    lo, hi = wilson(x, n); print(f"{label}: {x}/{n} = {100*x/n:.2f}%  CI95 {100*lo:.2f}%-{100*hi:.2f}%  projected {MODERN_POP*x/n:.0f} ({MODERN_POP*lo:.0f}-{MODERN_POP*hi:.0f})")
big = {4, 20, 10}
print(f"union of codes 4/20/10: {sum(1 for v in cats.values() if set(v)&big)}/{n}")
