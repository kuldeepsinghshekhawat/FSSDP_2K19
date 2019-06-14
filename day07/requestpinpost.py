# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:27:27 2019

@author: lenovo
"""

import json
import requests

Host = "https://en32r42kj1io.x.pipedream.net/"

data = {"firstname":"kuldeep","language":"english"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print( post_method().text )
def get_method():
    response=requests.get(Host,data)
    return response
print(get_method().text)