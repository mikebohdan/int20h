import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression
vect = TfidfVectorizer(max_df=0.25, stop_words=None, max_features=2500, ngram_range=(1,2), use_idf=True, norm='l2')
    
def create_classifier(file):    
    df = pd.read_csv(file, delimiter='\t', header=None)
    X_train_raw, y_train = df[1], df[0]
    
    X_train = vect.fit_transform(X_train_raw)
    
    clf = LogisticRegression(penalty='l2', C=10)
    clf.fit(X_train, y_train)
    return clf

    
def test(clf, file):
    with open(file, 'r') as inp:
        X_test_raw = [i for i in inp]   
    X_test = vect.transform(X_test_raw)	
    predictions = clf.predict(X_test)

    for i in zip(predictions, X_test_raw):
        print(i)

if __name__ == "__main__":
    test(create_classifier(sys.argv[1]), sys.argv[2])

