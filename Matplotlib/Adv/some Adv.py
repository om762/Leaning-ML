import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate a time series dataset of stock prices
np.random.seed(42)
num_days = 100
dates = pd.date_range(start="2023-01-01", periods=num_days, freq="D")
stock_prices = 100 + np.cumsum(np.random.randn(num_days))

# Create a Pandas DataFrame
df = pd.DataFrame({'Date': dates, 'StockPrice': stock_prices})

# Calculate daily returns
df['DailyReturn'] = df['StockPrice'].pct_change()

# Calculate a rolling 10-day moving average
df['10DayMovingAverage'] = df['StockPrice'].rolling(window=10).mean()

# Create a Matplotlib figure
plt.figure(figsize=(12, 6))

# Plot the stock price data
plt.subplot(2, 1, 1)
plt.plot(df['Date'], df['StockPrice'], label='Stock Price', color='b')
plt.plot(df['Date'], df['10DayMovingAverage'], label='10-Day Moving Average', color='r', linestyle='--')
plt.title('Stock Price and 10-Day Moving Average')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Plot the daily returns
plt.subplot(2, 1, 2)
plt.plot(df['Date'], df['DailyReturn'], label='Daily Returns', color='g')
plt.title('Daily Returns')
plt.xlabel('Date')
plt.ylabel('Return')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
