#
# Examples of map(), filter(), reduce()
# List comprehension
#

import functools
import math
import operator
import os.path

################################################################################
################################################################################
# Map example 1. Create a list and perform a function on each element of the list
print("Map example 1")
in_list = [1, 2, 3, 4, 5]
# map() returns an iterator of the result of applying the function on the in_list
res_iter = map(lambda x: x * 2, in_list)
res_list = list(res_iter)
print(res_list)


################################################################################
# Map example 2. Create a custom function to be applied in the map
def my_func(x):
    return x + 10


print("Map example 2")
# This is the typical pattern where the result list is created from the map iterator
res_list = list(map(my_func, in_list))
print(res_list)

################################################################################
# Example 3: Crete numbers from strings
print("Map example 3")
res_list = list(map(float, ["12.2", "4.456", "5"]))
print(res_list)


################################################################################
# Example 4: Numbers from strings with possible errors
# Define custom function
def to_float(x: str):
    try:
        return float(x.replace(',', '.'))
    except ValueError:
        return float("nan")


print("Map example 4")
my_numbers = ["10,8", "58", "realli not a number"]

res_list = list(map(to_float, my_numbers))
print(res_list)


################################################################################
# Example 5: Map and filter function
# filter() applies a predicate (true,false) function on the iterable
def is_positive(num):
    return num >= 0


def sanitized_sqrt(numbers):
    # cleaned_iter = map(math.sqrt, filter(is_positive, numbers))
    # Use lambda expression in filter()
    cleaned_iter = map(math.sqrt, filter(lambda num: num >= 0, numbers))
    return list(cleaned_iter)


print("Map and filter example 5")
res_list = sanitized_sqrt([25, 9, 81, -16, 0])
print(res_list)


#####################################################################################
# Example 6: Map and reduce() function
# Reduce aggregates values from the list/iterator returned by map
print("Map and reduce example 6")
home_dir = os.path.expanduser("~")
files_dirs = os.listdir(home_dir)
files = list(map(lambda file_name: home_dir + "/" + file_name, files_dirs))
aggregate_size = functools.reduce(operator.add, map(os.path.getsize, files))
print(f'Aggregate size is {aggregate_size}')


#####################################################################################
# Example 7: List comprehension

# Here we generate a list using map funcion
print("Map list")
res_list = list(map(to_float, my_numbers))
print(res_list)

print("List comprehension list")
# Here is the same using list comprehension
lc_list = [to_float(x) for x in my_numbers]
print(lc_list)

my_numlist = list(range(10))            # range() is an iterator
print(my_numlist)

my_second_range = range(10, 20)
for x in my_second_range:
    print(f'x+2={x + 2}')

#####################################################################################
# Generator expressions return iterators as map() does
print("Generator expression")
gen_list = list(to_float(x) for x in my_numbers)
print(gen_list)

# This shows that the generator expression returns an iterator. In this
# case it is used in the loop examples below. The for loop is the easiest
# to understand.
gen_iterator = (to_float(x) for x in my_numbers)
num = next(gen_iterator)
while num is not None:
    print(f'num={num}')
    try:
        num = next(gen_iterator)
    except StopIteration:
        break

# Note! The iterator is exhausted by the while loop above, it has to be
# re-initialized for the for-loop to work.
gen_iterator = (to_float(x) for x in my_numbers)
for num in gen_iterator:
    print(f'num={num}')
