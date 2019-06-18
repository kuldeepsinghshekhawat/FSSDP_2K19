# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 11:19:28 2019

@author: lenovo
"""
import numpy as np #it is the numpy library
x = np.random.randint(5,16,40)#it is use for find the random number between 5-15
print (len(x),x)
from scipy import stats
print("Mode value is: ", stats.mode(x))
num = np.bincount(x).argmax()
print(num)