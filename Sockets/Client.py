# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 06:19:47 2022

@author: jdemt
"""

import socket


# TCP SOCK STREAM
# UDP DGRAM
client_socket = socket.socket(socket.AF_INET, 
                              socket.SOCK_STREAM)

server_adresse = ('127.0.0.1', 1904)
client_socket.connect(server_adresse)
client_socket.send(bytes("huba", "utf8"))




