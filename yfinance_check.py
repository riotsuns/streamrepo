import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

#% matplotlib inline


days = 14
tickers  = {
    'apple': 'AAPL',
    'microsoft': 'MSFT',
    'facebook': 'FB',
    'google': 'GOOGL',
    'amazon': 'AMZN'
}

def get_data(days, tickers):
  df = pd.DataFrame()
  for company in tickers.keys():
  #company = 'facebook'

    tkr = yf.Ticker(tickers[company])

    hist = tkr.history(period=f'{days}d')

    hist.index = hist.index.strftime('%d %B %Y')
    hist= hist[['Close']]
    hist.columns = [company]

    hist = hist.T
    hist.index.name = 'Name'
  #hist
    df = pd.concat([df, hist])
  
  return df  


days = 14
tickers  = {
    'apple': 'AAPL',
    'microsoft': 'MSFT',
    'facebook': 'FB',
    'google': 'GOOGL',
    'amazon': 'AMZN'
}

get_data(days, tickers)






