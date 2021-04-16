# From realpython.com

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
