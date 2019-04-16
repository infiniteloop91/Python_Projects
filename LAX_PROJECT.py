#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:55:19 2019

@author: ericlyons
"""

import pandas as pd 
import numpy as np 
import matplotlib as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import preprocessing, cross_validation, svm

from sklearn.ensemble import RandomForestRegressor


NCAA = pd.read_csv("/Users/ericlyons/Desktop/NCAA.csv")
INSIDE_LAX = pd.read_csv("/Users/ericlyons/Desktop/InsideLacross.csv")

#check the data 
#print(NCAA.head())
#print(INSIDE_LAX.head())

final_df = pd.merge(NCAA, INSIDE_LAX, how='inner', on = 'Team')


final_df.sort_values('Ranking')

#sort them by ranking 
ranked = final_df.sort_values('Ranking')
#print(ranked.head())
#ranked.corr()

#how do the columns correlate
#pd.scatter_matrix(ranked, figsize=(6, 6))
#plt.show()

ranked['Team'] = ranked['Team'].astype('category')


X = np.array(ranked.drop(['W', 'Record', 'Team'], 1))
print(X)

y = np.array(ranked['W'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

#SVM
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))


#Random Forest
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))

