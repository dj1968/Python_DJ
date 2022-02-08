# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:33:38 2022

@author: jdemt
"""

class A:
    a = "0"
    #def __ge__(self, other):
    #    return self.a >= other.a
    
    #def __int__(self):
    #    return self.a
    
    def __str__(self):
        return self.a + "magic"
    
#a = A()
#print (int(a) + 5)

b = A()

print(str(b))
    