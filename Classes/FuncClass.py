# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:44:28 2022

@author: jdemt
"""

class A:
    a = 0
    def __call__(self, x) :
        print(self.a + x)
        
a = A()

a(4)
