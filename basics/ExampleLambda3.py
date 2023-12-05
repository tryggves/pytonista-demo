#
# Python Map Lambda Example
#

# map() function
# Map in Python is a function that works as an iterator to return a result after applying a
# function to every item of an iterable (tuple, lists, etc.). It is used when you want to
# apply a single transformation function to all the iterable elements. The iterable and
# function are passed as arguments to the map in Python.


def main():

    # map() takes 2 arguments: function and iterable (like a list)
    # Here the function is the lambda expression taking one parameter and doubles its value
    # Here the iterable is the list of integers 1-4
    # Variable a is assigned the map object
    a = map(lambda x: x * 2, [1, 2, 3, 4])
    print(f"a is {a}")

    # Instantiate a list from the map object
    my_list = list(a)
    print(f"my_list is {my_list}")

    # The classic code pattern for the above is:
    b = list(map(lambda x: x * 2, [1, 2, 3, 4]))
    print(f"b is {b}")


if __name__ == '__main__':
    main()
