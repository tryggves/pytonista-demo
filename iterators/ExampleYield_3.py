# Python3 code to demonstrate yield keyword

# Checking number of occurrence of
# geeks in string

# generator to print even numbers
def print_even(test_string):
    print('print_even: Call function')
    for i in test_string:
        if i == "geeks":
            print('print_even(): yield')
            yield i


# initializing string
test_string = " The are many geeks around you, geeks are known for teaching other geeks"

# printing even numbers using yield
count = 0

test_string = test_string.split()

for j in print_even(test_string):
    print(f'main: j is {j}')
    count = count + 1

print(f"The number of geeks in string is : {count}")

