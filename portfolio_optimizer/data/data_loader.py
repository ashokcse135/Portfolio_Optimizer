import os
import pandas as pd
from datetime import datetime

from typing import List, Union

from portfolio_optimizer.constants import NIFTY50_URL, RAW_DATA_DIRECTORY
from portfolio_optimizer.data.yfinance_data import download_stock_data


def get_nifty50_companies(path = None) -> pd.DataFrame:
    '''
    Returns a dataframe of Nifty50 companies
    '''
    url = NIFTY50_URL
    df = pd.read_csv(url)
    # Add company ticker column for yfinance
    df["Ticker"] = df["Symbol"] + ".NS"
    if path:
        df.to_csv(path)
    return df


def get_nifty50_OHLCV(tickers: Union[List[str], None] = None, period = "5y", interval = "1mo", path = None) -> pd.DataFrame:
    if tickers is None:
        tickers = get_nifty50_companies()["Ticker"].tolist()
    if path:
        df.to_csv(path)
    else:
        file_path = os.path.join(RAW_DATA_DIRECTORY, f"nifty50_OHLCV_{period}_{interval}.csv")
        # Check if the file exists and is recent
        if os.path.exists(file_path) and (datetime.now() - datetime.fromtimestamp(os.path.getmtime(file_path))).days < 25:
            df = pd.read_csv(file_path, index_col=0, header=[0,1], parse_dates=True)
            print(f"Using cached data from {file_path}")
        else:
            df = download_stock_data(tickers = tickers, period = period, interval = interval)
            # Create the RAW_DATA_DIRECTORY if it doesn't exist
            if not os.path.exists(RAW_DATA_DIRECTORY):
                os.makedirs(RAW_DATA_DIRECTORY)
            df.to_csv(file_path)
    return df
