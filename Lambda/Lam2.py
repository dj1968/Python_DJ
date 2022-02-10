# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:08:12 2022

@author: jdemt
"""
# filter
f = lambda x : x%2 == 0
  
list1 = [4,2,5,6,6,7,8,9,11,34]
list2 = list(filter(f, list1))

print (list2)

