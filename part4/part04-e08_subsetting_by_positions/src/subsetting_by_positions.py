#!/usr/bin/env python3

import pandas as pd

def subsetting_by_positions():
    """ Reads the data set of the top forty singles from the beginning of the year 1964 from the src folder.
    Return the top 10 entries and only the columns Title and Artist.
    Get these elements by their positions by using a single call to the iloc attribute."""
    df = pd.DataFrame(pd.read_csv('src/UK-top40-1964-1-2.tsv', sep="\t", index_col=0))
    #print(df.head())
    #    LW                         Title                    Artist       Publisher  Peak Pos  WoC
    #Pos
    #1    1      I WANT TO HOLD YOUR HAND               THE BEATLES      PARLOPHONE         1    5
    #print(df.count())
    cols = df.columns
    return df.iloc[0:10] [[cols[1], cols[2]]]

def main():
    subsetting_by_positions()

if __name__ == "__main__":
    main()
