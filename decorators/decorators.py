#
# Collect decorators into a module to make them re-usable.
#
# from functools import wraps
import functools
import time


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
            value = None
            for _ in range(num_times):
                value = func(*args, **kwargs)
            # This return ensures that the wrapped function return value
            # is passed to the caller.
            return value
        return wrapper_repeat
    return decorator_repeat


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.6f} secs")
        return value

    return wrapper_timer


# Here is a nice debug feature
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # repr is a function for creating human readable string of passed paraemter
        args_repr = [repr(a) for a in args]                      # 1
        # v!r means pass v to repr()
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug
