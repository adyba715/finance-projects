import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
from vol_impl import vol_implicite

def smile_vol(symbole_ticker,jours_min=15, borne_min=0.97, borne_max=1.10, volume_min=20, r=0.05):
    ticker = yf.Ticker(symbole_ticker)
    S = ticker.history(period="1d")['Close'].iloc[-1]
    for date_mat in ticker.options:
      date_mat_obj = dt.datetime.strptime(date_mat, '%Y-%m-%d')
      T = (date_mat_obj - dt.datetime.now()).days / 365
      if T >= jours_min/365:
        maturite = date_mat
        break
   
    calls = ticker.option_chain(maturite).calls
    calls_filtre = calls[(calls['strike'] > borne_min * S) & (calls['strike'] < borne_max * S) & (calls['volume'] > volume_min)]

    volimps = []
    for K, Cmarche in zip(calls_filtre['strike'], calls_filtre['lastPrice']):
        volimp = vol_implicite(Cmarche, S, K, r, T, "call")  
        volimps.append(volimp)
    return calls_filtre['strike'], volimps 


def graph_smile(symbole_ticker):
    strikes, vols = smile_vol(symbole_ticker)  
    plt.plot(strikes, vols)
    plt.xlabel("Strike")
    plt.ylabel("Vol implicite")
    plt.title(f"Smile de volatilité — {symbole_ticker}")
    plt.show()
