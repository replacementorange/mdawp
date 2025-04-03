#!/usr/bin/env python3

import pandas as pd

def top_bands():
    bands = pd.read_csv("src/bands.tsv", sep="\t")
    chart = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    #print(bands.head())
    #print(chart.head())
    # artist --> band (merge) !! to upper (The Beatles VS THE BEATLES)
    bands['Band'] = bands['Band'].str.upper()

    # merging
    merged = pd.merge(chart, bands, left_on=['Artist'], right_on=['Band'])

    return merged


def main():
    print(top_bands())
    #top_bands()

if __name__ == "__main__":
    main()
