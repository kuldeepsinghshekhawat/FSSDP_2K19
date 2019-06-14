# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:34:03 2019

@author: lenovo
"""
student_list=[]
while True:
    str_1=input("Enter the detail of student like name age and score")
    if not str_1:
        break
name, age, score = str_1.split(",")
student_list.append((name, int(age), int(score)))
print(student_list.sort())
