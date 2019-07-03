# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 12:23:33 2019

@author: lenovo
"""
"""
Q2. This famous classification dataset first time used in Fisher’s classic 1936 paper, The Use of Multiple Measurements in Taxonomic Problems. Iris dataset is having 4 features of iris flower and one target class.

The 4 features are

SepalLengthCm
SepalWidthCm
PetalLengthCm
PetalWidthCm
The target class

The flower species type is the target class and it having 3 types

Setosa
Versicolor
Virginica
The idea of implementing svm classifier in Python is to use the iris features to train an svm classifier and use the trained svm model to predict the Iris species type. To begin with let’s try to load the Iris dataset.
"""
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
#from sklearn.utils import load_iris
iris=load_iris()
features=pd.DataFrame(iris.data,columns=iris.feature_names).values
labels=pd.DataFrame(iris.target,columns=["class"])
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.5, random_state = 0)
#visualisation for svc how many cancerous and not cancerous
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(features_train, labels_train)

# Predicting the Test set results
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test, labels_pred)
score = classifier.score(features_test,labels_test)



