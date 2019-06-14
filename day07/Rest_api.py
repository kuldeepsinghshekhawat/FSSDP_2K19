
print ( post_method().text )# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:38:25 2019

@author: lenovo
"""

import json
import requests

Host = "http://13.127.155.43/api_v0.1/sending"

data = {"firstname":"kuldeep","language":"english","branch":"computer_enngineering"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response
print(post_method().text)
def get_method():
    response = requests.get("http://13.127.155.43/api_v0.1/get?firstname:"kuldeep","language"&"english","branch":"computer_enngineering"}
)
    return response

print (get_method().text)



