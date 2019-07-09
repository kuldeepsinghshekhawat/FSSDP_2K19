# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:18:10 2019

@author: lenovo
"""

"""
 (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.



"""


import numpy as np
import pandas as pd
dataset=pd.read_csv("PastHires.csv")



features = dataset.iloc[:,:-1].values
labels = dataset.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labelencoder1 = LabelEncoder()
features[:, 1] = labelencoder.fit_transform(features[:, 1])
features[:, 3] = labelencoder1.fit_transform(features[:, 3])
features[:, 4] = labelencoder.transform(features[:, 4])
features[:, 5] = labelencoder.transform(features[:,5])


from sklearn.model_selection import train_test_split  
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.28, random_state=0) 
#by decision tree

from sklearn.tree import DecisionTreeClassifier  
clss = DecisionTreeClassifier()  
clss.fit(features_train, labels_train)  

labels_pred = clss.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df  



#by Random forest classifier

from sklearn.ensemble import RandomForestClassifier

clss1 = RandomForestClassifier(n_estimators=20, random_state=0)  
clss1.fit(features_train, labels_train)  
labels_pred = clss1.predict(features_test)

#train the model
#Evaluating the algorithm
labels_pred =clss1.predict(features_test)
df=pd.DataFrame({'Actual':labels_test, 'Predicted':labels_pred})  
df 
x = [10,0,4,0,0,0]
x = np.array(x)
x = x.reshape(1,-1)
clss.predict(x)
clss1.predict(x)


