%%writefile vol_impl.py
import numpy as np

from bs_pricer import Option

def vol_implicite(Cmarche,S,K,r,T,type_option):
  sigma=0.20
  epsilon=1e-6
  opt=Option(S,K,r,T,sigma,type_option)
  prixBS=opt.prix()

  while np.absolute(prixBS-Cmarche)>epsilon:
    opt=Option(S,K,r,T,sigma,type_option)
    prixBS=opt.prix()
    vega=opt.vega()*100
    sigma=sigma-(prixBS-Cmarche)/vega # Corrected this line

   
    

  return sigma
