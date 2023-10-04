# Pandas DataFrame examples
# See: https://www.w3resource.com/python-exercises/pandas/datetime/pandas-datetime-exercise-9.php
# See: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

import pandas as pd


data = {"col1": [1, 4, 5, 6], "col2": [324, 324, 2, 23], "col3": [324, 32, 7, 374]}

print(data)

# Default index is 0, 1, 2,...
df = pd.DataFrame(data)
print(df.to_string())

# Here the list r1,... is the index
df2 = pd.DataFrame(data, index=["r1", "r2", "r3", "r4"])
print(df2.to_string())

# iloc[] access Dataframes based on numeric index
# .iloc[] returns a Series
p_series = df2.iloc[0]
print(p_series)

# this .iloc[] pics the element in row 0, column 1
p_element = df2.iloc[0, 1]
print(p_element)

# .iloc[[]] returns a DataFrame
p_df = df2.iloc[[0]]
print(f"Dataframe row:\n{p_df.to_string()}")

print(f"Dataframe slice iloc 2 first rows:\n{df.iloc[:2]}")
# Note that .loc is the index value rather than the row position
print(f"Dataframe slice loc[0:3] rows:\n{df.loc[0:3]}")
print(f"Dataframe slice loc[1:3] rows:\n{df.loc[1:3]}")
a = df.loc[0:3, "col1"]
print(f"Dataframe single column:\n{a}")

# Get rows based on boolean index mask
a = df.loc[[True, False, False, True]]
print(f"Dataframe slice loc[[True, False, False, True]] rows:\n{a.to_string()}")
# Using boolean list
print(
    f"Dataframe slice loc[[True, False, False, True]] rows:\n{df.loc[[True, False, False, True]]}"
)
