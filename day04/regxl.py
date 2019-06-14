# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:55:10 2019

@author: lenovo
"""
import re
str_1=input("Enter the float number").split()
result = re.match(r'\+ \- \. \d {1}',str_1[0])
if result:
    print ("true")
else:
    print ("false")
