# Lambda expression examples
#
# Then some training on using map() function
#
# https://realpython.com/python-lambda/
# https://realpython.com/python-map-function/
# https://realpython.com/python-reduce-function/
#
# Lambda expression contains:
# 1) keyword "lambda"
# 2) Any number of arguments
# 3) ":"
# 4) Expression with result returned

# !!!! Bad practice !!!
f = lambda a: a + 10

# Variable f has been assigned the object containing a lambda function
print(f(5))

# Enclose lambda expression in parentheses and it can be executed by passing parameter
print((lambda b: b * 10)(50))
print((lambda u, v: u + v)(3, 5))


# Define a function
def my_sqr(x):
    return x**2


print("====== Example with function.")
print(f"3 square is {my_sqr(3)}")
print(f"4 square is {my_sqr(4)}")

# Try this out with lambda expression - this is not a best practice.
# The lambda expression here makes it harder to read.
print("====== Example with lambda")
print(f"3 square is {(lambda x: x**2)(3)}")
print(f"4 square is {(lambda x: x**2)(4)}")
for i in range(10):
    print(f"sqr({i})={my_sqr(i)}")

print("====== Passing varargs")
print(f"varargs {(lambda *args: sum(args))(1,2,3)}")
print("# Passing kwargs (keyword arguments")
print(f"kwargs {(lambda **kwargs: sum(kwargs.values()))(en=1, to=2, tre=3)}")

# Unsure about the second argument
print(f"Argument ex 1: {(lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3)}")
# Could the second argument be positional? Yes, but you have to name the variable to ref it in the expression
print(f"Argument ex 1b: {(lambda x, *args, y=0, z=0: x + sum(args) + y + z)(1, 4, 5, y=2, z=3)}")
print(f"Argument ex 2: {(lambda x, y=0, z=0: x + y + z)(1, y=2, z=3)}")
# This does not work
# print((lambda x, *, y=0, z=0: x + y + z)(1, 2, 3, y=4, z=5))
print(f"Argument ex 3: {(lambda u, v, y=0, z=0: u + v + y + z)(1, 2, y=4, z=5)}")


#######################################################################################
# Function that returns the call of a lambda expression depending
# on the given operation parameter and the two arguments. Pretty
# neat example.


# get() method gets the dictionary element given by operation (add, sub, etc),
# in this case the lambda expression.
# If the operation does not exist the lambda: None is returned
# Note the ending () which calls the returned lambda function
def dispatch_dict(operation, x, y):
    return {
        "add": lambda: x + y,
        "sub": lambda: x - y,
        "mul": lambda: x * y,
        "div": lambda: x / y,
    }.get(operation, lambda: None)()


print("=== Run operation from dictionary of operations")
print(f"1+2={dispatch_dict('add', 1, 2)}")
print(f"2-1={dispatch_dict('sub', 2, 1)}")
print(f"2unknown1={dispatch_dict('unknown', 2, 1)}")


################################################################################
# Function returning another function - demonstrate the inner function
# becoming a closure:
# https://realpython.com/python-lambda/#python-lambda-and-regular-functions
# Free variable - everything expect parameters
# Bound variable - parameter
def outer_func(x):
    y = 4  # Variable inside function scope

    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z

    return inner_func


# For each iteration of the loop, closure is assigned the return of outer_func()
# called with the iteration value of i
print("=== CLOSURE WITH INNER FUNCTION DEF")
for i in range(3):
    closure = outer_func(i)
    # this in effect calls inner_func(i+5) (parameter z value becomes i+5)
    print(f"closure({i+5}) = {closure(i+5)}")


# Doing the same with lambda
def outer_func_l(x):
    y = 4
    return lambda z: x + y + z


print("=== CLOSURE WITH INNER LAMBDA EXPRESSION")
for ii in range(3):
    closure = outer_func_l(ii)
    print(f"closure({ii + 5}) = {closure(ii + 5)}")
