#!/usr/bin/env python3

import pandas as pd

def below_zero():
    wh = pd.read_csv("src/kumpula-weather-2017.csv")
    # days_below_zero = wh[wh['Air temperature (degC)'] < 0].count() --> 49
    return len(wh[wh['Air temperature (degC)'] < 0])

def main():
    cold_days = below_zero()
    print(f"Number of days below zero: {cold_days:.0f}")
    
if __name__ == "__main__":
    main()
