#
# Global variables tutorial
#
# https://realpython.com/python-use-global-variable-in-function/
#

# Comment out this statement to demo the effect of accessing global variable from an
# inner function scope.
some_variable = 10001

number = 42


def outer_func():
    def inner_func():
        print(f"Value of some_variable: {some_variable}")

    inner_func()


def access_number():
    # This makes a local scope number variable (shadows the global variable)
    # Uncomment the global statement to access global variable
    # global number
    number = 7


def main():
    print("=== GLOBAL VARIABLES EXAMPLE ===", "\n")
    outer_func()
    access_number()
    print(f"number is {number}")


if __name__ == "__main__":
    main()
