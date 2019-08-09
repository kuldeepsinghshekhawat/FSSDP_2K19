# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:03:43 2019

@author: lenovo
"""

#you are given two list of numbers and you need to find total of each of the list
#this is the function tpic

total1=[2100,3400,3500]
total2=[3499,3288,5443]
def calculate(exp):
    total=0
    for item in exp:
        total=total+item
    return total
calculate(total1)
calculate(total2)

