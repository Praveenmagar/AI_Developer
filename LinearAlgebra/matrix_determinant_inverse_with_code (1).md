# Determinant and Inverse of Matrices

## 🔹 Determinant

The **determinant** is a scalar value that can be computed from a square matrix.  
It indicates whether the matrix is invertible and has important geometric meaning (e.g., area/volume scaling).

---

### 🟢 Determinant of a 2×2 Matrix

If  
\[
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\]

then  
\[
\det(A) = ad - bc
\]

**Example:**  
\[
A =
\begin{bmatrix}
4 & 7 \\
2 & 6
\end{bmatrix}, \quad
\det(A) = (4)(6) - (7)(2) = 24 - 14 = 10
\]

---

### 🟢 Determinant of a 3×3 Matrix

If  
\[
A =
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
\]

then  
\[
\det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
\]

**Example:**  
\[
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
\]

\[
\det(A) = 1(5 \cdot 9 - 6 \cdot 8) - 2(4 \cdot 9 - 6 \cdot 7) + 3(4 \cdot 8 - 5 \cdot 7) = 0
\]

---

## 🔹 Inverse of a Matrix

The **inverse** of a square matrix \(A\) (denoted \(A^{-1}\)) exists only if \(\det(A) \neq 0\).  
It satisfies:  
\[
A \cdot A^{-1} = I
\]  
where \(I\) is the identity matrix.

---

### 🟢 Inverse of a 2×2 Matrix

If  
\[
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\]

then  
\[
A^{-1} = \frac{1}{ad - bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
\]

**Example:**  
\[
A =
\begin{bmatrix}
4 & 7 \\
2 & 6
\end{bmatrix}, \quad \det(A) = 10
\]

\[
A^{-1} = \frac{1}{10}
\begin{bmatrix}
6 & -7 \\
-2 & 4
\end{bmatrix}
=
\begin{bmatrix}
0.6 & -0.7 \\
-0.2 & 0.4
\end{bmatrix}
\]

---

### 🟢 Inverse of a 3×3 Matrix (General Method)

Steps to find \(A^{-1}\):  
1. Compute \(\det(A)\).  
2. Find the **matrix of minors** (determinants of 2×2 submatrices).  
3. Apply checkerboard signs (+, -, + pattern) → **cofactor matrix**.  
4. Transpose the cofactor matrix → **adjugate matrix**.  
5. Multiply by \(1/\det(A)\):  
   \[
   A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)
   \]

⚡ In practice, for larger matrices, we use numerical libraries like **NumPy** instead of manual calculation.

---

## 🔹 Python Examples

### ✅ Using NumPy

```python
import numpy as np

# Define a 2x2 matrix
A = np.array([[4, 7],
              [2, 6]])

# Determinant
det = np.linalg.det(A)
print("Determinant:", det)

# Inverse
inv = np.linalg.inv(A)
print("Inverse:
", inv)

# Verification: A * A^-1 = Identity
print("Check:
", A @ inv)
```

Output:
```
Determinant: 10.000000000000002
Inverse:
 [[ 0.6 -0.7]
 [-0.2  0.4]]
Check:
 [[1. 0.]
 [0. 1.]]
```

---

### ✅ Using SymPy (symbolic math)

```python
import sympy as sp

# Define matrix with symbolic entries
a, b, c, d = sp.symbols('a b c d')
A = sp.Matrix([[a, b], [c, d]])

# Determinant
print("Determinant:", A.det())

# Inverse
print("Inverse:")
print(A.inv())
```

Output:
```
Determinant: a*d - b*c
Inverse:
Matrix([[d/(a*d - b*c), -b/(a*d - b*c)],
        [-c/(a*d - b*c), a/(a*d - b*c)]])
```

---

## ✅ Key Takeaways

- If \(\det(A) = 0\), the matrix is **singular** (no inverse exists).  
- For 2×2 matrices, there is a direct formula.  
- For 3×3 and larger, use the adjugate method or computational tools like NumPy/SymPy.
