# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:45:04 2022

@author: jdemt
"""

# nutzung in listen
f = lambda x : x * 2
    
# alternativ als function
#def f2(x, y):    return x * y

list1 = [4,2,5,6]

list2 = list(map(f, list1))

print (list2[0])