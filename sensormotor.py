import logging
import sys
import time

import motor
from Adafruit_BNO055 import BNO055


engine = motor.Motor()#test
engine.idle(2)

# Raspberry Pi configuration with serial USB and RST connected to GPIO 18:
bno = BNO055.BNO055(serial_port='/dev/ttyUSB0', rst=18) # apparently rst value is not needed


# Initialize the BNO055 and stop if something went wrong.
if not bno.begin():
    raise RuntimeError('Failed to initialize BNO055! Is the sensor connected?')

# Print system status and self test result.
status, self_test, error = bno.get_system_status()
print('System status: {0}'.format(status))
print('Self test result (0x0F is normal): 0x{0:02X}'.format(self_test))
# Print out an error if system status is in error mode.
if status == 0x01:
    print('System error: {0}'.format(error))
    print('See datasheet section 4.3.59 for the meaning.')

print('Reading BNO055 data, press Ctrl-C to quit...')

    
heading = ""
roll = ""
pitch = ""
sys = ""
gyro = ""
accel = ""
mag = ""
temp_c = ""

# Sensor gyro is Frank
def readPhil():
    
    
def displayPhilData():
    print('Heading={0:0.2F} Roll={1:0.2F} Pitch={2:0.2F}\tSys_cal={3} Gyro_cal={4} Accel_cal={5} Mag_cal={6}'.format(
        heading, roll, pitch, sys, gyro, accel, mag))
