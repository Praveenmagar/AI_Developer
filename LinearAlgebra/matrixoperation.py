import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[2, 0], [1, 2]])

print("Matrix addition:\n", A + B)
print("Matrix multiplication:\n", np.matmul(A, B))
print("Transpose of A:\n", A.T)
