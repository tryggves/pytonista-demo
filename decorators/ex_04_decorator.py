#
# include module with wrapper
#
import math
import time

# from decorators import do_twice, repeat, timer
import decorators


def main():
    print("==== Example 1 =====================================")

    @decorators.do_twice
    def say_hello():
        print("Hello world")

    say_hello()

    print("==== Example 2 =====================================")
    # Wrapper supports any number of arguments

    @decorators.do_twice
    def greet_people(**kwargs):
        # zip makes iterable of tuples out of elements of iterables passed to it
        # in this case the typles are key, value pairs of kwargs
        zipped_kwargs = zip(kwargs.keys(), kwargs.values())
        # kwargs is dictionary
        for key, value in zipped_kwargs:
            print(f"{key} is {value}")

    greet_people(per="per", anders="anders")

    print("==== Example 3 =====================================")

    @decorators.do_twice
    def greet_people_2(**kwargs):
        # Here is another way to iterate kwargs, why the zip function above?
        for key, value in kwargs.items():
            print(f"{key} is {value}")

    greet_people_2(person1="kåre", person2="magnus")

    print("==== Example 4 =====================================")

    @decorators.repeat(num_times=2)
    def hello(name=None):
        return f"Hello {name}"

    print(hello("world"))

    print(
        """==== Example 5 =====================================
    Nested decorators"""
    )

    # Nested decorators
    @decorators.debug
    @decorators.timer
    def do_work():
        time.sleep(2)

    do_work()

    print(
        """==== Example 6 =====================================
    Using debug wrapper"""
    )

    @decorators.debug
    def make_greeting(name, age=None):
        """Create greeting string"""
        if age is None:
            return f"Happy birthday, {name}!"
        else:
            return f"Happy {age} birthday, {name}!"

    print(make_greeting("Per"))
    print(make_greeting("Kåre", 50))

    print(
        """==== Example 7 =====================================
        Apply a decorator to a standard library function"""
    )
    # Apply a decorator to a standard library function
    math.factorial = decorators.debug(math.factorial)

    def approximate_e(terms=18):
        return sum(1 / math.factorial(n) for n in range(terms))

    e = approximate_e(7)
    print(f"Approximate e={e}")


if __name__ == "__main__":
    main()
