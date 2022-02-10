# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:21:18 2022

@author: jdemt
"""

import threading
import time


class myFred(threading.Thread):
    def __init__(self, iD, name):
        threading.Thread.__init__(self)
        self.iD = iD
        self.name = name
        
    def run(self):
        if self.iD == 1:
            lockMe.acquire()
        print("-start ", self.iD)
        
        if self.iD == 2:
            lockMe2.acquire()
        
        time.sleep(self.iD * 3)
        print("-end ", self.iD)
        lockMe.release()
       # lockMe2.release()


lockMe = threading.Lock()
lockMe2 = threading.Lock()

t1 = myFred(1, "t1")
t2 = myFred(2, "t2")

t1.start()
t2.start()


if t1.isAlive():
    time.sleep(3)
#t1.join()
t2.join()

print ("-main fred ende")




