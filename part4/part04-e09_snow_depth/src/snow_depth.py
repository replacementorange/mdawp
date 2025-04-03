#!/usr/bin/env python3

import pandas as pd

def snow_depth():
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    # df[df[cols[1]]
    #return wh[wh[7]]
    #print(wh.describe())
    return wh['Snow depth (cm)'].max()

def main():
    max_snow_depth = snow_depth()
    print(f"Max snow depth: {max_snow_depth:.1f}")

if __name__ == "__main__":
    main()
