import numpy as np
import pandas as pd

def get_covariance_matrix(data: pd.DataFrame) -> np.ndarray:
    return data.cov()