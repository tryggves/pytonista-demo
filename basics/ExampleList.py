# Lists are one of the most powerful of mechanisms in Python.
# Here are some basic list examples.
print()
print("================")
print("Demo lists...")
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8]
mylist2 = [10, 20, 30, 40, 50, 60, 70, 80]

print("================")
# Notice the end=' ' property which continues the next print on the same line
print("mylist1:", end=" ")
print(mylist1)
print("mylist2:", end=" ")
print(mylist2)

# Demo indexing and ranges of lists
print()
print("================")
print("mylist1[1:3]", end=" ")
print(mylist1[1:3])

print("mylist1[3:]", end=" ")
print(mylist1[3:])

# Clearing elements from a list
del mylist1[:]
print(f"After clearing elements in mylist1: {mylist1}")

# Replace elements in list without creating new list
mylist1[:] = [7, 8, 9]
a = mylist1
print(f"List a is: {a}")
print(f"Testing if a is ref to mylist1 {a is mylist1}")

# Create shallow copy  of list
b = mylist1[:]
print(f"List b is: {b}")
print(f"Testing if b is ref to mylist1 {b is mylist1}")

print()
print("================")
print("Demo matrixes")
mymatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("mymatrix: ", end=" ")
print(mymatrix)

# Here is how to index a single matrix element
print("Element: ", end=" ")
print(mymatrix[0][0])

# Index a matrix row
print("row 0: ", end=" ")
print(mymatrix[0])
print("row 1: ", end=" ")
print(mymatrix[1])
print("row 2: ", end=" ")
print(mymatrix[2])

# Index column
print("Column (not correct): ", end=" ")
print(mymatrix[:][0])
# This did not work as anticipated. Getting a column requires some
# more work...
column = [row[0] for row in mymatrix]
print("Column 1: ", end=" ")
print(column)
# To get the columns use a «list comprehension» construct enclosed in
# a bracket (list) expression iterated over the rows of the matrix
# as shown in the two column extractions here.
#
# List comprehensions is a construct that can be used for any iterable
# object - in many cases this would be a String, iterating over characters
# or a string iterating over words for example.
column2 = [row[1] for row in mymatrix]
print("Column 2: ", end=" ")
print(column2)

# Testing list comprehension for a string
# Note the nice syntax in the for loop iterating over the iterable object of string.
exstring = "abcdefghijk"
print("exstring: ", end=" ")
print(exstring)
exlist = [character for character in exstring]
print("Character list: ", end=" ")
print(exlist)

# How do we do the same for words of a string???
# The split function might be the solution....
# In the string example I used the rsplit() function
mysentence = "Her er dagens tekst - rene ord for penga"
wordlist = mysentence.rsplit()
print(wordlist)
for word in wordlist:
    print(word)

print()
print("print letters of words..")
for word in wordlist:
    letters = [letter for letter in word]
    print(letters)

print("\nBye!")
