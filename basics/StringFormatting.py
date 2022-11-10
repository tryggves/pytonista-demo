# Here is a common way of making formatted output. there are numerous ways of 
# doing it with python.
#
# This example needs more work.
# See: https://www.w3schools.com/python/python_strings.asp

# String formatting
# https://realpython.com/python-formatted-output/#the-string-format-method-arguments

# String interpolation is the method of replacing placeholders with actual input at
# runtime when generating or outputting strings
# https://www.programiz.com/python-programming/string-interpolation

# What are the most useful features
# Strings contatenation
# Strings filtering including reqular expressions
# String input output.
# String interpolation
# Raw strings

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

print("\nF-string formatting introduced in version 3.6")
print(f'Hello format string of {month} {year}')
print(f'Hello format string of {month_oct} {year_2020}')


# Using the % operator
print('\nTry out the % operator')
print('year is %d' % year)
# The % operator takes one parameter, hence the tuple containing the variables
print('year is %d. month is %s' % (year, month))
print('year is %d. month is %s. mont_oct is %s' % (year, month, month_oct))

# Replacement field format:
# {[<name>][!<conversion>][:<format_spec>]}
# conversion is not much used in practice

print("\nUsing str.format")
# Field format with <name> using str.format and F-string
formatText1 = "Hello format string of {} {}"
print(formatText1.format(month_oct, year_2020))
print(f'Hello format string of {month_oct} {year_2020}')
formatText2 = "Hello format string of {0} {1}"
print(formatText2.format(month, year))
print(f'Hello format string of {month} {year}')
formatText3 = "Hello format string of {month} {year}"
print(formatText3.format(month=month_oct, year=year_2020))
print(f'Hello format string of {month_oct} {year_2020}')

# Access dictionary elements from replacement fields.
my_dict = {
    'first_name': 'Tryggve',
    'age': 59
}
formatText4 = "{d[first_name]}'s age is {d[age]}"
print(formatText4.format(d=my_dict))
print(f'{my_dict["first_name"]}\'s age is {my_dict["age"]}')
print(f"{my_dict['first_name']}'s age is {my_dict['age']}")

print("\nPrint multi line text constant.")
print(multiline_text)

# Print string in uppercase
print('UPPERCASE EXAMPLE:', month.upper())
# Lowercase ditto
print('lowercase example:', month.lower())

concatMnth = month + month_oct
print('Concatenated: ', concatMnth)

# Formatting numbers
squares_lc_2 = [i*i for i in range(10) if i > 5]
print(f'Before formatting: {squares_lc_2}')
for num in squares_lc_2:
    print(f'{num:.2f}')
print(f'Print with 2 decimals:[', end='')
for num in squares_lc_2:
    print(f'{num:.2f}', end='')
    print(', ', end='')
print(']')

# Raw strings are prefixed with character 'r'
print('\nRaw string example')
print(r'This is a raw string \n where \ is not an escape character')
print('This is not a raw string \n where \\ is treated as escape character')

