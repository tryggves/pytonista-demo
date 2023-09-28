#
# Simple decorator introduction
# by wrapper function pattern
#

from datetime import datetime


# Example 1
# my_decorator is a wrapper function taking another function as argument
# The argument func is called inside the wrapper() functions
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# Example 2
# Wrapper applies logic deciding the call to the wrapped function, in this case the
# time of day will either result in calling func() or not.
def not_during_the_night(func):
    def wrapper():
        # Adjust the time to test this behaviour
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper


def say_whee():
    print("Whee!")


# Example 3
# Introducing the pie syntax decorator statement using @ symbol
# First we make a wrapper function that takes another function as argument
def my_wrapper(func: callable):
    """

    :type func: object function to be wrapped
    """
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


# Example 3
# @my_wrapper statement is the same as the statement
# say_hello = my_wrapper(say_hello)
@my_wrapper
def say_hello():
    print("Hello!")


if __name__ == '__main__':
    # Call the decorator resulting in setting variable say_whee to the wrapper function
    # declared/defined inside my_decorator function
    print('======= Example 1 ==============================================================')
    print(f"Call say_whee() without decorator: ", end='')
    say_whee()

    print('\n======= Example 2 ==============================================================')
    say_whee = my_decorator(say_whee)
    print(f"Callable returned by my_decorator(say_whee): ", end='')
    print(say_whee)
    # Calling the wrapper which then calls say_whee() function
    print('\n======= Example 3 ==============================================================')
    print("Call the callable function")
    say_whee()

    print('\n======= Example 4 ==============================================================')
    say_whee = not_during_the_night(say_whee)
    say_whee()

    print('\n======= Example 5 ==============================================================')
    say_hello()

    # Example 4
    # Here we apply the wrapper defining an inner function
    print('\n======= Example 4 ==============================================================')

    @my_wrapper
    def say_good_morning():
        print('Good morning!')

    # Then calling the function through the wrapper
    say_good_morning()
