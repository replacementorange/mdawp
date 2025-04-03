#!/usr/bin/env python3

import pandas as pd

def average_temperature():
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    #print(wh.describe())
    #month = wh.loc[wh['m'] == 7]
    #temp = month['Air temperature (degC)'].mean()
    return wh.loc[wh['m'] == 7]['Air temperature (degC)'].mean()

def main():
    avg_temp = average_temperature()
    print(f"Average temperature in July: {avg_temp:.1f}")

if __name__ == "__main__":
    main()
