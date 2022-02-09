# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:22:26 2022

@author: jdemt
"""

class Katze():
    pfoten = 4
        
class Vogel():
    fluegel = 2
        
class KatzenVogel(Katze, Vogel):
    name = "rattattta"
    
    
cat = Katze()
print(cat.pfoten)

bird = Vogel()
print(bird.fluegel)

kv = KatzenVogel()
print(kv.name)
print(kv.fluegel)
print(kv.pfoten)