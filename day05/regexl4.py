# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 08:52:47 2019

@author: lenovo
"""

#emails="kdbannachirana101@gmial.com jeenu@gmail.com ganga@gmail.com ".split()
import re
l1=[]
while (True):
    str_1=input("enter the digits")
    if not str_1:
        break
    else:
        l1.append(str_1)
for item in l1:
    result=re.findall(r'^[a-z0-9\-\_]+@[\w]\.[a-z](2,4)$',item)
    if result:
        print("valid card")
        print(item)
    else:
        print("invalid")
list_2=sorted(l1)
print(list_2)

#print sorted(emails,key=lembda L: map(int re.findall('(\d+)@'L)),L))