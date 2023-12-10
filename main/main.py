import sys
sys.path.append('../DGA_detection/feature_extraction')
sys.path.append('../ml_algorithm')
import random_forest
import vectorize
import numpy as np
import pandas as pd
import re
from random import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
import joblib

if __name__ == '__main__':
    with open('../data/DGA/begnin/top-1m-domain.csv') as cl0, open('../data/DGA/dgaGenerated/360_dga.txt') as cl1:
        malicious,begnin = [],[]
        for i,j in zip(cl1,cl0):
            val = re.search(r'\w+(\.\w+)+',i)
            malicious.append(val.group())
            begnin.append(j.split(',')[1])
    
    i = 0
    features = np.zeros((60000,48))
    classs = np.zeros((60000,),dtype='int64')
    
    while i < 30000:
        mal = vectorize.vectorize(malicious[i])
        beg = vectorize.vectorize(begnin[i])
        features[2*i] = mal.vector
        features[2*i+1] = beg.vector
        classs[2*i] = 1 
        i += 1
df = pd.DataFrame(features)




X_train, X_test, y_train, y_test = train_test_split(
    df, classs, test_size=0.2, random_state=1234
)
print(type(X_train),X_train.shape,type(y_train),y_train.shape)

def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy

clf = random_forest.RandomForest(n_trees=20)
clf.fit(np.array(X_train), np.array(y_train))
predictions = clf.predict(np.array(X_test))

acc =  accuracy(y_test, predictions)
print(acc)
joblib.dump(clf,'save.joblib')
           
        


        