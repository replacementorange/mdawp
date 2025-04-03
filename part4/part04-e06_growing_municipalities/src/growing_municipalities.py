#!/usr/bin/env python3

import pandas as pd

def growing_municipalities(df):
    """gets subset of municipalities (a DataFrame) as a parameter and returns the proportion of 
    municipalities with increasing population in that subset."""
    # Return a tuple representing the dimensionality of the DataFrame.
    # Returning only first one from tuple
    #print(df.shape) #(490,6) #print(df.shape[0]) # 490
    count = df.shape[0]
    cols = df.columns
    # selects the values from the column specified by `cols[1]` --> "Population change from the previous year, %"
    # filters the selected values to only include those that are greater than zero
    # returns the index of the selected rows
    filtered = df[df[cols[1]] > 0].index
    proportion = len(filtered) / count
    return proportion


def main():
    df = pd.DataFrame(pd.read_csv('src/municipal.tsv', sep="\t", index_col=0))
    data = df[1:312]

    percentage = growing_municipalities(data) * 100

    #a = 0.0 # for print testing
    print(f"Proportion of growing municipalities: {percentage:.1f}%")
    growing_municipalities(df)

if __name__ == "__main__":
    main()
