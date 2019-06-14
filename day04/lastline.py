# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:14:55 2019

@author: lenovo
"""

with open("absentee.txt","rt") as fp1:
    print(fp1.name)
    lines=fp1.read().split()
    last_line=lines[-1]
    print(last_line)
    
    