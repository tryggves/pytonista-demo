# Pandas Timestamp example
# See: https://www.w3resource.com/python-exercises/pandas/datetime/pandas-datetime-exercise-9.php
# See: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

import numpy as np
import pandas as pd

# Map protobuf Iongeo.vessel_turn.ArcType to integers
arc_type_map = {"ANTICLOCKWISE": -1, "STRAIGHT": 0, "CLOCKWISE": 1}


def apply_map_on_column():
    arc_type_data = {
        "timestamp": [100, 101, 102, 103],
        "arc_type": ["ANTICLOCKWISE", "STRAIGHT", "STRAIGHT", "CLOCKWISE"],
    }
    at_df = pd.DataFrame(arc_type_data)
    print("=== arc_type dataframe =================================")
    print(at_df.to_string())
    print(at_df.dtypes)

    # Convert column arc_type values to int map - this iterates over all
    # values in the column (nice feature)
    # Parameter x to expression is the value of dataframe column arc_type
    at_df.arc_type = at_df.arc_type.apply(lambda x: arc_type_map[x])
    print("=== after applying arc_type_map ========================")
    print(at_df.to_string())
    print(at_df.dtypes)


# Construct a timestamp with RFC 3339 string
pd_timestamp = pd.Timestamp("2020-04-29T00:01:00.000500Z")
print(pd_timestamp)
# Convert timestamp to datetime
ts_epoc = pd.to_datetime(pd_timestamp, unit="ms", origin="unix")
print(ts_epoc.value)
print(ts_epoc.value // 10**6)

# Convert string to datetime
ts_epoc2 = pd.to_datetime("2020-04-29T00:01:00.000500Z")
print(ts_epoc2.value // 10**6)

# Create a data frame from a dictionary
data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

print("=== df ==============================")
print(df)

# Apply a function to all elements in dataframe
new_df = df.apply(lambda x: x**2, axis=1)
print("== Square of all elements in df ... ========================")
print(new_df)

# Axis 0 is the vertical axis, hence all columns are summed
new_df = df.apply(np.sum, axis=0)
print("== Sum of columns (axis=0) ... ========================")
print(new_df)

# Axis 1 is the horizontal axis, hence all rows are summed
new_df = df.apply(np.sum, axis=1)
print("== Sum of rows (axis=1) ... ========================")
print(new_df)

# Apply function on one column only
# NOtE: you can refer to a full column by subscripting dataframe with column name
df.a = df.a.apply(lambda x: x + 3)
print("== After applying to column a on df ===================")
print(df)

apply_map_on_column()
