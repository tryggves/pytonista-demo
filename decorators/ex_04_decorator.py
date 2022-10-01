#
# include module with wrapper
#
import time

from decorators import do_twice, repeat, timer


def main():
    print('==== Example 1 =====================================')

    @do_twice
    def say_hello():
        print('Hello world')

    say_hello()

    print('==== Example 2 =====================================')
    # Wrapper supports any number of arguments

    @do_twice
    def greet_people(**kwargs):
        # zip makes iterable of tuples out of elements of iterables passed to it
        # in this case the typles are key, value pairs of kwargs
        zipped_kwargs = zip(kwargs.keys(), kwargs.values())
        # kwargs is dictionary
        for key, value in zipped_kwargs:
            print(f'{key} is {value}')

    greet_people(per='per', anders='anders')

    @do_twice
    def greet_people_2(**kwargs):
        # Here is another way to iterate kwargs, why the zip function above?
        for key, value in kwargs.items():
            print(f'{key} is {value}')

    greet_people_2(person1='kåre', person2='magnus')

    @repeat(num_times=2)
    def hello(name=None):
        return f'Hello {name}'
    print(hello('world'))

    @timer
    def do_work():
        time.sleep(5)
    do_work()


if __name__ == '__main__':
    main()
