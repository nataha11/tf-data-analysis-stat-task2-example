import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1283808304

def solution(p: float, x: np.array) -> tuple:
    eps = 1 - p
    n = len(x)
    x_max = x.max()
    eps_n = pow(eps, (1/n))
    return x_max, (x_max + 0.011*(eps_n - 1))/eps_n
