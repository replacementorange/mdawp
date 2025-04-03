#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    # Create a dictionary to store the frequency of each letter
    letter_freq = {}
    for word in a:
        for letter in word:
            if letter not in letter_freq:
                letter_freq[letter] = 0
            letter_freq[letter] += 1

    # Create the feature matrix 
    features = np.zeros((len(a), 29))
    for i, word in enumerate(a):
        for char in word:
            if char in alphabet:
                features[i, alphabet.index(char)] += 1

    return features

def contains_valid_chars(s):
    # https://docs.python.org/3/library/functions.html#all
    return all(char in alphabet for char in s)
    # pseudokööde
    # for char in alphabet
    # if not char:
    #   return False
    #return true

def get_features_and_labels():
    # Load languages
    finnish = load_finnish()
    english = load_english()

    # Finnish
    finnish = [word.lower() for word in finnish]
    finnish = [word for word in finnish if contains_valid_chars(word)]

    # English
    english = [word for word in english if word[0].islower()]
    english = [word.lower() for word in english]
    english = [word for word in english if contains_valid_chars(word)]

    # Features and labels
    #X, y = get_features(filtered_finnish), [0] * len(filtered_finnish) # Labels finnish as 0
    #X += get_features(filtered_english), [1] * len(filtered_english) # Labels english as 1

    all_words = np.array(finnish + english)

    X = get_features(all_words)
    y = np.array(len(finnish) * [0] + len(english) * [1]) # 0 finnish, 1 english

    return X, y


def word_classification():
    # Use the function get_features_and_labels to get the feature matrix and the labels.
    X, y = get_features_and_labels()
    # Use multinomial naive Bayes to do the classification
    model = MultinomialNB()
    # accuracy scores using the sklearn.model_selection.cross_val_score
    # use 5-fold cross validation
    k_fold = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)

    acc = cross_val_score(model, X, y, cv=k_fold)
    
    # should return a list of five accuracy scores
    return acc


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
