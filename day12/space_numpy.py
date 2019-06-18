# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:33:17 2019

@author: lenovo
"""
import numpy as np
a=input("enter the number").split()
a=[int(i) for i in a]
x=np.array(a)
print(type(x))
x=x.reshape(3,3)
print(x)

