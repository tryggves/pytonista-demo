# Here is a common way of making formatted output. there are numerous ways of 
# doing it with python.
#
# This example needs more work.
# See: https://www.w3schools.com/python/python_strings.asp

# What are the most useful features
# Strings contatenation
# Strings filtering including reqular expressions
# String input output.

multiline_text = """
Welcome to this multi line text that can be 
entered as a text bloc enclosed by three double quotes or three
single quotes.
"""

# Formatting strings - mixing parameters of various types
# Notice that year is an integer.
year = 2018
month = 'September'
month_oct = 'October'
year_2020 = 2020
print(f'Hello format string of {month} {year}')
# Here is another way to do the above:
formatText = "Hello format string of {} {}"
print(formatText.format(month_oct, year_2020))

# Print multi line text constant.
print(multiline_text)

# Print string in uppercase
print('UPPERCASE EXAMPLE:', month.upper())
# Lowercase ditto
print('lowercase example:', month.lower())

concatMnth = month + month_oct
print('Concatenated: ', concatMnth)

