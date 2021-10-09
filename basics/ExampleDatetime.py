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
import datetime
today = datetime.date.today()

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
