import requests
import pandas as pd

# Set your Alpha Vantage API key here
api_key = "ZG5MLKJMUZ2UEAJ8"

# Set the symbol for the stock you want to download
symbol = "LPLA"

# Define the URL for Alpha Vantage's TIME_SERIES_DAILY_ADJUSTED API
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"

# Send a request to the API and get the response
response = requests.get(url)

# Load the response data into a pandas DataFrame
data = pd.DataFrame.from_dict(response.json()['Time Series (Daily)'], orient='index').astype(float)

# Convert the index to a datetime format
data.index = pd.to_datetime(data.index)

# Sort the data by date
data = data.sort_index()

# Define the trading strategy
def simple_strategy(data):
    # Buy if the closing price is higher than the previous day's closing price
    if data["4. close"] > data.shift(1)["4. close"]:
        return 1
    # Sell if the closing price is lower than the previous day's closing price
    elif data["4. close"] < data.shift(1)["4. close"]:
        return -1
    # Hold otherwise
    else:
        return 0

# Apply the trading strategy to the data
data["signal"] = data.apply(simple_strategy, axis=1)

# Calculate the daily returns based on the trading signal
data["return"] = data["signal"] * data["5. adjusted close"].pct_change()

# Calculate the cumulative return
data["cumulative_return"] = (1 + data["return"]).cumprod()

# Print the cumulative return
print(f"Cumulative return for {symbol}: {data['cumulative_return'].iloc[-1]}")
