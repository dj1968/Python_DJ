# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:40:04 2022

@author: jdemt
"""

import json
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
param = dict()

resp = requests.get(url=url,params=param)
data = resp.json()

print(json.dumps(data, indent = 4))
