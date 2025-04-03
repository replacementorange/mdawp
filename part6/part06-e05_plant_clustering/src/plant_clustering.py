#!/usr/bin/env python3

import scipy
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0]
        permutation.append(new_label)
    return permutation

def plant_clustering():
    # load data
    iris = load_iris()
    X,y = iris.data, iris.target

    # KMeans with 3 cluster
    model = KMeans
    model = KMeans(3, n_init=10, random_state=0)
    model.fit(X)

    # permutation
    permutation = find_permutation(3, y, model.labels_)

    # permute the labels
    new_labels = [permutation[label] for label in model.labels_]

    # print(model.cluster_centers_)
    acc=accuracy_score(y, new_labels)

    return acc

def main():
    print(plant_clustering())

if __name__ == "__main__":
    main()
