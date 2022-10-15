import numpy as np

# this creates a 4x3 two dimensional array - 4 rows each with 3 columns
s = np.random.randn(4, 3)
print(s)

print("Number of dimensions:", s.ndim)
print("Shape:", s.shape)
print("data type:", s.dtype)

print("s:\n", s)

# Create an identity matrix with dimension 3x3
t = np.eye(3, 3)
print(f"t:\n {t}")

u = np.array([[1,1,1],
            [1,1,1],
            [1,1,1],
            [1,1,1]])
print(f"u:\n {u}")
v = s+u
print(f"s+u=\n {v}")



