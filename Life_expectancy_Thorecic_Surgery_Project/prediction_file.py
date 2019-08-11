# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 17:43:17 2019

@author: HP
"""
import numpy as np
import pickle

def prediction(user_data):
    
    data = np.array([user_data])
    
    with open("static/models/trained_model.pkl","rb") as f:
        models = pickle.load(f)
    
    data = models["scaling"].transform(data)
    pre1 = models["Random_Forest"].predict(data)
    
    if  (pre1==0):
        return "Patient will die"
    else:
        return "Patient will live "

