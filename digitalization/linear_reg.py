#
# Linear regression example
#

import numpy as np
from sklearn.linear_model import LinearRegression

# Same array as 1 dimensional
x_tmo = np.array([5, 15, 25, 35, 45, 55])
# Flip the array into 2 dimensional with 1 column and value in rows.
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
print(x)
y = np.array([5, 20, 14, 32, 22, 38])
print(y)

model = LinearRegression().fit(x, y)

# R^2 (R square)
r_sq = model.score(x, y)
print(f'Coefficiet of determination: {r_sq}')
# Print b0
print(f'Intercept: {model.intercept_}')
# Print b1
print(f'Slope: {model.coef_}')

print('*** DONE ***')
