#!/usr/bin/env pythona3
# -*- coding: utf-8 -*-

import socket


target_host = "49.212.185.25"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))
client.send(b"GET / \r/ Host/1.1\r\n\r\n")
response = client.recv(2048)
print (response)


