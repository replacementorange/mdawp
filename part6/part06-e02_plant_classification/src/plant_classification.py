#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

def plant_classification():
    iris = load_iris()

    # splitting dataset
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,train_size=0.80, random_state=0)

    # model Gaussian naive Bayes
    model = naive_bayes.GaussianNB()
    model.fit(X_train, y_train)

    # prediction
    y_predict = model.predict(X_test)

    # accuracy
    acc = metrics.accuracy_score(y_test,y_predict)

    return acc


def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
