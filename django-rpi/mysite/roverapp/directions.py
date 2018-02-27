# -*- coding: utf-8 -*-

# RUNS ON AP

import socket
import sys

# Create a TCP/IP socket
server_name = '192.168.1.216' #sys.argv[1]
server_address = (server_name, 31417)

def sendToServer(message):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.connect(server_address)
    try:
        # Send message
        serverSocket.sendall(message)
        print >>sys.stderr, 'sending "%s"' % message
    finally:
        serverSocket.close()
        return
    
def forward():
    sendToServer('FORWARD')
    
def backward():
    sendToServer('BACKWARD')

    
def left():
    sendToServer('LEFT')
    
    
def right():
    sendToServer('RIGHT')
    
    
def idle():
    sendToServer('IDLE')
    
    
def up():
    sendToServer('UP')
    
    
def down():
    sendToServer('DOWN')
    
    
def off():
    sendToServer('OFF')

    