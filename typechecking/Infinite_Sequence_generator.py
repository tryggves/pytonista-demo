#
# This generator is a infinite sequence of integers
#

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


if __name__ == '__main__':
    # This needs you to stop the process manually, it will not exit the for loop.
    # for i in infinite_sequence():
    #     print(i, end=' ')

    # Test generator
    gen = infinite_sequence()
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(next(gen))
