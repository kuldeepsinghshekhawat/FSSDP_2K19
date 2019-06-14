# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:20:38 2019

@author: lenovo
"""

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])

print(mylist)

def addition():
    number1 = input("First number: ") 
    number2 = input("\nSecond number: ") 
  
# Adding two numbers 
# User might also enter float numbers 
sum = float(number1) + float(number2) 
  
# Display the sum 
# will print value in float 
print("The sum of {0} and {1} is {2}" .format(number1, number2, sum)) 
number1=int(input("Enter the 1st no"))
number2=int(input("Enter the 2st no"))
number3=int(input("Enter the 3st no"))
def largest():
    if(number1>number2) and (number1>number3):
        print("number1 is the greatest")
    elif (number2>number1) and (number2>number3):
        print("number2 is greatest")
    else:
        print("number3 is greatest")
    
print(largest())
            
def smallest():
    
    if(number1<number2) and (number1<number3):
        print("number1 is the smallest")
    elif (number2<number1) and (number2<number3):
        print("number2 is smallest")
    else:
        print("number3 is smallest")
print(smallest())     
   
        

