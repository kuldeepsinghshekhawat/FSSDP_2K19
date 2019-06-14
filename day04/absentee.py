# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:43:30 2019

@author: lenovo
"""
with open("absentee.txt","wt") as fp1:
    while(True):
        fp11=input("Enter the name >")
        fp1.write(fp11 +'\n')
        if not fp11:
            break

    