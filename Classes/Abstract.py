# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:22:18 2022

@author: jdemt
"""

from abc import ABCMeta, abstractmethod

class Tier:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def laufen(self):
        pass
    
    
class Katze(Tier):
    def laufen(self):
        print("katze rennt")
    