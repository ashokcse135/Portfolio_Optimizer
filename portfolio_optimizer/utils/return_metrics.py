import pandas as pd
import numpy as np

from typing import Union, List


def get_returns(prices: pd.DataFrame) -> pd.DataFrame:
    '''
    Returns a dataframe with returns
    '''
    # Order the dataframe by date
    prices = prices.sort_index()
    # Calculate returns
    returns = prices.pct_change().dropna()
    # Create a new datarame with returns
    returns = pd.DataFrame(returns)
    
    return returns

def get_log_returns(prices: pd.DataFrame) -> pd.DataFrame:
    '''
    Returns a dataframe with log returns
    '''
    # Order the dataframe by date
    prices = prices.sort_index()
    # Calculate log returns
    log_returns = np.log(prices / prices.shift(1)).dropna()
    # Create a new datarame with log returns
    log_returns = pd.DataFrame(log_returns)
    
    return log_returns

    '''
    Returns a dataframe with cumulative returns
    '''
    # Calculate cumulative returns
    cumulative_returns = prices.pct_change().cumsum()
    # Create a new datarame with cumulative returns
    cumulative_returns = pd.DataFrame(cumulative_returns)
    
    return cumulative_returns

def get_portfolio_return(returns: List, weights: Union[List, None] = None) -> float:
    '''
    Returns the portfolio return
    returns : List of returns as a column vector
    weights : List of weights as a column vector
    '''
    returns = np.array(returns).reshape((len(returns), 1))
    if weights is None:
        # If weights are not provided, use equal weights for all assets i.e., 1/total_num_assets
        weights = (np.ones(returns.shape[0]) / returns.shape[0]).reshape((returns.shape[0], 1))
    else:
        weights = np.array(weights).reshape((len(weights), 1))
    # Check if the weights and returns have the same shape
    if weights.shape != returns.shape:
        raise ValueError("Weights and returns must have the same shape")
    return float(np.sum(returns * weights))


def get_mean_returns(data: pd.DataFrame) -> np.ndarray:
    return data.mean(axis=0)

