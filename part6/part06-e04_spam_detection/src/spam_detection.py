#!/usr/bin/env python3

import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# https://docs.python.org/3/library/gzip.html
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html

def spam_detection(random_state=0, fraction=1.0):
    # Read the lines from these files into arrays.
    with gzip.open('src/ham.txt.gz') as f:
        ham_emails = f.readlines()
    ham_emails = ham_emails[:int(fraction*len(ham_emails))]

    with gzip.open('src/spam.txt.gz') as f:
        spam_emails = f.readlines()
    spam_emails = spam_emails[:int(fraction*len(spam_emails))]

    # All mails
    all_emails = ham_emails + spam_emails
    print(all_emails)

    # Use labels 0 for ham and 1 for spam
    labels = [0]*len(ham_emails) + [1]*len(spam_emails)

    # Forms the combined feature matrix using CountVectorizer class' fit_transform method.
    # rows for the ham dataset and then the rows for the spam dataset
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(all_emails)
    y = labels

    # Divide that feature matrix and the target label into training and test sets, using train_test_split. 
    # Use 75% of the data for training.
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, random_state=random_state)

    # Model
    model = MultinomialNB()
    model.fit(X_train, y_train)

    # y prediction
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = metrics.accuracy_score(y_test, y_pred)

    # total
    total = len(y_test)

    # Misclassified sample points
    misclassified = (y_test != y_pred).sum()

    # function return a triple consisting of accuracy score of the prediction, size of test sample, number of misclassified sample points
    return accuracy, total, misclassified

def main():
    accuracy, total, misclassified = spam_detection(fraction=0.1)
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
