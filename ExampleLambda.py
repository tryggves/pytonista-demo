# Lambda expression examples
#
# https://realpython.com/python-lambda/
# https://realpython.com/python-map-function/
#
# Lambda expression contains:
# keyword "lambda"
# Any number of arguments
# ":"
# Expression with result returned

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
for i in range(3):
    closure = outer_func(i)
    # this in effect calls inner_func(i+5) (parameter z value becomes i+5)
    print(f"closure({i+5}) = {closure(i+5)}")
