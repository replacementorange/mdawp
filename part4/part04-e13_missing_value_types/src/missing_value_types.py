#!/usr/bin/env python3

import pandas as pd
import numpy as np

def missing_value_types():
    persons = [[np.nan,None],[1917,'Niinistö'],[1776,'Trump'],[1523,None],[np.nan,'Steinmeier'],[1992,'Putin']]
    states = ['United Kingdom','Finland','USA','Sweden','Germany','Russia']

    # class pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
    return pd.DataFrame(data=persons,index=states,columns=['Year of independence','President'])
               
def main():
    print(missing_value_types())

if __name__ == "__main__":
    main()
