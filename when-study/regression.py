#!/usr/bin/env python3
"""Two-factor logistic regression (IRLS), Mann-Whitney and AUC for the
reduced-vs-intact compound study (thesis section 5.4.4.2)."""
import csv, math
import numpy as np
rows=[r for r in csv.DictReader(open('analysis_dataset.tsv'),delimiter='\t')]
y=np.array([float(r['reduced']) for r in rows])
X=np.array([[1.0,float(r['log_rarer_comp']),float(r['log_phrase_freq'])] for r in rows])
b=np.zeros(3)
for _ in range(60):
    p=1/(1+np.exp(-X@b)); W=p*(1-p)+1e-9
    z=X@b+(y-p)/W
    b2=np.linalg.solve(X.T@(W[:,None]*X),X.T@(W*z))
    if np.max(np.abs(b2-b))<1e-10: b=b2; break
    b=b2
p=1/(1+np.exp(-X@b)); W=p*(1-p)
se=np.sqrt(np.diag(np.linalg.inv(X.T@(W[:,None]*X))))
from math import erf, sqrt
for name,bb,ss in zip(["intercept","log(rarer-comp)","log(phrase-freq)"],b,se):
    pv=2*(1-0.5*(1+erf(abs(bb/ss)/sqrt(2))))
    print(f"{name:18} beta={bb:+.3f} se={ss:.3f} p={pv:.4g}")
