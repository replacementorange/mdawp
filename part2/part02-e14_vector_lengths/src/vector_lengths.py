#!/usr/bin/env python3

import numpy as np
#import scipy.linalg

def vector_lengths(a):
    return np.sqrt(np.sum(a**2, axis=1))

def main():
	np.random.seed(0)
	b=np.random.randint(0, 10, (4,5)) # 0-9, 4 rows, 5 columns
	print(b)
	lengths = vector_lengths(b)
	print(lengths)

if __name__ == "__main__":
    main()
