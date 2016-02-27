import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.cross_validation import train_test_split, cross_val_score


def create_classifier(file):
    ds = pd.read_csv('SMSSpamCollection.txt', delimiter='\t', header=None)
    X_train_raw, y_train = ds[1], ds[0]
    # ds_test = pd.read_csv('test.txt', delimiter='\t', header=None)
    # X_test_raw = ds_test[0]
    with open('test.txt', 'r') as inp:
        X_test_raw = [i for i in inp]   

    # X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1],df[0], test_size=0.01)
    # print(type(X_test_raw.as_matrix()))
    # for i in X_train_raw:
    #     try:
    #         print(i)
    #     except Exception:
    #         pass
    vectorizer = TfidfVectorizer()
    X_train = vectorizer.fit_transform(X_train_raw)

    X_test = vectorizer.transform(X_test_raw)

    classifier = LogisticRegression()
    # print(type(X_train))

    classifier.fit(X_train, y_train)
    
    return classifier
    predictions = classifier.predict(X_test)
    # print(X_test)
    for i in zip(predictions, X_test_raw):
        try:
            print(i)
        except Exception:
            pass
            
            