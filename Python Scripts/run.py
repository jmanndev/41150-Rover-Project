import logging
import sys
import time

import Rover
from Adafruit_BNO055 import BNO055


engine = Rover.Motor()#test
phil = Rover.Sensor()
engine.idle(2)

phil.readAll()
phil.displayData()