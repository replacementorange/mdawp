#!/usr/bin/env python3

import pandas as pd
from sklearn import linear_model


def coefficient_of_determination():
    # read file
    file = pd.read_csv('src/mystery_data.tsv', sep="\t")
    #print(file.head())

    # X1	X2	X3	X4	X5	Y
    # loc = Access a group of rows and columns by label(s) or a boolean array.
    x = file.loc[:,"X1":"X5"]
    y = file.loc[:,"Y"]

    # Implementing lr
    model=linear_model.LinearRegression(fit_intercept=True)
    model.fit(x,y)
    # Score
    # https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    score = model.score(x, y)

    r2 = [score]

    # returns R2-scores related to linear regression with each single feature in turn
    # iloc = is primarily integer position based (from 0 to length-1 of the axis)
    # "Purely integer-location based indexing for selection by position."
    for i in range(len(x.columns)):
        a = x.iloc[:,i].values.reshape(-1,1)
        model.fit(a, y)
        r2.append(model.score(a, y))

    return r2
    
def main():
    x = coefficient_of_determination()
    print(f"R2-score with feature(s) X: {x[0]}")

    for i in range(1, len(x)):
        print(f"R2-score with feature(s) X{i}: {x[i]}")

if __name__ == "__main__":
    main()
