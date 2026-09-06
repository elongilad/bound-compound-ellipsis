# Ellipsis in Bound Compounds in Modern Hebrew — Data & Code

Data and analysis code accompanying the MA thesis **"ההשמט בצירוף הכבול"**
(Ellipsis in Bound Compounds: A Lexical Mechanism in Modern Hebrew), Tel Aviv University.

## Contents
- `survey/classification_1007.tsv` — the author's etymological classification layer for the
  random sample of 1,007 nouns drawn from Even-Shoshan (2003) (headwords + category tags only;
  the dictionary's content is copyrighted and is **not** included).
- `survey/survey_stats.py` — Wilson confidence intervals and population projections (thesis ch. 3).
- `when-study/analysis_dataset.tsv` — the reduced-vs-intact compound dataset (phrase frequencies
  from the JPress historical newspaper archive; component frequencies from the NITE M1 lexeme list).
- `when-study/regression.py` — the two-factor logistic regression (thesis §7.2).
- `inventory/inventory_45.tsv` — the full inventory of 45 verified ellipsis cases (thesis appendix A).

## Sources
- JPress — Historical Jewish Press, National Library of Israel & Tel Aviv University (searches
  performed through the archive's public search interface).
- NITE NLP Tools, National Institute for Testing and Evaluation (hlp.nite.org.il/WebCorpora.aspx).
- Google Books Ngram Viewer (Hebrew 2019 corpus).

## Citation
Please cite the thesis. License for code: MIT. Data files: CC BY 4.0 (author's tagging layers only).

## Changes
- 2026-09-06 — *mivtza* (← *mivtza mekhirot*) and *mif'al* (← *mif'al ta'asiya*) removed from the inventory: on re-examination the surviving element kept its general sense and was applied to a new domain (semantic extension), so these are not cases of ellipsis. The inventory is now 45 cases; the reduced-vs-intact dataset never included them and is unchanged. Section references updated to the final thesis numbering.
