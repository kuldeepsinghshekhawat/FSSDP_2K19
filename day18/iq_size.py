# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 10:25:12 2019

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
import statsmodels.api as sm
features=sm.add_constant(features)


features_opt=features[:,[0,1,3]]
regressor_OLS = sm.OLS(endog = labels, exog = features_opt).fit()
regressor_OLS.summary()


while(True):
    regressor_OLS=sm.OLS(endog=labels,exog=features_opt).fit()
    p_values=regressor_OLS.pvalues
    if p_values.max()>.05:
        features_opt=np.delete(features_opt,p_values.argmax(),1)
    else:
        break
    
print( regressor_OLS.summary())  

    

