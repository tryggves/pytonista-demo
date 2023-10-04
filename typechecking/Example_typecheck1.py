# Type checking
# https://realpython.com/python-type-checking/
#
# Note that Python is a dynamic type language - the types are defined at run-time when assigning
# values to variables - as opposed to static typing languages (C, C++, Java etc)
#
# Generator and Callable:
# https://www.python.org/dev/peps/pep-0484/#annotating-generator-functions-and-coroutines
#
# See the article in this link for a description/examples of Callable and Generator:
# https://www.linuxjournal.com/content/pythons-mypy-callables-and-generators
#
# Callable can be used to tell abouth the type of a function - for example a function
# returns a function:

from typing import Callable, List


# Maybe you also want to make sure that it returns a function that takes an
# int as an argument. To do that, you'll use square brackets after the word
# Callable, putting two elements in those brackets. The first will be a list
# (in this case, a one-element list) of argument types. The second element in
# the list will describe the return type from the function.
def f() -> Callable[[int], List]:
    def g(x: int) -> int:
        # Do some work here
        a = []
        for i in range(x):
            a.append(i)

        return a

    return g


# Generator objects, for more information look at this:
# https://realpython.com/introduction-to-python-generators/
def csv_reader(file_name: str):
    for row in open(file_name, "r"):
        # Iterate through the file and yield a row
        yield row


# Test same function with return statement
def csv_reader_ret(file_name: str):
    in_file = open(file_name, "r")

    for row in in_file.readline():
        # Iterate through the file and yield a row
        return row


def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")


print(headline("python type checking"))
# Pycharm type checker kicks in below
print(headline("use mypy", align="center"))
print(headline("use mypy", align=False))


b = f()
print(f"b(2) = {b(2)}")
print(f"b(3) = {b(3)}")
print(f"b(4) = {b(4)}")
print(f"b(5) = {b(5)}")

print(
    "============================================================================================="
)
print("Generator example")
test_file = "input_data.txt"
print(f"Open test file {test_file}")
csv_gen = csv_reader(test_file)
row_count = 0
for next_row in csv_gen:
    row_count += 1
print(f"Number of rows: {row_count}")

print("Test calling function with return statement. This will result in only one line")
csv_gen = csv_reader_ret(test_file)
row_count = 0
for next_row in csv_gen:
    row_count += 1
print(f"Number of rows: {row_count}")
