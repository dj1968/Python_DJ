# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:44:43 2022

@author: jdemt
"""

class TestEx(Exception):
    pass  # vollständige klasse
    
    
def abc(a):
    if a == 2:
        raise TestEx()
    else:
        print("111")

try:
    abc(3)
    abc(2)    
    print("222")
except TestEx as detail:
    print(detail)
    print("klatsch")    
except Exception:
    print("fetter klatsch")
    
else:
    print("nothing ex")
    
