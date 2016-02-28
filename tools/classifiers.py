import sys
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model.logistic import LogisticRegression

class mentoryWEB:


    vect = TfidfVectorizer(max_df=0.25, stop_words=None, max_features=2500, ngram_range=(1,2), use_idf=True, norm='l2')
    
    def __init__(self, file):    
        df = pd.read_csv(file, delimiter='\t', header=None)
        X_train_raw, y_train = df[1], df[0]
    
        X_train = self.vect.fit_transform(X_train_raw)
    
        self.clf = LogisticRegression(penalty='l2', C=10)
        self.clf.fit(X_train, y_train)
        
    
    def test(self, string):
        X_test = self.vect.transform(string)	
        predictions = self.clf.predict(X_test)

        return zip(predictions, X_test_raw)
            
if __name__ == "__main__":
    test(create_classifier(sys.argv[1]), sys.argv[2])

