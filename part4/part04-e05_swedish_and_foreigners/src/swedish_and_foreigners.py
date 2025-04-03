#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df = pd.DataFrame(pd.read_csv('src/municipal.tsv', sep="\t", index_col=0))
    data = df[1:312]
    columns = data.columns

    # "Region 2018"	"Population"	"Population change from the previous year, %"	"Share of Swedish-speakers of the population, %"	"Share of foreign citizens of the population, %"
    subset = data[(data[columns[2]] > 5) & (data[columns[3]] > 5)]
    
    return subset[[columns[0], columns[2], columns[3]]]

def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
