#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import scipy

# Copy from 6-05
def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    # read data
    df = pd.read_csv('src/data.tsv', sep='\t')

    X = df[["X1","X2"]] # X == df's X1 & X2 rows
    y = df["y"] # y == df's y row

    # array for result
    result = []

    # np.arange(0.05, 0.2, 0.05) for clustering
    for eps_param in np.arange(0.05, 0.2, 0.05):
        # model
        model = DBSCAN(eps_param)
        model.fit(X)

        # DBSCAN uses label -1 to denote outliers
        # == those data points that didn't fit well in any cluster
        label = model.labels_ == -1
        outliers = np.sum(label)

        # clusters
        clusters = max(model.labels_) + 1

        # If no error: permutate + acc score
        if clusters == len(y.unique()):
            permutation = find_permutation(clusters, y, model.labels_)
            acc = accuracy_score(y[~label], [permutation[label] for label in model.labels_[~label]])
        # If fails
        else:
            acc = np.nan

        result.append([eps_param, acc, clusters, outliers])
    
    return pd.DataFrame(
        data=result, columns=["eps", "Score", "Clusters", "Outliers"], dtype="float64"
    )


def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
