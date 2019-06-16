# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:14:55 2019

@author: lenovo
"""

with open("absentee.txt","rt") as fp1:
    #open file with read mode
    print(fp1.name)
    lines=fp1.read().split()
    #the lines is define that it read the ono by one line in file
    last_line=lines[-1]
    #it is useed for only last line
    print(last_line)
    
    