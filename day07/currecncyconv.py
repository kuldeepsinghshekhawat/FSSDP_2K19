
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:02:05 2019

@author: lenovo
"""
import requests
import json
url1 = "https://free.currconv.com/api/v7/convert"
url2 = "?q=USD_INR"
url3 = "&compact=ultra&apiKey=f352c70776b5c618b0e6"
    
url = url1 + url2 + url3
print (url)
response = requests.get(url)
data=response.text
parsed=json.loads(data)
print(json.dumps(parsed))
jsondata = response.json()
print(jsondata)