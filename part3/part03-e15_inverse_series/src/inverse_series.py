#!/usr/bin/env python3

import pandas as pd

def inverse_series(s):
    return pd.Series(data=s.index, index=s.values)

def main():
    d = { 2001 : "Bush", 2005: "Bush", 2009: "Obama", 2013: "Obama", 2017 : "Trump"}
    s4 = pd.Series(d, name="Presidents")
    print(s4)

    print(inverse_series(s4))

if __name__ == "__main__":
    main()
