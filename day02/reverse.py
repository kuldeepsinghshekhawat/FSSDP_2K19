# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:10:08 2019

@author: lenovo
"""

def reverse_fun(greeting):
    return 'welcome {}'.format(greeting)
greeting="I am kuldeep"
print(reverse_fun(greeting))
greeting[::-1]