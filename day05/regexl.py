# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:13:17 2019

@author: lenovo
"""


import re
str_1=input("Enter the float number").split()
result = re.match(r'[+-.]?\d{1}\.\d{1,}',str_1[-1])
if result:
    print ("true")
else:
    print ("false")