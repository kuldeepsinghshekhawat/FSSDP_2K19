# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 10:55:02 2019

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
test_data=pd.read_csv("test.csv")
train_data=pd.read_csv("train.csv")
test_data.isnull().any(axis="columns")
features1=train_data.iloc[:,:-1].values
features2=test_data.iloc[:,:-1].values


labels1=train_data.iloc[:,-1]
labels2=test_data.iloc[:,-1]

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
labels1 = labelencoder.fit_transform(labels1)
labels1=pd.DataFrame(data=labels1)


labels2 = labelencoder.fit_transform(labels2)
labels2=pd.DataFrame(data=labels2)

#DECISION TREE
from sklearn.tree import DecisionTreeClassifier
reg1 = DecisionTreeClassifier()  
reg1.fit(features1, labels1)
labels_pred = reg1.predict(features2) 



#RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier
reg2 = RandomForestClassifier(n_estimators=20, random_state=0)  
reg2.fit(features1, labels1)  
labels_pred1 = reg2.predict(features2)
#Evaluate the algo
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(labels2,labels_pred))  
print(classification_report(labels2,labels_pred))  
print(accuracy_score(labels2, labels_pred))



#LOGISTIC REGRESSION
from sklearn.linear_model import LogisticRegression
reg3 = LogisticRegression()
reg3.fit(features1, labels1)
# Predicting the Test set results
labels_pred2 = reg3.predict(features2)
# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels2, labels_pred)
plt.scatter(labels2, labels_pred2, color = 'red')
plt.plot(labels2, labels_pred2, color = 'blue')
plt.title('data')
plt.xlabel('test')
plt.ylabel('Marks')
plt.show()
from sklearn.neighbors import KNeighborsClassifier
reg4 = KNeighborsClassifier(n_neighbors = 5, p = 2) #When p = 1, this is equivalent to using manhattan_distance (l1), and euclidean_distance (l2) for p = 2
reg4.fit(features1, labels1)

#Calculate Class Probabilities
probability = reg4.predict_proba(features2)

# Predicting the class labels
labels_pred3 = reg4.predict(features2)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels2, labels_pred)




score1=reg1.score(features2, labels2)
print (reg1.score(features1, labels1))



score2=reg2.score(features2, labels2)
print (reg2.score(features1, labels1))



score3=reg3.score(features2, labels2)
print (reg3.score(features1, labels1))



score4=reg4.score(features2, labels2)
print (reg4.score(features1, labels1))

 
labels = ('DECISION TREE', 'RENDOM FOREST', 'LOGISTIC REGRRESSION', 'KNN')
x_index = [0,1,2,3]

performance=[0.92,0.95,0.96,0.90]
plt.bar(x_index,performance)
plt.xlabel('score', fontsize=15)
plt.ylabel('data', fontsize=15)
plt.xticks(x_index, labels, fontsize=10, rotation=45)

plt.title('comparision')
 
plt.show()






import statsmodels.api as sm
features1 = sm.add_constant(features1)
features_opt1 = features1[:,0:561]
reg1_OLS1 = sm.OLS(endog =labels1, exog = features_opt1).fit()
reg1_OLS1.summary()






import statsmodels.api as sm


features_obj = features1[:,561]
features_obj = sm.add_constant(features_obj)
while (True):
    reg1_OLS = sm.OLS(endog = labels1,exog =features_obj).fit()
    p_values = reg1_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj = np.delete(features_obj, p_values.argmax(),1)
    else:
        break
    
    
    
    
features_obj2 = features2[:,561]
features_obj2 = sm.add_constant(features_obj2)
while (True):
    reg1_OLS1 = sm.OLS(endog = labels2,exog =features_obj2).fit()
    p_values1 = reg1_OLS.pvalues
    if p_values.max() > 0.05 :
        features_obj1 = np.delete(features_obj2, p_values.argmax(),1)
    else:
        break




