#!/usr/bin/env python3

import numpy as np

def most_frequent_first(a, c):
    column = a[:,c] # [4 1 0 1 0 9 2 3 1 2]

    # https://numpy.org/doc/stable/reference/generated/numpy.unique.html --> Find the unique elements of an array.

    # axis int or None, optional --> The axis to operate on. If None, ar will be flattened. 
    # If an integer, the subarrays indexed by the given axis will be flattened and treated as the 
    # elements of a 1-D array with the dimension of the given axis
    unique_values, inverse_indices, value_counts = np.unique(column, return_inverse=True, return_counts=True)

    # sorting uniques
    sorted = np.argsort(value_counts[inverse_indices])

    # returning rearranged original array
    return a[sorted][::-1]

def main():
    a = np.array(
     [[5, 0, 3, 3, 7, 9, 3, 5, 2, 4],
     [7, 6, 8, 8, 1, 6, 7, 7, 8, 1],
     [5, 9, 8, 9, 4, 3, 0, 3, 5, 0],
     [2, 3, 8, 1, 3, 3, 3, 7, 0, 1],
     [9, 9, 0, 4, 7, 3, 2, 7, 2, 0],
     [0, 4, 5, 5, 6, 8, 4, 1, 4, 9],
     [8, 1, 1, 7, 9, 9, 3, 6, 7, 2],
     [0, 3, 5, 9, 4, 4, 6, 4, 4, 3],
     [4, 4, 8, 4, 3, 7, 5, 5, 0, 1],
     [5, 9, 3, 0, 5, 0, 1, 2, 4, 2]])

    print(most_frequent_first(a, -1))

if __name__ == "__main__":
    main()
