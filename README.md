# Ellipsis in Bound Compounds in Modern Hebrew — Data & Code

Data and analysis code accompanying the MA thesis **"ההשמט בצירוף הכבול"**
(Ellipsis in Bound Compounds: A Lexical Mechanism in Modern Hebrew), Tel Aviv University.

## Contents
- `survey/classification_1007.tsv` — the author's etymological classification layer for the
  random sample of 1,007 nouns drawn from Even-Shoshan (2003) (headwords + category tags only;
  the dictionary's content is copyrighted and is **not** included).
- `survey/survey_stats.py` — Wilson confidence intervals and population projections (thesis ch. 3). Run from `survey/`; prints row/assignment sanity counts, both ellipsis counts (conservative 3, expanded 4), and the union coverage of the three dominant processes.
- `when-study/analysis_dataset.tsv` — the reduced-vs-intact compound dataset (phrase frequencies
  from the JPress historical newspaper archive; component frequencies from the NITE M1 lexeme list).
- `when-study/regression.py` — the two-factor logistic regression (thesis §7.2): coefficients, odds ratios per tenfold frequency change with 95% CIs, McFadden pseudo-R², AUC, and the upper-third Mann–Whitney comparison. Run from `when-study/`; needs Python 3 and NumPy.
- `inventory/inventory_45.tsv` — the full inventory of 45 verified ellipsis cases (thesis appendix A).

## Sources
- JPress — Historical Jewish Press, National Library of Israel & Tel Aviv University (searches
  performed through the archive's public search interface).
- NITE NLP Tools, National Institute for Testing and Evaluation (hlp.nite.org.il/WebCorpora.aspx).
- Google Books Ngram Viewer (Hebrew 2019 corpus).

## Citation
Please cite the thesis. License for code: MIT. Data files: CC BY 4.0 (author's tagging layers only).

## Reproducing
```
cd survey && python3 survey_stats.py
cd ../when-study && python3 regression.py
```
Expected: n=568 modern entries, 583 assignments; ellipsis 3/568 = 0.53% (CI 0.18–1.54%) and 4/568 = 0.70% (CI 0.27–1.80%); regression β = −0.95 (p ≈ 0.004) and +0.55 (p ≈ 0.010), pseudo-R² ≈ 0.09.

## Changes
- 2026-09-06 — *mivtza* (← *mivtza mekhirot*) and *mif'al* (← *mif'al ta'asiya*) removed from the inventory: on re-examination the surviving element kept its general sense and was applied to a new domain (semantic extension), so these are not cases of ellipsis. The inventory is now 45 cases; the reduced-vs-intact dataset never included them and is unchanged. Section references updated to the final thesis numbering.
- 2026-09-06 — `survey_stats.py` fixed (it filtered on the wrong period code and split JSON arrays as strings, selecting zero rows); `regression.py` now also reports odds ratios, AUC and the upper-third Mann–Whitney test it previously only promised.
