# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:07:18 2019

@author: lenovo
"""
import re
l1=[]

while (True):
    str_1=input("enter the digits")
    if not str_1:
        break
    else:
        l1.append(str_1)
for item in l1:
    result=re.findall(r'[456]([0-9]{15}|\d{3}\-(\d{4}\-){2}\d{4})',item)
    result_1=re.search(r'(\d)\1{3,}',item.replace("-",""))
    if result and not result_1:
        print("valid card")
        print(item)
    else:
        print("invalid")
            
    