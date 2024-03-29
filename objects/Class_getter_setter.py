###########################################################################################
#
# Example classes and objects
# Everything (almost) in Python is an object
# Check effect of class variables versus instance variables.
#
# Getters and setters
# Reference: https://realpython.com/python-property/
#
###########################################################################################
# Local modules supporting this example
from circle import Circle, DecoratorCircle
from point import Point, PythonicPoint


def main():
    point1 = Point(10, 20)
    print(f"point1.x: {point1.get_x()}")
    print(f"point1.y: {point1.get_y()}")

    point1.set_x(100)
    point1.set_y(200)
    print(f"point1.x: {point1.get_x()}")
    print(f"point1.y: {point1.get_y()}")

    # Pythonic coding
    point2 = PythonicPoint(10, 20)
    print(f"point2.x: {point2.x}")
    print(f"point2.y: {point2.y}")

    point2.x = 100
    point2.y = 200
    print(f"point2.x: {point2.x}")
    print(f"point2.y: {point2.y}")

    # Test the property object in Circle class
    circle = Circle(42.0)
    print(f"Circle radius: {circle.radius}")
    # Set new value of radius
    circle.radius = 100
    print(f"Circle radius: {circle.radius}")

    print(dir(Circle.radius))
    print(Circle.radius.fdel)

    # Decorator property
    dCircle = DecoratorCircle(10)
    r = dCircle.radius
    print(f"Radius is {r}")


if __name__ == "__main__":
    main()
