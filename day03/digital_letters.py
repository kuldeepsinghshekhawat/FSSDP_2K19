# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:28:51 2019

@author: lenovo
"""
from collections import OrderedDict 
#it is the library of ordered dict 
user_input = input("Enter string : ")

# initialising the counter for letter and digit
dict1 = OrderedDict() 
dict1["Digits"] = 0
dict1["Letters"] = 0


#for loop define the how many letter and digit
for character in user_input:    
    if character.isalpha():    # conditionto check for Letter.
        # if found increase counter variable by 1.
        dict1["Letters"] = dict1["Letters"] + 1 
    elif character.isdigit():      # conditiion to check for digit.
        # if found increase counter variable by 1.          
        dict1["Digits"] = dict1["Digits"] + 1 
print(dict1)           
for key, value in dict1.items() :
  print ( key, value )