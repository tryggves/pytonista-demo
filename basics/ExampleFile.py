import os
import sys

# Function
print(f"CWD is {os.getcwd()}")

# file handling examples
print("File handling examples")
f = open("test.txt", "w")
f.write("Hello world!")
f.close()
print("Done.")

# Example of reading multiple lines from file with handling of lines
# through a while loop.
print("File loop 1")
f2 = open("inputdata.txt", "r")
line = f2.readline
count = 1
line = f2.readline()
while line:
    print("L", count, ": ", line)
    count = count + 1
    line = f2.readline()

f2.close()
print("DONE LOOP1")

# Here is the same:
print("File loop 2")
with open("inputdata.txt", "r") as infile:
    line = infile.readline
    count = 1
    line = infile.readline()
    while line:
        print("L", count, ": ", line)
        count = count + 1
        line = infile.readline()

    infile.close()
print("DONE LOOP2")
