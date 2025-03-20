import numpy as np
import cvxpy as cp


import cvxpy as cp
import numpy as np
from typing import Union

class MeanVariancePortfolioOptimizer:
    def __init__(self, mean_returns: np.ndarray, cov_matrix: np.ndarray):
        """
        Initialize the portfolio optimizer.

        :param mean_returns: Expected returns (array of shape [num_assets])
        :param cov_matrix: Covariance matrix (array of shape [num_assets, num_assets])
        """
        self.mean_returns = mean_returns.reshape(-1, 1)
        self.num_assets = len(mean_returns)
        self.cov_matrix = cov_matrix.reshape(self.num_assets, self.num_assets)
        

    def optimize(self, objective: str, constraints: list = [], params: Union[dict, None] = None) -> np.ndarray:
        """
        Solve the portfolio optimization problem.

        :param objective: Objective function to use (e.g. 'min_volatility', 'max_return', 'sharpe_ratio', 'etc.)
        :param constraints: List of constraints to apply (e.g. ['long_only', 'required_return', etc.])
        :param params: Dictionary of parameters for the objective function and constraints
        :return: Optimized portfolio weights
        """
        w = cp.Variable(self.num_assets)

        possible_objectives = ['min_volatility', 'max_return', 'sharpe_ratio']

        # Define the objective function
        if objective == 'min_volatility':
            objective_func = cp.Minimize(cp.quad_form(w, self.cov_matrix))
        elif objective == 'max_return':
            objective_func = cp.Maximize(self.mean_returns.T @ w)
        elif objective == 'sharpe_ratio':
            risk_free_rate = params['risk_free_rate']
            # An optimizer friendly version of the Sharpe ratio
            objective_func = cp.Maximize((self.mean_returns - risk_free_rate).T @ w - 0.5 * cp.quad_form(w, self.cov_matrix))
        else:
            raise ValueError(f"Unsupported objective function. Possible values are {possible_objectives}")

        # Define the constraints
        possible_constraints = ['long_only', 'required_return']
        constraints_list = []
        for constraint in constraints:
            if constraint == 'long_only':
                constraints_list.append(w >= 0)
            elif constraint == 'required_return':
                constraints_list.append(self.mean_returns.T @ w >= params['required_return'])
            else:
                raise ValueError("Unsupported constraint")

        # Add Invest the total capital constraint
        constraints_list.append(cp.sum(w) == 1)

        # Solve the optimization problem
        problem = cp.Problem(objective_func, constraints_list)
        problem.solve()

        if problem.status not in ["optimal", "optimal_inaccurate"]:
            raise ValueError("Optimization problem did not converge!")

        return w.value


def mean_variance_optimization(mean_returns: np.ndarray, cov_matrix: np.ndarray) -> np.ndarray:
    """
    Solve the Mean-Variance Optimization problem to find the minimum variance portfolio.

    :param mean_returns: Expected returns (array of shape [num_assets])
    :param cov_matrix: Covariance matrix (array of shape [num_assets, num_assets])
    :return: Optimized portfolio weights
    """
    num_assets = len(mean_returns)
    w = cp.Variable(num_assets)

    # Objective: Minimize portfolio variance (w' Σ w)
    objective = cp.Minimize(cp.quad_form(w, cov_matrix))

    # Constraints: Weights sum to 1, no short-selling
    constraints = [
        cp.sum(w) == 1,
        w >= 0 # No short-selling constraint
    ]

    # Solve optimization problem
    problem = cp.Problem(objective, constraints)
    problem.solve()

    if problem.status not in ["optimal", "optimal_inaccurate"]:
        raise ValueError("Optimization problem did not converge!")

    return w.value