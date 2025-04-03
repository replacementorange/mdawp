#!/usr/bin/env python3

import pandas as pd
import numpy as np


def split_date():
    # Read the bicycle data set from
    df = pd.read_csv("src/Helsingin_pyorailijamaarat.csv", delimiter=";")
    # cleaning data
    df.dropna(how='all',axis=0,inplace=True)
    df.dropna(how='all',axis=1,inplace=True)

    # split the Päivämäärä column into a DataFrame with five columns with column names Weekday, Day, Month, Year, and Hour
    date = df['Päivämäärä'].str.split(expand=True) # 0 [ke, 1, tammi, 2014, 00:00]
    #print(date)
    # five columns with column names Weekday, Day, Month, Year, and Hour
    date.columns=['Weekday', 'Day', 'Month', 'Year', 'Hour']
    #  get Hours, drop the colon and minutes
    date['Hour'] = date['Hour'].str.split(':', expand=True)[0]

    # Convert field Weekday according the rule
    date.replace({'Weekday' : {'ma':'Mon', 'ti':'Tue', 'ke':'Wed', 'to':'Thu', 'pe':'Fri', 'la':'Sat', 'su':'Sun'},}, inplace=True)
    # Convert the Month column according to the mapping
    date.replace({'Month' : {'tammi':1, 'helmi':2, 'maalis':3, 'huhti':4, 'touko':5, 'kesä':6, 'heinä':7, 'elo':8, 'syys':9, 'loka':10, 'marras':11, 'joulu':12}}, inplace=True)

    # returns a DataFrame with five columns
    date = date.astype({'Day': 'int', 'Month': 'int', 'Year': 'int', 'Hour': 'int'})
    #print(date.info())
    return date


def main():
    print(split_date()) # 0 Wed 1 1 2014 0
       
if __name__ == "__main__":
    main()
