#!/usr/bin/env python3
"""Wilson CIs and population projections for the Even-Shoshan random survey.
Reproduces the figures in ch. 3 of the thesis from classification_1007.tsv."""
import csv, math, collections
def wilson(x, n, z=1.959964):
    p = x/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c-h, c+h
rows = list(csv.DictReader(open('classification_1007.tsv'), delimiter='\t'))
modern = [r for r in rows if (r['source_period'] or '').strip() in ('חדשה','ח','modern')]
n = len(modern)
counts = collections.Counter()
for r in modern:
    for c in (r['coinage_cats'] or '').split(','):
        c = c.strip()
        if c: counts[c] += 1
POP = 27330; MODERN_POP = round(POP*0.564)
print(f"modern-stratum sample n={n}; projected modern lexicon={MODERN_POP}")
for cat, x in counts.most_common():
    lo, hi = wilson(x, n)
    print(f"cat {cat:>4}: {x:3} / {n}  = {100*x/n:5.2f}%   CI95 {100*lo:.2f}%-{100*hi:.2f}%   projected {MODERN_POP*x/n:.0f} ({MODERN_POP*lo:.0f}-{MODERN_POP*hi:.0f})")
