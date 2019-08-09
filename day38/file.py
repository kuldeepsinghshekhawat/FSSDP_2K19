# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:29:21 2019

@author: lenovo
"""
#write =the file \
fp1=open("kd.txt","w")
fp1.write("Helo kuldeep my name is kuldeep singh shekhawatl,\n THis is my PC personal computer ,\nDon't worry about FAILURE you only have tobe right once")
fp1.close()




#Read the file system

fp2=open("kd.txt","r")
fp2.read()
#fp2.close()

for line in fp2:
    token=line.split(",")
    print(len(token))
fp2.close()