import numpy as np

C = np.array([[4, 7], [2, 6]])
det = np.linalg.det(C)
inv = np.linalg.inv(C)

print("Determinant:", det)
print("Inverse:\n", inv)
