#!/usr/bin/env python3

# Computes Pearson correlation between the variables
# sepal length and petal length
import scipy.stats
import numpy as np

def load():
    import pandas as pd
    # loads iris.csv and drops species
    # orig: sepal_length,sepal_width,petal_length,petal_width,species
    # loaded: sepal_length,sepal_width,petal_length,petal_width
    return pd.read_csv("src/iris.csv").drop('species', axis=1).values

# loads the data and returns the correlation
def lengths():
    # Load dataframe
    df = load()

    # slicing sepal [0] and petal lenghts [2]
    #sepal_length[:,0] --> df[:,0]
    #petal_length[:,2] df[:,2]
    # pearson : (df[:,0],df[:,2]) [0] We need statistic which is first one, [1] would print pvalue

    # Pearson correlation with scipy.stats.pearsonr
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
    # Pearson correlation coefficient and p-value for testing non-correlation.
    # x-array: sepal, y-array: petal
    return scipy.stats.pearsonr(df[:,0],df[:,2]) [0]

def correlations():
    df = load()

    # correlations between all the variables --> (df[:,0],df[:,1],df[:,2],df[:,3])
    # Use the function np.corrcoef
    return np.corrcoef((df[:,0],df[:,1],df[:,2],df[:,3]))

def main():
    print(lengths()) # 0.8717537758865831
    print(correlations()) # (4,4) -->

    #[[ 1.         -0.11756978  0.87175378  0.81794113]
    #[-0.11756978  1.         -0.4284401  -0.36612593]
    #[ 0.87175378 -0.4284401   1.          0.96286543]
    #[ 0.81794113 -0.36612593  0.96286543  1.        ]]

if __name__ == "__main__":
    main()
