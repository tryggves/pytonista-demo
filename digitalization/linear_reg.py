#
# Linear regression example
#

import numpy as np
from sklearn.linear_model import LinearRegression

# Same array as 1 dimensional
x_tmp = np.array([5, 15, 25, 35, 45, 55])
print(f"x_tmp={x_tmp}")
# Flip the array into 2 dimensional with 1 column and value in rows.
print("Flip the array into 2 dimensional with 1 column and value in rows.")
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(f"x={x}")
y = np.array([5, 20, 14, 32, 22, 38])
print(f"y={y}")

model = LinearRegression().fit(x, y)

# R^2 (R square)
r_sq = model.score(x, y)
print(f"Coefficiet of determination: {r_sq}")
# Print b0
print(f"Intercept: {model.intercept_}")
# Print b1
print(f"Slope: {model.coef_}")

print("*** DONE ***")
