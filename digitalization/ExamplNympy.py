# Testing numpy and scipy for numerical applications
# The fundamental data structure in numpy is the ndarray
# aka n-dimensional array

import numpy

# Creates a range of numbers and fills an ndarray
a = numpy.arange(18)
print("array a:", a)

# Reorganize into a 3x6 matrix
b = a.reshape(3, 6)
print("b after reshape:", b)

# Reorganize into a 3x3x2 cube
c = a.reshape(3, 3, 2)
print("c after reshape:")
print(c)
