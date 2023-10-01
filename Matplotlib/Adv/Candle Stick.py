import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Generate simulated stock market data
# np.random.seed(42)
num_days = 50
dates = pd.date_range(start="2023-01-01", periods=num_days, freq="D")
open_prices = 100 + np.cumsum(np.random.randn(num_days))
high_prices = open_prices + np.random.rand(num_days) * 10
low_prices = open_prices - np.random.rand(num_days) * 10
close_prices = open_prices + np.random.randn(num_days) * 5

# Create a Pandas DataFrame to store the stock data
df = pd.DataFrame({'Date': dates, 'Open': open_prices, 'High': high_prices, 'Low': low_prices, 'Close': close_prices})

# Create a Matplotlib figure and subplot for candlestick chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Create candlestick chart with thicker candlesticks
candlestick_width = 0.8  # Adjust the candlestick width as needed
for index, row in df.iterrows():
    if row['Open'] < row['Close']:
        color = 'g'
    else:
        color = 'r'
    ax.plot([mdates.date2num(row['Date']), mdates.date2num(row['Date'])], [row['Low'], row['High']], color, lw=10)  # Thick candlesticks
    # ax.plot([mdates.date2num(row['Date']) - candlestick_width / 2, mdates.date2num(row['Date']) + candlestick_width / 2], [row['Open'], row['Open']], color, lw=2)
    # ax.plot([mdates.date2num(row['Date']) - candlestick_width / 2, mdates.date2num(row['Date']) + candlestick_width / 2], [row['Close'], row['Close']], color, lw=2)

# Customize the plot
ax.set_title('Stock Price Candlestick Chart')
ax.set_xlabel('Date')
ax.set_ylabel('Price')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()
