# Pandas Timestamp example
# See: https://www.w3resource.com/python-exercises/pandas/datetime/pandas-datetime-exercise-9.php
# See: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html

from datetime import datetime
from cognite.client import CogniteClient
import cognite.client.exceptions
import os
import time
import json
import numbers
import pandas as pd
import numpy as np
from typing import List, Dict

import pandas as pd
import datetime as dt
import numpy as np

# Map protobuf Iongeo.vessel_turn.ArcType to integers
arc_type_map = {
    "ANTICLOCKWISE": -1,
    "STRAIGHT": 0,
    "CLOCKWISE": 1
}



def make_columns_map(vessel: str, source: str) -> Dict[str, str]:
    """map field name in json file to external ID used by CDF"""
    return {
        "is_arc": f"{vessel}_{source}_IS_ARC",
        "arc_type": f"{vessel}_{source}_TURN_SENSE",
        "turn_radius": f"{vessel}_{source}_TURN_RADIUS",
    }


def read_data_from_file(name) -> List[Dict]:
    """Used for unit testing, read data from file system instead of bucket"""
    with open(name, "r") as turn_json_file:
        return json.loads(turn_json_file.read())


def build_dataframe(rows: List[Dict], columns_map: Dict[str, str]) -> pd.DataFrame:
    """create dataframe from json records
    on format expected by CDF with timestamp as index and timeseries external ID as column names
    """
    df = pd.DataFrame.from_dict(rows)
    # Convert the timestamps from RFC 3339 strings to milliseconds since epoch and rename
    # column to timestamp
    df["time_stamp"] = pd.to_datetime(df.time_stamp.values)
    df["time_stamp"] = df.time_stamp.values.astype(np.int64) // 10**6
    df.rename(columns={'time_stamp': 'timestamp'}, inplace=True)
    df.set_index("timestamp", inplace=True)

    # Convert is_arc true/false to 1/0 values
    df["is_arc"] = df.is_arc.values.astype(int)

    # Convert arc_type to numerical value

    # Rename the columns to be ingested with external id names
    df = df[df.columns.intersection(list(columns_map.keys()))].rename(columns=columns_map)

    # df["timestamp"] = df.timestamp.astype(np.int64)
    # df.set_index("timestamp", inplace=True)
    # df = df[df.columns.intersection(list(columns_map.keys()))].rename(columns=columns_map) # type: ignore
    return df


# Construct a timestamp with RFC 3339 string
pd_timestamp = pd.Timestamp("2020-04-29T00:01:00.000500Z")
print(pd_timestamp)
# Convert timestamp to datetime
ts_epoc = pd.to_datetime(pd_timestamp, unit='ms', origin='unix')
print(ts_epoc.value)
print(ts_epoc.value // 10**6)

# Convert string to datetime
ts_epoc2 = pd.to_datetime("2020-04-29T00:01:00.000500Z")
print(ts_epoc2.value // 10**6)
