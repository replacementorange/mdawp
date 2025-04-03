#!/usr/bin/env python3

import pandas as pd
import numpy as np

def special_missing_values():
    # 0   Pos        40 non-null     int64
    # 1   LW         40 non-null     object --> to int
    # pandas.to_numeric: Convert argument to a numeric type.
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", delimiter="\t")
    numeric_df = pd.to_numeric(df['LW'], errors='coerce') # If ‘coerce’, then invalid parsing will be set as NaN.
    #print(df.info())
    #print(numeric_df) --> for comparing need to be same len as orig df --> Filling with NAs
    # pandas.DataFrame.fillna: Fill NA/NaN values using the specified method.
    numeric_df = numeric_df.fillna(len(df))
    #print(numeric_df) --> now compare "numeric_df < df.position"
    return df[numeric_df < df['Pos']]


def main():
    print(special_missing_values())

if __name__ == "__main__":
    main()
