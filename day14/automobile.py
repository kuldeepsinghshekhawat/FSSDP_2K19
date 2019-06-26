# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:17:09 2019

@author: lenovo
"""
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
automobile=pd.read_csv("Automobile.csv")
s1=pd.DataFrame()
#read the csv file
s2 = automobile["make"].value_counts()
print(s2)
s2.index
s2.values.max()
s2.size
#automobile['make'].max()
car=['toyota', 'nissan', 'mazda', 'mitsubishi', 'honda', 'subaru',
       'volkswagen', 'peugot', 'volvo', 'dodge', 'mercedes-benz', 'bmw',
       'audi', 'plymouth', 'saab', 'porsche', 'isuzu', 'chevrolet',
       'alfa-romero', 'jaguar', 'renault', 'mercury']
slices=[32, 18, 17, 13, 13, 12, 12, 11, 11,  9,  8,  8,  7,  7,  6,  5,  4,
        3,  3,  3,  2,  1]
explode = (0.2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)  # explode 1st slice to 10% of the radius

plt.pie(slices,labels=car,explode=explode, autopct='%.0f%%')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
s1['toyota']=automobile['make'][automobile['make']=='toyota'].value_counts()
print(s1)
df=pd.DataFrame()
automobile["width"].between(10,20)
