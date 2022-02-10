# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:37:18 2022

@author: jdemt
"""

class Wurstmann:
    # klassenvariable
    zahl = 42
    string = "sffs"
    
    def __init__(self, buchneu="ziege"):
        # instanz variable
        self.willi = buchneu        
            
    def machet(self, otto):
        self.string = otto
        
        
fred = Wurstmann("werner")
print(fred.string)

#fred.machet("fred")
print(fred.string)
print(fred.willi)
print("---> " + fred.string)

xx = Wurstmann()
print(xx.willi)
print("---> " + xx.string)



