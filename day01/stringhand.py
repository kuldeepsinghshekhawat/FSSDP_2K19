# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:30:01 2019

@author: lenovo
"""
#def palindrome_number(list_a):
 #   c=0
n=input("Enter the number").split(" ")
#these are the t
for i in n:
    if i == i[::-1]:
        print(i)
t=n
rev=0
#this is define the rewverse
rem = i % 10
#it used as the remainder
rev=rev*10+rem
#it is find the reverse number
i=i/10
#if rev==n
if rev == i:
    print("number is palindrome")
else:
    print("number is not palindrome")