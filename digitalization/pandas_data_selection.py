#
# Basic pandas data selection examples.
# https://pandas.pydata.org/docs/user_guide/indexing.html
#

import pandas as pd
import numpy as np

# Create a list (1-d array of 8 dates)
dates = pd.date_range("1/1/2000", periods=8)

# Create 8 rowx , 4 columns array of samples from standard normal distribution
np_array = np.random.randn(8, 4)

df = pd.DataFrame(np_array, index=dates, columns=["A", "B", "C", "D"])

print(df)
