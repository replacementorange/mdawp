#!/usr/bin/env python3

import numpy as np

def get_row_vectors(a):
	rows = []
	num_rows, num_colums = a.shape
	
	for i in range(num_rows):
	    row = a[i,:]
	    rows.append(row.reshape(1, num_colums))
	
	return rows

def get_column_vectors(a):
	columns = []
	num_rows, num_colums = a.shape

	for i in range(num_colums):
	    column = a[:,i]
	    columns.append(column.reshape(num_rows, 1))

	return columns

def main():
    np.random.seed(0)
    a=np.random.randint(0,10, (4,4))
    print("a:", a)
    print("Row vectors:", get_row_vectors(a))
    print("Column vectors:", get_column_vectors(a))

if __name__ == "__main__":
    main()
