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
from typing import List


class MyGraphClass:
    # Here we have some class variables
    m_edges = [5, 6, 7, 8, 9]
    m_edge_count = len(m_edges)
    m_count_updates = 0

    def __init__(self):
        self._x = 10
        print(f"Number of edges is {self.m_edge_count}")

    @classmethod
    def set_edges(cls, new_edges: List[int]) -> None:
        cls.m_edges = new_edges
        cls.m_edge_count = len(cls.m_edges)
        cls.m_count_updates += 1

    @staticmethod
    def class_static_method() -> None:
        print(f"In class static method")

    # Member attribute getter/setter/deleter
    @property
    def x(self):
        """I am the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


# Implement MyGraphClass with the state (edges) as member attributes.
# Hens change on the state will only impact one object instance and not
# all instances.
class MyGraphClassStatePrivate:
    def __init__(self):
        self._x = 10
        self._edges = [5, 6, 7, 8, 9]
        self._edge_count = len(self._edges)
        self._count_updates = 0

    @property
    def edges(self) -> List[int]:
        return self._edges

    @edges.setter
    def edges(self, new_value: List[int]) -> None:
        self._edges = new_value
        self._edge_count = len(self._edges)
        self._count_updates += 1

    @property
    def edge_count(self) -> int:
        return self._edge_count

    @property
    def count_updates(self) -> int:
        return self._count_updates

    # Member attribute getter/setter/deleter
    @property
    def x(self):
        """I am the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


def main():
    print(
        "==================================================================================="
    )
    print(" Testing static and class methods.")
    print(
        "==================================================================================="
    )
    my_first_graph = MyGraphClass()
    print(f"Before modifying graph:  {my_first_graph.m_edge_count}")
    # print(f'm_instance_variable: {my_first_graph.get_m_instance_variable()}')

    # Make a new graph
    my_new_graph = [1, 453, 3498, 3, 3, 38, 348, 3498, 10, 11, 342]

    # This will impact the class variable (static) m_edges. It will have a side effect on
    # all object (instances) which will reflect this change
    MyGraphClass.set_edges(my_new_graph)
    print(f"After modifying graph:  {my_first_graph.m_edge_count}")

    # Instantiate a new graph
    print(f"Create second graph")
    my_second_graph = MyGraphClass()
    print(f"After creating second graph:  {my_second_graph.m_edge_count}")

    MyGraphClass.set_edges([1, 2, 3, 4, 5, 6])
    print("\nAfter new modification to graph")
    print(
        f"my_first_graph num edges: {my_first_graph.m_edge_count}\tupdates: {my_first_graph.m_count_updates}"
    )
    print(
        f"my_second_graph num edges: {my_second_graph.m_edge_count}\tupdates: {my_first_graph.m_count_updates}"
    )

    # Call static method through class name
    MyGraphClass.class_static_method()
    # Can call static method through object instance
    my_second_graph.class_static_method()

    print()
    print(
        "==================================================================================="
    )
    print("Test class where state is protected")
    print(
        "==================================================================================="
    )
    print("Create first graph")
    my_first_graph = MyGraphClassStatePrivate()
    print(f"Before modifying graph edge_count:  {my_first_graph.edge_count}")

    # Make a new graph
    my_new_edges = [1, 453, 3498, 3, 3, 38, 348, 3498, 10, 11, 342]

    # This calls the object setter function
    my_first_graph.edges = my_new_edges
    print(f"After modifying graph edge_count:  {my_first_graph.edge_count}")

    # Instantiate a new graph
    print(f"Create second graph")
    my_second_graph = MyGraphClassStatePrivate()
    print(f"After creating second graph edge_count:  {my_second_graph.edge_count}")

    my_second_graph.edges = [1, 2, 3, 4, 5, 6]
    print("\nAfter new modification to graph")
    print(
        f"my_first_graph edge_count: {my_first_graph.edge_count}\tcount_updates: {my_first_graph.count_updates}"
    )
    print(
        f"my_second_graph edge_count: {my_second_graph.edge_count}\tcount_updates: {my_first_graph.count_updates}"
    )


if __name__ == "__main__":
    main()
