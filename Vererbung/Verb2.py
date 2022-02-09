# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:04:22 2022

@author: jdemt
"""


class Lebewesen:
    augen = 3
    def __init__(self):
        self.klasse = "saueger"
        
    def itchi(self):
        print("wemser")

class Hund(Lebewesen):
    beine = 4
    name = "Rudi"
    augen = 2
    
    def __init__(self):
        Lebewesen.__init__(self)
    
    def machwatt(self, neuebeine):
        self.beine = neuebeine

    def machwatt2(self, neueaugen):
        self.augen = neueaugen
    
    def itchi(self):
        print("itchi wemser")
        
wuff = Hund()
wuff.itchi()
print(wuff.augen)


lubbi = Lebewesen()
lubbi.itchi()
print(lubbi.augen)