# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 12:07:56 2019

@author: lenovo
"""


import pandas as pd  
import numpy as np   
dataset = pd.read_csv('iq_size.csv')  

#explore the dataset

features = dataset.iloc[:,1:].values
labels=dataset.iloc[:,0].values
#prepare the data to train the model
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0)  
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(regressor.intercept_)  
print (regressor.coef_)


# Predicting the Test set results
Pred = regressor.predict(features_test)

import pandas as pd

print (pd.DataFrame(Pred, labels_test))
x=[90,70,150]
x=np.array(x)
x = x.reshape(1,3)
regressor.predict(x)
