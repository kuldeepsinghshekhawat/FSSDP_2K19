# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:20:22 2019

@author: lenovo
"""
with open('romeo(1).txt','rt') as fp1:
    dict_1={}
    line = fp1.read().split()
    print (line )
    for words in line:
        print(words)
        if words in dict_1:
            dict_1[words]+= 1 
        else:
           dict_1[words]=1
print(dict_1)
                