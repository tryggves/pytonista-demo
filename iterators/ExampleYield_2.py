# A Python program to generate squares from 1
# to 100 using yield and therefore generator


# An infinite generator function that prints
# next square number. It starts with 1
def nextSquare():
    print("nextSquare: Call function nextSquare()")
    i = 1

    # An Infinite loop to generate squares
    while True:
        yield i * i  # Function returns here but saves state and instruction pointer
        i += 1  # Next execution resumes
        print("Resume execute after yield in nextSquare()")
    # from this point


# Driver code
iteration = 1
for num in nextSquare():
    print(f"main: iteration {iteration}")
    iteration = iteration + 1
    if num > 100:
        print(f"num is {num}. Break.")
        break
    print(f"main: Result from nextSquare(): {num}")
