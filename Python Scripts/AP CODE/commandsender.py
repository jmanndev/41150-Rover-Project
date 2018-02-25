# -*- coding: utf-8 -*-

import socket
import sys
import time

# Create a TCP/IP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = sys.argv[1]
server_address = (server_name, 31417)

def sendToServer(message):
    try:
        # Send message
        print >>sys.stderr, 'sending "%s"' % message
        serverSocket.sendall(message)
    finally:
        return
    

def doCommands():
    ### listen for commands from xbox here
    
    
def run():
    serverSocket.connect(server_address)
    doCommands()
    serverSocket.close()


run()