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

test_var = True

# Note that lambdas can only contain expressions, NOT STATEMENTS (see ref link 1 above)
# This is awkward use of lambda
a = (lambda test_var: "Hello" if test_var else "Foff")(test_var)
print(f"a={a}")

# This is how to use ternary expression
test_var = False
a = "Hello" if test_var else "Poff"
print(f"a={a}")
