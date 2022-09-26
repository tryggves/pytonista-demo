#
# Python functions are first-class objects
# This means they can be treated as "normal" variables and
# passed as arguments to functions.
#

# STEP 1: Passing functions as parameter to another function
# Go to ex_02

def say_hello(name):
    return f"Hello {name}"


def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def greet_bob(greeter_func):
    return greeter_func("Bob")


if __name__ == '__main__':
    print('======== EXAMPLE 1 ===================================================')

    # Here we pass say_hello function as parameter  to greet_bob.
    # We don't call say_hello - then we would have to pass say_hello()
    print(greet_bob(say_hello))
    print(greet_bob(be_awesome))