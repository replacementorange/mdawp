#!/usr/bin/env python3

import numpy as np

def diamond(n):
    # function creates the identity matrix, that is, a matrix with elements
	# on the diagonal are set to one, and non-diagonal elements are set to zero
	a = np.eye(n, dtype=int)
	# b is flipped a
	b = np.flip(a, 0)
	
	# creating diamond by merging ab --> creates half of a diamond
	diamond = np.concatenate((a,b), axis=1)
	# creates second half of a diamond by flipping first and merging it
	diamond = np.concatenate((np.flip(diamond, 0), diamond)) # --> creates too many rows & columns
	
	# https://numpy.org/doc/stable/reference/generated/numpy.delete.html#numpy-delete
	# numpy.delete(arr, obj, axis=None)
	diamond = np.delete(diamond, n, 1) # delete column
	diamond = np.delete(diamond, n, 0) # delete row
	
	return diamond

def main():
	print(diamond(5))
	print(diamond(3))
	print(diamond(1))
    
if __name__ == "__main__":
    main()
