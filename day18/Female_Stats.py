# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:00:35 2019

@author: lenovo
"""

import pandas as pd  
import numpy as np   
dataset = pd.read_csv('Female_Stats.csv')  
from sklearn.linear_model import LinearRegression

#explore the dataset

features = dataset.iloc[:,1:].values
labels=dataset.iloc[:,0].values
regressor = LinearRegression()

print(regressor.intercept_)
#to cslculate the slope like coef and intercept
print (regressor.coef_)
import statsmodels.api as sm #impoprtijng library summary
features=sm.add_constant(features)


features_opt=features[:,[0,1,2]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

while(True):
    regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
    p_values=regressor_OLS.pvalues
    if p_values.max()>.05:
        features_opt=np.delete(features_opt,p_values.argmax(),1)
    else:
        break
    
print(regressor_OLS.summary()) 








features = dataset.iloc[:,[1]].values
labels=dataset.iloc[:,0].values
regressor = LinearRegression()
#import statsmodels.api as sm #impoprtijng library summary

#dataset.drop("dadheight",axis=1)
features_opt=features[:,0]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(features_train,labels_train)
labels_test=lm.predict(features_test)
print(labels_test)
while(True):
    regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
    p_values=regressor_OLS.pvalues
    if p_values.max()>.05:
        features_opt=np.delete(features_opt,p_values.argmax(),1)
    else:
        break
   
print(regressor_OLS.summary()) 








features = dataset.iloc[:,[2]].values
labels=dataset.iloc[:,0].values
regressor = LinearRegression()
#import statsmodels.api as sm #impoprtijng library summary

#dataset.drop("dadheight",axis=1)
features_opt=features[:,[0]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()

from sklearn.cross_validation import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(features_train,labels_train)
labels_test=lm.predict(features_test)
print(labels_test)
while(True):
    regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
    p_values=regressor_OLS.pvalues
    if p_values.max()>.05:
        features_opt=np.delete(features_opt,p_values.argmax(),1)
    else:
        break
   
print(regressor_OLS.summary()) 
  