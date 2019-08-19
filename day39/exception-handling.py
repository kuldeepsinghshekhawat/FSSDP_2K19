# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:57:57 2019

@author: lenovo
"""

#exception handling=exception are error detected at the time of program execution




#it is simple program of divide 
x=input("Enter the 1st number ")
y=input("Enter the 2nd number")
z=int(y)/int(x)
print(z)



#program using exception  handling
x=input("Enter the 1st number ")
y=input("Enter the 2nd number")
try:
   z=int(y)/int(x)
except Exception as e:
    print("Excwptiojn as e",e)
    z=None
print("division is :",z)




try:
   z=int(y)/int(x)
except ZeroDivisionError as e:
    print("Excwptiojn as e",e)
    z=None
print("division is :",z)







try:
   z=int(y)/int(x)
except TypeError as e:
    print("Excwptiojn as e",e)
    z=None
print("division is :",z)






