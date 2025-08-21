# 📘 Determinant and Inverse of Matrices

## 🔹 Determinant

The **determinant** is a scalar value computed from a square matrix.  
It tells us whether the matrix is invertible and has geometric meaning (like area/volume scaling).

---

### 🟢 Determinant of a 2×2 Matrix

If  

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

then  

$$
\det(A) = ad - bc
$$

**Example:**

$$
A =
\begin{bmatrix}
4 & 7 \\
2 & 6
\end{bmatrix},
\quad
\det(A) = (4)(6) - (7)(2) = 24 - 14 = 10
$$

---

### 🟢 Determinant of a 3×3 Matrix

If  

$$
A =
\begin{bmatrix}
a & b & c \\
d & e & f \\
g & h & i
\end{bmatrix}
$$

then  

$$
\det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
$$

**Example:**

$$
A =
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

$$
\det(A) = 1(5\cdot9 - 6\cdot8) - 2(4\cdot9 - 6\cdot7) + 3(4\cdot8 - 5\cdot7) = 0
$$

---

## 🔹 Inverse of a Matrix

The **inverse** of a square matrix $A$ (denoted $A^{-1}$) exists only if $\det(A) \neq 0$.  
It satisfies:  

$$
A \cdot A^{-1} = I
$$  

where $I$ is the identity matrix.

---

### 🟢 Inverse of a 2×2 Matrix

If  

$$
A =
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
$$

then  

$$
A^{-1} = \frac{1}{ad - bc}
\begin{bmatrix}
d & -b \\
-c & a
\end{bmatrix}
$$

**Example:**

$$
A =
\begin{bmatrix}
4 & 7 \\
2 & 6
\end{bmatrix},
\quad \det(A) = 10
$$

$$
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
$$

---

### 🟢 Inverse of a 3×3 Matrix (General Method)

Steps to compute $A^{-1}$:  
1. Compute $\det(A)$.  
2. Find the **matrix of minors** (determinants of 2×2 submatrices).  
3. Apply the checkerboard sign pattern (+, -, +) → **cofactor matrix**.  
4. Transpose it → gives the **adjugate matrix**.  
5. Multiply by $1/\det(A)$:  

$$
A^{-1} = \frac{1}{\det(A)} \cdot \text{adj}(A)
$$

⚡ For larger matrices, we use computational tools like **NumPy**.

---

## 🔹 Python Examples

### ✅ Using NumPy
```python
import numpy as np

A = np.array([[4, 7],
              [2, 6]])

# Determinant
det = np.linalg.det(A)
print("Determinant:", det)

# Inverse
inv = np.linalg.inv(A)
print("Inverse:\n", inv)

# Verification
print("Check:\n", A @ inv)
```

---

### ✅ Using SymPy (Symbolic)
```python
import sympy as sp

a, b, c, d = sp.symbols('a b c d')
A = sp.Matrix([[a, b], [c, d]])

print("Determinant:", A.det())
print("Inverse:\n", A.inv())
```

---

## ✅ Key Takeaways
- If $\det(A) = 0$, the matrix is **singular** (no inverse).  
- For 2×2, use the direct formula.  
- For 3×3+, use the adjugate method or computational tools.
