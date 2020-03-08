# Function

# file handling examples
print("File handling examples")
f = open("test.txt", "w")
f.write("Hello world!")
f.close()
print("Done.")

# Example of reading multiple lines from file with handling of lines
# through a while loop.
f2 = open("inputdata.txt", "r")
line = f2.readline
count = 1
line = f2.readline()
while line:
	print("L",count,": ", line)
	count = count+1
	line = f2.readline()
	
f2.close()
