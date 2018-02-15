import time

import Rover


engine = Rover.Motor()#test
phil = Rover.Sensor()

while True:
    phil.readAll()
    phil.displayData()
    time.sleep(2)