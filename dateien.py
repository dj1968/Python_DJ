# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 12:45:55 2022

@author: jdemt
"""

file = open("d:\Python\djfile.csv", "r")
for line in file:
    print(line.strip())
file.close()    


file2 = open("d:\Python\schreiben.txt", "w")
file2.write("adasdsaa\n")
file2.write("adasdsaa333")
file2.close()