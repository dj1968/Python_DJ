# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:14:56 2022

@author: jdemt
"""

import logging

logging.basicConfig(filename="d:\\tmp\pyth.log", level=logging.INFO)

def f():
    logger = logging.getLogger("f-willbur")
    logger.setLevel(logging.DEBUG)
    
    fileh = logging.FileHandler("d:\\tmp\\logme.log")
    form = logging.Formatter('%(name)s :  %(levelname)s : %(asctime)s : %(message)s') 
    
    fileh.setFormatter(form)
    logger.addHandler(fileh)
    
    logger.debug("ffff called")
    
    print ("wemser")

#logging.debug("snoop loggi log")
#logging.info("info mann und sein kind")

f()