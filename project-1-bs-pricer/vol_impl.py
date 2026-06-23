import numpy as np
from bs_pricer import Option
def vol_implicite(Cmarche, S, K, r, T, type_option, max_iter=1000, epsilon=1e-6):
    sigma = 0.20
    
    for i in range(max_iter):
        opt = Option(S, K, r, T, sigma, type_option)
        prixBS = opt.prix()
        vega = opt.vega() * 100
        
        if np.abs(prixBS - Cmarche) < epsilon:
            return sigma
        
        if vega < 1e-8:
            return np.nan
        
        sigma = sigma - (prixBS - Cmarche) / vega
        sigma = max(sigma, 1e-4)
    
    return np.nan
