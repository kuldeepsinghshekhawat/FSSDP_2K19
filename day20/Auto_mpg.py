# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:17:14 2019

@author: lenovo
"""

"""
Q1. (Create a program that fulfills the following specification.)
Auto_mpg.txt

Here is the dataset about cars. The data concerns city-cycle fuel consumption in miles per gallon (MPG).

    Import the dataset Auto_mpg.txt
    Give the column names as "mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name" respectively
    Display the Car Name with highest miles per gallon value
    Build the Decision Tree and Random Forest models and find out which of the two is more accurate in predicting the MPG value
    Find out the MPG value of a 80's model car of origin 3, weighing 2630 kgs with 6 cylinders, having acceleration around 22.2 m/s due to it's 100 horsepower engine giving it a displacement of about 215. (Give the prediction from both the models)



"""
import pandas as pd
import numpy as np
dataset=pd.read_csv("Auto_mpg1.txt",sep="\s+",header=None)
dataset.columns=["mpg", "cylinders", "displacement","horsepower","weight","acceleration", "model year", "origin", "car name"]
dataset['horsepower']=dataset['horsepower'].replace("?",np.nan).astype(np.float64)
dataset.isnull().any(axis=0)
dataset['horsepower'].fillna(np.mean)
dataset["mpg"].max()
car_name=dataset["car name"][dataset["mpg"]==46.6]
print(car_name)

features = dataset.iloc[:,1:8]
labels = dataset.iloc[:,0] 
features.isnull().any(axis=0)
features['horsepower']=features['horsepower'].astype(np.float64)
features['horsepower']=features['horsepower'].fillna(features['horsepower'].mean())


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.2, random_state=0) 
#by decision tree

from sklearn.tree import DecisionTreeRegressor  
regressor = DecisionTreeRegressor()  
regressor.fit(features_train, labels_train)  

labels_pred = regressor.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  

x = [6,275,100,2630,22.2,80,3]
x = np.array(x)
x = x.reshape(1,-1)
regressor.predict(x)


from sklearn.ensemble import RandomForestRegressor

reg = RandomForestRegressor(n_estimators=20, random_state=0)  
reg.fit(features_train, labels_train)  
labels_pred = reg.predict(features_test)

#train the model
#Evaluating the algorithm
labels_pred = reg.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df 
x = []
x = np.array(x)
x = x.reshape(1,-1)
reg.predict(x)


