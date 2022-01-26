# Cleaning Pandas data frame objects
# Efficiency, vectorized operations
#
# https://realpython.com/python-data-cleaning-numpy-pandas/#combining-str-methods-with-numpy-to-clean-columns
# https://python.plainenglish.io/pandas-how-you-can-speed-up-50x-using-vectorized-operations-d6e829317f30
import numpy as np
import pandas as pd
import time


def standard_scaler_iterrows(pandas_dataframe: pd.DataFrame, mean_pandas_series: float,
                             std_pandas_series: float) -> pd.DataFrame:
    """
    Iterate through rows of Pandas DataFrame and do the standard scaler calculation row by row.
    VERY INEFFICIENT.
    :param pandas_dataframe:
    :param mean_pandas_series:
    :param std_pandas_series:
    :return:
    """
    for index, row in pandas_dataframe.iterrows():
        pandas_dataframe['scaled_random_numbers_2'] = (row['random_numbers_2'] - mean_pandas_series) / std_pandas_series

    return pandas_dataframe


def standard_scaler_apply(pandas_series: pd.Series,  mean_pandas_series: float,
                             std_pandas_series: float) -> pd.Series:
    """
    User pd.Series.apply() function to map through Pandas Series.
    Have to pass additional arguments through args =  ()

    :param pandas_series:
    :param mean_pandas_series:
    :param std_pandas_series:
    :return:
    """
    scaled_pandas_series = (pandas_series - mean_pandas_series) / std_pandas_series
    return scaled_pandas_series


# %%
# Create 3 data series each containing 100 mill elements
np.random.seed(42)
random_numbers_1 = np.random.randint(10e1, size=100000000)
random_numbers_2 = np.random.randint(10e2, size=100000000)
random_numbers_3 = np.random.randint(10e3, size=100000000)

# And put those in a pandas DataFrame
data_df = pd.DataFrame({'random_numbers_1': random_numbers_1,
                        'random_numbers_2': random_numbers_2,
                        'random_numbers_3': random_numbers_3})

print(data_df.info)

# %%time

# Calculate mean and standard deviation of column random_numbers_2
mean_pandas_series = np.mean(data_df['random_numbers_2'])
std_pandas_series = np.std(data_df['random_numbers_2'])

print(f'Mean: {mean_pandas_series}, Std: {std_pandas_series}')

# This call will take extremely long to execute
# data_df = standard_scaler_iterrows(pandas_dataframe=data_df, mean_pandas_series=mean_pandas_series,
#                                   std_pandas_series=std_pandas_series)
# print(data_df.info)

# This call will calculate on all elements of a column using apply() function
t_start = time.time()
data_df['scaled_random_numbers_2'] = data_df['random_numbers_2'].apply(standard_scaler_apply,
                                                                       args=(mean_pandas_series, std_pandas_series))
t_end = time.time()
print(data_df.info)
print(f'Duration: {t_end-t_start}')
