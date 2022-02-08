# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:41:48 2022

@author: jdemt
"""

import time
import datetime

#print(time.time())
start = time.time()
time.sleep(2)
end = time.time()
#print (end - start)

# ---------------------

print(datetime.datetime.now().strftime("%a %b %H:%M:%S %d.%m.%Y"))
