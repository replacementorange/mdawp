#!/usr/bin/env python3

import numpy as np

def multiplication_table(n):
    rows = np.arange(0, n).reshape(-1, 1)
    columns = np.arange(0, n).reshape(1, -1)

    return np.multiply(rows, columns)
    
def main():
	print(multiplication_table(4))
	print(multiplication_table(6))
	print(multiplication_table(10))

if __name__ == "__main__":
    main()
