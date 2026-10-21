import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    XT = X.T
    A = XT @ X
    A_inv = np.linalg.inv(A)
    b = XT @ y

    theta = A_inv @ b

    return [round(value, 4) for value in theta]
