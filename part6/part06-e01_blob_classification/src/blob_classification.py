#!/usr/bin/env python3

import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split

def blob_classification(X, y):
    # gets feature matrix X and label vector y as parameters
    # use train_test_split function from sklearn to split the dataset
    # two parts: one for training (75%) and one for testing (25%)
    # Give parameter random_state=0 --> result is deterministic
    X_train, X_test, y_train, y_test = train_test_split(X, y,train_size=0.75, random_state=0)

    # prediction using GaussianNB
    # classifier is trained on TRAINING SET
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Predict on test set
    y_predict = model.predict(X_test)

    # return the accuracy score of the prediction on test set
    acc=metrics.accuracy_score(y_test,y_predict)

    return acc

def main():
    X,y = datasets.make_blobs(100, 2, centers=2, random_state=2, cluster_std=2.5)
    print("The accuracy score is", blob_classification(X, y))
    a=np.array([[2, 2, 0, 2.5],
                [2, 3, 1, 1.5],
                [2, 2, 6, 3.5],
                [2, 2, 3, 1.2],
                [2, 4, 4, 2.7]])
    accs=[]
    for row in a:
        X,y = datasets.make_blobs(100, int(row[0]), centers=int(row[1]),
                                  random_state=int(row[2]), cluster_std=row[3])
        accs.append(blob_classification(X, y))
    print(repr(np.hstack([a, np.array(accs)[:,np.newaxis]])))

if __name__ == "__main__":
    main()