# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:50:14 2022

@author: jdemt
"""

class A:
    a = 0
    def __eq__(self, other):
        return self.a == other.a
        

a = A()
b = A()


print (a == b)