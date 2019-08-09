# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 12:42:33 2019

@author: lenovo
"""

#json=java script object notation
"""
The full-form of JSON is JavaScript Object Notation. 
It means that a script (executable) file which is made of text in a programming language, is used to
 store and transfer the data. Python supports JSON through a built-in package called json. 
 To use this feature, we import the json package in Python script. 
 The text in JSON is done through quoted string which contains value in key-value mapping within { }. 
 It is similar to the dictionary in Python. JSON shows an API similar to users of Standard Library
 marshal and pickle modules and Python natively supports JSON features
 """
 
import json
a={"Name":"Kuldeep singh shekhawat","Branch":"Computer Science","college":"Sobhasaria Engineering College ",
    "ph":"7742775759","Address":"Chirana,Jhunjhnu" }
b=json.dumps(a)
print(b)
c=json.loads()
