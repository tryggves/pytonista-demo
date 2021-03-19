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

# Include y in the globals parameter
result = eval("x + y", {"x": x, "y": y})
print(f'Result is {result}')