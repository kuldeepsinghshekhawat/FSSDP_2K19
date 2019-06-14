# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 08:50:01 2019

@author: lenovo
"""

new_list=["kuldeepsinghchirnana101@gmsil.com",
          "ghfhjklhgj@gmail.com",
          "kjhgfdsrtyuijhgcg@gmail.com",
         " ganagasinngh@gmail.com"]
old_list=["kuldeepsinghchirnana101@gmsil.com",
          "wetryhggfdjgfghhjgm@gmial.com",
         " ganagasinngh@gmail.com",
         "uytrduihb@gmail.com"]
email_list=list(set(new_list).difference(set(old_list)))
print(email_list)