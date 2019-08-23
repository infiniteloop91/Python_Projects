#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:38:27 2019

@author: ericlyons
"""

import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
import scipy as sp


hella_cool_data = '/Users/ericlyons/Downloads/Mall_Customers2.csv'

df = pd.read_csv(hella_cool_data,sep=',', header=0)

df['gender_factor'] = pd.factorize(df.Gender)[0]

df=df[['gender_factor','Age','Income','Spending']]



y = df.iloc[:,3]
X = df.iloc[:,:3]


y_log = y >  75.0


nb = Pipeline([('vect', CountVectorizer()),
               ('tfidf', TfidfTransformer()),
               ('clf', MultinomialNB()),
              ])


sp.stats.iqr(y, axis=None, rng=(25, 75))
df.quantile(q=0.8, axis=0, numeric_only=True, interpolation='linear')
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)



X_log_train, X_log_test, y_log_train, y_log_test = cross_validation.train_test_split(X, y_log, test_size=0.2)
logreg = LogisticRegression()
logreg.fit(X_train, y_log_train)
y_log_pred = logreg.predict(X_log_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_log_test, y_test)))
confusion_matrix = confusion_matrix(y_log_test, y_log_pred)
print(confusion_matrix)



clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)
print("SVC score")
print(clf.score(X_test, y_test))

rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(X_train, y_train)
print("random forest score")
print(rf.score(X_test, y_test))



