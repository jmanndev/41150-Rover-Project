# -*- coding: utf-8 -*-

import socket
import sys
import json

#   RUNS ON AP

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 31415)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)


    
def saveData():
    print('saving data')
    
    
try:
    while True:
        # Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        connection, client_address = sock.accept()
        newData = ''
        
        while True:
            data = connection.recv(50)
            
            if data:
                newData += data
                if data.endswith('☢'):
                    newData = newData.strip('☢')
                    print("received data:" + newData)
                    newData = ''
            else:
                break
finally:
    connection.close

    