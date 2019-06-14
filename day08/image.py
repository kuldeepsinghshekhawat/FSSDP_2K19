# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 19:47:56 2019

@author: lenovo
"""

from PIL import Image
import requests
from io import BytesIO
import requests

url = "http://facebook.in/images/kppppp_jpg_bw.jpg"
response = requests.get(url)
with open("kppppp.jpg","wb") as f:
    f.write(response.content)
