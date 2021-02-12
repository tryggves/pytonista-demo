# Lambda expression examples
#
# Then some training on using map() function
#
# https://realpython.com/python-lambda/
# https://realpython.com/python-map-function/
# https://realpython.com/python-reduce-function/
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

# Try this out with lambda expression - this is not a best practice.
# The lambda expression here makes it harder to read.
print('Example with lambda')
print(f'3 square is {(lambda x: x**2)(3)}')
print(f'4 square is {(lambda x: x**2)(4)}')
for i in range(10):
    print(f'sqr({i})={my_sqr(i)}')

# Passing varargs
print(f'varargs {(lambda *args: sum(args))(1,2,3)}')
# Passing kwargs (keyword arguments)
print(f'kwargs {(lambda **kwargs: sum(kwargs.values()))(en=1, to=2, tre=3)}')

# Unsure about the second argument
print(f'Argument ex 1: {(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)}')
print(f'Argument ex 2: {(lambda x, y=0, z=0: x + y + z)(1, y=2, z=3)}')
# This does not work
# print((lambda x, *, y=0, z=0: x + y + z)(1, 2, 3, y=4, z=5))
print(f'Argument ex 3: {(lambda u, v, y=0, z=0: u + v + y + z)(1, 2, y=4, z=5)}')


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
