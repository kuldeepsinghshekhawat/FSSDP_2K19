# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 18:11:48 2019

@author: HP
"""

import pandas as pd 
#import numpy as np
#import matplotlib.pyplot as plt
#from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
import pickle


df=pd.read_csv("ThoraricSurgery1.csv")
df.head()
df.describe()
df.dtypes
#check the null values
df.isnull().sum().sum()
df1=df
df1.head(10)
#replace the categorical value in numeric value 
df1.replace({'T':1,'F':0,
             'PRZ0':0,'PRZ1':1,'PRZ2':2,
             'OC10':0,'OC11':1,'OC12':2,'OC13':3,'OC14':4,'OC15':5,
             },inplace=True)
df1[['PRE7','PRE8','PRE9','PRE10','PRE11','PRE14','PRE17','PRE19','PRE25','PRE30','PRE32','Risk1Yr']] = df1[['PRE7','PRE8','PRE9','PRE10','PRE11','PRE14','PRE17','PRE19','PRE25','PRE30','PRE32','Risk1Yr']].apply(pd.to_numeric) 
print(df1.dtypes)

features=df1[['PRE5','PRE6','PRE8','PRE10','PRE11','PRE14','PRE19','PRE25','PRE30','PRE32','AGE']]
labels=df1['Risk1Yr']
#import skearn librry for train _test_split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.30, random_state = 0)



#featurs scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)   

reg1 = RandomForestClassifier(n_estimators=20, random_state=0)  
reg1.fit(features_train, labels_train)

models_dict = {}
models_dict["scaling"] = sc
models_dict["Random_Forest"] = reg1

with open("static/models/trained_model.pkl", "wb") as f:
    pickle.dump(models_dict, f)
print("Training Complete")
#labels_pred3 = reg1.predict(features_test)
##Evaluate the algo
#print(confusion_matrix(labels_test,labels_pred3))  
#print(classification_report(labels_test,labels_pred3))  
#print(accuracy_score(labels_test, labels_pred3))