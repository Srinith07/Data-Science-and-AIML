import numpy as np


# 1D array
arr = np.array([1, 2, 3, 4, 5])
print("1D numpy array:\n", arr)

# 2D array
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n2D numpy array:\n", arr_2d)

# 0D, 1D, 2D, 3D arrays
a = np.array(42)                 # 0D
b = np.array([1, 2, 3])          # 1D
c = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])                               # 2D

d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])                               # 3D

print("\n0D array:", a)
print("\n1D array:\n", b)
print("\n2D array:\n", c)
print("\n3D array:\n", d)

print('\nDimensions:')
print(a.ndim)  # 0
print(b.ndim)  # 1
print(c.ndim)  # 2
print(d.ndim)  # 3
