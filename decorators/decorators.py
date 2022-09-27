#
# Collect decorators into a module to make them re-usable.
#
import functools
# from functools import wraps


def do_twice(func):
    # Note the naming convention of the inner function prefixing it
    # with 'wrapper_'
    #
    # Note: The func argument should be a function that can have any
    #       number of arguments
    # Note the use of decorator from functool package (@functools.wraps). This will preserve the
    # information about the original function (func)
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        # *args and **kwargs unpacks the arguments
        # see basics/Var_args.py
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


def repeat(num_times=0):
    """ Repeat the function call

    :param num_times
    :return: callable wrapper function
    """

    # Note the naming convention of the inner function prefixing it
    # with 'wrapper_'
    #
    # Note: The func argument should be a function that can have any
    #       number of arguments
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat
