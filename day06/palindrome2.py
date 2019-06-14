# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:20:02 2019

@author: lenovo
"""
n=input("Enter the number>").split()
list_1=[True if (i==i[::-1]) and (int(i)>0) else False for i in n]
print(all(list_1))
