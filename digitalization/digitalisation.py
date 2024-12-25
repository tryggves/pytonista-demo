import numpy as np

# this creates a 4x3 two dimensional array - 4 rows each with 3 columns
s = np.random.randn(4, 3)
print(s)

print("Number of dimensions:", s.ndim)
print("Shape:", s.shape)
print("data type:", s.dtype)

print("s:\n", s)

# Create an identity matrix with dimension 3x3
I = np.eye(3, 3)
print(f"I=\n {I}")

u = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]])
print(f"u=\n {u}")
v = s + u
print(f"s+u=\n {v}")

# Try some linear algebra
print("\nAxis rotation example using matrix multiplication")
# Create a 3x3 matrix
A = np.array([[1, 0, 0], 
              [0, 1, 0], 
              [0, 0, 1]])
print(f"A=\n {A}")

# Create a 3x1 matrix as input data to the rotation
x = np.array([[1], [2], [3]])
print(f"x=\n {x}")

# Multiply the two matrices
b = A @ x
print(f"b=A @ x\n {b}")
