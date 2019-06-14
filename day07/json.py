# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:26:13 2019

@author: lenovo
"""

city_name=input("enter the name of the city ")
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+city_name
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)
# requests.get(url,params={"q":"Jaipur", "appid"="e9185b28e9969fb7a300801eb026de9c"})
response.content

# Content in binary form
print (type(response.content))
jsondata = response.json()
print(jsondata)
jsondata["main"]["temp"]
jsondata["coord"]["lon"]
jsondata["wind"]["speed"]
jsondata["sys"]["sunrise"]
jsondata["timezone"]