import pandas as pd
import numpy as np
from typing import Union, List


def get_portfolio_std(covariance_matrix, returns: pd.DataFrame, weights: Union[List, None] = None) -> float:
    '''
    Returns the portfolio standard deviation
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

    # Calculate the portfolio std using matrix multiplication operation
    portfolio_std = np.sqrt(np.dot(weights.T, np.dot(covariance_matrix, weights)))
    # Return the portfolio std as float
    return float(portfolio_std)