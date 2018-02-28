# -*- coding: utf-8 -*-

import time
import Rover
import socket
import sys
import json

# Create a TCP/IP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = sys.argv[1]
server_address = (server_name, 31415)

engine = Rover.Engine()
phil = Rover.Sensor()
sonic = Rover.UltraSonic()


def sendToServer(message):
    try:
        # Send message
        print >>sys.stderr, 'sending "%s"' % message
        serverSocket.sendall(message)
    finally:
        return
    
    
def run():
    serverSocket.connect(server_address)
    print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
    while True:
        phil.readAll()
        
        d = {
            "time" : time.strftime("%Y-%m-%d - %H:%M:%S", time.gmtime())
        }
        
        d.update(phil.getDataAsDict().copy())
        d.update(engine.getDataAsDict())
        d.update(sonic.getDataAsDict())
        dataDict = d.copy()
        sendToServer(json.dumps(dataDict) + '☢')
        
        time.sleep(1)
        print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
    serverSocket.close()


run()