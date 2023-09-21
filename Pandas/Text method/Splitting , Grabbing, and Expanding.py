import pandas as pd

tech_finance = ['GOOG,APPL,AMZN','JPM,BAC,GS']
tickers = pd.Series(tech_finance)
print(tickers.str.split(','), "\n\n\n")
print(tickers.str.split(",", expand= True))