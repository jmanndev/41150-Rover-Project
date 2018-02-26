# -*- coding: utf-8 -*-

# RUNS ON AP

import socket
import sys

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
    
def run():
    serverSocket.connect(server_address)
    sendToServer('DOWN')
    serverSocket.close()

run()

