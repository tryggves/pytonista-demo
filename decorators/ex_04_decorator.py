#
# include module with wrapper
#
from decorators import do_twice
print('==== Example 1 =====================================')


@do_twice
def say_hello():
    print('Hello world')


say_hello()

print('==== Example 2 =====================================')
# Wrapper supports any number of arguments


@do_twice
def greet_people(**kwargs):
    for key, value in zip(kwargs.keys(), kwargs.values()):
        print(f'{key} is {value}')


greet_people(per='per', anders='anders')
