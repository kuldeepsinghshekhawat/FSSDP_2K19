# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 12:12:36 2019

@author: lenovo
"""
acid="the quick brown fox jumps over the dog" 
#it is string
list1 = 'abcdefghijklmnopqrstuvwxyz'
#it is the total alphabet



for i in list1:
    if i not in acid:
        print('not panagram')
        break
    else: 
        print('panagram')
        break
    #break is use for only one time