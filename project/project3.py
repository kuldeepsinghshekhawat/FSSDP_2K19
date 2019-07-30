# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:22:55 2019

@author: lenovo
"""
#importing library
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
#seaborn lib use for good visualization 
import seaborn as sns
#read the csv file 
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
#using visulization to understand our data
df1.hist()
plt.show()
#correlation between attribute using pearson
# Pearson's correlation determines the degree to which a relationship is linear
df1.corr
plt.figure(figsize=(20,15))
sns.heatmap(df1.corr(),annot=True)
#skewness is the guassian distribution
#skewness = 0 : normally distributed.
#skewness > 0 : more weight in the left tail of the distribution.
#skewness < 0 : more weight in the right tail of the distribution.
df1.skew()
#split the features and labels
features=df1[['PRE5','PRE6','PRE8','PRE10','PRE11','PRE14','PRE19','PRE25','PRE30','PRE32','AGE']]
labels=df1['Risk1Yr']
#import skearn librry for train _test_split
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.70, random_state = 0)



#featurs scalling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()  
features_train = sc.fit_transform(features_train)  
features_test = sc.transform(features_test)   


#logistic Regression
from sklearn.linear_model import LogisticRegression
reg = LogisticRegression()
reg.fit(features_train, labels_train)     
# Predicting the Test set results
labels_pred = reg.predict(features_test)
# Making the Confusion Matrix
cm = confusion_matrix(labels_test, labels_pred)
print(classification_report(labels_test,labels_pred))  
print(accuracy_score(labels_test, labels_pred))
plt.scatter(labels_test, labels_pred, color = 'red')
plt.plot(labels_test, labels_pred, color = 'blue')
plt.title('thoracic surgery')
plt.xlabel('data')
plt.ylabel('acc')
plt.show()
#find the probability
probability = reg.predict_proba(features_test)
print(probability)



#SVC
#visualisation for svc how many cancerous and not cancerous
from sklearn.svm import SVC
classifier = SVC(kernel = 'poly', random_state = 0)
classifier.fit(features_train, labels_train)
# Predicting the Test set results
labels_pred1 = classifier.predict(features_test)
# Making the Confusion Matrix
cm1 = confusion_matrix(labels_test, labels_pred1)
print(classification_report(labels_test,labels_pred1))  
print(accuracy_score(labels_test, labels_pred1))
# Model Score
score = classifier.score(features_test,labels_test)
plt.scatter(labels_test, labels_pred1, color = 'red')
plt.plot(labels_test, labels_pred1, color = 'blue')
plt.title('thoracic surgery')
plt.xlabel('data')
plt.ylabel('acc')
plt.show()
probability1 =classifier.predict_proba(features_test)




#RANDOM FOREST
from sklearn.ensemble import RandomForestClassifier
reg1 = RandomForestClassifier(n_estimators=20, random_state=0)  
reg1.fit(features_train, labels_train)  
labels_pred3 = reg1.predict(features_test)
#Evaluate the algo
print(confusion_matrix(labels_test,labels_pred3))  
print(classification_report(labels_test,labels_pred3))  
print(accuracy_score(labels_test, labels_pred3))




# Applying k-Fold Cross Validation
# Fitting Knn to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier1 = KNeighborsClassifier(n_neighbors =5, metric = 'minkowski', p =2)
classifier1.fit(features_train, labels_train)
# Predicting the Test set results
labels_pred4 = classifier1.predict(features_test)
# Making the Confusion Matrix
cm = confusion_matrix(labels_test, labels_pred)
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier1, X = features_train, y = labels_train, cv = 10)
print ("mean accuracy is",accuracies.mean())
print (accuracies.std())




#Naive Apporach
# Convert categorical variable to numeric
df["PRE7"]=np.where(df["PRE7"]=="F",0,1)
df["PRE8"]=np.where(df["PRE8"]=="F",0,1)
df["PRE9"]=np.where(df["PRE9"]=="F",0,1)
df["PRE10"]=np.where(df["PRE10"]=="F",0,1)
df["PRE11"]=np.where(df["PRE11"]=="F",0,1)
df["PRE17"]=np.where(df["PRE17"]=="F",0,1)
df["PRE19"]=np.where(df["PRE19"]=="F",0,1)
df["PRE25"]=np.where(df["PRE25"]=="F",0,1)
df["PRE30"]=np.where(df["PRE30"]=="F",0,1)
df["PRE32"]=np.where(df["PRE32"]=="F",0,1)
df["Risk1Yr"]=np.where(df["Risk1Yr"]=="F",0,1)
df["PRE6"]=np.where(df["PRE6"]=="PRZ0",0,
                                           np.where(df["PRE6"]=="PRZ1",1,2)
                                          )
df["PRE14"]=np.where(df["PRE14"]=="OC10",0,
                                           np.where(df["PRE14"]=="OC11",1,
                                           np.where(df["PRE14"]=="OC12",2,
                                           np.where(df["PRE14"]=="OC13",3,
                                           np.where(df["PRE14"]=="OC14",4,5
                                                    )   
                                         
                                            )
                                 )
                       )
            )

# Split dataset in training and test datasets
from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB
from sklearn.model_selection import train_test_split
features_train, features_test = train_test_split(df, test_size=0.5, random_state=0)
gnb = GaussianNB()
used_features =[

     "PRE5",
     "PRE6",
     "PRE8",
     "PRE10",
     "PRE11",
     "PRE14",
     "PRE19",
     "PRE25",
     "PRE30",
     "PRE32",
     "AGE"
   
]
# Train classifier
gnb.fit(
    features_train[used_features].values,
    features_train["AGE"].values
)
labels_pred4= gnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_gnb = confusion_matrix(features_test["AGE"], labels_pred4)

mnb = MultinomialNB()
used_features =[
         "PRE5",
         "PRE6",
         "PRE8",
         "PRE10",
         "PRE11",
         "PRE14",
         "PRE19",
         "PRE25",
         "PRE30",
         "PRE32",
        
]

# Train classifier
mnb.fit(
    features_train[used_features].values,
    features_train["AGE"].values
)
labels_pred5 = mnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_mnb = confusion_matrix(features_test["AGE"], labels_pred5)


bnb = BernoulliNB()
used_features =[

     "PRE5",
     "PRE6",
     "PRE8",
     "PRE10",
     "PRE11",
     "PRE14",
     "PRE19",
     "PRE25",
     "PRE30",
     "PRE32",
     
   
]

# Train classifier
bnb.fit(   
    features_train[used_features].values,
    features_train["AGE"]
)
labels_pred6 = bnb.predict(features_test[used_features])

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm_bnb = confusion_matrix(features_test["AGE"], labels_pred6)


 
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
skb=test = SelectKBest(score_func=chi2, k=4)
skbfit=skb.fit(features,labels)     
skbfit.scores_
best_features=(skbfit.transform(features))
print("Score",skbfit.scores_)

#summary of selected features
print(best_features[1:11])
my_features=[['PRE5','PRE6','PRE8','PRE10','PRE11','PRE14','PRE19','PRE25','PRE30','PRE32','AGE']]
mybestscore=list(skbfit.scores_)
for b,f in zip(mybestscore,my_features):
    print('"features":{}==>'.format(b))

#features importance
from sklearn.ensemble import ExtraTreesClassifier
modelextra=ExtraTreesClassifier()
modelextra.fit(features,labels)
print(modelextra.feature_importances_)
myimportant_features=list(modelextra.feature_importances_)
for mi, mf in zip(myimportant_features,my_features):
    print(f'"features":{mf}==>{mi*100}')



#find the all models score    
result=reg.score(features_test,labels_test)
print("Accuracy Logistic Regression",result*100)
result1=classifier.score(features_test,labels_test)
print("Accuracy of SVC ",result1*100)
result2=reg1.score(features_test,labels_test)
print("Accuracy of Random Forest",result2*100)
#result3=accuracies.score(features_test,labels_test)
#print("Accuracy of k-fold",result3*100) 



#visualization the data of all model and check that which gives us best result
def visualization():
    
    labels = ('Logistic Regression', 'SVC', 'RENDOM FOREST', 'k-fold')
    x_index = [0,1,2,3]
    performance=[76.60,85.53,87.23,82.51]
    plt.bar(x_index,performance)
    plt.xlabel('score', fontsize=15)
    plt.ylabel('data', fontsize=15)
    plt.xticks(x_index, labels, fontsize=10, rotation=45)
    plt.title('comparision')
    plt.show()
visualization()


#features_predict=np.array([2.85,2,1,1,0,4,0,1,0,1,62])
#prediction
def prediction():
    
    features_predict1=np.array([x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11])
    type(features_predict1)
    features_predict.shape
    new_features=features_predict1.reshape(1,-1)
    new_features.shape
    print(reg.predict(new_features))
    pre=print(classifier.predict(new_features))
    pre1=print(classifier1.predict(new_features))
    pre2=print(reg1.predict(new_features))
    
    if  (pre1==0):
        print("patient will die")
    else:
        print("patient will live ")
prediction()


import pickle
with open('df1_pickle','wb') as fp:
    model=pickle.dump(reg1,fp)
    

with open('df1_pickle','rb') as fp1:
    model1=pickle.load(fp1)
model1.predict(np.array([2.85,2,1,0,0,4,0,1,0,1,62]).reshape(1,-1)  ) 

from sklearn.externals import joblib
joblib.dump(reg,'df1_joblib')
clf=joblib.load('df1_joblib')
clf.predict(np.array([2.85,2,1,0,0,4,0,1,0,1,62]).reshape(1,-1)  ) 

"""
#sampling of the data
from imblearn.datasets import fetch_datasets
from sklearn.pipeline import make_pipeline
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss
from imblearn.metrics import classification_report_imbalanced
from sklearn.metrics import precision_score,accuracy_score,classification_report
from imblearn.pipeline import make_pipeline as make_pipeline_imb
       

#build model with SMOTE imblearn
smote_pipeline=make_pipeline_imb(SMOTE(random_state=0),classifier(random_state=0))
smote_model=smote_pipeline.fit(features_train,labels_train)
smote_prediction=smote_model.predict(features_test)



#build model with undersampling
nearmiss_pipeline=make_pipeline_imb(NearMiss(random_state=42),classifier(random_state=42))
nearmiss_model=nearmiss_pipeline.fit(features_train,labels_train)
nearmiss_prediction=nearmiss_model.predict(features_test)

#classification_report
print(classification_report(labels_test,prediction))
print(classification_report_imbalanced(labels_test,smote_prediction))

"""




