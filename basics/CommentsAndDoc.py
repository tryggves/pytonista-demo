# This file shows how to make code comments and documentation inside the code
#
# See this good guide to the topic:
# https://realpython.com/documenting-python-code/
#


class SimpleClass:
    """Class docstring goes here (summary line)

    (The detailed documentation follows after the blank line)
    This is an example of making documentation inside the code implementation.
    This could be more practical than making a separate documentation to maintain.
    """

    def say_hello(self):
        """Class member function definition

        :return:
        """
        print("Hello world")


def main():
    s = SimpleClass()
    s.say_hello()

    exit(0)


if __name__ == "__main__":
    main()
