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
import typing


class MyGraphClass:
    # Here we have some class variables
    m_edges = [5, 6, 7, 8, 9]
    m_edge_count = len(m_edges)

    def __init__(self):
        m_instance_variable = 10
        m_count_updates = 0
        print(f'Number of edges is {self.m_edge_count}')

    @classmethod
    def set_edges(cls, new_edges: []):
        cls.m_edges = new_edges
        cls.m_edge_count = len(cls.m_edges)
        # cls.m_count_updates += 1

    @staticmethod
    def class_static_method():
        print(f'In class static method')

    # @property
    # def m_instance_variable(self):
    #     return self.m_instance_variable
    #
    # @property
    # def m_count_updates(self):
    #     return self.m_count_updates


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
    my_first_graph = MyGraphClass()
    print(f'Before modifying graph:  {my_first_graph.m_edge_count}')
    # print(f'm_instance_variable: {my_first_graph.get_m_instance_variable()}')

    # Make a new graph
    my_new_graph = [1, 453, 3498, 3, 3, 38, 348, 3498, 10, 11, 342]

    MyGraphClass.set_edges(my_new_graph)
    print(f'After modifying graph:  {my_first_graph.m_edge_count}')

    # Instantiate a new graph
    print(f'Create second graph')
    my_second_graph = MyGraphClass()
    print(f'After creating second graph:  {my_second_graph.m_edge_count}')

    # Call static method through class name
    MyGraphClass.class_static_method()
    # Can call static method through object instance
    my_second_graph.class_static_method()

    # Pizza examples using factory methods
    my_margherita = Pizza.margherita()
    print(f'Pizza 1: {my_margherita}')
    my_prosciutto = Pizza.prosciutto()
    print(f'Pizza 2: {my_prosciutto}')
    print(f'Pizza 1 area: {my_margherita.area()}')
    print(f'Pizza 1 area (static method call): {Pizza.circle_area(4)}')


if __name__ == '__main__':
    main()
