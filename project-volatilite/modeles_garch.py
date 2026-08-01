%%writefile modeles_garch.py
import numpy as np
import pandas as pd
from arch import arch_model

def estimer_garch(rendements, p=1, q=1):
    modele = arch_model(rendements * 100, vol='Garch', p=p, q=q)
    return modele.fit(disp='off')

def estimer_gjr(rendements, p=1, o=1, q=1):
    modele = arch_model(rendements * 100, vol='Garch', p=p, o=o, q=q)
    return modele.fit(disp='off')

def estimer_egarch(rendements, p=1, o=1, q=1):
    modele = arch_model(rendements * 100, vol='EGARCH', p=p, o=o, q=q)
    return modele.fit(disp='off')

def comparer_modeles(rendements):
    res_garch  = estimer_garch(rendements)
    res_gjr    = estimer_gjr(rendements)
    res_egarch = estimer_egarch(rendements)
    print(f"GARCH(1,1) — AIC: {res_garch.aic:.2f}, BIC: {res_garch.bic:.2f}")
    print(f"GJR-GARCH  — AIC: {res_gjr.aic:.2f}, BIC: {res_gjr.bic:.2f}")
    print(f"EGARCH     — AIC: {res_egarch.aic:.2f}, BIC: {res_egarch.bic:.2f}")
    return res_garch, res_gjr, res_egarch
