#!/usr/bin/env python3
"""Two-factor logistic regression (IRLS) for the reduced-vs-intact compound study
(thesis section 7.2), with odds ratios per tenfold frequency change, the
upper-third Mann-Whitney comparison and the AUC of the fitted model.
Predictors are base-10 logarithms: one unit = a tenfold change in frequency."""
import csv, math
import numpy as np
rows=[r for r in csv.DictReader(open('analysis_dataset.tsv', encoding='utf-8'),delimiter='\t')]
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
print(f"n = {len(rows)} (reduced {int(y.sum())}, intact {int(len(y)-y.sum())})")
for name,bb,ss in zip(["intercept","log10(rarer-comp)","log10(phrase-freq)"],b,se):
    pv=2*(1-0.5*(1+erf(abs(bb/ss)/sqrt(2))))
    line=f"{name:20} beta={bb:+.3f} se={ss:.3f} p={pv:.4g}"
    if name!="intercept": line+=f"   OR per tenfold = {math.exp(bb):.2f} (95% CI {math.exp(bb-1.96*ss):.2f}-{math.exp(bb+1.96*ss):.2f})"
    print(line)
# McFadden pseudo-R2
ll=np.sum(y*np.log(p)+(1-y)*np.log(1-p)); p0=y.mean(); ll0=np.sum(y*np.log(p0)+(1-y)*np.log(1-p0))
print(f"McFadden pseudo-R2 = {1-ll/ll0:.3f}")
# AUC of fitted probabilities (Mann-Whitney U / n1 n0)
pos=p[y==1]; neg=p[y==0]
auc=(np.sum(pos[:,None]>neg[None,:])+0.5*np.sum(pos[:,None]==neg[None,:]))/(len(pos)*len(neg))
print(f"AUC = {auc:.3f}")
# upper third by phrase frequency: rarer-component frequency, reduced vs intact (Mann-Whitney, normal approx., two-sided)
pf=X[:,2]; cut=np.quantile(pf,2/3); top=pf>=cut
a=X[top&(y==1),1]; c=X[top&(y==0),1]
U=np.sum(a[:,None]<c[None,:])+0.5*np.sum(a[:,None]==c[None,:]); n1,n0=len(a),len(c)
mu=n1*n0/2; sd=math.sqrt(n1*n0*(n1+n0+1)/12); zval=(U-mu)/sd; pmw=2*(1-0.5*(1+erf(abs(zval)/sqrt(2))))
print(f"upper third (phrase freq >= {cut:.2f}): reduced n={n1}, intact n={n0}; Mann-Whitney U={U:.1f}, z={zval:+.2f}, p={pmw:.3f} (rarer component rarer in reduced group if U < n1*n0/2)")
