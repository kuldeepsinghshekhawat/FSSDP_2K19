# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:35:17 2019
@author: lenovo
"""
"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""
import pandas as pd 
import numpy as np 
dataset=pd.read_csv("kc_house_data.csv")
dataset.head(10)
dataset.isnull().any(axis=0)
dataset['sqft_above'].fillna(np.mean)
features=dataset.iloc[:,3:]
#features.columns=["bedrooms","bathrooms","sqft_living","sqft_lot","floors","waterfronts","view","condition","grade","sqft_above","sqft_basement","yr_built","yr_renovvated","zipcode","lat","long","sqft_living15","sqft_lot15"]
features["sqft_above"]=features["sqft_above"].astype(np.float64)
#features=np.array(features)
features["sqft_above"]=features["sqft_above"].fillna(features["sqft_above"].mean()).values

labels=dataset.iloc[:,2].values
features.isnull().any(axis=0)
#labels=labels.reshape(1,-1)
from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.28, random_state=0) 

from sklearn.linear_model import LinearRegression
ln=LinearRegression()
ln.fit(features_train, labels_train)

#To see the value of the intercept and slop calculated by the linear regression algorithm for our dataset, execute the following code.
print(ln.intercept_)  
print (ln.coef_)


# Predicting the Test set results
Pred = ln.predict(features_test)

import pandas as pd

print (pd.DataFrame(Pred, labels_test))


x = [3,1,1180,5650,1,0,0,0,3,7,1180,0,1955,0,98178,47.5112,-122.47,1340,5650]
x = np.array(x)
x = x.reshape(1,-1)
ln.predict(x)




from sklearn.model_selection import cross_val_score

lin_reg = LinearRegression()

MSEs = cross_val_score(lin_reg, features, labels, scoring='neg_mean_squared_error', cv=5)

mean_MSE = np.mean(MSEs)

print(mean_MSE)







# Standardize x_train
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(features)
features = scaler.transform(features)
from sklearn.linear_model import Ridge, Lasso
# Fit x_train and y_train
ridge = Ridge().fit(features, labels)
lasso = Lasso().fit(features, labels)
# Print results for both Ridge and Lasso
print('Ridge: ', ridge.coef_)
print('Lasso:', lasso.coef_)





from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
ridge = Ridge()
ridge_regressor = GridSearchCV(ridge,features,scoring='neg_mean_squared_error', cv=5)
ridge_regressor.fit(features, labels)
ridge_regressor.best_params_
ridge_regressor.best_score_


#Lasso
from sklearn.linear_model import Lasso
lasso = Lasso()
lasso_regressor = GridSearchCV(lasso, features, scoring='neg_mean_squared_error', cv = 5)
lasso_regressor.fit(features, labels)
lasso_regressor.best_params_
lasso_regressor.best_score_

