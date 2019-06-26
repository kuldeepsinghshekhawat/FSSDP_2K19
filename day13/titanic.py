# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 10:55:22 2019

@author: lenovo
"""
import pandas as pd
titanic=pd.read_csv("training_titanic.csv")  
#sub for survived people
sub=titanic['Survived'][(titanic['Survived']==1)].value_counts()
print("survive the disaster",sub)
#sub1 for die people
sub1=titanic['Survived'][(titanic['Survived']==0)].value_counts()
print("died",sub1)
#sur_vile ise for checks that how many female and male are died and survived
sur_vile=titanic.groupby(['Sex', 'Survived'])
sur_vile.size()
s1=pd.DataFrame()
s2=pd.DataFrame()
s3=pd.DataFrame()
s4=pd.DataFrame()
s1['male']=titanic['Survived'][titanic['Sex']=='male'].value_counts(normalize = True)
print(s1)
s2['female']=titanic['Survived'][titanic['Sex']=='female'].value_counts(normalize = True)
print(s2)
sub2=titanic['Age'][(titanic['Age']<=18)].value_counts()
print(sub2)
sub3=titanic['Age'][(titanic['Age']>=18)].value_counts()
print(sub3)
s3['male']=titanic['Age'][titanic['Sex']=='male'].value_counts(normalize = True)
print(s3)
s4['female']=titanic['Age'][titanic['Sex']=='female'].value_counts(normalize = True)
print(s4)
