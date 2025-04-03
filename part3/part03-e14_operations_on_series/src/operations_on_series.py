#!/usr/bin/env python3
import pandas as pd

def create_series(L1, L2):
    s1 = pd.Series(L1, index=['a', 'b', 'c']) # first parameter list
    s2 = pd.Series(L2, index=['a', 'b', 'c']) # second parameter list
    return (s1, s2) # pair of series s1 and s2
    
def modify_series(s1, s2):
    s1['d'] = s2['b'] # new value in s1, same value as s2 index b
    s2 = s2.drop('b') # delete index b from s2
    return (s1, s2)
    
def main():
    s1, s2 = create_series([1,2,3], [4,5,6])
    s3,s4 = modify_series(s1, s2)
    print(s3 + s4)
    
if __name__ == "__main__":
    main()
