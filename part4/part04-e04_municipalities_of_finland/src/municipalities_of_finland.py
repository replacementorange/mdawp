#!/usr/bin/env python3

import pandas as pd

def municipalities_of_finland():
    # Reading municipalities
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    # index_col = Column(s) to use as row label(s), denoted either by column labels or column indices. If a sequence of labels or indices is given, MultiIndex will be formed for the row labels.
    df = pd.DataFrame(pd.read_csv('src/municipal.tsv', sep="\t", index_col=0))
    #print(df.head()) # Test print
    #print(df.count()) 490
    return df[1:312]
    
def main():
    print(municipalities_of_finland())
    
if __name__ == "__main__":
    main()
