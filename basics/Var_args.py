############################################################################
# Shows unpacking of variables.
# Shows how to pass variable number of arguments to functions.
# There are two variants:
# - non-keyworded variable length argument list - use *args
# - keyworded variable length argument list - use **kwargs
#
# References>
# https://www.geeksforgeeks.org/args-kwargs-python/
# https://medium.com/swlh/change-the-way-you-write-python-code-with-one-extra-character-6665b73803c1
#
############################################################################


def version1(a, b):
    print(a)
    print(b)


# Handle variable numbers of parameters
def version2(a, b, *args):
    print(a)
    print(b)

    if args:
        for c in args:
            print(c)


# Handle variable number of arguments including key,value arguments
def version3(a, b, *args, **kwargs):
    print(a)
    print(b)

    if args:
        for c in args:
            print(c)

    if kwargs:
        for key, value in zip(kwargs.keys(), kwargs.values()):
            print(key, ":", value)


mynumbers = range(100)
# This prints the object
print(f"object: {mynumbers}")

# This prints mynumbers list returned by the range() function
print(f"unpackaged:")
print(*mynumbers)

d = {"key1": "A", "key2": "B"}
# This prints the keys
print(*d)
e = {**d}
print(e)
# print(**d)
# for x in range(100):
#     print(x)

version1(10, 20)

# This breaks
# version1(10,20,30)
# Fixed by version 2
version2(10, 20, 30)

# This breaks if key,value parameter is given
# version2(10,20,30, Extra=40)
# Fixed by version 3
version3(10, 20, 30, 40, 50, Extra=40)


# Test all() function
class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


fruit_bowl = [Fruit("apple"), Fruit("banana")]
fruit_salad = FruitSalad(*fruit_bowl)
fruit_cubed = (fruit.cubed for fruit in fruit_salad.fruit)
print(fruit_cubed)
# same as:
# all(fruit.cubed for fruit in fruit_salad.fruit)
is_fruit_cubed = all(fruit_cubed)
if is_fruit_cubed:
    print("Proper fruit salad")
else:
    print("bad fruit")
