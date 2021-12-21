# Class with property() hiding managed attribute

class Circle:
    def __init__(self, radius):
        self._radius = radius

    # Non-public (by convention) methods
    def _get_radius(self):
        print('Get radius')
        return self._radius

    def _set_radius(self, value):
        print('Set radius')
        self._radius = value

    def _del_radius(self):
        print('Delete radius')
        del self._radius

    # Property object attaching getter/setter/delete
    radius = property(fget=_get_radius, fset=_set_radius, fdel=_del_radius, doc='The radius property.')
