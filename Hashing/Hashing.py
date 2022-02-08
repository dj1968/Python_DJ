# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:25:20 2022

@author: jdemt
"""

import hashlib
import hmac

h = hmac.new(b'sdidsof', b'', hashlib.sha3_512) 
h.update(b"ASDF1234")
print(h.digest())




