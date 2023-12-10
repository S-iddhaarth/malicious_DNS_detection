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
with open('save.joblib', 'rb') as file:
    loaded_model = joblib.load(file)
data = vectorize.vectorize('knxnyymewusvkxu.com')

value = loaded_model.predict(data.vector.reshape((48,1)).T)
print(value)