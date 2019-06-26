# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 12:37:48 2019

@author: lenovo
"""

total = 0
user_input=input("Enter the number")
for index in range( len( user_input ) ):
    # checks if current number or previous number is 13
    if (user_input[index] == 13 or user_input[index-1] == 13):
        continue
    else:
        total += 1

print (total)