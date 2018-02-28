# -*- coding: utf-8 -*-

# RUNS ON AP

import socket
import sys
import time

# Create a TCP/IP socket
server_name = '172.19.114.65' #sys.argv[1]
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
    time.sleep(1)
    return
    
def backward():
    sendToServer('BACKWARD')
    time.sleep(1)
    return

    
def left():
    sendToServer('LEFT')
    return
    
    
def right():
    sendToServer('RIGHT')
    return
    
    
def idle():
    sendToServer('IDLE')
    return
    
    
def up():
    sendToServer('UP')
    return
    
    
def down():
    sendToServer('DOWN')
    return
    
    
def off():
    sendToServer('OFF')
    return

    