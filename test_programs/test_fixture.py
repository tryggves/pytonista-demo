import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def __eq__(self, other):
        return self.name == other.name

    def cube(self):
        self.cubed = True


class FruitSalad:
    # The * in parameter means variable number of parameters
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# For explanation of @ syntax see https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators
# For info on fixtures: https://docs.pytest.org/en/6.2.x/fixture.html#fixture
# Arrange-act-assert pattern
# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    # Function all() checks all boolean values in iterable
    assert all(fruit.cubed for fruit in fruit_salad.fruit)


# Arrange for the next tests
@pytest.fixture
def my_fruit():
    return Fruit("apple")


# Parentheses seems to be optional...
@pytest.fixture
def my_fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


# This function does not request fixtures
def test_apple():
    apple = Fruit("apple")
    print(f"Fruit is {apple.name}")
    assert apple.name == "apple"


# Here we request a fixture by declaring it as a parameter to the test function
# pytest searches for fixtures matching parameter name, calls them and passes the result
# as parameter to the test function.
def test_apple2(my_fruit):
    assert my_fruit.name == "apple"


def test_my_fruit_in_basket(my_fruit, my_fruit_basket):
    assert my_fruit in my_fruit_basket
