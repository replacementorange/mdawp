#!/usr/bin/env python3

import pandas as pd

def best_record_company():
    chart = pd.read_csv("src/UK-top40-1964-1-2.tsv", delimiter="\t")
    #print(chart.head())

    # grouping by record company
    publisher_group = chart.groupby('Publisher')
    #print(publisher_group.head())

    # sum of the weeks on chart (WoC) sorted
    count = publisher_group.sum()["WoC"].sort_values(ascending=False)
    #print(count.head())

    chart_top = count.index[0]
    #print(chart_top) --> COLPIX
    return chart[chart["Publisher"] == chart_top]


def main():
    print(best_record_company())
    

if __name__ == "__main__":
    main()
