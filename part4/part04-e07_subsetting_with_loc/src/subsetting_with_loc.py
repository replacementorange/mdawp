#!/usr/bin/env python3

import pandas as pd

# loc is looking up for the index "Position doesn't matter"
# iloc is looking up for THE POSITION of the index "Position matters"
def subsetting_with_loc():
    """go takes the subset of municipalities from Akaa to Äänekoski and restricts it to columns: "Population", 
    "Share of Swedish-speakers of the population, %", and "Share of foreign citizens of the population, %". 
    Returns content as a DataFrame."""
    df = pd.DataFrame(pd.read_csv('src/municipal.tsv', sep="\t", index_col=0))
    cols = df.columns
    # ["Akaa":"Äänekoski"] [[cols[0],cols[2],cols[3]]]
    #print(df.loc["Akaa":"Äänekoski"],[[cols[0], cols[2], cols[3]]])
    return df.loc["Akaa":"Äänekoski"] [[cols[0], cols[2], cols[3]]]


def main():
    print(subsetting_with_loc)

if __name__ == "__main__":
    main()
