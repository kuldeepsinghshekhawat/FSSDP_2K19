# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:30:17 2019

@author: lenovo
"""



import pandas as pd
import re
import os
files=[]
for j in os.listdir('C://Users//lenovo//Desktop//FSSDP_2K19//day14//sources'):
    if j.endswith(".txt"):
        files.append(j)
    else:
        pass
counter=1880
df=pd.DataFrame()
for var in files:
    with open(var) as fileobj:
        #df1=pd.DataFrame(columns = ['Name', 'Sex', 'Number','Year'])
        data=fileobj.readlines()
        df_mod=pd.DataFrame()
        df_mod[counter]=data
        df=pd.concat([df,df_mod],axis=1)
        if counter<2011:
            counter+=1
        else:
            break
    
#baby=df[(df['Sex']=='M') &(df['year']==1880)]
#print(baby)df1=pd.DataFrame(columns = ['Name', 'Sex', 'Number','Year'])
column=["Name","gender","number"]
for item in df:
    result=re.findall(r'\w*\w*\d*',item)
    if result:
        print(item)
        column.append(item)
    else:
       break
list_2=sorted()
print(list_2)