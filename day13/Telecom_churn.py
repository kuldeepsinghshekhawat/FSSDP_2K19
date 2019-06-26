# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:16:31 2019

@author: lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt
telecom=pd.read_csv("Telecom_churn.csv")
s3=pd.DataFrame()
s4=pd.DataFrame()
s5=pd.DataFrame()
s1=pd.DataFrame()
s6=pd.DataFrame()
churn=telecom.groupby(['international plan','voice mail plan'])
churn.size()
s3['yes']=telecom['international plan'][telecom['voice mail plan']=='yes'].value_counts()
print(s3)
s4[False]=telecom['international plan'][telecom['churn']==False].value_counts()

print(s4)
s5[True]=telecom['international plan'][telecom['churn']==True].value_counts()

print(s5)
s1['yes']=telecom['voice mail plan'][telecom['international plan']=='yes'].value_counts()
print(s1)
sur_vile=telecom.groupby(['state', 'total night minutes'])
sur_vile.size()
s6[True]=telecom['state'][telecom['churn']==True].value_counts()
print(s6)
churn=telecom[telecom['churn']==True]['total intl charge'].sum()
print(churn)
nonchurn=telecom[telecom['churn']==False]['total intl charge'].sum()
print(nonchurn)
churn1=telecom[telecom['churn']==True]['total night minutes'].max()
print(churn1)
nonchurn1=telecom[telecom['churn']==False]['total night minutes'].sum()
print(nonchurn1)
state=telecom['state'][telecom['total night minutes']==354.9]
print(state)
label=['total day calls','total eve calls','total night calls','total intl calls','customer service calls']
slices=[48945,48571,48493,2011,1077]
churn2=telecom[telecom['churn']==True]['total day calls'].sum()
print(churn2)
churn3=telecom[telecom['churn']==True]['total night calls'].sum()
print(churn3)
churn4=telecom[telecom['churn']==True]['total eve calls'].sum()
print(churn4)
churn5=telecom[telecom['churn']==True]['total intl calls'].sum()
print(churn5)
churn6=telecom[telecom['churn']==True]['customer service calls'].sum()
print(churn6)
plt.pie(slices,labels=label,autopct='%0f%%')
plt.axis('equal')
plt.show()

churn8=telecom['account length'][telecom['churn']==True].max()
print(churn8)

churn9=telecom[telecom['churn']==True]['total day charge'].describe()
print(churn9)
churn_3=telecom[telecom['churn']==True]['total night charge'].describe()
print(churn_3)
churn_4=telecom[telecom['churn']==True]['total eve charge'].describe()
print(churn_4)
churn_5=telecom[telecom['churn']==True]['total intl charge'].describe()
print(churn_5)
df=pd.DataFrame()
churn6=telecom[telecom['churn']==True]['customer service calls'].value_counts()
print(churn6)
area_code=telecom[telecom['international plan']=='yes']['area code'].value_counts()
print(area_code)

