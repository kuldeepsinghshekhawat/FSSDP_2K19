# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 10:18:12 2019

@author: lenovo
"""

dict_1 = {} 
#it define the dictionary
with open('passwd') as fp:
    # it open the file
    for line in fp:
        if not line.startswith("#"):
    #it checks the condition 
            user_info = line.split(":")
            #it split the liines
            dict_1[user_info[0]] = user_info[2]
 
for username in sorted(dict_1):#it checks the sorted list of name in  the file
    print("{}:{}".format(username, dict_1[username]))

