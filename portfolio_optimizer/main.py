from portfolio_optimizer.data.yfinance_data import download_stock_data, get_ticker_info

# Example: Download historical data for Apple and Microsoft
tickers = ["TCS.NS", "INFY.NS"]
start_date = "2020-01-01"
end_date = "2025-03-12"
interval = "1mo" # 1 month

data = download_stock_data(tickers, start_date, end_date, interval)
print(data.tail())

# Example: Get metadata for Apple
ticker_info = get_ticker_info("TCS.NS")
print(ticker_info)