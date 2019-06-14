# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 23:01:38 2019

@author: lenovo
"""

with open('absentee.txt','rt') as fp1:
    dict_1={}
    sent = fp1.read().split()
    print (sent )
    for words in sent:
        print(words)
        if words in dict_1:
            dict_1[words]+= 1 
        else:
           dict_1[words]=1

print(dict_1)


for words in sent:
    for alphabet in words:
        if alphabet in dict_1:
            dict_1[alphabet]+= 1
    else:
        dict_1[alphabet]= 1

#print("number of lines in file ",file_len("absentee.txt"))
count=0
for line in open("absentee.txt").readlines():
    count+= 1
    print(count)

print('unique word')
print(len(set(sent)))