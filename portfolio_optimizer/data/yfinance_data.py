import yfinance as yf
import pandas as pd
from typing import List, Optional

def download_stock_data(
    tickers: List[str],
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    interval: str = "1d",
    period = None
) -> pd.DataFrame:
    """
    Download historical stock data from Yahoo Finance.

    Args:
        tickers (List[str]): List of stock tickers (e.g., ["AAPL", "MSFT"]).
        start_date (Optional[str]): Start date in YYYY-MM-DD format. If None, fetches data from the earliest available.
        end_date (Optional[str]): End date in YYYY-MM-DD format. If None, fetches data up to the current date.
        interval (str): Data interval. Options: "1d", "1h", "1m", etc. Default is "1d" (daily).
        period (Optional[str]): Period of data to fetch. If None, fetches data from start_date to end_date. 
                                Either period or start_date/end_date should be provided.

    Returns:
        pd.DataFrame: A DataFrame with historical stock data. Columns are MultiIndex with tickers as the first level.
    """
    try:
        if period:
            data = yf.download(
                tickers=tickers,
                period=period,
                interval=interval,
                group_by="ticker",
                progress=False,  # to disable the progress bar   
                auto_adjust=True # to fetch adjusted prices and volume
            )
        else:
            # Download OHLCV data along with Adjusted close price using yfinance
            data = yf.download(
                tickers=tickers,
                start=start_date,
                end=end_date,
                interval=interval,
                group_by="ticker",
                progress=False, # to disable the progress bar
                auto_adjust=True, # set it to False to fetch adjusted close price along with OHLCV 
            )
        
        # If only one ticker is provided, yfinance returns a DataFrame without MultiIndex columns.
        # We need to ensure the DataFrame always has MultiIndex columns for consistency.
        if len(tickers) == 1:
            data = pd.concat({tickers[0]: data}, axis=1)
        
        return data
    except Exception as e:
        print(f"Error downloading data: {e}")
        return pd.DataFrame()

def get_ticker_info(ticker: str) -> dict:
    """
    Get metadata and information about a specific ticker.

    Args:
        ticker (str): Stock ticker symbol (e.g., "AAPL").

    Returns:
        dict: A dictionary containing metadata about the ticker.
    """
    try:
        stock = yf.Ticker(ticker)
        return stock.info
    except Exception as e:
        print(f"Error fetching info for {ticker}: {e}")
        return {}


