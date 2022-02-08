# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:12:42 2022

@author: jdemt
"""

#api coin desk com

import json

with open('d:\\tmp\\login.json') as file:
    data = json.load(file)

print(json.dumps(data, indent=4))


data["LoginMailadresseReq"]["benutzerkng"] = "anonimized"


with open('d:\\tmp\\login_ano.json', 'w') as fout:
    fout.write(json.dumps(data, indent = 4))


