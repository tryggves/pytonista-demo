# Examples using eval() function
#
# This follows the tutorial found here:
# https://realpython.com/python-eval-function/

# Define a global variable
x = 100
y = 200

print("=========================================================================================")
print("Example using eval() function")
print("=========================================================================================")

# First argument is string with the expression passed to eval()
# Second argument is dictionary of global variables, this makes it possible to access the variable
# x that is assigned at the start of this script.
# There is a third argument with local variables.
print(f'x + 100 is {eval("x + 100", {"x": x})}')

# This will result in runtime error
# result = eval("x + y", {"x": x})

# Include y in the globals parameter - THIS WAY YOU CAN RESTRICT THE GLOBAL
# VARIABLES TO BE ACCESSIBLE TO EVAL() - FOR SECURITY.
result = eval("x + y", {"x": x, "y": y})
print(f'Result is {result}')

# You can achieve the same without passing globals parameter explicitly - global
# variable are implicitly passed to the eval() function
result2 = eval("x + y")
print(f'Result 2 is {result2}')

# Passing local variables
result3 = eval("x - 10", {}, {"x": 10000})
print(f'Result 3 is {result3}')
