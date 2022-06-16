# Pandas dataframes and pivot operations
#
# See: https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping

import pandas as pd
import numpy as np
import pandas._testing as tm


def unpivot(frame):
    N, K = frame.shape
    data = {
        "value": frame.to_numpy().ravel("F"),
        "variable": np.asarray(frame.columns).repeat(N),
        "date": np.tile(np.asarray(frame.index), K),
    }
    return pd.DataFrame(data, columns=["date", "variable", "value"])


# df is a DataFrame containing some values for some variables
df = unpivot(tm.makeTimeDataFrame(3))
print("=== Starting dataframe ===")
print(df)

# Get all data for variable A
filtered = df[df["variable"] == "A"]
print("=== Filtered dataframe ===")
print(filtered)

# Using pivot to organize DataFrame for working with time series
pivoted = df.pivot(index="date", columns="variable", values="value")
print("=== Pivoted ===")
print(pivoted)
