import sys
sys.path.append('../DGA_detection/feature_extraction')
sys.path.append('../ml_algorithm')
import vectorize
import numpy as np
import pandas as pd
import re


if __name__ == '__main__':
    with open('../../data/DGA/begnin/top-1m-domain.csv') as cl0, open('../../data/DGA/dgaGenerated/360_dga.txt') as cl1:
        malicious,begnin = [],[]
        for i,j in zip(cl1,cl0):
            val = re.search(r'\w+(\.\w+)+',i)
            malicious.append(val.group())
            begnin.append(j.split(',')[1])
    
    i = 0
    
    begnin_features = np.zeros((100000,47))
    malicious_features = np.zeros((100000,47))

    
    while i < 100000:
        mal = vectorize.vectorize(malicious[i])
        beg = vectorize.vectorize(begnin[i])
        begnin_features[i] = mal.vector
        malicious_features[i] = beg.vector
        i += 1
        
        
df1 = pd.DataFrame(begnin_features,columns=beg.features)
df2 = pd.DataFrame(malicious_features,columns=beg.features) 
df1.to_csv('good.csv')
df2.to_csv('bad.csv')

print(df1.head(),'\n',df2.head())