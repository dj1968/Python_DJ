# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:27:33 2022

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
    
    def __init__(self):
        Lebewesen.__init__(self)
    
    def machwatt(self, neuebeine):
        self.beine = neuebeine

    def machwatt2(self, neueaugen):
        self.augen = neueaugen

flutschi = Hund()
print(flutschi.augen)

flutschi.machwatt(33)
print(flutschi.beine)

flutschi.machwatt2(3333)
print(flutschi.augen)

print(flutschi.klasse)

flutschi.itchi()