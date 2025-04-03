#!/usr/bin/env python3

import pandas as pd

def main():
    # Loading data set
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    df = pd.DataFrame(pd.read_csv('src/municipal.tsv', sep="\t"))
    # Defining shape
    r, c = df.shape
    # Printing the shape and the column names
    print(f"Shape: {r},{c}")
    print("Columns:")
    for column in df.columns:
        print(column)


if __name__ == "__main__":
    main()
