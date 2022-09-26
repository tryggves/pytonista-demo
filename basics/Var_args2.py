#
# Examples showing unwrapping using the asterisk and double
# asterisk operator.
#
# Reference:
# https://realpython.com/python-kwargs-and-args/
# https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/
#
my_list = [1, 2, 3]
print(f'my_list is {my_list}')

# Unpacking list with the * operator
# Cannot use f-string with unpack
# print(f'my list is {*my_list}')
# The output is no longer the list itself, but rather the content of the list
print(*my_list)
# Above print() has taken three separate arguments as the input
# Equivalent to:
print(1, 2, 3)


def sum_three_numbers(a, b, c):
    return a + b + c


# This unpacks my_list to parameters a, b, c
print(sum_three_numbers(*my_list))

# Unpack dictionary
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(f'my_merged_dict is {my_merged_dict}')
# This prints the dictionary keys
print('Dictionary keys')
print(*my_merged_dict)
# This prints the dictionary values
print('Values')
print(*my_merged_dict.values())

# experimental = [**my_first_dict]
# experimental = list(*my_first_dict)
print('Experiment with unwrapping')
print(*my_merged_dict)
# experimental is a list of keys from my_merged_dict
experimental = [*my_merged_dict]
print(experimental)
print(*experimental, sep=';')
print(*experimental, sep=' \\\n')

