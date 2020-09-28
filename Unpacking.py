############################################################################
# Shows unpacking of variables.
#
# References>
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
            print(key, ':', value)

mynumbers = range(100)
print(mynumbers)

# This prints mynumbers list returned by the range() function
print(*mynumbers)

d = {'key1': 'A',
    'key2': 'B'}
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
version3(10,20,30,40,50, Extra=40)
