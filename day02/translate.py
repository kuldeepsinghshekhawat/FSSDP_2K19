# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:13:47 2019

@author: lenovo
"""

def translate (string_1):
    var1 = ''
    consonent = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','T','v','w','x','z']
    string_1 ="This is fun"
    for var  in string_1:
        if (var in consonent):
          var1 = var1+var + 'o' + var
          print(var1)
        else:
            var1=var1+var

string_1 = input("Enter a string")
print(translate(string_1))