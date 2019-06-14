# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:02:29 2019

@author: lenovo
"""

inc=input("Enter the bricks")
inc1=input("Enter the bricks")
inc2=input("Enter the bricks")
if int(inc2)%5>int(inc1):
    print(False)
else:
    red = 5*int(inc2)+1*int(inc1)
    if red>int(inc):
        print(True)
    else:
        print(False)