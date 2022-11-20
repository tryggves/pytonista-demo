###########################################################################################
#
# Example classes and objects
# Everything (almost) in Python is an object
# Check effect of class variables versus instance variables.
# Combine this with @classmethod, @staticmethod functions
# Class variable is like static in C++ and Java
# Instance variable is like class member variable (public)
#
# Reference: https://realpython.com/instance-class-and-static-methods-demystified/
#
###########################################################################################
import math


# Here is an example using classmethods to produce object instances where there are
# varying parameters to the constructor.
# In python a class can only have one __init__() function
#


class Pizza:
    def __init__(self, ingredients: [], radius=4):
        self.radius = radius
        self.ingredients = ingredients

    # This is the method printing object representation as string
    def __repr__(self):
        return f'Pizza({self.radius!r}, {self.ingredients!r})'

    # Object instance methods
    def area(self):
        return self.circle_area(self.radius)

    # Factory class methods
    @classmethod
    def margherita(cls):
        return cls(['mozarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozarella', 'tomatoes', 'ham'])

    @staticmethod
    def circle_area(radius):
        return radius ** 2 * math.pi


def main():
    print('===================================================================================')
    print(" Testing static and class methods.")
    print('===================================================================================')

    # Pizza examples using factory methods
    my_margherita = Pizza.margherita()
    print(f'Pizza 1: {my_margherita}')
    my_prosciutto = Pizza.prosciutto()
    print(f'Pizza 2: {my_prosciutto}')
    print(f'Pizza 1 area: {my_margherita.area()}')
    print(f'Pizza 1 area (static method call): {Pizza.circle_area(4)}')


if __name__ == '__main__':
    main()
