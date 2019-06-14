# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:14:15 2019

@author: lenovo
"""
import re
l1=[]

while (True):
    str_1=input("enter the emailaddress")
    if not str_1:
        break
    else:
        l1.append(str_1)
for item  in l1:
     result=re.findall(r'([a-z0-9\_\-]+\@\w+\.[a-z{2,}])',item)
     if result:
         print("valid id")
         print(item)
     else:
         print("no")