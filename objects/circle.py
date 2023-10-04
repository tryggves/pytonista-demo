# Class with property() hiding managed attribute


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Non-public (by convention) methods
    def _get_radius(self):
        print("Get radius")
        return self._radius

    def _set_radius(self, value):
        print("Set radius")
        self._radius = value

    def _del_radius(self):
        print("Delete radius")
        del self._radius

    # Property object attaching getter/setter/delete
    radius = property(
        fget=_get_radius, fset=_set_radius, fdel=_del_radius, doc="The radius property."
    )


# Use decorator to declare property
class DecoratorCircle:
    def __init__(self, radius):
        self._radius = radius

    # This sets class name radius.getter
    @property
    def radius(self):
        """The Radius property of circle

        We can make multiple lines to describe the prperty in more
        detail.
        """
        print("Decorator: Get radius")
        return self._radius

    # This sets class name radius.setter
    @radius.setter
    def radius(self, value):
        print("Decorator: Set radius")
        self._radius = value

    # This sets class name radius.deleter
    @radius.deleter
    def radius(self):
        print("Decorator: Delete radius")
        del self._radius
