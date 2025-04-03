#!/usr/bin/env python3

import pandas as pd

def cyclists():
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", delimiter=";")
    #print(df.head(5))
    #print(df.describe())
    #containing_null = df[df.isnull().any(axis=1)]

    # dropping empty rows
    # ‘all’ : If all values are NA, drop that row or column.
    # 'inplace': Whether to modify the DataFrame rather than creating a new one.
    df.dropna(how='all',inplace=True)
    # dropping columns that contains only missing values
    # axis : 1, or ‘columns’ : Drop columns which contain missing value.
    df.dropna(axis=1,how='all',inplace=True)
    return df

def main():
    cyclists()
    
if __name__ == "__main__":
    main()
