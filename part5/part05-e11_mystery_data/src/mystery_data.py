#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    # read file
    file = pd.read_csv('src/mystery_data.tsv', sep="\t")
    #print(file.head())

    # X1	X2	X3	X4	X5	Y
    # loc = Access a group of rows and columns by label(s) or a boolean array.
    x = file.loc[:,"X1":"X5"]
    y = file.loc[:,"Y"]

    # Implementing lr
    # You don't have to fit the intercept. --> fit_intercept=False
    model=LinearRegression(fit_intercept=False)
    model.fit(x,y)

    # return coef
    # coef_array of shape (n_features, ) or (n_targets, n_features)
    # --> Estimated coefficients for the linear regression problem.
    return model.coef_



def main():
    coefficients = mystery_data()
    # print the coefficients here
    # print(mystery_data()) [  3.  -1.   7.   0. -20.]
    for i in range(len(coefficients)):
         print(f"Coefficent of X:{i+1} is {coefficients[i]}")
    
if __name__ == "__main__":
    main()
