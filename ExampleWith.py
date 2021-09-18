########################################################################################
#
# Example of using with statement
#
# See: https://www.geeksforgeeks.org/with-statement-in-python/
#
# Commonly used for I/O patterns where ensuring proper cleanup of resources (files,
# sockets, message topics etc)
#
########################################################################################

# file handling

# 1) without using with statement
file = open('file_path', 'w')
file.write('hello world !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('hello world')
finally:
    file.close()

# using with statement
# This will ensure closing the file.
with open('file_path', 'w') as file:
    file.write('hello world !')
