# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:28:58 2019

@author: lenovo
"""

#if -else statement
age=int(input(" Enter your age:"))
if age>=18:
    print("you are capable for votting")
else:
    print("after {} year you are capable for votting".format(18-age))
    