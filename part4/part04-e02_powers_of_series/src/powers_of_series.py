#!/usr/bin/env python3

import pandas as pd

def powers_of_series(s, k):
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html
    # columnsIndex : or array-like
    # Column labels to use for resulting frame when data does not have them
    df = pd.DataFrame(s, columns=[1])

    for i in range(2, k+1):
        df[i] = s**i # power of k

    return df
    
def main():
    s = pd.Series([1,2,3,4], index=list("abcd"))
    print(powers_of_series(s, 3))
    
if __name__ == "__main__":
    main()
