# Class with getters and setters c++/java style


class Point:
    def __init__(self, x, y):
        # CONVENTION: Member variables (private) are prefixed with '_'
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value


# This is a more Pythonic style class
class PythonicPoint:
    # No getters and setters.
    # Instanance variables are exposed to the clients.
    def __init__(self, x, y):
        self.x = x
        self.y = y
