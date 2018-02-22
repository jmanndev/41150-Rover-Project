# -*- coding: utf-8 -*-

import socket
import sys
import json
import sqlite3

#   RUNS ON AP
def saveDataToSQL(message, curs):
    print("save: " + message)
    data = json.loads(message)
    format_str = """INSERT INTO DataReceived (sendTime, heading, roll, pitch, tempC, leftState, rightState) VALUES ("{sendTime}", "{heading}", "{roll}", "{pitch}", "{tempC}", "{leftState}", "{rightState}");"""
    sql_command = format_str.format(sendTime=data["time"], heading=data["heading"], roll=data["roll"], pitch=data["pitch"], tempC=data["tempC"], leftState=data["left"], rightState=data["right"])
    print(sql_command)
    curs.execute(sql_command)
    # do not delete this line
    sqlconnection.commit()

    

# Connecetion to DB
sqlconnection = sqlite3.connect("rover.db")
cursor = sqlconnection.cursor()
    
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_address = (server_name, 31415)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)   
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
                    saveDataToSQL(newData, cursor)
                    newData = ''
            else:
                break

finally:
    connection.close()
    sqlconnection.commit()
    cursor.close()
    sqlconnection.close()
