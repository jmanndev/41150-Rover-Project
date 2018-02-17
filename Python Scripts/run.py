import time
import Rover
import socket
import sys

RIGHT_MOTOR_GPIO = 18
LEFT_MOTOR_GPIO = 17
SERVER_IP = '192.168.1.216'

# Create a TCP/IP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

engine = Rover.Engine(RIGHT_MOTOR_GPIO, LEFT_MOTOR_GPIO)
phil = Rover.Sensor()
time.sleep(1)
engine.idle()
dataDict = {}


#   CLIENT STUFF
def setupServerConnection(ip):
    # Connect the socket to the port on the server given by the caller
    server_address = (ip, 31415)
    print >>sys.stderr, 'connecting to %s port %s' % server_address
    serverSocket.connect(server_address)
    return


def sendToServer(message):
    try:
        # Send message
        print >>sys.stderr, 'sending "%s"' % message
        serverSocket.sendall(message)

        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = serverSocket.recv(16)
            amount_received += len(data)
            print >>sys.stderr, 'received "%s"' % data

    finally:
        print >>sys.stderr, 'closing socket'
        serverSocket.close()
        return
    

def updateDataDict():
    # currrently appears not to update original dataDict.....
    phil.readAll()
    d = phil.getDataAsDict().copy()
    d.update(engine.getDataAsDict())
    dataDict = d.copy()
    return
    
    

#   ENGINE STUFF
def setDirection():
    #change code here to determine direction
    engine.forward()
    return
    
        

def run():
    print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
#    while True:
#        phil.readAll()
#        setDirection()
#        phil.Displ
#        time.sleep(1)
#        print('  ~~~~\t~~~~\t~~~~\t') #makes output pretty :)
    setupServerConnection(SERVER_IP)
    
    # this all doesnt work... cant figure out how to make DataDict a string that will send..........
    sendToServer("test")
    updateDataDict()
    sendToServer(str(dataDict))
    setDirection()
    updateDataDict()
    sendToServer(str(dataDict))
    sendToServer("endtest")
    
        

        
run()