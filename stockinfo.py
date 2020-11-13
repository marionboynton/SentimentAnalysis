#from yahoo_finance import Share
import yfinance as yf
import pandas as pd


def get_market_data(ticker, time_period = '10y'):
    """
    input: ticker we are interested in
    time_period: #1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    
    output: returns a dataframe with 
    """
    tick = yf.Ticker(ticker)


    hist = tick.history(period = time_period, interval= '1d')['Close'] #close price only

    df = pd.DataFrame(hist)
    
    return df
