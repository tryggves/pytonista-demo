# Handling of Unicode characters - I bumped into this on working with degrees Celsius

# Regular expression handling
import re

test_string = " V1 latitude (°)"

print(test_string)

# See https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python
# See https://en.wikipedia.org/wiki/List_of_Unicode_characters
# There are many ways to represent unicode characters...
# I  think this is Python 2
degree_sign = u'\N{DEGREE SIGN}'
degree_sign2 = u"\u00b0"
# Python 3 should allow this
degree_sign3 = '\u00b0'


print("Degree sign is:", degree_sign)
print("Degree sign 2 is:", degree_sign2)
print("Degree sign 3 is:", degree_sign3)

deg_pattern = re.compile(degree_sign)
patched = deg_pattern.sub('deg', test_string)
print("Patch 1:", patched)

patched = re.sub('\u00b0', 'deg', test_string)
print("Patch 2:", patched)

# Search returns a Match Object
match = re.search("\(.*\)", test_string)

if match:
    unit = match.group(0)
    print("Found match")
    print("Match is:", unit)
    patched_name = re.sub('\u00b0', 'deg', unit)
    patched_name = re.sub('[()]', '', patched_name)
    unit = patched_name
    print("Unit is:", unit)

