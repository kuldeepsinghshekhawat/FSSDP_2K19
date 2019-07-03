# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 10:43:21 2019

@author: lenovo
"""

"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat", delimiter =' ')

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LinearRegression 
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
#import seaborn as sns
from sklearn.model_selection import train_test_split

#read the .dat file 
dataset=pd.read_csv("Prostate_Cancer.dat",sep="\s+")
features=dataset.iloc[:,:-1]
labels=dataset.iloc[:,-1]
features_train, features_test, labels_train,labels_test	=	train_test_split(features, labels, test_size=0.3, random_state=1)
# Fitting Logistic Regression to the Training set
lm = LinearRegression ()
lm.fit(features_train, labels_train)
labels_pred = lm.predict(features_test)
pd.DataFrame(labels_pred,labels_test)
lm.score(features_test,labels_test)


lm_lasso = Lasso() 
lm_lasso.fit(features_train, labels_train)
labels_pred1 = lm_lasso.predict(features_test)
pd.DataFrame(labels_pred,labels_test)
lm_lasso.score(features_test,labels_test)



lm_ridge =  Ridge() 
lm_ridge.fit(features_train, labels_train)
labels_pred2 = lm_ridge.predict(features_test)
pd.DataFrame(labels_pred,labels_test)
lm_ridge.score(features_test,labels_test)





from sklearn import metrics
print ("Simple Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test, labels_pred),2) )

print ("Lasso Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test,labels_pred1 ),2) )


print ("Ridge Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test,labels_pred2 ),2) )


print ("ElasticNet Regression Mean Square Error (MSE) for TEST data is") 
print (np.round (metrics .mean_squared_error(labels_test,labels_pred3 ),2) )


labels1 = dataset.iloc[:,-1].values
labels1_train,labels1_test	=	train_test_split(labels1, test_size=0.3, random_state=1)

avg1=np.mean(dataset["lpsa"])
dataset["lpsa_category"] = "High"
dataset["lpsa_category"][dataset["lpsa"] < avg1] = "Low"   

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
classifier.fit(features_train, labels1_train)

#Calculate Class Probabilities
probability = classifier.predict_proba(features_test)

# Predicting the class labels
labels1_pred = classifier.predict(features_test)

