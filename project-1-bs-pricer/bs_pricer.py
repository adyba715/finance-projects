 import numpy as np
 import scipy.stats as stats
 
 class Option:
     def __init__(self, S, K, r, T, sig,type_option="call"):
         self.S = S
         self.K = K
         self.r = r
         self.T = T
         self.sig = sig
         self.type_option=type_option
     def _d1(self):
         return (np.log(self.S/self.K) + (self.r + 0.5*self.sig**2)*self.T) / (self.sig*np.sqrt(self.T))
 
     def _d2(self):
         return self._d1() - self.sig*np.sqrt(self.T)
 
     def prix (self):
         d1= self._d1()
         d2= self._d2()
         if self.type_option=="call":
           return self.S*stats.norm.cdf(d1) - self.K*np.exp(-self.r*self.T)*stats.norm.cdf(d2)
         else:
           return self.K*np.exp(-self.r*self.T)*stats.norm.cdf(-d2) - self.S*stats.norm.cdf(-d1)
     def delta(self):
         return stats.norm.cdf(self._d1())
     def gamma(self):
         return stats.norm.pdf(self._d1())/(self.S*self.sig*np.sqrt(self.T))
     def theta(self):
         return (-self.S*stats.norm.pdf(self._d1())*self.sig)/(2*np.sqrt(self.T))-self.r*self.K*np.exp(-self.r*self.T)*stats.norm.cdf(self._d2())
     def vega(self):
         return self.S*stats.norm.pdf(self._d1())*np.sqrt(self.T)




