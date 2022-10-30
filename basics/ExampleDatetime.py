"""
From realpython.com
This article explains more about this concept:
https://www.journaldev.com/22460/python-str-repr-functions

Both __str__ and __repr__ functions return string representation of the object.
The __str__ string representation is supposed to be human-friendly and mostly used
for logging purposes, whereas __repr__ representation is supposed to contain information
about object so that it can be constructed again. You should never use these
functions directly and always use str() and repr() functions.
"""

# When To Use __repr__ vs __str__?
# Emulate what the std lib does:
from datetime import datetime, date, timedelta
import time

today = date.today()

# Result of __str__ should be readable:
print(f"1: {str(today)}")

# Result of __repr__ should be unambiguous:
# >>> repr(today)
# 'datetime.date(2017, 2, 2)'
print(f"2: {repr(today)}")

# Python interpreter sessions use
# __repr__ to inspect objects:
# >>> today
# datetime.date(2017, 2, 2)

# Get epoch timestamp from date back in time
current_time = time.time()
print(f'current_time={current_time}')
nb_days_time = timedelta(days=3).total_seconds()
print(f'nb_days_time={nb_days_time}')
from_time = current_time - nb_days_time
print(f'from_time={int(from_time)}')

# Work with dates
from_date = datetime.today()
from_date_reset = from_date.replace(hour=0, minute=0, second=0, microsecond=0)
from_date_adjusted = from_date_reset - timedelta(days=3)

from_time_date = time.mktime(from_date_adjusted.timetuple())
print(f'from_time_date={from_time_date}')
