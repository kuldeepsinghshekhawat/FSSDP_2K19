# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 18:07:41 2019

@author: kuldeep shekhawat
"""
"""function in python 
function are 4 type
1. no argument and no returntype
2. no argument but return type
3. with argument but no return type 
4. with argument and return type
"""
#1. no argument and no returntype
def fun1():
    var1=int(input("Enter the first number:"))
    var2=int(input("Enter the second number:"))
    
    print("var3=",var1 + var2)



#2. no argument but return type
def fun2():
    var1=int(input("Enter the first number:"))
    var2=int(input("Enter the second number:"))
    return var1*var2



#3. with argument but no return type 
def fun3(var1,var2):
    var3=var1/var2
    print("div=",var3)
fun3(24,3)


#4. with argument and return type
def fun4(var1,var2):
    var3=var1*var2
    return var3
fun4(2,6)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    