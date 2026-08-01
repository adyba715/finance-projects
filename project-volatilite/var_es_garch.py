import numpy as np
import pandas as pd
from scipy import stats

def var_historique(rendements, alpha=0.05, fenetre=250):
    VaR = []
    for t in range(fenetre, len(rendements)):
        fenetre_hist = rendements.iloc[t-fenetre:t] * 100
        VaR.append(-np.percentile(fenetre_hist, alpha*100))
    return np.array(VaR)

def var_gaussienne(rendements, alpha=0.05):
    mu = rendements.mean() * 100
    sigma = rendements.std() * 100
    z = stats.norm.ppf(alpha)
    return -(mu + z * sigma)

def var_garch(previsions, mu, alpha=0.05):
    z = stats.norm.ppf(alpha)
    return -(mu + z * previsions)

def es_empirique(pertes, VaR):
    masque = pertes > VaR
    if masque.sum() == 0:
        return np.nan
    return np.mean(pertes[masque])

def test_kupiec(x, T, alpha=0.05):
    p_obs = x / T
    if p_obs == 0 or p_obs == 1:
        return None, None
    LR = -2*(x*np.log(alpha/p_obs) + (T-x)*np.log((1-alpha)/(1-p_obs)))
    p_value = 1 - stats.chi2.cdf(LR, df=1)
    return LR, p_value
