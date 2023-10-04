# Handling of Unicode characters - I bumped into this on working with degrees Celsius

# Regular expression handling
import re

# String with unicode character
test_string = " V1 latitude (°)"

print(test_string)

# See https://stackoverflow.com/questions/3215168/how-to-get-character-in-a-string-in-python
# See https://en.wikipedia.org/wiki/List_of_Unicode_characters
# There are many ways to represent unicode characters...
# I  think this is Python 2
degree_sign = "\N{DEGREE SIGN}"
degree_sign2 = "\u00b0"
# Python 3 should allow this
degree_sign3 = "\u00b0"


print("Degree character is:", degree_sign)
print("Degree character 2 is:", degree_sign2)
print("Degree character 3 is:", degree_sign3)

# Create regular expression
deg_re = re.compile(degree_sign)
# Substitute unicode degree character with string 'deg'
patched = deg_re.sub("deg", test_string)
print("Patch 1:", patched)

# Repeat the substitution - this time using the python3 unicode character
patched = re.sub("\u00b0", "deg", test_string)
print("Patch 2:", patched)

# Search returns a Match Object
match = re.search("\(.*\)", test_string)

if match:
    unit = match.group(0)
    print("Found match")
    print("Match is:", unit)
    patched_name = re.sub("\u00b0", "deg", unit)
    patched_name = re.sub("[()]", "", patched_name)
    unit = patched_name
    print("Unit is:", unit)
