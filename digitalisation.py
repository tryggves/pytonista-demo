import numpy as np
import matplotlib.pyplot as plt

# this creates a 4x3 two dimensional array
s = np.random.randn(4, 3)
print(s)

print("Number of dimensions:", s.ndim)
print("Shape:", s.shape)
print("data type:", s.dtype)

print("s:\n", s)
t = np.eye(4, 3)
print("t:\n", t)
u = s+t
print("s+t=", u)



