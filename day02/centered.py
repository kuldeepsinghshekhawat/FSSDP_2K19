# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 21:55:48 2019

@author: lenovo
"""
def centered_average(nums):
    x=0
    for i in range(nums):
        x = i + 0
        y = x + 1
        if y%2 == 0:
            return (nums[y/2] + nums[(y/2)+1]) / 2
        else:
            return nums[y/2]
centered_average(2)