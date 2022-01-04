# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 12:19:52 2022

@author: jdemt
"""

import random

satz = []

part1 = ["schalke","bochum","bvb","muffstadt"]
part2 = ["kölle","waldorf","poppencity","ickern"]
part3 = ["1","3","0","4"]
part4 = ["1","2","5","7"]

vollbier = [part1, part2, part3, part4]

for part in vollbier:
    r = random.randint(0, len(part)- 1)
    satz.append(part[r])
    
print(" ".join(satz))

