# Lambda expression examples
#
# Then some training on using map() function
#
# https://realpython.com/python-lambda/
# https://realpython.com/python-map-function/
#
# Lambda expression contains:
# keyword "lambda"
# Any number of arguments
# ":"
# Expression with result returned

import math
import functools
import operator
import os
import os.path

# !!!! Bad practice !!!
f = lambda a: a + 10

print(f(5))

# Enclose lambda expression in parentheses and it can be executed by passing parameter
print((lambda b: b * 10)(50))
print((lambda u, v: u + v)(3, 5))


# Define a function
def my_sqr(x):
    return x**2


print("Example with function.")
print(f'3 square is {my_sqr(3)}')
print(f'4 square is {my_sqr(4)}')

# Try this out with lambda expression
print('Example with lambda')
print(f'3 square is {(lambda x: x**2)(3)}')
print(f'4 square is {(lambda x: x**2)(4)}')

# Passing varargs
print(f'varargs {(lambda *args: sum(args))(1,2,3)}')
# Passing kwargs (keyword arguments)
print(f'kwargs {(lambda **kwargs: sum(kwargs.values()))(en=1, to=2, tre=3)}')

# Unsure about the second argument
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))
print((lambda x, y=0, z=0: x + y + z)(1, y=2, z=3))
# This does not work
# print((lambda x, *, y=0, z=0: x + y + z)(1, 2, 3, y=4, z=5))


################################################################################
# Function returning another function - demonstrate the inner function
# becoming a closure:
# https://realpython.com/python-lambda/#python-lambda-and-regular-functions
# Free variable - everything expect parameters
# Bound variable - parameter
def outer_func(x):
    y = 4       # Variable inside function scope

    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z

    return inner_func


# For each iteration of the loop, closure is assigned the return of outer_func()
# called with the iteration value of i
print("CLOSURE WITH INNER FUNCTION DEF")
for i in range(3):
    closure = outer_func(i)
    # this in effect calls inner_func(i+5) (parameter z value becomes i+5)
    print(f"closure({i+5}) = {closure(i+5)}")


# Doing the same with lambda
def outer_func_l(x):
    y = 4
    return lambda z: x + y + z


print("CLOSURE WITH INNER LAMBDA EXPRESSION")
for ii in range(3):
    closure = outer_func_l(ii)
    print(f"closure({ii + 5}) = {closure(ii + 5)}")
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