#!/usr/bin/env python3

import numpy as np
from functools import reduce

def matrix_power(a, n):
    if (n == 0):
        # returns the identity matrix of shape (m, m)
        return np.eye(a.shape[0])
    elif n > 0:
        # compute the result of raising the matrix a to the power n
        return reduce(np.matmul, (a for _ in range(n)))
    else:
        # computes the inverse of the matrix a
        # inv computes the inverse of a square matrix
        a_inv = np.linalg.inv(a)
        # computes result of raising the matrix to the power
        return reduce(np.matmul, (a_inv for _ in range(abs(n))))

def main():
    a = np.array([[1, 2], [3, 4]])
    print(a)
    print(matrix_power(a, 2))
    print(matrix_power(a, 3))

if __name__ == "__main__":
    main()
