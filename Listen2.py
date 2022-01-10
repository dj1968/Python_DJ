# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 10:10:14 2022

@author: jdemt
"""

planets = ["Venus", "Mars", "Saturn", "Jupiter"]

last = planets.pop()
print(last)
print(planets)


planets2 = ["Venus", "Mars", "Saturn", "Jupiter"]
planets3 = ["Uranus", "Neptun"]

#print(planets2 + planets3)
sammel = planets2 + planets3
print(sammel)

sammel.remove("Uranus")
print(sammel)
