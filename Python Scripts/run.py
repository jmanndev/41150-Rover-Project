# -*- coding: utf-8 -*-

import time
import Rover
import socket
import sys
import json

RIGHT_MOTOR_GPIO = 18
LEFT_MOTOR_GPIO = 17
SERVER_IP = '172.19.17.150'

# Create a TCP/IP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_IP, 31415)

engine = Rover.Engine(RIGHT_MOTOR_GPIO, LEFT_MOTOR_GPIO)
phil = Rover.Sensor()
time.sleep(1)
engine.idle()


def sendToServer(message):
    try:
        # Send message
        print >>sys.stderr, 'sending "%s"' % message
        serverSocket.sendall(message)
    finally:
        return
    

#   ENGINE STUFF
def setDirection():
    #change code here to determine direction
    engine.forward()
    return
    
    
def run():
    serverSocket.connect(server_address)
    print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
    while True:
        phil.readAll()
        
        d = {
            "time" : time.strftime("%H:%M:%S - %Y-%m-%d", time.gmtime())
        }
        d.update(phil.getDataAsDict().copy())
        d.update(engine.getDataAsDict())
        dataDict = d.copy()
        sendToServer(json.dumps(dataDict) + '☢')
        
        time.sleep(1)
        print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
    serverSocket.close()


run()