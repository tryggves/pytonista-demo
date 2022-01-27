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


def standard_scaler_map(pandas_element: int, mean_pandas_series: float,
                             std_pandas_series: float) -> float:
    """
    Use pd:Series.map() to map through the elements in Pandas Series
    :param pandas_element:
    :param mean_pandas_series:
    :param std_pandas_series:
    :return:
    """
    scaled_pandas_element = (pandas_element - mean_pandas_series) / std_pandas_series
    return scaled_pandas_element


def standard_scaler_vectorized_series(pandas_series: pd.Series) -> pd.Series:
    """
    Vectorized operation across Pandas Series
    :param pandas_series:
    :return:
    """
    scaled_series = (pandas_series - np.mean(pandas_series)) / np.std(pandas_series)
    return scaled_series


def standard_scaler_vectorized_array(numpy_array: np.array) -> np.array:
    """
    Vectorized operation across Numpy arrays
    :param numpy_array:
    :return:
    """
    scaled_array = (numpy_array - np.mean(numpy_array)) / np.std(numpy_array)
    return scaled_array


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

# ===================================================================
# Calculate mean and standard deviation of column random_numbers_2
mean_pandas_series = np.mean(data_df['random_numbers_2'])
std_pandas_series = np.std(data_df['random_numbers_2'])

print(f'Mean: {mean_pandas_series}, Std: {std_pandas_series}')

# ===================================================================
# This call will take extremely long to execute
# data_df = standard_scaler_iterrows(pandas_dataframe=data_df, mean_pandas_series=mean_pandas_series,
#                                   std_pandas_series=std_pandas_series)
# print(data_df.info)

# ===================================================================
# This call will calculate on all elements of a column using apply() function
# print(f'Use standard_scaler_apply()...')
# t_start = time.perf_counter()
# data_df['scaled_random_numbers_2'] = data_df['random_numbers_2'].apply(standard_scaler_apply,
#                                                                        args=(mean_pandas_series, std_pandas_series))
# t_end = time.perf_counter()
# print(data_df.info)
# print(f'Duration: {t_end-t_start:0.4f} seconds')

# ===================================================================
# This call will calculate on all elements of column using map() function
# print(f'Use standard_scaler_map()...')
# t_start = time.perf_counter()
# data_df['scaled_random_numbers_2'] = data_df['random_numbers_2'].map(lambda x: standard_scaler_map(x, mean_pandas_series=mean_pandas_series, std_pandas_series=std_pandas_series))
# t_end = time.perf_counter()
# print(data_df.info)
# print(f'Duration: {t_end-t_start:0.4f} seconds')

# ===================================================================
# This call will calculate on all elements of column using vectorized operation over Pandas Series
print(f'Use standard_scaler_vectorized_series()...')
t_start = time.perf_counter_ns()
data_df['scaled_random_numbers_2'] = standard_scaler_vectorized_series(data_df['random_numbers_2'])
t_end = time.perf_counter_ns()
# print(data_df.info)
duration = (t_end-t_start)/10e6
print(f'Duration: {duration:0.4f} milliseconds')


# ===================================================================
# This call will calculate on all elements of column using vectorized operation over Numpy array
print(f'Use standard_scaler_vectorized_array()...')
t_start = time.perf_counter_ns()
data_df['scaled_random_numbers_2'] = standard_scaler_vectorized_array(data_df['random_numbers_2'].values)
t_end = time.perf_counter_ns()
# print(data_df.info)
duration = (t_end-t_start)/10e6
print(f'Duration: {duration:0.4f} milliseconds')

