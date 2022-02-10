# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:40:15 2022

@author: jdemt
"""
from functools import partial

def multiplik(x, y):
    return x * y

mal2 = partial(multiplik, 2)

print (mal2(5))

# einsatz bei listen

